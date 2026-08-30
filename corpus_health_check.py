#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Corpus Health Check — 语料库体检：变体数 vs 批评数聚合。

聚合两侧语料库的度量（测量学第一原则：没有聚合的测量无法指导分配）：
  - 变体数：从各设计/结果类型文件实际计数（`### 变体 N:`，全角/半角冒号兼容），不信任 INDEX 计数表
  - 批评数：methods 读 `evidence.by_design_type.<类型>.validation_history`；
            results 读 `estimators.<键>.usage_stats`
  - 输出每类型一行：变体数 | revise | reject | 批评合计 | last_critique | critique_heavy | 趋同批评要点
  - 排序：critique_heavy 优先 → 批评合计降序 → 变体数降序

用法:
    python corpus_health_check.py --type both      # methods + results（默认）
    python corpus_health_check.py --type methods
    python corpus_health_check.py --type results
    python corpus_health_check.py --json           # 输出 JSON（供下游消费）

退出码:
    0 = 正常
    1 = 存在 critique_heavy 类型（体检发现薄弱点，下一轮蒸馏应优先 REPLACE/EXTEND）
"""

import argparse
import json
import re
import sys
from pathlib import Path

SKILLS = Path(__file__).resolve().parent
# 数字（methods/results）与字母（intro/theory 的 变体 A/B/C）均计数
VAR_RE = re.compile(r"^### 变体 ([A-Za-z0-9]+)[:：]", re.M)

VALID_KEYS = ("revise", "reject", "last_critique", "common_revise_reasons")


def norm_key(s: str) -> str:
    """registry 键名与文件名归一化匹配：去连字符/下划线。"""
    return re.sub(r"[-_]", "", s.lower())


def count_variants(path: Path) -> int:
    return len(VAR_RE.findall(path.read_text(encoding="utf-8")))


def load_usage(registry_path: Path) -> dict:
    """返回 {归一化键: usage_stats dict}。methods 与 results 结构不同，各自容错。"""
    import yaml
    data = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
    out = {}
    if not isinstance(data, dict):
        return out
    # methods: evidence.by_design_type.<类型>.validation_history
    bdt = (data.get("evidence") or {}).get("by_design_type")
    if isinstance(bdt, dict):
        for name, info in bdt.items():
            vh = (info or {}).get("validation_history")
            if isinstance(vh, dict):
                out[norm_key(name)] = vh
    # results: estimators.<键>.usage_stats
    est = data.get("estimators")
    if isinstance(est, dict):
        for name, info in est.items():
            us = (info or {}).get("usage_stats")
            if isinstance(us, dict):
                out[norm_key(name)] = us
    return out


def load_critique_usage(registry_path: Path) -> dict:
    """读 critique.per_file 段（键 = 相对路径如 hooks/03-data-shock.md）——intro/theory 使用。"""
    import yaml
    data = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
    out = {}
    if not isinstance(data, dict):
        return out
    per = (data.get("critique") or {}).get("per_file")
    if isinstance(per, dict):
        for rel, info in per.items():
            if isinstance(info, dict):
                out[norm_key(rel)] = info
    return out


def collect(side: str) -> list:
    """返回 [{type, file, variants, revise, reject, last_critique, reasons}]
    side: methods / results（registry validation_history/usage_stats）或 intro / theory（critique.per_file）。"""
    if side in ("methods", "results"):
        corpus = SKILLS / f"write-{side}" / "corpus"
        usage = load_usage(corpus / "_evidence_registry.yaml")
        rows = []
        for f in sorted(corpus.glob("*.md")):
            if f.name == "INDEX.md" or "草案" in f.name:
                continue
            n = count_variants(f)
            u = usage.get(norm_key(f.stem), {})
            rows.append({
                "side": "M" if side == "methods" else "R",
                "type": f.stem,
                "file": f.name,
                "variants": n,
                "revise": int(u.get("revise", 0) or 0),
                "reject": int(u.get("reject", 0) or 0),
                "last_critique": u.get("last_critique"),
                "reasons": u.get("common_revise_reasons") or [],
            })
        return rows

    # intro / theory：遍历子目录 canonical 文件，读 critique.per_file
    if side == "intro":
        corpus = SKILLS / "write-introduction" / "corpus"
        registry = corpus / "_evidence_registry.yaml"
    else:  # theory
        corpus = SKILLS / "write-theory" / "corpus"
        registry = corpus / "_evidence_registry.yaml"
    usage = load_critique_usage(registry)
    rows = []
    for d in sorted(p for p in corpus.iterdir() if p.is_dir()):
        for f in sorted(d.glob("*.md")):
            if f.name == "_index.md":
                continue
            rel = f"{d.name}/{f.name}"
            u = usage.get(norm_key(rel), {})
            rows.append({
                "side": "I" if side == "intro" else "T",
                "type": rel,
                "file": f.name,
                "variants": count_variants(f),
                "revise": int(u.get("revise", 0) or 0),
                "reject": int(u.get("reject", 0) or 0),
                "last_critique": u.get("last_critique"),
                "reasons": u.get("reasons") or [],
            })
    return rows


def fmt_rows(rows: list) -> list:
    """排序 + 标记。critique_heavy: revise+reject>=2。"""
    for r in rows:
        r["critiques"] = r["revise"] + r["reject"]
        r["heavy"] = r["critiques"] >= 2
    rows.sort(key=lambda r: (not r["heavy"], -r["critiques"], -r["variants"]))
    return rows


def print_report(rows: list) -> None:
    heavy = [r for r in rows if r["heavy"]]
    print("=" * 78)
    print("Corpus Health Check — 语料库体检（变体数 vs 批评数聚合）")
    print("=" * 78)
    print(f"{'侧':>2}{'类型':<20}{'变体':>5}{'revise':>7}{'reject':>7}{'批评合计':>8}{'最近批评':>12}  标记 / 趋同批评要点")
    print("-" * 80)
    for r in rows:
        last = r["last_critique"] or "—"
        mark = "⚠ critique_heavy" if r["heavy"] else ""
        reasons = "；".join(r["reasons"][:2])
        if reasons:
            mark = (mark + " " + reasons).strip()
        print(f"{r['side']:>2} {r['type']:<20}{r['variants']:>5}{r['revise']:>7}{r['reject']:>7}{r['critiques']:>8}{last:>12}  {mark}")
    print("-" * 78)
    if heavy:
        print(f"薄弱类型 {len(heavy)} 个（revise+reject ≥ 2 → 下一轮蒸馏优先 REPLACE/EXTEND）:")
        for r in heavy:
            print(f"  - {r['type']}（{r['variants']} 变体 / {r['critiques']} 次批评）")
    else:
        print("无 critique_heavy 类型；批评驱动的选材压力正常。")
    high = [r for r in rows if r["variants"] >= 5 and r["critiques"] > 0 and not r["heavy"]]
    if high:
        print("高变体数且有批评（观察区）:")
        for r in high:
            print(f"  - {r['type']}（{r['variants']} 变体 / {r['critiques']} 次批评）")


def main() -> int:
    ap = argparse.ArgumentParser(description="语料库体检：变体数 vs 批评数聚合（选材输入）")
    ap.add_argument("--type", "-t", choices=["methods", "results", "intro", "theory", "both", "all"],
                    default="all", help="both=methods+results（兼容旧用法）；all=四个 skills")
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    args = ap.parse_args()

    rows = []
    if args.type in ("methods", "both", "all"):
        rows += collect("methods")
    if args.type in ("results", "both", "all"):
        rows += collect("results")
    if args.type in ("intro", "all"):
        rows += collect("intro")
    if args.type in ("theory", "all"):
        rows += collect("theory")
    rows = fmt_rows(rows)

    if args.json:
        print(json.dumps([{k: r[k] for k in ("side", "type", "variants", "revise", "reject",
                                             "critiques", "heavy", "last_critique", "reasons")}
                          for r in rows], ensure_ascii=False, indent=2))
    else:
        print_report(rows)

    return 1 if any(r["heavy"] for r in rows) else 0


if __name__ == "__main__":
    sys.exit(main())
