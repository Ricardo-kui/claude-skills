"""Retrieve current-run learning objects from a v0.4-lite catalog.

Retrieval policy (see references/retrieval-contract.md — 1 primary + 1 contrast,
four required fields per result):

- `card.requires` is a RANKING PENALTY, never a hard gate. Each unmet required
  condition pushes a card down the ranking; it does not eliminate it.
- When `request.validated_conditions` is empty/absent the validation state is
  `unknown` (not "no conditions validated"), so cards with requirements remain
  eligible and are annotated with their unmet conditions.
- Tiers are a fixed, auditable fallback ladder, tried in order until a tier
  yields at least one candidate:
    tier 1  : suitable == "yes"; when the request declares retrieval_signals a
              retrieval_signals intersection is required, otherwise a
              narrative_dynamics / theoretical_problem_form hit is required.
    tier 2a : ignore the retrieval_signals requirement; keep a
              narrative_dynamics / theoretical_problem_form hit.
    tier 2b : additionally relax suitable to "partial".
    tier 2c : additionally drop the tag requirement; same outlet or paper_type.
  Every result is annotated with its tier, the rules relaxed, and the signals
  that matched. `--explain` reports per-gate elimination counts and each
  returned card's unmet conditions; an empty result always carries a reason.

- Request and card tags are first passed through the hand-curated synonym table
  at `references/tag-normalization.yaml`, then exactly intersected. This
  reconciles word-level spelling drift (e.g. request
  `cross-audience-partial-incommensurability` vs card
  `cross-audience-partial-criterion-overlap`). The table is a plain word list:
  no embedding, no semantic model, no substring matching.
- Degenerate-tier guardrail: if a tier's candidate set is non-empty but EVERY
  candidate both (a) lacks a `theoretical_problem_form` hit and (b) carries
  >=1 unmet required condition, that tier is not allowed to lock the outcome.
  Retrieval continues down the ladder; only if no tier produces a
  non-degenerate candidate is the last degenerate tier returned, marked
  `low_confidence` with a stated reason.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CATALOG = ROOT / "v4" / "catalog.json"
DEFAULT_TAG_NORMALIZATION = ROOT / "references" / "tag-normalization.yaml"

SECTIONS = ("introduction", "theory", "methods", "results", "discussion")
UNMET_PENALTY = 15

# cumulatively-relaxed fallback ladder, in fixed order.
TIER_SPEC: dict[str, dict] = {
    "1": {"allow_partial": False, "relevance": "strict"},
    "2a": {"allow_partial": False, "relevance": "tags"},
    "2b": {"allow_partial": True, "relevance": "tags"},
    "2c": {"allow_partial": True, "relevance": "same-class"},
}
TIER_RELAXED: dict[str, list[str]] = {
    "1": [],
    "2a": ["retrieval_signals"],
    "2b": ["retrieval_signals", "suitable<=partial"],
    "2c": ["retrieval_signals", "suitable<=partial", "relevance>=outlet+paper_type"],
}


def load_tag_normalization(path: Path) -> dict[str, str]:
    """Build a surface->canonical map from the auditable synonym table."""
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    mapping: dict[str, str] = {}
    for group in data.get("groups", []) or []:
        canonical = group.get("canonical")
        if not canonical:
            continue
        for surface in group.get("surfaces", []) or []:
            mapping[surface] = canonical
    return mapping


def normalize_tags(tags: list[str] | None, norm: dict[str, str]) -> list[str]:
    return [norm.get(tag, tag) for tag in (tags or [])]


def intersect(left: list[str], right: list[str], norm: dict[str, str]) -> list[str]:
    left_norm = normalize_tags(left, norm)
    right_norm = normalize_tags(right, norm)
    return sorted(set(left_norm) & set(right_norm))


def card_facts(card: dict, request: dict, norm: dict[str, str]) -> dict:
    section = request["section"]
    learning = card.get("section_learning", {}).get(section, {})
    requires = list(learning.get("requires", []) or [])
    validated_raw = request.get("validated_conditions")
    validation = "known" if isinstance(validated_raw, list) and validated_raw else "unknown"
    validated = set(validated_raw or [])
    # Under `unknown` every declared requirement is unverified, so it counts as
    # unmet for ranking (conservative: more requirements rank lower).
    unmet = [condition for condition in requires if condition not in validated]
    return {
        "id": card.get("id"),
        "suitable": learning.get("suitable"),
        "requires": requires,
        "validation": validation,
        "unmet_conditions": unmet,
        "overall_role": card.get("overall_role"),
        "paper_type": card.get("paper_type"),
        "outlet": card.get("outlet"),
        "declares_signals": bool(card.get("retrieval_signals")),
        "hits": {
            "retrieval_signals": intersect(request.get("retrieval_signals"), card.get("retrieval_signals"), norm),
            "narrative_dynamics": intersect(request.get("story_needs"), card.get("narrative_dynamics"), norm),
            "theoretical_problem_form": intersect(request.get("theoretical_problem_form"), card.get("theoretical_problem_form"), norm),
        },
    }


def tier_admits(facts: dict, request: dict, tier: str) -> bool:
    spec = TIER_SPEC[tier]
    if facts["overall_role"] == "cautionary_case":
        return False
    if facts["suitable"] is None:
        return False
    if not spec["allow_partial"] and facts["suitable"] != "yes":
        return False
    tag_hit = bool(facts["hits"]["narrative_dynamics"] or facts["hits"]["theoretical_problem_form"])
    if spec["relevance"] == "strict":
        # at least one positive soft relevance match, so a broadly useful card is
        # not injected into an unrelated writing call. When the request declares
        # retrieval_signals those take precedence; otherwise fall back to tags.
        if request.get("retrieval_signals"):
            return bool(facts["hits"]["retrieval_signals"])
        return tag_hit
    if spec["relevance"] == "tags":
        return tag_hit
    # same-class
    same_type = bool(request.get("paper_type")) and facts["paper_type"] == request.get("paper_type")
    same_outlet = bool(request.get("outlet")) and facts["outlet"] == request.get("outlet")
    return same_type or same_outlet


def score(facts: dict, card: dict, request: dict) -> int:
    value = 35 if facts["suitable"] == "yes" else 15
    if request.get("paper_type") and card.get("paper_type") == request["paper_type"]:
        value += 20
    value += min(30, 10 * len(facts["hits"]["narrative_dynamics"]))
    value += min(10, 5 * len(facts["hits"]["theoretical_problem_form"]))
    value += min(20, 10 * len(facts["hits"]["retrieval_signals"]))
    if card.get("publication_status") == "published":
        value += 5
    if card.get("coverage") == "complete":
        value += 5
    value -= UNMET_PENALTY * len(facts["unmet_conditions"])
    return value


def build_explain(catalog_cards, request, tier_attempts, returned, norm: dict[str, str]):
    cautionary = sum(1 for c in catalog_cards if c.get("overall_role") == "cautionary_case")

    def facts_of(card):
        return card_facts(card, request, norm)

    eliminated_suitable = sum(
        1 for c in catalog_cards
        if c.get("overall_role") != "cautionary_case" and facts_of(c)["suitable"] != "yes"
    )
    if request.get("retrieval_signals"):
        eliminated_soft = sum(
            1 for c in catalog_cards
            if c.get("overall_role") != "cautionary_case"
            and facts_of(c)["suitable"] == "yes"
            and not facts_of(c)["hits"]["retrieval_signals"]
        )
    else:
        eliminated_soft = sum(
            1 for c in catalog_cards
            if c.get("overall_role") != "cautionary_case"
            and facts_of(c)["suitable"] == "yes"
            and not facts_of(c)["hits"]["narrative_dynamics"]
            and not facts_of(c)["hits"]["theoretical_problem_form"]
        )
    unmet_ranked = sum(
        1 for c in catalog_cards
        if c.get("overall_role") != "cautionary_case" and facts_of(c)["unmet_conditions"]
    )
    return {
        "gate_eliminations": {
            "cautionary_case": cautionary,
            "suitable_not_yes_tier1": eliminated_suitable,
            "relevance_no_match_tier1": eliminated_soft,
        },
        "requires_unmet_but_ranked": unmet_ranked,
        "validation": "known" if request.get("validated_conditions") else "unknown",
        "tier_attempts": tier_attempts,
        "returned_unmet_conditions": {r["id"]: r["unmet_conditions"] for r in returned},
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True, type=Path)
    parser.add_argument("--catalog", default=DEFAULT_CATALOG, type=Path)
    parser.add_argument("--tag-normalization", default=DEFAULT_TAG_NORMALIZATION, type=Path,
                        help="hand-curated synonym table applied to both request and card tags")
    parser.add_argument("--explain", action="store_true",
                        help="report per-gate elimination counts and returned unmet conditions")
    args = parser.parse_args()
    request = json.loads(args.request.read_text(encoding="utf-8"))
    norm = load_tag_normalization(args.tag_normalization)
    if request.get("section") not in SECTIONS:
        raise SystemExit("request.section is required and invalid")
    catalog = json.loads(args.catalog.read_text(encoding="utf-8")) if args.catalog.exists() else {"cards": []}
    cards = catalog.get("cards", [])

    tier_attempts = []
    ranked: list[tuple[int, str, dict, dict]] = []
    winning_tier = None
    degenerate_fallback: tuple[str, list[tuple[int, str, dict, dict]]] | None = None
    for tier in TIER_SPEC:
        admitted = []
        for card in cards:
            facts = card_facts(card, request, norm)
            if tier_admits(facts, request, tier):
                admitted.append((score(facts, card, request), card.get("id", ""), card, facts))
        if not admitted:
            tier_attempts.append({"tier": tier, "candidates": 0})
            continue
        # Degenerate-tier guardrail: a tier whose only candidates are generic
        # (no theoretical_problem_form hit) AND unverified (unmet >= 1) must not
        # lock the outcome. Keep looking down the ladder; if nothing better
        # exists, fall back to the last degenerate tier with low_confidence.
        all_degenerate = all(
            (not facts["hits"]["theoretical_problem_form"]) and len(facts["unmet_conditions"]) >= 1
            for _s, _cid, _card, facts in admitted
        )
        if all_degenerate:
            tier_attempts.append({
                "tier": tier,
                "candidates": len(admitted),
                "degenerate": True,
                "skipped": True,
                "reason": "all candidates lack a theoretical_problem_form hit and carry unmet_conditions>=1",
            })
            degenerate_fallback = (tier, admitted)
            continue
        tier_attempts.append({"tier": tier, "candidates": len(admitted)})
        ranked = admitted
        winning_tier = tier
        break

    low_confidence = False
    low_confidence_reason = None
    if not ranked and degenerate_fallback is not None:
        winning_tier, ranked = degenerate_fallback
        low_confidence = True
        low_confidence_reason = (
            "no tier produced a non-degenerate candidate; returning tier "
            f"{winning_tier} marked low_confidence because every candidate lacks a "
            "theoretical_problem_form hit and carries unmet_conditions>=1"
        )

    ranked.sort(key=lambda item: (-item[0], item[1]))
    max_results = min(max(int(request.get("max_results", 2)), 0), 2)
    results = []
    seen_dynamics: set[str] = set()
    for value, _cid, card, facts in ranked:
        dynamics = set(card.get("narrative_dynamics", []))
        if results and dynamics and dynamics <= seen_dynamics:
            continue
        learning = card["section_learning"][request["section"]]
        reason_bits = [f"suitable={facts['suitable']}", f"tier={winning_tier}"]
        for key, tags in facts["hits"].items():
            if tags:
                reason_bits.append(f"{key}={tags}")
        if facts["unmet_conditions"]:
            reason_bits.append(f"unmet={facts['unmet_conditions']}")
        if low_confidence:
            reason_bits.append("low_confidence=true")
        result = {
            "id": card.get("id"),
            "path": card.get("path"),
            "score": value,
            "tier": winning_tier,
            "relaxed": TIER_RELAXED[winning_tier],
            "signals_hit": facts["hits"],
            "suitable": learning.get("suitable"),
            "requires": learning.get("requires", []),
            "validation": facts["validation"],
            "unmet_conditions": facts["unmet_conditions"],
            "low_confidence": low_confidence,
            "matching_reason": "; ".join(reason_bits),
            "learn": learning.get("learn", [])[:2],
            "caveat": learning.get("caveat", [])[:1],
        }
        if low_confidence:
            result["low_confidence_reason"] = low_confidence_reason
        results.append(result)
        seen_dynamics |= dynamics
        if len(results) == max_results:
            break
    payload: dict = {"request": request, "results": results}
    if not results:
        payload["no_match"] = (
            "no credible exemplar: tier 1/2a/2b/2c all empty "
            f"(validation={('known' if request.get('validated_conditions') else 'unknown')})"
        )
    if args.explain:
        payload["explain"] = build_explain(cards, request, tier_attempts, results, norm)

    # fitness 台账（第 4 项，2026-09-14）：检索命中落账（fail-open，遥测永不
    # 阻塞写作流）。resolve 先解析 junction 到 claude-skills 真身再拼路径，
    # 三根 skills 调用路径下均确定性。
    try:
        _ds = Path(__file__).resolve().parents[1].parent / "distill-paper-exemplar" / "scripts"
        if str(_ds) not in sys.path:
            sys.path.insert(0, str(_ds))
        from fitness_ledger import append_event
        append_event("retrieval", {
            "section": request.get("section"),
            "paper_type": request.get("paper_type") or "",
            "story_needs": list(request.get("story_needs") or [])[:8],
            "signals": list(request.get("retrieval_signals") or [])[:12],
            "returned": [{"id": r.get("id"), "score": r.get("score")}
                         for r in results],
            "n_results": len(results), "empty": not results,
        })
    except Exception as e:  # noqa: BLE001 — 遥测失败不影响检索输出
        print(f"WARN: fitness 检索落账失败（不影响输出）：{e}", file=sys.stderr)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
