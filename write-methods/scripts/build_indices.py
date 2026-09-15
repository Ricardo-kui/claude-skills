#!/usr/bin/env python3
"""Build the two-level skeleton index for the write-methods corpus.

Single source of truth
----------------------
Extracts *verbatim* original-sentence anchors and *fill-in templates* from the
corpus ``.md`` files and writes them ONLY under ``corpus/_skeleton/``.  Every
other consumer must reference these entries by ``id`` and must not copy text.

Methods-specific extraction rules
---------------------------------
verbatim  = 卡片里带引号/缩进的完整英文原句（有明确来源论文），逐字保留：
            * 主来源 ``**原始句锚点**: ...`` / ``[原始句锚点]: ...`` /
              ``- **原始句锚点**（…）: "..."`` 三种形态（逐字，含 ``…`` 不回填）
            * 次生来源 ``**原文锚定**/原文锚点`` 或 ``- **原文锚定**："..."``
              （id 后缀 .a/.b）
模板     = ``**骨架**`` / ``**模板**`` / ``**模板/骨架**`` / ``**结构**`` /
           ``[骨架]`` 后的 ``>`` 引用块、``` 代码围栏、或紧随的裸英文段
           （含 ``[槽位]`` 占位符的句式骨架）。
锚点     = ``corpus/<文件名>#变体-<变体号>``；``--verify`` 断言该标题存在。
citekey  = 优先取 ``<!-- wb:<citekey>:... -->`` 标记（机器可读），
           无则回退 ``**来源论文**`` / ``**来源**`` / 裸 ``来源：`` /
           ``- **出处**`` 原文；两者皆无标 ``未标注``（不编造）。
适配槽位 = 取 ``**槽位**`` / ``[适用槽位]`` 字段内 M1–M10（含 M2.5）与
           Q1–Q8（定性）token（去重排序）；判断不了或含 ``M?`` 标 ``通用``。

Variant numbering (口径与 Batch 1 一致)
---------------------------------------
* ``### 变体 [0-9A-Z]+`` —— 编号/字母变体，计入 342（与 validator、INDEX 对账）。
* ``### 变体：<标题>``（无编号，fang2025 POM）—— 不编号变体，**不计入 342**，
  在骨架索引中以合成 id ``U<n>`` 收录，citekey 无内联字段则标 ``未标注``
  （来源见 corpus 速查表）。
* ``#### 变体：<标题>``（EXTEND / gap HIGH 子变体）—— **不计入 342**，
  以合成 id ``<父编号>x<n>`` 收录，citekey 优先取 ``- **原文锚定**`` 尾部
  ``（citekey, …）`` 标注。

Output
------
- ``corpus/_skeleton/_index.md``   level-1 route by design type (<= 120 lines)
- ``corpus/_skeleton/<slug>.md``   level-2 list per design type; split by slot
                                   when the rendered file would exceed MAX_LINES.
- ``corpus/_skeleton/_unparsed.md`` entries that cannot be classified.

CLI
---
--check        build in memory and report, do not write.
--verify       verify verbatim byte-for-byte in source + anchor headings exist.
--sample N     also print N evenly-spaced verbatim entries with their source-hit.
--quiet        only print the summary.

Shared engine (2026-09-15)
--------------------------
工具层 / Entry·Unparsed / materialize / verify 回源与抽样 / 渲染原语 / 写盘 /
CLI 骨架已下沉到 ``_shared/indexing/indexing_engine.py``（唯一一份）；本适配器
只保留 write-methods 特异的：FAMILIES 设计类型表、三种变体标题（含不编号
``U<n>`` 与 EXTEND ``<父>x<n>`` 合成 id）、bracket/bullet-bold 字段形态、
M/Q 槽位机制、二级清单/路由页模板文本、``_heading_for`` 顺序重放式锚点校验。
「342 变体计数」对账仍在外部 ``validate_write_methods.py``（生成器/校验器
职责边界不变）。
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPT_DIR.parent
CORPUS = SKILL_ROOT / "corpus"
SKELETON = CORPUS / "_skeleton"

SHARED = SKILL_ROOT.parent / "_shared" / "indexing"
sys.path.insert(0, str(SHARED))

import indexing_engine as eng  # noqa: E402
from indexing_engine import Entry, Unparsed  # noqa: E402

MAX_LINES = eng.MAX_LINES

# ---------------------------------------------------------------- config ----

# One entry per corpus design-type file.  ``slug`` is the level-2 index
# filename stem and also the family prefix of every entry id.
FAMILIES: list[dict[str, str]] = [
    {"file": "面板数据-OLS.md", "slug": "panel-ols", "name": "面板数据-OLS",
     "desc": "面板/截面线性 OLS-FE 方法段全槽位（设置、样本、DV/IV、控制、规格）",
     "trigger": "主模型是 OLS/FE/动态面板/SUR，需写设置合法性、样本漏斗、操作化与规格叙事"},
    {"file": "自然实验-DiD.md", "slug": "did", "name": "自然实验-DiD",
     "desc": "DiD/准实验识别策略、平行趋势、staggered 卫生、安慰剂与威胁电池",
     "trigger": "因果设计是 DiD/准实验，需识别策略论证、预处理卫生或外生性辩护"},
    {"file": "非线性模型.md", "slug": "nonlinear", "name": "非线性模型",
     "desc": "计数/Logit/Probit/Tobit/交互的估计器选择与诊断",
     "trigger": "DV 是计数/二元/有序/受限，需分布诊断、估计器选择或交互项规格"},
    {"file": "生存分析.md", "slug": "survival", "name": "生存分析",
     "desc": "AFT/Cox/复发事件风险模型的方法叙事（操作化、分布、删失）",
     "trigger": "DV 是时长/生存时间，需 hazard 操作化、分布选择或复发事件处理"},
    {"file": "SEM.md", "slug": "sem", "name": "SEM",
     "desc": "联立方程 SEM、残差中心化、Granger 前置诊断",
     "trigger": "SEM/调节中介方法段（联合估计、交互共线性、时序方向诊断）"},
    {"file": "实验.md", "slug": "experiments", "name": "实验",
     "desc": "实验/多研究的方法段（被试、材料、操纵、测量）",
     "trigger": "数据来自实验，需写被试→材料→操纵→测量标准段"},
    {"file": "多研究.md", "slug": "multi-study", "name": "多研究综合",
     "desc": "多研究项目方法总览、操纵检验、递进设计论证",
     "trigger": "一篇论文含多个 study，需跨研究设计总览或递进论证"},
    {"file": "定性过程研究.md", "slug": "qualitative-process", "name": "定性过程研究",
     "desc": "归纳/质性方法（现象正当化、情境选择、编码进阶、可信性 Q1–Q8）",
     "trigger": "定性 Findings（过程模型/引语），非量化假设检验"},
    {"file": "稀有结果.md", "slug": "rare-outcome", "name": "稀有结果",
     "desc": "稀有二元/低基线率结果的估计器放弃与样本框设计",
     "trigger": "DV 低基线率（欺诈/破产/极端事故），FE 丢样本或 margin 分解"},
    {"file": "实证对象构建.md", "slug": "construct-object", "name": "实证对象构建",
     "desc": "交易/事件/竞争组等分析单位与实证对象的构造",
     "trigger": "分析单位需升级/构造（交易级、事件级、竞争组），需单位宣告与核验"},
    {"file": "事件历史+事件研究.md", "slug": "event-history-study", "name": "事件历史+事件研究",
     "desc": "事件窗口/事件日选择、CAR 测量、事件研究样本构造",
     "trigger": "事件研究/事件历史，需窗口选择、污染规避或 CAR 测量公式"},
    {"file": "同时方程.md", "slug": "simultaneous-equations", "name": "同时方程",
     "desc": "动态同时双方程、堆叠 Wald、辅助方程、DWH/SUR-3SLS",
     "trigger": "两个内生变量互为因果（status/reputation 型），需系统估计叙事"},
    {"file": "IV-2SLS.md", "slug": "iv-2sls", "name": "IV-2SLS",
     "desc": "工具变量选择、排除限制、第一阶段、DWH/控制函数",
     "trigger": "需内生性修正（2SLS/IV），报第一阶段 F、排除限制或弱识别诊断"},
    {"file": "动态面板-GMM.md", "slug": "dynamic-panel-gmm", "name": "动态面板-GMM",
     "desc": "短面板适用性、AB-GMM 诊断对报告链（AR(2)+Hansen）",
     "trigger": "动态面板（滞后 DV），需 AB-GMM/Blundell-Bond 诊断链"},
    {"file": "匹配DiD-广义DiD.md", "slug": "matched-did", "name": "匹配DiD-广义DiD",
     "desc": "CEM 匹配 + 冲击内部结构化对照",
     "trigger": "DiD 前用匹配构造可比处理/对照"},
    {"file": "同伴效应-网络效应.md", "slug": "peer-network", "name": "同伴/网络效应",
     "desc": "网络构念操作化（centrality、联结、风险集）与 dyadic 非独立性",
     "trigger": "同伴/网络效应结果，需网络构念操作化或 dyadic 依赖处理"},
    {"file": "文本构念测量.md", "slug": "text-construct", "name": "文本构念测量",
     "desc": "词典/LIWC/GLLM 等文本构念的操作化与效度链",
     "trigger": "从文本（财报/访谈/媒体）测构念，需词典效度或编码信度"},
    {"file": "PSM匹配面板.md", "slug": "psm-panel", "name": "PSM匹配面板",
     "desc": "PSM/EBM/CEM 匹配作为稳健性的方法叙事",
     "trigger": "用倾向得分/熵平衡匹配构造对照或稳健性"},
    {"file": "堆叠扩散Logit.md", "slug": "stacked-diffusion-logit", "name": "堆叠扩散Logit",
     "desc": "（骨架-only，无累积变体）",
     "trigger": "扩散/采纳 Logit 结构模型（当前无验证变体）"},
    {"file": "多行为者设计.md", "slug": "multi-actor", "name": "多行为者设计",
     "desc": "个体→组级聚合辩护、多行为者拆 dyad 与混淆控制",
     "trigger": "多行为者/多层级设计，需聚合辩护或 dyad 拆分"},
    {"file": "推断二元结果.md", "slug": "binary-outcome-inference", "name": "推断二元结果",
     "desc": "裁量权边界子样本等二元结果推断的样本聚焦",
     "trigger": "二元结果的因果推断（当前少量变体）"},
    {"file": "两阶段模型.md", "slug": "two-stage", "name": "两阶段模型",
     "desc": "Heckman/切换回归/控制函数/选择修正",
     "trigger": "样本选择/可观测性选择，需 Heckman 或控制函数叙事"},
    {"file": "VARX-PVAR.md", "slug": "varx-pvar", "name": "VARX / PVAR",
     "desc": "脉冲响应、方差分解、向量自回归系统的方法规格",
     "trigger": "向量自回归/脉冲响应，需滞后阶/GIRF/FEVD 规格"},
    {"file": "结构需求-state-space.md", "slug": "state-space", "name": "结构需求-state-space",
     "desc": "BLP 结构需求、Kalman/GMM 状态空间拟合",
     "trigger": "结构需求或状态空间模型，需拟合/反事实方法规格"},
]

# ------------------------------------------------------------- regexes -----

VARIANT_HDR_RE = re.compile(r"^###\s+变体\s+([0-9A-Z]+)\s*[:：]?(.*)$")
UNNUM_HDR_RE = re.compile(r"^###\s+变体\s*[:：]\s*(.*)$")
EXTEND_HDR_RE = re.compile(r"^####\s+变体\s*[:：]?\s*(.*)$")

WB_RE = re.compile(r"<!--\s*wb:([^:\s]+)")

FIELD_SRC_RE = re.compile(r"^\*\*来源(?:论文)?\*\*\s*[:：]\s*(.*)$")
PLAIN_SRC_RE = re.compile(r"^来源[:：]\s*(.*)$")
PRIMARY_VERBATIM_RE = re.compile(r"^\*\*原始句锚点\*\*\s*[:：]\s*(.*)$")
SECONDARY_VERBATIM_RE = re.compile(
    r"^\*\*原文锚[定点]\*\*\s*(?:\([^)]*\)|（[^）]*）)?\s*[:：]?\s*(.*)$")
FIELD_SLOT_RE = re.compile(r"^\*\*槽位\*\*\s*[:：]\s*(.*)$")
FIELD_SKELETON_RE = re.compile(
    r"^\*\*(?:骨架(?:/框架)?|模板(?:/骨架)?|结构)\*\*\s*[:：]?\s*(.*)$")

# bracket-form fields（不编号变体 / ball_2018 型）
BRACKET_SRC_RE = re.compile(r"^\[(?:来源论文|来源|出处)\]\s*[:：]?\s*(.*)$")
BRACKET_SLOT_RE = re.compile(r"^\[适用槽位\]\s*[:：]?\s*(.*)$")
BRACKET_VERBATIM_RE = re.compile(r"^\[原始句锚点\]\s*[:：]?\s*(.*)$")
BRACKET_SKELETON_RE = re.compile(r"^\[骨架\]\s*[:：]?\s*(.*)$")

# bullet-bold fields（ball_2018 / anand_mukherjee / EXTEND 子变体）
BULLET_SRC_RE = re.compile(r"^[-*]\s+\*\*(?:来源论文|来源|出处)\*\*\s*[:：]?\s*(.*)$")
BULLET_SLOT_RE = re.compile(r"^[-*]\s+\*\*槽位\*\*\s*[:：]?\s*(.*)$")
BULLET_PRIMARY_VERBATIM_RE = re.compile(
    r"^[-*]\s+\*\*原始句锚点\*\*(?:（[^）]*）|\([^)]*\))?\s*[:：]\s*(.*)$")
BULLET_SECONDARY_VERBATIM_RE = re.compile(
    r"^[-*]\s+\*\*原文锚[定点]\*\*\s*(?:（[^）]*）|\([^)]*\))?\s*[:：]\s*(.*)$")
BULLET_SKELETON_RE = re.compile(
    r"^[-*]\s+\*\*(?:骨架|模板(?:/骨架)?)\*\*\s*[:：]?\s*(.*)$")

M_TOKEN_RE = re.compile(r"\bM(?:2\.5|10|[1-9])\b")
Q_TOKEN_RE = re.compile(r"\bQ([1-8])\b")
SLOT_CELL_RE = re.compile(r"^(M(?:2\.5|10|[1-9])|Q[1-8])$")

KIND_NOTES = {"num": "", "unnum": "不编号变体", "extend": "EXTEND子变体"}


def extract_trailing_citekey(text: str) -> str | None:
    """Trailing annotation ``（post_2022_..., AMJ 2022, ...）`` -> citekey.

    Anchored at end of line so inline citations like ``(Hoobler et al., ...)``
    inside the quote are not mistaken for the source annotation.
    """
    m = re.search(r"[（(]([^，,()（）]+)[,，][^）)]*[）)]\s*$", text)
    return m.group(1).strip() if m else None


# ------------------------------------------------------------- records -----


@dataclass
class Variant:
    vid: str            # token / U<n> / <parent>x<n>
    title: str
    heading: str        # exact heading line (for anchor verification)
    kind: str           # "num" | "unnum" | "extend"
    wb: list[str] = field(default_factory=list)
    src: str | None = None
    slot_raw: str | None = None
    primary_verbatim: str | None = None
    templates: list[str] = field(default_factory=list)
    extra_verbatim: list[str] = field(default_factory=list)
    skeleton_seen: bool = False
    in_skeleton_prose: bool = False


def _slot_sort_key(tok: str) -> tuple:
    if tok == "M2.5":
        return (0, 2.5)
    m = re.match(r"([MQ])(\d+)", tok)
    letter = 0 if m.group(1) == "M" else 1
    return (letter, int(m.group(2)))


def normalize_slot(raw: str | None) -> str:
    if not raw:
        return "通用"
    tokens: list[str] = []
    seen: set[str] = set()
    for m in M_TOKEN_RE.finditer(raw):
        tok = m.group(0)
        if tok not in seen:
            seen.add(tok)
            tokens.append(tok)
    for m in Q_TOKEN_RE.finditer(raw):
        tok = m.group(0)
        if tok not in seen:
            seen.add(tok)
            tokens.append(tok)
    if not tokens:
        return "通用"
    tokens.sort(key=_slot_sort_key)
    return "/".join(tokens)


def slot_key(e: Entry) -> str:
    for tok in re.split(r"/", e.slot):
        if tok != "通用":
            return tok.lower().replace(".", "_")
    return "general"


def _slot_group_label(key: str) -> str:
    m = re.match(r"(m|q)(\d+)(?:_\d+)?", key)
    if m:
        prefix = m.group(1).upper()
        num = m.group(2)
        if key.startswith("m2_5"):
            return "M2.5"
        return f"{prefix}{num}"
    return "通用"


# ------------------------------------------------------------- parsing -----


def _collect_skeleton_prose(lines: list[str], start: int) -> tuple[str, int]:
    """Collect consecutive bare English prose lines (ball_2018 [骨架]: 后续裸段)."""
    chunks: list[str] = []
    j = start
    while j < len(lines):
        ln = lines[j].strip()
        if not ln:
            break
        if ln.startswith(("#", ">", "-", "*", "|", "`", "[", "<!--", "**")):
            break
        chunks.append(ln)
        j += 1
    return " ".join(chunks), j


def _load_quickref_sources(path: Path) -> dict[str, str]:
    """「变体速查表」（表头含 状态/来源 的明细表）→ {变体号: 来源列原文}。

    速查表绑定分支（2026-09-15）：来源列作 citekey 回退源——仅在 wb 标记与
    来源字段皆缺席时使用（不编造纪律的语料内回退）。文件无速查表返回 {}。
    methods 索引的状态列是 verbatim/模板，速查表状态列（ROBUST/VERIFIED/
    EMERGING）在 methods 不落列，故不取。
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


def parse_file(family: dict[str, str]) -> tuple[list[Entry], list[Unparsed], int, int, int]:
    path = CORPUS / family["file"]
    slug = family["slug"]
    entries: list[Entry] = []
    unparsed: list[Unparsed] = []
    relpath = f"corpus/{family['file']}"
    try:
        lines = [ln.rstrip("\r") for ln in path.read_text(encoding="utf-8").splitlines()]
    except OSError as exc:
        unparsed.append(Unparsed(card=path.stem, path=relpath, where="-",
                                 text="", reason=f"读取失败: {exc}"))
        return entries, unparsed, 0, 0, 0

    slot_table = eng.build_slot_table(lines, SLOT_CELL_RE, min_cells=3)
    qsrc = _load_quickref_sources(path)

    variants: list[Variant] = []
    cur: Variant | None = None
    in_comment = False
    unnum_counter = 0
    extend_counter: dict[str, int] = {}
    i = 0

    def start_variant(vid: str, title: str, heading: str, kind: str) -> None:
        nonlocal cur
        if cur is not None:
            variants.append(cur)
        cur = Variant(vid=vid, title=title.strip(), heading=heading.strip(), kind=kind)

    while i < len(lines):
        s = lines[i].strip()
        if in_comment:
            if "-->" in s:
                in_comment = False
            i += 1
            continue
        if s.startswith("<!--"):
            m = WB_RE.search(s)
            if cur is not None and m:
                cur.wb.append(m.group(1))
            if "-->" not in s:
                in_comment = True
            i += 1
            continue

        m = VARIANT_HDR_RE.match(s)
        if m:
            start_variant(m.group(1), m.group(2), s, "num")
            i += 1
            continue
        m = UNNUM_HDR_RE.match(s)
        if m:
            unnum_counter += 1
            start_variant(f"U{unnum_counter}", m.group(1), s, "unnum")
            i += 1
            continue
        m = EXTEND_HDR_RE.match(s)
        if m:
            parent = cur.vid if cur is not None else "?"
            n = extend_counter.get(parent, 0) + 1
            extend_counter[parent] = n
            start_variant(f"{parent}x{n}", m.group(1), s, "extend")
            i += 1
            continue

        if cur is None:
            i += 1
            continue

        # --- bracket-form fields（不编号 / ball_2018）--------------------
        bm = BRACKET_SRC_RE.match(s)
        if bm:
            cur.src = bm.group(1).strip()
            i += 1
            continue
        bm = BRACKET_SLOT_RE.match(s)
        if bm:
            cur.slot_raw = bm.group(1).strip()
            i += 1
            continue
        bm = BRACKET_VERBATIM_RE.match(s)
        if bm:
            seg = eng.trim_annotation(eng.strip_outer_quotes(bm.group(1)))
            if seg and eng.is_english(seg):
                cur.primary_verbatim = seg
            i += 1
            continue
        bm = BRACKET_SKELETON_RE.match(s)
        if bm:
            cur.skeleton_seen = True
            inline = bm.group(1).strip()
            if inline:
                cur.templates.append(eng.normalize(eng.strip_outer_quotes(inline)))
                i += 1
                continue
            text, j = _collect_skeleton_prose(lines, i + 1)
            if text and eng.is_english(text):
                cur.templates.append(eng.normalize(text))
            i = j
            continue

        # --- bullet-bold fields（ball_2018 / EXTEND）--------------------
        bm = BULLET_SRC_RE.match(s)
        if bm:
            cur.src = bm.group(1).strip()
            i += 1
            continue
        bm = BULLET_SLOT_RE.match(s)
        if bm:
            cur.slot_raw = bm.group(1).strip()
            i += 1
            continue
        bm = BULLET_PRIMARY_VERBATIM_RE.match(s)
        if bm:
            seg = eng.trim_annotation(eng.strip_outer_quotes(bm.group(1)))
            if seg and eng.is_english(seg):
                cur.primary_verbatim = seg
            i += 1
            continue
        bm = BULLET_SECONDARY_VERBATIM_RE.match(s)
        if bm:
            raw = bm.group(1).strip()
            if cur.src is None:
                ck = extract_trailing_citekey(raw)
                if ck:
                    cur.src = ck
            seg = eng.trim_annotation(eng.strip_outer_quotes(raw))
            if seg and eng.is_english(seg):
                cur.extra_verbatim.append(seg)
            i += 1
            continue
        bm = BULLET_SKELETON_RE.match(s)
        if bm:
            cur.skeleton_seen = True
            inline = bm.group(1).strip()
            if inline:
                cur.templates.append(eng.normalize(eng.strip_outer_quotes(inline)))
            i += 1
            continue

        # --- bold fields -------------------------------------------------
        fm = FIELD_SRC_RE.match(s) or PLAIN_SRC_RE.match(s)
        if fm:
            cur.src = fm.group(1).strip()
            i += 1
            continue
        fm = PRIMARY_VERBATIM_RE.match(s)
        if fm:
            vtext = eng.strip_outer_quotes(fm.group(1)).strip()
            if vtext:
                cur.primary_verbatim = vtext
            i += 1
            continue
        fm = SECONDARY_VERBATIM_RE.match(s)
        if fm:
            inline = fm.group(1).strip()
            if inline:
                seg = eng.trim_annotation(eng.strip_outer_quotes(inline))
                if seg and eng.is_english(seg):
                    cur.extra_verbatim.append(seg)
                i += 1
                continue
            if i + 1 < len(lines) and lines[i + 1].strip().startswith(">"):
                j = i + 1
                while j < len(lines) and lines[j].strip().startswith(">"):
                    body = lines[j].strip()[1:].strip()
                    if body:
                        seg = eng.trim_annotation(eng.strip_outer_quotes(body))
                        if seg and eng.is_english(seg):
                            cur.extra_verbatim.append(seg)
                    j += 1
                i = j
                continue
            i += 1
            continue
        fm = FIELD_SLOT_RE.match(s)
        if fm:
            cur.slot_raw = fm.group(1).strip()
            i += 1
            continue
        fm = FIELD_SKELETON_RE.match(s)
        if fm:
            cur.skeleton_seen = True
            inline = fm.group(1).strip()
            if inline:
                cur.templates.append(eng.normalize(eng.strip_outer_quotes(inline)))
                i += 1
                continue
            if i + 1 < len(lines) and lines[i + 1].strip().startswith(">"):
                chunks: list[str] = []
                j = i + 1
                while j < len(lines) and lines[j].strip().startswith(">"):
                    body = lines[j].strip()[1:].strip()
                    body = eng.strip_outer_quotes(body)
                    if body:
                        chunks.append(body)
                    j += 1
                if chunks:
                    cur.templates.append(eng.normalize(" ".join(chunks)))
                i = j
                continue
            if i + 1 < len(lines) and lines[i + 1].strip().startswith("```"):
                fence = eng.collect_fence(lines, i + 1)
                if fence["text"]:
                    cur.templates.append(eng.normalize(fence["text"]))
                i = fence["end"] + 1
                continue
            i += 1
            continue

        # --- code fences inside a variant（SEM 族等）---------------------
        if s.startswith("```"):
            fence = eng.collect_fence(lines, i)
            if fence["text"]:
                cur.templates.append(eng.normalize(fence["text"]))
            i = fence["end"] + 1
            continue

        i += 1

    if cur is not None:
        variants.append(cur)

    # --- materialize entries（共享引擎；methods 特异钩子 = kind note/标题列）--
    n_num = sum(1 for v in variants if v.kind == "num")
    n_unnum = sum(1 for v in variants if v.kind == "unnum")
    n_extend = sum(1 for v in variants if v.kind == "extend")

    def slot_for(v: Variant) -> str:
        if v.slot_raw and v.slot_raw.strip():
            return normalize_slot(v.slot_raw)
        return normalize_slot(slot_table.get(v.vid))

    entries, unparsed = eng.materialize_variants(
        variants, slug=slug, relpath=relpath, slot_for=slot_for,
        primary_note=lambda v: KIND_NOTES[v.kind],
        extra_note=lambda v: (f"{KIND_NOTES[v.kind]}·原文锚定节"
                              if KIND_NOTES[v.kind] else "原文锚定节"),
        unparsed_where=lambda v: v.heading,
        citekey_fallback=lambda v: qsrc.get(v.vid))

    return entries, unparsed, n_num, n_unnum, n_extend


# ------------------------------------------------------------ rendering ----


def _header(family: dict[str, str], nv: int, nt: int, note: str = "") -> list[str]:
    out = [
        f"# {family['slug']} — 二级骨架清单（{family['name']}）",
        "",
        "> 本目录由脚本重建，手改会被覆盖；重建命令 = `python scripts/build_indices.py`（路径基准：以本 skill 目录（SKILL.md 所在目录）为基准）。",
        "> **抽取规则（先定后抽）**：verbatim = 卡片 `**原始句锚点**` / `[原始句锚点]` / `- **原始句锚点**（…）` 内带引号/缩进的完整英文原句（有明确来源论文，逐字保留、含 `…` 不回填）+ `**原文锚定**`/`**原文锚点**`（含 `- **原文锚定**` 子弹式）下 `- \"...\"` 英文句（id 后缀 .a/.b）；模板 = `**骨架**` / `**模板**` / `**模板/骨架**` / `**结构**` / `[骨架]` 块、代码围栏或紧随裸英文段内带 `[槽位]` 的填槽骨架。",
        "> **citekey** 优先取卡片尾部 `<!-- wb:... -->` 标记，无则回退 `**来源论文**`/`**来源**`/裸 `来源：`/`- **出处**` 原文；EXTEND 子变体回退 `- **原文锚定**` 尾部 `（citekey, …）` 标注；皆无标 `未标注`（不编造）。**适配槽位** 取 `**槽位**`/`[适用槽位]` 字段内 M1–M10（含 M2.5）与 Q1–Q8（去重排序）；无字段或含 `M?` 标 `通用`。",
        "> **锚点** = `corpus/<文件名>#变体-<变体号>`（脚本自定义片段，指向 `### 变体 <N>` 标题；不编号/EXTEND 变体指向其真实 `### 变体：`/`#### 变体：` 标题；`--verify` 断言标题存在）。",
        "> 状态列：`verbatim` = 逐字底本（与源卡片逐字一致，不得改写/拼接/补全）；`模板` = 填槽骨架（不可当逐字底本引用）。`不编号变体`（fang2025 POM，不计入 342）与 `EXTEND子变体`（`####` 层，不计入 342）在 id 与状态列标注。",
    ]
    if note:
        out.append(f"> {note}")
    out.append("")
    out.append(f"条目：verbatim {nv} 条 / 模板 {nt} 条。")
    out.append("")
    return out


def render_family(family: dict[str, str], entries: list[Entry]) -> str:
    verbatim = [e for e in entries if e.status == "verbatim"]
    templates = [e for e in entries if e.status == "模板"]
    out = _header(family, len(verbatim), len(templates))
    if verbatim:
        out += eng.render_table("Verbatim 底本", verbatim)
    if templates:
        out += eng.render_table("填槽模板", templates)
    if not verbatim and not templates:
        out.append("（无累积变体：骨架-only，主骨架见 `references/slot-M*.md`。）")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def render_sub_route(slug: str, name: str, groups: list[tuple[str, str, list[Entry]]]) -> str:
    return eng.render_sub_route(
        slug, name,
        split_note="> 本设计类型条目超 400 行，按 M/Q 槽位拆成子清单；先读本表定位槽位，再整份读入对应子清单。",
        groups=groups)


def render_route(stats: list[tuple[dict[str, str], int, int, int, str]], nv_total: int,
                 nt_total: int, unparsed_count: int, n_unnum: int, n_extend: int) -> str:
    out = [
        "# write-methods 骨架索引路由（两级）",
        "",
        "> **本目录由脚本重建，手改会被覆盖；重建命令 = `python scripts/build_indices.py`（路径基准：以本 skill 目录（SKILL.md 所在目录）为基准；`--check` 干跑、`--verify` 回源校验）。**",
        "> **两层结构**：本路由 + 每设计类型一份二级清单（或槽位拆分子清单）。先读「何时读它」定位设计类型，再整份读入对应二级清单。",
        "> **一级轴 = 设计类型**；**二级槽位维度 = M1–M10（含 M2.5）与 Q1–Q8（定性）**（见各二级清单「适配槽位」列）。",
        "> 状态列：`verbatim` = 逐字原句（无槽位、与源卡片逐字一致）；`模板` = 含 `[槽位]` 的填槽骨架。抽取规则全文见各二级清单头部。",
        "",
        "| 设计类型 | 对应 corpus 文件 | 变体数 | 何时读它 |",
        "|---|---|---|---|",
    ]
    for family, nvar, nv, nt, target in stats:
        out.append(
            f"| [`{family['slug']}`]({target}) | `corpus/{family['file']}` | {nvar} | {family['trigger']} |")
    out.append("")
    out.append(f"合计：{len(stats)} 设计类型 / {sum(s[1] for s in stats)} 编号变体 / verbatim {nv_total} 条 / 模板 {nt_total} 条。")
    if n_unnum or n_extend:
        out.append(f"另有 {n_unnum} 条不编号变体（`### 变体：`，fang2025 POM）与 {n_extend} 条 EXTEND 子变体（`#### 变体：`）——已抽取进各二级清单但**不计入**上面的 342（口径与 validator/INDEX/速查表一致）。")
    out.append("")
    out.append("## 待补录")
    out.append("")
    out.append(f"- [`_unparsed.md`](_unparsed.md)：{unparsed_count} 条未自动命中或结构不规整，**待人工判定**。")
    out.append("")
    return "\n".join(out)


# ----------------------------------------------------------------- main ----

def _heading_for(relpath: str, vid: str, anchor: str) -> str:
    """Rebuild the heading line an anchor points at, for verification.

    Numbered anchors (``变体-<token>``) are matched by a fresh scan of the
    source (independent of the parse); unnumbered/EXTEND anchors are matched
    by re-running the header regexes.
    """
    path = SKILL_ROOT / relpath
    src = path.read_text(encoding="utf-8")
    is_unnum = bool(re.match(r"^U\d+$", vid))
    is_extend = bool(re.match(r"^.+x\d+$", vid))
    if not is_unnum and not is_extend:
        # numbered/lettered: find `### 变体 <token>` line
        for raw in src.splitlines():
            m = re.match(r"^###\s+变体\s+" + re.escape(vid) + r"\s*[:：]", raw)
            if m:
                return raw
        return ""
    # unnumbered U<n> or extend <parent>x<n>: rescan in order
    unnum = 0
    extend: dict[str, int] = {}
    cur_vid: str | None = None
    for raw in src.splitlines():
        s = raw.strip()
        m = VARIANT_HDR_RE.match(s)
        if m:
            cur_vid = m.group(1)
            continue
        m = UNNUM_HDR_RE.match(s)
        if m:
            unnum += 1
            cur_vid = f"U{unnum}"
            if cur_vid == vid:
                return raw
            continue
        m = EXTEND_HDR_RE.match(s)
        if m:
            parent = cur_vid if cur_vid else "?"
            n = extend.get(parent, 0) + 1
            extend[parent] = n
            if f"{parent}x{n}" == vid:
                return raw
            continue
    return ""


def main(argv: list[str] | None = None) -> int:
    ap = eng.build_argparser(__doc__)
    args = ap.parse_args(argv)

    all_entries: list[Entry] = []
    all_unparsed: list[Unparsed] = []
    stats: list[tuple[dict[str, str], int, int, int, str]] = []
    rendered: dict[str, str] = {}
    n_unnum_total = 0
    n_extend_total = 0

    for family in FAMILIES:
        entries, unparsed, n_num, n_unnum, n_extend = parse_file(family)
        all_entries.extend(entries)
        all_unparsed.extend(unparsed)
        n_unnum_total += n_unnum
        n_extend_total += n_extend
        nv = sum(1 for e in entries if e.status == "verbatim")
        nt = sum(1 for e in entries if e.status == "模板")
        text = render_family(family, entries)
        target = f"{family['slug']}.md"
        if len(text.splitlines()) > MAX_LINES and entries:
            groups: dict[str, list[Entry]] = {}
            for e in entries:
                groups.setdefault(slot_key(e), []).append(e)
            ordered = sorted(groups.items(), key=lambda kv: (kv[0] == "general", kv[0]))
            group_files: list[tuple[str, str, list[Entry]]] = []
            for key, ents in ordered:
                label = _slot_group_label(key)
                fname = f"{family['slug']}-{key}.md"
                rendered[fname] = eng.render_slot_file(
                    family["slug"], family["name"], label, ents, header_fn=_header)
                group_files.append((label, fname, ents))
            text = render_sub_route(family["slug"], family["name"], group_files)
        rendered[target] = text
        stats.append((family, n_num, nv, nt, target))

    nv_total = sum(1 for e in all_entries if e.status == "verbatim")
    nt_total = sum(1 for e in all_entries if e.status == "模板")
    route = render_route(stats, nv_total, nt_total, len(all_unparsed),
                         n_unnum_total, n_extend_total)
    unparsed_text = eng.render_unparsed(all_unparsed)

    counts: dict[str, int] = {"entries": len(all_entries),
                              "unparsed": len(all_unparsed)}

    # --- verification -----------------------------------------------------
    if args.verify:
        mismatch = eng.print_verbatim_check(all_entries, SKILL_ROOT, nv_total)

        # anchor verification: heading line must appear in source
        anchor_miss: list[Entry] = []
        src_cache: dict[str, str] = {}
        for e in all_entries:
            src = src_cache.get(e.path)
            if src is None:
                src = eng.normalize((SKILL_ROOT / e.path).read_text(encoding="utf-8"))
                src_cache[e.path] = src
            head = eng.normalize(_heading_for(e.path, e.vid, e.anchor))
            if head and head not in src:
                anchor_miss.append(e)
        total = len(all_entries)
        print(f"锚点标题存在校验: {total - len(anchor_miss)}/{total} 锚点指向的变体标题存在")
        for e in anchor_miss:
            print(f"  ANCHOR-MISS {e.id} ({e.path}#{e.anchor})")

        eng.print_sample_check(all_entries, SKILL_ROOT, args.sample)
        counts["mismatch"] = mismatch
        counts["anchor_miss"] = len(anchor_miss)

    # --- report -----------------------------------------------------------
    if not args.quiet:
        eng.print_report(stats, rendered, nv_total, nt_total, len(all_unparsed),
                         extra_lines=(f"不编号变体: {n_unnum_total} / "
                                      f"EXTEND 子变体: {n_extend_total}",))

    if args.check:
        return counts

    eng.write_skeleton(SKELETON, rendered, route, unparsed_text)
    return counts


if __name__ == "__main__":
    sys.exit(eng.entrypoint("write-methods", main))
