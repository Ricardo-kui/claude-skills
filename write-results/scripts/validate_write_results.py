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
    "`corpus/micro-templates/`",
    "_pilot_r2_index",
)
REQUIRED_SKILL_TEXT = (
    "Phase -1",
    "draft-revision-protocol.md",
    "feedback-protocol.md",
    "validation-protocol.md",
    "revision_constraints",
)
# 反馈闭环指针：远端架构改为指向 _feedback-registries.md 的单源指针，registry 文件名不再必须出现在 SKILL.md（任一即通过）
FEEDBACK_POINTER_TEXT = ("feedback-registry.json", "_feedback-registries.md")
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


def check_fence_balance(errors: list[str]) -> None:
    """孤立 ``` 围栏配平：每个 markdown 文件中围栏行数必须为偶数（奇数=有未闭合围栏）。"""
    md_files = [ROOT / "SKILL.md"]
    md_files += sorted((ROOT / "references").glob("*.md"))
    md_files += sorted((ROOT / "corpus").glob("*.md"))
    for path in md_files:
        if not path.is_file():
            continue
        fences = sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.lstrip().startswith("```"))
        if fences % 2:
            errors.append(f"unbalanced code fences (odd ``` count={fences}): {path.relative_to(ROOT)}")


def check_olsfe_quickref(errors: list[str]) -> None:
    """OLS-FE 速查表行数 == `### 变体 N` 标题数（死库存对账，真值=grep 计数）。"""
    path = ROOT / "corpus" / "OLS-FE.md"
    if not path.is_file():
        errors.append("missing corpus/OLS-FE.md")
        return
    text = path.read_text(encoding="utf-8")
    headings = re.findall(r"^### 变体\s*(\d+)", text, re.MULTILINE)
    quickref = text.split("## 变体速查表", 1)[-1].split("## 易混决策对", 1)[0]
    rows = re.findall(r"^\|\s*(\d+)\s*\|", quickref, re.MULTILINE)
    if len(rows) != len(set(rows)):
        errors.append(f"OLS-FE quick-ref has duplicate variant ids: {sorted({r for r in rows if rows.count(r) > 1}, key=int)}")
    if len(rows) != len(headings):
        missing = sorted(set(headings) - set(rows), key=int)
        errors.append(
            f"OLS-FE quick-ref rows ({len(rows)}) != variant headings ({len(headings)}); missing ids: {missing}"
        )


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
        if not any(marker in skill_text for marker in FEEDBACK_POINTER_TEXT):
            errors.append("SKILL.md missing feedback-loop pointer: expected 'feedback-registry.json' or '_feedback-registries.md'")

    check_story_table(errors)
    check_registry(errors)
    check_fence_balance(errors)
    check_olsfe_quickref(errors)

    if errors:
        print("write-results validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("write-results validation PASSED")
    print(f"- required files: {len(REQUIRED_FILES)}")
    print("- frontmatter, workflow markers, feedback registry, story table, fences, and OLS-FE quick-ref are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
