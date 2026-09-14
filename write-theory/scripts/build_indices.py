#!/usr/bin/env python3
"""write-theory 骨架索引全量建（Batch 2）：统一 entry schema 覆盖三来源全部可抽文件。

范围
----
- variants/ 全部 7 族（A–G）：A/B/E/G 走分支①（`### 变体 N`/`### 技巧 N` 块）；
  C/D/F 走分支④（段落功能地图 + `### 技巧 N`/命名小节切块，fenced [槽位] 模板）。
- subprotocols/ 7 个 pattern 库：`## Pattern:`/`## Framework:` 顶层块 + `### 变体/子变体/
  子型/模式/Micro-Move/框架/句式` 子块；pattern_id 注释按「就近 + DEPRECATED 过滤 +
  同 token wb 就近回绑 + legacy_ 前缀过滤 + 跳过含 band/wb-meta 的 gap 块」绑定。
- sentences/ 全部 8 文件：变体/句式块 + 决策矩阵内嵌模板句。

统一 entry schema（7 字段，三来源字段名完全一致）
------------------------------------------------
  id       pattern_id（有则用）/ 变体名 / 句式名 / 技巧号（verbatim 加 .a/.b，模板加 .t1/.t2）
  func     段落功能位：variants=P 表 token/小节标题；subprotocols=微观动作序列/排列模式；
           sentences=句位/论证角色
  citekey  source_papers 首个 citekey → wb 注释 → 来源字段 →「未标注」（不编造）
  status   ROBUST/VERIFIED/EMERGING（查 _evidence_registry.yaml）→「未标注」
  kind     verbatim | 模板
  text     verbatim 原文锚点（逐字）或填槽模板（含 [槽位]）
  anchor   corpus/<文件名>#<锚点>（变体号 / pattern_id / 标题）

CLI
---
--check        build in memory and report, do not write.
--verify       verbatim 逐字回源 + 锚点标题存在；--sample N 再抽 N 条逐字比对。
--sample N     抽样 N 条 verbatim 逐字回源。
--quiet        only print the summary.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPT_DIR.parent
CORPUS = SKILL_ROOT / "corpus"
SKELETON = CORPUS / "_skeleton"

# ---------------------------------------------------------------- 文件清单 ----

# variants：族 -> (相对路径, 分支)  分支①=变体块；分支④=段落功能地图+小节
VARIANT_FILES: dict[str, tuple[str, str]] = {
    "A": ("variants/A_construct_differentiation.md", "branch1"),
    "B": ("variants/B_mechanism_elaboration.md", "branch1"),
    "C": ("variants/C_hypothesis_tree.md", "branch4"),
    "D": ("variants/D_process_theory.md", "branch4"),
    "E": ("variants/E_moderation.md", "branch1"),
    "F": ("variants/F_competing_hypotheses.md", "branch4"),
    "G": ("variants/G_dialectical_opposition.md", "branch1"),
}

SUBPROTOCOL_FILES: list[str] = [
    "subprotocols/hypothesis_derivation_patterns.md",
    "subprotocols/argumentation_patterns.md",
    "subprotocols/hypothesis_organization_patterns.md",
    "subprotocols/evidence_patterns.md",
    "subprotocols/construct_differentiation_patterns.md",
    "subprotocols/moderator_selection_frameworks.md",
    "subprotocols/bilateral_argumentation_templates.md",
]

SENTENCE_FILES: list[str] = [
    "sentences/acknowledgment_response.md",
    "sentences/closure.md",
    "sentences/construct_definition.md",
    "sentences/cost_benefit_calculus.md",
    "sentences/hypothesis_forms.md",
    "sentences/leitmotif-section-opener.md",
    "sentences/mechanism_chain.md",
    "sentences/moderation.md",
]

VARIANT_NAMES = {
    "A": "构念辨析型", "B": "机制推演型", "C": "假设树型", "D": "质性/过程理论型",
    "E": "调节效应型", "F": "竞争假设型", "G": "辩证对立型",
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
                 "confidence": None, "deprecated": False}
    if "DEPRECATED" in text:
        out["deprecated"] = True
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


def finalize_block(b: Block, branch: str, relpath: str,
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
    if branch == "variants4":
        return b.vid
    return b.vid


def _citekey_from_src(src: str | None) -> str | None:
    if not src:
        return None
    m = re.match(r"^([a-z][a-z0-9_]{2,})", src.strip())
    return m.group(1) if m else None


def _slug(title: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "-", title).strip("-").lower()
    s = s[:40]
    if not s:
        s = "cjk-" + hashlib.sha1(title.encode("utf-8")).hexdigest()[:8]
    elif re.search(r"[\u4e00-\u9fff]", title):
        # CJK 标题：ASCII 部分可能碰撞，附 hash 兜底
        s = (s[:28] + "-" + hashlib.sha1(title.encode("utf-8")).hexdigest()[:6]).strip("-")
    return s


def _block_vid(title: str) -> str:
    """标题 → 稳定 vid（sentences 分支用）。"""
    m = re.search(r"变体\s+([A-Z0-9]+)", title)
    if m:
        return f"变体-{m.group(1)}"
    m = re.search(r"句式\s+([A-Z0-9]+)", title)
    if m:
        return f"句式-{m.group(1)}"
    return _slug(title)


def _branch4_vid(title: str) -> str:
    """标题 → 稳定 vid（variants 分支④用）。"""
    t = title.strip()
    m = re.search(r"技巧\s*(\d+)", t)
    if m:
        return f"技巧-{m.group(1)}"
    m = re.search(r"变体\s+([A-Za-z0-9]+)", t)
    if m:
        return f"变体-{m.group(1)}"
    m = re.search(r"句式\s+([A-Za-z0-9]+)", t)
    if m:
        return f"句式-{m.group(1)}"
    core = re.split(r"[：:（(]", t)[0].strip()
    return _slug(core)


# ---------------------------------------------------------------- 字段正则 --

VARIANT_HDR_RE = re.compile(r"^###\s+(?:变体|技巧)\s+([^：:\s（(]+)")
SKELETON_FIELD_RE = re.compile(
    r"^\*\*([^*\n]*(?:骨架|模板|句式|结构)[^*\n]*)\*\*\s*"
    r"(?:[（(][^）)]*[）)])?\s*[:：]?\s*(.*)$")
VERBATIM_FIELD_RE = re.compile(
    r"^\*\*原文锚[点定]\*\*\s*(?:[（(][^）)]*[）)])?\s*[:：]\s*(.*)$")
SRC_FIELD_RE = re.compile(r"^\*\*(?:范文来源|来源|出处)\*\*\s*[:：]\s*(.*)$")
STATUS_FIELD_RE = re.compile(
    r"^\*\*(?:验证状态|状态)\*\*\s*[:：]\s*(VERIFIED|ROBUST|EMERGING)")


# ---------------------------------------------------------------- 分支① -----

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
        if started:
            break
    return " ".join(tokens)


def _markdown_headers(lines: list[str]) -> list[tuple[int, str]]:
    """(line, stripped_text) for ##/### 标题（跳过代码围栏内伪标题）。"""
    out: list[tuple[int, str]] = []
    in_fence = False
    for j, raw in enumerate(lines):
        s = raw.strip()
        if s.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if s.startswith("##"):
            out.append((j, s))
    return out


def _bind_variant_ids(lines: list[str], block_starts: list[int],
                      all_headers: list[int], pcomments: list[dict],
                      wb_lines: list[dict]) -> dict[int, dict]:
    """pattern_id 注释绑定到 `### 变体`/`### 技巧` 块。

    - 同 token wb 紧随其后（到下一标题/文末）→ 后置约定，绑到最近前一个块。
    - 否则为前置约定，绑到紧随其后的块标题（若下一标题是块标题）。
    - 其余（`##` 级注释）→ 不绑（孤儿）。
    """
    bound: dict[int, dict] = {}
    for pc in pcomments:
        idx = pc["idx"]
        next_hdr = next((h for h in all_headers if h > idx), len(lines))
        post = None
        for w in wb_lines:
            if idx < w["idx"] < next_hdr and _same_token(w["pattern"], pc["pid"]):
                post = w
                break
        if post is not None:
            prev = [b for b in block_starts if b < idx]
            if prev:
                bound[prev[-1]] = pc
        else:
            if next_hdr in block_starts:
                bound[next_hdr] = pc
    return bound


def parse_variants(relpath: str, registry: dict[str, str],
                   slug: str) -> tuple[list[Entry], list[Unparsed]]:
    path = SKILL_ROOT / relpath
    lines = [ln.rstrip("\r") for ln in path.read_text(encoding="utf-8").splitlines()]
    p_tokens = _p_table_tokens(lines)
    entries: list[Entry] = []
    unparsed: list[Unparsed] = []

    # --- 阶段一：收集注释 / wb / 块边界 ---
    pcomments: list[dict] = []
    wb_lines: list[dict] = []
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("<!--"):
            cmt = _collect_comment(lines, i)
            meta = parse_comment(cmt["text"])
            if meta["pattern_id"] and not meta["deprecated"]:
                pcomments.append({"idx": i, "pid": meta["pattern_id"], "meta": meta})
            wm = WB_RE.search(cmt["text"])
            if wm:
                wb_lines.append({"idx": i, "citekey": wm.group(1),
                                 "pattern": wm.group(2)})
            i = cmt["end"] + 1
        else:
            i += 1

    block_starts: list[int] = []
    block_meta: dict[int, tuple[str, str]] = {}
    headers = _markdown_headers(lines)
    all_headers = [j for j, _ in headers]
    for j, s in headers:
        m = VARIANT_HDR_RE.match(s)
        if m:
            block_starts.append(j)
            block_meta[j] = (m.group(1), s)

    bound = _bind_variant_ids(lines, block_starts, all_headers, pcomments, wb_lines)
    block_ranges: list[tuple[int, int]] = []

    # --- 阶段二：逐块解析 ---
    for start in block_starts:
        end = next((h for h in all_headers if h > start), len(lines))
        vid, heading = block_meta[start]
        pc = bound.get(start)
        pid = pc["pid"] if pc else None
        src_papers = pc["meta"]["source_papers"] if pc else []
        inline_status = pc["meta"]["status"] if pc else None
        cur = Block(vid=vid, title=heading, heading=heading, pattern_id=pid,
                    source_papers=src_papers, inline_status=inline_status,
                    func=p_tokens)
        block_ranges.append((start, end - 1))
        j = start + 1
        while j < end:
            s = lines[j].strip()
            if s.startswith("<!--"):
                cmt = _collect_comment(lines, j)
                j = cmt["end"] + 1
                wm = WB_RE.search(cmt["text"])
                if wm and not cur.wb_citekey and \
                        (not wm.group(2) or not wm.group(2).startswith("legacy_")):
                    cur.wb_citekey = wm.group(1)
                    cur.wb_pattern = wm.group(2)
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
                    for q in extract_quotes(bq["text"]):
                        cur.verbatim.append(q)
                    j = bq["end"] + 1
                    continue
                j += 1
                continue
            fm = SKELETON_FIELD_RE.match(s)
            if fm:
                inline = fm.group(2).strip()
                if inline:
                    cur.templates.append(normalize(strip_outer_quotes(inline)))
                elif j + 1 < end and lines[j + 1].strip().startswith("```"):
                    fence = _read_fence(lines, j + 1)
                    if fence["text"]:
                        cur.templates.append(fence["text"])
                    j = fence["end"] + 1
                    continue
                elif j + 1 < end and lines[j + 1].strip().startswith(">"):
                    bq = _read_blockquote(lines, j + 1)
                    if bq["text"]:
                        cur.templates.append(normalize(strip_outer_quotes(bq["text"])))
                    j = bq["end"] + 1
                    continue
                else:
                    parts: list[str] = []
                    k = j + 1
                    while k < end:
                        ns = lines[k].strip()
                        if not ns or ns.startswith(("**", "#", "<!--", "|", "```", "---")):
                            break
                        parts.append(ns)
                        k += 1
                    if parts:
                        cur.templates.append(normalize(" ".join(parts)))
                        j = k - 1
                j += 1
                continue
            j += 1
        e, u = finalize_block(cur, "variants", relpath, registry)
        entries += e
        unparsed += u

    # 非变体/技巧块内的原文锚点 → _unparsed
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
            unparsed.append(Unparsed(
                card="(非变体块)", path=relpath, where="关键句式模板/小节级 原文锚点",
                text=snippet[:160],
                reason="非 `### 变体`/`### 技巧` 块内锚点：无块级变体号/pattern_id 可绑定，"
                       "citekey/status 无法稳定回源，故不进主清单（待人工判定归属）。"))
    return entries, unparsed


# ---------------------------------------------------------------- 分支④ -----

SENT_BLOCK_HDR_RE = re.compile(r"^#{2,3}\s+(.*)$")


def parse_variants_branch4(relpath: str, registry: dict[str, str],
                           slug: str) -> tuple[list[Entry], list[Unparsed]]:
    """C/D/F：段落功能地图 P 表 + `### 技巧 N`/命名小节切块。

    - 块边界 = 任意 `##`/`###` 标题（标题行即 anchor 指向的真实标题）。
    - func = 该块标题（段落功能位）。
    - verbatim = `**原文锚点**`/`**原文锚定**` 下引号内英文原句（逐字）。
    - 模板 = 任意 ``` fenced 块且含 `[槽位]`（骨架/句式/过程模型/命题模板统一走此）。
    - pattern_id/citekey = 块内 `<!-- pattern_id ... -->` + `<!-- wb:... -->` 注释。
    """
    path = SKILL_ROOT / relpath
    lines = [ln.rstrip("\r") for ln in path.read_text(encoding="utf-8").splitlines()]
    entries: list[Entry] = []
    unparsed: list[Unparsed] = []
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
                if wm and not cur.wb_citekey and \
                        (not wm.group(2) or not wm.group(2).startswith("legacy_")):
                    cur.wb_citekey = wm.group(1)
                    cur.wb_pattern = wm.group(2)
            continue
        m = SENT_BLOCK_HDR_RE.match(s)
        if m:
            if cur is not None:
                e, u = finalize_block(cur, "variants4", relpath, registry)
                entries += e
                unparsed += u
            title = m.group(1).strip()
            cur = Block(vid=_branch4_vid(title), title=title, heading=s, func=title)
            i += 1
            continue
        if cur is None:
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
        if s.startswith("```"):
            fence = _read_fence(lines, i)
            if fence["text"] and "[" in fence["text"] and "]" in fence["text"]:
                cur.templates.append(fence["text"])
            i = fence["end"] + 1
            continue
        i += 1
    if cur is not None:
        e, u = finalize_block(cur, "variants4", relpath, registry)
        entries += e
        unparsed += u
    return entries, unparsed


# ---------------------------------------------------------------- 分支② -----

PATTERN_HDR_RE = re.compile(
    r"^##\s+(?:Pattern|Framework)(?:\s+[A-Za-z])?\s*[:：]\s*(.*)$")
SUB_HDR_RE = re.compile(
    r"^###\s+(?:变体|子变体|子型|模式|Micro-Move|框架|句式|Pattern)\s*[:：]?\s*(.*)$")
MICROSEQ_RE = re.compile(r"^\*\*微观动作序列\*\*\s*[:：]\s*(.*)$")
ARRANGE_RE = re.compile(r"^\*\*排列模式\*\*\s*[:：]\s*(.*)$")


def _same_token(wb_pattern: str | None, pid: str | None) -> bool:
    if not wb_pattern or not pid:
        return False
    if wb_pattern.startswith("legacy_"):
        return False
    return wb_pattern == pid or wb_pattern.endswith(pid)


def parse_subprotocols(relpath: str, registry: dict[str, str],
                       slug: str) -> tuple[list[Entry], list[Unparsed]]:
    path = SKILL_ROOT / relpath
    lines = [ln.rstrip("\r") for ln in path.read_text(encoding="utf-8").splitlines()]
    entries: list[Entry] = []
    unparsed: list[Unparsed] = []

    # --- 阶段一：收集 pattern_id 注释（过滤 DEPRECATED 指针）与全部块边界 ---
    pcomments: list[dict] = []
    wb_lines: list[dict] = []      # {idx, citekey, pattern}
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("<!--"):
            cmt = _collect_comment(lines, i)
            meta = parse_comment(cmt["text"])
            if meta["pattern_id"] and not meta["deprecated"]:
                pcomments.append({"idx": i, "pid": meta["pattern_id"],
                                  "meta": meta})
            wm = WB_RE.search(cmt["text"])
            if wm:
                wb_lines.append({"idx": i, "citekey": wm.group(1),
                                 "pattern": wm.group(2)})
            i = cmt["end"] + 1
        else:
            i += 1

    block_starts: list[tuple[int, str, str]] = []  # (line, title, level)
    headers = _markdown_headers(lines)
    all_headers = [j for j, _ in headers]
    for j, s in headers:
        m = PATTERN_HDR_RE.match(s)
        if m:
            block_starts.append((j, m.group(1).strip(), "##"))
            continue
        m = SUB_HDR_RE.match(s)
        if m:
            block_starts.append((j, m.group(1).strip(), "###"))

    def block_content_has_gap(start: int, end: int) -> bool:
        for j in range(start, end):
            s = lines[j]
            if "wb-meta:" in s or s.strip().startswith("**band**"):
                return True
        return False

    # --- 阶段二：pattern_id 注释绑定到块 ---
    # 规则：
    #   1) 若注释后（到下一块边界/文末）出现同 token 的 wb 注释 → 后置约定，绑到
    #      最近的前一个块（注释所在块）。
    #   2) 否则为前置约定，绑到最近的下一个非 gap 块。
    bound: dict[int, dict] = {}   # block_start_line -> pcomment
    starts = [s[0] for s in block_starts]
    for pc in pcomments:
        idx = pc["idx"]
        # 找注释后的下一个 wb（同 token 判定）是否在下一块边界之前
        next_block = next((s for s in starts if s > idx), len(lines))
        post_anchor = None
        for w in wb_lines:
            if idx < w["idx"] < next_block and _same_token(w["pattern"], pc["pid"]):
                post_anchor = w
                break
        if post_anchor is not None:
            # 绑到最近前一个块
            prev = [s for s in starts if s < idx]
            if prev:
                target = prev[-1]
                bound[target] = pc
        else:
            # 绑到最近下一个非 gap 块
            for k, s0 in enumerate(starts):
                if s0 <= idx:
                    continue
                end = next((h for h in all_headers if h > s0), len(lines))
                if block_content_has_gap(s0, end):
                    continue
                bound[s0] = pc
                break

    # --- 阶段三：逐块解析 ---
    for bi, (start, title, level) in enumerate(block_starts):
        end = next((h for h in all_headers if h > start), len(lines))
        heading = lines[start].strip()
        pc = bound.get(start)
        pid = pc["pid"] if pc else None
        src_papers = pc["meta"]["source_papers"] if pc else []
        inline_status = pc["meta"]["status"] if pc else None
        cur = Block(vid=pid or _slug(title), title=title, heading=heading,
                    pattern_id=pid, source_papers=src_papers,
                    inline_status=inline_status)
        j = start + 1
        while j < end:
            s = lines[j].strip()
            if s.startswith("<!--"):
                cmt = _collect_comment(lines, j)
                j = cmt["end"] + 1
                wm = WB_RE.search(cmt["text"])
                if wm and not cur.wb_citekey and \
                        (not wm.group(2) or not wm.group(2).startswith("legacy_")):
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
                inline = fm.group(2).strip()
                if inline:
                    cur.templates.append(normalize(strip_outer_quotes(inline)))
                elif j + 1 < end and lines[j + 1].strip().startswith("```"):
                    fence = _read_fence(lines, j + 1)
                    if fence["text"]:
                        cur.templates.append(fence["text"])
                    j = fence["end"] + 1
                    continue
                elif j + 1 < end and lines[j + 1].strip().startswith(">"):
                    bq = _read_blockquote(lines, j + 1)
                    if bq["text"]:
                        cur.templates.append(normalize(strip_outer_quotes(bq["text"])))
                    j = bq["end"] + 1
                    continue
                else:
                    # 骨架/模板后的纯文本续行（inline 模板）
                    parts: list[str] = []
                    k = j + 1
                    while k < end:
                        ns = lines[k].strip()
                        if not ns or ns.startswith(("**", "#", "<!--", "|", "```", "---")):
                            break
                        parts.append(ns)
                        k += 1
                    if parts:
                        cur.templates.append(normalize(" ".join(parts)))
                        j = k - 1
                j += 1
                continue
            j += 1
        e, u = finalize_block(cur, "subprotocols", relpath, registry)
        entries += e
        unparsed += u
    return entries, unparsed


# ---------------------------------------------------------------- 分支③ -----

SENTPOS_RE = re.compile(r"^\*\*句位\*\*\s*[:：]\s*(.*)$")
ARG_ROLE_RE = re.compile(r"^>\s*论证角色\s*[:：]?\s*(.*)$")


def parse_sentences(relpath: str, registry: dict[str, str],
                    slug: str) -> tuple[list[Entry], list[Unparsed]]:
    path = SKILL_ROOT / relpath
    lines = [ln.rstrip("\r") for ln in path.read_text(encoding="utf-8").splitlines()]
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
                if wm and not cur.wb_citekey and \
                        (not wm.group(2) or not wm.group(2).startswith("legacy_")):
                    cur.wb_citekey = wm.group(1)
                    cur.wb_pattern = wm.group(2)
            continue
        m = SENT_BLOCK_HDR_RE.match(s)
        if m:
            if cur is not None:
                e, u = finalize_block(cur, "sentences", relpath, registry)
                entries += e
                unparsed += u
            cur = Block(vid=_block_vid(m.group(1)), title=m.group(1),
                        heading=s, func=arg_role)
            i += 1
            continue
        if cur is None:
            i += 1
            continue
        fm = ARG_ROLE_RE.match(s)
        if fm:
            cur.func = fm.group(1).strip()
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
            inline = fm.group(2).strip()
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
            else:
                parts: list[str] = []
                k = i + 1
                while k < len(lines):
                    ns = lines[k].strip()
                    if not ns or ns.startswith(("**", "#", "<!--", "|", "```", "---")):
                        break
                    parts.append(ns)
                    k += 1
                if parts:
                    cur.templates.append(normalize(" ".join(parts)))
                    i = k - 1
            i += 1
            continue
        i += 1
    if cur is not None:
        e, u = finalize_block(cur, "sentences", relpath, registry)
        entries += e
        unparsed += u

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
        f"# {slug} — 骨架清单（{name}）",
        "",
        "> 本目录由脚本重建，手改会被覆盖；重建命令 = `python scripts/build_indices.py`（路径基准：以本 skill 目录（SKILL.md 所在目录）为基准）。",
        "> **统一 entry schema（7 字段）**：`id` | `func`（段落功能位）| `citekey` | `status` | `kind`（verbatim/模板）| `text` | `anchor`。",
        "> **verbatim** = `**原文锚点**`/`**原文锚定**` 下引号内英文原句（逐字，含 `…` 不回填）；**模板** = `**骨架**`/`**模板**`/`**句式**` 等后的代码围栏或 `>` 引用块（含 `[槽位]`）。",
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


def render_index(routes: list[dict], unparsed_count: int) -> str:
    out = [
        "# write-theory 骨架索引（Batch 2 全量）",
        "",
        "> 本目录由脚本重建；重建命令 = `python scripts/build_indices.py`（`--check` 干跑、`--verify` 回源校验）。",
        "> **统一 schema**：`id | func | citekey | status | kind | text | anchor`（7 字段，三来源字段名完全一致）。",
        "> **verbatim** 逐字回源；**锚点** 指向真实标题/变体号/pattern_id；**citekey** 不编造（无机器可读 token 标「未标注」）。",
        "",
        "## 一级路由：变体族 A–G",
        "",
        "| 族 | 来源文件 | 子清单 | verbatim | 模板 |",
        "|---|---|---|---|---|",
    ]
    for r in routes:
        if r["group"] != "variants":
            continue
        out.append(
            f"| {r['label']} | `{r['relpath']}` | [`{r['target']}`]({r['target']}) "
            f"| {r['nv']} | {r['nt']} |")
    out.append("")
    out.append("## 来源子清单：subprotocols pattern 库")
    out.append("")
    out.append("| 库 | 来源文件 | 子清单 | verbatim | 模板 |")
    out.append("|---|---|---|---|---|")
    for r in routes:
        if r["group"] != "subprotocols":
            continue
        out.append(
            f"| {r['label']} | `{r['relpath']}` | [`{r['target']}`]({r['target']}) "
            f"| {r['nv']} | {r['nt']} |")
    out.append("")
    out.append("## 来源子清单：sentences 句式库")
    out.append("")
    out.append("| 文件 | 子清单 | verbatim | 模板 |")
    out.append("|---|---|---|---|")
    for r in routes:
        if r["group"] != "sentences":
            continue
        out.append(
            f"| {r['label']} | [`{r['target']}`]({r['target']}) "
            f"| {r['nv']} | {r['nt']} |")
    out.append("")
    nv_total = sum(r["nv"] for r in routes)
    nt_total = sum(r["nt"] for r in routes)
    out.append(f"合计：{len(routes)} 个子清单 / verbatim {nv_total} 条 / 模板 {nt_total} 条。")
    out.append("")
    out.append("## 待补录")
    out.append("")
    out.append(f"- [`_unparsed.md`](_unparsed.md)：{unparsed_count} 条（每条附「为什么进不了主清单」）。")
    out.append("")
    return "\n".join(out)


def render_unparsed(items: list[Unparsed]) -> str:
    out = [
        "# Skeleton Index — 待补录 / 未命中",
        "",
        "> 脚本未能自动判定为 verbatim/模板或结构不规整、无法绑定 citekey/status 的条目集中在此；每条附「为什么进不了主清单」。",
        "",
    ]
    if not items:
        out.append("（无）")
    else:
        out.append("| 卡片 | 路径 | 位置 | 原文摘录 | 为什么进不了主清单 |")
        out.append("|---|---|---|---|---|")
        for u in items:
            snip = escape_cell(u.text[:140] + ("…" if len(u.text) > 140 else ""))
            out.append(f"| {u.card} | `{u.path}` | {u.where} | {snip} | {u.reason} |")
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------- main -----

def _target_name(relpath: str, branch: str) -> str:
    stem = Path(relpath).stem
    prefix = {"variants": "variants", "variants4": "variants",
              "subprotocols": "subprotocols", "sentences": "sentences"}[branch]
    return f"{prefix}-{stem}.md"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--sample", type=int, default=0)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    registry = load_status_registry()
    all_entries: list[Entry] = []
    all_unparsed: list[Unparsed] = []
    routes: list[dict] = []
    rendered: dict[str, str] = {}

    # ---- variants ----
    for fam, (rel, branch) in VARIANT_FILES.items():
        rpath = "corpus/" + rel
        slug = f"variants-{Path(rel).stem}"
        if branch == "branch1":
            entries, unparsed = parse_variants(rpath, registry, slug)
        else:
            entries, unparsed = parse_variants_branch4(rpath, registry, slug)
        all_entries += entries
        all_unparsed += unparsed
        target = _target_name(rel, "variants4" if branch == "branch4" else "variants")
        _emit(rendered, routes, target, entries, unparsed, rpath,
              f"{fam}（{VARIANT_NAMES.get(fam, '')}）", "variants")

    # ---- subprotocols ----
    for rel in SUBPROTOCOL_FILES:
        rpath = "corpus/" + rel
        slug = f"subprotocols-{Path(rel).stem}"
        entries, unparsed = parse_subprotocols(rpath, registry, slug)
        all_entries += entries
        all_unparsed += unparsed
        target = _target_name(rel, "subprotocols")
        _emit(rendered, routes, target, entries, unparsed, rpath,
              Path(rel).stem, "subprotocols")

    # ---- sentences ----
    for rel in SENTENCE_FILES:
        rpath = "corpus/" + rel
        slug = f"sentences-{Path(rel).stem}"
        entries, unparsed = parse_sentences(rpath, registry, slug)
        all_entries += entries
        all_unparsed += unparsed
        target = _target_name(rel, "sentences")
        _emit(rendered, routes, target, entries, unparsed, rpath,
              Path(rel).stem, "sentences")

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
        for e in mismatch[:20]:
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
        for e in anchor_miss[:20]:
            print(f"  ANCHOR-MISS {e.id} ({e.file}#{e.heading[:50]})")

        # 分来源汇总表
        print("\n分来源汇总：")
        print(f"{'来源':<16}{'verbatim':>10}{'模板':>10}{'未标注(条)':>12}")
        for grp, label in [("variants", "variants"), ("subprotocols", "subprotocols"),
                           ("sentences", "sentences")]:
            grp_entries = [e for e in all_entries
                           if e.file.split("/")[1] == grp]
            gnv = sum(1 for e in grp_entries if e.kind == "verbatim")
            gnt = sum(1 for e in grp_entries if e.kind == "模板")
            gna = sum(1 for e in grp_entries if e.status == "未标注")
            print(f"{label:<16}{gnv:>10}{gnt:>10}{gna:>12}")

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
        print("source                     verbatim  templates")
        for r in routes:
            print(f"{r['target']:<28} {r['nv']:>8} {r['nt']:>10}")
        print(f"{'TOTAL':<28} {nv_total:>8} {nt_total:>10}")
        print(f"unparsed items: {len(all_unparsed)}")
        print(f"registry pattern keys: {len(registry)}")

    if args.check:
        return 0

    SKELETON.mkdir(parents=True, exist_ok=True)
    for fname, text in rendered.items():
        (SKELETON / fname).write_text(text, encoding="utf-8", newline="\n")
    (SKELETON / "_index.md").write_text(render_index(routes, len(all_unparsed)),
                                        encoding="utf-8", newline="\n")
    (SKELETON / "_unparsed.md").write_text(render_unparsed(all_unparsed),
                                           encoding="utf-8", newline="\n")
    return 0


def _emit(rendered: dict[str, str], routes: list[dict], target: str,
          entries: list[Entry], unparsed: list[Unparsed], relpath: str,
          label: str, group: str) -> None:
    """Render a sublist; if > 400 行, split by func."""
    nv = sum(1 for e in entries if e.kind == "verbatim")
    nt = sum(1 for e in entries if e.kind == "模板")
    text = render_branch(target.replace(".md", ""), label, group, relpath, entries)
    if len(text.splitlines()) <= 400 or not entries:
        rendered[target] = text
        routes.append({"group": group, "label": label, "relpath": relpath,
                       "target": target, "nv": nv, "nt": nt})
        return
    # 按 func 拆分
    by_func: dict[str, list[Entry]] = {}
    for e in entries:
        by_func.setdefault(e.func, []).append(e)
    base = target[:-3]
    for k, (func, grp) in enumerate(sorted(by_func.items(), key=lambda x: -len(x[1]))):
        fslug = _slug(func) or f"g{k}"
        t = f"{base}-{fslug}.md"
        rendered[t] = render_branch(t.replace(".md", ""), f"{label}｜{func}", group,
                                    relpath, grp)
        gnv = sum(1 for e in grp if e.kind == "verbatim")
        gnt = sum(1 for e in grp if e.kind == "模板")
        routes.append({"group": group, "label": f"{label}｜{func}", "relpath": relpath,
                       "target": t, "nv": gnv, "nt": gnt})


if __name__ == "__main__":
    sys.exit(main())
