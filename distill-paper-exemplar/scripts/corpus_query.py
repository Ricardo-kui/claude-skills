#!/usr/bin/env python3
"""Deterministic corpus-index query for distill selection gates and routing.

The distill-*-exemplar selection gates and routing lookups used to read
_index.md / INDEX.md / _evidence_registry.yaml / routing tables wholesale
(54-257KB per file) — the dominant token cost of distillation. This script
answers those queries deterministically and prints only the matching
lines/blocks (hard-capped at --limit lines, default 50), so the distill agent
reads ~1KB instead of ~100KB.

Subcommands:
  index    搜索 _index.md / INDEX.md 表格行（含状态列）
  registry 搜索 _evidence_registry.yaml 条目（validation_history / usage_stats / slots 等）
  routing  搜索路由表（theory: meta/routing_table.md；introduction: _routing_tables.yaml）

Usage:
  python corpus_query.py index    --section introduction --query "data shock"
  python corpus_query.py registry --section methods      --query "DiD"
  python corpus_query.py routing  --section theory       --query "Inadequacy"
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

# 中文 Windows 控制台默认 GBK；代理按 UTF-8 读工具输出，强制 UTF-8 避免乱码。
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

SKILLS_ROOT = Path(__file__).resolve().parent.parent.parent

CORPUS_ROOTS = {
    "introduction": SKILLS_ROOT / "write-introduction" / "corpus",
    "theory": SKILLS_ROOT / "write-theory" / "corpus",
    "methods": SKILLS_ROOT / "write-methods" / "corpus",
    "results": SKILLS_ROOT / "write-results" / "corpus",
}


class Budget:
    """Hard output cap — keeping the LLM read small is the whole point."""

    def __init__(self, limit: int):
        self.limit = limit
        self.n = 0

    def emit(self, line: str) -> bool:
        if self.n >= self.limit:
            return False
        print(line)
        self.n += 1
        return True


# 截断上限：hooks _index 实测最长行 316 字符；routing 关键散文实测 768 字符/行
# （曾被 160 切在 "...architectur"，2026-08-22 实测）。放宽到内容完整，
# 行数预算仍由 --limit 兜底，不失控。
ROW_CAP = 320
HEADER_CAP = 200
PROSE_CAP = 800


def clip(s: str, cap: int) -> str:
    """截断加省略号——截断不可见等于喂半句话。"""
    return s[:cap] + ("…" if len(s) > cap else "")


def rel(p: Path) -> str:
    try:
        return str(p.relative_to(SKILLS_ROOT))
    except ValueError:
        return str(p)


def terms(q: str) -> list[str]:
    return [t.lower() for t in q.split() if t]


def hit(text: str, ts: list[str]) -> bool:
    low = text.lower()
    return any(t in low for t in ts)


def is_sep(s: str) -> bool:
    """Markdown 表格分隔行（如 |------|------|）。"""
    return bool(s.startswith("|")) and "-" in s and re.fullmatch(r"[\s|\-:]+", s) is not None


def cmd_index(root: Path, query: str, budget: Budget) -> None:
    ts = terms(query)
    files = sorted(list(root.rglob("_index.md")) + list(root.rglob("INDEX.md")))
    if not files:
        print("（该 corpus 无 _index.md / INDEX.md）")
        return
    for f in files:
        try:
            lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        section = ""            # 最近的 # / ## 标题（子表归属）
        sec_emitted: set[str] = set()
        hdr_emitted: set[int] = set()   # 每张表头只输出一次（1-based 表头行号）
        for i, ln in enumerate(lines, 1):
            s = ln.strip()
            if s.startswith("#"):
                section = s.lstrip("#").strip()
                continue
            if not (s.startswith("|") and hit(s, ts)):
                continue
            sep_above = lines[i - 2].strip() if i >= 3 else ""
            hdr_above = lines[i - 3].strip() if i >= 4 else ""
            hdr_idx = i - 2   # 表头行（1-based）
            if is_sep(sep_above) and hdr_above.startswith("|"):
                if hdr_idx not in hdr_emitted:
                    hdr_emitted.add(hdr_idx)
                    if section and section not in sec_emitted:
                        sec_emitted.add(section)
                        if not budget.emit(f"## {section}"):
                            return
                    if not budget.emit(f"{rel(f)}:{hdr_idx}: {clip(hdr_above, HEADER_CAP)}"):
                        return
                    if not budget.emit(f"{rel(f)}:{hdr_idx + 1}: {clip(sep_above, HEADER_CAP)}"):
                        return
            elif section and section not in sec_emitted:
                sec_emitted.add(section)
                if not budget.emit(f"## {section}"):
                    return
            if not budget.emit(f"{rel(f)}:{i}: {clip(s, ROW_CAP)}"):
                return


def cmd_registry(root: Path, query: str, budget: Budget) -> None:
    ts = terms(query)
    regs = sorted(root.rglob("_evidence_registry.yaml"))
    if not regs:
        print("（该 corpus 无 _evidence_registry.yaml）")
        return
    for f in regs:
        try:
            data = yaml.safe_load(f.read_text(encoding="utf-8", errors="replace"))
        except Exception as e:  # noqa: BLE001 — 只读查询，损坏文件报错即可
            print(f"（registry 解析失败: {rel(f)}: {e}）")
            continue
        if data is None:
            continue
        _walk(data, ts, budget, f)


def _walk(node, ts, budget, f, path: str = ""):
    """Key-match: dump scalar children (compact block). Else recurse."""
    if isinstance(node, dict):
        for k, v in node.items():
            p = f"{path}.{k}" if path else str(k)
            if hit(str(k), ts):
                _dump_scalars(v, budget, f, p, 0)
            else:
                _walk(v, ts, budget, f, p)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            _walk(v, ts, budget, f, f"{path}[{i}]")
    elif isinstance(node, str) and hit(node, ts):
        budget.emit(f"{rel(f)}: {path}: {clip(node.strip(), PROSE_CAP)}")


def _dump_scalars(node, budget, f, p: str, depth: int) -> None:
    """Print a matched key's scalar children, one per line, ≤3 levels deep."""
    if depth > 3:
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(v, (dict, list)):
                _dump_scalars(v, budget, f, f"{p}.{k}", depth + 1)
            else:
                budget.emit(f"{rel(f)}: {p}.{k}: {clip(str(v), PROSE_CAP)}")
    elif isinstance(node, list):
        for i, v in enumerate(node[:8]):
            if isinstance(v, (dict, list)):
                _dump_scalars(v, budget, f, f"{p}[{i}]", depth + 1)
            else:
                budget.emit(f"{rel(f)}: {p}[{i}]: {clip(str(v), PROSE_CAP)}")
    else:
        budget.emit(f"{rel(f)}: {p}: {clip(str(node), PROSE_CAP)}")


def cmd_routing(root: Path, query: str, budget: Budget, section: str) -> None:
    ts = terms(query)
    if section == "theory":
        f = root / "meta" / "routing_table.md"
        if not f.is_file():
            print(f"（routing 表不存在: {rel(f)}）")
            return
        text = f.read_text(encoding="utf-8", errors="replace")
        blocks: list[tuple[str, str]] = []
        cur_head, cur_body = "", []
        for ln in text.splitlines():
            if ln.startswith("## "):
                if cur_head:
                    blocks.append((cur_head, "\n".join(cur_body)))
                cur_head, cur_body = ln[3:].strip(), []
            elif cur_head:
                cur_body.append(ln)
        if cur_head:
            blocks.append((cur_head, "\n".join(cur_body)))
        for head, body in blocks:
            if not (hit(head, ts) or hit(body, ts)):
                continue
            if not budget.emit(f"## {head}"):
                return
            lines = [ln.strip() for ln in body.splitlines() if ln.strip()]
            if lines and lines[0].startswith("|"):
                # 表格块：保留表头，其余只输出命中行（块尾散文命中同样输出）
                for ln in lines[:2]:
                    if not budget.emit(f"  {clip(ln, HEADER_CAP)}"):
                        return
                for ln in lines[2:]:
                    if hit(ln, ts):
                        # 表格块内可能混有块尾散文（如 R1–R4 判定段），按行型选上限
                        cap = ROW_CAP if ln.startswith("|") else PROSE_CAP
                        if not budget.emit(f"  {clip(ln, cap)}"):
                            return
            else:
                # 散文块：输出第一个命中行及其上一行作上下文
                for i, ln in enumerate(lines):
                    if hit(ln, ts):
                        if i > 0:
                            if not budget.emit(f"  {clip(lines[i - 1], PROSE_CAP)}"):
                                return
                        if not budget.emit(f"  {clip(ln, PROSE_CAP)}"):
                            return
                        break
    else:  # introduction: YAML routing tables
        files = sorted(root.rglob("_routing_tables.yaml"))
        if not files:
            print("（该 corpus 无 _routing_tables.yaml）")
            return
        for f in files:
            try:
                data = yaml.safe_load(f.read_text(encoding="utf-8", errors="replace"))
            except Exception as e:  # noqa: BLE001
                print(f"（routing 解析失败: {rel(f)}: {e}）")
                continue
            if data is not None:
                _walk(data, ts, budget, f)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="确定性语料索引查询（选材 gate / routing 专用，输出 ≤ --limit 行）")
    ap.add_argument("cmd", choices=["index", "registry", "routing"])
    ap.add_argument("--section", required=True, choices=sorted(CORPUS_ROOTS))
    ap.add_argument("--query", required=True,
                    help="关键词（空格分隔，任一命中即输出；建议中/英各查一轮，可含 canonical_id 前缀）")
    ap.add_argument("--limit", type=int, default=50, help="输出行上限（默认 50）")
    args = ap.parse_args()

    if args.cmd == "routing" and args.section not in ("introduction", "theory"):
        print(f"ERROR: routing 仅适用于 introduction/theory（{args.section} 无路由表）",
              file=sys.stderr)
        return 2
    root = CORPUS_ROOTS[args.section]
    if not root.is_dir():
        print(f"ERROR: corpus root 不存在: {root}", file=sys.stderr)
        return 2

    budget = Budget(args.limit)
    print(f"# corpus_query {args.cmd} --section {args.section} --query {args.query!r}"
          f"（确定性，命中行上限 {args.limit}）")
    if args.cmd == "index":
        cmd_index(root, args.query, budget)
    elif args.cmd == "registry":
        cmd_registry(root, args.query, budget)
    else:
        cmd_routing(root, args.query, budget, args.section)

    if budget.n >= args.limit:
        print(f"...（已截断至 {args.limit} 行；换更具体的 query 或调高 --limit）")
    elif budget.n == 0:
        print("（无命中——零命中 ≠ 语料缺口：换关键词重试，中/英各查一轮；连续无命中才按选材 gate 判 gap）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
