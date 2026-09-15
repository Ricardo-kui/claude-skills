#!/usr/bin/env python3
"""Shared skeleton-index engine for write-theory / write-methods / write-results.

单源声明（write-introduction/references/library-contract.md 边界 3 的工具层延伸）
------------------------------------------------------------------------------
本模块是三个 skill 骨架索引构建脚本（``<skill>/scripts/build_indices.py``）的
共享引擎：文本规整工具、Entry/Unparsed 模型、变体→条目 materialize、
``--verify`` 回源/抽样脚手架、渲染原语、写盘与 CLI 骨架只在本文件存在一份。
各 skill 的适配器只保留真正特异的部分：目录轴表、标题/字段正则、槽位机制、
表头与路由页模板、锚点校验器、解析主循环。

适配器接线手法（与 ``_shared/feedback/record_feedback`` 约定一致）::

    SCRIPT_DIR = Path(__file__).resolve().parent
    SKILL_ROOT = SCRIPT_DIR.parent
    SHARED = SKILL_ROOT.parent / "_shared" / "indexing"
    sys.path.insert(0, str(SHARED))
    import indexing_engine as eng  # noqa: E402

行为兼容约定
------------
- 引擎只承接逐字或近逐字同源的代码；任何会改变生成物字节的差异留在适配器。
- ``--check`` / ``--verify`` 保持恒 return 0 的既有行为；门禁职责在
  ``_shared/indexing/check_all.py``（维护期）。
- ``entrypoint`` 相比旧脚本的裸 traceback 是有意的行为改进：
  OSError/ValueError → ``error: ...`` + 退出码 2。
- 每次运行末尾追加一行机器可读汇总 ``SUMMARY skill=...``，供
  check_all.py 解析；现有 stdout 无其它消费方。

路径基准：引擎自身不持有 skill 路径；``skill_root`` 一律由适配器传入
（= SKILL.md 所在目录）。
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

MAX_LINES = 400

# --------------------------------------------------------------- text ----

ANNOTATION_RE = re.compile(r"[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]")

VARIANT_TOKEN_RE = re.compile(r"^(?:[0-9]+|[A-Z]+)$")


def normalize(text: str) -> str:
    return " ".join(text.replace("\t", " ").split())


def is_english(text: str) -> bool:
    letters = sum(1 for ch in text if ch.isascii() and ch.isalpha())
    return letters >= 15


def strip_outer_quotes(text: str) -> str:
    t = text.strip()
    if len(t) >= 2 and t[0] in "\"'“「" and t[-1] in "\"'”」":
        return t[1:-1].strip()
    return t


def trim_annotation(text: str) -> str:
    """Cut a trailing Chinese/fullwidth annotation glued to an English quote."""
    m = ANNOTATION_RE.search(text)
    if m:
        text = text[: m.start()]
    return text.strip().strip("\"'“”「」").strip()


def escape_cell(text: str) -> str:
    return text.replace("|", r"\|")


# -------------------------------------------------------------- records ----


@dataclass
class Entry:
    """methods/results 形态的骨架条目（theory 适配器保留自己的 7 字段 Entry）。"""

    id: str
    slot: str
    citekey: str
    text: str
    path: str          # corpus-relative, e.g. corpus/OLS-FE.md
    anchor: str        # 变体-<vid>
    status: str        # "verbatim" | "模板"
    note: str = ""
    vid: str = ""
    seq: int = 0


@dataclass
class Unparsed:
    card: str
    path: str
    where: str
    text: str
    reason: str


# ------------------------------------------------------------- parsing ----


def collect_fence(lines: list[str], start: int) -> dict:
    """Collect a ``` ... ``` code fence starting at ``start``."""
    text_parts: list[str] = []
    j = start + 1
    while j < len(lines) and not lines[j].strip().startswith("```"):
        if lines[j].strip():
            text_parts.append(lines[j].strip())
        j += 1
    return {"text": " ".join(text_parts), "end": j}


def build_slot_table(lines: list[str], slot_cell_re: re.Pattern,
                     min_cells: int) -> dict[str, str]:
    """Map variant id -> slot label from the file's 槽位分布 table.

    Fallback only: used when a variant has no inline slot field.  The first
    cell must match ``slot_cell_re`` (e.g. ``R1..R9``/``F1..F9`` or
    ``M1..M10``/``M2.5``/``Q1..Q8``); the last cell lists variant ids.
    """
    table: dict[str, str] = {}
    for line in lines:
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < min_cells:
            continue
        m = slot_cell_re.match(cells[0])
        if not m:
            continue
        slot_label = m.group(1)
        for token in re.split(r"[,，、;；\s]+", cells[-1]):
            token = re.sub(r"[（(].*$", "", token).strip()
            if VARIANT_TOKEN_RE.match(token):
                table[token] = slot_label
    return table


def materialize_variants(variants, *, slug: str, relpath: str, slot_for,
                         primary_note=None, extra_note=None,
                         unparsed_where=None, extra_unparsed=None,
                         citekey_fallback=None):
    """变体对象列表 -> (entries, unparsed)。

    methods/results 共享的 materialize 段；theory 保留自己的 ``finalize_block``。
    钩子（缺省即 results 行为）：

    - ``slot_for(v) -> str``           适配槽位列取值（必传）；
    - ``primary_note(v) -> str``       主 verbatim 条目 note（缺省 ""）；
    - ``extra_note(v) -> str``         `.a/.b` 原文锚定条目 note（缺省 "原文锚定节"）；
    - ``unparsed_where(v) -> str``     空块待补录的「位置」列（缺省 `### 变体 <vid>`）；
    - ``extra_unparsed(v, unparsed)``  逐变体追加待补录（如 results 的槽位异常），
      在空块待补录之后调用以保持既有行序；
    - ``citekey_fallback(v) -> str|None``  citekey 回退源（如速查表来源列），仅在
      wb 标记与来源字段皆缺席时调用（不编造纪律的语料内回退）。
    """
    entries: list[Entry] = []
    unparsed: list[Unparsed] = []
    seq = 0
    for v in variants:
        slot = slot_for(v)
        if v.wb:
            citekey = "/".join(dict.fromkeys(v.wb))
        else:
            citekey = v.src
            if not citekey and citekey_fallback is not None:
                citekey = citekey_fallback(v)
            if not citekey:
                citekey = "未标注"
        base = f"{slug}#{v.vid}"

        if v.primary_verbatim is not None and v.primary_verbatim.strip():
            vtext = v.primary_verbatim.strip()
            if is_english(vtext):
                seq += 1
                entries.append(Entry(
                    id=base, slot=slot, citekey=citekey, text=normalize(vtext),
                    path=relpath, anchor=f"变体-{v.vid}", status="verbatim",
                    note=(primary_note(v) if primary_note else ""),
                    vid=v.vid, seq=seq))
            else:
                unparsed.append(Unparsed(card=v.vid, path=relpath,
                                         where="**原始句锚点**",
                                         text=normalize(vtext)[:200],
                                         reason="非英文原句（转述/笔记），已从 verbatim 剔除"))
        for k, ev in enumerate(v.extra_verbatim):
            seq += 1
            suffix = chr(ord("a") + k)
            entries.append(Entry(
                id=f"{base}.{suffix}", slot=slot, citekey=citekey, text=normalize(ev),
                path=relpath, anchor=f"变体-{v.vid}", status="verbatim",
                note=(extra_note(v) if extra_note else "原文锚定节"),
                vid=v.vid, seq=seq))
        for k, tpl in enumerate(v.templates):
            seq += 1
            tid = base.replace(f"#{v.vid}", f"#T{v.vid}")
            if len(v.templates) > 1:
                tid = f"{tid}.{k + 1}"
            has_bracket = "[" in tpl or "{" in tpl
            entries.append(Entry(
                id=tid, slot=slot, citekey=citekey, text=tpl,
                path=relpath, anchor=f"变体-{v.vid}", status="模板",
                note=("" if has_bracket else "无显式槽位占位符"),
                vid=v.vid, seq=seq))

        if not v.primary_verbatim and not v.extra_verbatim and not v.templates:
            reason = ("骨架字段存在但无句级模板（表格/散文）" if v.skeleton_seen
                      else "变体块内无 原始句锚点/原文锚定/骨架")
            where = unparsed_where(v) if unparsed_where else f"### 变体 {v.vid}"
            unparsed.append(Unparsed(card=v.vid, path=relpath,
                                     where=where, text=v.title[:200], reason=reason))
        if extra_unparsed is not None:
            extra_unparsed(v, unparsed)

    return entries, unparsed


# ---------------------------------------------------------- verification ----


def print_verbatim_check(entries, skill_root, nv_total: int) -> int:
    """verbatim 逐字回源校验（``--verify`` 前半段）；返回 mismatch 数。"""
    src_cache: dict[str, str] = {}
    mismatch = []
    for e in entries:
        if e.status != "verbatim":
            continue
        src = src_cache.get(e.path)
        if src is None:
            src = normalize((Path(skill_root) / e.path).read_text(encoding="utf-8"))
            src_cache[e.path] = src
        if normalize(e.text) not in src:
            mismatch.append(e)
    print(f"verbatim 回源校验: {nv_total - len(mismatch)}/{nv_total} 命中源文件")
    for e in mismatch:
        print(f"  MISMATCH {e.id} ({e.path}): {e.text[:90]}")
    return len(mismatch)


def print_sample_check(entries, skill_root, n: int) -> None:
    """``--sample N``：均匀抽 N 条 verbatim 逐字回源并打印。"""
    if n <= 0:
        return
    verbatim = [e for e in entries if e.status == "verbatim"]
    verbatim.sort(key=lambda e: e.id)
    n = min(n, len(verbatim))
    step = max(1, len(verbatim) // n)
    picked = verbatim[::step][:n]
    src_cache: dict[str, str] = {}
    print(f"\n抽样 {len(picked)} 条 verbatim 逐字回源：")
    for e in picked:
        src = src_cache.get(e.path)
        if src is None:
            src = normalize((Path(skill_root) / e.path).read_text(encoding="utf-8"))
            src_cache[e.path] = src
        hit = normalize(e.text) in src
        print(f"  {'OK ' if hit else 'MISS'} {e.id}: {e.text[:70]}…")


def print_report(stats, rendered: dict, nv_total: int, nt_total: int,
                 n_unparsed: int, extra_lines=()) -> None:
    """summary 表（``--quiet`` 时跳过）；extra_lines 追加在末尾。"""
    print("family                      variants  verbatim  templates  lines")
    for family, nvar, nv, nt, target in stats:
        lines = len(rendered[target].splitlines())
        print(f"{family['slug']:<27} {nvar:>8} {nv:>8} {nt:>10} {lines:>6}")
    print(f"{'TOTAL':<27} {sum(s[1] for s in stats):>8} {nv_total:>8} {nt_total:>10}")
    print(f"unparsed items: {n_unparsed}")
    for line in extra_lines:
        print(line)


# ------------------------------------------------------------ rendering ----


def render_table(title: str, rows: list[Entry]) -> list[str]:
    """methods/results 共享的 6 列表；theory 的 7 列表留在其适配器。"""
    out = [f"## {title}", "",
           "| id | 适配槽位 | citekey | 句子原文（或模板） | 卡片路径#锚点 | 状态 |",
           "|---|---|---|---|---|---|"]
    for e in rows:
        status = "verbatim" if e.status == "verbatim" else "模板"
        if e.note:
            status = f"{status}（{e.note}）"
        out.append(
            f"| `{e.id}` | {e.slot} | {escape_cell(e.citekey)} | {escape_cell(e.text)} | "
            f"`{e.path}#{e.anchor}` | {status} |")
    out.append("")
    return out


def render_slot_file(slug: str, name: str, slot_label: str, entries: list[Entry],
                     header_fn) -> str:
    """拆分子清单；``header_fn(fam, nv, nt, note)`` 由适配器提供（模板文本）。"""
    verbatim = [e for e in entries if e.status == "verbatim"]
    templates = [e for e in entries if e.status == "模板"]
    fam = {"slug": slug, "name": name}
    out = header_fn(fam, len(verbatim), len(templates),
                    note=f"本文件是 `{slug}.md` 的拆分子清单（槽位分组：{slot_label}）。")
    if verbatim:
        out += render_table("Verbatim 底本", verbatim)
    if templates:
        out += render_table("填槽模板", templates)
    return "\n".join(out).rstrip() + "\n"


def render_sub_route(slug: str, name: str, split_note: str,
                     groups: list[tuple[str, str, list]]) -> str:
    out = [
        f"# {slug} — 二级骨架清单（{name}，按槽位拆分）",
        "",
        "> 本目录由脚本重建，手改会被覆盖；重建命令 = `python scripts/build_indices.py`（路径基准：以本 skill 目录（SKILL.md 所在目录）为基准）。",
        split_note,
        "",
        "| 槽位 | 子清单 | verbatim | 模板 |",
        "|---|---|---|---|",
    ]
    for label, filename, entries in groups:
        nv = sum(1 for e in entries if e.status == "verbatim")
        nt = sum(1 for e in entries if e.status == "模板")
        out.append(f"| {label} | [`{filename}`]({filename}) | {nv} | {nt} |")
    out.append("")
    return "\n".join(out)


def render_unparsed(items: list[Unparsed]) -> str:
    out = [
        "# Skeleton Index — 待补录 / 未命中",
        "",
        "> 脚本未能自动判定为 verbatim 或模板的条目集中在此，**待人工补录**。",
        "",
    ]
    if not items:
        out.append("（无）")
    else:
        out.append("| 变体 | 卡片路径 | 位置 | 原文摘录 | 原因 |")
        out.append("|---|---|---|---|---|")
        for u in items:
            snippet = escape_cell(u.text[:160] + ("…" if len(u.text) > 160 else ""))
            out.append(f"| {u.card} | `{u.path}` | {u.where} | {snippet} | {u.reason} |")
    out.append("")
    return "\n".join(out)


# ------------------------------------------------------- write & cli ----


def load_quickref_sources(path: Path) -> dict[str, str]:
    """「变体速查表」（表头含 状态/来源 的明细表）→ {变体号: 来源列原文}。

    节边界只被同级或更高级标题截断（速查表节内的 ### 子节表全部纳入）；
    以 未标注/待补 开头的来源格视为占位符，不作为绑定来源。
    methods/results 适配器共用；仅作 citekey 回退源（wb 标记与来源字段缺席时）。
    """
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return {}
    start = next((i for i, ln in enumerate(lines)
                  if ln.strip().startswith("#") and "速查表" in ln), None)
    if start is None:
        return {}
    level = len(lines[start].strip()) - len(lines[start].strip().lstrip("#"))
    end = next((i for i in range(start + 1, len(lines))
                if (m := re.match(r"^(#+)\s", lines[i].strip()))
                and len(m.group(1)) <= level), len(lines))
    header_cols: dict[str, int] = {}
    out: dict[str, str] = {}
    for ln in lines[start + 1:end]:
        s = ln.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if all(set(c) <= {"-"} for c in cells):
            continue
        if any("状态" in c for c in cells) and any("来源" in c for c in cells):
            header_cols = {c: k for k, c in enumerate(cells) if c in ("状态", "来源")}
            continue
        if "来源" not in header_cols or len(cells) <= max(header_cols.values(), default=0):
            continue
        vid = cells[0].strip()
        if not vid or vid == "#":
            continue
        src = cells[header_cols["来源"]].strip()
        if src and not src.startswith(("未标注", "待补")):
            out.setdefault(vid, src)
    return out


def write_skeleton(skeleton_dir: Path, rendered: dict, route: str,
                   unparsed_text: str) -> None:
    skeleton_dir.mkdir(parents=True, exist_ok=True)
    for filename, text in rendered.items():
        (skeleton_dir / filename).write_text(text, encoding="utf-8", newline="\n")
    (skeleton_dir / "_index.md").write_text(route, encoding="utf-8", newline="\n")
    (skeleton_dir / "_unparsed.md").write_text(unparsed_text, encoding="utf-8",
                                               newline="\n")


def build_argparser(description: str) -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=description)
    ap.add_argument("--check", action="store_true",
                    help="build in memory and report, do not write")
    ap.add_argument("--verify", action="store_true",
                    help="verify verbatim byte-for-byte in source + anchor headings exist")
    ap.add_argument("--sample", type=int, default=0,
                    help="also print N evenly-spaced verbatim entries with source-hit")
    ap.add_argument("--quiet", action="store_true", help="only print the summary")
    return ap


def entrypoint(skill: str, main_fn, argv=None) -> int:
    """统一入口：异常转退出码 + 末尾 SUMMARY 行。

    ``main_fn(argv)`` 返回 0，或返回 counts dict（如
    ``{"entries": n, "unparsed": n, "mismatch": n, "anchor_miss": n}``，
    键可按模式省略）。
    """
    try:
        result = main_fn(argv)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}")
        return 2
    counts = result if isinstance(result, dict) else {}
    parts = " ".join(f"{k}={v}" for k, v in counts.items())
    print(f"SUMMARY skill={skill}" + (f" {parts}" if parts else ""))
    return 0
