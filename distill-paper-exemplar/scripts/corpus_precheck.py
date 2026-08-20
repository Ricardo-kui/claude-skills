#!/usr/bin/env python3
"""Deterministic corpus precheck for distill writeback (Phase 4).

Moves the mechanical work OUT of the LLM: band selection, jaccard dedup
(threshold 0.33 per selection-gate protocol), registry lookup, and insert
anchor location. Produces a compact writeback plan (~1-2KB) so neither the
distill agent nor the writeback agent needs to read the corpus wholesale
(registry files run 54-257KB; variant files up to 166KB — reading them per
agent per pass was the dominant token cost of distillation).

Usage:
  python corpus_precheck.py --section results --citekey kalaignanametal2013 \
      --candidates candidates.yaml [--out writeback_plan.results.yaml]

candidates.yaml:
  candidates:
    - name: r8_ols_strategy_complete_mediation_kenny_signal
      target: "OLS-FE.md"          # file name or corpus subdir hint (optional)
      skeleton_text: "A question, then, is whether these [firm_characteristics] ..."
      keywords: ["kenny", "mediation"]   # optional, improves registry match

Plan output: per candidate -> band (gap/薄弱/quiet), dedup verdict
(SKIP at jaccard>=0.33 / EXTEND / ADD) with best match, registry matches,
and insert anchor (file + line of last variant heading).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

JACCARD_SKIP_THRESHOLD = 0.33
SKILLS_ROOT = Path(__file__).resolve().parent.parent.parent

CORPUS_ROOTS = {
    "introduction": SKILLS_ROOT / "write-introduction" / "academic-writing-corpus",
    "theory": SKILLS_ROOT / "write-theory" / "corpus",
    "methods": SKILLS_ROOT / "write-methods" / "econometric-models",
    "results": SKILLS_ROOT / "write-results" / "econometric-models",
}

CJK = re.compile(r"[一-鿿]")
WORD = re.compile(r"[a-z0-9]+")
BLOCK_HEAD = re.compile(r"^#{2,4}\s+.+$", re.M)
WEAK_MARKERS = ("EMERGING", "单篇", "待第二篇", "待交叉验证")
STRONG_MARKERS = ("ROBUST", "VERIFIED", "多篇")


def tokenize(text: str) -> set[str]:
    text = text.lower()
    tokens = set(WORD.findall(text))
    cjk = "".join(CJK.findall(text))
    tokens.update(cjk[i : i + 2] for i in range(len(cjk) - 1))
    return tokens


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def containment(a: set[str], b: set[str]) -> float:
    """Share of candidate tokens covered by the corpus block. Dedup is a
    coverage question ('is this candidate already in the corpus?'), so the
    short candidate vs long block comparison needs containment, not jaccard."""
    if not a:
        return 0.0
    return len(a & b) / len(a)


def load_blocks(path: Path) -> list[dict]:
    """Split a corpus file into heading blocks: [{heading, start_line, text}]."""
    lines = path.read_text(encoding="utf-8", errors="replace").split("\n")
    heads = [(i, ln) for i, ln in enumerate(lines) if BLOCK_HEAD.match(ln)]
    blocks = []
    for k, (i, ln) in enumerate(heads):
        end = heads[k + 1][0] if k + 1 < len(heads) else len(lines)
        blocks.append({"heading": ln.strip(), "start_line": i + 1,
                       "text": "\n".join(lines[i:end])})
    return blocks


def find_target_file(corpus_root: Path, hint: str | None) -> Path | None:
    if hint:
        exact = list(corpus_root.rglob(hint))
        if exact:
            return exact[0]
        stem = hint.rsplit(".", 1)[0]
        loose = [p for p in corpus_root.rglob("*.md") if stem in p.name]
        if loose:
            return loose[0]
    return None


def band_from_indexes(corpus_root: Path, target: Path | None) -> tuple[str, str]:
    """gap / 薄弱 / quiet from _index.md / INDEX.md table rows only
    (update-note lines contain per-variant EMERGING markers and must be ignored)."""
    if target is None:
        return "gap", "无目标文件——语料中无此变体/模块"
    rows = []
    for idx in list(corpus_root.rglob("_index.md")) + list(corpus_root.rglob("INDEX.md")):
        try:
            rows += [l for l in idx.read_text(encoding="utf-8", errors="replace").splitlines()
                     if target.stem in l and l.lstrip().startswith("|")]
        except OSError:
            pass
    if not rows:
        return "gap", f"索引中无 {target.name} 条目"
    joined = " ".join(rows)
    if any(m in joined for m in WEAK_MARKERS):
        return "薄弱", f"索引标单篇/EMERGING：{rows[0].strip()[:120]}"
    if any(m in joined for m in STRONG_MARKERS):
        return "quiet", f"索引标 ROBUST/VERIFIED：{rows[0].strip()[:120]}"
    return "quiet", f"索引有条目且无薄弱标记：{rows[0].strip()[:120]}"


def band_from_block(block_text: str | None) -> tuple[str, str] | None:
    """Variant-level band from the best-match block's own validation status."""
    if not block_text:
        return None
    if "ROBUST" in block_text or "VERIFIED" in block_text:
        return "quiet", "最佳匹配变体标 ROBUST/VERIFIED"
    if any(m in block_text for m in WEAK_MARKERS):
        return "薄弱", "最佳匹配变体为单篇/EMERGING"
    return None


def registry_matches(registry: Path | None, citekey: str, keywords: list[str]) -> list[str]:
    if registry is None or not registry.is_file():
        return []
    text = registry.read_text(encoding="utf-8", errors="replace")
    hits = []
    needles = [citekey.lower()] + [k.lower() for k in keywords]
    for m in re.finditer(r"^(\s*-?\s*id:\s*\S+.*?)(?=^\s*-?\s*id:\s*\S+|\Z)",
                         text, re.M | re.S):
        block = m.group(1)
        if any(n in block.lower() for n in needles):
            first = block.strip().splitlines()[0][:100]
            hits.append(f"{first}  ({len(block)} chars)")
    return hits[:10]


def find_registry(corpus_root: Path) -> Path | None:
    for p in corpus_root.rglob("_evidence_registry.yaml"):
        return p
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description="Corpus precheck -> writeback plan")
    ap.add_argument("--section", required=True, choices=sorted(CORPUS_ROOTS))
    ap.add_argument("--citekey", required=True)
    ap.add_argument("--candidates", required=True, help="candidates YAML from the distill agent")
    ap.add_argument("--out", default=None, help="plan output path (default: <candidates>.plan.yaml)")
    args = ap.parse_args()

    corpus_root = CORPUS_ROOTS[args.section]
    if not corpus_root.is_dir():
        print(f"ERROR: corpus root missing: {corpus_root}", file=sys.stderr)
        return 2
    cand_path = Path(args.candidates)
    spec = yaml.safe_load(cand_path.read_text(encoding="utf-8"))
    candidates = spec.get("candidates", []) if isinstance(spec, dict) else []
    registry = find_registry(corpus_root)

    plan_items = []
    for cand in candidates:
        name = cand.get("name", "unnamed")
        target = find_target_file(corpus_root, cand.get("target"))

        skeleton_tokens = tokenize(cand.get("skeleton_text", "") or name)
        # dedup scan: compare against blocks of the target file/dir first, else all corpus files
        if target is None:
            scan_files = sorted(corpus_root.rglob("*.md"))
        elif target.is_dir():
            scan_files = sorted(target.rglob("*.md"))
        else:
            scan_files = [target]
        best = {"file": None, "heading": None, "jaccard": 0.0, "containment": 0.0,
                "line": None, "block_text": None}
        for f in scan_files:
            if f is None or f.name.startswith(("_", "INDEX")):
                continue
            for blk in load_blocks(f):
                bt = tokenize(blk["text"])
                score = jaccard(skeleton_tokens, bt)
                cover = containment(skeleton_tokens, bt)
                if max(score, cover) > max(best["jaccard"], best["containment"]):
                    best = {"file": str(f), "heading": blk["heading"][:80],
                            "jaccard": round(score, 3), "containment": round(cover, 3),
                            "line": blk["start_line"], "block_text": blk["text"]}
        if best["jaccard"] >= JACCARD_SKIP_THRESHOLD or best["containment"] >= 0.60:
            verdict = "SKIP"
        elif target is not None and (best["jaccard"] >= 0.20 or best["containment"] >= 0.40):
            verdict = "EXTEND"
        else:
            verdict = "ADD"
        if verdict == "SKIP":
            band, band_ev = "quiet", f"语料已覆盖（{best['heading']}）"
        elif verdict == "ADD" and best["containment"] < 0.20:
            band, band_ev = "gap", f"无相近变体（containment={best['containment']}）——HIGH 优先"
        else:
            band, band_ev = (band_from_block(best["block_text"])
                             or band_from_indexes(corpus_root, target))

        anchor = None
        # for ADD: anchor in the target file, or (dir/unspecified target) in the
        # best-match file when similarity is non-trivial
        anchor_file = None
        if verdict == "ADD":
            if target is not None and target.is_file():
                anchor_file = target
            elif best["file"] and best["containment"] >= 0.10:
                anchor_file = Path(best["file"])
        if anchor_file is not None:
            blocks = load_blocks(anchor_file)
            # prefer anchoring after the last variant/pattern block, not a trailing
            # boundaries/anti-pattern section
            variant_blocks = [b for b in blocks
                              if re.search(r"变体|variant|pattern", b["heading"], re.I)
                              and not re.search(r"反模式|诚实边界|anti-?pattern|boundar", b["heading"], re.I)]
            anchor_block = (variant_blocks or blocks)[-1] if blocks else None
            if anchor_block:
                anchor = {"file": str(anchor_file),
                          "insert_after_line": anchor_block["start_line"]
                          + len(anchor_block["text"].splitlines()) - 1,
                          "after_heading": anchor_block["heading"][:80]}
            else:
                anchor = {"file": str(target), "insert_after_line": None,
                          "after_heading": "(file has no headings; append at end)"}
        elif verdict == "EXTEND" and best["file"]:
            anchor = {"file": best["file"], "insert_after_line": best["line"],
                      "after_heading": best["heading"]}

        plan_items.append({
            "name": name,
            "band": band,
            "band_evidence": band_ev,
            "dedup": {"verdict": verdict, "threshold": JACCARD_SKIP_THRESHOLD,
                      "best_match": {k: v for k, v in best.items() if k != "block_text"}},
            "registry_matches": registry_matches(registry, args.citekey,
                                                 cand.get("keywords", []) or []),
            "anchor": anchor,
            "human_review": "gate ① 仍须确认本 plan 后再写回（除非 --auto-write 已授权）",
        })

    plan = {"section": args.section, "citekey": args.citekey,
            "corpus_root": str(corpus_root),
            "registry": str(registry) if registry else None,
            "items": plan_items}
    out = Path(args.out) if args.out else cand_path.with_suffix(".plan.yaml")
    out.write_text(yaml.safe_dump(plan, allow_unicode=True, sort_keys=False),
                   encoding="utf-8")
    print(json.dumps({"plan": str(out), "items": len(plan_items),
                      "verdicts": {i["name"]: i["dedup"]["verdict"] for i in plan_items}},
                     ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
