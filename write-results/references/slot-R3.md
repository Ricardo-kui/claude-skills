<!-- write-results 槽位骨架 R3：由 SKILL.md「槽位骨架加载」按路由决策加载。内容为原 SKILL.md 该槽位段落骨架（通用 + 设计类型变体 + QC），未做语义修改。 -->

### R3. 主假设检验（四拍节奏）

**通用填空段落（每假设一段，内置四拍）**： ⭐ PREMIUM（28/28 篇范文使用）

```text
Hypothesis [x] predicted that [predictor] would be [positive/negative] associated with [outcome]. As shown in Model [y] of Table [z], the coefficient for [predictor] is [positive/negative] and statistically significant ([coefficient], [p-value]). Substantively, a [one-SD / one-unit / IQR] increase in [predictor] is associated with a [Y-unit / percentage-point / probability-shift] [increase/decrease] in [outcome], representing approximately [X%] change relative to [baseline / mean / median]. Thus, Hypothesis [x] is supported.
```

> **四拍完整性检查**：方向 → 显著性+系数 → 幅度+基准 → 支持判断。Beat-3（幅度）必须使用具体数值基准（one-SD / one-unit / IQR / 概率变化 / 百分比），禁止仅写 "This indicates that..." 等模糊表述。

**含经济显著性（R5 嵌入）的扩展版**： ✓ STANDARD（12+/28 篇含交互效应范文复现）
```text
Hypothesis [x] predicted that [predictor] would be [positive/negative] associated with [outcome]. As shown in Model [y] of Table [z], the coefficient for [predictor] is [positive/negative] and statistically significant ([coefficient], [p-value]). Substantively, a [one-standard-deviation/one-unit] increase in [predictor] is associated with a [Y-unit] [increase/decrease] in [outcome], representing approximately [percentage / standard deviation / probability] change relative to [baseline]. Thus, Hypothesis [x] is supported.
```

**OLS/FE 专用**： ✓ STANDARD（15+/28 篇面板数据范文复现）
```text
Hypothesis [x] predicted that [predictor] would be [positive/negative] related to [outcome]. Model [y] of Table [z] shows that the coefficient for [predictor] is [positive/negative] and statistically significant (β = [value], p < [threshold], 95% CI [[lower], [upper]]). The R² increases from [value] to [value] when [predictor] is added, indicating that [predictor] explains an additional [value]% of the variance in [outcome]. Thus, Hypothesis [x] is supported.
```

**Logit/Probit/Ordered Probit 专用**： ✓ STANDARD（8-10 篇非线性模型范文复现）
```text
Hypothesis [x] predicted that [predictor] would [increase/decrease] [outcome]. Because [model] is nonlinear, we interpret Hypothesis [x] using [marginal effects/predicted probabilities] rather than coefficient size alone. The marginal effect of [predictor] is [direction] and statistically significant ([value], p < [threshold]), indicating that [substantive probability change]. Thus, Hypothesis [x] is supported.
```

**Logit 经济显著性三层解释变体**（hoffmann2024 型）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：Logit/Probit 专用
```text
Hypothesis [x] predicted that [treatment] would [increase/decrease] the likelihood of [outcome]. Because we estimate a conditional logit model, we interpret results using three complementary approaches to convey economic significance.

First, the odds ratio for [treatment] is [value] (p < [threshold]), indicating that [treatment] is associated with a [X]% [increase/decrease] in the odds of [outcome] relative to [baseline condition]. Second, to translate this into more interpretable units, we compute the relative change in predicted probability: moving from [baseline] to [treatment condition], the predicted probability of [outcome] [increases/decreases] by approximately [X]% relative to the baseline probability of [base rate]%. Third, we anchor this effect in the absolute base rate: this relative change corresponds to an absolute change of [X] percentage points in the probability of [outcome] — a meaningful shift given that [base rate contextualization: e.g., the unconditional probability of [rare outcome] in any given year is only Y%].

This three-layer interpretation — odds ratio → relative probability change → absolute base-rate change — allows readers to assess both statistical and practical significance without overinterpreting logit coefficients, which lack a natural metric.
```

**Logit 经济显著性三层解释 QC**:
- Layer 1 (odds ratio): 必须报告 p 值或置信区间，不能只报告点估计
- Layer 2 (relative change): 必须从 odds ratio 转换为预测概率变化（非手动计算，需用 margins/marginsplot 或等效命令）
- Layer 3 (absolute base rate): 必须引用具体的基准概率（如样本中无条件召回概率），"meaningful" 判断必须有基准
- 三层必须同时出现，不能只报告 odds ratio 就跳到 "thus supported"

**有序 Probit 专用**： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：Logit/Probit 专用 + 增加序数解释句
```text
Hypothesis [x] predicted that [predictor] would [increase/decrease] the likelihood of [outcome category]. Because [outcome] is ordinal, coefficients indicate direction but not the category-specific magnitude of the effect. We therefore calculate marginal effects for [category A] and [category B]. The marginal effects show that [predictor] is associated with [higher/lower probability] of [category]. The effect is strongest for [category], which is consistent with [theoretical expectation]. Thus, Hypothesis [x] is supported.
```

**生存分析专用**： 🔬 EXPERIMENTAL（2-3 篇范文：Zhou 2017, Pontikes 2012 等）⚠️ 保守替代：通用 R3 段落 + 说明 shape parameter
```text
Hypothesis [x] predicted that [predictor] would [lengthen/shorten] time to [event]. Column [y] of Table [z] reports the [duration/AFT] model for [time outcome]. The shape parameter is [value] (p < [threshold]), suggesting that the hazard of [event] [increases/decreases/remains stable] over time. The coefficient for [predictor] is [direction/status], implying that [substantive change] changes [time outcome] by [percent/days]. Thus, Hypothesis [x] is [supported/partially supported/not supported].
```

**DiD 专用**：
```text
Hypothesis [x] predicted that [treatment] would [increase/decrease] [outcome]. Model [y] of Table [z] provides the baseline DiD estimate; Model [w] adds [controls/fixed effects]. Across these specifications, [treatment] is [direction/status]. The estimate implies that [treatment] is associated with a [substantive change] in [outcome], relative to [baseline]. Thus, Hypothesis [x] is supported.
```

**计数模型专用**： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：通用 R3 段落 + IRR 解释
```text
Hypothesis [x] predicted that [predictor] would [increase/decrease] [count outcome]. The incident rate ratio for [predictor] is [value] (p < [threshold]), indicating that [interpretation]. Thus, Hypothesis [x] is supported.
```

**计数模型完整四拍变体**（Haunschild et al. 2015 ORSC 模式，含 e^β − 1 百分比变化）： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：计数模型专用
```text
Hypothesis [x] predicted that [predictor] would be [positive/negative] associated with [count outcome]. Consistent with this prediction, the coefficient on [predictor] has a significantly [positive/negative] effect on [outcome] (Model [y] of Table [z]: β = [value], p < [threshold]). These estimates reveal that the occurrence of [event] contributes to a [N]% [increase/decrease] in the rate of [outcome] (the impact implied by a [negative binomial] regression coefficient β is e^β − 1), controlling for [key controls]. Thus, Hypothesis [x] is supported.
```

**计数模型 AME + 区域显著性变体**（Han 2024 模式，紧跟 IRR 后）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 R3 + 增加 AME 解释句
```text
Because coefficients in count models are difficult to interpret directly, we calculate average marginal effects (AMEs) and identify the region of significance. Figure [x] plots the marginal effect of [predictor] on [outcome] across the range of [conditioning variable / predictor itself]. The marginal effect is [positive/negative] and statistically significant when [condition, e.g., conditioning variable > threshold], but it [attenuates / reverses / becomes insignificant] when [opposite condition]. The turning point occurs at approximately [value], which corresponds to [theoretical interpretation, e.g., the median level of firm resources]. This pattern indicates that [theoretical mechanism] operates primarily within [boundary region].
```

**U-shaped / 倒U型专用**（Zhou 2017 模式，内置四拍 + 转折点计算）： 🔬 EXPERIMENTAL（1-2 篇范文：Zhou 2017 等）⚠️ 保守替代：通用 R3 段落 + 增加 squared term 解释
```text
Hypothesis [x] predicted that [predictor] would have an inverted U-shaped relationship with [outcome]. [Predictor] positively affects [outcome] (Model [X]), yet the squared term has a negative effect (Model [Y]; coefficient = [value], p [relation] [threshold]). Therefore, [predictor] has an inverted U-shaped relationship with [outcome], with a turning point at [percentage/value]. That is, a [moderate/medium] level of [predictor] is most beneficial for [outcome], in support of Hypothesis [x].
```

**U-shaped + 交互调节变体**（当 U-shaped 被三向交互调节时）： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：U-shaped 专用 + 增加交互解释
```text
Hypothesis [x] predicted that [predictor] would have an inverted U-shaped relationship with [outcome] that is moderated by [factor C]. The three-way interaction [predictor × squared term × factor C] is [status] (β = [value], p [relation] [threshold]). To interpret this effect, we calculate turning points at [low / mean / high] levels of [factor C]. When [factor C] is low, the turning point occurs at [value], whereas when [factor C] is high, it shifts to [value]. This indicates that [boundary condition] alters the optimal level of [predictor].
```

**IV/2SLS 第二阶段专用**：
```text
Hypothesis [x] predicted that [predictor] would be [positive/negative] associated with [outcome]. The 2SLS estimate in Panel B, Model [y] of Table [z] shows that the coefficient for [predictor] is [positive/negative] and statistically significant (β = [value], p [relation] [threshold]). The magnitude is [larger/smaller/similar] to the OLS estimate (β = [value]), which is consistent with [upward / downward] bias from [omitted variable / measurement error]. Thus, Hypothesis [x] is [supported / partially supported].
```

**推断二元结果专用**：
```text
Hypothesis [x] predicted that [predictor] would [increase/decrease] the likelihood of [binary outcome]. Because [binary outcome] is inferred rather than directly observed, we report results using both the [main inference rule] and the [alternative threshold]. Under the main classification, [percentage]% of [units] are classified as [state = 1]. Model [y] of Table [z] shows that [predictor] is [positive/negative] and statistically significant (β = [value], p [relation] [threshold]), indicating that [substantive interpretation]. The pattern is [consistent / qualitatively similar] when we use the alternative threshold. Thus, Hypothesis [x] is supported.
```

**跨受众构念对比专用**（Gamache 2020 模式，多结果上层梯队）：
```text
Hypothesis [x] predicted that [predictor] would be [positive/negative] associated with [outcome A] but [positive/negative / null] associated with [outcome B]. Model [a] of Table [z] shows that the coefficient for [predictor] on [outcome A] is [direction] and [significant / not significant] (β = [value], p = [value]). In contrast, Model [b] shows that the coefficient on [outcome B] is [direction] and [significant / not significant] (β = [value], p = [value]). The divergence between [outcome A] and [outcome B] is consistent with [theoretical mechanism: audience-specific interpretation / stakeholder-specific incentives], because [theoretical reasoning]. Thus, Hypothesis [x] is [supported / partially supported].
```

**双受众平行对比专用**（Pontikes 2012 模式，同一 X 对两类受众产生方向相反的效果）： ✓ STANDARD（Pontikes 2012 ASQ 等高被引范文复现）

```text
Models [a-b] test hypothesis [H_A], which predicted that [predictor] would be [negatively] associated with [DV_A]. Results show strong support for this prediction. [Measure] has a [negative] effect on [DV_A] ([coefficient], p < [threshold]). [Robustness checks: e.g., This pattern holds across alternative specifications / measures / subsamples]. In substantive terms, a one-standard-deviation [increase/decrease] in [predictor] corresponds to [magnitude statement: e.g., a decrease of X rank points / an X% change]. These results indicate that [one-sentence summary of finding for audience A].

Models [c-d] test hypothesis [H_B], which proposed the opposite relationship for [audience B]'s evaluation of [DV_B]. Results likewise show strong support. [Measure] has a [positive] effect on [DV_B] ([coefficient], p < [threshold]). [Robustness: This pattern also holds across alternative specifications]. In substantive terms, [magnitude statement: e.g., an organization one SD above the mean is X times more likely to receive funding]. The same [construct] that makes [entities] [less appealing to audience A] makes them [more appealing to audience B]. These opposing effects are illustrated in [Figure x].
```

> **双受众平行对比 QC 检查点**: (1) 双Y的系数方向必须真的相反（不只是一方显著一方不显著）；(2) 收束句 "The same [X] that makes...makes..." 必须在 R3 段落内出现，不由 Discussion 承担；(3) Figure 必须在 R3 段落内引用；(4) 两个受众段落的节奏应接近对称（都含 magnitude + robustness）。

**实验专用**：
```text
Hypothesis [x] predicted that [condition] would [increase/decrease] [outcome]. Participants in the [condition] condition scored [higher/lower] on [outcome] (M = [value], SD = [value]) than those in the [comparison] condition (M = [value], SD = [value]), t([df]) = [value], p [relation] [threshold]. Thus, Hypothesis [x] is supported.
```

**Prediction / Proposition / Research Question 风格专用**（无 H 编号时）：
```text
We predicted that [theoretical relationship]. As shown in Model [y] of Table [z], the coefficient for [predictor] is [positive/negative] and statistically significant ([coefficient], [p-value]). This indicates that [substantive interpretation]. Thus, the prediction is supported.
```

**GLM / 事件研究 CAR 专用**（当 DV 为累计异常收益时）：
```text
Hypothesis [x] predicted that [predictor] would [increase/decrease] stock market penalties. Columns [a–c] of Table [z] report GLM estimates for [CAR window] across [subsamples]. The coefficient on [predictor] is [negative/positive] and statistically significant ([coefficient], [p-value]) for [window], indicating that [one-SD] increase in [predictor] is associated with a [percentage] stock market penalty. The effect is [not significant] for [longer window], suggesting that [effect dissipates over time]. Thus, Hypothesis [x] is supported.
```

**中介专用（R3 扩展）**：
```text
Hypothesis [x] predicted that [mediator] mediates the relationship between [predictor] and [outcome]. Following [Baron and Kenny/Hayes], we conduct a mediation analysis. In Model [a], [predictor] is significantly related to [mediator] (β = [value], p < [threshold]), satisfying Condition 1. In Model [b], [mediator] is significantly related to [outcome] (β = [value], p < [threshold]), satisfying Condition 2. When both [predictor] and [mediator] are included in Model [c], the coefficient for [predictor] decreases from [value] (p < [threshold]) to [value] (p = [value]), while [mediator] remains significant (β = [value], p < [threshold]). The [Sobel test/bootstrap] confirms significant mediation ([statistic] = [value], p < [threshold]). These findings support Hypothesis [x].
```

**HLM / 多层模型专用**（当数据为嵌套结构时，区分 Level-1 与 Level-2 系数）：
```text
Hypothesis [x] predicted that [predictor] would be [positive/negative] related to [outcome]. Model [y] of Table [z] reports the HLM estimate. The Level-1 (within-[unit]) coefficient for [predictor] is [positive/negative] and statistically significant (γ = [value], p [relation] [threshold]), indicating that [substantive within-unit interpretation]. The Level-2 (between-[unit]) coefficient is [positive/negative] and [significant / not significant] (γ = [value], p [relation] [threshold]), suggesting that [between-unit interpretation]. The cross-level interaction between [level-2 predictor] and [level-1 predictor] is [positive/negative] and statistically significant (γ = [value], p [relation] [threshold]); a one-SD increase in [level-2 predictor] strengthens the [level-1 predictor]-[outcome] relationship by [Y-unit]. Thus, Hypothesis [x] is supported.
```

**文本构念结果四拍专用**（当预测变量或结果来自文本分析时）：
```text
Hypothesis [x] predicted that [predictor] would be [positive/negative] associated with [outcome]. Model [y] of Table [z] shows that the coefficient for [predictor] is [positive/negative] and statistically significant ([coefficient], [p-value]). Substantively, a one-standard-deviation increase in the text-based [predictor] score is associated with a [Y-unit / percentage-point] [increase/decrease] in [outcome], representing approximately [X%] change relative to the sample mean. This effect size is meaningful because [theoretical benchmark: e.g., comparable to the effect of a one-SD change in the archival measure of the same construct]. Thus, Hypothesis [x] is supported.
```
