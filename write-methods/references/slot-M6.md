<!-- write-methods 槽位骨架 M6：由 SKILL.md「槽位骨架加载」按路由决策加载。内容为原 SKILL.md 该槽位段落骨架（通用 + 设计类型变体 + QC），未做语义修改。 -->

### M6. 控制变量与竞争性解释

**通用填空段落**：

```text
We include controls for [threat family 1] because [alternative explanation 1]. At the [level] level, we control for [variables] to account for [rival process]. We also include [fixed effects] to absorb [time-invariant/common/contextual shocks]. All time-varying predictors are measured at [lag/timing] to preserve temporal ordering. We lag the control variables by [period] to reduce simultaneity concerns.
```

**自然实验/Bad Control 变体**： ✓ STANDARD（5-8 篇自然实验/DiD 范文复现）
```text
Because some controls may be affected by [treatment], we first estimate a parsimonious model with fixed effects before adding controls. We do not include [variable] because it may be post-treatment / mechanically related to [outcome].
```

**同时方程/方程特定控制变体**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M6 段落
```text
For [equation/outcome family], we include controls that address [rival explanation]. For [mediator equation], we further control for [industry benchmark] because firms may align [decision] with industry norms. In the [downstream outcome] equation, we control for [profitability], [growth], and [market position] because each may independently affect [value outcome]. In the [financial choice] equation, we include known determinants such as [industry norm], [asset structure], [firm size], and [profitability].
```

**实验变体**：
```text
We control for [participant characteristics] because [rival explanation]. Random assignment allows us to isolate the effect of [manipulation] on [outcome] within the experimental context.
```

**竞争焦点互控变体**（Haunschild et al. 2015 ORSC 模式）： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：通用 M6 段落
```text
The analysis controls for potential sources of heterogeneity across observations that might influence both the independent and dependent variables. In models estimating [DV1], we controlled for [DV2]; conversely, in models estimating [DV2], we controlled for [DV1]. This allows us to examine whether [focal IV] influences [DV1] and [DV2] net of each other, rather than merely reflecting [alternative explanation: e.g., a common third variable driving both foci]. To ensure that findings were not driven by collinearity involving the respective variables, we also ran models dropping the alternative focus from the equation.
```
