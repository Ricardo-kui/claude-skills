---
design_type: 自然实验-DiD
status: VERIFIED
source_papers: []
variants_count: 8
created: 2026-05-18
updated: '2026-05-22'
---

# 自然实验-DiD — Methods 骨架

## 设计特征摘要

<!-- 由 distill-methods-exemplar 首次蒸馏后填充 -->

## M1. 研究情境 / 实证背景

### 主骨架（通用）
： ⭐ PREMIUM（28/28 篇范文使用，跨所有模型类型复现）

```text
[Empirical setting] provides an appropriate context for examining [theoretical relationship] for three reasons. First, [setting property] makes [mechanism] observable. Second, [scope condition] reduces [confound]. Third, [data feature] allows us to observe [unit/process] over [period]. The unit of analysis is [unit], which aligns with our theorizing about [mechanism].
```

### 变体 1: 自然实验/DiD 变体
（替换首句）： ✓ STANDARD（5-8 篇 DiD/自然实验范文复现）

```text
We examine [phenomenon] using [policy/event/institutional change] that altered [exposure/risk/incentive] across [units] and time. [Empirical setting] is well suited because [process] is well documented and [context controls] reduce [confounding concern].
```

---

## M2. 数据来源与样本漏斗

### 主骨架（通用）
：

```text
We began with [starting population] from [source] over [period]. We matched these observations to [additional sources] to obtain [variables]. We excluded [cases] because [comparability/measurement/identification reason]. The final sample consists of [N] [units] observed over [period], with [unit] as the unit of analysis.
```

### 变体 1: 自然实验/DiD 变体
： ✓ STANDARD（5-8 篇 DiD 范文复现）

```text
Our primary sample consists of [units] observed from [period], drawn from [source] because it tracks [construct-relevant activity]. The observation window begins in [year] because [source/construct availability] and ends in [year] to capture [post-treatment horizon]. Treatment is observed for [treated units] after [event], while [control units] provide the counterfactual comparison. Because testing [moderation/mechanism] requires [additional source], the sample for H[x] is restricted to [available period/units].
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

### 变体 1: 处理分配稳定性补充
（DiD 可选）： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：省略此段

```text
During our sample period, [percentage] of [units] changed their [treatment-relevant characteristic, e.g., headquarters location]. We use [historical/fixed] [characteristic] information to maintain consistent treatment assignment.
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

### 变体 1: DiD 变体
：

```text
We estimate a difference-in-differences model in which [outcome] is regressed on [treatment], [moderator/interactions], controls, and fixed effects. Identification comes from comparing changes in [treated units] before and after [event] to contemporaneous changes among [control units]. We cluster standard errors at [unit/jurisdiction] to account for serial correlation and within-[cluster] dependence.
```

### 变体 2: DiD 方程编号与 SE 聚类引用补充
：

```text
We cluster standard errors at the [level] to address [dependence structure] ([citation, e.g., Bertrand et al. 2004; Jager et al. 2021]). Where relevant, we present numbered equations: Equation (1) reports the baseline DiD specification, and Equation (2) reports the event-study leads-and-lags specification.
```

---

## M8. 识别策略 / 效度 / 诊断检验

### 主骨架（通用）
：

```text
To address concerns about [threat], we [design feature/test]. This check assesses whether [assumption] is plausible. We report the results in [Results/Table/Appendix]. Although [assumption] cannot be directly tested, the evidence below helps reduce concerns about [threat].
```

### 变体 1: 自然实验/DiD 变体
：

```text
Our identification strategy relies on [source of variation]. [Shock/event/policy] creates variation in [treatment] that is plausibly exogenous to [outcome] because [reason]. The key identifying assumption is that [treated and control units] would have followed similar trends absent [treatment]. We assess this assumption in the Results section using [event-study/leads-lags] specifications. We first estimate a parsimonious specification because [controls] may be affected by [treatment].
```

### 变体 2: DiD 置换检验预览补充
（可选，置于自然实验/DiD 变体后）：

```text
We also conduct permutation tests by randomly assigning [treatment status/timing] across [N] iterations to assess whether [unobserved characteristics] could drive our results.
```

### 变体 3: 制度/政策体制安慰剂检验变体
：

```text
Because [outcome] may reflect [alternative mechanism] rather than [focal mechanism], we exploit a [regime change] as a falsification test. During the [mandatory regime], [behavior] should not exhibit [focal pattern] because [institutional reason]. We re-estimate our models using [mandatory regime subsample] and find [null effect], consistent with the assumption that [focal mechanism] requires [voluntary regime condition].
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

<!-- distill-methods-exemplar Phase 4 验证通过的变体写入此处 -->
<!-- 格式：
### 变体 N: [来源论文] (YYYY-MM-DD)
**验证状态**: 通过 / 需修正
**槽位**: M?
**骨架**:
> "..."
**与原骨架差异**: ...
-->