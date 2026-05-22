---
design_type: PSM匹配面板
status: VERIFIED
source_papers:
- darby2026_faster_recalls_large_institutional_ownership
- darby2023_ceo_stock_ownership_recall_timing_msom
variants_count: 4
created: 2026-05-18
updated: '2026-05-22'
---

# PSM匹配面板 — Methods 骨架

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

### 变体 1: PSM匹配面板变体
（在通用段落中加入匹配步骤）： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：通用 M2 + M8 匹配检验

```text
To reduce selection bias, we first estimate propensity scores using [logit/probit] with [covariates] as predictors of [treatment/status]. We match [treated units] to [control units] using [method: one-to-one nearest-neighbor / kernel / caliper] matching with [calipersize] caliper on [distance metric]. After matching, the standardized bias for all covariates is below [threshold], and the [t-test / KS-test] indicates no significant difference in [covariates] between groups. The matched sample consists of [N] [unit-years / dyads / firms].
```

### 变体 2: 层级回退匹配变体
（如 Pfarrer et al. AMJ，1:3 SIC 匹配 + 层级回退）： 🔬 EXPERIMENTAL（2 篇范文：Pfarrer et al., Mayo et al.）⚠️ 保守替代：通用 M2 + PSM 变体

```text
To construct the sample, we first identified [N] [treatment group] firms that [criterion]. We then matched each [treatment group] firm with [ratio: e.g., three] firms from the same [primary matching criterion: e.g., four-digit SIC code] that were similar in [matching variables: e.g., assets, revenues, and ROA]. Where appropriate matches were not found at the [primary level], we looked at [secondary level] and [tertiary level] for similar firms. Through this process we identified [N] matching firms at the [primary level], [N] at the [secondary level], and [N] at the [tertiary level]. A t-test comparing differences in [variable] revealed no significant differences between the [treatment] and [control] companies; however, in keeping with the predictions of prior [construct] research, there were significant differences in [variables]. [Attrition description]. These characteristics suggested our sample provided a [conservative/liberal] test of our hypotheses since they result in some restriction of range to primarily [sample characteristic].
```

### 变体 3: 多源嵌套调查变体
（如 Mannor et al. SMJ，多方法数据 + 聚类标准误）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M2 + M7 多层模型/聚类标准误

```text
We used a multisource, multimethod data collection approach to test our ideas. This involved gathering data from [N] sources: [source 1: e.g., in-person interviews], [source 2: e.g., online surveys to subordinates], [source 3: e.g., hard-copy surveys to friends/family], and [source 4: e.g., archival company data]. Testing our theory required gaining access to [phenomenon], and our methodology was designed with this goal in mind. We established [N] criteria to govern recruitment: [criterion 1], [criterion 2], and [criterion 3]. We tested our hypotheses using [estimator: e.g., hierarchical linear regression]. To account for the nonindependence in our data (i.e., [nesting structure]), we specified [SE type: e.g., Huber/White/sandwich standard errors] using the [software option]. [Observations] were clustered by [clustering variable].
```

---

## M3. 因变量

### 主骨架（通用）
：

```text
Our dependent variable is [outcome construct], measured as [operational definition] using [source]. This measure captures [construct] because [construct-validity logic]. Higher values indicate [interpretation direction]. Because [outcome] is [continuous/binary/ordinal/count/censored/time-to-event], we use [model] and interpret [coefficients/marginal effects/hazards/probabilities].
```

---

## M4. 自变量 / 核心预测变量

### 主骨架（通用）
：

```text
Our focal independent variable, [predictor name], is measured as [operation] based on [source/timing]. This variable corresponds to Hypothesis [x] because it captures [mechanism]. We present the focal variables in the order of the theory: [predictor A], [predictor B], and [moderator].
```

---

## M5. 调节/中介/机制变量

### 主骨架（通用）
：

```text
To capture [boundary/mechanism], we measure [moderator/mediator] as [operation]. We interact [predictor] with [moderator] to test whether [relationship] is stronger/weaker under [condition]. To test the proposed mechanism, we measured [mediator] and included [alternative mechanisms] as rival explanations.
```

---

## M6. 控制变量与竞争性解释

### 主骨架（通用）
：

```text
We include controls for [threat family 1] because [alternative explanation 1]. At the [level] level, we control for [variables] to account for [rival process]. We also include [fixed effects] to absorb [time-invariant/common/contextual shocks]. All time-varying predictors are measured at [lag/timing] to preserve temporal ordering. We lag the control variables by [period] to reduce simultaneity concerns.
```

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

### 变体 1: PSM匹配面板 + 随机效应Tobit 变体
： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：M7 Tobit + M2 PSM

```text
After propensity-score matching (described in M2), we estimate the treatment effect using [random-effects Tobit / fractional logit / GEE] because [outcome] is [censored / fractional / non-normal] and matching does not fully eliminate [unobserved heterogeneity]. We include [random effects] to account for [unit-level unobservables] and [time fixed effects] to absorb [common shocks]. Standard errors are clustered at [level].
```

---

## M8. 识别策略 / 效度 / 诊断检验

### 主骨架（通用）
：

```text
To address concerns about [threat], we [design feature/test]. This check assesses whether [assumption] is plausible. We report the results in [Results/Table/Appendix]. Although [assumption] cannot be directly tested, the evidence below helps reduce concerns about [threat].
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

### 变体 1: CEM 五步论证链 (主分析版本)
**来源论文**: Darby2026 JOM / Darby2023 MSOM
**验证状态**: 通过 (2/4 复现)
**写入日期**: 2026-05-19
**更新日期**: 2026-05-20 (新增 Darby2023 MSOM 复现)
**槽位**: M8 / M2
**骨架**:
> While [base_estimator] account for [capability_1], they may not account for [threat]. To address concerns related to [threat_type], we first processed our data using [method] ([citation]).
>
> The underlying goal of [method] is to [objective] by [mechanism] ([citation]). Following previous research (e.g., [citations]), we used a [split_type] of the focal variable ([IV]) for the treatment. The treatment group consists of [definition], whereas the control group consists of [definition].
>
> We selected [covariate] as the primary matching covariate to address [concern] that may influence [treatment] as well as [outcome]. The underlying rationale is that [theoretical_reason_for_correlation], and [additional_reason] ([citation]). For the primary analysis, the aim was to [tradeoff_objective]—in other words, "[quote_about_tradeoff]" ([citation], [page]). As described in the robustness checks, we [verification_strategy].
>
> The primary matching covariate, [covariate], was coarsened using [algorithm] ([citations]). This process yielded [N] matched strata containing [N_treated] treated observations and [N_control] control observations for a total of [N_total] observations. [Weights] then were used to [weight_application] ([citation]).
>
> Unlike other matching techniques (e.g., [alternative_method]), there is "[quote_about_method_property]" for [method] ([citation], [page]). However, [balance_measure] is often used to [purpose]. This measure is "[quote_about_interpretation]" ([citation], [page]). The overall [measure] [value_before] before matching to [value_after] after matching, which indicates [interpretation]. [Table_reference] presents the [details]. The [changes] suggest [conclusion] ([citations]).
**与原骨架差异**: 这是CEM的**完整五步论证链**。关键要素：(1) 目标与威胁声明；(2) 方法原理；(3) 协变量选择与理论依据；(4) 匹配结果；(5) 平衡检验。Darby2026将此结构用于主分析（M2/M7），Darby2023将其简化为稳健性检验中的一段（M8）。PSM版本需替换为propensity score估计和common support检查。

### 变体 2: CEM 作为外生冲击的稳健性验证
**来源论文**: Darby2023 MSOM
**验证状态**: 可选变体 (1/4，将CEM置于稳健性检验的新位置)
**写入日期**: 2026-05-20
**槽位**: M8
**骨架**:
> Our finding that [IV_effect_summary] may be subject to endogeneity. It is possible that [endogeneity_threat]. We address this endogeneity concern by exploiting an exogenous shock in our data—[exogenous_event]. [Event] is an exogenous shock to [treatment], contingent upon one key criterion: [exclusion_condition]. This ensures that [exogeneity_rationale].
>
> To test this, we first used [method] ([citation]). In our study, the treatment group consists of [definition_when_exogenous_event_occurred], whereas the control group consists of [definition_when_not]. To use this treatment, we first needed to identify [units] in which there was [exogenous_event]. We assign the variable [treatment_var] as a one for all [observations] in which [condition] and zero otherwise. Importantly, we only assigned this measure as a one if [timing_condition]—not [alternative_timing]. This distinction ensures that our treatment group only captures [observations] in which [treatment_exposure_was_complete].
>
> We matched each observation in the treatment group to those in the control group based on [N] pretreatment variables—[var_list]—that address [rationale] ([citations]). This process yielded [N] matched strata containing [N_treated] treated observations and [N_control] control observations for a total of [N_total] observations across [N] firms from [year_start] to [year_end]; [N_excluded] observations were not matched in any stratum and thus were excluded from the analysis.
**与原骨架差异**: 与变体1(主分析CEM)的关键区别：(1) **处理变量是外生冲击**（如CEO变更）而非内生变量本身（如CEO持股）；(2) 关键时点规则确保treatment exposure完整（"CEO was in the role prior to defect awareness date, not recall initiation date"）；(3) CEM在稳健性检验而非主分析中出现，用于验证内生变量效应的稳健性。这为匹配方法创造了一种新的使用位置——不仅是建立可比样本，更是**外生冲击验证工具**。