<!-- write-results 槽位骨架 R7：由 SKILL.md「槽位骨架加载」按路由决策加载。内容为原 SKILL.md 该槽位段落骨架（通用 + 设计类型变体 + QC），未做语义修改。 -->

### R7. 稳健性 / 效度 / 敏感性检验

**通用填空段落（按威胁组织，每威胁一段）**：

**测量威胁**： ✓ STANDARD（20+/28 篇范文使用）
```text
One concern is that our findings depend on the specific operationalization of [construct]. To address this concern, we re-estimate our models using [alternative measure] instead of [main measure]. The results are substantively unchanged, reducing concerns that [measurement choice] drives the findings.
```

**模型威胁**：
```text
To ensure that our results are not sensitive to model choice, we re-estimate our models using [alternative model, e.g., Tobit / Poisson / negative binomial / Cox]. The pattern of coefficients is [consistent/qualified], suggesting that [model choice] is unlikely to account for the main pattern.
```

**样本威胁**：
```text
Our results may be sensitive to sample composition. We exclude [specific subsample, e.g., high-tech firms / financial crisis years / outliers] and re-estimate our models. The results [remain consistent/are qualified], suggesting that [sample restriction] does not drive the findings.
```

**时点威胁**： ✓ STANDARD（10+/28 篇范文使用）
```text
To address timing concerns, we use [alternative lag structure / different event window / extended pre-period]. The results are [consistent/qualified], reducing concern that [timing choice] explains the main pattern.
```

**内生性威胁**：
```text
A potential threat to our causal claims is [reverse causality / omitted variables / simultaneity]. To address this concern, we employ [2SLS / matching / control function / natural experiment] using [method]. The [timing/predictor] effect remains [status], suggesting that the relationship is not driven solely by [endogeneity threat].
```

**机制/边界威胁**： ✓ STANDARD（8-10 篇范文使用）
```text
We conducted supplemental analyses to examine whether [alternative mechanism / scope condition] explains the results. When [alternative mechanisms] were included, [focal predictor] continued to explain the effect, whereas [rival mechanisms] did not. This strengthens confidence that [main inference] reflects [theorized process].
```

**替代解释三步反驳变体**（Pontikes 2012 模式：提出替代解释 → 设计实证检验 → 证伪排除）： ✓ STANDARD

```text
[Alternative explanation / rival mechanism] could account for our findings if [condition for rival to hold]. To test this possibility, we [specific empirical test: e.g., restrict sample to subsample where rival should be strongest / add control for rival mechanism / test whether effect persists under rival's predicted condition]. If [alternative explanation] were driving the results, we would expect [pattern that rival predicts]. Instead, we find [opposite / null pattern]. The [focal effect] [persists / remains directionally consistent] even in [the subsample most favorable to the rival], suggesting that [alternative explanation] does not account for the main pattern.

A second alternative is that [second rival]. If this were the case, [empirical implication]. We test this by [test]. Results show [null/support for focal], reducing concern that [second rival] explains the findings.

Taken together, these falsification tests provide evidence against the most plausible alternative explanations for our results.
```

> **替代解释三步反驳 QC**:
> - 每个替代解释必须有可证伪的经验蕴含（如果 rival 为真，数据应显示 X）
> - 不能只用 "future research should examine" 替代实证反驳
> - 反驳逻辑必须对称：如果 rival 成立 → 应看到 pattern Y → 我们没看到 Y → rival 不被支持
> - 建议 2-3 个 rival，按 plausibility 排序，但不超过 4 个

**稳健性的 alternative-strategy 组织变体**（当多种识别/估计策略相互验证时）： ✓ STANDARD
```text
To assess whether our findings are robust to alternative empirical strategies, we conduct four supplemental analyses. First, to address [temporal carryover / dynamic effects], we re-estimate the model using [lagged predictor / stock measure / Koyck model]; the coefficient on [focal predictor] remains [direction/status]. Second, to address [system dependence / correlated error structure], we estimate [simultaneous equation system / 3SLS / GMM] that allows [outcome processes] to be jointly determined; the results are [status]. Third, to exploit [exogenous variation / external shock] outside our main design, we compare [affected units] with [unaffected units] before and after [event] using [DiD/event-study] and find [status]. Fourth, to ensure that the [count/ordinal/censored] nature of [outcome] does not drive the results, we re-estimate using [Poisson / negative binomial / ordered probit / Tobit] and find that [status].
```

> **组织方式选择**：若稳健性检验回应的是同一识别策略下的不同**威胁**（测量/样本/时点/内生性），用 threat-based 段落；若稳健性检验对应的是不同**识别或估计策略**（长短期、联立方程、外生事件、非线性），用 alternative-strategy 段落。两者可混合，但每段只采用一种逻辑。

**受众类型 falsification 专用**（Pontikes 2012 模式，排除一类受众中的子类型混淆）： ✓ STANDARD

```text
One might argue that the results for [audience B] are driven not by [theorized mechanism] but by [confounded subtype within audience B: e.g., corporate VCs pursuing strategic goals rather than financial returns]. To rule out this alternative, we [empirical strategy: e.g., partition audience B into subtypes and re-estimate]. If [confounded subtype] were driving the effect, the coefficient for [focal predictor] should be concentrated in [subtype X] and absent in [subtype Y]. Instead, we find [consistency across subtypes / opposite pattern]. The coefficient for [focal predictor] is [result for subtype A] and [result for subtype B], both [direction/significance]. This pattern indicates that [theorized mechanism]—not [confounded subtype]—drives the main [audience B] result.
```

> **受众 falsification QC**: 仅当理论中区分了多类受众且某一类受众内部存在可观察的异质性时使用

**DiD 平行趋势专用**：
```text
To assess parallel trends, we estimate an event-study model with leads and lags around [event]. The pre-treatment coefficients are [not distinguishable from zero / stable], suggesting no detectable pre-treatment divergence. The post-treatment coefficients [emerge / increase / persist] after [event], which is consistent with [causal / timing claim]. The lack of pre-treatment movement reduces concern that [outcome trend] anticipated or caused [treatment].
```

**替代解释两步排除变体**（hoffmann2024 型 — CONTROL 步 + INTERACT 步）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：替代解释三步反驳变体
```text
A plausible alternative explanation for our main effect is that [alternative mechanism] — rather than [theorized mechanism] — drives the reduction in [outcome] following [treatment]. [Alternative mechanism] logic would predict that [treatment] changes [outcome] because [rival causal chain: e.g., firms improve governance in response to law, which independently reduces incidents that would trigger [outcome]], not because [theorized mechanism: e.g., managers facing lower litigation risk become less vigilant].

We rule out this alternative through a two-step empirical strategy. 

First, we CONTROL for [alternative mechanism proxy] directly. Model [x] of Table [y] adds [control variable(s)] measuring [alternative mechanism]. If [alternative mechanism] were driving the main effect, including these controls should attenuate or eliminate the [treatment] coefficient. Instead, [treatment] remains [direction] and statistically significant ([coefficient], [p-value]), and its magnitude is [qualitatively similar / only modestly reduced] compared to the baseline specification. This indicates that [alternative mechanism] does not account for the main effect.

Second, we INTERACT [treatment] with [alternative mechanism proxy]. If [alternative mechanism] logic holds, the effect of [treatment] should be [stronger/weaker] when [alternative mechanism] is [more/less] operative. Model [z] tests this by adding [treatment × alternative mechanism proxy]. The interaction is [not statistically significant / direction opposite to alternative mechanism prediction] ([coefficient], [p-value]), inconsistent with the [alternative mechanism] account.

Combined, these two tests — direct control and interaction — provide converging evidence against [alternative mechanism] as an alternative explanation for our findings.
```

**替代解释两步排除 QC**:
- CONTROL 步必须使用与 main specification 相同的模型规格（仅增加替代机制变量）
- INTERACT 步的交互项方向必须有明确的理论预测（如果 rival 为真，交互应为正/负）
- 两步必须都通过才算排除——仅 CONTROL 步通过（系数不变）但 INTERACT 步显著 → rival 部分成立
- 替代机制变量不能与核心自变量高度相关（r > .7），否则 CONTROL 步的 "系数不变" 是多重共线性造成的假象

**DiD 置换检验专用**： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：省略
```text
We conduct permutation tests by randomly assigning [treatment/timing] and re-estimating the model. The placebo estimates center around [null pattern], whereas the observed estimate is [relative location]. This reduces concern that the main result is an artifact of the panel structure or treatment timing.
```

**实验排除标准专用**： ✓ STANDARD（5-6 篇实验范文复现）
```text
Results were [unchanged/qualified] when [alternative exclusion/coding rule] was applied, suggesting that the findings are not driven by [exclusion choice].
```

**IV 有效性专用**：
```text
To assess whether [instrument] satisfies the exclusion restriction, we conduct [overidentification test / placebo test / sensitivity analysis]. The [Sargan / Hansen J] test yields [value] (p = [value]), [failing to reject / rejecting] the null that all instruments are exogenous. We also estimate the model using [alternative instrument / limited information maximum likelihood] and find that the [predictor] effect remains [status], reducing concern that [instrument validity] drives the results.
```

**匹配DiD 重叠支撑专用**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：R7 内生性威胁 + 增加重叠支撑说明
```text
To ensure that our findings are not sensitive to matching specification, we re-estimate the model using [alternative matching method: kernel / radius / one-to-many] and [alternative caliper]. The treatment effect remains [status] across all specifications. We also test whether results differ inside and outside the common support region; restricting the sample to [propensity score range] yields [similar / slightly larger] estimates, suggesting that [lack of overlap] is not driving the null or significant result.
```

**空间安慰剂检验专用**（DiD / 自然实验）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：R7 内生性威胁 + 增加安慰剂说明
```text
A potential threat is that [treatment] is correlated with unobserved [regional trends]. To address this concern, we conduct a placebo test using [treatment in neighboring units]. Because neighboring units likely share similar [regional characteristics], if unobserved regional trends drive the results, we would expect [neighboring treatment] to also yield a significant effect. The coefficient on [neighboring treatment] is [not significant / indistinguishable from zero], whereas the focal effect remains [status], reducing concern that [regional trends] explain the main pattern.
```

**事件研究稳健性专用**（替代事件日期）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：R7 时点威胁 + 增加替代日期说明
```text
To address concerns about event date exogeneity, we replicated the event study using [alternative event date, e.g., defect awareness date / subsequent trading day] as the event. The CARs are [not significant / consistent], reducing concern that [timing choice] explains the main pattern.
```

**市场地位/主导企业固定效应专用**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：R7 样本威胁
```text
Our results may be sensitive to [market position / dominant firm dynamics]. To address this concern, we add [leader / dominant firm] x year fixed effects to absorb time-varying shocks specific to [market leaders]. The [focal effect] remains [status], suggesting that [market position] does not drive the findings.
```

**同伴效应/网络效应 falsification 专用**： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：R7 内生性威胁
```text
To distinguish true peer influence from common shocks or sorting, we re-estimate the model using [placebo network: random assignment / future peers / unrelated network layer]. The coefficient on [placebo network] is [not significant / much smaller / opposite direction] (β = [value], p = [value]), whereas the coefficient on [focal network] remains [status]. This pattern suggests that the [focal network] effect is not an artifact of [common shock / sorting]. We also conduct a [spillover / leave-one-out] test and find [result], further supporting [theorized mechanism].
```

**推断二元结果阈值敏感性专用**： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：R7 测量威胁 + 增加阈值说明
```text
Because [binary outcome] is inferred using a threshold on [continuous signal / classifier probability], we test whether the results are sensitive to [threshold choice]. We reclassify [outcome] using [threshold – 1 SD / median / domain-specific cutoff] and re-estimate the models. The [predictor] effect remains [status] across all thresholds, indicating that [inference rule] does not mechanically produce the result. We also report [precision / recall / F1] at each threshold in [Appendix Table X].
```

**稳健性检验汇总表变体（Aim / Tests / Results / Details 四列）**（Li et al. 2025 JSCM 型）： ✓ STANDARD candidate — 当稳健性/内生性检验 ≥4 项、跨多种威胁类型时，用一张表总览，正文再逐条展开
```text
Additional analyses (summarized in Table [N]) tested the robustness of the results and addressed endogeneity concerns.

| Aim | Summary of tests | Results | Details |
|-----|------------------|---------|---------|
| [threat 1: e.g., event-window choice] | [what was re-estimated and how] | [consistent / qualified pattern] | [Table / Appendix ref] |
| [threat 2: alternative measures of IVs] | [alternative operationalizations] | [identical / consistent] | [Table ref] |
| [threat 3: selection / endogeneity] | [Heckman two-stage / IV / matching] | [identical after correction] | [Tables ref] |
| [threat 4: alternative data source] | [re-estimate with public/alternative DB] | [similar; often larger] | [Table ref] |
| [threat 5: long-term / alternative DV] | [predict downstream performance] | [consistent direction] | [Table ref] |

[正文随后逐条展开关键检验的设计与结果细节，表格作为导航与总览。]
```
**关键特征**:
- 一张表把所有稳健性/内生性检验的"**目的—做法—结果—出处**"结构化呈现，读者与审稿人可一行一检验地核验覆盖面
- Aim 列按**威胁类型**组织（测量/样本/时点/内生性/替代数据/长期影响），与 R7 threat-based 逻辑一致
- Details 列引用具体表/附录，把分散在多张附录表的检验**可追溯地索引**
- 表格做总览，正文仍逐条展开关键检验的**细节与解释**——表格不替代文字论证

**适用**: 稳健性检验 ≥4 项、跨多种威胁类型的研究（event study + 内生性 + 替代数据 + 长期效应的组合尤为典型）；正文篇幅紧张、需要紧凑呈现多重检验时

**禁忌**:
- 表格不能替代正文对关键检验（尤其内生性/识别策略）的**细节论证**——审稿人仍需读到检验设计与系数
- Results 列不可只写 "consistent"——必须点明**在哪个维度**一致（符号/显著性/量级），并对部分一致的检验诚实标注 "qualified"（如某调节只在长窗口一致）
- 若某检验结果与主分析不一致，必须在表格和正文**同时披露**，不可只在正文脚注里提

**Specification-Curve / Epistemic Map 变体（可视化规格稳健性）**（Lee & Wang 2026 型, following King, Goldfarb & Simcoe 2021）： ✓ STANDARD 候选 — 当稳健性维度是"分析者规格选择"（clustering level × sample restriction × control set）而非具体识别威胁时，用一张图展示系数跨全部规格组合的稳定性

```text
To further assess the robustness of our findings to analyst degrees-of-freedom in specification choice, we develop an epistemic map of the coefficient on [predictor] ([Citation: King, Goldfarb, & Simcoe, 2021]). Specifically, we plot the coefficient and its [95% confidence interval] across all combinations of [specification dimensions: e.g., four clustering levels × two sample restrictions × two control-set choices], yielding [N_total_models] specifications. [Figure X] shows that all [N_total_models] coefficients are [of the predicted sign / greater than zero], and [N_significant] of them are statistically significant at the [threshold] level. The coefficients cluster tightly around the main estimate (β ≈ [value]), indicating that the magnitude of the effect is not sensitive to how the analyst chooses among these reasonable specifications. These robustness checks collectively demonstrate that our findings are not driven by model specification or sample composition.
```

**关键特征**:
- **可视化而非表格**: 与 threat-based 表格（Aim / Tests / Results / Details）按威胁汇总不同，specification curve 把系数 + CI 跨全部规格组合绘制在一张视觉画布上，读者一眼看到系数分布与显著性边界
- **规格选择，非识别威胁**: threat-based 稳健性回应具体识别担忧（omitted variables, reverse causality）；specification curve 系统性地变化"合理的分析者选择"（聚类层级、样本限制、控制变量纳入）来展示结果不依赖任何单一选择
- **基数显式**: "16 models (4×2×2)" 让读者看到规格空间的精确枚举，防止选择性报告的印象
- **Mass sign test**: "All 16 coefficients > 0" 是简单但有力的汇总，与视觉互补——符号在全部规格空间稳定

**适用**: 观察性研究中分析者自由度较大（多种聚类层级、样本限制、控制变量规则都合理）的设计；尤其适用于面板 / FE 设计（facility / firm / industry / state 多种聚类层级并存时）

**禁忌**:
- 规格维度必须与识别威胁正交——specification curve **补充而非替代** threat-based 稳健性；若 reverse causality 是担忧，specification curve 单独不能回应
- 必须**全部 [N_total_models] 规格**都报告；不可选择性省略不显著的规格
- 图必须显示 CI，不能只画点估计——读者需同时判断符号稳定性与显著性稳定性
