#!/usr/bin/env python3
"""Dependency-free structural validation for the write-results skill."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REQUIRED_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "references/draft-revision-protocol.md",
    "references/feedback-protocol.md",
    "references/feedback-registry.json",
    "references/validation-protocol.md",
    "references/design-branches.md",
    "references/anti-patterns.md",
    "references/post-generation-checklist.md",
    "references/hypothesis-fulfillment-map.md",
    "references/story-resolution.md",
    "references/paper-state-schema.md",
    "references/slot-R2.md",
    "references/slot-R3.md",
    "references/slot-R7.md",
    "references/slot-R8.md",
    "scripts/lint_results_language.py",
    "scripts/record_feedback.py",
)
FORBIDDEN_SKILL_TEXT = (
    "distill-results-exemplar --validate",
    "references/output-metadata-template.md",
    "`econometric-models/micro-templates/`",
)
REQUIRED_SKILL_TEXT = (
    "Phase -1",
    "draft-revision-protocol.md",
    "feedback-protocol.md",
    "feedback-registry.json",
    "validation-protocol.md",
    "revision_constraints",
)
REQUIRED_RECORD_FIELDS = {
    "id",
    "scope",
    "category",
    "severity",
    "rule",
    "reason",
    "evidence",
    "source",
    "status",
    "count",
    "first_seen",
    "last_seen",
}


def check_frontmatter(text: str, errors: list[str]) -> None:
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", text, re.DOTALL)
    if not match:
        errors.append("SKILL.md has no valid YAML frontmatter fence")
        return
    keys = []
    for line in match.group(1).splitlines():
        if line and not line.startswith((" ", "\t", "#")) and ":" in line:
            keys.append(line.split(":", 1)[0].strip())
    if set(keys) != {"name", "description"}:
        errors.append(f"SKILL.md frontmatter keys must be name and description only; found {keys}")
    if not re.search(r"^name:\s*write-results\s*$", match.group(1), re.MULTILINE):
        errors.append("SKILL.md frontmatter name must be write-results")


def check_story_table(errors: list[str]) -> None:
    lines = (ROOT / "references" / "story-resolution.md").read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines[:-1]):
        if line.startswith("| Storyline |"):
            header_cells = [cell for cell in line.split("|")[1:-1]]
            rule_cells = [cell for cell in lines[index + 1].split("|")[1:-1]]
            if len(header_cells) != len(rule_cells):
                errors.append("story-resolution.md table header/separator column count differs")
            return
    errors.append("story-resolution.md storyline table not found")


def check_registry(errors: list[str]) -> None:
    path = ROOT / "references" / "feedback-registry.json"
    try:
        registry = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"feedback registry is invalid JSON: {exc}")
        return
    if not isinstance(registry, dict) or not isinstance(registry.get("records"), list):
        errors.append("feedback registry must contain a records list")
        return
    if registry.get("schema_version") != "1.1.0":
        errors.append("feedback registry schema_version must be 1.1.0")
    ids: set[str] = set()
    for index, record in enumerate(registry["records"], start=1):
        missing = REQUIRED_RECORD_FIELDS - set(record)
        if missing:
            errors.append(f"feedback record {index} missing fields: {sorted(missing)}")
        record_id = record.get("id")
        if record_id in ids:
            errors.append(f"duplicate feedback id: {record_id}")
        ids.add(record_id)
        benchmark = record.get("benchmark")
        if benchmark is not None and not isinstance(benchmark, str):
            errors.append(f"feedback record {index} benchmark must be a string")
        for field in ("supersedes", "prohibited_patterns"):
            values = record.get(field)
            if values is not None and (
                not isinstance(values, list) or not all(isinstance(item, str) for item in values)
            ):
                errors.append(f"feedback record {index} {field} must be a list of strings")
        for pattern in record.get("prohibited_patterns", []):
            try:
                re.compile(pattern)
            except re.error as exc:
                errors.append(f"feedback record {index} has invalid prohibited pattern {pattern!r}: {exc}")


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    skill_path = ROOT / "SKILL.md"
    if skill_path.is_file():
        skill_text = skill_path.read_text(encoding="utf-8")
        check_frontmatter(skill_text, errors)
        for forbidden in FORBIDDEN_SKILL_TEXT:
            if forbidden in skill_text:
                errors.append(f"stale or invalid SKILL.md reference: {forbidden}")
        for required in REQUIRED_SKILL_TEXT:
            if required not in skill_text:
                errors.append(f"SKILL.md missing required workflow marker: {required}")

    check_story_table(errors)
    check_registry(errors)

    if errors:
        print("write-results validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("write-results validation PASSED")
    print(f"- required files: {len(REQUIRED_FILES)}")
    print("- frontmatter, workflow markers, feedback registry, and story table are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
