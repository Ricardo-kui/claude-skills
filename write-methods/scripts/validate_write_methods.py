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


def check_variant_counts(errors: list[str], warnings: list[str]) -> None:
    """Reconcile `### 变体 N` heading counts with frontmatter variants_count and INDEX.md cells."""
    corpus_dir = ROOT / "corpus"
    heading_counts: dict[str, int] = {}
    for path in sorted(corpus_dir.glob("*.md")):
        if path.name == "INDEX.md":
            continue
        text = path.read_text(encoding="utf-8")
        count = len(re.findall(r"^### 变体 \d+", text, re.MULTILINE))
        heading_counts[path.name] = count
        match = re.search(r"^variants_count:\s*(\d+)", text, re.MULTILINE)
        if match and int(match.group(1)) != count:
            message = f"{path.name}: variants_count={match.group(1)} but {count} '### 变体 N' headings"
            # 面板数据-OLS 已完成 2026-09-08 计数对账，其一致性是硬断言；其余文件历史漂移仅告警，待后续专线收敛
            (errors if path.name == "面板数据-OLS.md" else warnings).append(message)

    index_path = corpus_dir / "INDEX.md"
    if not index_path.is_file():
        return
    index_text = index_path.read_text(encoding="utf-8")
    for name, target, declared in re.findall(
        r"^\| \[([^]]+)]\(([^)]+\.md)\) \| [^|]+ \| (\d+) \|", index_text, re.MULTILINE
    ):
        actual = heading_counts.get(target)
        if actual is None:
            warnings.append(f"INDEX.md row '{name}' links to missing corpus file {target}")
        elif int(declared) != actual:
            message = f"INDEX.md row '{name}' declares {declared} variants but {target} has {actual} headings"
            (errors if target == "面板数据-OLS.md" else warnings).append(message)


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
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
    check_variant_counts(errors, warnings)
    if errors:
        print("write-methods validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("write-methods validation PASSED")
    print(f"- required files: {len(REQUIRED_FILES)}")
    print("- frontmatter, workflow markers, and feedback registry are valid")
    if warnings:
        print(f"- variant-count warnings (non-fatal): {len(warnings)}")
        for warning in warnings:
            print(f"  - {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
