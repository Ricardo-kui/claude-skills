#!/usr/bin/env python3
"""Shared feedback registry engine for the write-* skills.

Parameterized by a per-skill ``SkillConfig``. Implements:

- fingerprint dedup (sha256 over scope + project + section + scope discriminator
  + category + normalized rule, namespaced by a per-skill id prefix);
- supersedes / benchmark / prohibited_patterns merge-on-upsert;
- registry read/write with a schema-layer migration (1.0.0 -> 1.1.0 in-memory,
  never rewriting the on-disk data file).

Canonical record shape is 1.1.0 (see ``schema.json`` in this directory).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class SkillConfig:
    """Per-skill wiring for the shared engine."""

    skill_name: str
    id_prefix: str                          # e.g. "wrf_", "wmf_", "wif_"
    registry_default: Path
    valid_categories: frozenset = field(default_factory=frozenset)
    canonical_schema_version: str = "1.1.0"
    scope_field: str = "estimator"          # canonical 4th scope discriminator
    scope_cli_flag: str | None = "--estimator"
    scope_cli_dest: str = "estimator"
    valid_scopes: frozenset = field(
        default_factory=lambda: frozenset({"skill", "project", "section", "estimator"})
    )
    valid_severities: frozenset = field(
        default_factory=lambda: frozenset({"revise", "reject"})
    )
    valid_statuses: frozenset = field(
        default_factory=lambda: frozenset({"active", "retired"})
    )
    # Legacy on-disk shape (only write-methods still writes 1.0.0 on disk).
    legacy_disk_schema_version: str | None = None
    legacy_scope_field: str | None = None
    # Language-lint wiring (consumed by lint_language.py).
    end_heading: str = r"^##\s+生成后自检记录"
    standalone_patterns_path: Path | None = None


def normalize(value: str | None) -> str:
    """Normalize user-entered text for stable matching."""
    return re.sub(r"\s+", " ", (value or "").strip())


def normalize_list(raw: Any, field: str, *, collapse_whitespace: bool = True) -> list[str]:
    """Normalize optional string lists while preserving insertion order."""
    if raw is None:
        return []
    if not isinstance(raw, list):
        raise ValueError(f"{field} must be a list of strings")
    normalized: list[str] = []
    seen: set[str] = set()
    for value in raw:
        if not isinstance(value, str):
            raise ValueError(f"{field} must contain only strings")
        item = normalize(value) if collapse_whitespace else value.strip()
        if item and item not in seen:
            normalized.append(item)
            seen.add(item)
    return normalized


def _scope_discriminator(raw: dict[str, Any], config: SkillConfig) -> str:
    """Read the 4th scope slot, accepting both canonical and legacy field names."""
    if config.scope_field in raw:
        return normalize(raw.get(config.scope_field))
    if config.legacy_scope_field and config.legacy_scope_field in raw:
        return normalize(raw.get(config.legacy_scope_field))
    return ""


def fingerprint(record: dict[str, Any], config: SkillConfig) -> str:
    fields = (
        record["scope"],
        record.get("project", ""),
        record.get("section", ""),
        record.get(config.scope_field, ""),
        record["category"],
        record["rule"].casefold(),
    )
    digest = hashlib.sha256("\x1f".join(fields).encode("utf-8")).hexdigest()[:16]
    return f"{config.id_prefix}{digest}"


def migrate_record_in(record: dict[str, Any], config: SkillConfig) -> dict[str, Any]:
    """Normalize a legacy on-disk record to the canonical 1.1.0 shape (in-memory only)."""
    legacy = config.legacy_scope_field
    canonical = config.scope_field
    if legacy is None or legacy == canonical:
        return record
    migrated = dict(record)
    if legacy in migrated and canonical not in migrated:
        migrated[canonical] = migrated.pop(legacy)
    if migrated.get("scope") == legacy:
        migrated["scope"] = canonical
    return migrated


def migrate_registry_in(registry: dict[str, Any], config: SkillConfig) -> dict[str, Any]:
    if (
        config.legacy_disk_schema_version is not None
        and registry.get("schema_version") == config.legacy_disk_schema_version
    ):
        registry["schema_version"] = config.canonical_schema_version
    registry["records"] = [migrate_record_in(r, config) for r in registry["records"]]
    return registry


def migrate_record_out(record: dict[str, Any], config: SkillConfig) -> dict[str, Any]:
    """Demote a canonical 1.1.0 record back to the skill's legacy on-disk shape."""
    legacy = config.legacy_scope_field
    canonical = config.scope_field
    if legacy is None or legacy == canonical:
        return record
    demoted = dict(record)
    if canonical in demoted and legacy not in demoted:
        demoted[legacy] = demoted.pop(canonical)
    if demoted.get("scope") == canonical:
        demoted["scope"] = legacy
    return demoted


def load_registry(path: Path, config: SkillConfig) -> dict[str, Any]:
    if not path.exists():
        return {"schema_version": config.canonical_schema_version, "updated": None, "records": []}
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict) or not isinstance(data.get("records"), list):
        raise ValueError(f"invalid feedback registry: {path}")
    data.setdefault("schema_version", config.canonical_schema_version)
    data.setdefault("updated", None)
    return migrate_registry_in(data, config)


def validate_date(value: str) -> str:
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError as exc:
        raise ValueError(f"invalid ISO date: {value}") from exc


def prepare_record(raw: dict[str, Any], default_date: str, config: SkillConfig) -> dict[str, Any]:
    record = {
        "scope": normalize(raw.get("scope")),
        "project": normalize(raw.get("project")),
        "section": normalize(raw.get("section")),
        config.scope_field: _scope_discriminator(raw, config),
        "category": normalize(raw.get("category")),
        "severity": normalize(raw.get("severity")),
        "rule": normalize(raw.get("rule")),
        "reason": normalize(raw.get("reason")),
        "evidence": normalize(raw.get("evidence")),
        "source": normalize(raw.get("source")),
        "status": normalize(raw.get("status")) or "active",
    }
    benchmark = normalize(raw.get("benchmark"))
    supersedes = normalize_list(raw.get("supersedes"), "supersedes")
    prohibited_patterns = normalize_list(
        raw.get("prohibited_patterns"),
        "prohibited_patterns",
        collapse_whitespace=False,
    )
    seen = validate_date(normalize(raw.get("date")) or default_date)

    if record["scope"] not in config.valid_scopes:
        raise ValueError(f"scope must be one of {sorted(config.valid_scopes)}")
    if record["category"] not in config.valid_categories:
        raise ValueError(f"category must be one of {sorted(config.valid_categories)}")
    if record["severity"] not in config.valid_severities:
        raise ValueError(f"severity must be one of {sorted(config.valid_severities)}")
    if record["status"] not in config.valid_statuses:
        raise ValueError(f"status must be one of {sorted(config.valid_statuses)}")
    for field_name in ("rule", "reason", "evidence", "source"):
        if not record[field_name]:
            raise ValueError(f"{field_name} is required")
    if record["scope"] == "project" and not record["project"]:
        raise ValueError("project is required when scope=project")
    if record["scope"] == "section" and not record["section"]:
        raise ValueError("section is required when scope=section")
    if record["scope"] == config.scope_field and not record[config.scope_field]:
        raise ValueError(f"{config.scope_field} is required when scope={config.scope_field}")
    for pattern in prohibited_patterns:
        try:
            re.compile(pattern)
        except re.error as exc:
            raise ValueError(f"invalid prohibited pattern {pattern!r}: {exc}") from exc

    if benchmark:
        record["benchmark"] = benchmark
    if supersedes:
        record["supersedes"] = supersedes
    if prohibited_patterns:
        record["prohibited_patterns"] = prohibited_patterns

    record["id"] = fingerprint(record, config)
    record["first_seen"] = seen
    record["last_seen"] = seen
    record["count"] = 1
    return record


def upsert(registry: dict[str, Any], incoming: dict[str, Any]) -> str:
    for existing in registry["records"]:
        if existing.get("id") != incoming["id"]:
            continue
        existing["count"] = int(existing.get("count", 0)) + 1
        existing["last_seen"] = incoming["last_seen"]
        for field_name in ("severity", "reason", "evidence", "source", "status"):
            existing[field_name] = incoming[field_name]
        if incoming.get("benchmark"):
            existing["benchmark"] = incoming["benchmark"]
        for field_name in ("supersedes", "prohibited_patterns"):
            if incoming.get(field_name):
                existing[field_name] = list(
                    dict.fromkeys([*existing.get(field_name, []), *incoming[field_name]])
                )
        return "updated"
    registry["records"].append(incoming)
    return "added"


def write_registry(path: Path, registry: dict[str, Any], config: SkillConfig) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = dict(registry)
    data["records"] = [migrate_record_out(r, config) for r in registry["records"]]
    if config.legacy_disk_schema_version is not None:
        data["schema_version"] = config.legacy_disk_schema_version
    text = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    temp_path = path.with_suffix(path.suffix + ".tmp")
    temp_path.write_text(text, encoding="utf-8")
    temp_path.replace(path)


def record_from_args(args: argparse.Namespace, config: SkillConfig) -> dict[str, Any]:
    scope_value = getattr(args, config.scope_cli_dest, "") if config.scope_cli_flag else ""
    return {
        "scope": args.scope,
        "project": args.project,
        "section": args.section,
        config.scope_field: scope_value,
        "category": args.category,
        "severity": args.severity,
        "rule": args.rule,
        "reason": args.reason,
        "evidence": args.evidence,
        "source": args.source,
        "status": args.status,
        "benchmark": args.benchmark,
        "supersedes": args.supersedes,
        "prohibited_patterns": args.prohibited_patterns,
        "date": args.date,
    }


def build_parser(config: SkillConfig) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=f"Record or inspect user feedback for the {config.skill_name} skill."
    )
    parser.add_argument("--registry", type=Path, default=config.registry_default)
    parser.add_argument("--input", type=Path, help="JSON object/list of feedback records")
    parser.add_argument("--list-active", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--scope", choices=sorted(config.valid_scopes))
    parser.add_argument("--project", default="")
    parser.add_argument("--section", default="")
    if config.scope_cli_flag:
        parser.add_argument(config.scope_cli_flag, dest=config.scope_cli_dest, default="")
    parser.add_argument("--category", choices=sorted(config.valid_categories))
    parser.add_argument("--severity", choices=sorted(config.valid_severities))
    parser.add_argument("--rule")
    parser.add_argument("--reason")
    parser.add_argument("--evidence")
    parser.add_argument("--source")
    parser.add_argument("--benchmark", default="")
    parser.add_argument("--supersedes", action="append", default=[])
    parser.add_argument("--prohibited-pattern", dest="prohibited_patterns", action="append", default=[])
    parser.add_argument("--status", choices=sorted(config.valid_statuses), default="active")
    parser.add_argument("--date", default=date.today().isoformat())
    return parser


def main(config: SkillConfig) -> int:
    parser = build_parser(config)
    args = parser.parse_args()
    registry = load_registry(args.registry, config)

    if args.list_active:
        active = [item for item in registry["records"] if item.get("status") == "active"]
        print(json.dumps(active, ensure_ascii=False, indent=2, sort_keys=True))
        return 0

    if args.input:
        raw_data = json.loads(args.input.read_text(encoding="utf-8"))
        raw_records = raw_data if isinstance(raw_data, list) else [raw_data]
    else:
        required = (args.scope, args.category, args.severity, args.rule, args.reason, args.evidence, args.source)
        if any(value is None for value in required):
            parser.error(
                "single-record mode requires --scope, --category, --severity, --rule, "
                "--reason, --evidence, and --source"
            )
        raw_records = [record_from_args(args, config)]

    actions: list[dict[str, str]] = []
    for raw in raw_records:
        incoming = prepare_record(raw, args.date, config)
        action = upsert(registry, incoming)
        actions.append({"id": incoming["id"], "action": action, "rule": incoming["rule"]})

    registry["schema_version"] = config.canonical_schema_version
    registry["updated"] = validate_date(args.date)
    registry["records"].sort(
        key=lambda item: (
            item.get("scope", ""),
            item.get("project", ""),
            item.get("category", ""),
            item.get("id", ""),
        )
    )
    if not args.dry_run:
        write_registry(args.registry, registry, config)

    print(
        json.dumps(
            {"dry_run": args.dry_run, "registry": str(args.registry), "actions": actions},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


def entrypoint(config: SkillConfig) -> int:
    try:
        return main(config)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
