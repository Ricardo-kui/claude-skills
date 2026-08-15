#!/usr/bin/env python3
"""Record or inspect user feedback for the write-methods skill."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any


SKILL_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REGISTRY = SKILL_ROOT / "references" / "feedback-registry.json"
VALID_SCOPES = {"skill", "project", "section", "design_type"}
VALID_CATEGORIES = {
    "source_intake",
    "methods_results_boundary",
    "section_order",
    "slot_assignment",
    "sample_scope",
    "estimand_definition",
    "terminology",
    "language_lock",
    "voice_tone",
    "measurement_argument",
    "estimator_justification",
    "evidence_interpretation",
    "corpus_fit",
    "interface",
}
VALID_SEVERITIES = {"revise", "reject"}
VALID_STATUSES = {"active", "retired"}


def normalize(value: str | None) -> str:
    return re.sub(r"\s+", " ", (value or "").strip())


def normalize_list(raw: Any, field: str, *, collapse_whitespace: bool = True) -> list[str]:
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


def fingerprint(record: dict[str, Any]) -> str:
    fields = (
        record["scope"],
        record.get("project", ""),
        record.get("section", ""),
        record.get("design_type", ""),
        record["category"],
        record["rule"].casefold(),
    )
    digest = hashlib.sha256("\x1f".join(fields).encode("utf-8")).hexdigest()[:16]
    return f"wmf_{digest}"


def load_registry(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"schema_version": "1.0.0", "updated": None, "records": []}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("records"), list):
        raise ValueError(f"invalid feedback registry: {path}")
    data.setdefault("schema_version", "1.0.0")
    data.setdefault("updated", None)
    return data


def validate_date(value: str) -> str:
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError as exc:
        raise ValueError(f"invalid ISO date: {value}") from exc


def prepare_record(raw: dict[str, Any], default_date: str) -> dict[str, Any]:
    record = {
        "scope": normalize(raw.get("scope")),
        "project": normalize(raw.get("project")),
        "section": normalize(raw.get("section")),
        "design_type": normalize(raw.get("design_type")),
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

    if record["scope"] not in VALID_SCOPES:
        raise ValueError(f"scope must be one of {sorted(VALID_SCOPES)}")
    if record["category"] not in VALID_CATEGORIES:
        raise ValueError(f"category must be one of {sorted(VALID_CATEGORIES)}")
    if record["severity"] not in VALID_SEVERITIES:
        raise ValueError(f"severity must be one of {sorted(VALID_SEVERITIES)}")
    if record["status"] not in VALID_STATUSES:
        raise ValueError(f"status must be one of {sorted(VALID_STATUSES)}")
    for field in ("rule", "reason", "evidence", "source"):
        if not record[field]:
            raise ValueError(f"{field} is required")
    if record["scope"] == "project" and not record["project"]:
        raise ValueError("project is required when scope=project")
    if record["scope"] == "section" and not record["section"]:
        raise ValueError("section is required when scope=section")
    if record["scope"] == "design_type" and not record["design_type"]:
        raise ValueError("design_type is required when scope=design_type")
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
    record["id"] = fingerprint(record)
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
        for field in ("severity", "reason", "evidence", "source", "status"):
            existing[field] = incoming[field]
        if incoming.get("benchmark"):
            existing["benchmark"] = incoming["benchmark"]
        for field in ("supersedes", "prohibited_patterns"):
            if incoming.get(field):
                existing[field] = list(dict.fromkeys([*existing.get(field, []), *incoming[field]]))
        return "updated"
    registry["records"].append(incoming)
    return "added"


def write_registry(path: Path, registry: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(registry, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def record_from_args(args: argparse.Namespace) -> dict[str, Any]:
    return {
        "scope": args.scope,
        "project": args.project,
        "section": args.section,
        "design_type": args.design_type,
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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--input", type=Path, help="JSON object/list of feedback records")
    parser.add_argument("--list-active", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--scope", choices=sorted(VALID_SCOPES))
    parser.add_argument("--project", default="")
    parser.add_argument("--section", default="")
    parser.add_argument("--design-type", dest="design_type", default="")
    parser.add_argument("--category", choices=sorted(VALID_CATEGORIES))
    parser.add_argument("--severity", choices=sorted(VALID_SEVERITIES))
    parser.add_argument("--rule")
    parser.add_argument("--reason")
    parser.add_argument("--evidence")
    parser.add_argument("--source")
    parser.add_argument("--benchmark", default="")
    parser.add_argument("--supersedes", action="append", default=[])
    parser.add_argument("--prohibited-pattern", dest="prohibited_patterns", action="append", default=[])
    parser.add_argument("--status", choices=sorted(VALID_STATUSES), default="active")
    parser.add_argument("--date", default=date.today().isoformat())
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    registry = load_registry(args.registry)

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
            parser.error("single-record mode requires --scope, --category, --severity, --rule, --reason, --evidence, and --source")
        raw_records = [record_from_args(args)]

    actions: list[dict[str, str]] = []
    for raw in raw_records:
        incoming = prepare_record(raw, args.date)
        action = upsert(registry, incoming)
        actions.append({"id": incoming["id"], "action": action, "rule": incoming["rule"]})

    registry["schema_version"] = "1.0.0"
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
        write_registry(args.registry, registry)

    print(json.dumps({"dry_run": args.dry_run, "registry": str(args.registry), "actions": actions}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
