#!/usr/bin/env python3
"""Verify evidence quotes from toc-review branch records against the manuscript.

Usage:
    python verify_quotes.py <manuscript.md> <records.json> [--out annotated.json]

<records.json> accepts either the merged list of surviving nodes, or the
merged branch-return structure {"branch": ..., "nodes": [...]} (a list of
those is fine too). Each node must carry node["claim"]["evidence_quote"].

Matching normalizes case, whitespace runs, curly quotes, and dash variants on
both sides, then tests substring containment. A quote containing an ellipsis
(…) or "[...]" fails — the debate protocol requires continuous verbatim quotes.

Output: JSON with per-node evidence_verified plus a summary line to stderr.
Exit code is 0 even when some quotes fail (verification ran); nonzero only on
usage/IO errors.
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

    verified, failed, empty = 0, 0, 0
    for node in iter_nodes(data):
        claim = node.get("claim", {})
        quote = claim.get("evidence_quote", "")
        if not quote or not quote.strip():
            node["evidence_verified"] = False
            node["evidence_note"] = "empty quote"
            empty += 1
            continue
        note = None
        if has_ellipsis(quote):
            ok = False
            note = "ellipsis in quote (continuous verbatim required)"
        else:
            q_norm = normalize(quote)
            ok = q_norm in manuscript_norm or q_norm.replace(" ", "") in manuscript_nospace
        node["evidence_verified"] = bool(ok)
        if ok:
            verified += 1
        else:
            failed += 1
            node["evidence_note"] = note or "no normalized substring match"

    payload = json.dumps(data, ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(payload)
    else:
        print(payload)

    total = verified + failed
    print(
        f"verified {verified}/{total} quotes"
        + (f", {empty} empty quotes skipped" if empty else ""),
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
