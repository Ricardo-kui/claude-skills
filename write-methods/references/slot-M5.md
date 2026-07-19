<!-- write-methods 槽位骨架 M5：由 SKILL.md「槽位骨架加载」按路由决策加载。内容为原 SKILL.md 该槽位段落骨架（通用 + 设计类型变体 + QC），未做语义修改。 -->

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
