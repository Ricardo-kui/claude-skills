#!/usr/bin/env python3
"""Build the two-level skeleton index for the write-results corpus (pilot).

Single source of truth
----------------------
Extracts *verbatim* original-sentence anchors and *fill-in templates* from the
corpus ``.md`` files and writes them ONLY under ``corpus/_skeleton/``.  Every
other consumer (shape packs, 借句表, retrieval sidecars) must reference these
entries by ``id`` and must not copy the text.

Extraction rules (先定后抽, also written into every generated file header)
---------------------------------------------------------------------------
verbatim  = 卡片里带引号/缩进的完整英文原句（有明确来源论文），逐字保留：
            * 主来源 ``**原始句锚点**: ...`` 字段（逐字，含 ``…`` 省略号，不回填）
            * 次生来源 ``#### 原文锚定`` 下 ``- "..."`` 带引号英文句（id 后缀 .a/.b）
模板     = ``**骨架**:`` / ``**骨架/框架**:`` 后的 ``>`` 引用块或 ``` 代码围栏
           （含 ``[槽位]`` 占位符的句式骨架）；SEM 族无 ``**骨架**`` 字段，
           其变体块内的代码围栏按位置视同模板。
锚点     = ``corpus/<文件名>#变体-<变体号>``；``--verify`` 断言该标题存在。
citekey  = 优先取卡片尾部 ``<!-- wb:<citekey>:... -->`` 标记（机器可读），
           无则回退 ``**来源论文**`` 原文；两者皆无标 ``未标注``（不编造）。
适配槽位 = 取 ``**槽位**:`` 字段内 R1–R9（去重排序），判断不了或含 F 槽位
           （定性）标 ``通用``。

Anything that does not match is collected in ``_skeleton/_unparsed.md``.

Output
------
- ``corpus/_skeleton/_index.md``   level-1 route by model family (<= 120 lines)
- ``corpus/_skeleton/<slug>.md``   level-2 list per family; split by slot when
                                   the rendered file would exceed MAX_LINES.
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
只保留 write-results 特异的：FAMILIES 模型族表、标题与字段正则、R1–R9 槽位
机制、二级清单/路由页模板文本、集合式锚点校验。
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

# One entry per corpus model-family file.  ``slug`` is the level-2 index
# filename stem and also the family prefix of every entry id.
FAMILIES: list[dict[str, str]] = [
    {"file": "OLS-FE.md", "slug": "ols-fe", "name": "OLS-FE（面板/截面线性）",
     "desc": "线性/面板 OLS-FE 结果段全槽位（主假设、交互调节、经济显著性、稳健性）",
     "trigger": "主模型是 OLS/FE/动态面板/SUR 时写 R1–R9 结果段，或需要表导航/幅度翻译/稳健性叙述"},
    {"file": "Logit-Probit-Ordered-Probit.md", "slug": "logit-probit-ordered-probit",
     "name": "Logit-Probit-Ordered-Probit",
     "desc": "二元/有序/条件 Logit、Probit 的结果报告（OR、边际概率、阈值、Heckman/内生转换）",
     "trigger": "DV 是二元/有序/类别变量，需要 OR/概率尺度翻译或分样本二元模型裁决"},
    {"file": "生存分析.md", "slug": "survival-analysis",
     "name": "生存分析（AFT/Cox）",
     "desc": "风险模型 AFT 四拍、exp(β)−1 百分比、交互与分样本风险报告",
     "trigger": "DV 是时长/生存时间，需 hazard/exp(β) 或「四拍+百分比」风险结果"},
    {"file": "DiD.md", "slug": "did", "name": "DiD / 事件差分",
     "desc": "DiD 交互项幅度、平行趋势、分样本条件效应与识别威胁电池",
     "trigger": "因果设计是 DiD/准实验，需交互项幅度翻译、pre-trend 或 placebo 稳健性"},
    {"file": "计数模型.md", "slug": "count-models", "name": "计数模型（负二项/Poisson）",
     "desc": "计数 DV 主效应四拍、exp(β) 乘法翻译、倒U链、文本测量稳健性",
     "trigger": "DV 是计数（召回次数/专利数），需发生率比翻译或计数诊断"},
    {"file": "实验.md", "slug": "experiments", "name": "实验（ANOVA/PROCESS）",
     "desc": "实验主效应 ANOVA 五拍、中介 Hayes PROCESS、条件干预拆解",
     "trigger": "数据来自实验/多研究，需 F/p/η² 或 PROCESS 中介报告"},
    {"file": "多研究.md", "slug": "multi-study", "name": "多研究综合",
     "desc": "跨研究镜像首句、逐研究收敛与边界保留、跨研究差异讨论",
     "trigger": "一篇论文含多个 study，需跨研究综合或差异解释"},
    {"file": "定性过程研究.md", "slug": "qualitative-process", "name": "定性过程研究",
     "desc": "过程模型总览、前台/后台/侧台对照、引语选择框架（F1–F6，非 R1–R9）",
     "trigger": "定性 Findings（过程模型/引语），非量化假设检验"},
    {"file": "IV-2SLS.md", "slug": "iv-2sls", "name": "IV-2SLS / 3SLS",
     "desc": "工具变量两阶段、弱识别/排他性、控制函数、3SLS 系统",
     "trigger": "需内生性修正（2SLS/IV），报第一阶段 F、排他性或弱识别诊断"},
    {"file": "匹配DiD.md", "slug": "matched-did", "name": "匹配 DiD",
     "desc": "CEM 匹配作准实验事前对称威胁回应",
     "trigger": "DiD 前用匹配（CEM/PSM）构造可比处理/对照"},
    {"file": "Tobit.md", "slug": "tobit", "name": "Tobit / 左删失",
     "desc": "删失 DV 条件幅度四拍 + 实际重要性拍",
     "trigger": "DV 在 0 处删失/受限（如召回延迟下限），需 Tobit 报告"},
    {"file": "堆叠扩散Logit.md", "slug": "stacked-diffusion-logit", "name": "堆叠扩散 Logit",
     "desc": "（骨架-only，无累积变体）",
     "trigger": "扩散/采纳 Logit 结构模型（当前无验证变体）"},
    {"file": "同伴效应-网络效应.md", "slug": "peer-network-effects", "name": "同伴/网络效应",
     "desc": "（骨架-only，无累积变体）",
     "trigger": "同伴效应或网络效应结果（当前无验证变体）"},
    {"file": "推断二元结果.md", "slug": "binary-outcome-inference", "name": "推断二元结果",
     "desc": "（骨架-only，无累积变体）",
     "trigger": "二元结果的因果推断（当前无验证变体）"},
    {"file": "跨受众构念对比.md", "slug": "cross-audience-construct", "name": "跨受众构念对比",
     "desc": "同一构念跨两类受众的镜像相反效应（独立模型 + 镜像符号 + 分受众翻译）",
     "trigger": "同一 IV 在两受众/两 DV 上符号相反，需镜像对比报告"},
    {"file": "三向交互.md", "slug": "three-way-interaction", "name": "三向交互",
     "desc": "三向交互条件分解、连续调节三向、中和阈值",
     "trigger": "模型含三向交互，需条件两向分解或简单斜率差异"},
    {"file": "构造暴露分解.md", "slug": "construct-exposure-decomposition", "name": "构造暴露分解",
     "desc": "（骨架-only，无累积变体）",
     "trigger": "构造暴露分解结果（当前无验证变体）"},
    {"file": "SEM-moderated-mediation.md", "slug": "sem-moderated-mediation", "name": "SEM / 调节中介",
     "desc": "SEM 路径/条件间接效应、抑制变量、竞争排序敏感性",
     "trigger": "SEM/调节中介报告（路径系数、条件间接效应、fit 指标）"},
    {"file": "事件研究法.md", "slug": "event-study", "name": "事件研究法",
     "desc": "CAR 分组裁决、检验统计量背书、时序符号反转高潮",
     "trigger": "事件研究 CAR/AR，需分组裁决、t 检验或主效应保护段"},
    {"file": "VARX-PVAR.md", "slug": "varx-pvar", "name": "VARX / PVAR",
     "desc": "GIRF 弹性/美元翻译、FEVD 相对重要性、wear-in/out 动态",
     "trigger": "向量自回归/脉冲响应，需弹性表或方差分解解读"},
    {"file": "BLP-状态空间.md", "slug": "blp-state-space", "name": "BLP / 状态空间",
     "desc": "BLP 结构需求、Kalman/GMM 状态空间拟合与反事实",
     "trigger": "结构需求或状态空间模型，需拟合/反事实报告"},
]

# ------------------------------------------------------------- regexes -----

VARIANT_HDR_RE = re.compile(r"^###\s+变体\s+([^:\s：]+)\s*[:：]?(.*)$")
WB_RE = re.compile(r"<!--\s*wb:([^:\s]+)")
FIELD_SRC_RE = re.compile(r"^\*\*来源(?:论文)?\*\*\s*[:：]\s*(.*)$")
PLAIN_SRC_RE = re.compile(r"^来源[:：]\s*(.*)$")
PRIMARY_VERBATIM_RE = re.compile(r"^\*\*原始句锚点\*\*\s*[:：]\s*(.*)$")
SECONDARY_VERBATIM_RE = re.compile(r"^\*\*原文锚定\*\*(?:\([^)]*\))?\s*[:：]?\s*(.*)$")
BRACKET_VERBATIM_RE = re.compile(r"^\[原始句锚点\]\s*(.*)$")
FIELD_SLOT_RE = re.compile(r"^\*\*槽位\*\*\s*[:：]\s*(.*)$")
FIELD_SKELETON_RE = re.compile(r"^\*\*(?:骨架(?:/框架)?|模板(?:/骨架)?)\*\*\s*[:：]?\s*(.*)$")
R_TOKEN_RE = re.compile(r"\bR([1-9])\b")
R_ANY_TOKEN_RE = re.compile(r"\bR(\d+|\?)\b")
SLOT_CELL_RE = re.compile(r"^(R[1-9]|F[1-9])$")


def normalize_slot(raw: str | None) -> str:
    if not raw:
        return "通用"
    tokens = sorted({int(m) for m in R_TOKEN_RE.findall(raw)})
    if tokens:
        return "/".join(f"R{t}" for t in tokens)
    return "通用"


def slot_anomaly(raw: str) -> str | None:
    """Return a human note when the raw slot has R-ish tokens out of R1–R9."""
    tokens = R_ANY_TOKEN_RE.findall(raw)
    bad = [t for t in tokens if t not in {str(i) for i in range(1, 10)}]
    return f"槽位含异常 token {','.join(bad)}" if bad else None


# ------------------------------------------------------------- parsing -----


@dataclass
class Variant:
    vid: str
    title: str
    start: int
    wb: list[str] = field(default_factory=list)
    src: str | None = None
    slot_raw: str | None = None
    primary_verbatim: str | None = None
    templates: list[str] = field(default_factory=list)
    extra_verbatim: list[str] = field(default_factory=list)
    skeleton_seen: bool = False
    seen_field: bool = False


def slot_key(e: Entry) -> str:
    m = R_TOKEN_RE.search(e.slot)
    return f"r{m.group(1)}" if m else "general"


def parse_file(family: dict[str, str]) -> tuple[list[Entry], list[Unparsed], int]:
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
        return entries, unparsed, 0
    slot_table = eng.build_slot_table(lines, SLOT_CELL_RE, min_cells=2)

    variants: list[Variant] = []
    cur: Variant | None = None
    in_comment = False
    i = 0
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
            if cur is not None:
                variants.append(cur)
            cur = Variant(vid=m.group(1), title=m.group(2).strip(), start=i)
            i += 1
            continue

        if cur is None:
            i += 1
            continue

        # bracket-form verbatim: [原始句锚点] "..."（ball_2018 型）
        bm = BRACKET_VERBATIM_RE.match(s)
        if bm:
            seg = eng.trim_annotation(eng.strip_outer_quotes(bm.group(1)))
            if seg and eng.is_english(seg):
                cur.extra_verbatim.append(seg)
            cur.seen_field = True
            i += 1
            continue

        # leading bare prose skeleton (ball_2018-style, before any **field**)
        if (not cur.seen_field and s
                and not s.startswith(("#", ">", "-", "*", "|", "`", "[", "<!--"))):
            if "[" in s and eng.is_english(s):
                cur.templates.append(eng.normalize(s))
            i += 1
            continue

        if s.startswith("**"):
            cur.seen_field = True

        # --- field lines inside a variant block ---------------------------
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
                if seg:
                    cur.extra_verbatim.append(seg)
                i += 1
                continue
            # blockquote form: **原文锚定**:\n> "..."  (one entry per > line)
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
                # rare: template glued on the header line itself
                cur.templates.append(eng.normalize(eng.strip_outer_quotes(inline)))
                i += 1
                continue
            # blockquote form: **骨架**:\n> ...
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
            # code-fence form: **骨架**:\n``` ... ```
            if i + 1 < len(lines) and lines[i + 1].strip().startswith("```"):
                fence = eng.collect_fence(lines, i + 1)
                if fence["text"]:
                    cur.templates.append(eng.normalize(fence["text"]))
                i = fence["end"] + 1
                continue
            # otherwise: table / plain prose after the header -> structural
            i += 1
            continue

        # --- code fences inside a variant (SEM族 etc.) --------------------
        if s.startswith("```"):
            fence = eng.collect_fence(lines, i)
            if fence["text"]:
                cur.templates.append(eng.normalize(fence["text"]))
            i = fence["end"] + 1
            continue

        # --- secondary verbatim: #### 原文锚定 -> "- \"...\"" -------------
        if s.startswith("####") and ("原文锚定" in s or "语料锚定" in s):
            j = i + 1
            while j < len(lines):
                ln = lines[j].strip()
                if ln.startswith("#") or FIELD_SKELETON_RE.match(ln) or ln.startswith("**"):
                    break
                if ln.startswith("- ") or ln.startswith("* "):
                    body = ln[2:].strip()
                    if body.startswith('"'):
                        quote = eng.trim_annotation(eng.strip_outer_quotes(body))
                        if quote and eng.is_english(quote):
                            cur.extra_verbatim.append(quote)
                    # non-quoted (Chinese summary) bullets are ignored here
                elif ln == "":
                    pass
                else:
                    break
                j += 1
            i = j
            continue

        i += 1
    if cur is not None:
        variants.append(cur)

    # --- materialize entries（共享引擎；results 特异钩子 = 槽位异常待补录）--
    def slot_for(v: Variant) -> str:
        if v.slot_raw and v.slot_raw.strip():
            return normalize_slot(v.slot_raw)
        return normalize_slot(slot_table.get(v.vid))

    def extra_unparsed(v: Variant, out: list[Unparsed]) -> None:
        if not v.slot_raw:
            return
        note = slot_anomaly(v.slot_raw)
        if note:
            out.append(Unparsed(card=v.vid, path=relpath,
                                where="**槽位**", text=(v.slot_raw or "")[:200],
                                reason=note))

    entries, unparsed = eng.materialize_variants(
        variants, slug=slug, relpath=relpath, slot_for=slot_for,
        extra_unparsed=extra_unparsed)

    return entries, unparsed, len(variants)


# ------------------------------------------------------------ rendering ----


def _header(family: dict[str, str], nv: int, nt: int, note: str = "") -> list[str]:
    out = [
        f"# {family['slug']} — 二级骨架清单（{family['name']}）",
        "",
        "> 本目录由脚本重建，手改会被覆盖；重建命令 = `python scripts/build_indices.py`（路径基准：以本 skill 目录（SKILL.md 所在目录）为基准）。",
        "> **抽取规则（先定后抽）**：verbatim = 卡片 `**原始句锚点**` 内带引号/缩进的完整英文原句（有明确来源论文，逐字保留、含 `…` 不回填）+ `#### 原文锚定` 下 `- \"...\"` 英文句（id 后缀 .a/.b）；模板 = 卡片 `**骨架**` / `**骨架/框架**` 块或代码围栏内带 `[槽位]` 的填槽骨架。",
        "> **citekey** 优先取卡片尾部 `<!-- wb:... -->` 标记，无则回退 `**来源论文**` 原文，两者皆无标 `未标注`（不编造）。**适配槽位** 取 `**槽位**:` 字段内 R1–R9（去重排序）；无字段时回退文件内「槽位分布」表；仍判断不了或含 F 槽位标 `通用`。",
        "> **锚点** = `corpus/<文件名>#变体-<变体号>`（脚本自定义片段，指向 `### 变体 <N>` 标题；`--verify` 断言该标题存在）。",
        "> 状态列：`verbatim` = 逐字底本（与源卡片逐字一致，不得改写/拼接/补全）；`模板` = 填槽骨架（不可当逐字底本引用）。",
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
        out.append("（无累积变体：骨架-only，主骨架见 `references/slot-R*.md`。）")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def render_sub_route(slug: str, name: str, groups: list[tuple[str, str, list[Entry]]]) -> str:
    return eng.render_sub_route(
        slug, name,
        split_note="> 本模型族条目超 400 行，按 R1–R9 槽位拆成子清单；先读本表定位槽位，再整份读入对应子清单。",
        groups=groups)


def render_route(stats: list[tuple[dict[str, str], int, int, int, str]], nv_total: int,
                 nt_total: int, unparsed_count: int) -> str:
    out = [
        "# write-results 骨架索引路由（两级）",
        "",
        "> **本目录由脚本重建，手改会被覆盖；重建命令 = `python scripts/build_indices.py`（路径基准：以本 skill 目录（SKILL.md 所在目录）为基准；`--check` 干跑、`--verify` 回源校验）。**",
        "> **两层结构**：本路由 + 每模型族一份二级清单（或槽位拆分子清单）。先读「何时读它」定位模型族，再整份读入对应二级清单。",
        "> **一级轴 = 模型族**；**二级槽位维度 = R1–R9**（见各二级清单「适配槽位」列）。",
        "> 状态列：`verbatim` = 逐字原句（无槽位、与源卡片逐字一致）；`模板` = 含 `[槽位]` 的填槽骨架。抽取规则全文见各二级清单头部。",
        "",
        "| 模型族 | 对应 corpus 文件 | 变体数 | 何时读它 |",
        "|---|---|---|---|",
    ]
    for family, nvar, nv, nt, target in stats:
        out.append(
            f"| [`{family['slug']}`]({target}) | `corpus/{family['file']}` | {nvar} | {family['trigger']} |")
    out.append("")
    out.append(f"合计：{len(stats)} 模型族 / verbatim {nv_total} 条 / 模板 {nt_total} 条。")
    out.append("")
    out.append("## 待补录")
    out.append("")
    out.append(f"- [`_unparsed.md`](_unparsed.md)：{unparsed_count} 条未自动命中或结构不规整，**待人工判定**。")
    out.append("")
    return "\n".join(out)


# ----------------------------------------------------------------- main ----

def _variant_headings(path: Path) -> set[str]:
    """Set of real variant ids (headings) in a source file, comments stripped."""
    ids: set[str] = set()
    in_comment = False
    for raw in path.read_text(encoding="utf-8").splitlines():
        s = raw.strip()
        if in_comment:
            if "-->" in s:
                in_comment = False
            continue
        if s.startswith("<!--"):
            if "-->" not in s:
                in_comment = True
            continue
        m = VARIANT_HDR_RE.match(s)
        if m:
            ids.add(m.group(1))
    return ids


def main(argv: list[str] | None = None) -> int:
    ap = eng.build_argparser(__doc__)
    args = ap.parse_args(argv)

    all_entries: list[Entry] = []
    all_unparsed: list[Unparsed] = []
    stats: list[tuple[dict[str, str], int, int, int, str]] = []
    rendered: dict[str, str] = {}

    for family in FAMILIES:
        entries, unparsed, nvar = parse_file(family)
        all_entries.extend(entries)
        all_unparsed.extend(unparsed)
        nv = sum(1 for e in entries if e.status == "verbatim")
        nt = sum(1 for e in entries if e.status == "模板")
        text = render_family(family, entries)
        target = f"{family['slug']}.md"
        if len(text.splitlines()) > MAX_LINES and entries:
            # split by primary slot
            groups: dict[str, list[Entry]] = {}
            for e in entries:
                groups.setdefault(slot_key(e), []).append(e)
            labels = {"r1": "R1", "r2": "R2", "r3": "R3", "r4": "R4", "r5": "R5",
                      "r6": "R6", "r7": "R7", "r8": "R8", "r9": "R9", "general": "通用"}
            ordered = sorted(groups.items(), key=lambda kv: (kv[0] == "general", kv[0]))
            group_files: list[tuple[str, str, list[Entry]]] = []
            for key, ents in ordered:
                label = labels.get(key, key)
                fname = f"{family['slug']}-{key}.md"
                rendered[fname] = eng.render_slot_file(
                    family["slug"], family["name"], label, ents, header_fn=_header)
                group_files.append((label, fname, ents))
            text = render_sub_route(family["slug"], family["name"], group_files)
        rendered[target] = text
        stats.append((family, nvar, nv, nt, target))

    nv_total = sum(1 for e in all_entries if e.status == "verbatim")
    nt_total = sum(1 for e in all_entries if e.status == "模板")
    route = render_route(stats, nv_total, nt_total, len(all_unparsed))
    unparsed_text = eng.render_unparsed(all_unparsed)

    counts: dict[str, int] = {"entries": len(all_entries),
                              "unparsed": len(all_unparsed)}

    # --- verification -----------------------------------------------------
    if args.verify:
        mismatch = eng.print_verbatim_check(all_entries, SKILL_ROOT, nv_total)

        headings_cache: dict[str, set[str]] = {}
        anchor_miss: list[Entry] = []
        for e in all_entries:
            heads = headings_cache.get(e.path)
            if heads is None:
                heads = _variant_headings(SKILL_ROOT / e.path)
                headings_cache[e.path] = heads
            if e.vid not in heads:
                anchor_miss.append(e)
        total = len(all_entries)
        print(f"锚点标题存在校验: {total - len(anchor_miss)}/{total} 锚点指向的「### 变体 N」标题存在")
        for e in anchor_miss:
            print(f"  ANCHOR-MISS {e.id} ({e.path}#{e.anchor})")

        eng.print_sample_check(all_entries, SKILL_ROOT, args.sample)
        counts["mismatch"] = mismatch
        counts["anchor_miss"] = len(anchor_miss)

    # --- report -----------------------------------------------------------
    if not args.quiet:
        eng.print_report(stats, rendered, nv_total, nt_total, len(all_unparsed))

    if args.check:
        return counts

    eng.write_skeleton(SKELETON, rendered, route, unparsed_text)
    return counts


if __name__ == "__main__":
    sys.exit(eng.entrypoint("write-results", main))
