#!/usr/bin/env python3
"""Verify evidence quotes from tod-debate records against their source papers.

Usage:
    python verify_quotes_tod.py --papers A=<pathA> B=<pathB> records.json [--out verified.json]

records.json holds the debate tree records; every object carrying quotes uses
a "paper" field ("A"|"B") alongside its "evidence_quotes" list. Accepts any
nesting: the script walks the JSON tree, finds dicts with evidence_quotes,
and verifies each quote against the named paper.

Matching normalizes case, whitespace runs, curly quotes, and dash variants,
then tests substring containment. A quote containing an ellipsis (…) or
"[...]" fails — the protocol requires continuous verbatim quotes.

Output: JSON copy of records with an added "verified" list per quoting object
(quote -> bool), a per-paper summary to stderr. Exit 0 whenever verification
ran; nonzero only on usage/IO errors.
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
    return re.sub(r"\s+", " ", text).strip()


def has_ellipsis(quote: str) -> bool:
    return "…" in quote or "[...]" in quote.lower() or "..." in quote


def walk(node, paper, found):
    """Collect dicts carrying evidence_quotes; paper key is inherited from
    enclosing dicts (records nest quotes inside claims/verdicts)."""
    if isinstance(node, dict):
        p = node.get("paper", paper)
        if isinstance(node.get("evidence_quotes"), list) and p:
            found.append((node, p))
        for value in node.values():
            walk(value, p, found)
    elif isinstance(node, list):
        for item in node:
            walk(item, paper, found)


def quote_text(q):
    if isinstance(q, dict):
        return q.get("quote", "")
    return q if isinstance(q, str) else ""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--papers", nargs="+", required=True,
                    help="paperId=path pairs, e.g. A=ms.md B=rival.md")
    ap.add_argument("records")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    papers = {}
    for spec in args.papers:
        key, _, path = spec.partition("=")
        if not key or not path:
            ap.error(f"--papers expects KEY=PATH, got {spec!r}")
        with open(path, encoding="utf-8-sig", errors="replace") as f:
            norm = normalize(f.read())
        papers[key] = (norm, norm.replace(" ", ""))

    with open(args.records, encoding="utf-8-sig") as f:
        data = json.load(f)

    quoting = []
    walk(data, None, quoting)

    per_paper = {key: [0, 0] for key in papers}  # verified, total
    for node, paper_key in quoting:
        results = []
        for q in node.get("evidence_quotes", []):
            text = quote_text(q)
            ok = False
            note = None
            if text.strip() and paper_key in papers:
                if has_ellipsis(text):
                    note = "ellipsis in quote (continuous verbatim required)"
                else:
                    qn = normalize(text)
                    ms_norm, ms_nospace = papers[paper_key]
                    ok = qn in ms_norm or qn.replace(" ", "") in ms_nospace
            elif paper_key not in papers:
                note = f"unknown paper key {paper_key!r}"
            else:
                note = "empty quote"
            if isinstance(q, dict):
                q["verified"] = bool(ok)
                if note:
                    q["verify_note"] = note
            results.append(ok)
            stats = per_paper.get(paper_key)
            if stats:
                stats[1] += 1
                stats[0] += int(ok)
        node["quotes_verified"] = all(results) if results else False

    payload = json.dumps(data, ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(payload)
    else:
        print(payload)

    for key, (ok, total) in per_paper.items():
        print(f"paper {key}: verified {ok}/{total} quotes", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
