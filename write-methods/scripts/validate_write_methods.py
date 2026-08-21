#!/usr/bin/env python3
"""Dependency-free structural validation for the write-methods skill."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REQUIRED_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "references/anti-patterns.md",
    "references/draft-revision-protocol.md",
    "references/feedback-protocol.md",
    "references/feedback-registry.json",
    "references/post-generation-checklist.md",
    "references/validation-protocol.md",
    "scripts/lint_methods_language.py",
    "scripts/record_feedback.py",
)
REQUIRED_SKILL_TEXT = (
    "Phase -1",
    "draft-revision-protocol.md",
    "feedback-protocol.md",
    "feedback-registry.json",
    "validation-protocol.md",
    "revision_constraints",
    "lint_methods_language.py",
)
FORBIDDEN_SKILL_TEXT = (
    "_update_registry.py",
    "只登记变体产出质量批评，不登记 [placeholder] 流程抱怨与风格偏好",
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
    required = {"name", "description"}
    optional = {"whenToUse", "when_to_use"}  # 多端部署自动触发字段（whenToUse 2026-08-19 标配；when_to_use 由 frontmatter 标准化引入）
    if not required.issubset(keys) or set(keys) - required - optional:
        errors.append(f"SKILL.md frontmatter keys must be name/description (whenToUse optional); found {keys}")
    if not re.search(r"^name:\s*write-methods\s*$", match.group(1), re.MULTILINE):
        errors.append("SKILL.md frontmatter name must be write-methods")


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
    if registry.get("schema_version") != "1.0.0":
        errors.append("feedback registry schema_version must be 1.0.0")
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
        for required in REQUIRED_SKILL_TEXT:
            if required not in skill_text:
                errors.append(f"SKILL.md missing required workflow marker: {required}")
        for forbidden in FORBIDDEN_SKILL_TEXT:
            if forbidden in skill_text:
                errors.append(f"SKILL.md contains stale feedback instruction: {forbidden}")

    check_registry(errors)
    if errors:
        print("write-methods validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("write-methods validation PASSED")
    print(f"- required files: {len(REQUIRED_FILES)}")
    print("- frontmatter, workflow markers, and feedback registry are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
