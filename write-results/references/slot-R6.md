<!-- write-results 槽位骨架 R6：由 SKILL.md「槽位骨架加载」按路由决策加载。内容为原 SKILL.md 该槽位段落骨架（通用 + 设计类型变体 + QC），未做语义修改。 -->

### R6. 非显著 / 混合 / 意外发现

> **区分原则**：非显著的**假设检验**必须在 Results 中报告（inline 或独立段均可）。非显著的**假设验证、判别效度或安慰剂检验**可放在 Supplemental Analyses（R8），因其本质是支撑理论假设而非正式假设检验。

**通用填空段落（每非显著/混合假设一段）**：

```text
Hypothesis [x] predicted that [predictor] would be [direction] related to [outcome]. Contrary to our prediction, the coefficient for [predictor] is [not statistically significant/opposite direction] ([coefficient], [p-value]). We therefore interpret this finding as [no evidence/mixed evidence/partial support] and avoid drawing stronger conclusions from it. We return to this unexpected result in the Discussion.
```

**方向一致但未达显著**：
```text
The coefficient on [predictor] is [direction] but does not reach conventional significance levels ([coefficient], [p-value]), providing no support for Hypothesis [x]. The direction is consistent with our prediction, but the estimate is too imprecise to draw firm conclusions.
```

**部分支持**：
```text
We find partial support for Hypothesis [x]: [supported part], but [unsupported part]. The pattern suggests that [relationship] may be more contingent than predicted.
```

**混合结果分解**：
```text
Results do not support Hypothesis [x]. To examine this possibility, we separate [aggregate construct] into [components] and estimate [additional comparison]. The additional analysis suggests [refined interpretation]. We defer broader interpretation of this pattern to the Discussion.
```

**非显著间接调节变体**（mediated moderation 中部分路径不显著时）： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：省略或 inline 报告
```text
We test whether the interaction between [mediator] and [predictor] mediates the moderating effect of [moderator 1] on the [predictor-outcome] relationship. In the full system (Equation 5), the coefficient on the original [predictor × moderator 1] interaction (β₄₃) is [not statistically significant / reduced in magnitude compared with Equation 2], whereas the [predictor × mediator] interaction (β₄₅) is [significant/direction]. This pattern indicates that [mediator] [fully/partially] accounts for the moderating role of [moderator 1] in the [outcome type] specification. However, we do not find a statistically significant indirect moderation effect in the [alternative outcome type] specification, suggesting that the mediated moderation mechanism may be [context-dependent / limited to specific decision domains]. We interpret this pattern cautiously and defer broader theoretical implications to the Discussion.
```

**主效应不显著但交互显著变体**（Mannor 2016 模式；禁止跳过主效应）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：R3 通用段落 + 增加交互警告句
```text
Hypothesis [x] predicted that [predictor] would be [direction] related to [outcome]. The coefficient for [predictor] is [direction] but does not reach conventional significance levels ([coefficient], [p-value]), providing no direct support for the main effect. However, the interaction between [predictor] and [moderator] (Hypothesis [z]) is [direction] and statistically significant (β = [value], p [relation] [threshold]). Because the interaction is significant, the main effect of [predictor] should not be interpreted independently ([Aiken & West / Dawson & Richter]); instead, its effect is conditional on [moderator]. We therefore interpret the results through the lens of the significant interaction and defer discussion of the null main effect to the Discussion.
```

**非显著深化变体**（非显著结果构成后续显著发现的 baseline，而非孤立报告）： ✓ STANDARD（Pontikes 2012 模式）

```text
[Hypothesis / prediction] proposed that [expected relationship]. The coefficient for [predictor] is [direction] but does not reach conventional significance levels ([coefficient], [p-value]). This null result is noteworthy because it establishes a baseline: [construct A] does not appear to [expected effect] for this audience. Yet this same [construct]—when tested against [audience B] below—shows the opposite pattern, suggesting that the null result is not a measurement failure but a theoretically meaningful audience difference.
```

> **非显著深化 QC**: 
> - 仅当该非显著结果为后续的显著对立发现提供对比基线时使用
> - 非显著 + 显著对立 = 理论上有意义的双受众差异，而非“我们测不出来”
> - 如果只是孤立非显著（没有后续理论对比），使用通用填空段落，不要过度解释

**方向相反诚实解释变体**（结果方向与假设相反，但有理论依据可解释）： ✓ STANDARD（Pontikes 2012 模式）

```text
Contrary to Hypothesis [x], which predicted [expected direction], the coefficient for [predictor] is [opposite direction] and [statistically significant / not significant] ([coefficient], [p-value]). Rather than treating this as a simple null finding, we note that [theoretical explanation grounded in prior literature or alternative mechanism]. This pattern is consistent with [alternative theoretical account], though we did not hypothesize it ex ante. Given the post-hoc nature of this interpretation, we treat it as suggestive and return to it in the Discussion.
```

> **方向相反 QC**: 
> - 必须有理论解释（不是 "unexpected future research" 空话）
> - 必须诚实标注 post-hoc 性质
> - 仅当方向相反的结果有 ≥2 个理论锚点（citation 或机制逻辑）时才使用此变体；否则使用通用填空段落
