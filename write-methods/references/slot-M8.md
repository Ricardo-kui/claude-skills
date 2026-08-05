<!-- write-methods 槽位骨架 M8：由 SKILL.md「槽位骨架加载」按路由决策加载。内容为原 SKILL.md 该槽位段落骨架（通用 + 设计类型变体 + QC），未做语义修改。 -->

### M8. 识别策略 / 效度 / 诊断检验

> **M8 的写作边界**：M8 只写**基准估计所需的识别论证与诊断**，不写 Results 才展开的稳健性检验。例如：IV 的排他性约束、DiD 的平行趋势假设、实验的操纵检验、匹配的共同支撑域——这些是基准识别的一部分。而替代模型、替代测量、子样本敏感性、安慰剂检验等属于 Results（R7/R8）。

**通用填空段落**：

```text
To address concerns about [threat], we [design feature/test]. This check assesses whether [assumption] is plausible. We report the results in [Results/Table/Appendix]. Although [assumption] cannot be directly tested, the evidence below helps reduce concerns about [threat].
```

**自然实验/DiD 变体**：
```text
Our identification strategy relies on [source of variation]. [Shock/event/policy] creates variation in [treatment] that is plausibly exogenous to [outcome] because [reason]. The key identifying assumption is that [treated and control units] would have followed similar trends absent [treatment]. We assess this assumption in the Results section using [event-study/leads-lags] specifications. We first estimate a parsimonious specification because [controls] may be affected by [treatment].
```

**固定效应局限诚实说明变体**（hoffmann_cheong_phan_zurbruegg2024 型 — 二元 rare outcome 下无法加入 firm FE）： 🔬 EXPERIMENTAL（1 篇范文，2026-08-05 重蒸馏）⚠️ 保守替代：省略或脚注提及
```text
It is not possible to include [unit] fixed effects given how our data are structured. Our sample includes [units] that never experience the binary outcome alongside [units] that do, leaving no within-[unit] variation in the dependent variable for the former group; [unit] fixed effects would therefore be perfectly collinear with the outcome. Consistent with prior work in comparable settings ([citation]), we instead include year fixed effects to absorb common temporal shocks and industry fixed effects to absorb time-invariant industry heterogeneity — for example, [industry-specific confound: e.g., product types with different baseline hazard of the outcome]. We further control for observable time-varying [unit] characteristics, including [named controls], that may correlate with both [treatment] and [outcome]. While this approach does not eliminate all [unit]-level confounding, the staggered adoption design and these controls provide meaningful mitigation.
```

**固定效应局限诚实说明 QC**:
- 必须诚实说明为什么不能使用 firm FE（不能假装不存在这个问题）
- **禁止误引 incidental parameters**：若真实理由是 always-zero outcome → perfect collinearity，必须如实写 collinearity，而非泛化为 incidental parameters
- 必须命名具体的 time-varying firm controls 来辩护替代方案（不能只写 "we control for firm characteristics"）
- 必须给出 industry FE 的 because（如产品类型/监管强度差异），不能只说 "we use industry FE"
- 不能声称 "we fully address endogeneity" — 使用 "meaningful mitigation" / "increase confidence" 等诚实措辞

**Staggered DiD 识别栈变体**（hoffmann_cheong_phan_zurbruegg2024 型 — model-free → 机制检验 → 平行趋势 → 安慰剂）： 🔬 EXPERIMENTAL（1 篇范文，2026-08-05 重蒸馏）⚠️ 保守替代：自然实验/DiD 变体
```text
We follow [Goldfarb, Tucker & Wang 2022] guidelines for quasi-experiments in marketing. Our identification relies on staggered adoption of [law/policy] across [jurisdictions], creating variation in [treatment construct] while [assignment rule: e.g., incorporation state] determines exposure.

Before estimating regressions, we present model-free evidence comparing mean [outcome] for exposed versus unexposed [unit-years]. Although our theory centers on [mechanism/threat construct], prior literature documents that [observable manipulation check: e.g., actual filings/behavior] declines significantly after adoption ([citations]), supporting that the shock operates through the theorized channel.

The key DiD assumption is parallel trends. We add pretreatment indicators [Pre(-3)], [Pre(-2)], and [Pre(-1)] and interact each with [TreatGroup]; insignificant pretreatment interactions indicate no detectable pretrend. We also test whether adoption coincided with unrelated changes in [outcome] by conducting a falsification test: we randomly reassign each [unit]'s [jurisdiction attribute] to another [jurisdiction] with different adoption timing, reestimate the model, save the test statistic, and repeat [N] times. If state-level confounds drive the results, placebo assignments should often reproduce significance; the distribution of placebo statistics relative to the true estimate supports identification.

Finally, while adoption itself may not be random, prior work shows that adoption timing is plausibly exogenous ([citation]) and does not affect [assignment rule] ([citation]), reducing selection concerns.
```

**DiD 置换检验预览补充**（可选，置于自然实验/DiD 变体后）：
```text
We also conduct permutation tests by randomly assigning [treatment status/timing] across [N] iterations to assess whether [unobserved characteristics] could drive our results.
```

**内生性/控制函数变体**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：M8 通用段落
```text
Because [timing/choice] may be endogenously chosen in the [outcome] model, we use a control-function approach: first estimate [timing model], then include the first-stage residual in the [outcome model]. [Variable] identifies the first stage because it should affect [timing] but not [second-stage outcome], since [theoretical reason].
```

**测量局限辩护：披露阈值/左删失变体**（当数据存在报告阈值或下限堆积时）： ✓ STANDARD
```text
[Source] reports [measure] only when [threshold/rule], so values below [threshold] appear as zero or are not observed. This rule could introduce measurement error if [firms/actors] cluster just below the threshold or if the threshold varies systematically with [confound]. We examine the distribution of observed [measure] values and find no evidence of bunching around [threshold]; [percentage]% of positive observations exceed [multiple of threshold], and the mean and median positive values ([mean], [median]) are well above the reporting floor. We therefore expect any attenuation from threshold-based measurement error to be limited, and if anything it would bias our estimates toward zero, making significant results harder to obtain.
```

> **披露阈值 QC**:
> - 必须说明具体 threshold/rule
> - 必须检查并报告是否存在 bunching（不能仅假设无堆积）
> - 必须解释为什么该测量误差不至于推翻推断（最好是保守偏误逻辑）
> - 若存在明显堆积，不应使用此变体，应考虑 Tobit / Heckman / 其他删失模型

**实验效度变体**：
```text
To assess the [manipulation] manipulation, participants rated [check item]. Participants in the [condition] condition perceived [construct] as [higher/lower] than those in the [comparison] condition. These results indicate that the manipulation was successful. Results were [unchanged/qualified] when [attention-check/manipulation-check exclusion] was applied.
```

**多研究变体**：
```text
The sample, method, and analyses for Study [x] were preregistered at [repository/link placeholder]. As preregistered, we excluded participants who [criterion], producing a final analytic sample of [N].
```

**IV 排他性约束/过度识别检验变体**：
```text
A threat to our IV strategy is that [instrument] may affect [outcome] through channels other than [endogenous predictor]. We address this concern in three ways. First, we argue theoretically that [instrument] influences [outcome] only through [predictor] because [theoretical mechanism / institutional feature]. Second, we include [control for alternative channel] in the second stage to absorb [potential violation path]. Third, [IF overidentified: we report the Sargan / Hansen J overidentification test ([value], p = [value]), which does not reject the null that all instruments are valid, strengthening confidence in the exclusion restriction. IF just-identified: because the model is just-identified (one instrument for one endogenous variable), overidentification tests are infeasible. We therefore rely on theoretical arguments for the exclusion restriction and conduct placebo tests / sensitivity analyses to assess robustness.]
```

**同伴效应/网络效应 falsification 变体**： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：M8 通用段落
```text
Because [network-based construct] may capture common shocks or sorting rather than true peer influence, we conduct falsification tests. We re-estimate our models using [placebo network: random peers / future peers / peers from unrelated network layer] as the independent variable. If the main effect is driven by common shocks, the placebo network should also yield a significant coefficient. The coefficient on [placebo network] is [not significant / opposite direction / much smaller], suggesting that the [focal network] effect is not an artifact of [common shock / sorting]. We also test [alternative mechanism] by [test description]; the result is [status], further distinguishing [theorized mechanism] from [alternative].
```

**匹配DiD 平行趋势与重叠支撑变体**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：M8 自然实验/DiD 变体
```text
The key identifying assumption is that [treated] and [matched control] units would have followed parallel trends absent [treatment]. We assess this assumption using [event-study / leads-and-lags] specifications in which we include [lead/lag indicators] relative to [event]. The pre-treatment coefficients are [individually / jointly] insignificant ([test statistic] = [value], p = [value]), suggesting no detectable pre-treatment divergence. We also verify overlap by plotting [propensity-score distributions / covariate balance] before and after matching; the [common support region] covers [percentage]% of the sample, and no observations lie outside the [calipersize] caliper.
```

**粗化精确匹配（CEM）/ 匹配解决内生性变体**（非 DiD，仅用匹配加权解决内生性）：
```text
To address concerns about endogeneity — specifically, that [predictor] may be influenced by [past outcome / ongoing confound] — we exploit an exogenous shock: [treatment definition, e.g., a change in the firm's CEO]. We use coarsened exact matching (CEM)-weighted [estimator], matching [treated units] to [control units] on pretreatment variables: [matching variables]. This yields [N] matched strata containing [N treated] and [N control] observations. The CEM-weighted results confirm that [focal effect] remains [status] even when [predictor] changes are exogenously driven.

To validate the exogeneity of [treatment], we demonstrate that [pretreatment outcomes] do not predict the likelihood of [treatment] ([logit/Probit] regression) and do not predict [predictor] levels (panel fixed-effects models). These checks reduce concerns that the [predictor-outcome] relationship is driven by reverse causality or omitted variables related to [confound].
```

**制度/政策体制安慰剂检验变体**：
```text
Because [outcome] may reflect [alternative mechanism] rather than [focal mechanism], we exploit a [regime change] as a falsification test. During the [mandatory regime], [behavior] should not exhibit [focal pattern] because [institutional reason]. We re-estimate our models using [mandatory regime subsample] and find [null effect], consistent with the assumption that [focal mechanism] requires [voluntary regime condition].
```

**部分重叠同伴群体 + 形式化识别证明变体**（网络效应核心识别故事）：
```text
Our identification strategy relies on two features of partially overlapping peer groups. First, because [percentage] of firms operate in multiple industries, peer groups vary at the individual firm level. This breaks the linear dependence between the endogenous peer variable and exogenous peer characteristics that plagues perfectly overlapping groups. Formally, in a perfectly overlapping group, PeerDisclosure is a linear combination of peer characteristics, making identification impossible. With partial overlap, the peer group matrix has full rank because each firm faces a unique combination of peers.

Second, we instrument [endogenous peer variable] with [second-degree peer characteristics], which are plausibly uncorrelated with unobservable shocks affecting the focal firm's [outcome] because second-degree peers are not in the focal firm's peer group. The exclusion restriction is supported by three arguments: (1) [theoretical argument], (2) [mandatory-regime falsification], and (3) [Hansen J-test / statistical argument].
```

**SEM 模型识别变体**（当使用结构方程模型或联立方程时）：
```text
Because we estimate a system of [N] equations simultaneously, we verify model identification before interpreting coefficients. The model has [degrees of freedom] degrees of freedom (positive, indicating over-identification). Each structural equation satisfies the order condition (number of excluded exogenous variables ≥ number of included endogenous variables minus one) and the rank condition (the matrix of excluded exogenous variables has full column rank). For the measurement model, we report confirmatory factor analysis (CFA) fit indices: CFI = [value] (≥ 0.90), RMSEA = [value] (≤ 0.08), and SRMR = [value] (≤ 0.08), indicating acceptable fit. We also report the χ² test ([value], df = [df], p = [value]) as an absolute fit measure, noting that χ² is sensitive to sample size. All factor loadings are significant (p < [threshold]) and exceed [value], supporting convergent validity. The average variance extracted (AVE) for each construct is [value], exceeding the squared correlation between constructs, supporting discriminant validity.
```
