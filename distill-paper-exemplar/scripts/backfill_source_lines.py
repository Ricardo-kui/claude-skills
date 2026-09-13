#!/usr/bin/env python3
"""S3 legacy backfill, methods/results leg: deterministic source-line analysis.

Harvests `**来源**/**来源论文**/原文锚点` lines from unmarked blocks, parses
prose citations (surnames / year / journal tokens), and triple-checks each
against the registry papers universe (author tokens + year + journal token).
Classifies per block: HIGH (unique registry key, all checks pass), LOW
(ambiguous/no match -> human adjudication list), NONE (no source line).

REPORT-ONLY by default — minting (`--apply`) is gated on the 10% human
sampling review per plan S3.

Usage: py backfill_source_lines.py [--report out.yaml] [--apply]
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rebuild_views as rv  # noqa: E402  (scanner, alias engine, corpus keys)

ROOTS = {k: rv.SKILLS_ROOT / v for k, v in rv.CORPUS_KEYS.items()
         if k in ("methods", "results")}
SRC_RE = re.compile(r"\*\*(?:来源|来源论文|原文锚点|原文锚定|数据来源)\**\s*[:：]\s*(.+)$", re.M)
YEAR_RE = re.compile(r"(?<!\d)(\d{4})(?!\d)")

JOURNAL_TOKENS = {  # prose -> registry key token
    "management science": "ms", "strategic management journal": "smj",
    "academy of management journal": "amj", "administrative science quarterly": "asq",
    "organization science": "os", "journal of marketing": "jm",
    "journal of marketing research": "jmr", "marketing science": "mktsci",
    "journal of consumer research": "jcr", "journal of product innovation management": "jpim",
    "strategic organization": "so", "journal of operations management": "jom",
    "production and operations management": "pom", "journal of management": "jom2",
    "msom": "msom", "amj": "amj", "smj": "smj", "asq": "asq", "os": "os",
    "jm": "jm", "jmr": "jmr", "ms": "ms", "orsc": "orsc", "jams": "jams",
}


def parse_citation(prose: str) -> dict:
    """Prose citation -> {surnames, year, journal_token}."""
    s = prose.strip()
    year_m = YEAR_RE.search(s)
    year = year_m.group(1) if year_m else None
    # journal: parenthesized text or trailing known token
    journal = None
    for token, key in JOURNAL_TOKENS.items():
        if token in s.lower():
            journal = key
            break
    # surnames: first alpha word of each comma/&/and-separated segment,
    # taken from the part before the year/journal
    head = s[:year_m.start()] if year_m else s
    head = re.split(r"\(", head)[0]
    segs = re.split(r"\s*(?:&|,| and | 与 )\s*", head)
    surnames = []
    for seg in segs:
        w = re.match(r"([A-Za-z][A-Za-z\-']+)", seg.strip())
        if w and w.group(1).lower() not in ("et", "al", "the"):
            surnames.append(w.group(1).lower())
    return {"surnames": surnames, "year": year, "journal": journal}


def registry_universe(corpus: str, doc: dict) -> dict[str, dict]:
    """registry key -> {surnames, year, journal, files} (papers universe)."""
    uni: dict[str, dict] = {}

    def add(key: str, meta: dict | None = None):
        years = set(YEAR_IN_TOKENS(key))
        toks = set(re.findall(r"[a-z0-9]+", key.lower()))
        uni[key] = {"tokens": toks, "years": years,
                    "meta": meta or {}}

    def YEAR_IN_TOKENS(key):
        return rv.YEAR_IN_TOKEN_RE.findall(key)

    if corpus == "methods":
        ev = doc.get("evidence") or {}
        for pk, p in (ev.get("by_source_paper") or {}).items():
            if isinstance(p, dict):
                add(pk, p)
        for dk, d in (ev.get("by_design_type") or {}).items():
            if not isinstance(d, dict):
                continue
            for p in rv.flowlist(d.get("papers")):
                add(rv.strip_journal(p))
    elif corpus == "results":
        for ek, e in (doc.get("estimators") or {}).items():
            if not isinstance(e, dict):
                continue
            for s in (e.get("slots") or {}).values():
                if not isinstance(s, dict):
                    continue
                for v in (s.get("skeleton_variants") or []):
                    if isinstance(v, dict):
                        for src in rv.flowlist(v.get("sources")):
                            add(rv.strip_journal(src))
    return uni


def match_citation(cit: dict, uni: dict[str, dict]) -> list[str]:
    """Triple check (surnames + year + journal) -> matching registry keys."""
    hits = []
    for key, info in uni.items():
        if cit["year"] and info["years"] and cit["year"] not in info["years"]:
            continue
        toks = info["tokens"]
        if cit["surnames"]:
            hit = sum(1 for s in cit["surnames"] if s in toks)
            if hit < min(2, len(cit["surnames"])) and \
                    not (len(cit["surnames"]) == 1 and hit == 1):
                continue
        if cit["journal"] and cit["journal"] not in toks:
            continue
        hits.append(key)
    return hits


def analyze(corpus: str) -> dict:
    root = ROOTS[corpus]
    reg = root / "_evidence_registry.yaml"
    doc = yaml.safe_load(reg.read_bytes().decode("utf-8"))
    uni = registry_universe(corpus, doc)
    scan = rv.scan_corpus(root)
    out = {"blocks": [], "summary": {}}
    verdicts = Counter()
    for b in scan.all_blocks():
        if b.wb:
            continue
        body = "\n".join((root / b.rel).read_text(encoding="utf-8")
                         .split("\n")[b.start:b.end])
        srcs = SRC_RE.findall(body)
        if not srcs:
            continue
        votes: Counter = Counter()
        lines_detail = []
        for ln in srcs:
            cit = parse_citation(ln)
            if not cit["surnames"] and not cit["year"]:
                lines_detail.append({"line": ln[:80], "parses": False})
                continue
            hits = match_citation(cit, uni)
            for h in hits:
                votes[h] += 1
            lines_detail.append({"line": ln[:80], "citation": cit, "hits": hits})
        if not votes:
            verdict = "LOW"
        else:
            best, n = votes.most_common(1)[0]
            tied = [k for k, c in votes.items() if c == n]
            verdict = "HIGH" if len(tied) == 1 and n >= 1 else "LOW"
        verdicts[verdict] += 1
        out["blocks"].append({
            "file": b.rel, "heading": b.heading[:70], "verdict": verdict,
            "candidate": votes.most_common(1)[0][0] if votes else None,
            "votes": dict(votes.most_common(3)), "lines": lines_detail})
    out["summary"] = {"unmarked_blocks_with_source": len(out["blocks"]),
                      **dict(verdicts)}
    return out


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass
    report = {}
    for corpus in ROOTS:
        report[corpus] = analyze(corpus)
        s = report[corpus]["summary"]
        print(f"[{corpus}] {s}")
    out = Path.home() / ".claude" / "distill-work" / "rebuild_views" / \
        "backfill_source_lines_report.yaml"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(yaml.safe_dump(report, allow_unicode=True, sort_keys=False,
                                  width=100), encoding="utf-8")
    print(f"report -> {out}  (report-only; minting gated on 10% human sampling)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
