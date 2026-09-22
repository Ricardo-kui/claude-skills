#!/usr/bin/env python3
"""Recall probe generator v1 — metric-contract §试点判据 阶段②.

Builds paired probe docs from real exemplar sentences (story-blueprints
sentences archives) with minimal contract-violating mutations, plus
unmutated controls. Expected outcomes are derived from the contract rule
table (design_allowance), NOT hand-waved.

Classes:
  M1  statless "is associated with" -> "causes"          expect OVERCLAIM  (T_DEFINITIVE forbidden, all designs except experiment)
  M2a statless "is associated with" -> "increases/reduces" expect CONDITION_MISSING (T_DIRECTIONAL conditional; doc markerless & statless)
  M2b stats-bearing "is associated with" -> "increases/reduces" expect PASS (conditional satisfied by RESULT_MARKERS)
  M3  "we find that" -> "we reveal that"                 expect OVERCLAIM
  M4  discussion: "may/might/could cause/drive" -> modal stripped expect OVERCLAIM (discussion_mechanism)
  M5  stats-bearing: "X is associated with" -> "X may be associated with" expect UNDERCLAIM (tentative + STAT_HARD)
  M6  statless markerless "the effect of ... on ..." in did doc expect CONDITION_MISSING; identical doc under ols_fe expect PASS

Each probe has an unmutated control twin (same doc skeleton); a control
with any flag invalidates the pair (context contamination).

Deterministic: random.seed(20260921). Regenerate: delete tests/probes_v1/ first.
"""
from __future__ import annotations

import json
import random
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).parent
PKG = HERE.parent
SOURCES = Path(r"C:/Users/admin/.claude/skills/story-blueprints/v4/rhetoric-moves/sources")
OUT = HERE / "probes_v1"
WL = json.loads((PKG / "wordlists-v1.json").read_text(encoding="utf-8"))

LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
ID_MARKERS = WL["identification_markers"]
HYP_MARKERS = WL["hypothesis_markers"]
TIER_PATS = [p for pats in WL["verb_tiers"].values() for p in pats]
TENT_PATS = WL["tentative"] + [r"\b(may|might|could)\b"]
RESULT_MARKER = re.compile(
    r"(\bcoefficient\b|\bp[\s-]?value|β|\bbeta\b|\bstandard error|\bconfidence interval|\bCI\b"
    r"|\bmodel\s+\d|\bcolumn\s*\d|\btable\s*\d|\bfigure\s*\d|\bsignificant|\bmarginally\b"
    r"|\bp\s*[<=]\s*0?\.?\d|\bstatistically|\bwe\s+find|\bwe\s+observe|\bH\d"
    r"|\bstandard deviation\b)", re.I)
STAT_HARD = re.compile(r"(\bcoefficient\b|\bp[\s-]?value|β|\btable\s*\d|\bmodel\s+\d|\bcolumn\s*\d|\bsignificant|\bp\s*[<=]\s*0?\.?\d)")
DEG_ADJ = {"higher", "lower", "more", "fewer", "less", "greater", "increased",
           "decreased", "reduced", "improved", "worse", "better", "significant",
           "marginally", "substantially", "considerably"}

def clean(s: str) -> str:
    s = LINK.sub(r"\1", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def has(pat_list, s):
    return any(re.search(p, s, re.I) for p in pat_list)

def id_free(s: str) -> bool:
    return not any(re.search(m, s, re.I) for m in ID_MARKERS)

def load_sections(p: Path) -> dict[str, list[str]]:
    txt = p.read_text(encoding="utf-8", errors="replace")
    txt = re.sub(r"^---\n.*?\n---\n", "", txt, flags=re.S)
    out: dict[str, list[str]] = {}
    cur = None
    for line in txt.split("\n"):
        st = line.strip()
        if st.startswith("## "):
            cur = st[3:].strip().lower()
            out.setdefault(cur, [])
        elif cur and st and not st.startswith("<!--") and not st.startswith(("#", "|", "!", "`", "-", "---", "<")):
            out[cur].append(clean(st))
    return out

def neutral_filler(s: str) -> bool:
    return (60 < len(s) < 260 and "?" not in s
            and not has(TIER_PATS, s) and not has(TENT_PATS, s)
            and not RESULT_MARKER.search(s) and id_free(s)
            and not has(HYP_MARKERS, s) and not s.startswith(("However,", "Moreover,")))

def main() -> int:
    random.seed(20260921)
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    pools = {"assoc_statless": [], "assoc_stats": [], "we_find": [],
             "modal_cause": [], "effect_of": []}
    fillers: list[str] = []
    per_paper_fillers: dict[str, list[str]] = {}

    for p in sorted(SOURCES.glob("*.sentences.md")):
        key = p.stem
        secs = load_sections(p)
        res = secs.get("results", [])
        ppf = [s for s in res if neutral_filler(s)]
        per_paper_fillers[key] = ppf
        fillers.extend(ppf[:3])
        for s in res:
            if not (60 < len(s) < 400) or "?" in s or has(HYP_MARKERS, s) or not id_free(s):
                continue
            if "is associated with" in s.lower():
                if STAT_HARD.search(s) or RESULT_MARKER.search(s):
                    pools["assoc_stats"].append((key, s))
                else:
                    pools["assoc_statless"].append((key, s))
            if re.search(r"\bwe find that\b", s, re.I):
                pools["we_find"].append((key, s))
            m = re.search(r"\bthe effect of\b.{1,80}\bon\b", s, re.I)
            if m and not STAT_HARD.search(s) and not RESULT_MARKER.search(s) and id_free(s):
                # exclude sentences carrying other tier hits beyond T_CAUSAL_EFFECT
                rest = [t for t in WL["verb_tiers"] if t != "T_CAUSAL_EFFECT"
                        and any(re.search(pp, s, re.I) for pp in WL["verb_tiers"][t])]
                if not rest:
                    pools["effect_of"].append((key, s))
        for s in secs.get("discussion", []):
            pass
        # M4 pool from all sections (placed in Discussion doc; rule is section-scoped)
        for sec, sents in secs.items():
            for s in sents:
                if not (60 < len(s) < 400) or "?" in s or has(HYP_MARKERS, s):
                    continue
                if re.search(r"\b(may|might|could)\s+(cause|drive)\b", s, re.I):
                    # discussion-branch suppressions must not pre-exist
                    if (not has(WL["tentative"] + [r"\bsuggests?\b", r"\bappears?\b", r"\bseems?\b"], s)
                            and not re.search(r"\b(we found|we find|our finding|our results?|consistent with)\b", s, re.I)
                            and not re.search(r"\b(literature has|prior (research|studies|work)|studies have|existing studies|previous (research|studies|work))\b", s, re.I)):
                        pools["modal_cause"].append((key, s))

    def dedup(pool):
        seen, out = set(), []
        for k, s in pool:
            if s[:80] not in seen:
                seen.add(s[:80])
                out.append((k, s))
        return out

    for k in pools:
        pools[k] = dedup(pools[k])

    random.shuffle(pools["assoc_statless"])
    random.shuffle(pools["assoc_stats"])
    random.shuffle(pools["we_find"])
    random.shuffle(pools["modal_cause"])
    random.shuffle(pools["effect_of"])

    m1_pool, m2a_pool = pools["assoc_statless"][:12], pools["assoc_statless"][12:21]
    m2b_pool, m5_pool = pools["assoc_stats"][:7], pools["assoc_stats"][7:15]
    m3_pool = pools["we_find"][:7]
    m4_pool = pools["modal_cause"][:10]
    m6_pool = pools["effect_of"][:8]

    ROT4 = ["ols_fe_panel_hlm", "did_natural_experiment", "iv_2sls", "nonlinear"]
    ROT3 = ["ols_fe_panel_hlm", "did_natural_experiment", "iv_2sls"]
    ROT3b = ["ols_fe_panel_hlm", "did_natural_experiment", "nonlinear"]

    entries: list[dict] = []

    def build_doc(target: str, header: str, paper: str, idx: int) -> str:
        ppf = per_paper_fillers.get(paper, [])
        f1 = ppf[idx % len(ppf)] if ppf else fillers[idx % len(fillers)]
        f2 = ppf[(idx + 1) % len(ppf)] if len(ppf) > 1 else fillers[(idx + 3) % len(fillers)]
        return f"## {header}\n\n{f1}\n\n{target}\n\n{f2}\n"

    def emit(cid, cls, paper, orig, mutated, expected, design, header="Results"):
        doc = build_doc(mutated, header, paper, len(entries))
        ctrl = build_doc(orig, header, paper, len(entries))
        dpath = OUT / f"{cid}.md"
        cpath = OUT / f"{cid}.ctrl.md"
        dpath.write_text(doc, encoding="utf-8")
        cpath.write_text(ctrl, encoding="utf-8")
        entries.append({"id": cid, "class": cls, "paper": paper, "design": design,
                        "expected": expected, "header": header,
                        "orig": orig, "mutated": mutated,
                        "doc": str(dpath.relative_to(HERE)), "control": str(cpath.relative_to(HERE))})

    # M1: is associated with -> causes
    for i, (paper, s) in enumerate(m1_pool):
        mut = re.sub(r"\bis associated with\b", " causes ", s, count=1)
        emit(f"m1_{i+1:03d}", "M1", paper, s, mut, "OVERCLAIM", ROT4[i % 4])
    # M2a: -> increases/reduces (statless markerless doc)
    for i, (paper, s) in enumerate(m2a_pool):
        m = re.search(r"\bis associated with\s+(\w+)", s, re.I)
        if not m or m.group(1).lower() in DEG_ADJ:
            continue
        verb = "increases" if i % 2 == 0 else "reduces"
        mut = re.sub(r"\bis associated with\b", f" {verb} ", s, count=1)
        emit(f"m2a_{i+1:03d}", "M2a", paper, s, mut, "CONDITION_MISSING", ROT3[i % 3])
    # M2b: stats retained -> conditional satisfied -> PASS
    for i, (paper, s) in enumerate(m2b_pool):
        m = re.search(r"\bis associated with\s+(\w+)", s, re.I)
        if not m or m.group(1).lower() in DEG_ADJ or re.search(r"\d+%", s):
            continue
        verb = "increases" if i % 2 == 0 else "reduces"
        mut = re.sub(r"\bis associated with\b", f" {verb} ", s, count=1)
        emit(f"m2b_{i+1:03d}", "M2b", paper, s, mut, "PASS", ROT3b[i % 3])
    # M3: we find that -> we reveal that
    for i, (paper, s) in enumerate(m3_pool):
        mut = re.sub(r"\bwe find that\b", "we reveal that", s, count=1, flags=re.I)
        mut = mut[0].upper() + mut[1:]
        emit(f"m3_{i+1:03d}", "M3", paper, s, mut, "OVERCLAIM", ROT4[i % 4])
    # M4: modal+cause -> stripped, in Discussion doc
    FUNC = {"that", "which", "who", "whom", "and", "or", "but", "to", "a", "an", "the",
            "of", "in", "on", "by", "with", "as", "at", "for", "their", "its", "his", "her", "also", "often"}
    for i, (paper, s) in enumerate(m4_pool):
        m = re.search(r"\b(may|might|could)\s+(cause|drive)\b", s, re.I)
        modal, verb = m.group(1), m.group(2)
        before = s[:m.start()].strip()
        words = re.findall(r"[A-Za-z\u2019'-]+", before)
        subj = next((w for w in reversed(words) if w.lower() not in FUNC), "")
        plural = subj.endswith("s") and not subj.lower().endswith(("ss", "us", "is"))
        forms = {"cause": ("causes", "cause"), "drive": ("drives", "drive")}
        repl = forms[verb.lower()][1] if plural else forms[verb.lower()][0]
        mut = s[:m.start()] + repl + s[m.end():]
        mut = re.sub(r"\s+", " ", mut).strip()
        emit(f"m4_{i+1:03d}", "M4", paper, s, mut, "OVERCLAIM", "ols_fe_panel_hlm", header="Discussion")
    # M5: X is associated -> X may be associated (stats retained)
    for i, (paper, s) in enumerate(m5_pool):
        mut = re.sub(r"\bis associated with\b", " may be associated with ", s, count=1)
        emit(f"m5_{i+1:03d}", "M5", paper, s, mut, "UNDERCLAIM", ROT3b[i % 3])
    # M6: effect-of sentence: did -> CONDITION_MISSING; ols_fe -> PASS (paired in one entry)
    for i, (paper, s) in enumerate(m6_pool):
        doc = build_doc(s, "Results", paper, 90 + i)
        dpath = OUT / f"m6_{i+1:03d}.did.md"
        opath = OUT / f"m6_{i+1:03d}.ols.md"
        dpath.write_text(doc, encoding="utf-8")
        opath.write_text(doc, encoding="utf-8")
        entries.append({"id": f"m6_{i+1:03d}", "class": "M6", "paper": paper,
                        "design": "did_natural_experiment", "expected": "CONDITION_MISSING",
                        "header": "Results", "orig": s, "mutated": s,
                        "doc": str(dpath.relative_to(HERE)), "control": str(opath.relative_to(HERE)),
                        "control_design": "ols_fe_panel_hlm", "control_expected": "PASS"})

    entries = [e for e in entries if "_tmp" not in e]
    (OUT / "manifest.json").write_text(json.dumps(entries, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"probes: {len(entries)} | docs: {len(list(OUT.glob('*.md')))}")
    from collections import Counter
    print(Counter(e["class"] for e in entries))
    return 0

if __name__ == "__main__":
    sys.exit(main())
