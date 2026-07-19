<!-- write-methods 槽位骨架 M7：由 SKILL.md「槽位骨架加载」按路由决策加载。内容为原 SKILL.md 该槽位段落骨架（通用 + 设计类型变体 + QC），未做语义修改。 -->

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
