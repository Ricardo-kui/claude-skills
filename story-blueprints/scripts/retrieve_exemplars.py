"""Retrieve current-run learning objects from a v0.4-lite catalog."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CATALOG = ROOT / "v4" / "catalog.json"


def overlap(left: list[str], right: list[str]) -> int:
    return len(set(left or []) & set(right or []))


def score(card: dict, request: dict) -> int | None:
    section = request["section"]
    learning = card.get("section_learning", {}).get(section, {})
    suitability = learning.get("suitable")
    if suitability not in {"yes", "partial"}:
        return None
    required_conditions = set(learning.get("requires", []))
    validated_conditions = set(request.get("validated_conditions", []))
    if not required_conditions.issubset(validated_conditions):
        return None
    if card.get("overall_role") == "cautionary_case":
        return None
    story_overlap = overlap(request.get("story_needs", []), card.get("narrative_dynamics", []))
    problem_overlap = overlap(request.get("theoretical_problem_form", []), card.get("theoretical_problem_form", []))
    signal_overlap = overlap(request.get("retrieval_signals", []), card.get("retrieval_signals", []))
    if card.get("retrieval_signals") and not (story_overlap or problem_overlap or signal_overlap):
        return None
    value = 35 if suitability == "yes" else 15
    if request.get("paper_type") and card.get("paper_type") == request["paper_type"]:
        value += 20
    value += min(30, 10 * story_overlap)
    value += min(10, 5 * problem_overlap)
    value += min(20, 10 * signal_overlap)
    if card.get("publication_status") == "published":
        value += 5
    if card.get("coverage") == "complete":
        value += 5
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True, type=Path)
    parser.add_argument("--catalog", default=DEFAULT_CATALOG, type=Path)
    args = parser.parse_args()
    request = json.loads(args.request.read_text(encoding="utf-8"))
    if request.get("section") not in {"introduction", "theory", "methods", "results", "discussion"}:
        raise SystemExit("request.section is required and invalid")
    catalog = json.loads(args.catalog.read_text(encoding="utf-8")) if args.catalog.exists() else {"cards": []}
    ranked = []
    for card in catalog.get("cards", []):
        value = score(card, request)
        if value is not None:
            ranked.append((value, card))
    ranked.sort(key=lambda item: (-item[0], item[1].get("id", "")))
    max_results = min(max(int(request.get("max_results", 2)), 0), 2)
    results = []
    seen_dynamics: set[str] = set()
    for value, card in ranked:
        dynamics = set(card.get("narrative_dynamics", []))
        if results and dynamics and dynamics <= seen_dynamics:
            continue
        learning = card["section_learning"][request["section"]]
        results.append({
            "id": card.get("id"),
            "path": card.get("path"),
            "score": value,
            "suitable": learning.get("suitable"),
            "requires": learning.get("requires", []),
            "learn": learning.get("learn", [])[:2],
            "caveat": learning.get("caveat", [])[:1],
        })
        seen_dynamics |= dynamics
        if len(results) == max_results:
            break
    print(json.dumps({"request": request, "results": results}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
