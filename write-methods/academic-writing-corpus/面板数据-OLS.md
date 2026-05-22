---
design_type: 面板数据-OLS
status: VERIFIED
source_papers:
- darby2023_ceo_stock_ownership_recall_timing_msom
- darby2025_activist_investors_supply_chain_failures
- darby2026_faster_recalls_large_institutional_ownership
- eilert2017_recall_timing_stock_market
- test2026 (AMJ)
variants_count: 16
created: 2026-05-18
updated: '2026-05-22'
---


# 面板数据-OLS — Methods 骨架

## 设计特征摘要

<!-- 由 distill-methods-exemplar 首次蒸馏后填充 -->

## M1. 研究情境 / 实证背景

### 主骨架（通用）
： ⭐ PREMIUM（28/28 篇范文使用，跨所有模型类型复现）

```text
[Empirical setting] provides an appropriate context for examining [theoretical relationship] for three reasons. First, [setting property] makes [mechanism] observable. Second, [scope condition] reduces [confound]. Third, [data feature] allows us to observe [unit/process] over [period]. The unit of analysis is [unit], which aligns with our theorizing about [mechanism].
```

---

## M2. 数据来源与样本漏斗

### 主骨架（通用）
：

```text
We began with [starting population] from [source] over [period]. We matched these observations to [additional sources] to obtain [variables]. We excluded [cases] because [comparability/measurement/identification reason]. The final sample consists of [N] [units] observed over [period], with [unit] as the unit of analysis.
```

### 变体 1: 多源匹配型（数据源交叉逻辑）
： ✓ STANDARD（当使用3+个独立数据源，匹配逻辑比排除步骤更重要时）

```text
Our data come from [N] sources. [Source A] provides [data type A: e.g., recall date, firm name, recall description text] for [scope]. [Source B] provides [data type B: e.g., firm financial data, stock returns] for [scope]. [Source C] provides [data type C: e.g., CEO compensation and demographics] for [scope]. [Source D] provides [data type D: e.g., board composition] for [scope]. [Source E] provides [data type E: e.g., press releases, media articles] for [scope].

We matched [source A] to [source B] using [matching key: firm name / ticker / CUSIP / GVKEY] and [matching procedure: e.g., fuzzy name matching with manual verification]. We then matched these observations to [source C] to obtain [variables]. Because there is no common identifier between [source C] and [source D], we [manual matching procedure: e.g., manually matched brands to corresponding parent firms / used firm name and year]. [Optional: For companies present in source X but absent in source Y, we manually collected data from proxy statements filed with the SEC.] [Optional: We sought data directly from agency through the Freedom of Information Act regarding variable.]

The intersection of these data sources leads to a sample of [N] [phenomenon] across [N] [higher-level units] from [year_start] to [year_end]. [Optional: We also excluded cases because reason, resulting in a final sample of N units.] The unit of analysis is [unit].
```

**设计变体**：
- **标准多源匹配模式**（如 JOM Malik2025）：FDA→Compustat→Execucomp→BoardEx→Factiva→FOIA，逐源说明+匹配键+最终样本。
- **档案+外部评级模式**（如 JM Eilert2017）：NHTSA+Consumer Reports+Ward's+Annual Reports+Compustat，按变量来源组织而非按匹配顺序。
- **交集匹配模式**（如 POMS Mayo2023）：多个标准数据库交集，强调"The intersection of these data sources leads to..."
- **FOIA/一手数据补充模式**：标准数据库+FOIA请求/手工收集，需说明非公开数据的获取方式和覆盖范围。
- **诚实边界**：若起始N无法精确确定（如FOIA获得的一手数据），应在Limitations中说明。多源匹配型不替代样本排除审计，而是在匹配逻辑复杂时优先呈现数据源交叉，排除步骤可简化或后置。

---

## M3. 因变量

### 主骨架（通用）
：

```text
Our dependent variable is [outcome construct], measured as [operational definition] using [source]. This measure captures [construct] because [construct-validity logic]. Higher values indicate [interpretation direction]. Because [outcome] is [continuous/binary/ordinal/count/censored/time-to-event], we use [model] and interpret [coefficients/marginal effects/hazards/probabilities].
```

### 变体 1: 指数/净指数变体
： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M3 段落

```text
Because the theory concerns both [positive actions] and mitigation of [negative actions], we construct [net outcome] from [strengths] and [concerns]. For each [category-year], we divide the number of [items] by the maximum possible number in each [category-year] to account for changes in measurement coverage. The net index subtracts [negative index] from [positive index] and sums across [categories].
```

### 变体 2: 构念构建型（因变量多步构建）
： ✓ STANDARD（当 DV 需从原始文本/档案痕迹提取时）

```text
Our dependent variable is [outcome construct]. Because [construct] is not directly available in [standard databases], we construct it from [raw trace/source] in [N] steps. First, we [acquisition step: e.g., downloaded all press releases from Factiva for the sample period / obtained all available 10-K filings for all years of the study period]. Second, we [processing step: e.g., parsed text, sources, and dates into separate columns using a custom R program / searched for the presence of the word "recall" in each 10-K and reviewed all 10-Ks that contained the word to match against the recalls within our data set]. Third, we [coding/operationalization step: e.g., had two coders independently review flagged press releases and reach consensus on whether they mentioned product recalls; differences were less than 1% of cases / designated the recall as Low Discretion if mentioned in any 10-K filing, and High Discretion otherwise]. We operationalized [construct] as [final measure: e.g., a binary variable equal to 1 if the firm did not mention the recalled product in its press releases within 30 days after recall initiation, and 0 otherwise]. This measure captures [construct] because [construct-validity logic]. We assess the reliability of this coding by [inter-coder agreement / match rate], which was [value]. As a robustness check, we [alternative operationalization: e.g., widened the window to 60 days] and obtained [consistent/qualitatively similar] results. Because [outcome] is [continuous/binary/ordinal/count/censored/time-to-event], we use [model] and interpret [coefficients/marginal effects/hazards/probabilities].
```

**设计变体**：
- **文本/档案痕迹编码型**（如 JOM Strategic Silence, POMS Discretion）：原始痕迹获取 → 解析/清洗 → 匹配/编码 → 效度检验（双人编码一致性 / 匹配率）。
- **PCA/指标聚合型**（如 JM Problem Severity, JM Brand Reliability）：多指标获取 → 主成分分析 / 时间平均 → 单变量得分 → 方向解释。
- **分类/阈值判别型**（如 POMS Discretion 的 SEC 披露编码）：原始痕迹获取 → 搜索/匹配 → 二元分类（披露 vs 未披露）→ 分类效度论证。

---

## M4. 自变量 / 核心预测变量

### 主骨架（通用）
：

```text
Our focal independent variable, [predictor name], is measured as [operation] based on [source/timing]. This variable corresponds to Hypothesis [x] because it captures [mechanism]. We present the focal variables in the order of the theory: [predictor A], [predictor B], and [moderator].
```

### 变体 1: 竞争机制预测变量变体
（机制测试中分解核心构念时）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M4 段落

```text
To test how [actors] resolve [uncertainty], we decompose [core construct] into [N] subgroups based on [criterion]: [variable 1], [variable 2], [variable 3], and [variable 4]. We restrict the mechanism test subsample to [criteria] to ensure sufficient variation across the subgroups. These variables correspond to [RQ/Prediction x] because they distinguish [mechanism A] versus [mechanism B].
```

### 变体 2: 网络/组合/配对构念变体
：

```text
We define [focal construct] as occurring when [actor] simultaneously holds/links/participates in [two or more related units]. The pair-level measure captures [shared influence/exposure] between the focal unit and each same-category peer. The numerator sums [shared holdings/links/exposure]; the denominator adds [non-focal holdings/relationships] so the measure reflects [focal actor influence] relative to [other actors]. We aggregate the pair-level measure across all same-category peers to form a continuous focal-unit measure. We require [minimum stake/link/intensity] so that the focal actor has sufficient incentive and ability to influence [unit].
```

### 变体 3: 构造暴露/指数变体
（用于堆叠扩散或媒体暴露）：

```text
We construct [focal exposure] from [raw trace] by [aggregation rule]. The measure equals [formula: count / proportion / intensity] of [event/type] per [unit-time]. To account for [scale differences / coverage variation], we normalize by [denominator]. We require [minimum threshold] to ensure that [spurious zeros / noise] do not drive the results.
```

### 变体 4: 构念构建型（自变量多步构建）
： ✓ STANDARD（当核心预测变量需从原始文本/档案痕迹提取时）

```text
Our focal independent variable, [predictor name], is not available in standard databases, so we construct it from [raw trace/source]. The construction proceeds in [N] steps. First, we [acquisition step: e.g., collected data on the number of (1) consumer complaints, (2) crashes or fires, (3) injuries, and (4) fatalities from NHTSA / obtained all available 10-K filings for all years of the study period]. Second, we [processing/aggregation step: e.g., performed principal component analysis on these four items to generate a univariate score / searched for the presence of the word "recall" in each 10-K and reviewed all 10-Ks that contained the word to match against the recalls within our data set]. Higher scores on this component reflect [interpretation direction]. This variable corresponds to Hypothesis [x] because it captures [mechanism]. We validate this measure by [face-validity / convergent-validity check], showing that [correlation / pattern with external benchmark]. We also examine [alternative operationalization] as a robustness check.
```

**设计变体**：
- **PCA/指标聚合型**（如 JM Problem Severity）：多指标获取 → 主成分分析 → 单变量得分 → 方向解释。需报告 KMO / 累计方差贡献率。
- **文本/档案编码型**（如 POMS Discretion）：原始痕迹获取 → 搜索/匹配 → 编码分类 → 编码效度检验。
- **外部数据映射型**（如 JM Brand Reliability）：外部评级数据获取 → 时间平均 / 跨模型聚合 → 品牌层级映射 → 方向解释。

---

## M5. 调节/中介/机制变量

### 主骨架（通用）
：

```text
To capture [boundary/mechanism], we measure [moderator/mediator] as [operation]. We interact [predictor] with [moderator] to test whether [relationship] is stronger/weaker under [condition]. To test the proposed mechanism, we measured [mediator] and included [alternative mechanisms] as rival explanations.
```

### 变体 1: 子样本分割变体
（用样本分割而非交互项检验调节时）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M5 段落

```text
To capture the boundary condition of [moderator], we measure [moderator] using [classification]. We split the sample by [moderator] into [category A] and [category B] to test whether [relationship] differs across [categories], rather than including an interaction term, because [reason: small sample within categories / theoretical focus on distinct regimes].
```

### 变体 2: 行为者类型分解变体
：

```text
To test the proposed mechanism, we decompose [predictor] by [actor type/horizon]. [Type A] and [Type B] capture actors expected to have [theory-relevant orientation], whereas [Type C] captures a comparison group. We map [classification data] onto [focal source] and construct separate measures for [type A], [type B], and [type C].
```

### 变体 3: 边界条件验证变体
：

```text
We define [boundary condition] as contexts where [spillovers/externalities/stakeholder responses] are likely to be economically meaningful. We validate this classification using [external source A] for [dimension A] and [external source B] for [dimension B].
```

### 变体 4: 间接调节（ mediated moderation ）变体
： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：通用 M5 段落

```text
To test the indirect moderation model, we specify a system of equations. Equation (2) captures the moderating effect of [moderator 1] on the [predictor-outcome] relationship: [outcome] = β₁₀ + β₁₁[predictor] + β₁₂[moderator 1] + β₁₃[predictor × moderator 1] + ε₁. Equation (3) captures the moderating effect of [moderator 2]: [outcome] = β₂₀ + β₂₁[predictor] + β₂₂[moderator 2] + β₂₃[predictor × moderator 2] + ε₂. Equation (4) models the relationship between [moderator 1] and [mediator]: [mediator] = β₃₀ + β₃₁[moderator 1] + ε₃. Equation (5) represents the full system with both moderators: [outcome] = β₄₀ + β₄₁[predictor] + β₄₂[moderator 1] + β₄₃[predictor × moderator 1] + β₄₄[mediator] + β₄₅[predictor × mediator] + ε₄.

We test for full indirect moderation through [mediator] according to whether: (1) [moderator 1] functions as a moderator when [mediator] is not considered (β₁₃ ≠ 0); (2) [moderator 1] influences [mediator] (β₃₁ ≠ 0); (3) [mediator] moderates the effect of [predictor] on [outcome] (β₄₅ ≠ 0); and (4) the coefficient on the original interaction term in the full system (β₄₃) indicates the pattern of mediation—β₄₃ = 0 indicates full indirect moderation (the direct moderating effect of [moderator 1] becomes nonsignificant in the presence of [mediator]), whereas β₄₃ ≠ 0 and |β₄₃| < |β₁₃| indicates partial indirect moderation.
```

---

## M6. 控制变量与竞争性解释

### 主骨架（通用）
：

```text
We include controls for [threat family 1] because [alternative explanation 1]. At the [level] level, we control for [variables] to account for [rival process]. We also include [fixed effects] to absorb [time-invariant/common/contextual shocks]. All time-varying predictors are measured at [lag/timing] to preserve temporal ordering. We lag the control variables by [period] to reduce simultaneity concerns.
```

### 变体 1: 控制变量表格呈现型（多层级/多方程）
： ✓ STANDARD（当控制变量≥10个、跨多层级，或涉及多方程时）

```text
Because the set of control variables is extensive, we present them in [Table X] rather than in the main text. The table is organized by [analytical level / equation assignment] to facilitate readability and cross-reference with the model specification. For each variable, the table reports the variable name, operational definition, the theoretical factor it addresses, and supporting citations.

[Table X about here]

**Notes to Table X.** [Level 1] characteristics describe [scope] and may influence [DV] through [mechanism] ([citation]). [Level 2] characteristics capture [scope]; each variable is intended to control for [aspect] that may influence [DV] ([citation]). To control for skewed distributions and to aid interpretability, we [transform: log-transform / center / standardize] all [type] variables, except [exceptions]. All time-varying predictors are measured at [lag/timing] to preserve temporal ordering. [Fixed effects] are included in every model to absorb [unobserved heterogeneity].
```

**设计变体**：
- **多层级分组模式**（如 POMS 范文：Industry / Firm / CEO）：表格行按分析层级分组；列使用 "Potential factor of influence" 承载 because 逻辑。
- **多方程映射模式**（如 JM 2015 范文）：表格列使用 "Purpose" + "Appears in Equation(s)" + "Data Set" + "Supporting Literature"，适用于同时方程/SEM 设计。
- 表格呈现不替代 because 逻辑，只是将其压缩为列内容或 Notes。若控制变量数量中等（5–10个），建议保留主骨架的段落式 because 结构。

---

## M7. 模型规格与估计方法

### 主骨架（通用）
：

```text
Because [dependent variable] is [continuous/binary/ordinal/count/censored/time-to-event], we estimate [model]. The specification includes [fixed effects] to absorb [unobserved heterogeneity/common shocks]. Standard errors are clustered at [level] to account for [within-unit dependence]. We use [estimator] for [hypotheses] because [outcome/design logic]. We also considered [alternative estimator]; results using this approach are reported as [robustness/supplement].
```

### 主骨架（通用）
（按需添加）： ✓ STANDARD（15+/28 篇范文使用）

```text
We employ [unit] fixed effects rather than random effects because the Hausman test rejects the random-effects assumption (χ² = [value], p < 0.01), indicating that unobserved [unit]-specific factors are correlated with our independent variables. [Year] fixed effects control for temporal trends such as [macroeconomic shocks/industry-wide shifts].
```

### 主骨架（通用）
：

```text
We conduct several diagnostic tests. First, the Variance Inflation Factor (VIF) for all independent variables is below [value], well below the conventional threshold of 10, indicating that multicollinearity is not a concern. Second, the [Wooldridge/modified Wald] test indicates [presence/absence] of [autocorrelation/heteroskedasticity], and we report [robust/clustered] standard errors accordingly.
```

### 主骨架（通用）
：
当模型同时涉及非线性 DV 和工具变量时（如 Zhou 2017 ASQ），建议按以下顺序拼接：
1. 先报告 estimator-DV 匹配逻辑（Tobit 处理 censored / Poisson 处理 count）；
2. 再报告 IV 必要性与工具变量合理性；
3. 最后说明 second-stage 的解释策略（marginal effects / turning points / count effects）。
first-stage 统计量可置于 M7 正文、表格脚注或 R1 诊断段，取决于识别策略在论文中的核心程度。若 first-stage 仅作为诊断而非展示重点（如 ASQ 常见做法），建议在 M7 中仅简要提及"first-stage F 超过 Stock-Yogo 阈值"，将具体数值放入表格脚注。

**混合效应（within-between 分解）变体**：

```text
To disentangle the within-[unit] and between-[unit] effects of [predictor], we estimate mixed-effects models that decompose [predictor] into two components: [predictor]_{within}, which captures deviations from each [unit]'s mean over time, and [predictor]_{between}, which captures each [unit]'s time-invariant average. The within-effect answers whether [predictor] changes within the same [unit] are associated with [outcome] changes. The between-effect answers whether [units] with higher average [predictor] exhibit systematically different [outcome]. We include [random effects] to account for [unit]-level unobserved heterogeneity and [fixed effects] to absorb [time/common shocks].
```

### 变体 1: HLM/多层模型变体
（当数据为嵌套结构，如员工-团队-公司，或重复测量-个体时）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M7 段落 + 说明聚类标准误

```text
Because observations are nested within [level-2 unit, e.g., firms / teams / individuals], we estimate a hierarchical linear model (HLM) with random intercepts at the [level-2] level. The intraclass correlation (ICC) is [value], indicating that [percentage]% of the variance in [outcome] resides between [level-2 units], justifying the use of multilevel modeling. We include [predictor] at [level-1 / level-2 / both levels] and test cross-level interactions (e.g., [level-2 predictor] × [level-1 predictor]). Random slopes for [predictor] are included when the likelihood-ratio test favors their inclusion (χ² = [value], p [relation] [threshold]). We center [level-1 predictor] at the [group mean / grand mean] to facilitate interpretation of [main effects / cross-level interactions]. Standard errors are robust to [heteroskedasticity / clustering] at the [level] level.
```

### 变体 2: 方法选择诊断（简单 vs 复杂估计器）
： ✓ STANDARD（当需在 OLS/FE/SUR 与 IV/3SLS/GMM 之间做选择时）

```text
Because our model involves [endogeneity concern: omitted variables / simultaneity / reverse causality], we must choose between [simple estimator] and [complex estimator]. We follow the established procedure of estimating both and selecting the preferred estimator based on [diagnostic test]. First, we estimate the model using [simple estimator]. Second, we estimate the model using [complex estimator] with [instrument specification / additional assumptions]. We then apply the [Durbin-Wu-Hausman / Hausman / Sargan-Hansen] test to compare the two estimators. The [nonsignificant / significant] test statistic (χ² = [value], p [relation] [threshold]) indicates that [simple estimator] is [preferred / rejected] and [complex estimator] does [not] provide efficiency gains [or is / is not necessary to address endogeneity]. We report the [simple / complex] estimator as our preferred specification. As a robustness check, we also report results using the [alternative estimator] in [location].
```

**设计变体**：
- **FE vs RE 选择模式**（已有主骨架，Hausman test）：适用于面板数据内生性检验。
- **OLS vs IV 选择模式**（DWH test）：适用于横截面/面板数据中潜在遗漏变量导致内生性。
- **滞后阶数选择模式**（如 JM 2015 Malshe）：比较 t-1 / t-2 / t-3 滞后，用 AIC/BIC 选择最优滞后阶数。
- **动态面板 FE vs GMM 选择模式**：当 T < 10 且因变量具有持续性时，FE 存在 Nickell bias，需用系统 GMM / 差分 GMM。用 AR(2) 检验和 Hansen J 检验判断 GMM 的有效性。
- **诚实边界**：方法选择诊断是"用数据说话"，但需在 Theory 中预先说明为什么内生性是合理关切。不要在 Methods 中首次引入内生性顾虑。

---

## M8. 识别策略 / 效度 / 诊断检验

### 主骨架（通用）
：

```text
To address concerns about [threat], we [design feature/test]. This check assesses whether [assumption] is plausible. We report the results in [Results/Table/Appendix]. Although [assumption] cannot be directly tested, the evidence below helps reduce concerns about [threat].
```

### 变体 1: 内生性/控制函数变体
： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：M8 通用段落

```text
Because [timing/choice] may be endogenously chosen in the [outcome] model, we use a control-function approach: first estimate [timing model], then include the first-stage residual in the [outcome model]. [Variable] identifies the first stage because it should affect [timing] but not [second-stage outcome], since [theoretical reason].
```

---

## M10. Methods 到 Results 的过渡

### 主骨架（通用）
：

```text
The Results section first reports [main tests] and then examines [validity/robustness checks]. Because [measure/design] raises [concern], we address this issue in supplemental analyses using [test]. The model requires interpreting [marginal effects/predicted values], which we report after the coefficient estimates. We assess the plausibility of [identification assumption] through [event-study/placebo/diagnostic] tests.
```

---

## 累积变体

### 变体 1: 控制变量分层 because 结构 (4/4 复现)
**来源论文**: Darby2026 JOM / Darby2025 JSCM / Eilert2017 JM / Darby2023 MSOM
**验证状态**: 通过
**写入日期**: 2026-05-19
**更新日期**: 2026-05-20 (新增 Darby2023 MSOM 复现)
**槽位**: M6
**骨架**:
> We included a broad set of control variables that influence [DV] directly and those that help address alternative explanations ([methodology_citation]); in our case, variables correlated with [IV] that may also influence [DV]. We first included [level_1]_level factors that may influence how [DV] is handled. To address alternative explanations stemming from [concern_1], we included [control_1], measured as [definition] ([citation]), and [control_2], measured as [definition] ([citation]). [IV]_related_rationale: [actor] may be sensitive to [outcome] ([citation]), so it is important to control for [related_factor] as well as the scale and scope of a particular [phenomenon].
>
> We also controlled for [level_2]_level characteristics that have been shown to influence [DV] using data from [source]. In doing so, we aimed to address alternative explanations related to [concern_3] and [concern_4], which are important [theory] considerations for [actor] ([citation]). [control_4] was measured as [definition] ([citation]).
>
> [Actor_type] can influence both [IV] and [DV], so [number] [actor_type] characteristics were controlled for. [Control_7] was measured as [definition] ([citation]). [Control_8] was measured as [definition] ([citation]).
>
> Lastly, we included firm and year fixed effects to account for [time_varying_concerns] as well as [time_invariant_concerns] ([citation]).
**与原骨架差异**: 这是面板数据控制变量的**黄金标准结构**。关键要素：(1) 总起句锚定方法论引用(如Shang & Rönkkö 2022)；(2) 按分析层级递进呈现；(3) 每个变量有显式because逻辑；(4) 过渡句衔接各层级("We also...", "Beyond...", "Lastly...")。because密度目标：>=60%为优秀。4/4复现确认此为产品召回研究**必写模块**。

### 变体 2: 样本交集漏斗 (3/4 复现)
**来源论文**: Darby2026 JOM / Darby2025 JSCM / Darby2023 MSOM
**验证状态**: 通过
**写入日期**: 2026-05-19
**更新日期**: 2026-05-20 (新增 Darby2023 MSOM 复现)
**槽位**: M2
**骨架**:
> The intersection of these datasets resulted in a sample of [N] [phenomenon] across [N] firms from [year_start] to [year_end].
**与原骨架差异**: 产品召回论文的**常见缺陷**——缺少起始N到最终N的逐层排除audit trail。理想写法应补充："Of the [N] initial observations, [N] were excluded due to [reason_1], [N] due to [reason_2], resulting in a final sample of [N]."
**诚实边界**: 若数据为FOIA请求获得的一手数据，起始N可能无法精确确定，需在Limitations中说明。

### 变体 3: IV 选择三层 because 论证链
**来源论文**: Darby2023 MSOM
**验证状态**: 可选变体 (1/4，但生成力极高)
**写入日期**: 2026-05-20
**槽位**: M4
**骨架**:
> We used [IV] as our primary measure because it is a broad, comprehensive measure that reflects the [number] related, but distinct, mechanisms we theorized about in [Hypothesis]—[mechanism_1], [mechanism_2], and [mechanism_3]. First, [theoretical_rationale_1] ([citation]), and research indicates that [IV] is one of the most effective tools to do so ([citation]). Second, research suggests that [IV_property_2] ([citation]). Third, [IV_property_3] ([citation]). Overall, prior studies conclude that [IV] is key to understanding [theoretical_consequence] ([citation]), which is why we use it as our primary measure, although we examine alternative measures in [location].
**与原骨架差异**: 一般论文在M4中简单报告"We measure X as Y"，而此骨架构建了从构念→操作化→多机制映射的完整论证链。适用于任何**单一操作化同时代理多个理论机制**的情境。关键策略：(1) 理论机制枚举（"three related, but distinct, mechanisms"）；(2) 每个机制有独立文献链；(3) 末句预告替代变量检验（"although we examine alternative measures"），建立M4→M5的叙事桥梁。

### 变体 4: Mixed-effects within/between 机制分解
**来源论文**: Darby2023 MSOM
**验证状态**: 可选变体 (1/4，机制检验设计特有)
**写入日期**: 2026-05-20
**槽位**: M5
**骨架**:
> We used mixed-effects models to explore the within-[unit] and between-[unit] effects of [IV], and the results are reported in [Table_reference]. Model ([ref]) indicates that the within-component of [IV] has a [direction] and [significance] relationship with [DV] (β = [value], p < [threshold]), whereas the between-component is [not statistically significant / opposite direction]. The results suggest that the effect of [IV] is driven by the within-component rather than the between-component. That is, it is not the difference in [IV] between [units], but, rather, a relative increase in [IV] for a given [unit] within the same [cluster] that explains [DV].
**与原骨架差异**: 这是将统计结果翻译为机制语言的核心句式。关键策略：(1) 报告within/between系数对比；(2) "it is not... but, rather..."句式将统计输出转化为理论叙事；(3) 明确指出是"个体内部变化"还是"个体间差异"驱动效应。适用于任何面板数据中需要区分个体内变化vs个体间差异的机制检验。

### 变体 5: 替代变量机制对齐矩阵
**来源论文**: Darby2023 MSOM
**验证状态**: 可选变体 (1/4，需配合 Figure 1 机制对齐图使用)
**写入日期**: 2026-05-20
**槽位**: M5
**骨架**:
> Following extant research ([citation]), we used [Primary_IV] as our primary measure because it broadly reflects [number] mechanisms: [mechanism_list]. To probe these mechanisms at a more granular level, we replicated our analyses using two alternative measures of [construct]—[Alternative_1] and [Alternative_2]. We measured [Alternative_1] as [definition]. We measured [Alternative_2] as [definition]. [Figure_reference] details each measure and its alignment with our theorized mechanisms. Both our primary measure and the alternative measures inherently reflect [shared_mechanism]. [Alternative_1] also proxies for [mechanism_A] because [rationale] ([citation]), whereas [Alternative_2] also proxies for [mechanism_B] because [rationale] ([citation]). Thus, although our primary measure is comprehensive and reflects all [number] mechanisms, the alternative measures help us examine whether, indeed, all [number] mechanisms contribute to [DV].
**与原骨架差异**: 这是**三角验证**策略在 variable construction 层面的应用。关键要素：(1) 主变量+替代变量矩阵；(2) Figure 1 机制对齐图（每个变量→哪些机制→理论基础）；(3) 部分重叠的机制映射（变量A覆盖机制1+2，变量B覆盖机制1+3，变量C覆盖机制2+3）；(4) "虽然主变量全面，但替代变量帮我们检验是否所有机制都起作用"的诚实表述。适用于任何"一个构念→多个可分离机制"的构念效度设计。
