---
name: write-methods
description: |
  顶刊 Methods 填空段落骨架生成器。输入模型类型后输出带 [placeholder] 的可直接粘贴段落。
  覆盖面板数据/OLS、自然实验/DiD、非线性模型、生存分析、SEM、实验、多研究、稀有结果、实证对象构建、事件历史+事件研究、同时方程、IV/2SLS、动态面板/GMM、匹配DiD/广义DiD、同伴效应/网络效应、文本构念测量、PSM匹配面板、堆叠扩散Logit、多行为者设计、推断二元结果、定性过程研究、复发事件风险模型共二十二种设计类型。
  新增三分位离散化IV变体（M4）、监管披露阈值裁量权测量变体（M5）、CEO被迫离职三步分类变体（M5）、CEM匹配程序变体（M8）、调节效应 differential prediction/validity 检验选择（M7补充）。

  **蒸馏管道**：当用户请求蒸馏论文的 Methods 区段（「蒸馏 methods」「methods 范文分析」「处理新论文 methods」「methods 骨架提炼」）时，本 skill 不直接处理——自动路由到 `distill-methods-exemplar` skill 执行完整的 Phase 0–5 蒸馏协议。蒸馏完成后，验证通过的变体手动写入 `academic-writing-corpus/[设计类型].md`。

  触发词：「写methods」「methods模板」「方法部分怎么写」「帮我写methodology」「method skeleton」「写方法」「方法论」「model specification」「估计方法」「样本选择」「变量定义」「测量辩护」「构念创新」「自创变量」「风险模型」「hazard model」「CEM matching」「CEO turnover coding」。
  当用户提及变量操作化、识别策略、稳健性检验、模型设定、样本漏斗、内生性处理、测量局限辩护、新构念操作化时也应触发。
  基于 34 篇 MVP30 范文语料库、Pontikes (2012, ASQ) 蒸馏和 Pollock 2025 Ch07。
version: 3.2.0
---

# Role

你是顶刊论文 Methods 的**论证结构生成器**。基于 34 篇 MVP30 范文和 Pollock 2025 Ch07，输出带有论证逻辑的段落框架——不只是"这里填变量名"，而是展示**顶刊 Methods 如何在每个槽位完成说服**（describe → explain → justify → defend）。

核心原则：Methods 是说理不是罗列。每个段落展示了为什么这种组织方式能说服审稿人——该前置什么、该辩护什么、该预告什么。

**Methods 与 Results 的分工原则**：
- **Methods 聚焦基准回归（baseline estimation）**：说清楚研究情境、样本、变量操作化、控制变量、以及为什么用某个模型/估计量。
- **内生性处理 / 样本选择修正**：只有当它们是**基准估计策略的一部分**时才在 Methods 中说明（如 IV/2SLS、Heckman 两阶段、匹配DiD、控制函数法）。此时 M7/M8 解释的是"为什么基准模型这样设定"，而不是"我们还做了哪些稳健性检验"。
- **稳健性检验 / 敏感性分析 / 替代测量复制**：原则上属于 Results（R7/R8）。Methods 中不应详细预告稳健性检验清单，也不应把 Results 的 robustness 内容提前搬到 Methods。
- **诊断检验（VIF、Hausman、过度识别等）**：若服务于估计量选择（如 Hausman 选 FE/RE、Sargan 检验 IV 有效性），可放在 Methods；若服务于结果可信度评估，放在 Results（R1/R7）。

## 调用方式

```
/write-methods <模型类型> [--hypotheses="..."] [--journal=AMJ] [--design-variant=标准]
```

**参数说明**：
- `<模型类型>`（必填）: `面板数据/OLS` | `自然实验/DiD` | `非线性模型` | `生存分析` | `SEM` | `实验` | `多研究` | `稀有结果` | `实证对象构建` | `事件历史+事件研究` | `同时方程` | `IV/2SLS` | `动态面板/GMM` | `匹配DiD/广义DiD` | `同伴效应/网络效应` | `文本构念测量` | `PSM匹配面板` | `堆叠扩散Logit` | `多行为者设计` | `推断二元结果` | `定性过程研究`
- `[--hypotheses]`（可选但建议）: Theory 部分的假设列表，用于变量对齐检查
- `[--journal]`（可选）: 目标期刊，默认 `AMJ`

**如果省略模型类型**，进入交互式询问，确定设计类型后输出对应骨架。

## 前置检查

- [ ] 用户已明确模型类型和设计变体
- [ ] 用户已提供数据来源和时间范围
- [ ] 用户已了解：输出的是带 `[placeholder]` 的段落，需替换为实际内容

## 输入接口

可直接消费 `/write-theory` 的输出：
- `假设列表` → 用于构建假设-变量映射表
- `核心构念` → 用于变量操作化模板

## 叙事槽位目录（M1–M10）

| 槽位 | 名称 | 输出形式 |
|------|------|----------|
| M1 | 研究情境 / 实证背景 | 1 段填空；JM/ASQ 通常保留，AMJ 约 30% 缺失（被 Introduction 覆盖） |
| M2 | 数据来源与样本漏斗 | 1–2 段填空 |
| M3 | 因变量 | 1 段填空 |
| M4 | 自变量 / 核心预测变量 | 每假设 1 段填空 |
| M5 | 调节/中介/机制变量 | 每变量 1 段填空 |
| M6 | 控制变量与竞争性解释 | 1–2 段填空 |
| M7 | 模型规格与估计方法 | 1–3 段填空（含公式+文字） |
| M7补充 | 调节效应检验选择（differential prediction vs. differential validity） | 1 段填空 + 1 张检验-方法对应表；当 Theory 含调节假设时必填 |
| M8 | 识别策略 / 效度 / 诊断检验 | 1–2 段填空；仅当识别策略是基准估计的一部分时才写（IV/DiD/实验/匹配 强制；OLS/FE 可选）。**不用于预告 Results 的稳健性检验** |
| M9 | 多研究 / 实验程序 / 质性编码 | 多研究时逐研究重复 M1–M8 |
| M10 | Methods 到 Results 的过渡 | 1 段填空；**顶刊中极度罕见（<10%），可省略** |

## 标准顺序与特殊分支

**默认顺序**：M1 → M2 → M3 → M4 → M5 → M6 → M7 → M7补充（如含调节假设）→ M8 → M10

**特殊分支顺序调整**：
- **稀有结果**：M2 先说明抽样策略，再进入变量
- **实证对象构建**：M2 先说明数据构建逻辑
- **自然实验**：M1 中先说明冲击/处理/对照/时点；M8 前置或与 M7 合并
- **多研究**：M9 前置为总览，然后逐研究重复 M1–M8
- **事件历史+事件研究**：M3 分为过程时钟 DV 和市场时钟 DV 两段
- **同时方程**：M1 替换为概念框架→方程系统声明
- **IV/2SLS**：M4 增加工具变量合理性论证；M7 分两阶段说明；M8 增加排他性约束检验
- **动态面板/GMM**：M7 增加系统/差分 GMM 选择逻辑与过度识别检验
- **匹配DiD/广义DiD**：M2 增加匹配前后样本描述；M7 增加匹配估计量选择；M8 增加平行趋势与重叠支撑检验
- **同伴效应/网络效应**：M4 增加网络构念定义与反射性问题处理；M8 增加 falsification 检验
- **文本构念测量**：M3/M4 增加测量构建→效度检验→与人工程度相关性三段式
- **PSM匹配面板**：M2 增加倾向得分匹配步骤与共同支撑域；M7 增加匹配后估计量
- **堆叠扩散Logit**：M7 增加堆叠结构与条件Logit设定
- **多行为者设计**：M2 增加多数据源匹配；M3 区分主/辅行为者结果
- **推断二元结果**：M3 增加从连续/文本信号推断二元状态的逻辑与阈值
- **定性过程研究**：M1 替换为现象正当化+情境选择；M2 替换为多源数据角色说明；M9 替换为编码进阶与可信性机制；不输出 M4–M8（无假设检验模型）。完整填空骨架参见 `write-methods/academic-writing-corpus/定性过程研究.md`。该设计类型目前为 EMERGING / 单来源，F1–F6 Findings 骨架参见 `write-results/academic-writing-corpus/定性过程研究.md`。

---

## 填空段落骨架

### M1. 研究情境 / 实证背景

**通用填空段落**： ⭐ PREMIUM（28/28 篇范文使用，跨所有模型类型复现）

```text
[Empirical setting] provides an appropriate context for examining [theoretical relationship] for three reasons. First, [setting property] makes [mechanism] observable. Second, [scope condition] reduces [confound]. Third, [data feature] allows us to observe [unit/process] over [period]. The unit of analysis is [unit], which aligns with our theorizing about [mechanism].
```

**自然实验/DiD 变体**（替换首句）： ✓ STANDARD（5-8 篇 DiD/自然实验范文复现）
```text
We examine [phenomenon] using [policy/event/institutional change] that altered [exposure/risk/incentive] across [units] and time. [Empirical setting] is well suited because [process] is well documented and [context controls] reduce [confounding concern].
```

**Staggered DiD + 二元结果 变体**（hoffmann2024 型，替换首句）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：自然实验/DiD 变体 + M7 非线性模型变体
```text
We examine [phenomenon] in the context of staggered adoption of [policy/law] across [jurisdictions] over [period]. Because [law] adoption is staggered across [N] [jurisdictions/states] between [start year] and [end year] — affording us both temporal and cross-sectional identifying variation — we use a difference-in-differences design in which [outcome] is regressed on [treatment indicator], [controls], and [fixed effects]. Since [outcome] is binary, we estimate [conditional logit / linear probability model] to assess whether [law] adoption affects the likelihood of [outcome]. The identifying assumption is that [law] adoption in any given [jurisdiction] is orthogonal to changes in [outcome] in the same [jurisdiction], conditional on [controls] and [fixed effects].
```

**实验变体**： ✓ STANDARD（5-6 篇实验范文复现）
```text
We test [theoretical claim] using a [laboratory/field/online] experiment. This design is strongest for assessing [internal validity], although it requires caution in generalizing to [boundary condition].
```

**多研究变体**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：省略
```text
Across [N] studies, we use complementary designs to test [theory] and address [validity concerns]. Study 1 examines [field/archival evidence], Study 2 tests [replication/design upgrade], and Studies [x–y] examine [mechanism/intervention/behavior].
```

**同时方程/SEM 变体**（替换整个 M1）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用填空段落 + M7 同时方程变体
```text
Our conceptual framework links [driver], [mechanisms], [outcome], and [downstream outcome]. We therefore specify a system of [N] equations to capture [direct path], [mediating paths], [downstream path], and [reverse/auxiliary path]. [Empirical setting] provides the data needed to estimate these relationships jointly.
```

**质性→量化混合方法变体**（Haunschild et al. 2015 ORSC 模式）： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：通用 M1 段落
```text
[Empirical setting A] provides an appropriate context for developing theory because [extreme manifestation] makes [underlying mechanism] observable. [Empirical setting B] then provides a complementary context for testing the theory because [phenomenon] occurs with sufficient frequency to enable large-N analysis. Together, these contexts provide a more comprehensive, grounded, and generalized test of new theory than either case study or deductive empirical work alone.
```

---

### M2. 数据来源与样本漏斗

**通用填空段落**：

```text
We began with [starting population] from [source] over [period]. We matched these observations to [additional sources] to obtain [variables]. We excluded [cases] because [comparability/measurement/identification reason]. The final sample consists of [N] [units] observed over [period], with [unit] as the unit of analysis.
```

**稀有结果变体**（在通用段落前插入）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M2 段落 + 脚注说明抽样策略
```text
Because [outcome] is rare, a simple random sample would yield too few [cases] for meaningful analysis; we therefore used [sampling strategy]. The screening criterion increased the likelihood of observing [rare phenomenon], but it did not determine [final outcome measure]. Because [sampling design] affects [representation/effect sizes], we interpret signs and significance but avoid overinterpreting magnitude.
```

**实证对象构建变体**（替换或前置）： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：通用 M2 段落
```text
No authoritative database exists for [empirical object], so we constructed the dataset from [trace/source]. We used [trace/source] because it records [actor claim/action/evaluation] over time. From [raw records], we identified [entities], [events/labels/claims], and [time points]. We then transformed [raw trace] into [analytic variable] by [coding/aggregation rule]. To make the construction auditable, we define each step from [raw input] to [final measure].
```

**自然实验/DiD 变体**： ✓ STANDARD（5-8 篇 DiD 范文复现）
```text
Our primary sample consists of [units] observed from [period], drawn from [source] because it tracks [construct-relevant activity]. The observation window begins in [year] because [source/construct availability] and ends in [year] to capture [post-treatment horizon]. Treatment is observed for [treated units] after [event], while [control units] provide the counterfactual comparison. Because testing [moderation/mechanism] requires [additional source], the sample for H[x] is restricted to [available period/units].
```

**Staggered DiD 样本周期双重辩护变体**（hoffmann2024 型）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：自然实验/DiD 变体
```text
Our primary sample consists of [units] observed from [start year] to [end year]. We choose [start year] for two reasons: first, [data availability / quality reason]; second, this year coincides with [institutional event / regime change] that marks [theoretical relevance]. We end in [end year] to capture a meaningful post-treatment window following the last [law/policy] adoption in [last adoption year], while avoiding contamination from [confounding event: e.g., COVID-19 pandemic].

We exclude [excluded observations] from our sample because they involve [exclusion rationale: e.g., known product defects that already caused injuries/deaths]. This exclusion is theoretically motivated: [theory-based justification — e.g., when harm has already materialized, managers face reputational and legal pressures that override the discretion mechanisms our theory examines]. The final sample consists of [N] [unit-years] across [K] [units].
```

**多研究变体**（逐研究）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M2 段落 + M9 多研究过渡段
```text
Study [x] used [sample source]. Participants/observations were included if [criterion], yielding [analytic sample]. For supplemental analyses, we also use [source] to measure [assumption/mechanism/alternative outcome].
```

**PSM匹配面板变体**（在通用段落中加入匹配步骤）： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：通用 M2 + M8 匹配检验
```text
To reduce selection bias, we first estimate propensity scores using [logit/probit] with [covariates] as predictors of [treatment/status]. We match [treated units] to [control units] using [method: one-to-one nearest-neighbor / kernel / caliper] matching with [calipersize] caliper on [distance metric]. After matching, the standardized bias for all covariates is below [threshold], and the [t-test / KS-test] indicates no significant difference in [covariates] between groups. The matched sample consists of [N] [unit-years / dyads / firms].
```

**层级回退匹配变体**（如 Pfarrer et al. AMJ，1:3 SIC 匹配 + 层级回退）： 🔬 EXPERIMENTAL（2 篇范文：Pfarrer et al., Mayo et al.）⚠️ 保守替代：通用 M2 + PSM 变体
```text
To construct the sample, we first identified [N] [treatment group] firms that [criterion]. We then matched each [treatment group] firm with [ratio: e.g., three] firms from the same [primary matching criterion: e.g., four-digit SIC code] that were similar in [matching variables: e.g., assets, revenues, and ROA]. Where appropriate matches were not found at the [primary level], we looked at [secondary level] and [tertiary level] for similar firms. Through this process we identified [N] matching firms at the [primary level], [N] at the [secondary level], and [N] at the [tertiary level]. A t-test comparing differences in [variable] revealed no significant differences between the [treatment] and [control] companies; however, in keeping with the predictions of prior [construct] research, there were significant differences in [variables]. [Attrition description]. These characteristics suggested our sample provided a [conservative/liberal] test of our hypotheses since they result in some restriction of range to primarily [sample characteristic].
```

**多行为者设计变体**（替换通用段落）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M2 段落 + 说明多数据源匹配
```text
Our data link [actor A], [actor B], and [actor C] through [matching key / dyadic structure]. We began with [starting universe of actor A] from [source A] over [period] and matched these to [actor B observations] from [source B] using [matching rule]. We then linked [actor C characteristics] from [source C]. The final analytic sample consists of [N] [dyads / triads / observations] in which [inclusion condition]. Because [actor B] characteristics are measured at [level], we aggregate [construct] to the [analysis level] using [aggregation rule].
```

**多源嵌套调查变体**（如 Mannor et al. SMJ，多方法数据 + 聚类标准误）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M2 + M7 多层模型/聚类标准误
```text
We used a multisource, multimethod data collection approach to test our ideas. This involved gathering data from [N] sources: [source 1: e.g., in-person interviews], [source 2: e.g., online surveys to subordinates], [source 3: e.g., hard-copy surveys to friends/family], and [source 4: e.g., archival company data]. Testing our theory required gaining access to [phenomenon], and our methodology was designed with this goal in mind. We established [N] criteria to govern recruitment: [criterion 1], [criterion 2], and [criterion 3]. We tested our hypotheses using [estimator: e.g., hierarchical linear regression]. To account for the nonindependence in our data (i.e., [nesting structure]), we specified [SE type: e.g., Huber/White/sandwich standard errors] using the [software option]. [Observations] were clustered by [clustering variable].
```

---

### M2.5. Model-Free Evidence（可选 credibility-building 段落）

**通用填空段落**： ✓ STANDARD（IV/DiD/匹配/自然实验/复杂档案研究中常见）

```text
Before estimating the formal model, we present model-free evidence for the relationship between [predictor] and [outcome]. We split the sample into [high/low] groups based on [criterion: e.g., median / mean of predictor], yielding [N_high] and [N_low] observations. Because [confound] could mechanically produce a difference, we standardize [outcome] by [denominator] before comparing groups. The mean standardized [outcome] is [value] for the [high] group and [value] for the [low] group; a [t-test/Wilcoxon rank-sum test] indicates that the difference is statistically [significant/not significant] ([statistic] = [value], p [relation] [threshold]). This pattern is consistent with [theory], but it does not address [identification threat]; the formal estimates below speak to that concern.
```

> **使用条件**：Model-free evidence 仅作为**描述性可信度铺垫**，不能替代识别策略。若设计本身不涉及复杂识别（纯 OLS/FE 面板），此段落通常多余。

**IV/2SLS 变体**（替换首句和末句）：
```text
Before estimating the instrumental-variable model, we present model-free evidence to show that the raw data exhibit the pattern implied by our theory. We split the sample into [high/low] groups based on [predictor] and compare [standardized outcome] across groups. The descriptive pattern is consistent with [negative/positive association], but it does not establish causality; the IV estimates below address the endogeneity of [predictor].
```

**自然实验/DiD 变体**（替换末句）：
```text
Before estimating the difference-in-differences model, we plot [outcome] over time for [treated] and [control] groups. The raw trajectories appear [parallel] prior to [event], and [diverge/converge] afterward, consistent with [theory]. Formal event-study estimates in the Results section assess whether this visual pattern is statistically reliable.
```

**事件历史变体**（在通用段落中加入过程说明）： 🔬 EXPERIMENTAL（2-3 篇范文：Zhou 2017, Pontikes 2012 等）⚠️ 保守替代：通用 M2 + M3 生存分析变体
```text
[Authority/actor] opens [process] when [trigger]. The process ends when [event occurs] or [case closes/continues]. [Time outcome] is the elapsed time between [start date] and [event date]. Cases without [event] by [end of observation] are treated as [right-censored] because [logic].
```

---

### M3. 因变量

**通用填空段落**：

```text
Our dependent variable is [outcome construct], measured as [operational definition] using [source]. This measure captures [construct] because [construct-validity logic]. Higher values indicate [interpretation direction]. Because [outcome] is [continuous/binary/ordinal/count/censored/time-to-event], we use [model] and interpret [coefficients/marginal effects/hazards/probabilities].
```

**稀有结果/序数变体**（替换末句）： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：通用 M3 段落
```text
Given the skewed distribution of [construct], we treat it as ordered categories that distinguish [low/mid/high states]. Because [outcome] is ordinal, coefficients indicate direction but substantive interpretation requires [marginal effects/predicted probabilities].
```

**事件研究变体**： ✓ STANDARD（3-4 篇事件研究范文复现）
```text
We measure [market/stakeholder reaction] as [CAR/abnormal response] around [event], using [benchmark model] to estimate expected returns. Expected returns are estimated over [estimation window] using [factor model]; abnormal returns are observed returns minus expected returns. We aggregate abnormal returns over [event window] to allow for [information leakage/dissemination].
```

**指数/净指数变体**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M3 段落
```text
Because the theory concerns both [positive actions] and mitigation of [negative actions], we construct [net outcome] from [strengths] and [concerns]. For each [category-year], we divide the number of [items] by the maximum possible number in each [category-year] to account for changes in measurement coverage. The net index subtracts [negative index] from [positive index] and sums across [categories].
```

**行为编码变体（实验）**： 🔬 EXPERIMENTAL（3-4 篇实验范文）⚠️ 保守替代：通用 M3 段落 + 说明编码者间信度
```text
We capture [outcome] behaviorally by [task/coding procedure], reducing reliance on self-reported intentions. Blind coders rated [behavior] on [scale]. We averaged ratings because interrater reliability was [acceptable statistic].
```

**文本构念测量变体**（M3 或 M4 均可使用，三段式效度链）： 🔬 EXPERIMENTAL（3-4 篇范文：Zhao 2022, Gamache 2020 等）⚠️ 保守替代：通用 M3 + 增加效度检验句
```text
Our dependent variable, [text-derived construct], is measured from [text source: earnings calls / press releases / 10-K / media / survey open-ends] using [method: dictionary / LDA / supervised ML / word embeddings]. We first [preprocessing: remove stop words / stem / lemmatize / exclude boilerplate]. We then [measurement step: count semantic similarity / topic proportion / trained classifier probability / cosine distance to anchor]. The measure captures [construct] because [theoretical link between text feature and underlying construct]. To validate the measure, we correlate it with [external benchmark: human-coded sample / established scale / related archival measure]; the correlation is [value] (p [relation] [threshold]). We also inspect [example excerpts] to confirm face validity. Higher values indicate [interpretation direction].
```

**LIWC 心理语言学构念测量变体**（如 Mannor et al. SMJ，Pfarrer et al. AMJ）： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：通用 M3 段落 + 增加字典说明
```text
We used a [method: e.g., psycholinguistic] approach aimed at measuring [construct] based on the language [participants/actors] used during [data collection context]. [Software] contains established dictionaries of words that have been validated by [citation] to reflect underlying [psychological phenomenon]. For example, [prior study] used [software] to measure [prior construct]. We followed a similar approach in constructing our measures for [construct components]. [Component 1] was captured by assessing [language feature: e.g., use of positive emotion language and words associated with achievement]. The [dictionary] included [N] words (such as [examples]) whose average coefficient alpha was [value]. [Component 2] was measured by assessing [language feature: e.g., use of negative affective language and words associated with inhibition]. This component was calculated as the [relative percentage / raw count] of words contained in the [dictionary]. Next, we standardized the [component scores]. We then used these standardized scores to create a [net / composite] [construct] score, which was calculated as [formula].
```

**人工内容分析 + 编码者间信度变体**（如 Desai AMJ，Pfarrer et al. AMJ）： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：通用 M3 段落 + 编码者间信度说明
```text
To develop the [variable], we collected [document type] from [source]. Searches were conducted on [databases] for [keywords / search terms]. [Relevance criterion] yielded [N] unique [documents]. [Construct] falls into [N] categories: [category 1: definition and example], [category 2: definition and example], and [category 3: definition and example]. I read and coded all [documents], and a colleague used the same coding scheme on [percentage]% of them, selected randomly. The two raters agreed on [N] of the codings, a level of agreement resulting in a Cohen's kappa of [value], suggesting [interpretation: e.g., high intercoder reliability]. The [variable] equals [operationalization: e.g., a count of the documents meeting any of the above criteria].
```

**推断二元结果变体**：
```text
Our dependent variable is [binary outcome construct]. Because [direct observation is unavailable / the construct is latent], we infer [binary state] from [observable signal: text / count threshold / categorical mapping]. We classify a [unit] as [state = 1] when [rule: keyword presence / count exceeds threshold / human-coded indicator / classifier probability > cutoff]. We set the threshold at [value] because [justification: distribution elbow / domain convention / validation against human coding]. To assess classification accuracy, we [validation procedure: manual audit of random sample / compare to gold-standard subsample / report precision-recall]. The inferred [binary state] aligns with [external indicator] for [percentage] of cases.
```

**多行为者因变量变体**：
```text
We measure [outcome] at the [actor B] level because [theoretical reason: actor B is the decision maker / actor B bears the consequence]. The dependent variable is [operational definition] from [source B]. For robustness, we also construct an alternative measure from [source C] using [alternative rule]. The correlation between the two measures is [value], indicating [acceptable / strong] convergent validity.
```

**测量防御三段式变体**（Pontikes 2012 模式：承认局限 → 论证最优可用 → 保守检验逻辑）： ✓ STANDARD

```text
We acknowledge that our measure of [construct] has limitations. [Specific limitation 1: e.g., the measure relies on observable classification claims rather than direct perceptual data]. [Specific limitation 2 if applicable: e.g., the measure captures only one dimension of a multi-dimensional construct]. These limitations stem from [inherent data constraint: e.g., the lack of fine-grained perceptual surveys for the full population over the study period].

Despite these limitations, this measure is the best available operationalization for three reasons. First, [reason 1: construct coverage — the measure captures the core theoretical mechanism because...]. Second, [reason 2: empirical precedent — similar approaches have been used in...]. Third, [reason 3: scope — the measure is available for the full population, avoiding selection issues that would arise from survey-based alternatives].

Importantly, the limitations of this measure bias against finding the hypothesized results. [Conservative test logic: e.g., measurement error in the independent variable attenuates coefficients toward zero / if anything, our measure undercounts the phenomenon, making significant findings harder to obtain]. Finding [significant results / the predicted pattern] despite this conservative bias strengthens confidence in the underlying relationship.
```

> **测量防御 QC**:
> - 三段结构必须完整：承认局限 → 论证最优可用 → 保守检验逻辑
> - 局限必须诚实（不能只说 "future research should improve"），且必须解释为什么在此局限下测量仍有效
> - 保守检验逻辑必须有方向性：为什么局限让显著结果更难（而非更容易）获得？
> - 如果局限可能让结果更容易显著，不能使用此变体——应改用通用 M3 + 诚实标注局限

**替代测量效度三角变体**（Haunschild et al. 2015 ORSC 模式）： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：通用 M3 段落
```text
To measure [construct], we used [primary operationalization] because [theoretical justification]. [Specific mechanism]. As an alternative measure of [construct], we used [alternative operationalization] because [additional theoretical justification]. This alternative is instructive because [why it differs from primary measure and what it adds]. Because [alternative measure] relies on a different [data source / institutional process] than [primary measure], finding consistent results across the two measures increases confidence that our findings reflect [construct] rather than [idiosyncrasy of primary measure].
```

---

### M4. 自变量 / 核心预测变量

**通用填空段落（每预测变量一段）**：

```text
Our focal independent variable, [predictor name], is measured as [operation] based on [source/timing]. This variable corresponds to Hypothesis [x] because it captures [mechanism]. We present the focal variables in the order of the theory: [predictor A], [predictor B], and [moderator].
```

**自然实验/处理变量变体**：
```text
The treatment indicator equals one for [unit-years/participants] exposed to [event/condition] and zero otherwise. [Treatment] equals 1 for [unit-years] after [policy/event] becomes effective in [jurisdiction/group], and 0 otherwise.
```

**处理分配稳定性补充**（DiD 可选）： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：省略此段
```text
During our sample period, [percentage] of [units] changed their [treatment-relevant characteristic, e.g., headquarters location]. We use [historical/fixed] [characteristic] information to maintain consistent treatment assignment.
```

**竞争机制预测变量变体**（机制测试中分解核心构念时）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M4 段落
```text
To test how [actors] resolve [uncertainty], we decompose [core construct] into [N] subgroups based on [criterion]: [variable 1], [variable 2], [variable 3], and [variable 4]. We restrict the mechanism test subsample to [criteria] to ensure sufficient variation across the subgroups. These variables correspond to [RQ/Prediction x] because they distinguish [mechanism A] versus [mechanism B].
```

**实验操纵变体**：
```text
To manipulate [construct], participants were shown/told [condition-specific cue], while [other information] was held constant.
```

**网络/组合/配对构念变体**：
```text
We define [focal construct] as occurring when [actor] simultaneously holds/links/participates in [two or more related units]. The pair-level measure captures [shared influence/exposure] between the focal unit and each same-category peer. The numerator sums [shared holdings/links/exposure]; the denominator adds [non-focal holdings/relationships] so the measure reflects [focal actor influence] relative to [other actors]. We aggregate the pair-level measure across all same-category peers to form a continuous focal-unit measure. We require [minimum stake/link/intensity] so that the focal actor has sufficient incentive and ability to influence [unit].
```

**同伴效应/网络效应变体**：
```text
Our focal independent variable, [network-based construct], is defined using [network boundary: same industry / same board / same supply chain / geographic proximity]. We calculate [focal exposure] as the [average / weighted average] of [peer outcome/characteristic] among [peers], excluding the focal unit. Formally, [network variable]_{i,t} = Σ_{j≠i} [weight]_{ij,t} × [peer characteristic]_{j,t} / Σ_{j≠i} [weight]_{ij,t}. Because peer outcomes may reflect common shocks rather than true influence, we instrument [network variable] with [instrument: lagged peer characteristic / network from different layer / exogenous network formation] and report falsification tests in M8.
```

**构造暴露/指数变体**（用于堆叠扩散或媒体暴露）：
```text
We construct [focal exposure] from [raw trace] by [aggregation rule]. The measure equals [formula: count / proportion / intensity] of [event/type] per [unit-time]. To account for [scale differences / coverage variation], we normalize by [denominator]. We require [minimum threshold] to ensure that [spurious zeros / noise] do not drive the results.
```

**文本构念预测变量变体**（当预测变量来自文本分析，如 earnings calls、10-K、媒体、访谈时）：
```text
Our focal independent variable, [predictor name], is derived from [text source, e.g., earnings call transcripts / 10-K filings / media coverage] using [method: LIWC dictionary / custom dictionary / machine-learning classifier]. We chose this source because [theoretical reason for text reflecting construct]. The dictionary includes [N] words/phrases capturing [theoretical dimension], validated by [human coding / prior literature / expert review]. To ensure convergent validity, we correlate the text-based measure with [alternative measure, e.g., survey / archival proxy]; the correlation is [value] (p [relation] [threshold]), supporting construct validity. We standardize the text score to mean zero and standard deviation one to facilitate coefficient interpretation. Because text-based measures may capture noise unrelated to [construct], we control for [general text characteristics: length / sentiment / formality] in all specifications.
```

**同时方程变体**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M7 段落
```text
Equation [x] predicts [primary outcome] as a function of [focal predictor], [mechanisms], [moderators], interactions, and controls. Equations [y–z] model [mediator A] and [mediator B], allowing us to test whether [focal predictor] affects the mechanisms implied by the theory. Equation [w] predicts [downstream outcome] using [focal outcome], [focal predictor], their interaction, and value-relevant controls. We include an additional equation for [potentially endogenous choice] to account for the possibility that [anticipated need/reverse path] influences [focal predictor].
```

---

### M5. 调节变量 / 中介变量 / 机制变量

**通用填空段落（每变量一段）**：

```text
To capture [boundary/mechanism], we measure [moderator/mediator] as [operation]. We interact [predictor] with [moderator] to test whether [relationship] is stronger/weaker under [condition]. To test the proposed mechanism, we measured [mediator] and included [alternative mechanisms] as rival explanations.
```

**子样本分割变体**（用样本分割而非交互项检验调节时）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M5 段落
```text
To capture the boundary condition of [moderator], we measure [moderator] using [classification]. We split the sample by [moderator] into [category A] and [category B] to test whether [relationship] differs across [categories], rather than including an interaction term, because [reason: small sample within categories / theoretical focus on distinct regimes].
```

**行为者类型分解变体**：
```text
To test the proposed mechanism, we decompose [predictor] by [actor type/horizon]. [Type A] and [Type B] capture actors expected to have [theory-relevant orientation], whereas [Type C] captures a comparison group. We map [classification data] onto [focal source] and construct separate measures for [type A], [type B], and [type C].
```

**边界条件验证变体**：
```text
We define [boundary condition] as contexts where [spillovers/externalities/stakeholder responses] are likely to be economically meaningful. We validate this classification using [external source A] for [dimension A] and [external source B] for [dimension B].
```

**间接调节（ mediated moderation ）变体**： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：通用 M5 段落
```text
To test the indirect moderation model, we specify a system of equations. Equation (2) captures the moderating effect of [moderator 1] on the [predictor-outcome] relationship: [outcome] = β₁₀ + β₁₁[predictor] + β₁₂[moderator 1] + β₁₃[predictor × moderator 1] + ε₁. Equation (3) captures the moderating effect of [moderator 2]: [outcome] = β₂₀ + β₂₁[predictor] + β₂₂[moderator 2] + β₂₃[predictor × moderator 2] + ε₂. Equation (4) models the relationship between [moderator 1] and [mediator]: [mediator] = β₃₀ + β₃₁[moderator 1] + ε₃. Equation (5) represents the full system with both moderators: [outcome] = β₄₀ + β₄₁[predictor] + β₄₂[moderator 1] + β₄₃[predictor × moderator 1] + β₄₄[mediator] + β₄₅[predictor × mediator] + ε₄.

We test for full indirect moderation through [mediator] according to whether: (1) [moderator 1] functions as a moderator when [mediator] is not considered (β₁₃ ≠ 0); (2) [moderator 1] influences [mediator] (β₃₁ ≠ 0); (3) [mediator] moderates the effect of [predictor] on [outcome] (β₄₅ ≠ 0); and (4) the coefficient on the original interaction term in the full system (β₄₃) indicates the pattern of mediation—β₄₃ = 0 indicates full indirect moderation (the direct moderating effect of [moderator 1] becomes nonsignificant in the presence of [mediator]), whereas β₄₃ ≠ 0 and |β₄₃| < |β₁₃| indicates partial indirect moderation.
```

**自主构念测量理论锚定变体**（Pontikes 2012 模式：无现成 validated scale，从理论定义直接操作化）： ✓ STANDARD

```text
No pre-validated scale exists for [construct], so we develop a measure directly from its theoretical definition. [Construct] is defined as [theoretical definition with citation]. This definition implies [observable feature 1] and [observable feature 2]. We operationalize these features as follows.

[Measure name] captures [theoretical dimension 1] by [operational rule: e.g., whether a market label has a clear, agreed-upon definition]. We determine this by [empirical procedure: e.g., coding whether industry publications provide consistent category definitions]. [Alternative measure name] captures [theoretical dimension 2] by [operational rule: e.g., the number of market labels an organization simultaneously claims]. Both measures are continuous, with higher values indicating greater [construct].

To assess whether these measures capture distinct dimensions of [construct] rather than a single underlying factor, we examine their correlation. The correlation between [measure A] and [measure B] is [value], indicating that [they are empirically distinguishable / they share common variance but are not redundant]. This is consistent with the theoretical distinction between [dimension 1] (a property of the [unit A: e.g., category]) and [dimension 2] (a property of the [unit B: e.g., organization]).

Although these measures are novel, their construction follows directly from the theoretical definition of [construct] and is anchored in [prior theoretical work / qualitative observation / institutional features of the empirical context]. We validate the measures through [face validity check: e.g., inspection of extreme cases / correlation with known correlates / expert review]. In supplemental analyses, we also test [alternative operationalization] and find [consistency / qualification].
```

> **自主构念测量 QC**:
> - 理论定义必须在操作化之前明确给出（citation-anchored）
> - 每个测量维度必须有对应的可观测特征和操作化规则
> - 多维度测量必须报告维度间相关性，论证它们是 distinguishable 而非 redundant
> - 必须有一个 validation check（face validity / convergent / discriminant / known-group），不能只有理论论证
> - 如果存在相近的现有测量，说明为什么不使用它（覆盖面不足 / 样本不适用 / 理论维度不匹配）

---

### M6. 控制变量与竞争性解释

**通用填空段落**：

```text
We include controls for [threat family 1] because [alternative explanation 1]. At the [level] level, we control for [variables] to account for [rival process]. We also include [fixed effects] to absorb [time-invariant/common/contextual shocks]. All time-varying predictors are measured at [lag/timing] to preserve temporal ordering. We lag the control variables by [period] to reduce simultaneity concerns.
```

**自然实验/Bad Control 变体**： ✓ STANDARD（5-8 篇自然实验/DiD 范文复现）
```text
Because some controls may be affected by [treatment], we first estimate a parsimonious model with fixed effects before adding controls. We do not include [variable] because it may be post-treatment / mechanically related to [outcome].
```

**同时方程/方程特定控制变体**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M6 段落
```text
For [equation/outcome family], we include controls that address [rival explanation]. For [mediator equation], we further control for [industry benchmark] because firms may align [decision] with industry norms. In the [downstream outcome] equation, we control for [profitability], [growth], and [market position] because each may independently affect [value outcome]. In the [financial choice] equation, we include known determinants such as [industry norm], [asset structure], [firm size], and [profitability].
```

**实验变体**：
```text
We control for [participant characteristics] because [rival explanation]. Random assignment allows us to isolate the effect of [manipulation] on [outcome] within the experimental context.
```

**竞争焦点互控变体**（Haunschild et al. 2015 ORSC 模式）： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：通用 M6 段落
```text
The analysis controls for potential sources of heterogeneity across observations that might influence both the independent and dependent variables. In models estimating [DV1], we controlled for [DV2]; conversely, in models estimating [DV2], we controlled for [DV1]. This allows us to examine whether [focal IV] influences [DV1] and [DV2] net of each other, rather than merely reflecting [alternative explanation: e.g., a common third variable driving both foci]. To ensure that findings were not driven by collinearity involving the respective variables, we also ran models dropping the alternative focus from the equation.
```

---

### M7. 模型规格与估计方法

**通用填空段落**：

```text
Because [dependent variable] is [continuous/binary/ordinal/count/censored/time-to-event], we estimate [model]. The specification includes [fixed effects] to absorb [unobserved heterogeneity/common shocks]. Standard errors are clustered at [level] to account for [within-unit dependence]. We use [estimator] for [hypotheses] because [outcome/design logic]. We also considered [alternative estimator]; results using this approach are reported as [robustness/supplement].
```

**模型选择理由补充段**（按需添加）： ✓ STANDARD（15+/28 篇范文使用）
```text
We employ [unit] fixed effects rather than random effects because the Hausman test rejects the random-effects assumption (χ² = [value], p < 0.01), indicating that unobserved [unit]-specific factors are correlated with our independent variables. [Year] fixed effects control for temporal trends such as [macroeconomic shocks/industry-wide shifts].
```

**诊断检验补充段**：
```text
We conduct several diagnostic tests. First, the Variance Inflation Factor (VIF) for all independent variables is below [value], well below the conventional threshold of 10, indicating that multicollinearity is not a concern. Second, the [Wooldridge/modified Wald] test indicates [presence/absence] of [autocorrelation/heteroskedasticity], and we report [robust/clustered] standard errors accordingly.
```

**非线性模型变体**： ✓ STANDARD（8-10 篇非线性模型范文复现）
```text
Because [outcome] is [binary/ordinal/count/censored/time-to-event], we estimate [model]. Coefficients indicate direction, but substantive interpretation requires [marginal effects/predicted probabilities/hazard ratios/odds ratios]. We assess [assumption] using [diagnostic/test], discussed below.
```

**计数模型负二项变体**（Haunschild et al. 2015 ORSC 模式）： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：非线性模型变体
```text
Both dependent variables, [DV1] and [DV2], are count variables, which violate the assumption of homoskedastic, normally distributed error terms. Although [Poisson] models can be used to estimate influences on count variables, they can produce underestimated standard errors and spuriously high significance levels when the assumption of equality between the mean and the variance is violated. As a result, our analysis adopts a [negative binomial] specification. Models account for [random effects across firms] to capture [time-invariant unobserved heterogeneity]. All independent and control variables are lagged by [one period] to ensure temporal precedence.
```

**DiD 变体**：
```text
We estimate a difference-in-differences model in which [outcome] is regressed on [treatment], [moderator/interactions], controls, and fixed effects. Identification comes from comparing changes in [treated units] before and after [event] to contemporaneous changes among [control units]. We cluster standard errors at [unit/jurisdiction] to account for serial correlation and within-[cluster] dependence.
```

**DiD 方程编号与 SE 聚类引用补充**：
```text
We cluster standard errors at the [level] to address [dependence structure] ([citation, e.g., Bertrand et al. 2004; Jager et al. 2021]). Where relevant, we present numbered equations: Equation (1) reports the baseline DiD specification, and Equation (2) reports the event-study leads-and-lags specification.
```

**Staggered DiD + 条件 Logit 变体**（hoffmann2024 型，二元结果 + 交错处理时点）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：DiD 变体 + 非线性模型变体
```text
Because our dependent variable [outcome] is binary and [treatment] adoption is staggered across [jurisdictions] over time, we estimate a conditional (fixed-effects) logit model. The conditional logit specification accounts for [unit]-invariant unobserved heterogeneity through [unit] fixed effects, while the staggered adoption structure provides identifying variation through two channels: (1) within-[unit] before-after comparisons (units switching from non-adoption to adoption) and (2) cross-[unit] comparisons at each point in time (adopting vs. not-yet-adopting units). The estimated equation is:

[Outcome]_{it} = α_i + β[Treat]_{it} + γ[X]_{it} + δ_t + ε_{it}

where [Treat]_{it} equals one after [jurisdiction] i adopts [law/policy] in year t, and zero otherwise; α_i are [unit] fixed effects; [X]_{it} is a vector of time-varying controls; and δ_t are year fixed effects. Because [outcome] is binary, we use conditional logit rather than linear probability model as our primary specification. Standard errors are clustered at the [jurisdiction/unit] level to account for serial correlation and within-[cluster] dependence ([Bertrand et al. 2004]). We report odds ratios for economic interpretation, supplemented by predicted probabilities at key values of [treatment] and [moderators] to aid substantive interpretation.

Four features of this estimation strategy merit discussion. First, we cannot include [unit] fixed effects in a standard linear probability model estimated via OLS with a large number of [units] and a rare binary outcome — this would create an incidental parameters problem. Conditional logit addresses this through the fixed-effects estimator. Second, a consequence of this specification choice is that [time-invariant predictors: e.g., industry dummies, state-level characteristics] cannot be included because they are absorbed by the [unit] fixed effects. Where such variables are theoretically relevant (e.g., for moderation analyses), we interact them with [treatment] rather than including them as main effects. Third, we lag all time-varying predictors by [one period/year] to preserve temporal ordering and reduce simultaneity concerns. Fourth, we conduct a comprehensive set of sensitivity analyses — including [alternative estimators: LPM with FE, random-effects logit], [alternative samples: balanced panel, excluding early/late adopters], and [placebo tests: pseudo-adoption dates, pre-treatment leads] — to assess the robustness of our findings.
```

**Staggered DiD + 条件 Logit 的 6 个关键范式**（hoffmann2024 蒸馏）：

| # | 范式 | 功能 | 方法防御 |
|---|------|------|---------|
| 1 | **样本周期双重辩护** | 建立样本窗口的理论+制度合理性 | start year: 数据可用性 + 制度事件双重理由；end year: 最后 adoption + N 年 post-treatment + 排除 confound |
| 2 | **样本排除理论化** | 将样本限制与理论机制对齐 | 排除"伤害已发生的召回"→ 理论关心的是管理者有裁量权的召回决策 |
| 3 | **条件 Logit 选择辩护** | 解释为什么不能用 OLS FE | 二元 DV + 大量固定效应 → incidental parameters problem → 条件 Logit 的 FE estimator 解决 |
| 4 | **时不变变量处理** | 解释为什么某些变量不能出现 | "absorbed by FE" → 交互项而非主效应 → 但限于调节分析 |
| 5 | **固定效应局限诚实说明** | 承认方法局限而非隐藏 | "cannot include firm FE because of incidental parameters problem; firm controls proxy for some of this variation" |
| 6 | **滞后与敏感性预注册** | 在 Methods 中预承诺稳健性分析范围 | 滞后所有 time-varying predictors + 列出全部 sensitivity checks（非在 Results 中 cherry-pick）

**生存分析变体**： 🔬 EXPERIMENTAL（2-3 篇范文：Zhou 2017, Pontikes 2012 等）⚠️ 保守替代：通用 M7 段落 + 说明分布选择
```text
Because the shape of [event timing] is not known ex ante, we compare [candidate distributions] and select [distribution] based on [fit criterion]. We use an accelerated failure time metric so coefficients can be interpreted in terms of [longer/shorter] time to [event].
```

**复发事件 AFT 变体**（当同一主体经历多次事件时）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M7 + 生存分析变体
```text
Because [units] experience multiple [events] over the observation period, we estimate recurrent-event accelerated failure time (AFT) models with a [distribution] distribution for the underlying failure rate. Recurrent-event AFT models are appropriate because they examine how [predictors] influence the time to [event] while accounting for repeated occurrences within the same [unit]. We report robust standard errors to account for within-[unit] dependence across multiple events. The specification includes [fixed effects] to absorb unobserved heterogeneity.
```

**复发事件风险模型变体**（Recurrent-Event Hazard，如 Mayo et al. POMS）
```text
Because our objective was to examine how [IV] is associated with the hazard of a future [event], we use a hazard model. Hazard models estimate the hazard rate of an event occurring based upon independent variables that change across time, using time-to-event as the dependent variable. We measure time as [operationalization: e.g., elapsed days from the first observed data point]. We treat [event A] as failures (failure measure = 1) and [event B] as non-failures (failure measure = 0). Because many [units] in our sample experience more than one [event] (in our data, [N] average [events] per [unit]), we use a recurrent-event hazard model with clustered standard errors at the [cluster level]. We assume a [distribution: e.g., exponential] for the underlying hazard rate as it assumes that failures are [property: e.g., memoryless] after controlling for explanatory variables, making it one of the more parsimonious distributions in parametric hazard modeling. However, to ensure that this modeling choice is not the underlying reason for our results, we demonstrate that results are robust to [alternative distributions: e.g., Weibull and Gompertz].
```

**复发事件时间测量策略补充段**（当需要论证 continuous vs. reset time 时）：
```text
There are two main ways to handle the time measure in a recurrent-event hazard model. One way is to allow the time measure to continue to grow after each event for a given firm; that is, time to an event is always measured since the beginning of the data for a given firm. The other approach is to reset the time to zero after each failure for a given firm; that is, time is measured since the last failure. We chose the former method because longer panels like ours tend to have a large number of failures within a firm and may therefore be better suited toward a continuously incremented time measure due to shared variance that develops within a firm with multiple failures.
```

**同时方程变体**：
```text
Joint estimation addresses simultaneity and accounts for correlated errors across equations. We check [order/rank] conditions to ensure that each equation is identified. We further assess whether [alternative endogenous specification] is necessary by estimating [IV/3SLS] and comparing it with [preferred estimator] using [diagnostic test].
```

**IV/2SLS 变体**： ✓ STANDARD（3-4 篇 IV 范文复现）
```text
Although [baseline estimator] can exploit [within/between] variation, it may still be biased if [predictor] is endogenous due to [omitted variable / reverse causality / measurement error]. We therefore use two-stage least squares (2SLS) with [instrument] as an instrument for [endogenous predictor]. [Instrument] satisfies the relevance condition because [first-stage F-statistic / theoretical reason for correlation with endogenous predictor]. It satisfies the exclusion restriction because [theoretical argument for why instrument affects outcome only through predictor]. In the first stage, [endogenous predictor] is regressed on [instrument], [exogenous controls], and [fixed effects]. The first-stage F-statistic is [value], exceeding the Stock-Yogo threshold, indicating that [instrument] is not weak. In the second stage, [outcome] is regressed on the predicted [endogenous predictor] and the same controls. Standard errors are [robust / clustered] to account for [error structure].
```

**策略性内生性变体**（当核心解释变量是行动者主动选择时）： ✓ STANDARD（IV/控制函数/自然实验范文通用）
```text
Although [baseline estimator] can exploit [within/between] variation, it may still yield biased estimates because [predictor] reflects a strategic choice. [Actors] may adjust [predictor] in anticipation of [future outcome / regulatory risk / competitive pressure], and unobserved factors underlying this strategic orientation are likely correlated with both [predictor] and [outcome]. Fixed effects remove time-invariant heterogeneity, but they do not address time-varying omitted variables that drive both the choice of [predictor] and the realization of [outcome]. We therefore use [2SLS / control function / natural experiment] to isolate variation in [predictor] that is plausibly unrelated to these unobserved strategic considerations.
```

**IV/2SLS 多结果对称变体**（同 IV，多个相关 second-stage 结果）： ✓ STANDARD（双结果/利益相关者反应研究常见）
```text
We use a single first-stage equation to isolate exogenous variation in [endogenous predictor], but we estimate separate second-stage equations for [outcome A] and [outcome B] because the two outcomes are generated by [different actors / different decision processes]. The first-stage specification is identical across equations: [endogenous predictor] is regressed on [instrument], [common controls], and [fixed effects]. The second-stage equations differ only in the outcome and in the covariates most relevant to each decision process. For [outcome A], we include [covariate set A] to capture [process A determinants]; for [outcome B], we include [covariate set B] to capture [process B determinants]. This structure allows us to test whether the same identifying variation produces [parallel / divergent] effects across outcome streams.
```

**计数 DV 的 linear IV 选择说明**（count outcome + 2SLS 时）：
```text
Because [outcome] is a count with a skewed distribution, one might consider Poisson or negative binomial IV. However, when the research question focuses on the [average marginal effect / mean change in count] and the instrument is strong, a linear 2SLS specification provides a consistent estimate of the local average treatment effect and yields coefficients that are directly interpretable. We therefore report linear 2SLS as the primary specification and use [Poisson IV / negative-binomial IV / ordered probit] as a robustness check to ensure that the distributional form does not drive the results.
```

**线性概率模型（LPM）+ 2SLS 变体**（二元 DV 且需固定效应时）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：IV/2SLS 变体
```text
Because the dependent variable is binary, one might consider Logit or Probit. However, when using 2SLS with fixed effects, the linear probability model (LPM) is often preferred because coefficients are directly interpretable as probability changes and computational tractability is preserved. We therefore estimate LPM with 2SLS for the main analyses and report Probit/Logit IV only as robustness. The specification includes [fixed effects] to absorb [unobserved heterogeneity]. Standard errors are clustered at the [level] to account for [dependence structure].
```

**事件研究 GLM 变体**（CAR 为 DV 时）：
```text
Because [CAR/abnormal response] is continuous but subject to nonconstant error variance, we estimate generalized linear models (GLM) rather than ordinary least squares. GLMs are robust to nonconstant error variance and relaxed distributional assumptions. Expected returns are estimated over [estimation window] using [factor model]; abnormal returns are observed returns minus expected returns. We aggregate abnormal returns over [event window] to allow for [information leakage/dissemination].
```

**动态面板/GMM 变体**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M7 段落 + M8 Nickell bias 提示
```text
Because [dependent variable] is persistent and our panel is [short / has few time periods], fixed-effects estimation may be biased (Nickell bias). We therefore estimate a dynamic panel model using [system GMM / difference GMM] with [lag structure] as instruments. We collapse the instrument matrix to avoid instrument proliferation and report [Hansen J-test / Sargan test] for overidentification ([value], p = [value]) and the [AR(2)] test for second-order serial correlation ([value], p = [value]). We treat [lags] as predetermined and [further lags] as instruments. The number of instruments is [N], which is [less than / approximately equal to] the number of groups, satisfying the rule of thumb that instruments should not exceed groups.
```

**匹配DiD/广义DiD 变体**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：DiD 变体 + M2 PSM 变体
```text
We estimate a generalized difference-in-differences model using [matching estimator: nearest-neighbor / kernel / inverse probability weighting] to construct a credible counterfactual. Matching is performed on [covariates] using [propensity score / Mahalanobis distance] within [strata / caliper]. After matching, we estimate [outcome] on [treatment], [time], [treatment × time], controls, and [fixed effects] using the matched sample. Identification comes from comparing [treated units] to [matched control units] before and after [event]. We cluster standard errors at [level] to account for [dependence structure].
```

**堆叠扩散Logit 变体**： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：通用 M7 段落
```text
Because [outcome] is a binary adoption decision observed across multiple [entities / markets / practices] and time, we estimate a conditional (fixed-effects) logit model in a stacked structure. Each stack corresponds to [entity-practice-time triplet / adoption event], and the dependent variable equals one if [adoption occurred]. The stacked structure accounts for [unobserved heterogeneity] by including [fixed effects: entity / practice / time] while allowing [predictors] to vary across [dimensions]. We cluster standard errors at [entity] level to account for repeated observations within [entity].
```

**PSM匹配面板 + 随机效应Tobit 变体**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：M7 Tobit + M2 PSM
```text
After propensity-score matching (described in M2), we estimate the treatment effect using [random-effects Tobit / fractional logit / GEE] because [outcome] is [censored / fractional / non-normal] and matching does not fully eliminate [unobserved heterogeneity]. We include [random effects] to account for [unit-level unobservables] and [time fixed effects] to absorb [common shocks]. Standard errors are clustered at [level].
```

**组合设计注释（Tobit/Poisson/Logit + IV）**：
当模型同时涉及非线性 DV 和工具变量时（如 Zhou 2017 ASQ），建议按以下顺序拼接：
1. 先报告 estimator-DV 匹配逻辑（Tobit 处理 censored / Poisson 处理 count）；
2. 再报告 IV 必要性与工具变量合理性；
3. 最后说明 second-stage 的解释策略（marginal effects / turning points / count effects）。
first-stage 统计量可置于 M7 正文、表格脚注或 R1 诊断段，取决于识别策略在论文中的核心程度。若 first-stage 仅作为诊断而非展示重点（如 ASQ 常见做法），建议在 M7 中仅简要提及"first-stage F 超过 Stock-Yogo 阈值"，将具体数值放入表格脚注。

**混合效应（within-between 分解）变体**：
```text
To disentangle the within-[unit] and between-[unit] effects of [predictor], we estimate mixed-effects models that decompose [predictor] into two components: [predictor]_{within}, which captures deviations from each [unit]'s mean over time, and [predictor]_{between}, which captures each [unit]'s time-invariant average. The within-effect answers whether [predictor] changes within the same [unit] are associated with [outcome] changes. The between-effect answers whether [units] with higher average [predictor] exhibit systematically different [outcome]. We include [random effects] to account for [unit]-level unobserved heterogeneity and [fixed effects] to absorb [time/common shocks].
```

**HLM/多层模型变体**（当数据为嵌套结构，如员工-团队-公司，或重复测量-个体时）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M7 段落 + 说明聚类标准误
```text
Because observations are nested within [level-2 unit, e.g., firms / teams / individuals], we estimate a hierarchical linear model (HLM) with random intercepts at the [level-2] level. The intraclass correlation (ICC) is [value], indicating that [percentage]% of the variance in [outcome] resides between [level-2 units], justifying the use of multilevel modeling. We include [predictor] at [level-1 / level-2 / both levels] and test cross-level interactions (e.g., [level-2 predictor] × [level-1 predictor]). Random slopes for [predictor] are included when the likelihood-ratio test favors their inclusion (χ² = [value], p [relation] [threshold]). We center [level-1 predictor] at the [group mean / grand mean] to facilitate interpretation of [main effects / cross-level interactions]. Standard errors are robust to [heteroskedasticity / clustering] at the [level] level.
```

**实验变体**：
```text
Participants were randomly assigned to one of [N] conditions and then completed [task/measures]. We used [model/test] to analyze [outcome] because [outcome form/design logic].
```

---

### M7 补充：调节效应检验选择（differential prediction vs. differential validity）

**上游接口**：本段承接 `/write-theory` 的假设形式决策矩阵。Theory 部分应已明确每个调节假设是 **differential prediction**（Z 改变 X→Y 的 slope/nature）还是 **differential validity**（Z 改变 X→Y 的 strength/correlation）。Methods 的任务是选择与之匹配的检验。

**检验-方法对应表**：

| Theory 概念类型 | 假设语言信号 | 推荐检验 | 解释对象 | 报告位置 |
|---|---|---|---|---|
| Differential prediction（同层，连续 Z） | "effect... is stronger/weaker/changes" | Moderated multiple regression：Y ~ X + Z + X×Z | 交互项系数（slope 变化） | M7 主模型 |
| Differential prediction（类别 Z） | "X relates to Y for A but not B" | 分组 OLS/FE/Logit，或 MMR 加 X×D_Z | 组间系数差异 | M7 主模型 |
| Differential validity（连续/类别 Z） | "correlation/strength... is greater/lesser" | Subgroup correlation comparison；Fisher z 转换后比较 | 组间相关系数差异 | M7 或 M8 |
| Cross-level differential prediction | "higher-level Z changes lower-level X→Y slope" | HLM / multilevel model with cross-level interaction | 跨层交互项系数 | M7 主模型 |
| Cross-level differential validity | "strength of lower-level X–Y correlation varies by higher-level Z" | Multigroup SEM 或 level-2 分组相关比较 | 跨层相关强度差异 | M7/M8 |

**differential prediction 填空段落**：
```text
Because H[X] predicts that [Z] changes the slope of the [X]→[Y] relationship (differential prediction), we estimate [model: e.g., OLS/FE/Logit] with the interaction term [X × Z]. A significant coefficient on [X × Z] indicates that the effect of [X] on [Y] differs across levels of [Z]. We interpret the interaction using [simple slopes / marginal effects at ±1 SD of Z / predicted values at low and high Z].
```

**differential validity 填空段落**：
```text
Because H[X] predicts that [Z] changes the strength of the [X]–[Y] correlation rather than its slope (differential validity), we follow Andersson, Cuervo-Cazurra, and Nielsen (2014) and split the sample by [Z]. We estimate the [X]–[Y] correlation separately for [group A] and [group B] and compare the coefficients using [Fisher z-test / χ² test for equality of correlations]. A significant difference in correlation strength supports H[X].
```

**跨层调节填空段落**：
```text
Because [Z] operates at the [level-2] level while [X] and [Y] are measured at the [level-1] level, we estimate a hierarchical linear model with a cross-level interaction [level-1 X × level-2 Z]. This specification allows the slope of [X]→[Y] to vary across [level-2 units] and tests whether [Z] explains part of that slope variance.
```

**QC 检查点**：
- [ ] Theory 假设中是否明确是 differential prediction 还是 differential validity？
- [ ] 所选检验是否与假设语言匹配？（slope 语言 → 交互项；strength/correlation 语言 → 分组相关比较）
- [ ] 是否区分了 cross-level direct effect 与 cross-level slope effect？
- [ ] 是否在 M7 中说明交互项/分组比较的解释策略（simple slopes、Fisher z 等）？

**常见反模式**：
- 声称 differential validity 却用 MMR 交互项系数解释；
- 用 subgroup regression 的系数差异代替 correlation 强度差异；
- 跨层调节未在 M7 中声明 focal unit 和 nesting structure；
- 调节假设改变 slope，但 Results 仅报告主效应方向，未解释交互形态。

---

### M8. 识别策略 / 效度 / 诊断检验

> **M8 的写作边界**：M8 只写**基准估计所需的识别论证与诊断**，不写 Results 才展开的稳健性检验。例如：IV 的排他性约束、DiD 的平行趋势假设、实验的操纵检验、匹配的共同支撑域——这些是基准识别的一部分。而替代模型、替代测量、子样本敏感性、安慰剂检验等属于 Results（R7/R8）。

**通用填空段落**：

```text
To address concerns about [threat], we [design feature/test]. This check assesses whether [assumption] is plausible. We report the results in [Results/Table/Appendix]. Although [assumption] cannot be directly tested, the evidence below helps reduce concerns about [threat].
```

**自然实验/DiD 变体**：
```text
Our identification strategy relies on [source of variation]. [Shock/event/policy] creates variation in [treatment] that is plausibly exogenous to [outcome] because [reason]. The key identifying assumption is that [treated and control units] would have followed similar trends absent [treatment]. We assess this assumption in the Results section using [event-study/leads-lags] specifications. We first estimate a parsimonious specification because [controls] may be affected by [treatment].
```

**固定效应局限诚实说明变体**（hoffmann2024 型 — 条件 Logit 不能加入 firm FE 时的诚实辩护）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：省略或脚注提及
```text
An important methodological note concerns our use of [industry/state] rather than [firm] fixed effects. Ideally, we would include [firm] fixed effects to absorb all time-invariant firm-level heterogeneity. However, in a conditional logit framework with a binary dependent variable, [firm] fixed effects create an incidental parameters problem: the number of fixed effects grows with sample size, producing inconsistent estimates. We therefore include [industry/state] fixed effects, which absorb unobserved heterogeneity at the [industry/state] level, and we control for observable time-varying [firm] characteristics — including [examples: e.g., firm size, leverage, R&D intensity, profitability] — that may correlate with both [treatment] and [outcome]. While this approach does not eliminate all firm-level confounding, the staggered adoption design and the inclusion of [number] time-varying firm controls provide meaningful mitigation. We also report robustness checks using a linear probability model with [firm] fixed effects, which yields [qualitatively similar / directionally consistent] results, increasing confidence that our findings are not artifacts of unobserved firm heterogeneity.
```

**固定效应局限诚实说明 QC**:
- 必须诚实说明为什么不能使用 firm FE（不能假装不存在这个问题）
- 必须命名具体的 time-varying firm controls 来辩护替代方案（不能只写 "we control for firm characteristics"）
- 必须报告替代估计量结果（如 LPM + firm FE）作为 robustness
- 不能声称 "we fully address endogeneity" — 使用 "meaningful mitigation" / "increase confidence" 等诚实措辞

**DiD 置换检验预览补充**（可选，置于自然实验/DiD 变体后）：
```text
We also conduct permutation tests by randomly assigning [treatment status/timing] across [N] iterations to assess whether [unobserved characteristics] could drive our results.
```

**内生性/控制函数变体**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：M8 通用段落
```text
Because [timing/choice] may be endogenously chosen in the [outcome] model, we use a control-function approach: first estimate [timing model], then include the first-stage residual in the [outcome model]. [Variable] identifies the first stage because it should affect [timing] but not [second-stage outcome], since [theoretical reason].
```

**测量局限辩护：披露阈值/左删失变体**（当数据存在报告阈值或下限堆积时）： ✓ STANDARD
```text
[Source] reports [measure] only when [threshold/rule], so values below [threshold] appear as zero or are not observed. This rule could introduce measurement error if [firms/actors] cluster just below the threshold or if the threshold varies systematically with [confound]. We examine the distribution of observed [measure] values and find no evidence of bunching around [threshold]; [percentage]% of positive observations exceed [multiple of threshold], and the mean and median positive values ([mean], [median]) are well above the reporting floor. We therefore expect any attenuation from threshold-based measurement error to be limited, and if anything it would bias our estimates toward zero, making significant results harder to obtain.
```

> **披露阈值 QC**:
> - 必须说明具体 threshold/rule
> - 必须检查并报告是否存在 bunching（不能仅假设无堆积）
> - 必须解释为什么该测量误差不至于推翻推断（最好是保守偏误逻辑）
> - 若存在明显堆积，不应使用此变体，应考虑 Tobit / Heckman / 其他删失模型

**实验效度变体**：
```text
To assess the [manipulation] manipulation, participants rated [check item]. Participants in the [condition] condition perceived [construct] as [higher/lower] than those in the [comparison] condition. These results indicate that the manipulation was successful. Results were [unchanged/qualified] when [attention-check/manipulation-check exclusion] was applied.
```

**多研究变体**：
```text
The sample, method, and analyses for Study [x] were preregistered at [repository/link placeholder]. As preregistered, we excluded participants who [criterion], producing a final analytic sample of [N].
```

**IV 排他性约束/过度识别检验变体**：
```text
A threat to our IV strategy is that [instrument] may affect [outcome] through channels other than [endogenous predictor]. We address this concern in three ways. First, we argue theoretically that [instrument] influences [outcome] only through [predictor] because [theoretical mechanism / institutional feature]. Second, we include [control for alternative channel] in the second stage to absorb [potential violation path]. Third, [IF overidentified: we report the Sargan / Hansen J overidentification test ([value], p = [value]), which does not reject the null that all instruments are valid, strengthening confidence in the exclusion restriction. IF just-identified: because the model is just-identified (one instrument for one endogenous variable), overidentification tests are infeasible. We therefore rely on theoretical arguments for the exclusion restriction and conduct placebo tests / sensitivity analyses to assess robustness.]
```

**同伴效应/网络效应 falsification 变体**： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：M8 通用段落
```text
Because [network-based construct] may capture common shocks or sorting rather than true peer influence, we conduct falsification tests. We re-estimate our models using [placebo network: random peers / future peers / peers from unrelated network layer] as the independent variable. If the main effect is driven by common shocks, the placebo network should also yield a significant coefficient. The coefficient on [placebo network] is [not significant / opposite direction / much smaller], suggesting that the [focal network] effect is not an artifact of [common shock / sorting]. We also test [alternative mechanism] by [test description]; the result is [status], further distinguishing [theorized mechanism] from [alternative].
```

**匹配DiD 平行趋势与重叠支撑变体**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：M8 自然实验/DiD 变体
```text
The key identifying assumption is that [treated] and [matched control] units would have followed parallel trends absent [treatment]. We assess this assumption using [event-study / leads-and-lags] specifications in which we include [lead/lag indicators] relative to [event]. The pre-treatment coefficients are [individually / jointly] insignificant ([test statistic] = [value], p = [value]), suggesting no detectable pre-treatment divergence. We also verify overlap by plotting [propensity-score distributions / covariate balance] before and after matching; the [common support region] covers [percentage]% of the sample, and no observations lie outside the [calipersize] caliper.
```

**粗化精确匹配（CEM）/ 匹配解决内生性变体**（非 DiD，仅用匹配加权解决内生性）：
```text
To address concerns about endogeneity — specifically, that [predictor] may be influenced by [past outcome / ongoing confound] — we exploit an exogenous shock: [treatment definition, e.g., a change in the firm's CEO]. We use coarsened exact matching (CEM)-weighted [estimator], matching [treated units] to [control units] on pretreatment variables: [matching variables]. This yields [N] matched strata containing [N treated] and [N control] observations. The CEM-weighted results confirm that [focal effect] remains [status] even when [predictor] changes are exogenously driven.

To validate the exogeneity of [treatment], we demonstrate that [pretreatment outcomes] do not predict the likelihood of [treatment] ([logit/Probit] regression) and do not predict [predictor] levels (panel fixed-effects models). These checks reduce concerns that the [predictor-outcome] relationship is driven by reverse causality or omitted variables related to [confound].
```

**制度/政策体制安慰剂检验变体**：
```text
Because [outcome] may reflect [alternative mechanism] rather than [focal mechanism], we exploit a [regime change] as a falsification test. During the [mandatory regime], [behavior] should not exhibit [focal pattern] because [institutional reason]. We re-estimate our models using [mandatory regime subsample] and find [null effect], consistent with the assumption that [focal mechanism] requires [voluntary regime condition].
```

**部分重叠同伴群体 + 形式化识别证明变体**（网络效应核心识别故事）：
```text
Our identification strategy relies on two features of partially overlapping peer groups. First, because [percentage] of firms operate in multiple industries, peer groups vary at the individual firm level. This breaks the linear dependence between the endogenous peer variable and exogenous peer characteristics that plagues perfectly overlapping groups. Formally, in a perfectly overlapping group, PeerDisclosure is a linear combination of peer characteristics, making identification impossible. With partial overlap, the peer group matrix has full rank because each firm faces a unique combination of peers.

Second, we instrument [endogenous peer variable] with [second-degree peer characteristics], which are plausibly uncorrelated with unobservable shocks affecting the focal firm's [outcome] because second-degree peers are not in the focal firm's peer group. The exclusion restriction is supported by three arguments: (1) [theoretical argument], (2) [mandatory-regime falsification], and (3) [Hansen J-test / statistical argument].
```

**SEM 模型识别变体**（当使用结构方程模型或联立方程时）：
```text
Because we estimate a system of [N] equations simultaneously, we verify model identification before interpreting coefficients. The model has [degrees of freedom] degrees of freedom (positive, indicating over-identification). Each structural equation satisfies the order condition (number of excluded exogenous variables ≥ number of included endogenous variables minus one) and the rank condition (the matrix of excluded exogenous variables has full column rank). For the measurement model, we report confirmatory factor analysis (CFA) fit indices: CFI = [value] (≥ 0.90), RMSEA = [value] (≤ 0.08), and SRMR = [value] (≤ 0.08), indicating acceptable fit. We also report the χ² test ([value], df = [df], p = [value]) as an absolute fit measure, noting that χ² is sensitive to sample size. All factor loadings are significant (p < [threshold]) and exceed [value], supporting convergent validity. The average variance extracted (AVE) for each construct is [value], exceeding the squared correlation between constructs, supporting discriminant validity.
```

---

### M9. 多研究 / 实验程序 / 质性编码

**多研究总览段**（M9 前置）：
```text
Study [x] tests [hypothesis/effect] using [sample/design]. Study [y] extends Study [x] by examining [mechanism/boundary/alternative explanation]. Together, the studies provide evidence for [main effect], [mechanism], and [boundary condition].
```

**逐研究过渡段**：
```text
In Study [x], we sought to test [hypotheses] and address [limitation/gap] from [prior study/evidence]. Study [x] used a [factorial/correlational/archival] design with [factors/conditions] and tested H[x–y]. Participants were directed to [task/context], randomly assigned to [condition], and then completed [outcome/mechanism] measures.
```

**研究间衔接段**：
```text
Although Study [x] addresses [issue], it cannot establish [remaining need]. Study [x+1] therefore [design upgrade]. Across Studies [x–y], the evidence converges on [theoretical pattern] while progressively addressing [validity concerns].
```

---

### M10. Methods 到 Results 的过渡

**通用填空段落**：

```text
The Results section first reports [main tests] and then examines [validity/robustness checks]. Because [measure/design] raises [concern], we address this issue in supplemental analyses using [test]. The model requires interpreting [marginal effects/predicted values], which we report after the coefficient estimates. We assess the plausibility of [identification assumption] through [event-study/placebo/diagnostic] tests.
```

---

---

## 下游接口

- `/write-results` — 使用本骨架的变量名、模型规格和 M10 预告作为 Results 报告的基准
- `/paper-review` — 进行 Theory-Methods 假设-变量映射对齐检查
- `/methods-review` — 如用户已有 Methods 草稿，使用本骨架作为理想基准对比审查
- `/distill-methods-exemplar` — 对生成后的 Methods 段落进行反向蒸馏审查，检查槽位覆盖、DNA 指标、可迁移性和因果语言合规性。审查结果作为 Vault 参考注释，不自动修改本 skill 的骨架库

### Cross-Section 对齐检查（与上游 Skill 的接口）

本 Skill 的输出必须与上游 Skill 的承诺严格对齐。生成骨架后，执行以下对齐检查：

#### 对齐检查 1：Introduction ↔ Methods（I6 Preview ↔ M7/M8）

| Introduction 承诺（I6 Preview） | Methods 兑现（M7/M8） | 检查问题 | 失败信号 |
|-------------------------------|---------------------|---------|---------|
| "Drawing on... we argue that..." | M7 的 estimator 和 model specification | Theory 承诺的机制是否在模型中被正确设定？ | M7 缺少 mediator 方程或交互项 |
| "Using [data] and [methods]" | M2 数据来源 + M7 估计方法 | 数据和方法是否与 Preview 一致？ | 数据来源或估计方法与 Preview 不符 |
| "We account for [identification concern]" | M8 识别策略 / 效度检验 | Preview 中提到的识别关切是否在 M8 中被处理？ | M8 缺失 Preview 承诺的检验 |

#### 对齐检查 2：Theory ↔ Methods（假设列表 ↔ M3-M6 变量操作化）

| Theory 假设 | Methods 变量 | 检查问题 | 失败信号 |
|------------|-------------|---------|---------|
| H1: [IV] → [DV] | M4 自变量 + M3 因变量 | IV 和 DV 的操作化是否与假设中的构念一致？ | 构念名与变量名不一致 |
| H2: [Mediator] 中介 | M5 中介变量 | 中介变量是否被正确测量和纳入模型？ | M5 缺失中介变量或测量方式不符 |
| H3: [Moderator] 调节 | M5 调节变量 + M7/M7补充 检验选择 | 调节变量是否被操作化？检验方法是否与 Theory 的 differential prediction / differential validity 声明一致？ | M7 缺少交互项（prediction）或 M7补充 缺少分组相关比较（validity） |
| 控制逻辑 | M6 控制变量 | 每个控制变量是否对应 Theory 中的竞争性解释？ | M6 出现与 Theory 无关的控制变量 |

**对齐偏离记录格式**：

```markdown
### Cross-Section 对齐偏离记录

| 偏离ID | 上游承诺 | 本段实际内容 | 偏离类型 | 严重程度 | 修正建议 |
|--------|---------|------------|---------|---------|---------|
| D1 | I6 Preview: "We use IV to address endogeneity" | M7 使用 OLS/FE，未提及 IV | 识别策略缺失 | 高 | 在 M7 中添加 2SLS 或在 I6 中删除 IV 承诺 |
| D2 | Theory H2: Mediation via routine updating | M5 未包含 routine updating 变量 | 机制变量缺失 | 高 | 补充 M5 中介变量段 |
```

---

## Robustness Check Menu

顶刊论文通常要求系统报告稳健性，但**位置取决于该检验是否属于基准识别策略的一部分**。

### 归属判断

| 检验类型 | 归属 | 原因 |
|---|---|---|
| IV 排他性约束 / 弱工具变量诊断 | **M8**（基准识别一部分） | 没有这些诊断，2SLS 估计量本身不可信 |
| DiD 平行趋势 / 事件研究 | **R7**（通常）或 **M8 预览 + R7 报告** | 平行趋势是识别假设，但其结果通常在 Results 中展示；M8 可预告 "we assess in Results" |
| 匹配共同支撑域 / 平衡性 | **M2/M8**（基准样本构造） | 匹配是获得可比对照组的前提 |
| 替代模型 / 替代测量 / 子样本 / 安慰剂 / 时点敏感性 | **R7** | 属于对主结果稳健性的补充验证 |
| 机制 / 替代解释排除 / 探索性扩展 | **R8** | 非假设检验，属于补充或事后分析 |

### Results 稳健性清单（供 M10 预告时引用）

当用户在 Methods 中问及 robustness 时，提示："稳健性检验通常在 Results 中展开；Methods 只在基准识别需要时简要说明。"

- [ ] **Model selection**: Alternative functional forms, distributions, or estimators (e.g., Weibull/Gompertz for hazard models; GEE for panel logit; LPM+2SLS for binary IV)
- [ ] **Measure sensitivity**: Alternative operationalizations, cutoffs, percentile thresholds, or transformations (e.g., top/bottom 20%, 30%, 40% vs. quartile; raw count vs. relative percentage)
- [ ] **Sample selection**: Matching (CEM, PSM), weighting, subsample analysis, or attrition comparison
- [ ] **Reverse causality**: Lag structures (t-1, t-2), Granger causality, lead-lag tests, or control-function approach
- [ ] **Alternative explanations**: Mechanism vs. confound via interactions, auxiliary models, or placebo tests
- [ ] **Outliers and influential observations**: With and without top/bottom 1% or Cook's distance thresholds
- [ ] **Clustering and SE sensitivity**: Alternative clustering levels, wild bootstrap, or spatial HAC

### M10 Results 预告段（仅用于预告 R7 内容，不展开结果）

```text
To assess the robustness of our findings, we report a series of sensitivity analyses in the Results section. These address [measurement concerns] through [alternative operationalizations], [model choice] through [alternative estimators], [sample composition] through [subsample analyses], and [endogeneity concerns] through [lag structures / placebo tests].
```

**注意**：该预告段不得包含具体结果、系数或 "results remain consistent" 等结论性表述——那些属于 R7。

### M8 中不应出现的稳健性内容

以下检查应严格留在 Results（R7/R8），不得在 M8 中详细展开：
- 替代模型（如 OLS 换 Tobit / Poisson 换负二项）的估计结果；
- 替代测量/截断点选择后的系数变化；
- 安慰剂检验、随机化处理、置换检验的具体结果；
- 子样本敏感性分析的结果。

---

## 常见反模式

以下错误在 Methods 中高频出现，生成段落前主动排查：

- **模型选择无文字解释**：只写 "we estimate FE model" 而不解释为什么 FE 优于 RE/OLS，或为什么选此 estimator
- **控制变量无 because**：列出 Size, Age, ROA 但不解释每个变量控制的是什么竞争性解释
- **因果语言越级**：面板数据 design 下使用 "caused" "led to" 等强因果词；自然实验未通过平行趋势检验就用 "effect of... on..."
- **样本漏斗缺数字**：写 "we exclude missing values" 但不报告每一步损失了多少观测
- **识别策略后置或缺失**：DiD/IV/自然实验不把识别假设和检验放在核心位置，而是 buried 在脚注或附录
- **交互/非线性模型无解释策略**：加入 interaction/nonlinear term 后未预告如何在 Results 中解释（marginal effects / simple slopes / AME）
- **调节假设检验错位**：Theory 声明 differential validity（关系强度变化）却用 MMR 交互项检验；或声明 differential prediction（slope 变化）却用分组相关比较检验
- **时间顺序模糊**：未明确说明预测变量是 t-1 还是 contemporaneous，或事件窗口的起止逻辑
- **Bad Control 问题**：在 DiD/自然实验中控制了 post-treatment 变量或 collider
- **设计排他性混淆**：把 IV 的语言习惯（"effect of X on Y"）套用到 OLS/FE 设计；把实验的操纵检验语言套用到档案数据
- **动态面板 FE 陷阱**：为短面板推荐固定效应而不提示 Nickell bias 或提供 GMM 替代方案
- **过度泛化诊断要求**：为非 IV 设计要求排他性约束检验，为非 DiD 设计要求平行趋势检验，为非匹配设计要求重叠支撑检验
- **机构/政策名残留**：用户填入的 [placeholder] 中混入了论文特有的机构名、政策名、数据库名，导致段落不可迁移到其他情境

## 诚实边界

本 skill 基于 32 篇 MVP30 范文语料库（2010–2025）提炼，存在以下局限：

1. **不能替代统计诊断**：提供段落骨架和 ritual 规范，但不能判断您的数据是否满足模型假设（平行趋势、工具变量相关性、共同支撑域、VIF、序列相关等）。这些必须基于实际数据。
2. **不能消除期刊差异**：SMJ/AMJ/ASQ/JM/OS/JOM/ASR 对 Methods 的 ritual 偏好不同。本 skill 以"最大公约数"为主，投稿前需对照目标期刊最新范文调整。
3. **不能生成真实统计量**：所有 [placeholder] 中的系数、p 值、F 统计量、样本量、VIF 值必须由用户根据实际估计结果填入。本 skill 不虚构任何数字。
4. **语料库领域偏差**：范文主要来自战略管理、营销、组织行为。金融、会计、运筹、宏观等领域的 ritual 可能不同。
5. **不能覆盖最新方法论**：语料库截止于 2025 年，更新的估计量或识别策略可能未覆盖。
6. **设计排他性不可违反**：不能为不需要某诊断的设计强制插入该诊断。例如：非 IV 设计不得要求排他性约束检验；非 DiD 设计不得要求平行趋势检验；非匹配设计不得要求重叠支撑检验。
7. **动态面板必须提示 Nickell bias**：当面板时间维度较短（T < 10）且因变量具有持续性时，不能推荐固定效应而不提示 Nickell bias 或提供系统 GMM / 差分 GMM 替代方案。
8. **不得泛化特殊设计的 causal 语言**：OLS/FE 的骨架必须使用 "associated with"；自然实验在平行趋势/事件研究支持后才可使用 "effect of... on..."；实验设计可使用 "caused"。不得让面板数据 design 的段落中出现 "leads to" 或 "causes"。

## 生成后自检清单

生成 Methods 段落后，逐条核对：

### Completeness
- [ ] M1：研究情境有至少 3 个理由，且与理论机制直接挂钩
- [ ] M2：样本漏斗包含起始总体 → 每步排除（理由+数字）→ 最终 N
- [ ] M2.5（如适用）：复杂识别设计前是否插入 model-free evidence 作为可信度铺垫
- [ ] M3：因变量有构念定义 + 操作化 + 测量来源 + 方向解释
- [ ] M4：每假设一段，含 Hypothesis 编号对齐，变量按理论顺序排列
- [ ] M5：调节/中介/机制变量有操作化和交互项说明
- [ ] M6：每个控制变量都有 because [rival explanation]
- [ ] M7：estimator + fixed effects + SE clustering + 选择理由（文字+诊断）
- [ ] M7补充：若 Theory 含调节假设，检验方法（MMR / 分组相关比较 / HLM 跨层交互）与 differential prediction/differential validity 声明一致
- [ ] M8：关键识别假设 + 检验方法 + 结果位置
- [ ] M10：Results 预告（表格顺序、特殊解释需求、识别检验位置）

### Clarity
- [ ] 变量名与 Results 表格完全一致
- [ ] 时间顺序明确（滞后几期、事件窗口、观测期起止）
- [ ] 因果语言强度与 design strength 匹配
- [ ] 所有 [placeholder] 已被替换，无残留方括号

### Credibility
- [ ] 识别假设有检验（平行趋势/过度识别/manipulation check）
- [ ] 样本漏斗可审计（每步有数字和排除理由）
- [ ] 模型选择有文字解释，不埋在方程里
- [ ] 非显著假设在 Methods 中未预告支持状态

### 论证质量诊断
- [ ] **Because 密度**：M6 中每个控制变量都有 "because [rival explanation]"——这是 Methods 说服力的核心来源
- [ ] **假设对齐**：M4/M5 中每预测变量明确提及对应 Hypothesis 编号
- [ ] **因果语言自律**：面板数据用 "associated with"；自然实验识别支持后用 "effect of"；实验可用 "caused"。无越级
- [ ] **审计链完整**：M2 起始 N → 每步排除（含理由+数字）→ 最终 N，全程可追踪
- [ ] **时间逻辑清晰**：所有预测变量标注 t-1 / contemporaneous / event window

### 反向审查（可选但建议）
生成完成后，可使用 `/distill-methods-exemplar` 对输出段落进行反向蒸馏审查，生成 Vault 参考注释，供人工判断：
- 槽位覆盖是否完整（M1–M10）
- 表达骨架是否可迁移（无机构名/政策名残留）
- 因果语言强度是否与 design strength 匹配
- 识别策略和 validity threat 处理是否达到顶刊 ritual 标准

**注意**：反向审查产出存入 Vault，不自动修改本 skill 的骨架库。是否采纳为 skill 参考由人工决定。

## Constraints

- 必须提醒用户：替换所有 `[方括号占位符]` 为实际内容；不虚构样本量、来源、变量定义或诊断结果。
- 变量名必须与 Results 表格完全一致。
- 每个控制变量必须有明确的控制逻辑（已在段落骨架中内置 "because [rival explanation]" 槽位）。
- 样本漏斗必须包含每一步的数字和理由（已在 M2 骨架中内置）。
- 因果语言强度必须与 design strength 匹配。以下是按设计家族的强制词汇表：

| 设计家族 | 允许动词 | 禁止动词 | 使用条件 |
|---------|---------|---------|---------|
| 面板数据/OLS/FE/HLM | associated with, related to, linked to, corresponds to | increases, decreases, leads to, causes, drives, produces | 无条件禁止强因果词 |
| DiD / 自然实验 | effect of ... on ..., associated with | causes, leads to, drives | 仅在平行趋势/事件研究支持后可用 "effect of... on..."；否则退回 "associated with" |
| IV/2SLS | effect of ... on ..., increases, decreases | causes, leads to, produces | 仅在 M8 识别假设 preview 后可用；second-stage 汇报可用 "effect" 但避免 "causes" |
| 非线性模型 (Logit/Probit/Tobit/计数) | associated with, increases the likelihood of, changes the probability of | increases, decreases, causes, leads to | 系数本身不可直接解释；必须通过边际效应/概率变化转述 |
| 生存分析 | associated with, lengthens/shortens time to, changes the hazard of | causes, leads to, produces | hazard ratio / AFT 系数需通过生存概率或时间变化转述 |
| SEM / 同时方程 | associated with, predicts, influences | causes, leads to, produces | 结构方程系数表示预测关系，非因果；仅在过度识别且模型拟合良好时可谨慎使用 "effect" |
| 实验 | caused, led to, produced, increased, decreased | — | 随机化支持后可直接使用强因果词 |

- 不要报告支持状态在 Methods 中。
- 不要把模型选择埋在方程里而没有文字解释。

## 语料与变体

设计类型的具体变体见 `academic-writing-corpus/[设计类型].md`。新论文的蒸馏结果通过 `distill-methods-exemplar` → Phase 4 `skill_update_instructions` 自动写入。

---
*基于 34 篇 MVP30 范文语料库、Pollock 2025 Ch07 构建。版本 3.2.0。*
