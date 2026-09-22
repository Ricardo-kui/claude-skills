#!/usr/bin/env python3
"""Verify evidence quotes from toc-review branch records against the manuscript.

Usage:
    python verify_quotes.py <manuscript.md> <records.json> [--out annotated.json]

<records.json> accepts either the merged list of surviving nodes, or the
merged branch-return structure {"branch": ..., "nodes": [...]} (a list of
those is fine too). Each node must carry node["claim"]["evidence_quote"].

Verified quote slots (every quote that can influence moderator/Panel verdicts):
  - claim.evidence_quote        — the skeptic's grounding quote (required)
  - advocate.citation_quote     — the author's counter-quote. Verified when
                                  present; a non-acknowledging advocate with
                                  no citation_quote is an ungrounded deflection
                                  and counts as failed. (Per protocol the
                                  revision stage carries no new quotes.)

Matching normalizes case, whitespace runs, curly quotes, and dash variants on
both sides, then tests substring containment. A quote containing an ellipsis
(…) or "[...]" fails — the debate protocol requires continuous verbatim quotes.

Output: JSON with per-node evidence_verified, citation_verified, and
panel_blocked (true when any verdict-relevant quote failed — such nodes must
not enter Panel). Summary lines go to stderr.

Exit codes (fail-closed):
  0  nodes were found and every verdict-relevant quote verified
  1  at least one quote failed or one node is panel_blocked
  2  no nodes found, or usage/IO error
"""

import argparse
import json
import re
import sys

TRANSLATIONS = str.maketrans({
    "\u2018": "'", "\u2019": "'",
    "\u201c": '"', "\u201d": '"',
    "\u2013": "-", "\u2014": "-", "\u2212": "-",
    "\u00a0": " ",
})


def normalize(text: str) -> str:
    text = text.translate(TRANSLATIONS).casefold()
    text = re.sub(r"\s+", " ", text).strip()
    return text


def has_ellipsis(quote: str) -> bool:
    return "…" in quote or "[...]" in quote.lower() or "..." in quote


def iter_nodes(records):
    if isinstance(records, dict) and "nodes" in records:
        records = [records]
    if isinstance(records, list):
        for item in records:
            if isinstance(item, dict) and "nodes" in item:
                yield from item["nodes"]
            elif isinstance(item, dict):
                yield item
    else:
        raise ValueError("records.json must be a node list or branch-return structure")


def check_quote(quote, manuscript_norm, manuscript_nospace):
    """Return (ok, note). note is None on success."""
    if has_ellipsis(quote):
        return False, "ellipsis in quote (continuous verbatim required)"
    q_norm = normalize(quote)
    ok = q_norm in manuscript_norm or q_norm.replace(" ", "") in manuscript_nospace
    return ok, None if ok else "no normalized substring match"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("manuscript")
    ap.add_argument("records")
    ap.add_argument("--out", default=None, help="write annotated records here (default: stdout)")
    args = ap.parse_args()

    with open(args.manuscript, encoding="utf-8-sig", errors="replace") as f:
        manuscript_norm = normalize(f.read())
        manuscript_nospace = manuscript_norm.replace(" ", "")

    with open(args.records, encoding="utf-8-sig") as f:
        data = json.load(f)

    claim_stats = [0, 0, 0]      # verified, failed, empty
    citation_stats = [0, 0, 0]   # verified, failed, skipped
    blocked = 0
    node_count = 0

    for node in iter_nodes(data):
        node_count += 1
        node_bad = False

        # --- claim.evidence_quote (required) ---
        claim = node.get("claim", {})
        quote = claim.get("evidence_quote", "")
        if not quote or not quote.strip():
            node["evidence_verified"] = False
            node["evidence_note"] = "empty quote"
            claim_stats[2] += 1
            node_bad = True
        else:
            ok, note = check_quote(quote, manuscript_norm, manuscript_nospace)
            node["evidence_verified"] = bool(ok)
            if ok:
                claim_stats[0] += 1
            else:
                claim_stats[1] += 1
                node["evidence_note"] = note
                node_bad = True

        # --- advocate.citation_quote (verdict-relevant when deflecting) ---
        advocate = node.get("advocate")
        if isinstance(advocate, dict):
            citation = advocate.get("citation_quote", "")
            acknowledges = advocate.get("acknowledges")
            if isinstance(citation, str) and citation.strip():
                ok, note = check_quote(citation, manuscript_norm, manuscript_nospace)
                advocate["citation_verified"] = bool(ok)
                if ok:
                    citation_stats[0] += 1
                else:
                    citation_stats[1] += 1
                    advocate["citation_note"] = note
                    node_bad = True
            elif acknowledges is False:
                advocate["citation_verified"] = False
                advocate["citation_note"] = (
                    "non-acknowledging advocate must supply citation_quote "
                    "(ungrounded deflection)"
                )
                citation_stats[1] += 1
                node_bad = True
            else:
                citation_stats[2] += 1

        node["panel_blocked"] = bool(node_bad)
        if node_bad:
            blocked += 1

    payload = json.dumps(data, ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(payload)
    else:
        print(payload)

    cv, cf, ce = claim_stats
    av, af, askip = citation_stats
    print(f"claim quotes: verified {cv}/{cv + cf}" + (f", {ce} empty" if ce else ""), file=sys.stderr)
    print(
        f"advocate citations: verified {av}/{av + af}" + (f", {askip} skipped" if askip else ""),
        file=sys.stderr,
    )
    print(f"nodes: {node_count}, panel_blocked: {blocked}", file=sys.stderr)

    if node_count == 0:
        print("error: no nodes found in records (fail-closed)", file=sys.stderr)
        return 2
    return 0 if blocked == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
