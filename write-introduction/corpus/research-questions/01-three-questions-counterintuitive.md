---
type: canonical_research_question
canonical_id: "01-three-questions-counterintuitive"
status: EMERGING
gap_type: Incompleteness
cross_paper: EMERGING
generativity: ADAPTABLE
exclusivity: LOW
source_papers:
  - kim2022 (MS, 2022): "Three numbered RQs each with counterintuitive follow-up; previews non-monotonic findings"
created: 2026-05-24
source: Distilled by distill-introduction-exemplar Phase 4.6
---

# 01-three-questions-counterintuitive — 三问法（含反直觉追问）

## 功能描述

将研究问题以编号列表形式呈现，每个问题包含正面提问 + 反直觉追问。反直觉追问预告了论文的 non-monotonic / counterintuitive 发现，同时建立了 "这篇文章不是在讲显而易见的故事" 的读者预期。

## 适用场景

- Gap 类型 = **Incompleteness** 或 **Inadequacy**（Incommensurability 通常不需要编号 RQ）
- 研究有 2-4 个明确可分离的研究问题
- 论文有反直觉发现需要预告
- 目标期刊接受显式 RQ 列表（MS、MSOM、POM、JOM 等；AMJ/ASQ 较少使用编号 RQ）

## 验证状态

### 跨论文复现
- **EMERGING** (1 paper): kim2022 (MS)

### 生成力
- **ADAPTABLE**: RQ 三问法是广泛使用的模式；反直觉追问的附加可迁移到任何有 counterintuitive findings 的研究

### 排他性
- **LOW**: 所有 Gap 类型和贡献维度均可使用（但 Incommensurability 通常以 "debate" 而非 "questions" 框架组织）

---

## 句法模板

### 变体 A：三问 + 反直觉追问（kim2022 型）

**模板**:
> "In this study, we shed light on how [actors] determine [core decision] when facing [key uncertainties], as well as the implications of this decision for [upstream activity]. Our analysis addresses the following specific research questions:
>
> - Under what conditions do [actors] [Action A] versus [Action B]? [Counterintuitive follow-up: Are they always more likely to [expected behavior] as [variable] increases?]
> - What are the implications of [decision] on [outcome 1] and [outcome 2]? How does [moderating/contextual variable] influence [decisions and outcomes]?
> - What is the relationship between [upstream phenomenon] and [ex ante behavior]? [Counterintuitive follow-up: Does an increase in [variable] always depress [behavior]?]"

**来源**: kim2022 (MS), P6

**原文锚定**:
> "In this study, we shed light on how firms determine whether to conduct rigorous quality assurance testing when facing uncertainty over product failure and competitive pressures, as well as the implications of this decision for undertaking innovation efforts. Our analysis addresses the following specific research questions:
>
> - Under what conditions do firms conduct versus forgo time-consuming quality assurance testing of their innovation prior to launch? Are firms always more likely to conduct such testing as the negative consequences of a recall increase?
> - What are the implications of firms' testing and launch-timing decisions on pricing and profits? How does greater heterogeneity in consumer preferences influence firms' decisions and profit levels?
> - What is the relationship between the possibility of a product recall and firms' ex ante willingness to innovate? Does an increase in the likelihood of post-launch product failure always depress firms' incentives to invest in R&D?"

**关键特征**:
- 每个 RQ 包含一个正面提问 + 一个反直觉追问——预告论文的 counterintuitive 发现，建立 "这篇文章不是在讲显而易见的故事" 的读者预期
- 三个 RQ 按模型层次递进：核心决策 → 市场后果 → 上游创新投入——映射论文的分析结构
- 以 bullet points 呈现，视觉上清晰分离三个问题——比 "We ask: (1)... (2)... (3)..." 的 inline 格式更易读
- RQ 编号使读者可对照后文的 equilibria 和 results 进行验证——建立可验证性预期
- 反直觉追问以一般疑问句形式（"Are they always...?" / "Does... always...?"），暗示答案通常是 "No"

**适用**: 适用于分析模型论文和实证论文——有多个明确可分离的研究问题；特别适合 MS、MSOM、POM 等接受显式 RQ 列表的期刊；反直觉追问适用于确实发现了 non-monotonic 或 counterintuitive 结果的论文

**禁忌**: "RQ 不要超过 4 个（超过则读者失去焦点）；每个 RQ 必须可在论文中找到对应的 analysis/result section；反直觉追问必须基于真实的发现——如果论文没有反直觉结果，不要为了吸睛而发明一个；'Are they always...?' 式追问预设答案为 'No'——如果答案确实是 'Yes'，不要用此格式"

---

## 组装规则

### 必须配对
- **与 Preview 配对**: RQ 提出后必须有 Preview 段回应（"To answer these questions, we..."）
- **与 Contribution 配对**: RQ 的反直觉追问必须在 Contribution 段得到兑现（"The analysis further reveals an interesting property..."）

### 互斥
- **不适合与 Incommensurability 直接配对**: Incommensurability 的 RQ 通常以 "debate" 或 "paradox" 框架组织，而非编号列表

### 反模式提醒
- **不要只问不答**: 每个 RQ 必须在分析中有对应的解答
- **不要让 RQ 列表过长**: 3 个是最优数量，4 个是上限，5+ 个失去焦点
- **不要在 RQ 中做理论承诺**: RQ 是问题，不是假设——不要在 RQ 中夹带 "Drawing on..." 等理论框架引入

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| MS | ⭐⭐⭐⭐⭐ | 编号 RQ 是 MS 建模论文的标准做法 |
| MSOM | ⭐⭐⭐⭐⭐ | 同 MS |
| POM | ⭐⭐⭐⭐⭐ | 同 MS |
| JOM | ⭐⭐⭐⭐☆ | 可用，但常与 "research gap" 段落合并 |
| SMJ | ⭐⭐⭐☆☆ | 较少使用显式编号 RQ——更偏好以 Puzzle 驱动 |
| AMJ/ASQ | ⭐⭐☆☆☆ | 几乎不使用编号 RQ——以叙事驱动的 Puzzle 代替 |

---

## 槽位填充正误对比

### `[Counterintuitive follow-up]` — 反直觉追问

❌ "Are firms always rational?" → 太宽泛，无法在论文中真正回答

✅ "Are firms always more likely to conduct such testing as the negative consequences of a recall increase?" → 具体、可检验、预告了论文的 non-monotonic 发现

**填充检查**: 反直觉追问的答案必须能从后文的 analysis/results 中提取——如果答案不是 "No, and here's when..." 就不要使用此句式
