#!/usr/bin/env python3
"""Build the two-layer skeleton index for the write-introduction corpus.

Single source of truth
----------------------
This script extracts *verbatim* sentence anchors from the corpus and writes
them only under ``corpus/_skeleton/``.  Other files (narrative shape packs,
借句表) must reference these entries by ``id`` and must not copy the text.

Three card forms are parsed
---------------------------
1. 段级卡的 ``**原文锚定**`` / ``**范文锚定**`` 块 -> ``> "..."`` 逐字底本。
2. phrasebank 正文里的英文句子行（Morley 借句）-> 逐字底本。
3. micro-templates 的 ``范文锚定`` 引用句 -> 逐字底本；代码围栏 / 无出处示例行 /
   词表行 -> ``模板``。

Anything that does not match is collected in ``_skeleton/_unparsed.md`` so a
human can triage it.  An optional exclusion ledger at
``scripts/skeleton_exclusions.txt`` (one ``id`` per line, ``#`` comments
allowed) lets a human remove a mis-parsed entry durably: the script re-reads
it on every run, so re-running is stable and idempotent.

Output is deterministic: cards are sorted, ids are derived from filename +
document-order anchor number, no timestamps are emitted.
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
EXCLUSIONS_PATH = SCRIPT_DIR / "skeleton_exclusions.txt"

# ---------------------------------------------------------------- config ----

MODULES: list[dict[str, str]] = [
    {
        "dir": "hooks",
        "file": "hooks.md",
        "kind": "card",
        "desc": "开篇 Hook 的逐字底本（数据冲击 / 悖论 / 范式挑战 / 轶事等）与填槽模板",
        "trigger": "要写 Hook、换 Hook 类型，或 Hook 只有信息没有张力时",
    },
    {
        "dir": "tensions",
        "file": "tensions.md",
        "kind": "card",
        "desc": "问题化 / Gap 张力句底本与填槽模板",
        "trigger": "要把 Gap 写成张力，或 Gap 强度不足、像 few-studies 套话时",
    },
    {
        "dir": "stakes",
        "file": "stakes.md",
        "kind": "card",
        "desc": "研究重要性 / stakes 句底本与填槽模板",
        "trigger": "要论证为什么重要，或 stakes 与 Hook 单调重复时",
    },
    {
        "dir": "literature-turns",
        "file": "literature-turns.md",
        "kind": "card",
        "desc": "文献对话组织句底本（progressive / synthesized / non-coherence）",
        "trigger": "要定位文献关系、写 Literature Turn 时",
    },
    {
        "dir": "theory-lens",
        "file": "theory-lens.md",
        "kind": "card",
        "desc": "理论透镜引入句底本与填槽模板",
        "trigger": "要引入理论透镜，或 theory 声明与机制脱节时",
    },
    {
        "dir": "previews",
        "file": "previews.md",
        "kind": "card",
        "desc": "研究设计 / 发现预览句底本与填槽模板",
        "trigger": "要预告假设、样本、量级、稳健性或边界时",
    },
    {
        "dir": "contributions",
        "file": "contributions.md",
        "kind": "card",
        "desc": "贡献声明句底本与填槽模板",
        "trigger": "要写 Contribution 段，或贡献与 tension 脱节时",
    },
    {
        "dir": "research-questions",
        "file": "research-questions.md",
        "kind": "card",
        "desc": "Research Question 句底本与填槽模板",
        "trigger": "要写 RQ，或 RQ 与 gap 不对应时",
    },
    {
        "dir": "transitions",
        "file": "transitions.md",
        "kind": "card",
        "desc": "模块间过渡（Hook→Literature Turn 等）底本与填槽模板",
        "trigger": "段落之间跳跃、需要模块级过渡时",
    },
    {
        "dir": "differentiation",
        "file": "differentiation.md",
        "kind": "card",
        "desc": "与最近文献划界句底本与填槽模板",
        "trigger": "要写 Differentiation，或与 closest paper 未区分时",
    },
    {
        "dir": "phrasebank",
        "file": "phrasebank.md",
        "kind": "phrasebank",
        "desc": "Morley 措辞库借句（单研究批判 / hedging 强度 / 过程与数值描述）",
        "trigger": "G2 落句后需要换说法或校准声明强度时",
    },
    {
        "dir": "micro-templates",
        "file": "micro-templates.md",
        "kind": "micro",
        "desc": "句级骨架、范文 key line、过渡信号词与 thesis 模型",
        "trigger": "需要句法骨架、句级 transition 或 thesis 定位模型时",
    },
]

ANCHOR_RE = re.compile(r"^(?:#{1,6}\s*)?(?:\*\*)?(原文锚定|范文锚定)(?:\*\*)?")
SKELETON_HEADING_RE = re.compile(r"^#{2,6}\s*(?:Skeleton|骨架)\s*$", re.IGNORECASE)
TEMPLATE_RE = re.compile(r"^\*\*模板\*\*")
SOURCE_RE = re.compile(r"^(?:\*\*)?来源(?:\*\*)?\s*[:：]\s*(.+?)\s*$")
CITEKEY_TOKEN_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]{2,}$")
YEAR_RE = re.compile(r"(?:18|19|20)\d{2}")
ATTR_RE = re.compile(r"—\s*([A-Z][^—]{2,80}?)\s*\(((?:18|19|20)\d{2})\)")
SECTION_RE = re.compile(r"^(#{1,6})\s+(.*)$")
BULLET_RE = re.compile(r"^[-*]\s+(.*)$")
WORDLIST_RE = re.compile(r"^\*\*(常用词|学术写作偏好)\*\*\s*[:：]\s*(.+?)\s*$")

# Stable, block-based anchor: ``标题-{H}`` = document-order ordinal of the
# source heading the quote sits under (anchor markers are never headings).
# This replaces the old accepted-verbatim counter, which drifted whenever a
# non-verbatim block (or an extra segment in a multi-quote block) sat between.
HEADING_ANCHOR_RE = re.compile(r"^标题-(\d+)$")
CITEKEY_OVERRIDES_PATH = SCRIPT_DIR / "citekey_overrides.yaml"

# --------------------------------------------------------------- records ----


@dataclass
class Entry:
    id: str
    citekey: str
    text: str
    path: str
    anchor: str
    status: str  # "verbatim" | "模板"
    note: str = ""
    card: str = ""
    seq: int = 0
    citekey_conflict: bool = False
    from_anchor_block: bool = False  # quote extracted from 原文锚定 / 范文锚定


@dataclass
class Unparsed:
    card: str
    path: str
    where: str
    text: str
    reason: str


@dataclass
class CardResult:
    entries: list[Entry] = field(default_factory=list)
    unparsed: list[Unparsed] = field(default_factory=list)
    parsed: bool = False


# ----------------------------------------------------------- citekey util ---


FRONTMATTER_ENTRY_RE = re.compile(r"^\s*-\s+([A-Za-z][A-Za-z0-9_]+)\s*[:(]")


def build_known_citekeys() -> set[str]:
    known: set[str] = set()
    for path in sorted(CORPUS.rglob("*.md")):
        if "_skeleton" in path.parts or "packs" in path.parts:
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except OSError:
            continue
        fm_end = split_frontmatter(lines)
        for i, line in enumerate(lines):
            in_frontmatter = i < fm_end
            m = SOURCE_RE.match(line.strip())
            if m:
                token = m.group(1).split()[0].strip(",;()")
                if token_is_citekey(token) and YEAR_RE.search(token):
                    known.add(token)
            if in_frontmatter:
                fm = FRONTMATTER_ENTRY_RE.match(line)
                if fm:
                    known.add(fm.group(1))
                for tok in re.findall(r"[A-Za-z][A-Za-z0-9_]*\d{4}[A-Za-z0-9_]*", line):
                    known.add(tok)
    # v4 catalog ids add another authoritative spelling set.
    catalog = SKILL_ROOT.parent / "story-blueprints" / "v4" / "catalog.json"
    if catalog.exists():
        import json

        try:
            data = json.loads(catalog.read_text(encoding="utf-8"))
            for card in data.get("cards", []):
                cid = card.get("id", "")
                if cid:
                    known.add(cid)
                    known.add(cid.split("-")[0])
        except (ValueError, OSError):
            pass
    return known


def token_is_citekey(token: str) -> bool:
    if not CITEKEY_TOKEN_RE.match(token):
        return False
    if token.lower() in {"adapted", "from", "see", "based"}:
        return False
    return True


# -------------------------------------------------------------- parsing -----


def split_frontmatter(lines: list[str]) -> int:
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return i + 1
    return 0


QUOTE_SEP_RE = re.compile(r'["”]\s*/\s*["“]')
QUOTE_PAIR_RE = re.compile(r'["“]([^"“”]+)["”]')
CJK_RE = re.compile(r"[\u4e00-\u9fff]")


def _is_english_sentence(text: str) -> bool:
    if CJK_RE.search(text) or "→" in text:
        return False
    letters = sum(1 for ch in text if ch.isascii() and ch.isalpha())
    return letters >= 40


ANNOTATION_RE = re.compile(r"[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]")


def _trim_annotation(text: str) -> str:
    """Cut a trailing Chinese/fullwidth annotation glued to the quote (e.g. （原文出处见…）)."""
    m = ANNOTATION_RE.search(text)
    if m:
        text = text[: m.start()]
    return text.strip().strip('"“”\'「」').strip()


def extract_verbatim(body: str) -> list[str]:
    """Return one or more verbatim segments from an anchor line, or [] ."""
    text = body.strip()
    if not text:
        return []
    parts = QUOTE_SEP_RE.split(text) if QUOTE_SEP_RE.search(text) else [text]
    segments: list[str] = []
    for part in parts:
        p = part.strip()
        if not p:
            continue
        p = p.lstrip("-* ").strip()
        inner: str | None = None
        if p.startswith(("'", '"', "“", "「")):
            inner = p.strip('"“”\'「」').strip()
        else:
            m = QUOTE_PAIR_RE.search(p)
            if m and len(m.group(1).strip()) >= 15:
                inner = m.group(1).strip()
            elif _is_english_sentence(p):
                inner = p
        if inner is None:
            continue
        inner = _trim_annotation(inner)
        if len(inner) >= 15:
            segments.append(inner)
    return segments


def card_stem(path: Path) -> str:
    stem = path.stem
    if stem == "_index":
        return f"{path.parent.name}-index"
    return stem


def normalize(text: str) -> str:
    return " ".join(text.replace("\t", " ").split())


class CardParser:
    def __init__(self, known: set[str]) -> None:
        self.known = known

    # -- citekeys ---------------------------------------------------------
    def _source_at(self, lines: list[str], idx: int) -> str | None:
        """Citekey from the nearest 来源 line on either side of ``idx``.

        Distance-based (not direction-preferring) because inline anchors put the
        原文锚定 on one line and 来源 on the next line, while block anchors keep
        来源 before the block.
        """
        best: tuple[int, str] | None = None
        for direction in (-1, 1):
            i = idx + direction
            dist = 1
            while 0 <= i < len(lines):
                m = SOURCE_RE.match(lines[i].strip())
                if m:
                    raw = m.group(1)
                    token = raw.split()[0].strip(",;()")
                    citekey: str | None = None
                    if token_is_citekey(token) and YEAR_RE.search(token):
                        citekey = token
                    else:
                        for cand in re.findall(r"[A-Za-z][A-Za-z0-9_]{3,}", raw):
                            if cand in self.known:
                                citekey = cand
                                break
                    if citekey is None:
                        author = re.match(r"([A-Za-z][A-Za-z\-]+)", raw)
                        year = YEAR_RE.search(raw)
                        citekey = f"{author.group(1).lower()}{year.group(0)}" if author and year else "未标注"
                    if best is None or dist < best[0]:
                        best = (dist, citekey)
                    break
                i += direction
                dist += 1
        return best[1] if best else None

    def _citekey_from_text(self, text: str) -> str | None:
        for token in re.findall(r"[A-Za-z][A-Za-z0-9_]{3,}", text):
            if token in self.known:
                return token
        return None

    def resolve_citekey(self, lines: list[str], idx: int, text: str) -> str:
        token = self._source_at(lines, idx)
        if token is not None:
            return token
        token = self._citekey_from_text(text)
        return token or "未标注"

    # -- blocks -----------------------------------------------------------
    def parse(self, path: Path, module: str, kind: str) -> CardResult:
        try:
            raw_lines = path.read_text(encoding="utf-8").splitlines()
        except OSError as exc:  # pragma: no cover - defensive
            result = CardResult()
            result.unparsed.append(
                Unparsed(card=path.stem, path=self.rel(path), where="-", text="", reason=f"读取失败: {exc}")
            )
            return result
        lines = [ln.rstrip("\r") for ln in raw_lines]
        if kind == "card":
            return self._parse_card(path, module, lines)
        if kind == "phrasebank":
            return self._parse_phrasebank(path, module, lines)
        if kind == "micro":
            return self._parse_micro(path, module, lines)
        raise ValueError(f"unknown kind {kind}")

    @staticmethod
    def rel(path: Path) -> str:
        return path.relative_to(SKILL_ROOT).as_posix()

    def _parse_card(self, path: Path, module: str, lines: list[str]) -> CardResult:
        result = CardResult()
        stem = card_stem(path)
        verbatim_seq = 0
        template_seq = 0
        heading_ordinal = 0
        i = split_frontmatter(lines)
        while i < len(lines):
            stripped = lines[i].strip()
            if SECTION_RE.match(stripped) and not ANCHOR_RE.match(stripped):
                heading_ordinal += 1
            anchor_match = ANCHOR_RE.match(stripped)
            if anchor_match:
                header = stripped
                # 原文锚定 glued directly under a **模板** header is a copied
                # slot template, not a verbatim quote: slot text must never be
                # labelled verbatim (the P1 status rule).
                after_template = i > 0 and TEMPLATE_RE.match(lines[i - 1].strip()) is not None
                j = i + 1
                found_quote = False
                while j < len(lines) and lines[j].strip().startswith(">"):
                    body = lines[j].strip()[1:].strip()
                    if body:
                        segments = extract_verbatim(body)
                        if CJK_RE.search(body):
                            # Chinese-annotated line: only a long English quote counts as verbatim.
                            segments = [
                                s
                                for s in segments
                                if sum(1 for ch in s if ch.isascii() and ch.isalpha()) >= 60
                            ]
                        if segments:
                            for seg in segments:
                                verbatim_seq += 1
                                if after_template:
                                    status, note = "模板", "原文锚定紧邻模板，实为槽位模板"
                                else:
                                    status, note = "verbatim", ""
                                result.entries.append(
                                    Entry(
                                        id=f"{stem}#{verbatim_seq}",
                                        citekey=self.resolve_citekey(lines, j, seg),
                                        text=normalize(seg),
                                        path=self.rel(path),
                                        anchor=f"标题-{heading_ordinal}",
                                        status=status,
                                        note=note,
                                        card=path.stem,
                                        seq=verbatim_seq,
                                        from_anchor_block=True,
                                    )
                                )
                            found_quote = True
                        else:
                            result.unparsed.append(
                                Unparsed(
                                    card=path.stem,
                                    path=self.rel(path),
                                    where=f"{header} (行 {j + 1})",
                                    text=normalize(body),
                                    reason="非逐字（转述 / 笔记 / 词表），已从 verbatim 剔除",
                                )
                            )
                    j += 1
                # Inline anchor form: ``**原文锚定**: "..."`` on the header line itself.
                remainder = stripped[anchor_match.end():].strip().lstrip("*:：").strip()
                if remainder and len(remainder) >= 25:
                    inline = extract_verbatim(remainder)
                    if CJK_RE.search(remainder):
                        inline = [
                            s for s in inline if sum(1 for ch in s if ch.isascii() and ch.isalpha()) >= 60
                        ]
                    if inline:
                        for seg in inline:
                            verbatim_seq += 1
                            if after_template:
                                status, note = "模板", "原文锚定紧邻模板，实为槽位模板"
                            else:
                                status, note = "verbatim", ""
                            result.entries.append(
                                Entry(
                                    id=f"{stem}#{verbatim_seq}",
                                    citekey=self.resolve_citekey(lines, i, seg),
                                    text=normalize(seg),
                                    path=self.rel(path),
                                    anchor=f"标题-{heading_ordinal}",
                                    status=status,
                                    note=note,
                                    card=path.stem,
                                    seq=verbatim_seq,
                                    from_anchor_block=True,
                                )
                            )
                        found_quote = True
                result.parsed = result.parsed or found_quote or j > i + 1
                i = j
                continue
            if SKELETON_HEADING_RE.match(stripped):
                j = i + 1
                chunk: list[str] = []
                while j < len(lines) and not SECTION_RE.match(lines[j].strip()):
                    if lines[j].strip():
                        chunk.append(lines[j].strip())
                    j += 1
                if chunk:
                    template_seq += 1
                    result.entries.append(
                        Entry(
                            id=f"{stem}#T{template_seq}",
                            citekey=self.resolve_citekey(lines, i, " ".join(chunk)),
                            text=normalize(" ".join(chunk)),
                            path=self.rel(path),
                            anchor=f"标题-{heading_ordinal}",
                            status="模板",
                            note="段首骨架",
                            card=path.stem,
                            seq=template_seq,
                        )
                    )
                    result.parsed = True
                i = j
                continue
            if TEMPLATE_RE.match(stripped):
                j = i + 1
                chunk: list[str] = []
                while j < len(lines) and lines[j].strip().startswith(">"):
                    body = lines[j].strip()[1:].strip()
                    if body:
                        chunk.append(body)
                    j += 1
                if chunk:
                    template_seq += 1
                    result.entries.append(
                        Entry(
                            id=f"{stem}#T{template_seq}",
                            citekey=self.resolve_citekey(lines, i, " ".join(chunk)),
                            text=normalize(" ".join(chunk)),
                            path=self.rel(path),
                            anchor=f"标题-{heading_ordinal}",
                            status="模板",
                            note="填槽模板",
                            card=path.stem,
                            seq=template_seq,
                        )
                    )
                    result.parsed = True
                i = j
                continue
            i += 1
        if not result.parsed and path.stem != "_index":
            result.unparsed.append(
                Unparsed(
                    card=path.stem,
                    path=self.rel(path),
                    where="整卡",
                    text="",
                    reason="未命中「原文锚定」或「模板」形态",
                )
            )
        return result

    def _parse_phrasebank(self, path: Path, module: str, lines: list[str]) -> CardResult:
        result = CardResult()
        stem = card_stem(path)
        seq = 0
        in_bad = False
        bad_level = 0
        for i, line in enumerate(lines):
            stripped = line.strip()
            m = SECTION_RE.match(stripped)
            if m:
                level = len(m.group(1))
                if "反模式" in m.group(2) or "禁忌" in m.group(2):
                    in_bad, bad_level = True, level
                elif in_bad and level <= bad_level:
                    in_bad = False
                continue
            if in_bad:
                continue
            candidates: list[str] = []
            bm = BULLET_RE.match(stripped)
            if bm:
                candidates.append(bm.group(1).strip())
            elif stripped.startswith("|"):
                cells = [c.strip() for c in stripped.strip("|").split("|")]
                for cell in cells:
                    for seg in QUOTE_PAIR_RE.findall(cell):
                        candidates.append(seg.strip())
                if not candidates and len(cells) > 1:
                    second = cells[1].strip()
                    if _is_english_sentence(second):
                        candidates.append(second)
            for body in candidates:
                if len(body) < 20 or CJK_RE.search(body):
                    continue
                letters = sum(1 for ch in body if ch.isascii() and ch.isalpha())
                if letters < 15:
                    continue
                seq += 1
                has_slot = "[" in body
                result.entries.append(
                    Entry(
                        id=f"{stem}#{seq}",
                        citekey=self._citekey_from_text(body) or "morley2021",
                        text=normalize(body),
                        path=self.rel(path),
                        anchor=f"句子行-{seq}",
                        # P1 统一规则：含槽位 → 模板；无槽位且逐字 → verbatim。
                        status="模板" if has_slot else "verbatim",
                        note="借句（含槽位，模板）" if has_slot else "借句",
                        card=path.stem,
                        seq=seq,
                    )
                )
                result.parsed = True
        if not result.parsed and path.stem != "_index":
            result.unparsed.append(
                Unparsed(
                    card=path.stem,
                    path=self.rel(path),
                    where="整卡",
                    text="",
                    reason="未命中英文句子行形态",
                )
            )
        return result

    def _parse_micro(self, path: Path, module: str, lines: list[str]) -> CardResult:
        result = CardResult()
        stem = card_stem(path)
        vseq = 0
        tseq = 0
        in_bad = False
        bad_level = 0
        heading_ordinal = 0
        i = 0
        while i < len(lines):
            stripped = lines[i].strip()
            m = SECTION_RE.match(stripped)
            if m:
                heading_ordinal += 1
                level = len(m.group(1))
                if "反模式" in m.group(2) or "禁忌" in m.group(2):
                    in_bad, bad_level = True, level
                elif in_bad and level <= bad_level:
                    in_bad = False
                i += 1
                continue
            if not in_bad:
                # code fence -> template skeleton
                if stripped.startswith("```"):
                    block: list[str] = []
                    j = i + 1
                    while j < len(lines) and not lines[j].strip().startswith("```"):
                        if lines[j].strip():
                            block.append(lines[j].strip())
                        j += 1
                    if block:
                        tseq += 1
                        text = normalize(" ".join(block))
                        result.entries.append(
                            Entry(
                                id=f"{stem}#T{tseq}",
                                citekey=self.resolve_citekey(lines, i, text),
                                text=text,
                                path=self.rel(path),
                                anchor=f"标题-{heading_ordinal}",
                                status="模板",
                                note="句法骨架",
                                card=path.stem,
                                seq=tseq,
                            )
                        )
                        result.parsed = True
                    i = j + 1
                    continue
                wl = WORDLIST_RE.match(stripped)
                if wl:
                    tseq += 1
                    text = normalize(f"{wl.group(1)}: {wl.group(2)}")
                    result.entries.append(
                        Entry(
                            id=f"{stem}#T{tseq}",
                            citekey="未标注",
                            text=text,
                            path=self.rel(path),
                            anchor=f"标题-{heading_ordinal}",
                            status="模板",
                            note="词表",
                            card=path.stem,
                            seq=tseq,
                        )
                    )
                    result.parsed = True
                    i += 1
                    continue
                if stripped.startswith(">"):
                    body = stripped[1:].strip()
                    attrs = ATTR_RE.findall(body)
                    cleaned = ATTR_RE.sub("", body).strip()
                    parts = QUOTE_SEP_RE.split(cleaned) if QUOTE_SEP_RE.search(cleaned) else [cleaned]
                    segments: list[str] = []
                    for part in parts:
                        p = _trim_annotation(part.strip().strip('"“”「」'))
                        if len(p) >= 15 and sum(1 for ch in p if ch.isascii() and ch.isalpha()) >= 20:
                            segments.append(p)
                    if segments:
                        if attrs:
                            for idx, seg in enumerate(segments):
                                vseq += 1
                                authors, year = attrs[min(idx, len(attrs) - 1)]
                                citekey = self._citekey_from_text(seg) or self._normalize_attr(authors, year)
                                result.entries.append(
                                    Entry(
                                        id=f"{stem}#{vseq}",
                                        citekey=citekey,
                                        text=normalize(seg),
                                        path=self.rel(path),
                                        anchor=f"标题-{heading_ordinal}",
                                        status="verbatim",
                                        note="范文借句",
                                        card=path.stem,
                                        seq=vseq,
                                        from_anchor_block=True,
                                    )
                                )
                        else:
                            for seg in segments:
                                tseq += 1
                                result.entries.append(
                                    Entry(
                                        id=f"{stem}#T{tseq}",
                                        citekey="未标注",
                                        text=normalize(seg),
                                        path=self.rel(path),
                                        anchor=f"标题-{heading_ordinal}",
                                        status="模板",
                                        note="示例行（无出处）",
                                        card=path.stem,
                                        seq=tseq,
                                    )
                                )
                        result.parsed = True
                        i += 1
                        continue
            i += 1
        if not result.parsed:
            result.unparsed.append(
                Unparsed(
                    card=path.stem,
                    path=self.rel(path),
                    where="整卡",
                    text="",
                    reason="未命中范文锚定 / 代码骨架 / 词表 / 示例行形态",
                )
            )
        return result

    @staticmethod
    def _normalize_attr(authors: str, year: str) -> str:
        key = re.sub(r"[^A-Za-z]", "", authors).lower()
        return f"{key}{year}"


# ------------------------------------------------------------- rendering ----


def escape_cell(text: str) -> str:
    return text.replace("|", r"\|")


def render_module_index(module: dict[str, str], entries: list[Entry]) -> str:
    verbatim = [e for e in entries if e.status == "verbatim"]
    templates = [e for e in entries if e.status == "模板"]
    out: list[str] = []
    out.append(f"# {module['file'][:-3]} — 骨架子索引")
    out.append("")
    out.append("> 由 `scripts/build_indices.py` 生成，可重复运行、幂等。请勿手改本文件。")
    out.append("> **底本单源**：verbatim 原句只存本索引；形状包与借句表只引 `id`，不复写正文。")
    out.append("> `状态=verbatim` 为逐字底本（无槽位、与源文件逐字一致，不得改写/拼接/补全）；`状态=模板` 为含 `[槽位]` 的填槽骨架，不可当逐字底本引用。")
    out.append("> 锚点格式 `标题-{序数}`：指向源文件中该引文所在标题块的文档序数（非已接受 verbatim 计数），块内增删其它 verbatim 不影响定位。")
    out.append("> `路径#锚点` 可用于回源核对；`--verify` 会断言每条底本可在其锚点块内逐字定位。人工剔除记录见 `scripts/skeleton_exclusions.txt`，待补录项见 `_unparsed.md`。")
    out.append("")
    out.append(f"条目：verbatim {len(verbatim)} 条 / 模板 {len(templates)} 条。")
    out.append("")
    if verbatim:
        out.append("## Verbatim 底本")
        out.append("")
        out.append("| id | citekey | verbatim 原句 | 卡片路径#锚点 | 状态 |")
        out.append("|---|---|---|---|---|")
        for e in verbatim:
            note = f" verbatim（{e.note}）" if e.note else " verbatim"
            if e.citekey_conflict:
                note += " citekey_conflict"
            out.append(
                f"| `{e.id}` | {escape_cell(e.citekey)} | {escape_cell(e.text)} | "
                f"`{e.path}#{e.anchor}` |{note} |"
            )
        out.append("")
    if templates:
        out.append("## 填槽模板（模板）")
        out.append("")
        out.append("| id | citekey | 模板 | 卡片路径#锚点 | 状态 |")
        out.append("|---|---|---|---|---|")
        for e in templates:
            note = e.note or "模板"
            if e.citekey_conflict:
                note += " citekey_conflict"
            out.append(
                f"| `{e.id}` | {escape_cell(e.citekey)} | {escape_cell(e.text)} | "
                f"`{e.path}#{e.anchor}` | 模板（{note}） |"
            )
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def render_route(
    module_stats: list[tuple[dict[str, str], int, int, int]],
    unparsed_count: int,
    excluded_count: int,
    unlabeled_by_module: list[tuple[str, int]],
) -> str:
    out: list[str] = []
    out.append("# Skeleton Index — 骨架索引路由")
    out.append("")
    out.append("> **两层结构**：本路由 + 每模块一份子索引。先读本文件的「何时读它」定位模块，再整份读入对应子索引。")
    out.append("> 由 `scripts/build_indices.py` 生成；底本来源为 corpus 段级卡「原文锚定」块、phrasebank 借句行、micro-templates 范文锚定行。")
    out.append("> **单源纪律**：verbatim 底本只存在子索引里；形状包（`../packs/`）与借句表只引 `id`。")
    out.append("> 状态列：`verbatim` = 逐字底本（无槽位、与源文件逐字一致）；`模板` = 含 `[槽位]` 的填槽骨架（不可当逐字底本）。")
    out.append("")
    out.append("| 子索引 | verbatim | 模板 | 行数 | 一行说明 | 何时读它 |")
    out.append("|---|---|---|---|---|---|")
    total_v = total_t = total_l = 0
    for module, nv, nt, nlines in module_stats:
        total_v += nv
        total_t += nt
        total_l += nlines
        out.append(
            f"| [`{module['file']}`]({module['file']}) | {nv} | {nt} | {nlines} | "
            f"{module['desc']} | {module['trigger']} |"
        )
    out.append("")
    out.append(f"合计：verbatim {total_v} 条 / 模板 {total_t} 条 / {total_l} 行。")
    out.append("")
    unlabeled_total = sum(n for _, n in unlabeled_by_module)
    breakdown = "、".join(f"{name[:-3]} {n}" for name, n in unlabeled_by_module if n)
    out.append("## 核对记录")
    out.append("")
    out.append(
        f"- `未标注` citekey 实测 **{unlabeled_total} 条**（{breakdown}）；"
        "生成物逐行实测值，非估算。"
    )
    out.append("")
    out.append("## 待补录")
    out.append("")
    out.append(
        f"- [`_unparsed.md`](_unparsed.md)：{unparsed_count} 条未自动命中或疑似误抽 "
        f"+ {excluded_count} 条人工剔除（合计 {unparsed_count + excluded_count} 条），"
        "**待补录 / 待人工判定**。任何模块的子索引条目在被人工核对前都视为草稿。"
    )
    out.append("- 人工剔除记录：`scripts/skeleton_exclusions.txt`（重跑脚本时保留剔除，保证幂等）。")
    out.append("")
    return "\n".join(out)


def render_unparsed(items: list[Unparsed], excluded: dict[str, str], applied: set[str]) -> str:
    out: list[str] = []
    out.append("# Skeleton Index — 待补录 / 未命中")
    out.append("")
    out.append("> 脚本未能自动判定为 verbatim 或模板的条目集中在此，**待人工补录**。")
    out.append("> 已剔除项由 `scripts/skeleton_exclusions.txt` 持久化；重跑脚本不会把它们放回子索引。")
    out.append("")
    if excluded:
        out.append("## 人工剔除（已写入 exclusion ledger）")
        out.append("")
        for eid, reason in sorted(excluded.items()):
            mark = "已生效" if eid in applied else "该 id 本次未自动生成（已由解析规则避开）"
            out.append(f"- `{eid}` — {reason}（{mark}）")
        out.append("")
    out.append("## 未命中 / 非逐字")
    out.append("")
    if not items:
        out.append("（无）")
    else:
        out.append("| 卡片 | 卡片路径 | 位置 | 原文摘录 | 原因 |")
        out.append("|---|---|---|---|---|")
        for u in items:
            snippet = escape_cell(u.text[:200] + ("…" if len(u.text) > 200 else ""))
            out.append(f"| {u.card} | `{u.path}` | {u.where} | {snippet} | {u.reason} |")
    out.append("")
    return "\n".join(out)


# ------------------------------------------------------------------ main ----


def load_exclusions() -> dict[str, str]:
    if not EXCLUSIONS_PATH.exists():
        return {}
    out: dict[str, str] = {}
    for line in EXCLUSIONS_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(None, 1)
        ident = parts[0].lstrip("-*").strip()
        reason = parts[1].lstrip("#").strip() if len(parts) > 1 else ""
        if ident:
            out[ident] = reason or "人工剔除"
    return out


def load_citekey_overrides() -> dict[str, dict[str, str]]:
    """Read ``scripts/citekey_overrides.yaml`` (id -> override record).

    Each record carries ``index_value`` (what the parser generated from the
    card's ``**来源**`` line) and ``override_value`` (the human-reviewed truth).
    A missing file is not an error: the override table is optional.
    """
    if not CITEKEY_OVERRIDES_PATH.exists():
        return {}
    try:
        import yaml

        data = yaml.safe_load(CITEKEY_OVERRIDES_PATH.read_text(encoding="utf-8")) or {}
    except Exception as exc:  # noqa: BLE001 - surface, never crash generation
        print(f"WARN: citekey_overrides.yaml 读取失败: {exc}", file=sys.stderr)
        return {}
    out: dict[str, dict[str, str]] = {}
    for item in data.get("overrides", []) or []:
        ident = str(item.get("id", "")).strip()
        if not ident:
            continue
        out[ident] = {k: str(item.get(k, "")) for k in ("index_value", "override_value", "evidence", "reviewed")}
    return out


def apply_citekey_overrides(entries: list[Entry], overrides: dict[str, dict[str, str]]) -> None:
    """Apply the override table in place; mark unresolved conflicts explicitly."""
    for e in entries:
        ov = overrides.get(e.id)
        if not ov:
            continue
        index_value = ov.get("index_value", "")
        override_value = ov.get("override_value", "")
        if override_value and e.citekey == index_value:
            e.citekey = override_value
            e.note = (e.note + f" | citekey 覆盖 {index_value}→{override_value}").strip(" |")
        elif override_value:
            # Override table disagrees with the freshly generated index value:
            # keep both and flag it, never silently pick one.
            e.citekey = f"{e.citekey} / {override_value}"
            e.citekey_conflict = True


def heading_regions(path: Path) -> dict[int, str]:
    """Map heading ordinal -> normalized body of that heading's section.

    Mirrors the parser's ordinal: anchor markers written heading-style
    (``### 原文锚定``) do NOT count as headings, and frontmatter is skipped.
    Ordinal ``0`` is the pre-first-heading region.
    """
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return {}
    regions: dict[int, list[str]] = {0: []}
    ordinal = 0
    for line in lines[split_frontmatter(lines):]:
        stripped = line.strip()
        if SECTION_RE.match(stripped) and not ANCHOR_RE.match(stripped):
            ordinal += 1
            regions.setdefault(ordinal, [])
            continue
        regions.setdefault(ordinal, []).append(line)
    return {k: normalize("\n".join(v)) for k, v in regions.items()}


def verify_anchors(entries: list[Entry]) -> list[str]:
    """Return one string per block-anchored entry that misses its source block."""
    failures: list[str] = []
    cache: dict[str, dict[int, str]] = {}
    for e in entries:
        m = HEADING_ANCHOR_RE.match(e.anchor)
        if not m:
            continue
        regions = cache.get(e.path)
        if regions is None:
            regions = heading_regions(SKILL_ROOT / e.path)
            cache[e.path] = regions
        if e.text not in regions.get(int(m.group(1)), ""):
            failures.append(f"{e.id} ({e.path}#{e.anchor}): {e.text[:90]}")
    return failures


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="build in memory and report, do not write")
    parser.add_argument("--verify", action="store_true", help="verify every verbatim entry is byte-for-byte present in its source and its anchor resolves to that block")
    parser.add_argument("--verify-anchors", action="store_true", help="verify each block anchor resolves to a source block containing its text")
    parser.add_argument("--quiet", action="store_true", help="only print the summary")
    args = parser.parse_args(argv)

    known = build_known_citekeys()
    exclusions = load_exclusions()
    cp = CardParser(known)

    all_entries: list[Entry] = []
    all_unparsed: list[Unparsed] = []
    excluded_applied: set[str] = set()
    module_entries: dict[str, list[Entry]] = {}

    for module in MODULES:
        dir_path = CORPUS / module["dir"]
        paths = sorted(dir_path.glob("*.md"))
        entries: list[Entry] = []
        for path in paths:
            result = cp.parse(path, module["dir"], module["kind"])
            for e in result.entries:
                if e.id in exclusions:
                    excluded_applied.add(e.id)
                    continue
                entries.append(e)
            all_unparsed.extend(result.unparsed)
        module_entries[module["file"]] = entries
        all_entries.extend(entries)

    overrides = load_citekey_overrides()
    apply_citekey_overrides(all_entries, overrides)

    stats: list[tuple[dict[str, str], int, int, int]] = []
    rendered: dict[str, str] = {}
    for module in MODULES:
        entries = module_entries[module["file"]]
        text = render_module_index(module, entries)
        rendered[module["file"]] = text
        nv = sum(1 for e in entries if e.status == "verbatim")
        nt = sum(1 for e in entries if e.status == "模板")
        stats.append((module, nv, nt, len(text.splitlines())))

    nv_total = sum(1 for e in all_entries if e.status == "verbatim")
    nt_total = sum(1 for e in all_entries if e.status == "模板")
    unlabeled_by_module = [
        (m["file"], sum(1 for e in module_entries[m["file"]] if e.citekey == "未标注")) for m in MODULES
    ]
    unparsed_text = render_unparsed(all_unparsed, exclusions, excluded_applied)
    route = render_route(stats, len(all_unparsed), len(excluded_applied), unlabeled_by_module)

    if args.verify:
        cache: dict[str, str] = {}
        mismatches: list[Entry] = []
        for e in all_entries:
            if e.status != "verbatim":
                continue
            src = cache.get(e.path)
            if src is None:
                src = normalize((SKILL_ROOT / e.path).read_text(encoding="utf-8"))
                cache[e.path] = src
            if e.text not in src:
                mismatches.append(e)
        print(f"verbatim 回源校验: {nv_total - len(mismatches)}/{nv_total} 命中源文件")
        for e in mismatches:
            print(f"  MISMATCH {e.id} ({e.path}): {e.text[:100]}")

    if args.verify or args.verify_anchors:
        anchor_entries = [
            e for e in all_entries if HEADING_ANCHOR_RE.match(e.anchor) and e.from_anchor_block
        ]
        anchor_failures = verify_anchors(anchor_entries)
        n_verbatim = sum(1 for e in anchor_entries if e.status == "verbatim")
        print(
            f"锚点局部性校验（原文锚定/范文锚定块）: "
            f"{len(anchor_entries) - len(anchor_failures)}/{len(anchor_entries)} 命中其 #标题-N 所在源块"
            f"（其中 verbatim {n_verbatim} 条）"
        )
        for f in anchor_failures:
            print(f"  ANCHOR-MISS {f}")

    if not args.quiet:
        print("module                     verbatim  templates  lines")
        for module, nv, nt, nl in stats:
            print(f"{module['file']:<26} {nv:>8} {nt:>10} {nl:>6}")
        print(f"{'TOTAL':<26} {nv_total:>8} {nt_total:>10}")
        print(f"unparsed items: {len(all_unparsed)} (+{len(excluded_applied)} manually excluded)")

    if args.check:
        return 0

    SKELETON.mkdir(parents=True, exist_ok=True)
    for filename, text in rendered.items():
        (SKELETON / filename).write_text(text, encoding="utf-8", newline="\n")
    (SKELETON / "_index.md").write_text(route, encoding="utf-8", newline="\n")
    (SKELETON / "_unparsed.md").write_text(unparsed_text, encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
