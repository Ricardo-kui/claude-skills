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

**Null-result 被抵消力解释变体（posthoc moderator 揭示 offsetting force）**（Li et al. 2026 POM 型）： 🔬 EXPERIMENTAL（1 篇范文）— 当 null 主效应可由一个 posthoc moderator 揭示的抵消力来解释时
```text
Hypothesis [x] predicted that [predictor] would be [direction] related to [outcome]. This hypothesis is not supported, as the coefficient for [predictor] is not significant ([coefficient], [p-value]). A possible explanation is that two opposing forces operate simultaneously: [force 1 — the theorized mechanism, e.g., distance increases monitoring challenges → +risk] and [force 2 — a context-specific offsetting mechanism, e.g., distant suppliers are in stronger-institution countries → −risk]. Under this account, the null result reflects the net of two opposing forces rather than the absence of an effect. To test this explanation, we examined whether [moderator that isolates force 2, e.g., supplier-country regulatory quality] moderates the [predictor]→[outcome] relationship. Consistent with the offsetting-force account, [moderator] [weakens/reverses] the relationship ([coefficient], [p-value]) — when [force 2 is strong], the [predictor]→[outcome] effect is [weaker/negative]; when [force 2 is weak], it is [stronger/positive]. Thus the null main effect masks a context-contingent relationship: [predictor] does affect [outcome], but its effect is offset by [force 2] in this setting.
```
**关键特征**:
- **null 不是"无效应"而是"两抵消力的净"**: 把 null 重新框定为 opposing forces 的 net，而非 effect absence——升级为"context-contingent relationship"
- **posthoc moderator 隔离抵消力**: 用一个针对 force 2 的 moderator 检验，揭示 null 背后的抵消机制
- **诚实标注 posthoc**: 这是 posthoc 解释（H 先 null，再用 moderator 解释），须如实标注，不能伪装成 a priori 预测
- **与 WEIRD gap 配对**: 非 WEIRD 语境中 WEIRD 预测 null 常因抵消力（li2026: distance 的 +risk 被 up-gradient sourcing 的 −risk 抵消 → 用 regulatory-quality moderator 揭示）

**适用**: null 主效应但理论预期应有效应的研究；非 WEIRD 语境中 WEIRD 预测失效、可用语境特定抵消力解释的情况；任何 null 结果可用 offsetting moderator 救回的情境

**禁忌**:
- posthoc moderator 必须有理论依据（force 2 须先论证，不能数据挖掘后合理化）
- 必须诚实标注 posthoc 性质——不能伪装成 a priori 预测
- 抵消力论证须具体（哪个制度/结构因素产生 opposing force），不能泛泛"可能是其他因素"
- 若找不到合理的抵消力，应接受 null（用 R6 通用段落），不要强行 rescue
- 不要与 R6「方向相反诚实解释变体」混淆——本变体是 **null + moderator 揭示抵消**，彼变体是 **方向相反 + 理论解释**（无 null）


**Post-treatment selection 诚实边界变体**（Kim & Lee 2026 SMJ 型，Slough 2023）： 🔬 EXPERIMENTAL（1 篇范文）— multi-stage pipeline 中后置 outcome 的 ATE undefined 承认
```text
An important caveat is that [downstream outcomes: e.g., retention / satisfaction / performance] are only defined for [units that passed an earlier stage: e.g., candidates who were hired / customers who converted] — a form of post-treatment selection that renders the unconditional average treatment effect on these outcomes undefined ([Slough 2023]). Since [treatment] itself predicts [passage through the earlier stage], as our earlier results establish, the [downstream] comparisons are necessarily made on a selected sample whose composition differs between [treatment] and [control] groups. We therefore interpret the [downstream null / downstream estimates] as conditional on selection rather than population-average effects, and defer broader causal claims to future research with designs that exogenously vary selection.
```
**关键特征**:
- **multi-stage pipeline 的天然配对**: 凡报告"前置 + 后置"结果的研究（招聘漏斗、销售漏斗、创新采纳、晋升）都面临后置 outcome 仅对通过前期筛选者定义 -> unconditional ATE undefined
- **诚实承认升级可信度**: 把后置 null（retention/satisfaction）从"失败"重新框定为"条件性估计"，反而提升方法学自觉；多数论文沉默
- **Slough 2023 是 growing citation 节点**: AMJ/SMJ 近期审稿人会要求此类 pipeline 设计的 post-treatment caveat
**适用**: 任何 multi-stage/funnel 设计中后置 outcome 条件于前期筛选的研究。配套见 OLS-FE.md 变体27（多阶段管道）。
**禁忌**:
- 不可把后置条件性 null 包装为"无效应"的因果结论——ATE undefined 不是 null
- 须明确指出 treatment 本身预测前期 passage（否则 post-treatment 论证不成立）
