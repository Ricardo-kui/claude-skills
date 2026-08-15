<!-- write-results 槽位骨架 R8：由 SKILL.md「槽位骨架加载」按路由决策加载。 -->

### R8. 补充 / 事后 / 机制分析

**分析定位与导航（强制）**：先将每项分析标记为 confirmatory mechanism、rival explanation、corroborating evidence、heterogeneity 或 exploratory extension，并在标题和判决中维持该证据地位。不同分析原则上使用独立、问题导向的小标题。若变量或样本信息已从 Methods 移出，首次出现时必须自包含地给出数据源、操作化、时间窗口和样本边界。

**段落逻辑**：机制和竞争解释段落按“理论预测/竞争预测 → 可观察含义 → 检验匹配 → 结果 → 判决与边界”组织。该链条是功能约束，不是统一四句模板；应从 corpus 中选择与当前功能匹配的句法并段落级改写，避免逐项罗列。

**通用填空段落**：

```text
We conducted supplemental analyses to examine [mechanism/boundary/alternative explanation]. This analysis helps assess whether [interpretation] rather than [alternative] explains the results. The results are [consistent with the proposed mechanism / provide a boundary condition / offer an exploratory extension]. These findings should be interpreted as [confirmatory/exploratory] evidence for [claim].
```

**机制检验专用**： ✓ STANDARD（8-10 篇含机制检验范文复现）
```text
We tested [mediation/moderated mediation] using [method] with [bootstrap samples]. The interaction predicted [mediator], and [mediator] predicted [outcome]. The indirect effect through [mediator] was [status] for [condition] but [status] for [comparison], and the difference between indirect effects was [status]. Because [alternative mechanisms] could also explain the pattern, we included [rival mediators] in the model. The focal mechanism [remained/did not remain] while the alternative mechanisms [did/did not] account for the effect.
```

**替代机制排除专用**（多机制竞争检验）： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：通用 R8 段落 + 增加竞争机制说明
```text
To examine whether [focal mechanism] rather than [alternative mechanism A] or [alternative mechanism B] explains the [predictor → outcome] relationship, we estimate [model] including [focal mediator], [alternative mediator A], and [alternative mediator B] simultaneously. Column [a] shows that [focal mediator] is [status] while [alternative A] is [status]. Column [b] adds [alternative B]; the coefficient on [focal mediator] [remains stable / attenuates], whereas [alternative B] is [status]. This pattern suggests that [focal mechanism] is the primary channel through which [predictor] affects [outcome], although we cannot rule out [remaining alternative] entirely.
```

**假设验证 / Corroborating Evidence 专用**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 R8 段落
```text
We conducted supplemental analyses to verify [theoretical assumption]. Using [alternative data source / proxy], we examine whether [assumption] holds in our context. The results [support / do not support] the assumption that [theoretical claim]. Because [proxy] is an imperfect measure of [construct], these findings should be interpreted as [supportive / suggestive] rather than definitive evidence.
```

**MCMC / 模拟中介专用**（当使用贝叶斯模拟检验中介时）： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：通用 R8 段落 + 增加模拟说明
```text
We used MCMC simulation with [N, e.g., 20,000] draws to test whether [mediator] mediates the relationship between [predictor] and [outcome]. The results indicate [partial / full / no] mediation for [condition] but [status] for [comparison]. A moderated mediation analysis confirms that the indirect effect is significantly moderated by [moderator]. These findings should be interpreted as [exploratory / suggestive] evidence for the mediating role of [mediator].
```

**辅助方程闭合专用（同时方程）**：
```text
Finally, Table [x], Column [y] reports the results for [auxiliary equation], which we included in Methods to address [reverse-path concern]. The pattern is consistent with the idea that [reverse path] is accounted for, while remaining secondary to the main hypothesis tests.
```


**跨组不对称中介变体（机制对一组成立、对另一组为 null）**（Falchetti, Cattani & Ferriani 2022 型）： 🔬 EXPERIMENTAL（1 篇范文）— 当同一中介在两组（如 novice vs expert）分别检验时，对一组显著、对另一组为 null
```text
To unpack the underlying cognitive process, we measured [mediator] and ran a mediation analysis (PROCESS model [N], [N] bootstrap samples) — separately for [group A] and [group B]. For [group A], a one-way ANOVA showed that [IV] increased [mediator] (F([df1],[df2]) = [value], p [rel] [threshold]; M_[cond1] = [value] vs M_[cond2] = [value]), and the indirect effect of [IV] on [DV] through [mediator] was [significant] (b = [value], SE = [value], 95% CI [[lo]; [hi]]). For [group B], by contrast, [IV] had no effect on [mediator] (F([df1],[df2]) = [value], p [rel] [threshold]), and the indirect effect through [mediator] was [not significant] (b = [value], 95% CI [[lo]; [hi]]). We also tested [alternative mediators, e.g., positive/negative affect] as parallel mediators; none were significant for either group. Hence, [mediator] is the mechanism underlying [group A]'s evaluation, whereas for [group B] other mechanisms may be at work.
```
**关键特征**:
- **诚实报告跨组不对称**: 同一中介对一组显著、对另一组 null——不掩盖 null，而是把它框定为"机制本身有受众/组别边界"的发现（与 R6 null/mixed 透明原则一致）
- **逐组报告完整中介链**: 每组都报 IV→M 的 ANOVA + 间接效应 bootstrap CI，让读者看到 null 出现在哪一环（IV→M 断裂？还是 M→DV？）
- **排除竞争中介**: 把替代中介（如 affect）作为 parallel mediators 测并排除，强化"该机制对 A 组特定"的结论
- **Discussion 升级 null**: null 组的机制悬置为 "other mechanisms may be at work"，为 future research 留口（如专家可能用 convergent thinking / feasibility 而非 fluency）

**适用**: 多组/多受众研究中，理论机制预期对各组都成立但实证只对部分组成立；任何跨组 mediation 比较出现不对称（一组 significant indirect effect、一组 null）的情况

**禁忌**:
- 必须逐组报告 IV→M 的 ANOVA 与间接效应 CI，不能只说"中介对 A 成立、对 B 不成立"而无统计细节
- null 中介**不可隐藏**——若只报告显著组而略去 null 组，是选择性披露
- 若理论预测机制对两组都成立但实证只对一组成立，Discussion **必须解释**（不能只报数字），通常指向两组认知路径的质性差异
- "PROCESS model 4 分别跑两组" 与 "moderated mediation (model 7/8/14)" 不同——本变体是分组跑 mediation 后描述性比较，非正式的 moderated-mediation 检验；若要正式检验"中介是否跨组不同"，应用 moderated mediation 而非分组对比

**观察面板中介：Baron-Kenny 步骤 + Bootstrap CI + 间接效应占比 + 工具变量中介变体**（Lee & Wang 2026 型）： ✓ STANDARD 候选 — 适用于观察性面板 OLS/FE 中的中介检验，需要回应"中介本身内生"的审稿质疑

```text
To examine whether [mediator] transmits the effect of [predictor] on [outcome], we adopt two complementary approaches. First, following the causal steps framework ([Baron & Kenny, 1986]), we estimate (a) the effect of [predictor] on [mediator] (a-path) and (b) the effect of [mediator] on [outcome] conditional on [predictor] (b-path). [Model 1] shows that [predictor] is [direction] on [mediator] (β = [a-path], p = [value]). [Model 2] shows [mediator] is [direction] and significant on [outcome] (β = [b-path], p = [value]). Multiplying these coefficients, the estimated indirect effect is [a × b ≈ value]. Relative to the total effect (β = [c-total]), the indirect path accounts for approximately [%] of the total effect ([a×b] / [c-total] ≈ [%]), indicating that [interpretation: e.g., "most of the impact operates through [mediator]"].

Second, to corroborate this inference, we implement a non-parametric bootstrap with [N] replications. The bootstrapped estimate of the indirect effect is [value] (SE = [value], z = [value], p = [value]); the 95% confidence interval [[lower], [upper]] does not include zero, confirming the statistical and economic significance of the mediation. Because the mediator may itself be endogenous, [Model 2] instruments [mediator] with [instrument(s)] to address mediator-endogeneity concerns. Together, these two approaches provide compelling evidence that [predictor] affects [outcome] substantially through [mediator].
```

**关键特征**:
- **双重方法相互印证**: 因果步骤框架（Baron-Kenny）提供直觉，非参数 bootstrap 提供推断稳健性——明确框定为相互印证而非相互竞争（不可只用 causal steps 而无 bootstrap，Hayes 2009 批评）
- **间接效应占总效应的比例**: 报告 "indirect = X% of total effect"（如 70%）把抽象的 a×b 乘积转化为实质可理解的份额——直接回答"总效应中有多少通过该渠道传导"。这一量化在 corpus 此前缺失
- **工具变量中介**: 在 b-path 中用 IV 工具化中介变量，回应"中介本身可能内生"的审稿质疑——与普通 OLS 中介不同，适用于观察性面板中行为 / 物质中介（废物处理、研发支出、检查频率）可能受同一未观测因素影响的情况
- **经济重要性诠释**: bootstrap CI 解读为同时确认统计显著性和经济重要性，延伸了"CI 不含零"的标准解读

**适用**: 观察性面板 OLS/FE 研究中（a）中介是可测量的行为 / 物质构念，（b）中介内生性是可信担忧，（c）总效应可被有意义地分解为份额

**禁忌**:
- "间接占比"的计算假设总效应定义良好且稳定；若总效应小、噪声大、或跨规格变动，% 不稳定，应保守报告
- 工具变量中介需要独立的排除限制论证（通常在 Methods），不能在 Results 中默默引入
- 不可只报告 "indirect = 70%" 而无 bootstrap CI——% 是点估计，CI 传达不确定性
- a-path 不显著时（如本文 β=−0.002, p=0.115），仍可基于 bootstrap CI 报告中介显著——但**必须诚实披露 a-path 的边缘性**，不可掩盖
