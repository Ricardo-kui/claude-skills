---
name: write-methods
description: |
  顶刊 Methods 填空段落骨架生成器。输入模型类型后输出带 [placeholder] 的可直接粘贴段落。
  覆盖OLS/FE、自然实验/DiD、非线性模型、生存分析、SEM、实验、多研究、稀有结果、实证对象构建、事件历史+事件研究、同时方程、IV/2SLS、动态面板/GMM、匹配DiD/广义DiD、同伴效应/网络效应、文本构念测量、PSM匹配面板、堆叠扩散Logit、多行为者设计、推断二元结果共二十种设计类型。
  触发词：「写methods」「methods模板」「方法部分怎么写」「帮我写methodology」「method skeleton」「写方法」「方法论」「model specification」「估计方法」「样本选择」「变量定义」。
  当用户提及变量操作化、识别策略、稳健性检验、模型设定、样本漏斗、内生性处理时也应触发。
  基于 28 篇 MVP30 范文语料库和 Pollock 2025 Ch07。
version: 2.5.0
---

# Role

你是顶刊论文 Methods 的**填空模板生成器**。基于 28 篇 MVP30 范文和 Pollock 2025 Ch07，输出可直接复制到 Word/LaTeX 中、填入用户具体信息即可成段的 Methods 骨架。

核心原则：Methods 要 **describe, explain, justify**。每个填空段落已经内置了这三重功能，用户只需替换方括号中的占位符。

## 调用方式

```
/write-methods <模型类型> [--hypotheses="..."] [--journal=AMJ] [--design-variant=标准]
```

**参数说明**：
- `<模型类型>`（必填）: `OLS/FE` | `自然实验/DiD` | `非线性模型` | `生存分析` | `SEM` | `实验` | `多研究` | `稀有结果` | `实证对象构建` | `事件历史+事件研究` | `同时方程` | `IV/2SLS` | `动态面板/GMM` | `匹配DiD/广义DiD` | `同伴效应/网络效应` | `文本构念测量` | `PSM匹配面板` | `堆叠扩散Logit` | `多行为者设计` | `推断二元结果`
- `[--hypotheses]`（可选但建议）: Theory 部分的假设列表，用于变量对齐检查
- `[--journal]`（可选）: 目标期刊，默认 `AMJ`

**如果省略模型类型**，进入交互式询问，确定设计类型后输出对应骨架。

## 快速开始（3 步上手）

**第 1 步**：输入 `/write-methods OLS/FE --hypotheses="H1: X -> Y (+); H2: X -> M (+)"`

**第 2 步**：复制生成的 M1–M8 骨架到 Word/LaTeX

**第 3 步**：逐段替换 `[方括号占位符]` 为你的实际内容

> 如果你只有 **1 个主效应 + 1 个调节变量**，通常只需填充 M1（研究情境）、M2（样本漏斗）、M3（因变量）、M4（自变量）、M5（调节变量）、M6（控制变量）、M7（模型规格）共 7 段。M8（识别策略）仅在 DiD/IV/实验/匹配设计时强制要求；M10（过渡段）约 90% 论文可省略。

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
| M8 | 识别策略 / 效度 / 诊断检验 | 1–2 段填空；IV/DiD/实验/匹配 强制；OLS/FE 可选 |
| M9 | 多研究 / 实验程序 / 质性编码 | 多研究时逐研究重复 M1–M8 |
| M10 | Methods 到 Results 的过渡 | 1 段填空；**顶刊中极度罕见（<10%），可省略** |

## 标准顺序与特殊分支

**默认顺序**：M1 → M2 → M3 → M4 → M5 → M6 → M7 → M8 → M10

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

---

## 填空段落骨架

### M1. 研究情境 / 实证背景

**通用填空段落**：

```text
[Empirical setting] provides an appropriate context for examining [theoretical relationship] for three reasons. First, [setting property] makes [mechanism] observable. Second, [scope condition] reduces [confound]. Third, [data feature] allows us to observe [unit/process] over [period]. The unit of analysis is [unit], which aligns with our theorizing about [mechanism].
```

**自然实验/DiD 变体**（替换首句）：
```text
We examine [phenomenon] using [policy/event/institutional change] that altered [exposure/risk/incentive] across [units] and time. [Empirical setting] is well suited because [process] is well documented and [context controls] reduce [confounding concern].
```

**实验变体**：
```text
We test [theoretical claim] using a [laboratory/field/online] experiment. This design is strongest for assessing [internal validity], although it requires caution in generalizing to [boundary condition].
```

**多研究变体**：
```text
Across [N] studies, we use complementary designs to test [theory] and address [validity concerns]. Study 1 examines [field/archival evidence], Study 2 tests [replication/design upgrade], and Studies [x–y] examine [mechanism/intervention/behavior].
```

**同时方程/SEM 变体**（替换整个 M1）：
```text
Our conceptual framework links [driver], [mechanisms], [outcome], and [downstream outcome]. We therefore specify a system of [N] equations to capture [direct path], [mediating paths], [downstream path], and [reverse/auxiliary path]. [Empirical setting] provides the data needed to estimate these relationships jointly.
```

---

### M2. 数据来源与样本漏斗

**通用填空段落**：

```text
We began with [starting population] from [source] over [period]. We matched these observations to [additional sources] to obtain [variables]. We excluded [cases] because [comparability/measurement/identification reason]. The final sample consists of [N] [units] observed over [period], with [unit] as the unit of analysis.
```

**稀有结果变体**（在通用段落前插入）：
```text
Because [outcome] is rare, a simple random sample would yield too few [cases] for meaningful analysis; we therefore used [sampling strategy]. The screening criterion increased the likelihood of observing [rare phenomenon], but it did not determine [final outcome measure]. Because [sampling design] affects [representation/effect sizes], we interpret signs and significance but avoid overinterpreting magnitude.
```

**实证对象构建变体**（替换或前置）：
```text
No authoritative database exists for [empirical object], so we constructed the dataset from [trace/source]. We used [trace/source] because it records [actor claim/action/evaluation] over time. From [raw records], we identified [entities], [events/labels/claims], and [time points]. We then transformed [raw trace] into [analytic variable] by [coding/aggregation rule]. To make the construction auditable, we define each step from [raw input] to [final measure].
```

**自然实验/DiD 变体**：
```text
Our primary sample consists of [units] observed from [period], drawn from [source] because it tracks [construct-relevant activity]. The observation window begins in [year] because [source/construct availability] and ends in [year] to capture [post-treatment horizon]. Treatment is observed for [treated units] after [event], while [control units] provide the counterfactual comparison. Because testing [moderation/mechanism] requires [additional source], the sample for H[x] is restricted to [available period/units].
```

**多研究变体**（逐研究）：
```text
Study [x] used [sample source]. Participants/observations were included if [criterion], yielding [analytic sample]. For supplemental analyses, we also use [source] to measure [assumption/mechanism/alternative outcome].
```

**PSM匹配面板变体**（在通用段落中加入匹配步骤）：
```text
To reduce selection bias, we first estimate propensity scores using [logit/probit] with [covariates] as predictors of [treatment/status]. We match [treated units] to [control units] using [method: one-to-one nearest-neighbor / kernel / caliper] matching with [calipersize] caliper on [distance metric]. After matching, the standardized bias for all covariates is below [threshold], and the [t-test / KS-test] indicates no significant difference in [covariates] between groups. The matched sample consists of [N] [unit-years / dyads / firms].
```

**多行为者设计变体**（替换通用段落）：
```text
Our data link [actor A], [actor B], and [actor C] through [matching key / dyadic structure]. We began with [starting universe of actor A] from [source A] over [period] and matched these to [actor B observations] from [source B] using [matching rule]. We then linked [actor C characteristics] from [source C]. The final analytic sample consists of [N] [dyads / triads / observations] in which [inclusion condition]. Because [actor B] characteristics are measured at [level], we aggregate [construct] to the [analysis level] using [aggregation rule].
```

**事件历史变体**（在通用段落中加入过程说明）：
```text
[Authority/actor] opens [process] when [trigger]. The process ends when [event occurs] or [case closes/continues]. [Time outcome] is the elapsed time between [start date] and [event date]. Cases without [event] by [end of observation] are treated as [right-censored] because [logic].
```

---

### M3. 因变量

**通用填空段落**：

```text
Our dependent variable is [outcome construct], measured as [operational definition] using [source]. This measure captures [construct] because [construct-validity logic]. Higher values indicate [interpretation direction]. Because [outcome] is [continuous/binary/ordinal/count/censored/time-to-event], we use [model] and interpret [coefficients/marginal effects/hazards/probabilities].
```

**稀有结果/序数变体**（替换末句）：
```text
Given the skewed distribution of [construct], we treat it as ordered categories that distinguish [low/mid/high states]. Because [outcome] is ordinal, coefficients indicate direction but substantive interpretation requires [marginal effects/predicted probabilities].
```

**事件研究变体**：
```text
We measure [market/stakeholder reaction] as [CAR/abnormal response] around [event], using [benchmark model] to estimate expected returns. Expected returns are estimated over [estimation window] using [factor model]; abnormal returns are observed returns minus expected returns. We aggregate abnormal returns over [event window] to allow for [information leakage/dissemination].
```

**指数/净指数变体**：
```text
Because the theory concerns both [positive actions] and mitigation of [negative actions], we construct [net outcome] from [strengths] and [concerns]. For each [category-year], we divide the number of [items] by the maximum possible number in each [category-year] to account for changes in measurement coverage. The net index subtracts [negative index] from [positive index] and sums across [categories].
```

**行为编码变体（实验）**：
```text
We capture [outcome] behaviorally by [task/coding procedure], reducing reliance on self-reported intentions. Blind coders rated [behavior] on [scale]. We averaged ratings because interrater reliability was [acceptable statistic].
```

**文本构念测量变体**（M3 或 M4 均可使用，三段式效度链）：
```text
Our dependent variable, [text-derived construct], is measured from [text source: earnings calls / press releases / 10-K / media / survey open-ends] using [method: dictionary / LDA / supervised ML / word embeddings]. We first [preprocessing: remove stop words / stem / lemmatize / exclude boilerplate]. We then [measurement step: count semantic similarity / topic proportion / trained classifier probability / cosine distance to anchor]. The measure captures [construct] because [theoretical link between text feature and underlying construct]. To validate the measure, we correlate it with [external benchmark: human-coded sample / established scale / related archival measure]; the correlation is [value] (p [relation] [threshold]). We also inspect [example excerpts] to confirm face validity. Higher values indicate [interpretation direction].
```

**推断二元结果变体**：
```text
Our dependent variable is [binary outcome construct]. Because [direct observation is unavailable / the construct is latent], we infer [binary state] from [observable signal: text / count threshold / categorical mapping]. We classify a [unit] as [state = 1] when [rule: keyword presence / count exceeds threshold / human-coded indicator / classifier probability > cutoff]. We set the threshold at [value] because [justification: distribution elbow / domain convention / validation against human coding]. To assess classification accuracy, we [validation procedure: manual audit of random sample / compare to gold-standard subsample / report precision-recall]. The inferred [binary state] aligns with [external indicator] for [percentage] of cases.
```

**多行为者因变量变体**：
```text
We measure [outcome] at the [actor B] level because [theoretical reason: actor B is the decision maker / actor B bears the consequence]. The dependent variable is [operational definition] from [source B]. For robustness, we also construct an alternative measure from [source C] using [alternative rule]. The correlation between the two measures is [value], indicating [acceptable / strong] convergent validity.
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

**处理分配稳定性补充**（DiD 可选）：
```text
During our sample period, [percentage] of [units] changed their [treatment-relevant characteristic, e.g., headquarters location]. We use [historical/fixed] [characteristic] information to maintain consistent treatment assignment.
```

**竞争机制预测变量变体**（机制测试中分解核心构念时）：
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

**同时方程变体**：
```text
Equation [x] predicts [primary outcome] as a function of [focal predictor], [mechanisms], [moderators], interactions, and controls. Equations [y–z] model [mediator A] and [mediator B], allowing us to test whether [focal predictor] affects the mechanisms implied by the theory. Equation [w] predicts [downstream outcome] using [focal outcome], [focal predictor], their interaction, and value-relevant controls. We include an additional equation for [potentially endogenous choice] to account for the possibility that [anticipated need/reverse path] influences [focal predictor].
```

---

### M5. 调节变量 / 中介变量 / 机制变量

**通用填空段落（每变量一段）**：

```text
To capture [boundary/mechanism], we measure [moderator/mediator] as [operation]. We interact [predictor] with [moderator] to test whether [relationship] is stronger/weaker under [condition]. To test the proposed mechanism, we measured [mediator] and included [alternative mechanisms] as rival explanations.
```

**子样本分割变体**（用样本分割而非交互项检验调节时）：
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

**间接调节（ mediated moderation ）变体**：
```text
To test the indirect moderation model, we specify a system of equations. Equation (2) captures the moderating effect of [moderator 1] on the [predictor-outcome] relationship: [outcome] = β₁₀ + β₁₁[predictor] + β₁₂[moderator 1] + β₁₃[predictor × moderator 1] + ε₁. Equation (3) captures the moderating effect of [moderator 2]: [outcome] = β₂₀ + β₂₁[predictor] + β₂₂[moderator 2] + β₂₃[predictor × moderator 2] + ε₂. Equation (4) models the relationship between [moderator 1] and [mediator]: [mediator] = β₃₀ + β₃₁[moderator 1] + ε₃. Equation (5) represents the full system with both moderators: [outcome] = β₄₀ + β₄₁[predictor] + β₄₂[moderator 1] + β₄₃[predictor × moderator 1] + β₄₄[mediator] + β₄₅[predictor × mediator] + ε₄.

We test for full indirect moderation through [mediator] according to whether: (1) [moderator 1] functions as a moderator when [mediator] is not considered (β₁₃ ≠ 0); (2) [moderator 1] influences [mediator] (β₃₁ ≠ 0); (3) [mediator] moderates the effect of [predictor] on [outcome] (β₄₅ ≠ 0); and (4) the coefficient on the original interaction term in the full system (β₄₃) indicates the pattern of mediation—β₄₃ = 0 indicates full indirect moderation (the direct moderating effect of [moderator 1] becomes nonsignificant in the presence of [mediator]), whereas β₄₃ ≠ 0 and |β₄₃| < |β₁₃| indicates partial indirect moderation.
```

---

### M6. 控制变量与竞争性解释

**通用填空段落**：

```text
We include controls for [threat family 1] because [alternative explanation 1]. At the [level] level, we control for [variables] to account for [rival process]. We also include [fixed effects] to absorb [time-invariant/common/contextual shocks]. All time-varying predictors are measured at [lag/timing] to preserve temporal ordering. We lag the control variables by [period] to reduce simultaneity concerns.
```

**自然实验/Bad Control 变体**：
```text
Because some controls may be affected by [treatment], we first estimate a parsimonious model with fixed effects before adding controls. We do not include [variable] because it may be post-treatment / mechanically related to [outcome].
```

**同时方程/方程特定控制变体**：
```text
For [equation/outcome family], we include controls that address [rival explanation]. For [mediator equation], we further control for [industry benchmark] because firms may align [decision] with industry norms. In the [downstream outcome] equation, we control for [profitability], [growth], and [market position] because each may independently affect [value outcome]. In the [financial choice] equation, we include known determinants such as [industry norm], [asset structure], [firm size], and [profitability].
```

**实验变体**：
```text
We control for [participant characteristics] because [rival explanation]. Random assignment allows us to isolate the effect of [manipulation] on [outcome] within the experimental context.
```

---

### M7. 模型规格与估计方法

**通用填空段落**：

```text
Because [dependent variable] is [continuous/binary/ordinal/count/censored/time-to-event], we estimate [model]. The specification includes [fixed effects] to absorb [unobserved heterogeneity/common shocks]. Standard errors are clustered at [level] to account for [within-unit dependence]. We use [estimator] for [hypotheses] because [outcome/design logic]. We also considered [alternative estimator]; results using this approach are reported as [robustness/supplement].
```

**模型选择理由补充段**（按需添加）：
```text
We employ [unit] fixed effects rather than random effects because the Hausman test rejects the random-effects assumption (χ² = [value], p < 0.01), indicating that unobserved [unit]-specific factors are correlated with our independent variables. [Year] fixed effects control for temporal trends such as [macroeconomic shocks/industry-wide shifts].
```

**诊断检验补充段**：
```text
We conduct several diagnostic tests. First, the Variance Inflation Factor (VIF) for all independent variables is below [value], well below the conventional threshold of 10, indicating that multicollinearity is not a concern. Second, the [Wooldridge/modified Wald] test indicates [presence/absence] of [autocorrelation/heteroskedasticity], and we report [robust/clustered] standard errors accordingly.
```

**非线性模型变体**：
```text
Because [outcome] is [binary/ordinal/count/censored/time-to-event], we estimate [model]. Coefficients indicate direction, but substantive interpretation requires [marginal effects/predicted probabilities/hazard ratios/odds ratios]. We assess [assumption] using [diagnostic/test], discussed below.
```

**DiD 变体**：
```text
We estimate a difference-in-differences model in which [outcome] is regressed on [treatment], [moderator/interactions], controls, and fixed effects. Identification comes from comparing changes in [treated units] before and after [event] to contemporaneous changes among [control units]. We cluster standard errors at [unit/jurisdiction] to account for serial correlation and within-[cluster] dependence.
```

**DiD 方程编号与 SE 聚类引用补充**：
```text
We cluster standard errors at the [level] to address [dependence structure] ([citation, e.g., Bertrand et al. 2004; Jager et al. 2021]). Where relevant, we present numbered equations: Equation (1) reports the baseline DiD specification, and Equation (2) reports the event-study leads-and-lags specification.
```

**生存分析变体**：
```text
Because the shape of [event timing] is not known ex ante, we compare [candidate distributions] and select [distribution] based on [fit criterion]. We use an accelerated failure time metric so coefficients can be interpreted in terms of [longer/shorter] time to [event].
```

**复发事件 AFT 变体**（当同一主体经历多次事件时）：
```text
Because [units] experience multiple [events] over the observation period, we estimate recurrent-event accelerated failure time (AFT) models with a [distribution] distribution for the underlying failure rate. Recurrent-event AFT models are appropriate because they examine how [predictors] influence the time to [event] while accounting for repeated occurrences within the same [unit]. We report robust standard errors to account for within-[unit] dependence across multiple events. The specification includes [fixed effects] to absorb unobserved heterogeneity.
```

**同时方程变体**：
```text
Joint estimation addresses simultaneity and accounts for correlated errors across equations. We check [order/rank] conditions to ensure that each equation is identified. We further assess whether [alternative endogenous specification] is necessary by estimating [IV/3SLS] and comparing it with [preferred estimator] using [diagnostic test].
```

**IV/2SLS 变体**：
```text
Although [baseline estimator] can exploit [within/between] variation, it may still be biased if [predictor] is endogenous due to [omitted variable / reverse causality / measurement error]. We therefore use two-stage least squares (2SLS) with [instrument] as an instrument for [endogenous predictor]. [Instrument] satisfies the relevance condition because [first-stage F-statistic / theoretical reason for correlation with endogenous predictor]. It satisfies the exclusion restriction because [theoretical argument for why instrument affects outcome only through predictor]. In the first stage, [endogenous predictor] is regressed on [instrument], [exogenous controls], and [fixed effects]. The first-stage F-statistic is [value], exceeding the Stock-Yogo threshold, indicating that [instrument] is not weak. In the second stage, [outcome] is regressed on the predicted [endogenous predictor] and the same controls. Standard errors are [robust / clustered] to account for [error structure].
```

**线性概率模型（LPM）+ 2SLS 变体**（二元 DV 且需固定效应时）：
```text
Because the dependent variable is binary, one might consider Logit or Probit. However, when using 2SLS with fixed effects, the linear probability model (LPM) is often preferred because coefficients are directly interpretable as probability changes and computational tractability is preserved. We therefore estimate LPM with 2SLS for the main analyses and report Probit/Logit IV only as robustness. The specification includes [fixed effects] to absorb [unobserved heterogeneity]. Standard errors are clustered at the [level] to account for [dependence structure].
```

**事件研究 GLM 变体**（CAR 为 DV 时）：
```text
Because [CAR/abnormal response] is continuous but subject to nonconstant error variance, we estimate generalized linear models (GLM) rather than ordinary least squares. GLMs are robust to nonconstant error variance and relaxed distributional assumptions. Expected returns are estimated over [estimation window] using [factor model]; abnormal returns are observed returns minus expected returns. We aggregate abnormal returns over [event window] to allow for [information leakage/dissemination].
```

**动态面板/GMM 变体**：
```text
Because [dependent variable] is persistent and our panel is [short / has few time periods], fixed-effects estimation may be biased (Nickell bias). We therefore estimate a dynamic panel model using [system GMM / difference GMM] with [lag structure] as instruments. We collapse the instrument matrix to avoid instrument proliferation and report [Hansen J-test / Sargan test] for overidentification ([value], p = [value]) and the [AR(2)] test for second-order serial correlation ([value], p = [value]). We treat [lags] as predetermined and [further lags] as instruments. The number of instruments is [N], which is [less than / approximately equal to] the number of groups, satisfying the rule of thumb that instruments should not exceed groups.
```

**匹配DiD/广义DiD 变体**：
```text
We estimate a generalized difference-in-differences model using [matching estimator: nearest-neighbor / kernel / inverse probability weighting] to construct a credible counterfactual. Matching is performed on [covariates] using [propensity score / Mahalanobis distance] within [strata / caliper]. After matching, we estimate [outcome] on [treatment], [time], [treatment × time], controls, and [fixed effects] using the matched sample. Identification comes from comparing [treated units] to [matched control units] before and after [event]. We cluster standard errors at [level] to account for [dependence structure].
```

**堆叠扩散Logit 变体**：
```text
Because [outcome] is a binary adoption decision observed across multiple [entities / markets / practices] and time, we estimate a conditional (fixed-effects) logit model in a stacked structure. Each stack corresponds to [entity-practice-time triplet / adoption event], and the dependent variable equals one if [adoption occurred]. The stacked structure accounts for [unobserved heterogeneity] by including [fixed effects: entity / practice / time] while allowing [predictors] to vary across [dimensions]. We cluster standard errors at [entity] level to account for repeated observations within [entity].
```

**PSM匹配面板 + 随机效应Tobit 变体**：
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

**实验变体**：
```text
Participants were randomly assigned to one of [N] conditions and then completed [task/measures]. We used [model/test] to analyze [outcome] because [outcome form/design logic].
```

---

### M8. 识别策略 / 效度 / 诊断检验

**通用填空段落**：

```text
To address concerns about [threat], we [design feature/test]. This check assesses whether [assumption] is plausible. We report the results in [Results/Table/Appendix]. Although [assumption] cannot be directly tested, the evidence below helps reduce concerns about [threat].
```

**自然实验/DiD 变体**：
```text
Our identification strategy relies on [source of variation]. [Shock/event/policy] creates variation in [treatment] that is plausibly exogenous to [outcome] because [reason]. The key identifying assumption is that [treated and control units] would have followed similar trends absent [treatment]. We assess this assumption in the Results section using [event-study/leads-lags] specifications. We first estimate a parsimonious specification because [controls] may be affected by [treatment].
```

**DiD 置换检验预览补充**（可选，置于自然实验/DiD 变体后）：
```text
We also conduct permutation tests by randomly assigning [treatment status/timing] across [N] iterations to assess whether [unobserved characteristics] could drive our results.
```

**内生性/控制函数变体**：
```text
Because [timing/choice] may be endogenously chosen in the [outcome] model, we use a control-function approach: first estimate [timing model], then include the first-stage residual in the [outcome model]. [Variable] identifies the first stage because it should affect [timing] but not [second-stage outcome], since [theoretical reason].
```

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

**同伴效应/网络效应 falsification 变体**：
```text
Because [network-based construct] may capture common shocks or sorting rather than true peer influence, we conduct falsification tests. We re-estimate our models using [placebo network: random peers / future peers / peers from unrelated network layer] as the independent variable. If the main effect is driven by common shocks, the placebo network should also yield a significant coefficient. The coefficient on [placebo network] is [not significant / opposite direction / much smaller], suggesting that the [focal network] effect is not an artifact of [common shock / sorting]. We also test [alternative mechanism] by [test description]; the result is [status], further distinguishing [theorized mechanism] from [alternative].
```

**匹配DiD 平行趋势与重叠支撑变体**：
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

## 按设计类型一键生成示例

### 示例：面板数据 / OLS

**输入**：`/write-methods 面板数据/OLS --hypotheses="H1: DT -> Routine updating; H2: Routine updating -> Innovation" --journal=SMJ`

**输出骨架**（用户应直接复制以下段落，替换方括号内容）：

```text
We focus on [U.S. publicly traded manufacturing firms] for three reasons. First, [manufacturing industries have experienced substantial digital transformation pressures], providing sufficient variation in our key independent variable. Second, [publicly traded firms are required to disclose IT expenditure data], enabling reliable measurement of [digital transformation]. Third, [manufacturing firms' innovation outcomes are well-documented in patent databases], allowing us to construct a comprehensive measure of [innovation performance]. The unit of analysis is [firm-year].

We began with [all publicly traded manufacturing firms] from [Compustat North America] over [2010–2020]. We matched these observations to [Harte-Hanks CI Technology Database] to obtain [IT expenditure data] and to [NBER Patent Database] to obtain [patent filings]. We excluded [financial firms (SIC 6000–6999) and utilities (SIC 4900–4999)] because [their regulatory environments and accounting practices differ substantially from manufacturing firms]. We also excluded firms with fewer than [three] years of consecutive data to ensure sufficient within-firm variation for fixed-effects estimation. The final sample consists of [X] [firm-year observations] from [Y] [unique firms].

Our dependent variable is [firm innovation performance], measured as [the natural logarithm of one plus the number of patents filed by the firm in a given year, scaled by R&D expenditure] using [NBER Patent Database]. This measure captures both the quantity and efficiency of innovation output because [patent count correlates highly with other innovation indicators]. Higher values indicate [greater innovation efficiency].

Our focal independent variable, [digital transformation intensity], is measured as [IT expenditure divided by total assets] based on [Compustat item X]. This variable corresponds to Hypothesis 1 because it captures [the firm's relative investment in digital technologies]. We present the focal variables in the order of the theory: [digital transformation intensity], [organizational routine updating], and [absorptive capacity].

To capture [the moderating role of absorptive capacity], we measure [absorptive capacity] as [R&D intensity / patent citations / knowledge stock measure]. We interact [digital transformation] with [absorptive capacity] to test whether [the effect of digital transformation on innovation performance] is stronger when [absorptive capacity] is high.

We include controls for [firm resources and baseline heterogeneity] because [larger and older firms may have more resources for both digital transformation and innovation]. At the [firm] level, we control for [firm size (ln total assets), firm age, profitability (ROA), leverage (total debt / total assets), and industry competition (Herfindahl-Hirschman Index)]. We also include [firm and year fixed effects] to absorb [time-invariant unobserved firm characteristics and common macroeconomic shocks]. All time-varying predictors are measured at [t–1] to preserve temporal ordering.

Because [firm innovation performance] is [continuous], we estimate [fixed-effects panel regression models]. The specification includes [firm and year fixed effects] to absorb [unobserved heterogeneity and common shocks]. Standard errors are clustered at the [firm] level to account for [serial correlation within firms over time]. We employ firm fixed effects rather than random effects because the Hausman test rejects the random-effects assumption (χ² = [value], p < 0.01). We conduct several diagnostic tests. First, the Variance Inflation Factor (VIF) for all independent variables is below [value], well below the conventional threshold of 10. Second, the Wooldridge test rejects autocorrelation in the residuals (F = [value], p = [value]).

To address concerns about [reverse causality], we lag [digital transformation intensity] by [one year] and re-estimate our models. This check assesses whether [simultaneity] is a plausible threat. We report the results in [the robustness section of the Results].

The Results section first reports [the main hypothesis tests in Table 2] and then examines [robustness checks in Table 3]. Because [our models involve panel data with fixed effects], we address [remaining endogeneity concerns] in supplemental analyses using [instrumental variables].
```

---

## 下游接口

- `/write-results` — 使用本骨架的变量名、模型规格和 M10 预告作为 Results 报告的基准
- `/paper-review` — 进行 Theory-Methods 假设-变量映射对齐检查
- `/methods-review` — 如用户已有 Methods 草稿，使用本骨架作为理想基准对比审查
- `/distill-methods-exemplar` — 对生成后的 Methods 段落进行反向蒸馏审查，检查槽位覆盖、DNA 指标、可迁移性和因果语言合规性。审查结果作为 Vault 参考注释，不自动修改本 skill 的骨架库

## 常见反模式

以下错误在 Methods 中高频出现，生成段落前主动排查：

- **模型选择无文字解释**：只写 "we estimate FE model" 而不解释为什么 FE 优于 RE/OLS，或为什么选此 estimator
- **控制变量无 because**：列出 Size, Age, ROA 但不解释每个变量控制的是什么竞争性解释
- **因果语言越级**：面板数据 design 下使用 "caused" "led to" 等强因果词；自然实验未通过平行趋势检验就用 "effect of... on..."
- **样本漏斗缺数字**：写 "we exclude missing values" 但不报告每一步损失了多少观测
- **识别策略后置或缺失**：DiD/IV/自然实验不把识别假设和检验放在核心位置，而是 buried 在脚注或附录
- **交互/非线性模型无解释策略**：加入 interaction/nonlinear term 后未预告如何在 Results 中解释（marginal effects / simple slopes / AME）
- **时间顺序模糊**：未明确说明预测变量是 t-1 还是 contemporaneous，或事件窗口的起止逻辑
- **Bad Control 问题**：在 DiD/自然实验中控制了 post-treatment 变量或 collider
- **设计排他性混淆**：把 IV 的语言习惯（"effect of X on Y"）套用到 OLS/FE 设计；把实验的操纵检验语言套用到档案数据
- **动态面板 FE 陷阱**：为短面板推荐固定效应而不提示 Nickell bias 或提供 GMM 替代方案
- **过度泛化诊断要求**：为非 IV 设计要求排他性约束检验，为非 DiD 设计要求平行趋势检验，为非匹配设计要求重叠支撑检验
- **机构/政策名残留**：用户填入的 [placeholder] 中混入了论文特有的机构名、政策名、数据库名，导致段落不可迁移到其他情境

## 诚实边界

本 skill 基于 28 篇 MVP30 范文语料库（2012–2025）提炼，存在以下局限：

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
- [ ] M3：因变量有构念定义 + 操作化 + 测量来源 + 方向解释
- [ ] M4：每假设一段，含 Hypothesis 编号对齐，变量按理论顺序排列
- [ ] M5：调节/中介/机制变量有操作化和交互项说明
- [ ] M6：每个控制变量都有 because [rival explanation]
- [ ] M7：estimator + fixed effects + SE clustering + 选择理由（文字+诊断）
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

### DNA Metrics（与顶刊范本的 rhetorical 距离）
- [ ] **Because 密度**：M6 中每个控制变量都有 "because [rival explanation]" 或等效逻辑（目标：>=40%；MVP30 顶刊中位数约 35%，AMJ 可低至 0%，JM/ASQ 约 25-30%）
- [ ] **假设对齐密度**：M4/M5 中每预测变量都明确提及对应的 Hypothesis 编号（目标：>=85%；MVP30 中位数约 80%）
- [ ] **因果语言强度**：面板数据用 "associated with"；自然实验在识别支持后用 "effect of... on..."；实验可用 "caused"。无越级。
- [ ] **诊断检验前置比例**：IV/DiD/实验 目标 ≥80%（平行趋势/操纵检验/F-statistic 必须在 Methods 预告）；OLS/FE 目标 ≥30%（VIF/Hausman 可省略或脚注处理）
- [ ] **样本数字审计链**：M2 中起始 N → 每步排除（含数字）→ 最终 N 完整无缺（目标：100%）
- [ ] **时点标记密度**：所有预测变量明确标注 t-1 / contemporaneous / event window；所有时间范围有起止年份（目标：>=85%；MVP30 中位数约 85%）
- [ ] **功能定位密度**：每段首句说明本段做什么（如 "We include controls for..." / "To address concerns about..."）（目标：≥70%）

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
- 因果语言强度必须与 design strength 匹配：面板数据用 "associated with"；自然实验在识别支持后用 "effect of... on..."；实验可用 "caused"。
- 不要报告支持状态在 Methods 中。
- 不要把模型选择埋在方程里而没有文字解释。

## 外部资产位置

如需查询特定范文的具体措辞或设计变体：

- **叙事分析索引**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/_mvp30_methods_results_index.md`
- **28篇覆盖矩阵**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/deep_distillation/_methods_results_28_paper_coverage_matrix.md`
- **逐论文精细解构**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/fine_grained/batch_*/[paper]_fine_methods_results.md`
- **Pollock Ch07 表达库**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/fine_grained/_four_paper_expression_corpus_pollock_ch07.md`

---
*基于 28 篇 MVP30 范文语料库、Pollock 2025 Ch07 和深度叙事分析框架构建。版本 2.5.0 — 填空式模板。*
