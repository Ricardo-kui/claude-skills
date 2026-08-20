#!/usr/bin/env python3
"""Check a Methods manuscript against active deterministic feedback rules."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


SKILL_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REGISTRY = SKILL_ROOT / "references" / "feedback-registry.json"
DEFAULT_END_HEADING = r"^(?:##\s+生成后自检记录|>\s+\*\*\d{4}-\d{2}-\d{2}\s+修订记录)"


def normalized(value: str | None) -> str:
    return re.sub(r"\s+", " ", (value or "").strip()).casefold()


def load_registry(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("records"), list):
        raise ValueError(f"invalid feedback registry: {path}")
    return data


def context_matches(record: dict[str, Any], args: argparse.Namespace) -> bool:
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
    elif scope == "design_type":
        if not args.design_type or normalized(record.get("design_type")) != normalized(args.design_type):
            return False
    else:
        return False
    return not record.get("project") or normalized(record.get("project")) == normalized(args.project)


def applicable_records(registry: dict[str, Any], args: argparse.Namespace) -> list[dict[str, Any]]:
    records = [record for record in registry["records"] if context_matches(record, args)]
    superseded = {
        item
        for record in records
        for item in record.get("supersedes", [])
        if isinstance(item, str) and item.startswith("wmf_")
    }
    return [record for record in records if record.get("id") not in superseded]


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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manuscript", help="Methods Markdown path, or - for stdin")
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--project", default="")
    parser.add_argument("--section", default="")
    parser.add_argument("--design-type", dest="design_type", default="")
    parser.add_argument("--end-heading", default=DEFAULT_END_HEADING)
    parser.add_argument("--whole-file", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    registry = load_registry(args.registry)
    records = applicable_records(registry, args)
    compiled: list[tuple[dict[str, Any], str, re.Pattern[str]]] = []
    for record in records:
        for pattern in record.get("prohibited_patterns", []):
            compiled.append((record, pattern, re.compile(pattern)))

    source_name, all_lines = read_lines(args.manuscript)
    end_heading = None if args.whole_file else re.compile(args.end_heading)
    lines = manuscript_lines(all_lines, end_heading, args.whole_file)
    violations: list[tuple[int, str, str, str]] = []
    for line_number, line in lines:
        for record, pattern_text, pattern in compiled:
            for match in pattern.finditer(line):
                violations.append((line_number, record["id"], match.group(0), pattern_text))

    if violations:
        print("write-methods language lint FAILED")
        for line_number, record_id, matched, pattern_text in violations:
            print(f"- {source_name}:{line_number} [{record_id}] matched {matched!r} ({pattern_text})")
        return 1

    print("write-methods language lint PASSED")
    print(f"- source: {source_name}")
    print(f"- scanned lines: {len(lines)}")
    print(f"- applicable active rules: {len(records)}")
    print(f"- prohibited patterns: {len(compiled)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError, re.error) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
