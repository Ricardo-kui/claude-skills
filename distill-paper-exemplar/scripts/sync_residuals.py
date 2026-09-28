#!/usr/bin/env python3
"""Semi-automatic residuals sync pass (2026-09-28 hardening).

Consumes the writeback_residuals.yaml emitted by verify_writeback.py and
discharges the deterministic portion of the historical "edit by hand" list:

  registry_missing_paper  -> AUTO (with --apply): append "(ABBR)" to the bare
                             citekey line rebuild wrote, bump paper_count,
                             bump gap_distribution[--gap].
  registry_no_entry       -> PRINT a paste-ready by_source_paper registration
                             block (micro-template precedent 2026-08-28);
                             never auto-written (design_types/slots need a
                             human call).
  registry_variant_missing-> PRINT instructions only (executor-side anomaly).

Paper-line format contract: `- <citekey> (<ABBR>)` — what verify V3b expects.
Rebuild derives bare citekeys (it scans blocks, no journal context), so this
script is the designated place where the journal abbreviation enters.

EOL discipline: registry files are read/written as BYTES; output preserves the
file's own convention (CRLF stays CRLF, LF stays LF) — see
rebuild_apply's per-convention EOL guard.

Usage:
  python sync_residuals.py --residuals <writeback_residuals.yaml> \
      --journal "Academy of Management Journal" --gap Incompleteness [--apply]
      [--registry-root <skills root>] [--journal-abbr AMJ]

Default is DRY-RUN; pass --apply to write.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

SECTION_SKILL = {
    "introduction": "write-introduction",
    "theory": "write-theory",
    "methods": "write-methods",
    "results": "write-results",
}

JOURNAL_ABBR = {
    "Academy of Management Journal": "AMJ",
    "Academy of Management Review": "AMR",
    "Academy of Management Annals": "AMA",
    "Administrative Science Quarterly": "ASQ",
    "Strategic Management Journal": "SMJ",
    "Organization Science": "ORSC",
    "Organization Studies": "ORGSTUD",
    "Management Science": "MS",
    "Journal of Marketing": "JM",
    "Journal of Marketing Research": "JMR",
    "Journal of Consumer Research": "JCR",
    "Marketing Science": "MKS",
    "Journal of Operations Management": "JOM",
    "Journal of Supply Chain Management": "JSCM",
    "Production and Operations Management": "POM",
    "Journal of Management": "JMG",
    "Journal of Management Studies": "JMS",
    "Journal of International Business Studies": "JIBS",
    "Manufacturing & Service Operations Management": "MSOM",
    "Journal of Product Innovation Management": "JPIM",
    "IEEE Transactions on Engineering Management": "ITEM",
    "Journal of Business Venturing": "JBV",
    "Entrepreneurship Theory and Practice": "ETP",
    "Journal of Applied Psychology": "JAP",
    "Personnel Psychology": "PPSY",
    "Sloan Management Review": "SMR",
    "Harvard Business Review": "HBR",
}


def resolve_abbr(journal: str, explicit: str | None) -> str:
    if explicit:
        return explicit
    for full, ab in JOURNAL_ABBR.items():
        if journal.strip().lower() == full.lower():
            return ab
    raise SystemExit(
        f"[sync] journal 未在缩写表命中且未给 --journal-abbr：{journal!r}\n"
        f"       可用 --journal-abbr 显式指定（治理格式：大写缩写）")


def load_bytes(path: Path) -> tuple[bytes, str, bool]:
    """(raw, lf-normalized text, was_crlf) — 匹配逻辑在 LF 语义上做，
    写盘前按原约定还原（CRLF 治理惯例，见 rebuild_apply EOL 守卫）。"""
    raw = path.read_bytes()
    was_crlf = b"\r\n" in raw
    text = raw.decode("utf-8")
    if was_crlf:
        text = text.replace("\r\n", "\n")
    return raw, text, was_crlf


def save_bytes(path: Path, text: str, was_crlf: bool) -> None:
    if was_crlf:
        text = text.replace("\r\n", "\n").replace("\n", "\r\n")
    path.write_bytes(text.encode("utf-8"))


def entry_span(text: str, key: str) -> tuple[int, int] | None:
    """(start, end) of the `key:` entry block — same locating rule as
    verify_writeback.find_registry_entry (indent-delimited)."""
    pat = re.compile(r"^( +)%s:\n" % re.escape(key), re.M)
    m = pat.search(text)
    if not m:
        return None
    ind = len(m.group(1))
    nxt = re.search(r"^ {1,%d}\S" % ind, text[m.end():], re.M)
    end = m.end() + nxt.start() if nxt else len(text)
    return m.start(), end


def fix_missing_paper(text: str, key: str, paper: str, abbr: str,
                      gap: str, dry: bool) -> tuple[str, list[str]]:
    log: list[str] = []
    span = entry_span(text, key)
    if span is None:
        return text, [f"  !! {key}: 条目块不可定位（schema 漂移？）— 转人工"]
    s, e = span
    blk = text[s:e]
    line_re = re.compile(r"^(\s*)- %s\s*$" % re.escape(paper), re.M)
    if line_re.search(blk):
        nb = line_re.sub(lambda m: f"{m.group(1)}- {paper} ({abbr})", blk)
        log.append(f"  {key}: 裸行 → `- {paper} ({abbr})`")
    elif re.search(r"^\s*- %s \(" % re.escape(paper), blk, re.M):
        return text, [f"  {key}: paper 行已带括号 — 跳过（残项过期）"]
    else:
        # papers: 列表存在但无该行 → append 到列表末尾
        pl = re.search(r"^(\s*)papers:\s*\n((?:\1\s+- .*\n)+)", blk, re.M)
        if not pl:
            return text, [f"  !! {key}: 无 papers 列表且无裸行 — 转人工"]
        indent = pl.group(1)
        nb = blk[:pl.end(2)] + f"{indent}  - {paper} ({abbr})\n" + blk[pl.end(2):]
        log.append(f"  {key}: papers 列表追加 `- {paper} ({abbr})`")
    # paper_count bump
    pc = re.search(r"^(\s*)paper_count: (\d+)", nb, re.M)
    if pc:
        nb = nb[:pc.start()] + f"{pc.group(1)}paper_count: {int(pc.group(2)) + 1}" \
            + nb[pc.end():]
        log.append(f"  {key}: paper_count {pc.group(2)} → {int(pc.group(2)) + 1}")
    # gap bump（gap_distribution 子块内该 gap 行 +1）
    gp = re.search(r"^(\s*)%s: (\d+)$" % re.escape(gap), nb, re.M)
    if gp:
        nb = nb[:gp.start()] + f"{gp.group(1)}{gap}: {int(gp.group(2)) + 1}" \
            + nb[gp.end():]
        log.append(f"  {key}: gap_distribution.{gap} {gp.group(2)} → "
                   f"{int(gp.group(2)) + 1}")
    else:
        log.append(f"  {key}: （gap_distribution.{gap} 行未命中 — 保持不动）")
    return text[:s] + nb + text[e:], log


def no_entry_block(paper: str, journal: str, items: list[dict]) -> str:
    names = "；".join(f"{it['item']}（{it['stem']}）" for it in items)
    return (
        f"by_source_paper 手动登记块（micro-template 先例 2026-08-28，语义字段需人定）：\n"
        f"  {paper}:\n"
        f"    journal: {journal}\n"
        f"    title: \"<补全>\"\n"
        f"    status: EMERGING\n"
        f"    verification_basis: \"first_distill_ladder_default\"\n"
        f"    design_types: ['<从 plan identity design_family 提炼>']\n"
        f"    slots_covered: ['<从 plan items 的槽位标注提炼>']\n"
        f"    note: \"写回补登记：{names}。micro-templates 文件层无独立 registry "
        f"条目结构，按邻近 by_source_paper 格式登记。\"\n")


def main() -> int:
    ap = argparse.ArgumentParser(description="Semi-automatic writeback residuals sync")
    ap.add_argument("--residuals", required=True, help="verify_writeback 产出的 writeback_residuals.yaml")
    ap.add_argument("--journal", default="", help="论文期刊全名（缩写表匹配）")
    ap.add_argument("--journal-abbr", default=None, help="显式缩写（表未命中时必给）")
    ap.add_argument("--gap", default=None, choices=["Incompleteness", "Inadequacy", "Incommensurability"])
    ap.add_argument("--registry-root", default=None, help="skills 根目录（默认本脚本 ../../..）")
    ap.add_argument("--apply", action="store_true", help="缺省 dry-run")
    args = ap.parse_args()

    root = Path(args.registry_root) if args.registry_root else \
        Path(__file__).resolve().parent.parent.parent
    res = yaml.safe_load(Path(args.residuals).read_text(encoding="utf-8"))
    residuals = res.get("residuals") or []
    paper = res.get("paper") or ""
    if not residuals:
        print("[sync] 残项为空 — 无事可做")
        return 0

    abbr = resolve_abbr(args.journal, args.journal_abbr) if \
        any(r["type"] == "registry_missing_paper" for r in residuals) else None
    gap = args.gap or ""
    if any(r["type"] == "registry_missing_paper" for r in residuals) and not gap:
        raise SystemExit("[sync] registry_missing_paper 需要 --gap（计数归属）")

    mode = "APPLY" if args.apply else "DRY-RUN"
    by_section: dict[str, list[dict]] = {}
    for r in residuals:
        by_section.setdefault(r["section"], []).append(r)

    touched: list[str] = []
    for section, items in sorted(by_section.items()):
        skill = SECTION_SKILL.get(section)
        if not skill:
            print(f"[sync][{section}] 未知 section — 转人工")
            continue
        reg = root / skill / "corpus" / "_evidence_registry.yaml"
        if not reg.is_file():
            print(f"[sync][{section}] registry 不存在: {reg} — 转人工")
            continue
        raw, text, was_crlf = load_bytes(reg)
        orig = text
        # 同 key 去重
        seen_mp: dict[str, list[dict]] = {}
        no_entry: list[dict] = []
        for r in items:
            if r["type"] == "registry_missing_paper":
                seen_mp.setdefault(r["key"], []).append(r)
            elif r["type"] == "registry_no_entry":
                no_entry.append(r)
            else:
                print(f"[sync][{section}] {r['type']}:{r.get('item')} — "
                      "打印模式外类型，转人工")
        for key in sorted(seen_mp):
            text, log = fix_missing_paper(text, key, paper, abbr, gap,
                                          dry=not args.apply)
            print(f"[sync][{section}/{mode}] {reg.name}::{key}")
            for ln in log:
                print(ln)
        if no_entry:
            stems = sorted({r["stem"] for r in no_entry})
            print(f"[sync][{section}/{mode}] registry_no_entry ×{len(no_entry)} "
                  f"(stems: {', '.join(stems)})：")
            print("  " + no_entry_block(paper, args.journal or "<journal>",
                                        no_entry).replace("\n", "\n  ").rstrip())
        if text != orig:
            if args.apply:
                save_bytes(reg, text, was_crlf)
                print(f"[sync][{section}] WRITTEN: {reg}")
            else:
                print(f"[sync][{section}] (dry-run，未写盘 — --apply 生效)")
            touched.append(section)

    if not touched:
        print("[sync] 无需写盘的变更")
    return 0


if __name__ == "__main__":
    sys.exit(main())
