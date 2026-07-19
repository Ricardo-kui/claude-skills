<!-- write-results 槽位骨架 R5：由 SKILL.md「槽位骨架加载」按路由决策加载。内容为原 SKILL.md 该槽位段落骨架（通用 + 设计类型变体 + QC），未做语义修改。 -->

### R5. 经济 / 实质显著性

**通用填空段落（可嵌入 R3 或独立成段）**：

```text
To assess substantive magnitude, we calculated [marginal effects/predicted probabilities/effect sizes]. A [one-standard-deviation/one-unit] increase in [predictor] is associated with [change] in [outcome]. This represents approximately [percentage / standard deviation / probability] change relative to [baseline]. The magnitude is meaningful because [theoretical/practical benchmark].
```

**当效应较小时的诚实表述**：
```text
Although statistically significant, the effect is substantively modest; we interpret it cautiously.
```

**市场价值/经济影响专用**：
```text
To assess the economic impact of [predictor], we examine predicted changes in [downstream outcome] across meaningful levels of [conditioning variable]. The pattern indicates that [predictor] is associated with [positive value consequence] for [condition/group A] but [negative value consequence] for [condition/group B]. This translation matters because [market-value outcome] is difficult to interpret from coefficients alone.
```

**分位数经济显著性专用**（配合分位数表展示幅度）：
```text
To assess substantive magnitude, we examine [outcome] across quartiles of [predictor]. Table [x] presents the range of [outcome] for [subsamples]. Moving from the first quartile ([Q1 value]) to the second quartile ([Q2 value]) — an approximately [time/amount] change — is associated with a [percentage] [increase/decrease] in [outcome]. The magnitude is meaningful because [industry benchmark or theoretical reason].
```

**调节变量经济显著性：25th→75th 百分位预测概率变体**（hoffmann2024 型）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 R5 段落
```text
To assess the economic significance of the moderating effect, we calculate predicted probabilities of [outcome] at different combinations of [moderator] and [treatment]. Holding other variables at their means, moving from the 25th to the 75th percentile of [moderator] changes the predicted probability of [outcome] by [X] percentage points when [treatment condition] holds — an economically meaningful shift given that the unconditional probability in our sample is only [Y]%. In contrast, when [treatment condition] does not hold, the same change in [moderator] is associated with a [smaller / negligible] shift of only [Z] percentage points. This asymmetry confirms that [moderator] primarily operates through the [treatment → outcome] channel, as our theory predicts.
```

**调节经济显著性 QC**:
- 必须报告 25th 和 75th 百分位的具体值，不能只写 "low" 和 "high"
- 必须同时报告 treatment=0 和 treatment=1 两种状态下的预测概率变化（展示不对称性）
- 必须引用无条件基准概率作为"meaningful"的参照
- 禁止只报告 "the interaction is significant (p < .05)" 就结束——交互项的经济显著性必须量化

**转折点 / 最优水平经济显著性专用**（配合 U-shaped R3）：
```text
To assess the substantive magnitude of the U-shaped relationship, we examine the turning point and its position in the empirical distribution. The turning point occurs at [value/percentage] of [predictor], which corresponds to [the 65th percentile / one SD above mean / median] of the observed distribution. This level is economically meaningful because [benchmark: e.g., it exceeds the average state ownership ratio among partially privatized firms]. A shift from [low baseline] to the optimal level is associated with a [Y-unit] increase in [outcome], representing approximately [percentage] improvement relative to the sample mean.
```

**多构念联合经济显著性专用**（Pontikes 2012 模式，报告两个 predictor 联合变动的净效应）： ✓ STANDARD

```text
It is important to note that the combined effect of [predictor A] and [predictor B] is [direction] through most of the range of these data. An [entity] one standard deviation above the mean on both [predictor A] and [predictor B] [suffers/benefits from] a [change] of [magnitude] in [DV] compared with an [entity] one standard deviation below the mean on each measure. The combined effect of [construct], considering both [component X: e.g., label-level ambiguity] and [component Y: e.g., organization-level spanning], is [summary: e.g., negative / positive / null].
```

> **多构念联合 QC**: 仅当两个 predictor 理论上来自同一构念的两个维度时使用（如 label-level × org-level）；不要对任意不相关的 predictor 计算联合效应。

**计数结果 cost-per-event 经济显著性专用**（把系数/幅度翻译为"每改变一个事件需要多少投入"）： ✓ STANDARD
```text
To translate the coefficient into a more interpretable cost metric, we divide the estimated effect by the unit cost of [predictor]. The results imply that an additional [monetary unit] of [predictor] is associated with approximately [1/N] fewer [outcome events]. Equivalently, approximately [monetary amount] more in [predictor] is associated with one fewer [outcome event]. Given that the average [outcome event] involves [scale: e.g., units affected / duration / scope] and an estimated per-event cost of [cost], this magnitude is economically meaningful.
```

> **cost-per-event QC**:
> - 必须明确 "one unit of outcome" 对应的实际含义
> - 投入与产出单位必须匹配（如美元投入 → 事件数变化）
> - 必须提供一个保守或文献锚定的 per-event cost 作为基准
> - 仅适用于计数或近似计数的结果（recalls, patents, lawsuits, product launches, failures）
