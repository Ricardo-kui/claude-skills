"""Validate v0.4-lite story-learning cards without judging their interpretations."""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CARDS = ROOT / "v4" / "blueprints"
REQUIRED_HEADINGS = ["Story Reading", "Theme question", "Whole-story synopsis", "Characters and storylines", "Five acts", "Story Assessment", "Learning Affordances"]
SECTIONS = {"introduction", "theory", "methods", "results", "discussion"}
SUITABILITY = {"yes", "partial", "no"}
ROLES = {"exemplar", "partial_exemplar", "contrastive_case", "cautionary_case", "descriptive_only"}


def metadata(text: str) -> dict:
    match = re.search(r"## Metadata\s+```yaml\s*(.*?)```", text, re.S)
    if not match:
        raise ValueError("missing Metadata YAML block")
    value = yaml.safe_load(match.group(1))
    if not isinstance(value, dict):
        raise ValueError("Metadata YAML block is not a mapping")
    return value


def validate(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    try:
        data = metadata(text)
    except ValueError as exc:
        return [str(exc)]
    if data.get("schema_version") != "4.0-lite":
        errors.append("schema_version must be 4.0-lite")
    for key in ("id", "paper", "reading_scope", "section_learning", "story_assessment"):
        if key not in data:
            errors.append(f"missing metadata field: {key}")
    for heading in REQUIRED_HEADINGS:
        if f"## {heading}" not in text and f"### {heading}" not in text:
            errors.append(f"missing heading: {heading}")
    scope = data.get("reading_scope", {})
    if scope.get("coverage") not in {"complete", "partial"}:
        errors.append("reading_scope.coverage must be complete or partial")
    learning = data.get("section_learning", {})
    for section in SECTIONS:
        item = learning.get(section)
        if not isinstance(item, dict):
            errors.append(f"section_learning.{section} must be a mapping")
            continue
        if item.get("suitable") not in SUITABILITY:
            errors.append(f"section_learning.{section}.suitable is invalid")
        if item.get("suitable") in {"yes", "partial"} and not item.get("learn"):
            errors.append(f"section_learning.{section} needs a learning move")
    assessment = data.get("story_assessment", {})
    role = assessment.get("overall_role")
    if role not in ROLES:
        errors.append("story_assessment.overall_role is invalid")
    if role == "exemplar" and scope.get("coverage") != "complete":
        errors.append("exemplar requires complete reading coverage")
    return errors


def main() -> int:
    cards = sorted(CARDS.glob("*.md"))
    if not cards:
        print("v0.4-lite: no cards yet (scaffold valid)")
        return 0
    failures = 0
    for card in cards:
        issues = validate(card)
        if issues:
            failures += 1
            for issue in issues:
                print(f"ERROR {card.name}: {issue}")
    print(f"v0.4-lite cards: {len(cards)} | invalid: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
