<!-- write-results 槽位骨架 R4：由 SKILL.md「槽位骨架加载」按路由决策加载。内容为原 SKILL.md 该槽位段落骨架（通用 + 设计类型变体 + QC），未做语义修改。 -->

### R4. 交互效应 / 条件效应

> **图设计纪律**：交互效应图的纵轴起点、方向选择与"论点明言"规则（"If the table or figure supports a point, state it"）见 `visual-evidence.md` §1/§5——截断纵轴会夸大两线斜率差异，若非零点起标必须在 caption 或正文明示。

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

**联合调节 "Switch-Off" 高百分位中和变体**（hoffmann2024 型 — 文本式）： 🔬 EXPERIMENTAL（1 篇范文；2026-08-05 重蒸馏校准）⚠️ 保守替代：DiD 调节专用 + 分别报告两个交互项
```text
As a final sensitivity analysis, we explore whether there are conditions where [moderator 1] and [moderator 2] do not just weaken the effect of [treatment] on [outcome], but can effectively "switch it off." In this regard, we find that when the values of [moderator 1] and [moderator 2] are both at or above those representing the [90th percentile], the [negative/positive] effect of [treatment] on [outcome] is neutralized. However, note that due to the limited overlap of the distributions of [moderator 1] and [moderator 2], only for [X]% of all [unit]-observations, both cutoff levels are concurrently met. In other words, the effect of [treatment] extends to almost all [units].
```

**联合调节 Switch-Off 高百分位 QC**（hoffmann2024 校准）:
- 必须在 **两个 moderator 分别显著** 之后报告；标注为 sensitivity / final analysis，非新假设
- 阈值必须透明（如 90th percentile）；**必须报告联合满足阈值的样本占比**——否则 switch-off 易过度解读
- 原文 **无** 2×2 场景图；以 predicted-probability 计算 + 文本中和为主；若有 Figure 则为可选增强
- "extends to almost all firms" 类收束句把边界条件叙事从 **机制有效** 拉回 **普遍适用性**

**联合调节变量 "Switch-Off" 四场景图变体**（扩展范式；hoffmann 未用）： 🔬 EXPERIMENTAL ⚠️ 保守替代：上方高百分位中和变体
```text
Our theory predicts that [moderator 1] (an [intrinsic] constraint) and [moderator 2] (an [extrinsic] constraint) each independently weaken the [direction] effect of [treatment] on [outcome]. To provide a more complete picture of how these constraints jointly shape [outcome] decisions, we examine what happens when both constraints are simultaneously present versus absent.

We define four joint-constraint scenarios based on [moderator 1] and [moderator 2] being at their [low/high] levels ([operational cutoff: e.g., above/below median]). Figure [x] plots the predicted probability of [outcome] under [treatment = 0] versus [treatment = 1] for each scenario.

When [treatment] is absent, the predicted probability of [outcome] is [relatively stable / low / high] across all four scenarios, ranging from [X%] to [Y%]. When [treatment] is adopted, predicted probabilities diverge sharply across scenarios. In the [worst-case] scenario — where both constraints are absent ([moderator 1] = low, [moderator 2] = low) — [treatment] is associated with a [large] [decrease/increase] in [outcome] probability, from [baseline%] to [post-treatment%]. In the [best-case] scenario — where both constraints are present ([moderator 1] = high, [moderator 2] = high) — the difference between [treatment] and [no treatment] [narrows substantially / becomes statistically indistinguishable from zero].

This "switch-off" analysis — documenting that the main effect is strongest when both constraints are absent and weakest (or absent) when both are present — provides a holistic view of how [intrinsic] and [extrinsic] governance mechanisms jointly shape [agent] decision making.
```

**联合调节四场景 QC**:
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

**交叉/翻转型调节变体（moderator 反转符号）+ 可选 dissociation**（Cutolo & Ferriani 2024 型）： 🔬 EXPERIMENTAL（1 篇范文）— 当 buffering moderator 不只衰减负效应而**完全翻转**它（penalty → premium），且/或对两组 actor 方向相反时
```text
To elucidate the practical implications, using estimations from the fully specified model (Model [x]), we compare the [outcome units, e.g., sales] for [focal / atypical group] at different levels of [moderator]. After controlling for [key controls], the results show that when [focal group] [is low on moderator], they [experience] [N_fewer] [outcome units] than [reference / typical group]. However, increasing [moderator] [eliminates / overturns] this [penalty]: at the [maximum] level of [moderator], [focal group] [achieve] [N_more] [outcome units] than [reference group]. Figure [x] plots predicted [outcome] against [moderator] for both groups and illustrates the [crossover / sign reversal].
[Optional dissociation] Interestingly, the main effect of [moderator] is [opposite in direction] (β = [value], p [relation] [threshold]) — [moderator] [benefits the focal group but does not help / even harms the typical group]. This [dissociation] suggests that [the mechanism, e.g., processing-fluency benefit] operates for [focal group], for whom [the mechanism's precondition holds], but not for [typical group].
```
**关键特征**:
- **不只"衰减"而"反转/翻转"**: 报告 moderator 把主效应从显著负（penalty）翻转为显著正（premium）——比通用 R4 的 "stronger/weaker" 更强的叙事，直接展示 moderator 的 substantive 威力
- **双极端量化**: at minimum moderator = −[N_fewer]; at maximum = +[N_more]，把 crossover 的经济意义用 outcome units（如 sales 数）做实（配合 R5 经济显著性）
- **dissociation 诚实披露**: 若 moderator 的 main effect 与 interaction 方向相反（对 focal group 有利但对 typical group 无益/有害），必须披露——这是机制有边界条件的信号（机制只在某组成立），不是缺陷
- **图形辅助 crossover**: plotted predicted values at [low/high] moderator 让 sign reversal / 两线交叉可视化

**适用**: buffering moderation 研究中 moderator 完全翻转主效应（penalty→premium）的情况；任何带 sign reversal / crossover 的交互；调节机制对两组 actor 作用方向不同的 differential effect

**禁忌**:
- 必须报告 min 和 max 两个极端的**具体值**（outcome units），不能只说 "the penalty was overturned"
- dissociation **不可隐藏**——若 moderator 对 reference group 有害却只报告对 focal group 的好处，是选择性披露，审稿人会质疑
- crossover 点（moderator 在何值时净效应 = 0）若可估计（如 margins, at）应报告，让读者知道"需要多高的 moderator 才能翻身"
- 若主效应在 moderator 高位翻转为正，需在 Discussion 解释**为何翻转**（不能只报数字）——通常对应"moderator 不只抵消 penalty 还带来独立收益"

**连续调节双重量化变体（±1SD 端点对比 + 百分位边际效应轨迹）**（Abdurakhmonov, Ingram & Ridge 2026 型）： ✓ STANDARD 候选 — 适用于连续 DV 的调节效应报告，把"幅度量化"和"形状可视化"配对呈现

```text
Hypothesis [x] posits that [moderator] weakens the effect of [predictor] on [outcome]. The interaction term is [negative/positive] and statistically significant in Model [y] (β = [value], p < [threshold]), indicating that when [moderator] is [high], the positive relationship between [predictor] and [outcome] diminishes. In practical terms, as displayed in [Figure Xa], when [moderator] is low, increasing [predictor] from one standard deviation below to above the mean leads to a [A]% increase in [outcome], but when [moderator] is high, the same increase yields only a [B]% increase [— or "has virtually no effect"]. [Figure Xb] further visualizes this moderation by showing that the marginal effect of [predictor] decreases steadily across percentiles of [moderator], falling from strongly positive at the 1st percentile to near zero [or slightly negative] at the 95th percentile. Thus, Hypothesis [x] is supported.
```

**关键特征**:
- **双重量化**: (a) ±1SD 端点对比用 % DV 量化幅度（如 10.7% vs 1.1%），让读者看到 moderator 从低到高时效应衰减的绝对量级；(b) 百分位边际效应轨迹图（1st→95th）展示效应衰减的完整形状（线性下降 / 从显著正到近零或微负）
- **端点对比与轨迹图互补**: 端点对比回答"衰减多少"，轨迹图回答"如何衰减"——两者配对比单一 ±1SD simple slopes 或单一交互图信息量更大
- **轨迹的言语化**: 不只展示图，还用一句话描述曲线形状（"decreases steadily... falling from strongly positive at the 1st percentile to near zero or slightly negative at the 95th percentile"），让读者不看图也能抓住 moderation 的动态
- **连续 DV 专用**: 与 R5 Hoffmann 25th→75th 变体（二元 DV 预测概率）互补——本变体用于连续结果（指数得分、金额、rating）

**适用**: 任何连续 DV 的调节效应报告（OLS / FE / GEE / panel）；moderator 为连续变量且理论预测"效应随 moderator 升高而衰减至近零"的 weakening moderation

**禁忌**: 端点对比必须报告具体 %（如 10.7% vs 1.1%），不能只说 "stronger when low, weaker when high"；轨迹描述必须标明百分位范围（1st→95th 或 5th→95th），不能只说 "decreases across percentiles"；若效应在高位翻转为相反符号（penalty→premium），应改用上方「交叉/翻转型调节变体」而非本变体；本变体不替代交互项显著性报告——必须先报告 β_interaction + p，再进入双重量化
