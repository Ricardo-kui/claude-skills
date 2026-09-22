#!/usr/bin/env python3
"""Verify evidence quotes from tod-debate records against their source papers.

Usage:
    python verify_quotes_tod.py --paper A=<pathA> --paper B=<pathB> records.json [--out verified.json]

(Deprecated alias: `--papers A=... B=...` — its nargs="+" swallows trailing
positionals, so records.json must precede it; prefer repeatable --paper.)

records.json holds the debate tree records. Recognized quote containers:

  1. dicts carrying an "evidence_quotes" list. The paper key comes from the
     dict's own "paper" field (root claims), or is inherited from an ancestor
     "paper" field, or from an ancestor map key that is itself a known paper
     key — rounds store stage output as {"present": {"A": {...}, "B": {...}}}.
  2. leaf-verdict style fields "evidence_A" / "evidence_B" / ... — the
     suffix is the paper key; entries may be plain strings or {"quote": ...}.

Matching normalizes case, whitespace runs, curly quotes, and dash variants,
then tests substring containment. A quote containing an ellipsis (…) or
"[...]" fails — the protocol requires continuous verbatim quotes.

Output: JSON copy of records annotated per container — dict quote entries get
"verified"/"verify_note"; every container gets "<field>_all_verified" plus a
per-entry "<field>_verified" list; "evidence_quotes" containers also keep the
legacy "quotes_verified" flag. Per-paper stats go to stderr.

Exit codes (fail-closed):
  0  quotes were found and all verified
  1  at least one quote failed (no match / empty / ellipsis / unknown paper)
  2  no quotes found, or usage/IO error
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

EVIDENCE_PREFIX = "evidence_"


def normalize(text: str) -> str:
    text = text.translate(TRANSLATIONS).casefold()
    return re.sub(r"\s+", " ", text).strip()


def has_ellipsis(quote: str) -> bool:
    return "…" in quote or "[...]" in quote.lower() or "..." in quote


def walk(node, paper, found, paper_keys):
    """Collect (dict, field, paper_key) quoting containers.

    Paper context is inherited from an enclosing "paper" field or from an
    ancestor map key that is a known paper key (rounds.present.A etc.).
    """
    if isinstance(node, dict):
        p = node.get("paper", paper)
        if isinstance(node.get("evidence_quotes"), list) and p:
            found.append((node, "evidence_quotes", p))
        for key, value in node.items():
            if (
                isinstance(key, str)
                and key.startswith(EVIDENCE_PREFIX)
                and key != "evidence_quotes"
                and isinstance(value, list)
            ):
                suffix = key[len(EVIDENCE_PREFIX):]
                if suffix:
                    found.append((node, key, suffix))
        for key, value in node.items():
            child_paper = key if (isinstance(key, str) and key in paper_keys) else p
            walk(value, child_paper, found, paper_keys)
    elif isinstance(node, list):
        for item in node:
            walk(item, paper, found, paper_keys)


def quote_text(q):
    if isinstance(q, dict):
        return q.get("quote", "")
    return q if isinstance(q, str) else ""


def verify_field(node, field, paper_key, papers, per_paper):
    """Verify one quoting container in place; return True iff all passed."""
    results = []
    per_entry = []
    for q in node.get(field, []):
        text = quote_text(q)
        ok = False
        note = None
        if not text or not str(text).strip():
            note = "empty quote"
        elif paper_key not in papers:
            note = f"unknown paper key {paper_key!r}"
        elif has_ellipsis(text):
            note = "ellipsis in quote (continuous verbatim required)"
        else:
            qn = normalize(text)
            ms_norm, ms_nospace = papers[paper_key]
            ok = qn in ms_norm or qn.replace(" ", "") in ms_nospace
            if not ok:
                note = "no normalized substring match"
        if isinstance(q, dict):
            q["verified"] = bool(ok)
            if note and not ok:
                q["verify_note"] = note
        results.append(bool(ok))
        per_entry.append({"quote": text, "verified": bool(ok), **({"note": note} if note and not ok else {})})
        stats = per_paper.setdefault(paper_key, [0, 0])
        stats[1] += 1
        stats[0] += int(ok)
    node[f"{field}_verified"] = [r["verified"] for r in per_entry]
    node[f"{field}_all_verified"] = all(results) if results else False
    if field == "evidence_quotes":
        node["quotes_verified"] = node[f"{field}_all_verified"]
    return all(results) if results else False


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--paper", action="append", dest="paper_specs", metavar="KEY=PATH",
                    help="repeatable: --paper A=ms.md --paper B=rival.md")
    ap.add_argument("--papers", nargs="+", dest="paper_specs_multi",
                    help="deprecated alias for --paper (records.json must precede it)")
    ap.add_argument("records")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    specs = []
    if args.paper_specs:
        specs.extend(args.paper_specs)
    if args.paper_specs_multi:
        specs.extend(args.paper_specs_multi)
    if not specs:
        ap.error("at least one --paper KEY=PATH is required")

    papers = {}
    for spec in specs:
        key, _, path = spec.partition("=")
        if not key or not path:
            ap.error(f"--paper expects KEY=PATH, got {spec!r}")
        with open(path, encoding="utf-8-sig", errors="replace") as f:
            norm = normalize(f.read())
        papers[key] = (norm, norm.replace(" ", ""))

    with open(args.records, encoding="utf-8-sig") as f:
        data = json.load(f)

    quoting = []
    walk(data, None, quoting, set(papers))

    per_paper = {}
    all_ok = True
    for node, field, paper_key in quoting:
        if not verify_field(node, field, paper_key, papers, per_paper):
            all_ok = False

    payload = json.dumps(data, ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(payload)
    else:
        print(payload)

    for key in sorted(per_paper):
        ok, total = per_paper[key]
        print(f"paper {key}: verified {ok}/{total} quotes", file=sys.stderr)

    total_quotes = sum(t for _, t in per_paper.values())
    if total_quotes == 0:
        print("error: no evidence quotes found in records (fail-closed)", file=sys.stderr)
        return 2
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
