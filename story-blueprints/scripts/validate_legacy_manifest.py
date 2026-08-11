"""Validate the generated Legacy Evidence Layer without evaluating story quality."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BLUEPRINTS = ROOT / "blueprints"
MANIFEST = ROOT / "legacy" / "legacy-manifest.json"
MIGRATION_STATUSES = {"not_assessed", "candidate", "reviewed", "migrated", "retained_as_legacy"}
REQUIRED = {
    "id",
    "original_blueprint",
    "paper",
    "full_text",
    "legacy_coverage_confidence",
    "legacy_interpretation",
    "research_profile",
    "legacy_story_evidence",
    "seed_relations",
    "v4_relation",
    "runtime_eligibility",
    "migration_status",
    "source_records",
}


def main() -> int:
    if not MANIFEST.exists():
        print("ERROR: manifest does not exist; run build_legacy_manifest.py")
        return 1
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    entries = data.get("entries", [])
    expected = len([p for p in BLUEPRINTS.glob("*.md") if p.name != "_index.md"])
    errors: list[str] = []
    if data.get("schema_version") != "legacy-evidence-layer-1.0":
        errors.append("invalid schema_version")
    if len(entries) != expected:
        errors.append(f"entry count {len(entries)} does not match legacy blueprint count {expected}")
    seen: set[str] = set()
    for entry in entries:
        card_id = entry.get("id", "<missing>")
        missing = REQUIRED - set(entry)
        if missing:
            errors.append(f"{card_id}: missing {sorted(missing)}")
        if card_id in seen:
            errors.append(f"duplicate id: {card_id}")
        seen.add(card_id)
        if entry.get("runtime_eligibility") != "no":
            errors.append(f"{card_id}: legacy entry must have runtime_eligibility=no")
        if entry.get("migration_status") not in MIGRATION_STATUSES:
            errors.append(f"{card_id}: invalid migration_status")
        coverage = entry.get("legacy_coverage_confidence", {})
        if not isinstance(coverage, dict) or coverage.get("value") not in {"claimed_complete", "claimed_partial"}:
            errors.append(f"{card_id}: invalid legacy_coverage_confidence")
        if not (ROOT / entry.get("original_blueprint", "")).exists():
            errors.append(f"{card_id}: original_blueprint does not exist")
        full_text = entry.get("full_text", {})
        if not isinstance(full_text, dict) or full_text.get("availability") not in {
            "reported_readable_from_legacy",
            "not_assessed",
        }:
            errors.append(f"{card_id}: invalid full_text availability")
        interpretation = entry.get("legacy_interpretation", {})
        if not isinstance(interpretation, dict) or interpretation.get("status") != "historical_analyst_interpretation_only":
            errors.append(f"{card_id}: invalid legacy_interpretation status")
        profile = entry.get("research_profile", {})
        if not isinstance(profile, dict) or {
            "theoretical_domain", "research_form", "empirical_setting", "main_constructs"
        } - set(profile):
            errors.append(f"{card_id}: incomplete research_profile")
        story_evidence = entry.get("legacy_story_evidence", {})
        if not isinstance(story_evidence, dict) or {
            "observed_assets", "known_risks", "unverified_aspects"
        } - set(story_evidence):
            errors.append(f"{card_id}: incomplete legacy_story_evidence")
        relation = entry.get("v4_relation", {})
        if not isinstance(relation, dict) or "relation" not in relation or "v4_card_ids" not in relation:
            errors.append(f"{card_id}: invalid v4_relation")
        elif entry.get("migration_status") == "migrated" and not relation.get("v4_card_ids"):
            errors.append(f"{card_id}: migrated entry lacks a v4_card_id")
        seed_relations = entry.get("seed_relations")
        if not isinstance(seed_relations, list):
            errors.append(f"{card_id}: seed_relations must be a list")
        elif entry.get("migration_status") == "candidate" and not seed_relations:
            errors.append(f"{card_id}: candidate lacks a seed relation")
        else:
            for seed_relation in seed_relations:
                if not isinstance(seed_relation, dict) or {
                    "seed_id", "relation_hypothesis", "comparison_question", "status"
                } - set(seed_relation):
                    errors.append(f"{card_id}: malformed seed relation")
                elif seed_relation["status"] not in {"proposed", "confirmed", "refuted"}:
                    errors.append(f"{card_id}: invalid seed relation status")
    for error in errors:
        print(f"ERROR: {error}")
    print(f"legacy manifest entries: {len(entries)} | invalid: {len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
