"""Build a read-only evidence manifest from v0.3 story blueprints.

The builder never writes a legacy blueprint. It records missing v0.3 metadata as
not_assessed rather than inferring facts from a paper title or journal prestige.
"""

from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
BLUEPRINTS = ROOT / "blueprints"
V4_BLUEPRINTS = ROOT / "v4" / "blueprints"
LEGACY_DIR = ROOT / "legacy"
OVERRIDES = LEGACY_DIR / "legacy-overrides.yaml"
OUTPUT = LEGACY_DIR / "legacy-manifest.json"

MIGRATION_STATUSES = {
    "not_assessed",
    "candidate",
    "reviewed",
    "migrated",
    "retained_as_legacy",
}


def fenced_yaml(text: str, heading: str | None = None) -> dict[str, Any]:
    scope = text
    if heading:
        match = re.search(
            rf"^#{{2,3}} {re.escape(heading)}\s*$([\s\S]*?)(?=^#{{2,3}} |\Z)",
            text,
            re.M,
        )
        if not match:
            return {}
        scope = match.group(1)
    match = re.search(r"```yaml\s*([\s\S]*?)```", scope)
    if not match:
        return {}
    try:
        value = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return {"_legacy_yaml_parse_status": "unstructured"}
    return value if isinstance(value, dict) else {}


def section_text(text: str, heading: str) -> str:
    match = re.search(
        rf"^### {re.escape(heading)}\s*$([\s\S]*?)(?=^### |^## |\Z)",
        text,
        re.M,
    )
    return match.group(1).strip() if match else ""


def first_nonempty(*values: Any) -> Any:
    for value in values:
        if value not in (None, "", [], {}):
            return value
    return None


def normal_list(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [str(item) for item in value if str(item).strip()]


def reported_full_text_status(text: str, source_records: list[str]) -> dict[str, Any]:
    source_hint = " ".join(source_records)
    markers = ("全文", "ocr", "clippings", "parsed", "原文回读", "full text")
    if any(marker.lower() in (text + " " + source_hint).lower() for marker in markers):
        return {
            "availability": "reported_readable_from_legacy",
            "verification": "not_currently_verified",
            "basis": "Legacy text contains a full-text/OCR/Clippings reading marker.",
        }
    return {
        "availability": "not_assessed",
        "verification": "not_currently_verified",
        "basis": "v0.3 metadata does not establish a current full-text locator.",
    }


def coverage(sections: list[str]) -> dict[str, Any]:
    core = {"intro", "theory", "methods", "results"}
    normalized = {str(item).strip().lower() for item in sections}
    return {
        "value": "claimed_complete" if core.issubset(normalized) else "claimed_partial",
        "sections": sections,
        "basis": "v0.3 distilled_sections declaration; not a narrative-quality judgment.",
    }


def v4_ids() -> set[str]:
    ids: set[str] = set()
    for path in V4_BLUEPRINTS.glob("*.md"):
        metadata = fenced_yaml(path.read_text(encoding="utf-8"), None)
        if isinstance(metadata.get("id"), str):
            ids.add(metadata["id"])
    return ids


def load_overrides() -> dict[str, dict[str, Any]]:
    if not OVERRIDES.exists():
        return {}
    value = yaml.safe_load(OVERRIDES.read_text(encoding="utf-8")) or {}
    cards = value.get("cards", {}) if isinstance(value, dict) else {}
    return cards if isinstance(cards, dict) else {}


def build_entry(path: Path, overrides: dict[str, dict[str, Any]], migrated_ids: set[str]) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    header = fenced_yaml(text, "文件头")
    knot_block = fenced_yaml(text, "knot")
    character_block = fenced_yaml(text, "characters")
    knot = knot_block.get("knot", knot_block) if isinstance(knot_block, dict) else {}
    characters = character_block.get("characters", character_block) if isinstance(character_block, dict) else {}
    card_id = str(header.get("id") or path.stem)
    override = overrides.get(card_id, {})
    if not isinstance(override, dict):
        override = {}

    source_records = normal_list(header.get("source_records"))
    source_records += normal_list(header.get("vault_reports"))
    primary_type = knot.get("primary_type") if isinstance(knot.get("primary_type"), str) else None
    resolution = section_text(text, "resolution_logic")
    protagonists = normal_list(characters.get("protagonist"))
    setting = normal_list(characters.get("ensemble"))
    explicit_form = header.get("paper_type") if isinstance(header.get("paper_type"), str) else None
    inferred_form = explicit_form or "not_assessed"
    migration_status = "migrated" if card_id in migrated_ids else override.get("migration_status", "not_assessed")
    if migration_status not in MIGRATION_STATUSES:
        raise ValueError(f"{card_id}: invalid migration_status override: {migration_status}")

    v4_relation = {
        "relation": "migrated_exact_id" if card_id in migrated_ids else "no_v4_card_yet",
        "v4_card_ids": [card_id] if card_id in migrated_ids else [],
    }

    entry = {
        "id": card_id,
        "original_blueprint": str(path.relative_to(ROOT)).replace("\\", "/"),
        "paper": {
            "legacy_citation": header.get("paper") or "not_assessed",
            "identity_verification": "not_currently_verified",
        },
        "full_text": reported_full_text_status(text, source_records),
        "legacy_coverage_confidence": coverage(normal_list(header.get("distilled_sections"))),
        "legacy_interpretation": {
            "knot_primary": primary_type or "not_assessed",
            "knot_compound": normal_list(knot.get("compound_types")),
            "resolution_excerpt": resolution or "not_assessed",
            "status": "historical_analyst_interpretation_only",
        },
        "research_profile": {
            "theoretical_domain": override.get("theoretical_domain", "not_assessed"),
            "research_form": {
                "value": override.get("research_form", inferred_form),
                "basis": (
                    "human_verified_override"
                    if "research_form" in override
                    else "legacy_paper_type_field"
                    if explicit_form
                    else "not_encoded_in_v0.3_metadata"
                ),
            },
            "empirical_setting": override.get("empirical_setting", setting or "not_assessed"),
            "main_constructs": override.get("main_constructs", protagonists or "not_assessed"),
        },
        "legacy_story_evidence": {
            "observed_assets": [
                name
                for name, value in {
                    "one_liner": section_text(text, "one_liner"),
                    "five_acts": fenced_yaml(text, "five_acts"),
                    "alternative_tellings": section_text(text, "alternative_tellings"),
                    "storytelling_tools": fenced_yaml(text, "storytelling_tools"),
                }.items()
                if value
            ],
            "known_risks": override.get("known_risks", []),
            "unverified_aspects": override.get(
                "unverified_aspects",
                [
                    "No independent v0.4 story assessment has established narrative quality.",
                    "No section-specific transfer conditions have been reviewed under v0.4.",
                ],
            ),
        },
        "seed_relations": override.get("seed_relations", []),
        "v4_relation": v4_relation,
        "runtime_eligibility": "no",
        "migration_status": migration_status,
        "source_records": source_records,
    }
    return entry


def main() -> int:
    overrides = load_overrides()
    migrated_ids = v4_ids()
    entries = [
        build_entry(path, overrides, migrated_ids)
        for path in sorted(BLUEPRINTS.glob("*.md"))
        if path.name != "_index.md"
    ]
    manifest = {
        "schema_version": "legacy-evidence-layer-1.0",
        "generated_on": date.today().isoformat(),
        "source_policy": "Generated from immutable v0.3 blueprints plus optional human-verified overrides.",
        "runtime_policy": "Legacy entries are discovery and migration evidence only; runtime recommendation is prohibited.",
        "entries": entries,
    }
    LEGACY_DIR.mkdir(exist_ok=True)
    OUTPUT.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"legacy manifest built: {len(entries)} entries -> {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
