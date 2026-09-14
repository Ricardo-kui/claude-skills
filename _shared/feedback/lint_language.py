#!/usr/bin/env python3
"""Shared deterministic language-lock scanner for the write-* skills.

Scans a manuscript against two sources of prohibited patterns:

1. active registry records with inline ``prohibited_patterns`` (per-skill registry);
2. an optional standalone vocabulary file (e.g. write-introduction's meta-language
   word list), each entry ``{"id": ..., "pattern": ...}``.

Parameterized by the same ``SkillConfig`` used by ``record_feedback.py``, plus the
per-skill end-heading and standalone vocabulary path carried on the config.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from record_feedback import SkillConfig, load_registry


def normalized(value: str | None) -> str:
    return re.sub(r"\s+", " ", (value or "").strip()).casefold()


def context_matches(record: dict[str, Any], args: argparse.Namespace, config: SkillConfig) -> bool:
    if record.get("status") != "active":
        return False
    scope = record.get("scope")
    if scope == "skill":
        return True
    if scope == "project":
        return bool(args.project) and normalized(record.get("project")) == normalized(args.project)
    if scope == "section":
        if not args.section or normalized(record.get("section")) != normalized(args.section):
            return False
    elif scope == config.scope_field:
        provided = getattr(args, config.scope_cli_dest, "")
        if not provided or normalized(record.get(config.scope_field)) != normalized(provided):
            return False
    else:
        return False
    return not record.get("project") or normalized(record.get("project")) == normalized(args.project)


def applicable_records(
    registry: dict[str, Any], args: argparse.Namespace, config: SkillConfig
) -> list[dict[str, Any]]:
    records = [record for record in registry["records"] if context_matches(record, args, config)]
    superseded = {
        item
        for record in records
        for item in record.get("supersedes", [])
        if isinstance(item, str) and item.startswith(config.id_prefix)
    }
    return [record for record in records if record.get("id") not in superseded]


def load_standalone_patterns(path: Path | None) -> list[tuple[str, str]]:
    """Load a standalone vocabulary file into [(id, pattern), ...]."""
    if path is None or not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    items = data.get("patterns", []) if isinstance(data, dict) else data
    if not isinstance(items, list):
        raise ValueError(f"invalid prohibited patterns file: {path}")
    out: list[tuple[str, str]] = []
    for item in items:
        if isinstance(item, str):
            out.append((item, item))
        elif isinstance(item, dict):
            pattern = item.get("pattern")
            if not isinstance(pattern, str):
                raise ValueError(f"invalid prohibited pattern entry in {path}: {item!r}")
            out.append((str(item.get("id", pattern)), pattern))
        else:
            raise ValueError(f"invalid prohibited pattern entry in {path}: {item!r}")
    return out


def read_lines(source: str) -> tuple[str, list[str]]:
    if source == "-":
        return "<stdin>", sys.stdin.read().splitlines()
    path = Path(source)
    return str(path), path.read_text(encoding="utf-8").splitlines()


def manuscript_lines(
    lines: list[str],
    end_heading: re.Pattern[str] | None,
    whole_file: bool,
) -> list[tuple[int, str]]:
    selected: list[tuple[int, str]] = []
    in_fence = False
    in_frontmatter = bool(lines and lines[0].strip() == "---")
    for line_number, line in enumerate(lines, start=1):
        stripped = line.strip()
        if in_frontmatter:
            if line_number > 1 and stripped == "---":
                in_frontmatter = False
            continue
        if not whole_file and end_heading and end_heading.search(line):
            break
        if stripped.startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if not in_fence:
            selected.append((line_number, line))
    return selected


def build_parser(config: SkillConfig) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            f"Check a {config.skill_name} manuscript against active deterministic "
            "language locks."
        )
    )
    parser.add_argument("manuscript", help="Markdown path, or - for stdin")
    parser.add_argument("--registry", type=Path, default=config.registry_default)
    parser.add_argument("--project", default="")
    parser.add_argument("--section", default="")
    if config.scope_cli_flag:
        parser.add_argument(config.scope_cli_flag, dest=config.scope_cli_dest, default="")
    parser.add_argument(
        "--end-heading",
        default=config.end_heading,
        help="Stop before the first matching heading unless --whole-file is set",
    )
    parser.add_argument("--whole-file", action="store_true")
    return parser


def main(config: SkillConfig) -> int:
    args = build_parser(config).parse_args()
    registry = load_registry(args.registry, config)
    records = applicable_records(registry, args, config)
    compiled: list[tuple[str, str, re.Pattern[str]]] = []
    for record in records:
        for pattern in record.get("prohibited_patterns", []):
            compiled.append((record["id"], pattern, re.compile(pattern)))
    for pattern_id, pattern in load_standalone_patterns(config.standalone_patterns_path):
        compiled.append((pattern_id, pattern, re.compile(pattern)))

    source_name, all_lines = read_lines(args.manuscript)
    end_heading = None if args.whole_file else re.compile(args.end_heading)
    lines = manuscript_lines(all_lines, end_heading, args.whole_file)
    violations: list[tuple[int, str, str, str]] = []
    for line_number, line in lines:
        for record_id, pattern_text, pattern in compiled:
            for match in pattern.finditer(line):
                violations.append((line_number, record_id, match.group(0), pattern_text))

    if violations:
        print(f"{config.skill_name} language lint FAILED")
        for line_number, record_id, matched, pattern_text in violations:
            print(f"- {source_name}:{line_number} [{record_id}] matched {matched!r} ({pattern_text})")
        return 1

    print(f"{config.skill_name} language lint PASSED")
    print(f"- source: {source_name}")
    print(f"- scanned lines: {len(lines)}")
    print(f"- applicable active rules: {len(records)}")
    print(f"- prohibited patterns: {len(compiled)}")
    return 0


def entrypoint(config: SkillConfig) -> int:
    try:
        return main(config)
    except (OSError, ValueError, json.JSONDecodeError, re.error) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
