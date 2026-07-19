<!-- write-results 槽位骨架 R4：由 SKILL.md「槽位骨架加载」按路由决策加载。内容为原 SKILL.md 该槽位段落骨架（通用 + 设计类型变体 + QC），未做语义修改。 -->

### R4. 交互效应 / 条件效应

> **上游接口**：在解释交互效应前，先确认 `/write-theory` 和 `/write-methods` M7补充 已明确该假设是 **differential prediction**（slope/nature 改变）还是 **differential validity**（strength/correlation 改变）。默认 R4 模板适用于 differential prediction；若 Theory 声明为 differential validity，使用下方的专用变体。

**通用填空段落**：

```text
Hypothesis [x] predicted that [moderator] would moderate the relationship between [predictor] and [outcome]. Model [y] adds the interaction between [predictor] and [moderator]. The interaction term is [positive/negative] and [significant/not significant] ([coefficient], [p-value]). To interpret this effect, Figure [x] plots the predicted values of [Y] at high and low levels of [moderator]. The relationship between [predictor] and [outcome] is [stronger/weaker/significant/null] when [moderator] is [high] than when it is [low]. Thus, Hypothesis [x] is [supported/partially supported/not supported].
```

**非线性交互专用**：
```text
Because the model is nonlinear, we interpret the [predictor × moderator] interaction using [average marginal effects/simple slopes]. At low levels of [moderator] (mean – 1 SD), [predictor] changes [outcome] by [placeholder]; at high levels (mean + 1 SD), it changes [outcome] by [placeholder]. This pattern indicates that [moderator] [weakens/strengthens] the effect. Figure [x] illustrates this pattern and shows that [theoretical interpretation].
```

**主效应解释警告（当交互显著时，强烈建议紧跟）**：
```text
Because the interaction term is significant, the main effects of [predictor] and [moderator] cannot be interpreted independently. The main effect of [predictor] (β = [value], p = [value]) represents the effect when [moderator] is at its mean, which is not substantively meaningful.
```

**非线性模型中无显式交互项的调节效应变体**（Haunschild et al. 2015 ORSC 模式，图形+子样本 t 检验）： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：通用 R4 段落
```text
Hypothesis [x] predicted that the [positive/negative] impact of [predictor] on [outcome] [diminishes/intensifies] over [moderator]. The traditional approach to testing such a contingency effect through interaction terms is inappropriate in the context of our analysis because we adopt a [nonlinear specification] and because the incidence of [treatment] may vary systematically across different levels of [moderator] ([Citation]). As such, we tested this hypothesis through graphical analysis and a formal econometric test of differences in marginal effects of [predictor] across subsamples containing different levels of [moderator]. Using the full models in Table [x], we predicted [outcome] and then plotted the predicted values against [predictor] with a least-square fitted line separately for [low moderator group] and [high moderator group]. As Figures [a] and [b] show, the slope of the fitted line is [less positive / less negative] for [high group] than for [low group], indicating that the marginal impact of [predictor] on [outcome] [diminishes/intensifies] as [moderator] increases. To examine whether the marginal effect of [predictor] is indeed significantly different across levels of [moderator], we split the sample by levels of [moderator] while holding other variables constant at their means. We then conducted t-tests to compare differences in the marginal effect of [predictor] across the subsamples. Results reveal that the influence of [predictor] is [less positive / less negative] for [high group] than for [low group] (t = [value], p < [threshold]). Thus, Hypothesis [x] is supported.
```

> **注意**：在部分顶刊（如 SMJ）中，若交互项是理论焦点且主效应本身已不显著，该警告可省略。但包含此警告通常能增强可信度。

**三向交互专用**（Paruchuri 2020 扩展版，含简单斜率分解）：
```text
Hypothesis [x] predicted that [factor C] would condition the [predictor × moderator] interaction. The [predictor × moderator × factor C] three-way interaction is [direction/status] (β = [value], p [relation] [threshold]). To interpret this effect, we decompose the [predictor × moderator] interaction at [low / mean / high] levels of [factor C]. When [factor C] is low (mean – 1 SD), the [predictor × moderator] interaction is [status] (β = [value], p = [value]), and the simple slope of [predictor] on [outcome] at high [moderator] is [status] (β = [value], p = [value]). When [factor C] is high (mean + 1 SD), the [predictor × moderator] interaction is [status] (β = [value], p = [value]), and the simple slope of [predictor] at high [moderator] is [status] (β = [value], p = [value]). Figure [x] plots these conditional effects and shows that [theoretical interpretation: the contingency itself is contingent on factor C]. Thus, Hypothesis [x] is [supported/partially supported/not supported].
```

**构造暴露分解专用**（Shipilov 2020 模式，堆叠扩散或多层暴露）：
```text
Hypothesis [x] predicted that [predictor] would [increase/decrease] [outcome], and that this effect would be stronger when [exposure intensity / network proximity] is high. We decompose [predictor] into [component A] and [component B] to distinguish [mechanism A] from [mechanism B]. Model [a] shows that [component A] is [status] (β = [value], p = [value]), whereas [component B] is [status] (β = [value], p = [value]). This decomposition indicates that [theoretical interpretation of asymmetry]. Thus, Hypothesis [x] is [supported / partially supported].
```

**DiD 调节专用**：
```text
Model [x] tests whether [moderator] conditions the effect of [treatment] on [outcome]. The interaction is [direction/status]. As Figure [y] shows, the treatment effect is [stronger/weaker] when [moderator] is high and [weaker/null] when [moderator] is low, consistent with [mechanism].
```

**联合调节变量 "Switch-Off" 分析变体**（hoffmann2024 型）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：DiD 调节专用 + 分别报告两个交互项
```text
Our theory predicts that [moderator 1] (an [intrinsic] constraint) and [moderator 2] (an [extrinsic] constraint) each independently weaken the negative effect of [treatment] on [outcome]. To provide a more complete picture of how these constraints jointly shape [outcome] decisions, we examine what happens when both constraints are simultaneously present versus absent.

We define four joint-constraint scenarios based on [moderator 1] and [moderator 2] being at their [low/high] levels ([operational cutoff: e.g., above/below median]). Figure [x] plots the predicted probability of [outcome] under [treatment = 0] versus [treatment = 1] for each scenario.

When [treatment] is absent, the predicted probability of [outcome] is [relatively stable / low / high] across all four scenarios, ranging from [X%] to [Y%]. When [treatment] is adopted, predicted probabilities diverge sharply across scenarios. In the [worst-case] scenario — where both constraints are absent ([moderator 1] = low, [moderator 2] = low) — [treatment] is associated with a [large] [decrease/increase] in [outcome] probability, from [baseline%] to [post-treatment%]. In the [best-case] scenario — where both constraints are present ([moderator 1] = high, [moderator 2] = high) — the difference between [treatment] and [no treatment] [narrows substantially / becomes statistically indistinguishable from zero].

This "switch-off" analysis — documenting that the main effect is strongest when both constraints are absent and weakest (or absent) when both are present — provides a holistic view of how [intrinsic] and [extrinsic] governance mechanisms jointly shape [agent] decision making.
```

**联合调节 "Switch-Off" QC**:
- 必须在两种约束分别测试通过（各自单独显著）之后，再做联合分析
- 四种场景的定义必须透明（median split / quartile / specific threshold），不能隐含分类逻辑
- "worst-case" 和 "best-case" 必须有理论依据——对应理论预测中约束最弱和最强的组合
- 必须同时展示 treatment=0 和 treatment=1 两种状态，不能只报告 difference
- 联合分析不是独立的假设检验——它是补充证据，服务于边界条件的完整叙事

**子样本交互变体**（用分组检验而非交互项时，R4 报告）：
```text
Hypothesis [x] predicted that [moderator] would moderate the relationship between [predictor] and [outcome]. Because [theoretical reason for distinct regimes / distribution characteristics], we split the sample by [moderator] into [high-severity / high-group] and [low-severity / low-group] subsamples and estimated separate models for each group. For the [high group], the coefficient on [predictor] is [direction] and [significant/not significant] ([coefficient], [p-value]). For the [low group], the coefficient is [direction] and [significant/not significant] ([coefficient], [p-value]). The pattern indicates that [predictor] [influences/does not influence] [outcome] in the [high group] but [not in the low group / to a lesser extent in the low group], supporting Hypothesis [x]. We note that because we use separate subsamples rather than a pooled interaction term, we do not conduct a formal test of coefficient equality; the pattern should be interpreted descriptively.
```

**differential validity 结果解释变体**（当 Theory / M7补充 声明 moderator 改变的是 X–Y 相关强度而非 slope 时）：
```text
Hypothesis [x] predicted that [moderator] would change the strength of the [predictor]–[outcome] relationship rather than its slope (differential validity). Following Andersson, Cuervo-Cazurra, and Nielsen (2014), we split the sample by [moderator] into [high group] and [low group] and estimate the [predictor]–[outcome] correlation separately for each group. The correlation is [value] (p [relation] [threshold]) for [high group] and [value] (p [relation] [threshold]) for [low group]. The difference between these correlations is [significant/not significant] according to the [Fisher z-test / χ² test for equality of correlations] ([statistic] = [value], p [relation] [threshold]). Thus, Hypothesis [x] is [supported / not supported].
```

**differential validity QC**: 
- 必须报告两组各自的相关系数及其显著性，不能只报告差异检验；
- 若使用分组回归系数而非相关系数，需在 Methods 中说明理由，否则不能声称检验的是 "strength"；
- 分组标准必须透明（median split / quartile / 理论阈值），并在 Methods 中预告。

**IV/2SLS 交互效应变体**（second-stage 含交互项时）：
```text
Hypothesis [x] predicted that [moderator] would moderate the effect of [endogenous predictor] on [outcome]. Model [y] adds the interaction between the predicted [endogenous predictor] (from the first stage) and [moderator] to the second-stage equation. The [predictor × moderator] interaction term is [direction] and [significant/not significant] ([coefficient], [p-value]). This indicates that the marginal effect of [predictor] on [outcome] [increases/decreases] by [magnitude] for each unit increase in [moderator], evaluated at the predicted values of [endogenous predictor]. Because the model is linear, the interaction coefficient can be interpreted directly; standard errors are [robust/clustered] to account for the two-stage estimation.
```
