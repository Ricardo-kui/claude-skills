#!/usr/bin/env python3
"""write-theory 骨架索引解析试点（Batch 2）：三套块结构统一 schema 验证。

范围
----
只解析 3 个样本文件（每套块结构各一），验证 variants / subprotocols / sentences
三套块结构能否统一为一种 entry schema，验证通过后即停，不全量。

- 分支① variants：corpus/variants/A_construct_differentiation.md
- 分支② subprotocols：corpus/subprotocols/hypothesis_derivation_patterns.md
- 分支③ sentences：corpus/sentences/hypothesis_forms.md

统一 entry schema（7 字段，三套字段名完全一致）
------------------------------------------------
  id       pattern_id（有则用）/ 变体名 / 句式名（verbatim 段加 .a/.b，模板加 .t1/.t2）
  func     段落功能位：variants=P 表 token；subprotocols=微观动作序列/排列模式；
           sentences=句位/论证角色
  citekey  source_papers 首个 citekey → wb 注释 → 来源字段 →「未标注」（不编造）
  status   ROBUST/VERIFIED/EMERGING（查 _evidence_registry.yaml）→「未标注」
  kind     verbatim | 模板
  text     verbatim 原文锚点（逐字）或填槽模板（含 [槽位]）
  anchor   corpus/<文件名>#<锚点>（变体号 / pattern_id / 标题）

抽取规则（先定后抽）
--------------------
verbatim  = ``**原文锚点**``/``**原文锚定**`` 下的引号内英文原句，逐字保留（含 ``…``
            省略号，不回填）；一行多引号拆成 .a/.b 多条，每条独立回源。
模板      = ``**骨架**``/``**模板**``/``**句式骨架**``/``**模板/骨架**``/``**结构**``
            后的代码围栏或 ``>`` 引用块（含 ``[槽位]`` 占位符的填槽骨架）。
锚点      = variants/subprotocols 指向真实标题（``### 变体 N`` / ``## Pattern: X``）；
            sentences 指向 ``### 标题``；``--verify`` 断言标题行存在。
citekey   = 优先 ``<!-- pattern_id: ...; source_papers:[...] -->`` 注释内的
            source_papers 首个值；无则 ``<!-- wb:<citekey>:... -->``；再无则
            ``**来源**`` 字段的 citekey 形 token；皆无标「未标注」。
status    = 查 _evidence_registry.yaml 的 patterns:/source_papers: 两节，
            按 pattern_id（含 sentence_/s_ 前缀变体）与 wb 注释 pattern token 匹配；
            命中即取 ROBUST>VERIFIED>EMERGING，未命中标「未标注」。

决策矩阵内嵌模板句（分支③ 特有）
--------------------------------
sentences 文件里带「模板/模板句」列的表，单元格内 ``"..."`` 引号且含 ``[槽位]``
的句子按模板收录（func=该节标题，citekey=未标注——它们是来源无关的形式模板）；
引号边界模糊（无 [槽位] 或无引号）的进 _unparsed。

Output
------
- corpus/_skeleton/_index.md   三套试点路由（<= 60 行）
- corpus/_skeleton/variants-A_construct_differentiation.md
- corpus/_skeleton/subprotocols-hypothesis_derivation_patterns.md
- corpus/_skeleton/sentences-hypothesis_forms.md
- corpus/_skeleton/_unparsed.md

CLI
---
--check        build in memory and report, do not write.
--verify       verbatim 逐字回源 + 锚点标题存在；--sample N 再抽 N 条逐字比对。
--sample N     抽样 N 条 verbatim 逐字回源。
--quiet        only print the summary.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPT_DIR.parent
CORPUS = SKILL_ROOT / "corpus"
SKELETON = CORPUS / "_skeleton"

# 三个样本文件（每套结构各一；相对 corpus/ 的路径）
SAMPLES = {
    "variants": "variants/A_construct_differentiation.md",
    "subprotocols": "subprotocols/hypothesis_derivation_patterns.md",
    "sentences": "sentences/hypothesis_forms.md",
}

# ---------------------------------------------------------------- 基础工具 ----

ANNOTATION_RE = re.compile(r"[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]")


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
    """Cut trailing CJK/fullwidth annotation glued to an English quote."""
    m = ANNOTATION_RE.search(text)
    if m:
        text = text[: m.start()]
    return text.strip().strip("\"'“”「」").strip()


def extract_quotes(text: str) -> list[str]:
    """Return all double-quoted segments in ``text``, trimmed of trailing CJK."""
    segs: list[str] = []
    for m in re.finditer(r'"([^"]+)"', text):
        seg = trim_annotation(m.group(1))
        if seg and is_english(seg):
            segs.append(seg)
    return segs


def _extract_verbatim_inline(lines: list[str], start: int, inline: str,
                             end: int) -> tuple[list[str], int]:
    """引号未闭合时吞后续行，再抽引号内原句；返回 (quotes, 结束行号)。"""
    text = inline
    j = start
    while text.count('"') % 2 == 1 and j + 1 < end:
        nxt = lines[j + 1].strip()
        if nxt == "" or nxt.startswith(("**", "#", "<!--", ">", "|")):
            break
        text += " " + nxt
        j += 1
    return extract_quotes(text), j


def _read_fence(lines: list[str], start: int) -> dict:
    """Collect a ``` ... ``` code fence starting at ``start``."""
    parts: list[str] = []
    j = start + 1
    while j < len(lines) and not lines[j].strip().startswith("```"):
        if lines[j].strip():
            parts.append(lines[j].strip())
        j += 1
    return {"text": normalize(" ".join(parts)), "end": j}


def _read_blockquote(lines: list[str], start: int) -> dict:
    """Collect consecutive ``> ...`` lines starting at ``start``."""
    parts: list[str] = []
    j = start
    while j < len(lines) and lines[j].strip().startswith(">"):
        body = lines[j].strip()[1:].strip()
        if body:
            parts.append(body)
        j += 1
    return {"text": normalize(" ".join(parts)), "end": j}


def _collect_comment(lines: list[str], start: int) -> dict:
    """Collect an HTML comment (possibly multi-line) starting at ``start``."""
    parts: list[str] = []
    j = start
    while j < len(lines):
        s = lines[j].strip()
        parts.append(s)
        if "-->" in s:
            break
        j += 1
    return {"text": " ".join(parts), "end": j}


PATTERN_ID_RE = re.compile(r"pattern_id:\s*([^\s;]+)")
SOURCE_PAPERS_RE = re.compile(r"source_papers:\s*\[([^\]]*)\]")
CONFIDENCE_RE = re.compile(r"confidence:\s*([^\s;]+)")
STATUS_RE = re.compile(r"status:\s*([^\s;]+)")
WB_RE = re.compile(r"<!--\s*wb:([^:\s>]+)(?::([^\s>]+))?")


def parse_comment(text: str) -> dict:
    """Extract pattern_id / source_papers / status / confidence from a comment."""
    out: dict = {"pattern_id": None, "source_papers": [], "status": None,
                 "confidence": None}
    m = PATTERN_ID_RE.search(text)
    if m:
        out["pattern_id"] = m.group(1)
    m = SOURCE_PAPERS_RE.search(text)
    if m:
        toks = []
        for tok in m.group(1).split(","):
            tok = strip_outer_quotes(tok).strip()
            tok = re.sub(r"[（(][^）)]*[）)]$", "", tok).strip()  # 去尾部括注
            if tok:
                toks.append(tok)
        out["source_papers"] = toks
    m = STATUS_RE.search(text)
    if m:
        out["status"] = m.group(1)
    m = CONFIDENCE_RE.search(text)
    if m:
        out["confidence"] = m.group(1)
    return out


# ---------------------------------------------------------------- registry ---

def load_status_registry() -> dict[str, str]:
    """Build {pattern_key -> status} from _evidence_registry.yaml.

    两个来源：patterns: 节（key -> status）与 source_papers: 节（fragment
    type -> status）。ROBUST > VERIFIED > EMERGING 优先级。
    """
    path = CORPUS / "_evidence_registry.yaml"
    if not path.exists():
        return {}
    rank = {"ROBUST": 3, "VERIFIED": 2, "EMERGING": 1}
    result: dict[str, str] = {}

    def add(key: str, status: str) -> None:
        if not key or not status:
            return
        status = status.upper().split()[0] if status else ""
        if status not in rank:
            return
        if key not in result or rank.get(result[key], 0) < rank[status]:
            result[key] = status

    lines = path.read_text(encoding="utf-8").splitlines()
    # 第一遍：patterns: 节（key -> status）
    section = None
    cur_key = None
    for raw in lines:
        s = raw.strip()
        if s == "patterns:":
            section = "patterns"
            continue
        if s == "source_papers:":
            section = "papers"
            continue
        if not s or s.startswith("#"):
            continue
        if section == "patterns":
            m = re.match(r"^([a-zA-Z0-9_.-]+):$", s)
            if m:
                cur_key = m.group(1)
                continue
            m = re.match(r"^status:\s*([^\s#]+)", s)
            if m and cur_key:
                add(cur_key, m.group(1))
    # 第二遍：source_papers: 节（fragment type -> 其后紧跟的 status）
    section = None
    last_type = None
    for raw in lines:
        s = raw.strip()
        if s == "source_papers:":
            section = "papers"
            continue
        if s == "patterns:":
            section = "patterns"
            continue
        if not s or s.startswith("#"):
            continue
        if section == "papers":
            m = re.match(r"^type:\s*([^\s#]+)", s)
            if m:
                last_type = m.group(1)
                continue
            m = re.match(r"^status:\s*([^\s#]+)", s)
            if m and last_type:
                add(last_type, m.group(1))
    return result


def resolve_status(registry: dict[str, str], pattern_id: str | None,
                   wb_pattern: str | None) -> str:
    candidates: list[str] = []
    if pattern_id:
        candidates += [pattern_id, "sentence_" + pattern_id, "s_" + pattern_id]
    if wb_pattern:
        candidates.append(wb_pattern)
    for c in candidates:
        if c in registry:
            return registry[c]
    return "未标注"


# ---------------------------------------------------------------- records ----

@dataclass
class Entry:
    id: str
    func: str
    citekey: str
    status: str
    kind: str          # verbatim | 模板
    text: str
    anchor: str
    heading: str = ""  # 内部：用于 --verify 断言标题存在
    file: str = ""     # 内部：corpus 相对路径


@dataclass
class Unparsed:
    card: str
    path: str
    where: str
    text: str
    reason: str


@dataclass
class Block:
    vid: str                 # 变体号 / pattern_id / 标题 slug
    title: str
    heading: str             # 精确标题行（供 --verify）
    pattern_id: str | None = None
    source_papers: list[str] = field(default_factory=list)
    inline_status: str | None = None
    wb_citekey: str | None = None
    wb_pattern: str | None = None
    src_field: str | None = None
    func: str = ""
    verbatim: list[str] = field(default_factory=list)
    templates: list[str] = field(default_factory=list)


def finalize_block(b: Block, branch: str, slug: str, relpath: str,
                   registry: dict[str, str]) -> tuple[list[Entry], list[Unparsed]]:
    entries: list[Entry] = []
    unparsed: list[Unparsed] = []
    base = b.pattern_id or (
        b.wb_pattern if (b.wb_pattern and not b.wb_pattern.startswith("legacy_"))
        else b.vid)
    citekey = b.source_papers[0] if b.source_papers else \
        (b.wb_citekey or _citekey_from_src(b.src_field) or "未标注")
    status = resolve_status(registry, b.pattern_id, b.wb_pattern)
    if status == "未标注" and b.inline_status and \
            b.inline_status.upper() in {"ROBUST", "VERIFIED", "EMERGING"}:
        status = b.inline_status.upper()
    func = b.func or "—"

    if not b.verbatim and not b.templates:
        return entries, unparsed

    for k, seg in enumerate(b.verbatim):
        suffix = chr(ord("a") + k)
        entries.append(Entry(
            id=f"{base}.{suffix}", func=func, citekey=citekey, status=status,
            kind="verbatim", text=normalize(seg),
            anchor=f"{relpath}#{_anchor_for(b, branch)}",
            heading=b.heading, file=relpath))
    for k, tpl in enumerate(b.templates):
        suffix = f".t{k + 1}"
        entries.append(Entry(
            id=f"{base}{suffix}", func=func, citekey=citekey, status=status,
            kind="模板", text=tpl,
            anchor=f"{relpath}#{_anchor_for(b, branch)}",
            heading=b.heading, file=relpath))
    return entries, unparsed


def _anchor_for(b: Block, branch: str) -> str:
    if branch == "subprotocols":
        return b.pattern_id or f"Pattern: {b.title}"
    return b.vid


def _citekey_from_src(src: str | None) -> str | None:
    if not src:
        return None
    m = re.match(r"^([a-z][a-z0-9_]{2,})", src.strip())
    return m.group(1) if m else None


# ---------------------------------------------------------------- 分支① -----

VARIANT_HDR_RE = re.compile(r"^###\s+(?:变体|技巧)\s+([^：:\s（(]+)")
SKELETON_FIELD_RE = re.compile(
    r"^\*\*(?:骨架|模板(?:/骨架)?|句式骨架|结构)\*\*\s*(?:[（(][^）)]*[）)])?\s*[:：]?\s*(.*)$")
VERBATIM_FIELD_RE = re.compile(
    r"^\*\*原文锚[点定]\*\*\s*(?:[（(][^）)]*[）)])?\s*[:：]\s*(.*)$")
SRC_FIELD_RE = re.compile(r"^\*\*(?:范文来源|来源|出处)\*\*\s*[:：]\s*(.*)$")
STATUS_FIELD_RE = re.compile(
    r"^\*\*(?:验证状态|状态)\*\*\s*[:：]\s*(VERIFIED|ROBUST|EMERGING)")


def _p_table_tokens(lines: list[str]) -> str:
    """首个「段落功能地图」表的 P token（如 P1 P2 P3 P4-P7 ...）。"""
    tokens: list[str] = []
    started = False
    for s in lines:
        s = s.strip()
        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if cells and re.match(r"^P\d+", cells[0]):
                tok = cells[0].split()[0]
                if tok not in tokens:
                    tokens.append(tok)
                started = True
                continue
        # 首个 P 表之后的非表格行即停止
        if started:
            break
    return " ".join(tokens)


def parse_variants(relpath: str, registry: dict[str, str]) -> tuple[list[Entry], list[Unparsed]]:
    path = SKILL_ROOT / relpath
    lines = [ln.rstrip("\r") for ln in path.read_text(encoding="utf-8").splitlines()]
    p_tokens = _p_table_tokens(lines)
    slug = "variants-A"
    entries: list[Entry] = []
    unparsed: list[Unparsed] = []
    cur: Block | None = None
    block_ranges: list[tuple[int, int]] = []
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("<!--"):
            cmt = _collect_comment(lines, i)
            i = cmt["end"] + 1
            meta = parse_comment(cmt["text"])
            wm = WB_RE.search(cmt["text"])
            if cur is not None:
                if meta["pattern_id"] and not cur.pattern_id:
                    cur.pattern_id = meta["pattern_id"]
                if meta["source_papers"] and not cur.source_papers:
                    cur.source_papers = meta["source_papers"]
                if wm and not cur.wb_citekey and                         (not wm.group(2) or not wm.group(2).startswith("legacy_")):
                    cur.wb_citekey = wm.group(1)
                    cur.wb_pattern = wm.group(2)
            continue
        m = VARIANT_HDR_RE.match(s)
        if m:
            if cur is not None:
                block_ranges.append((cur_range_start, i - 1))
                e, u = finalize_block(cur, "variants", slug, relpath, registry)
                entries += e
                unparsed += u
            cur = Block(vid=m.group(1), title=s, heading=s, func=p_tokens)
            cur_range_start = i
            i += 1
            continue
        # 章节边界（## 或非变体/技巧的 ###）关闭当前块
        if s.startswith("##") or (s.startswith("###") and not VARIANT_HDR_RE.match(s)):
            if cur is not None:
                block_ranges.append((cur_range_start, i - 1))
                e, u = finalize_block(cur, "variants", slug, relpath, registry)
                entries += e
                unparsed += u
                cur = None
            i += 1
            continue
        if cur is None:
            i += 1
            continue
        # --- 块内字段 ---
        fm = SRC_FIELD_RE.match(s)
        if fm:
            if not cur.src_field:
                cur.src_field = fm.group(1).strip()
            i += 1
            continue
        fm = VERBATIM_FIELD_RE.match(s)
        if fm:
            inline = fm.group(1).strip()
            if inline:
                qs, i = _extract_verbatim_inline(lines, i, inline, len(lines))
                cur.verbatim += qs
            elif i + 1 < len(lines) and lines[i + 1].strip().startswith(">"):
                bq = _read_blockquote(lines, i + 1)
                for q in extract_quotes(bq["text"]):
                    cur.verbatim.append(q)
                i = bq["end"] + 1
                continue
            i += 1
            continue
        fm = SKELETON_FIELD_RE.match(s)
        if fm:
            inline = fm.group(1).strip()
            if inline:
                cur.templates.append(normalize(strip_outer_quotes(inline)))
            elif i + 1 < len(lines) and lines[i + 1].strip().startswith("```"):
                fence = _read_fence(lines, i + 1)
                if fence["text"]:
                    cur.templates.append(fence["text"])
                i = fence["end"] + 1
                continue
            elif i + 1 < len(lines) and lines[i + 1].strip().startswith(">"):
                bq = _read_blockquote(lines, i + 1)
                if bq["text"]:
                    cur.templates.append(normalize(strip_outer_quotes(bq["text"])))
                i = bq["end"] + 1
                continue
            i += 1
            continue
        i += 1
    if cur is not None:
        block_ranges.append((cur_range_start, len(lines) - 1))
        e, u = finalize_block(cur, "variants", slug, relpath, registry)
        entries += e
        unparsed += u
    # 非变体/技巧块内的原文锚点 → _unparsed（分支① 未覆盖）
    for j, raw in enumerate(lines):
        if any(a <= j <= b for a, b in block_ranges):
            continue
        vm = VERBATIM_FIELD_RE.match(raw.strip())
        if vm:
            snippet = vm.group(1) or ""
            if not snippet and j + 1 < len(lines) and \
                    lines[j + 1].strip().startswith(">"):
                bq = _read_blockquote(lines, j + 1)
                qs = extract_quotes(bq["text"])
                snippet = qs[0] if qs else bq["text"][:160]
            unparsed.append(Unparsed(card="(非变体块)", path=relpath,
                                     where="关键句式模板/小节级 原文锚点",
                                     text=snippet[:160],
                                     reason="非 `### 变体`/`### 技巧` 块内锚点"))
    return entries, unparsed


# ---------------------------------------------------------------- 分支② -----

PATTERN_HDR_RE = re.compile(r"^##\s+Pattern:\s*(.*)$")
MICROSEQ_RE = re.compile(r"^\*\*微观动作序列\*\*\s*[:：]\s*(.*)$")
ARRANGE_RE = re.compile(r"^\*\*排列模式\*\*\s*[:：]\s*(.*)$")


def parse_subprotocols(relpath: str, registry: dict[str, str]) -> tuple[list[Entry], list[Unparsed]]:
    path = SKILL_ROOT / relpath
    lines = [ln.rstrip("\r") for ln in path.read_text(encoding="utf-8").splitlines()]
    slug = "subprotocols-hypothesis-derivation"
    entries: list[Entry] = []
    unparsed: list[Unparsed] = []

    # --- 阶段一：收集 pattern_id 注释（含行号）与各 pattern 块的 wb citekey ---
    pcomments: list[dict] = []
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("<!--"):
            cmt = _collect_comment(lines, i)
            meta = parse_comment(cmt["text"])
            if meta["pattern_id"]:
                pcomments.append({"idx": i, "meta": meta, "used": False})
            i = cmt["end"] + 1
        else:
            i += 1

    # 块边界
    block_starts: list[int] = []
    for j, raw in enumerate(lines):
        if PATTERN_HDR_RE.match(raw.strip()):
            block_starts.append(j)

    def is_gap_block(start: int, end: int) -> bool:
        for j in range(start, end):
            s = lines[j]
            if "wb-meta:" in s or s.strip().startswith("**band**"):
                return True
        return False

    # --- 阶段二：逐块解析；pattern_id 按「就近 + 跳过 gap 块」指针绑定 ---
    pc_idx = 0
    for bi, start in enumerate(block_starts):
        end = block_starts[bi + 1] if bi + 1 < len(block_starts) else len(lines)
        heading = lines[start].strip()
        title = PATTERN_HDR_RE.match(heading).group(1)

        # 消费本块起始前的 pattern_id 注释；最后一个为候选
        candidate = None
        while pc_idx < len(pcomments) and pcomments[pc_idx]["idx"] < start:
            candidate = pcomments[pc_idx]
            pc_idx += 1
        pid = None
        src_papers: list[str] = []
        inline_status = None
        if is_gap_block(start, end):
            if candidate is not None:
                pc_idx -= 1  # 还给下一个非 gap 块
        elif candidate is not None:
            pid = candidate["meta"]["pattern_id"]
            src_papers = candidate["meta"]["source_papers"]
            inline_status = candidate["meta"]["status"]

        cur = Block(vid=pid or _slug(title), title=title, heading=heading,
                    pattern_id=pid, source_papers=src_papers,
                    inline_status=inline_status)
        # 块内字段
        j = start + 1
        while j < end:
            s = lines[j].strip()
            if s.startswith("<!--"):
                cmt = _collect_comment(lines, j)
                j = cmt["end"] + 1
                wm = WB_RE.search(cmt["text"])
                if wm and not cur.wb_citekey and                         (not wm.group(2) or not wm.group(2).startswith("legacy_")):
                    cur.wb_citekey = wm.group(1)
                    cur.wb_pattern = wm.group(2)
                continue
            fm = MICROSEQ_RE.match(s) or ARRANGE_RE.match(s)
            if fm:
                if not cur.func:
                    cur.func = fm.group(1).strip()
                j += 1
                continue
            fm = SRC_FIELD_RE.match(s)
            if fm:
                if not cur.src_field:
                    cur.src_field = fm.group(1).strip()
                j += 1
                continue
            fm = VERBATIM_FIELD_RE.match(s)
            if fm:
                inline = fm.group(1).strip()
                if inline:
                    qs, j = _extract_verbatim_inline(lines, j, inline, end)
                    cur.verbatim += qs
                elif j + 1 < end and lines[j + 1].strip().startswith(">"):
                    bq = _read_blockquote(lines, j + 1)
                    cur.verbatim += extract_quotes(bq["text"])
                    j = bq["end"] + 1
                    continue
                j += 1
                continue
            fm = SKELETON_FIELD_RE.match(s)
            if fm:
                inline = fm.group(1).strip()
                if inline:
                    cur.templates.append(normalize(strip_outer_quotes(inline)))
                elif j + 1 < end and lines[j + 1].strip().startswith("```"):
                    fence = _read_fence(lines, j + 1)
                    if fence["text"]:
                        cur.templates.append(fence["text"])
                    j = fence["end"] + 1
                    continue
                j += 1
                continue
            j += 1
        e, u = finalize_block(cur, "subprotocols", slug, relpath, registry)
        entries += e
        unparsed += u
    return entries, unparsed


def _slug(title: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "-", title).strip("-").lower()
    s = s[:40]
    if not s:
        import hashlib
        s = "cjk-" + hashlib.sha1(title.encode("utf-8")).hexdigest()[:8]
    return s


# ---------------------------------------------------------------- 分支③ -----

SENT_BLOCK_HDR_RE = re.compile(r"^#{2,3}\s+(.*)$")
SENTPOS_RE = re.compile(r"^\*\*句位\*\*\s*[:：]\s*(.*)$")
ARG_ROLE_RE = re.compile(r"^>\s*论证角色\s*[:：]?\s*(.*)$")


def _block_vid(title: str) -> str:
    m = re.search(r"变体\s+([A-Z0-9]+)", title)
    if m:
        return f"变体-{m.group(1)}"
    m = re.search(r"句式\s+([A-Z0-9]+)", title)
    if m:
        return f"句式-{m.group(1)}"
    return _slug(title)


def parse_sentences(relpath: str, registry: dict[str, str]) -> tuple[list[Entry], list[Unparsed]]:
    path = SKILL_ROOT / relpath
    lines = [ln.rstrip("\r") for ln in path.read_text(encoding="utf-8").splitlines()]
    slug = "sentences-hypothesis-forms"
    entries: list[Entry] = []
    unparsed: list[Unparsed] = []
    arg_role = ""
    for s in lines:
        m = ARG_ROLE_RE.match(s.strip())
        if m:
            arg_role = m.group(1).strip()
            break

    cur: Block | None = None
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("<!--"):
            cmt = _collect_comment(lines, i)
            i = cmt["end"] + 1
            meta = parse_comment(cmt["text"])
            wm = WB_RE.search(cmt["text"])
            if cur is not None:
                if meta["pattern_id"] and not cur.pattern_id:
                    cur.pattern_id = meta["pattern_id"]
                if meta["source_papers"] and not cur.source_papers:
                    cur.source_papers = meta["source_papers"]
                if wm and not cur.wb_citekey and                         (not wm.group(2) or not wm.group(2).startswith("legacy_")):
                    cur.wb_citekey = wm.group(1)
                    cur.wb_pattern = wm.group(2)
            continue
        m = SENT_BLOCK_HDR_RE.match(s)
        if m:
            if cur is not None:
                e, u = finalize_block(cur, "sentences", slug, relpath, registry)
                entries += e
                unparsed += u
            cur = Block(vid=_block_vid(m.group(1)), title=m.group(1),
                        heading=s, func=arg_role)
            i += 1
            continue
        if cur is None:
            i += 1
            continue
        fm = SENTPOS_RE.match(s)
        if fm:
            cur.func = fm.group(1).strip()
            i += 1
            continue
        fm = STATUS_FIELD_RE.match(s)
        if fm and not cur.inline_status:
            cur.inline_status = fm.group(1).strip()
            i += 1
            continue
        fm = SRC_FIELD_RE.match(s)
        if fm:
            if not cur.src_field:
                cur.src_field = fm.group(1).strip()
            i += 1
            continue
        fm = VERBATIM_FIELD_RE.match(s)
        if fm:
            inline = fm.group(1).strip()
            if inline:
                qs, i = _extract_verbatim_inline(lines, i, inline, len(lines))
                cur.verbatim += qs
            elif i + 1 < len(lines) and lines[i + 1].strip().startswith(">"):
                bq = _read_blockquote(lines, i + 1)
                cur.verbatim += extract_quotes(bq["text"])
                i = bq["end"] + 1
                continue
            i += 1
            continue
        fm = SKELETON_FIELD_RE.match(s)
        if fm:
            inline = fm.group(1).strip()
            if inline:
                cur.templates.append(normalize(strip_outer_quotes(inline)))
            elif i + 1 < len(lines) and lines[i + 1].strip().startswith("```"):
                fence = _read_fence(lines, i + 1)
                if fence["text"]:
                    cur.templates.append(fence["text"])
                i = fence["end"] + 1
                continue
            elif i + 1 < len(lines) and lines[i + 1].strip().startswith(">"):
                bq = _read_blockquote(lines, i + 1)
                if bq["text"]:
                    cur.templates.append(normalize(strip_outer_quotes(bq["text"])))
                i = bq["end"] + 1
                continue
            i += 1
            continue
        i += 1
    if cur is not None:
        e, u = finalize_block(cur, "sentences", slug, relpath, registry)
        entries += e
        unparsed += u

    # --- 决策矩阵内嵌模板句 ---
    entries += _matrix_templates(lines, relpath, arg_role)
    return entries, unparsed


def _matrix_templates(lines: list[str], relpath: str, arg_role: str) -> list[Entry]:
    """决策矩阵/速查表单元格内 ``"..."`` 且含 [槽位] 的模板句 → 模板条目。"""
    out: list[Entry] = []
    seen: set[str] = set()
    section = arg_role or "决策矩阵"
    section_heading = ""
    for raw in lines:
        s = raw.strip()
        if s.startswith("##") or s.startswith("###"):
            section = s.lstrip("#").strip()
            section_heading = s
            continue
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        for cell in cells:
            for q in re.findall(r'"([^"]+)"', cell):
                q = q.strip()
                if "[" not in q or not is_english(q):
                    continue
                key = normalize(q)
                if key in seen:
                    continue
                seen.add(key)
                out.append(Entry(
                    id=f"matrix-{len(seen)}", func=section, citekey="未标注",
                    status="未标注", kind="模板", text=key,
                    anchor=f"{relpath}#{section}",
                    heading=section_heading, file=relpath))
    return out


# ---------------------------------------------------------------- 渲染 -----

def escape_cell(text: str) -> str:
    return text.replace("|", r"\|")


def render_branch(slug: str, name: str, branch: str, relpath: str,
                  entries: list[Entry]) -> str:
    nv = sum(1 for e in entries if e.kind == "verbatim")
    nt = sum(1 for e in entries if e.kind == "模板")
    out = [
        f"# {slug} — 骨架试点清单（{name}）",
        "",
        "> 本目录由脚本重建，手改会被覆盖；重建命令 = `python scripts/build_indices.py`（在 `write-theory/` 目录下）。",
        "> **统一 entry schema（7 字段，三套一致）**：`id` | `func`（段落功能位）| `citekey` | `status` | `kind`（verbatim/模板）| `text` | `anchor`。",
        "> **verbatim** = `**原文锚点**`/`**原文锚定**` 下引号内英文原句（逐字，含 `…` 不回填）；**模板** = `**骨架**`/`**模板**`/`**句式骨架**` 等后的代码围栏或 `>` 引用块（含 `[槽位]`）。",
        "> **citekey** 取 source_papers 首个 → wb 注释 → 来源字段，无则「未标注」；**status** 查 `_evidence_registry.yaml`（ROBUST>VERIFIED>EMERGING），未命中「未标注」。",
        f"> **来源文件**：`{relpath}`。",
        "",
        f"条目：verbatim {nv} 条 / 模板 {nt} 条。",
        "",
    ]
    out.append("| id | func | citekey | status | kind | text | anchor |")
    out.append("|---|---|---|---|---|---|---|")
    for e in entries:
        out.append(
            f"| `{e.id}` | {escape_cell(e.func)} | {escape_cell(e.citekey)} | "
            f"{e.status} | {e.kind} | {escape_cell(e.text)} | `{e.anchor}` |")
    out.append("")
    return "\n".join(out)


def render_index(stats: list[tuple[str, str, str, int, int]], unparsed_count: int) -> str:
    out = [
        "# write-theory 骨架索引解析试点（Batch 2，三套块结构）",
        "",
        "> 本目录由脚本重建；重建命令 = `python scripts/build_indices.py`（`--check` 干跑、`--verify` 回源校验）。",
        "> 本试点只解析 3 个样本文件，验证 variants / subprotocols / sentences 三套块结构可统一为一种 entry schema；验证通过后即停，不全量。",
        "> **统一 schema**：`id | func | citekey | status | kind | text | anchor`（7 字段，三套字段名完全一致）。",
        "",
        "| 分支 | 来源文件 | 子清单 | verbatim | 模板 |",
        "|---|---|---|---|---|",
    ]
    for name, relpath, target, nv, nt in stats:
        out.append(f"| {name} | `{relpath}` | [`{target}`]({target}) | {nv} | {nt} |")
    out.append("")
    nv_total = sum(s[3] for s in stats)
    nt_total = sum(s[4] for s in stats)
    out.append(f"合计：{len(stats)} 分支 / verbatim {nv_total} 条 / 模板 {nt_total} 条。")
    out.append("")
    out.append("## 待补录")
    out.append("")
    out.append(f"- [`_unparsed.md`](_unparsed.md)：{unparsed_count} 条（非块内锚点/边界模糊矩阵句等，待人工判定）。")
    out.append("")
    return "\n".join(out)


def render_unparsed(items: list[Unparsed]) -> str:
    out = [
        "# Skeleton Index — 待补录 / 未命中（试点）",
        "",
        "> 脚本未能自动判定为 verbatim/模板或结构不规整的条目集中在此。",
        "",
    ]
    if not items:
        out.append("（无）")
    else:
        out.append("| 卡片 | 路径 | 位置 | 原文摘录 | 原因 |")
        out.append("|---|---|---|---|---|")
        for u in items:
            snip = escape_cell(u.text[:140] + ("…" if len(u.text) > 140 else ""))
            out.append(f"| {u.card} | `{u.path}` | {u.where} | {snip} | {u.reason} |")
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------- main -----

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--sample", type=int, default=0)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    registry = load_status_registry()
    all_entries: list[Entry] = []
    all_unparsed: list[Unparsed] = []
    stats: list[tuple[str, str, str, int, int]] = []
    rendered: dict[str, str] = {}

    for branch, name, target in [
        ("variants", "① variants（变体/技巧块）",
         "variants-A_construct_differentiation.md"),
        ("subprotocols", "② subprotocols（pattern 库）",
         "subprotocols-hypothesis_derivation_patterns.md"),
        ("sentences", "③ sentences（变体块+决策矩阵）",
         "sentences-hypothesis_forms.md"),
    ]:
        relpath = "corpus/" + SAMPLES[branch]
        if branch == "variants":
            entries, unparsed = parse_variants(relpath, registry)
        elif branch == "subprotocols":
            entries, unparsed = parse_subprotocols(relpath, registry)
        else:
            entries, unparsed = parse_sentences(relpath, registry)
        all_entries += entries
        all_unparsed += unparsed
        nv = sum(1 for e in entries if e.kind == "verbatim")
        nt = sum(1 for e in entries if e.kind == "模板")
        rendered[target] = render_branch(target.replace(".md", ""), name, branch,
                                         relpath, entries)
        stats.append((name, relpath, target, nv, nt))

    nv_total = sum(1 for e in all_entries if e.kind == "verbatim")
    nt_total = sum(1 for e in all_entries if e.kind == "模板")

    # --- verification ---
    if args.verify:
        src_cache: dict[str, str] = {}
        mismatch: list[Entry] = []
        for e in all_entries:
            if e.kind != "verbatim":
                continue
            src = src_cache.get(e.file)
            if src is None:
                src = normalize((SKILL_ROOT / e.file).read_text(encoding="utf-8"))
                src_cache[e.file] = src
            if normalize(e.text) not in src:
                mismatch.append(e)
        print(f"verbatim 回源校验: {nv_total - len(mismatch)}/{nv_total} 命中源文件")
        for e in mismatch:
            print(f"  MISMATCH {e.id} ({e.file}): {e.text[:80]}")

        anchor_miss: list[Entry] = []
        for e in all_entries:
            if not e.heading:
                continue
            src = src_cache.get(e.file)
            if src is None:
                src = normalize((SKILL_ROOT / e.file).read_text(encoding="utf-8"))
                src_cache[e.file] = src
            if normalize(e.heading) not in src:
                anchor_miss.append(e)
        with_heading = sum(1 for e in all_entries if e.heading)
        print(f"锚点标题存在校验: {with_heading - len(anchor_miss)}/{with_heading} "
              f"锚点指向的标题存在")
        for e in anchor_miss:
            print(f"  ANCHOR-MISS {e.id} ({e.file}#{e.heading[:50]})")

        if args.sample > 0:
            verbatim = [e for e in all_entries if e.kind == "verbatim"]
            verbatim.sort(key=lambda e: e.id)
            n = min(args.sample, len(verbatim))
            step = max(1, len(verbatim) // n)
            picked = verbatim[::step][:n]
            print(f"\n抽样 {len(picked)} 条 verbatim 逐字回源：")
            for e in picked:
                src = src_cache.get(e.file)
                if src is None:
                    src = normalize((SKILL_ROOT / e.file).read_text(encoding="utf-8"))
                    src_cache[e.file] = src
                hit = normalize(e.text) in src
                print(f"  {'OK ' if hit else 'MISS'} {e.id}: {e.text[:70]}…")

    if not args.quiet:
        print("branch                      verbatim  templates")
        for name, relpath, target, nv, nt in stats:
            print(f"{name:<27} {nv:>8} {nt:>10}")
        print(f"{'TOTAL':<27} {nv_total:>8} {nt_total:>10}")
        print(f"unparsed items: {len(all_unparsed)}")
        print(f"registry pattern keys: {len(registry)}")

    if args.check:
        return 0

    SKELETON.mkdir(parents=True, exist_ok=True)
    for fname, text in rendered.items():
        (SKELETON / fname).write_text(text, encoding="utf-8", newline="\n")
    (SKELETON / "_index.md").write_text(render_index(stats, len(all_unparsed)),
                                        encoding="utf-8", newline="\n")
    (SKELETON / "_unparsed.md").write_text(render_unparsed(all_unparsed),
                                           encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
