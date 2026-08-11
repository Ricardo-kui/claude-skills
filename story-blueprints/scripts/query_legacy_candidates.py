"""Discover legacy re-reading candidates; never return runtime writing recommendations."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "legacy" / "legacy-manifest.json"

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, ValueError):
    pass


def text(entry: dict) -> str:
    return json.dumps(entry, ensure_ascii=False).lower()


def next_action(entry: dict) -> str:
    status = entry.get("migration_status")
    if status == "migrated":
        card_ids = entry.get("v4_relation", {}).get("v4_card_ids", [])
        return f"Consult the reviewed v0.4 card ({', '.join(card_ids) or 'linked card'}); legacy remains non-runtime evidence."
    if status == "reviewed":
        return "Complete or validate the v0.4 card before any runtime writing use."
    return "Read full text and perform a v0.4 assessment before any writing use."


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contains", default="", help="Case-insensitive metadata search, for discovery only.")
    parser.add_argument("--legacy-knot", default="", help="Filter by historical primary knot label.")
    parser.add_argument("--seed", default="", help="Show only candidates manually linked to a v0.4 seed.")
    parser.add_argument("--migration-status", default="not_assessed")
    parser.add_argument("--limit", type=int, default=3)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    args = parser.parse_args()
    data = json.loads(args.manifest.read_text(encoding="utf-8"))
    needle = args.contains.lower().strip()
    knot = args.legacy_knot.strip()
    seed = args.seed.strip()
    candidates = []
    for entry in data.get("entries", []):
        if entry.get("migration_status") != args.migration_status:
            continue
        if knot and entry.get("legacy_interpretation", {}).get("knot_primary") != knot:
            continue
        if seed and seed not in {
            relation.get("seed_id")
            for relation in entry.get("seed_relations", [])
            if isinstance(relation, dict)
        }:
            continue
        if needle and needle not in text(entry):
            continue
        candidates.append(
            {
                "id": entry["id"],
                "paper": entry["paper"]["legacy_citation"],
                "original_blueprint": entry["original_blueprint"],
                "legacy_interpretation": entry["legacy_interpretation"],
                "research_profile": entry["research_profile"],
                "migration_status": entry["migration_status"],
                "runtime_eligibility": "no",
                "next_action": next_action(entry),
            }
        )
        if len(candidates) >= max(args.limit, 0):
            break
    print(json.dumps({"discovery_only": True, "candidates": candidates}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
