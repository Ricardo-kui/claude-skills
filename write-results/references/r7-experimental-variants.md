<!-- write-results R7 实验变体库：slot-R7 的 EXPERIMENTAL 伴生文件。不入 slot-R*.md glob（I14 冻结：槽位文件名与 9 槽数不变）；全部变体 🔬 EXPERIMENTAL（单源或未经范文蒸馏验证），各带保守替代指针；蒸馏验证后回迁 slot-R7.md 并升档。段落写作受 slot-R7.md「R7 段落级体裁 QC」约束。 -->

# R7 实验变体库（EXPERIMENTAL）

## A. 专用实验变体（范文单源）

**Top-firm 集中度样本敏感性变体**（hoffmann2024 型）： 🔬 EXPERIMENTAL（1 篇范文；2026-08-05 重蒸馏）⚠️ 保守替代：R7 样本威胁 — 排除敏感性
```text
Finally, one might be concerned that our results are influenced by the fact that a few firms, such as [firm examples], account for a substantial proportion of the number of [outcome events]. Hence, as a sensitivity check, we exclude these top [N] [outcome]-producing firms — together accounting for [X]% of all [outcomes] — from our sample and re-estimate our models. [Appendix Table] confirms that our baseline results continue to hold, and so do the moderation effects when examined separately. When including both moderators simultaneously, the interaction effect of [moderator A] remains significant, while that of [moderator B] [only just fails to reach significance at conventional levels (z-statistic = [value]) / remains significant]. In sum, we conclude that our results are generally robust.
```

**替代解释两步排除变体**（hoffmann2024 型 — CONTROL 步 + INTERACT 步）： 🔬 EXPERIMENTAL（1 篇范文；2026-08-05 重蒸馏校准）⚠️ 保守替代：替代解释三步反驳变体
```text
A plausible alternative explanation for our main effect is that [alternative mechanism] — rather than [theorized mechanism] — drives the reduction in [outcome] following [treatment]. [Alternative mechanism] logic would predict that [treatment] changes [outcome] because [rival causal chain: e.g., firms improve governance in response to law, which independently reduces incidents that would trigger [outcome]], not because [theorized mechanism: e.g., managers facing lower litigation risk become less vigilant].

We rule out this alternative through a two-step empirical strategy.

First, we CONTROL for [alternative mechanism proxy] directly. Model [x] of Table [y] adds [control variable(s)] measuring [alternative mechanism]. If [alternative mechanism] were driving the main effect, including these controls should attenuate or eliminate the [treatment] coefficient. Instead, [treatment] remains [direction] and statistically significant ([coefficient], [p-value]), and its magnitude is [qualitatively similar / only modestly reduced] compared to the baseline specification. This indicates that [alternative mechanism] does not account for the main effect.

Second, we INTERACT [treatment] with [alternative mechanism proxy]. If [alternative mechanism] logic holds, the effect of [treatment] should be [stronger/weaker] when [alternative mechanism] is [more/less] operative. Model [z] tests this by adding [treatment × alternative mechanism proxy]. The interaction is [not statistically significant / direction opposite to alternative mechanism prediction] ([coefficient], [p-value]), inconsistent with the [alternative mechanism] account.

Combined, these two tests — direct control and interaction — provide converging evidence against [alternative mechanism] as an alternative explanation for our findings.
```

**DiD 置换检验专用**： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：省略
```text
We conduct permutation tests by randomly assigning [treatment/timing] and re-estimating the model. The placebo estimates center around [null pattern], whereas the observed estimate is [relative location]. This reduces concern that the main result is an artifact of the panel structure or treatment timing.
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

## B. 六维框架扩展（Yuan et al. 2026 JOM）
## 六维框架扩展：Preprocessing & Covariate Variation（Yuan et al. 2026 JOM）

> 以下子变体源自 Yuan et al. (2026, *Journal of Management*) 对 1,706 篇管理学期刊文章的系统性审查。该论文发现预处理变异在不到 30% 的子研究中被报告，协变量变异虽有中等覆盖率（69.8%）但缺少标准化报告模板。所有新增变体均为 🔬 EXPERIMENTAL，在 distill-results-exemplar 从已发表论文中验证对应模式之前保持此标记。

### Preprocessing Variation（预处理变异）

论文 REC B3.4 建议对所有研究设计实施预处理稳健性检验——因为这些检验不需要额外数据收集。

**预处理威胁 — 缺失数据处理**： 🔬 EXPERIMENTAL (Yuan et al. 2026 JOM; 尚未经范文蒸馏验证) ⚠️ 保守替代: 通用 R7 测量威胁段落 + 在 Methods 中增加缺失数据处理说明

```text
Our results may be sensitive to how we handle missing data. To assess this, we compare results across [two or more justifiable approaches: listwise deletion / multiple imputation / full information maximum likelihood (FIML) / mean substitution]. In the primary analysis, we used [primary approach] because [justification]. When we re-estimate the models using [alternative approach], the [focal coefficient] remains [direction] and statistically significant (β = [value], p [rel] [threshold]), and the magnitude is [qualitatively similar / modestly reduced]. This suggests that [missing data treatment] does not drive the findings. [If applicable: When using multiple imputation, we also varied the number of imputations from [M1] to [M2] and the imputation algorithm from [algorithm-A] to [algorithm-B]; results were unchanged.]
```

**预处理威胁 — 离群值/错误观测处理**： 🔬 EXPERIMENTAL (Yuan et al. 2026 JOM; 尚未经范文蒸馏验证) ⚠️ 保守替代: 通用 R7 样本威胁段落 + 增加离群值处理说明

```text
We examine whether our results are sensitive to the treatment of outliers and influential observations. In the primary analysis, we [primary approach: winsorized continuous variables at the 1st and 99th percentiles / excluded observations with |DFBETA| > threshold / used Cook's distance cutoff]. To assess robustness, we compare results when [alternative approach: winsorizing at the 5th and 95th percentiles / using multivariate outlier detection (Mahalanobis distance) / including versus excluding flagged observations]. The [focal coefficient] remains [direction] and significant at conventional levels across all specifications, indicating that [outlier treatment choice] does not affect the conclusions. [If applicable: We also tested whether results are sensitive to univariate versus multivariate outlier detection methods; the pattern is consistent.]
```

**预处理威胁 — 数据转换策略**： 🔬 EXPERIMENTAL (Yuan et al. 2026 JOM; 尚未经范文蒸馏验证) ⚠️ 保守替代: 通用 R7 模型威胁段落 + 在 Methods 中说明转换策略

```text
To ensure that our findings are not artifacts of data transformation choices, we compare results across alternative transformation approaches. In the primary analysis, [primary approach: e.g., we use the natural logarithm of R&D expenditure to address right skewness / we treat the count variable as continuous after log transformation]. As a robustness check, we [alternative approach: re-estimate using the untransformed variable / apply a square-root transformation / use an inverse hyperbolic sine transformation / treat the variable as discrete using a count model]. The coefficient on [focal predictor] remains [direction] and statistically significant (p [rel] [threshold]), suggesting that [transformation choice] does not drive the results. For [skewed count variable with frequent zeros], we further tested whether results differ when treating the variable as continuous versus discrete ([reference: e.g., Kneeland, Schilling, & Aharonson, 2020]); the pattern is [consistent / qualified].
```

**预处理威胁 — 粗心回答筛查**（主要适用于调查/实验设计）： 🔬 EXPERIMENTAL (Yuan et al. 2026 JOM; 尚未经范文蒸馏验证) ⚠️ 保守替代: 通用 R7 样本威胁段落 + 增加筛查说明

```text
We assessed whether our results are sensitive to the inclusion of potentially careless responses. In the primary analysis, we [primary approach: retained all respondents who passed attention checks / excluded respondents completing the survey in less than [threshold] minutes / used [specific screening method]]. To evaluate robustness, we [alternative approach: compared results with and without flagged respondents / applied alternative screening thresholds (e.g., [threshold-A] vs. [threshold-B] minutes) / used a different careless response index]. The [focal coefficient] is [status] whether or not flagged respondents are excluded, and the pattern of results is [consistent / qualified]. This reduces concern that [careless responding] accounts for the findings.
```

### Covariate Variation（协变量变异）

论文 REC B3.3 指出协变量变异是**最普遍报告**的稳健性维度（69.8%），但当前缺少标准化段落模板。

**协变量威胁 — 含/不含控制变量对比**： 🔬 EXPERIMENTAL (Yuan et al. 2026 JOM; 尚未经范文蒸馏验证) ⚠️ 保守替代: 通用 R7 模型威胁段落

```text
A concern is that our conclusions may depend on the specific set of control variables included in the models. To address this, we compare results across alternative covariate specifications. Model [X] (baseline) includes only [focal predictor(s)] without controls. Model [Y] adds [core theoretical controls: e.g., firm size, age, leverage]. Model [Z] (our preferred specification) further includes [extended control set]. The coefficient on [focal predictor] changes from [β_baseline] to [β_preferred]—a [magnitude] shift—and remains [direction] and statistically significant across all specifications. This pattern indicates that [focal relationship] is not spuriously driven by the inclusion or exclusion of specific covariates. [If applicable: We also used a data-driven approach (e.g., LASSO / double selection) to identify alternative covariate sets; the [focal coefficient] remains stable.] [If focal coefficient substantially changes magnitude: Although the coefficient magnitude attenuates when [specific control] is added, the direction and significance remain stable, suggesting that [control] accounts for some variance but does not eliminate the relationship.]
```

**协变量威胁 — 替代控制变量集（含 DAG/理论辩护）**： 🔬 EXPERIMENTAL (Yuan et al. 2026 JOM; 尚未经范文蒸馏验证) ⚠️ 保守替代: 通用 R7 模型威胁段落 + 增加控制变量敏感性说明

```text
Theoretical guidance on which covariates to include is sometimes ambiguous. To assess whether our results are sensitive to uncertainty in covariate selection, we compare our preferred specification against [two / three] alternative control-variable sets derived from [theoretical rationale / Directed Acyclic Graph (DAG) analysis / prior studies]. Set [A] includes [description]. Set [B] replaces [controls] with [alternative controls] because [theoretical justification]. Across these alternative sets, the coefficient on [focal predictor] ranges from [β_min] to [β_max], all [direction] and [status: e.g., statistically significant at p < .05 / consistent in direction but varying in significance]. The stability of [direction] across theoretically motivated covariate sets reduces concern that [covariate selection uncertainty] drives the findings. [If including mediators as controls is a risk: Importantly, we do not include [mediator variables] as controls because doing so would bias the estimate of [focal predictor] (per Bernerth et al., 2018; Hünermund, Louw, & Rönkkö, 2025).]
```

### Subsampling Variation 细化：Theory-Driven Subsampling（新增）

原"样本威胁"段落已重命名为"样本威胁 — 排除敏感性"（见 `slot-R7.md`）。新增理论驱动子样本变体：

**样本威胁 — 理论驱动子样本变异**（新增）： 🔬 EXPERIMENTAL (Yuan et al. 2026 JOM; 尚未经范文蒸馏验证) ⚠️ 保守替代: 通用 R7 样本威胁段落（排除敏感性变体）

```text
To examine whether our findings generalize across theoretically meaningful subgroups, we re-estimate our models within subsamples defined by [theoretically relevant moderator: e.g., firm size (above/below median) / industry (manufacturing vs. services) / time period (pre- vs. post-regulation) / demographic group]. If the [focal effect] were driven by a specific subset of the data, we would expect the coefficient to be concentrated in [subgroup A] and absent in [subgroup B]. Instead, we find that [focal predictor] is [direction] and [significant / not significant] in both [subgroup A] (β = [value], p = [value]) and [subgroup B] (β = [value], p = [value]). The [similarity / difference] in coefficients across subgroups [supports generalizability / reveals a boundary condition that warrants further theorizing]. [If applicable: We also employed random subsampling ([N] draws of [X%] of the sample) and find that the [focal coefficient] is [direction] in [Y%] of draws, with a mean coefficient of [value] (95% CI [[lo], [hi]]), consistent with the full-sample estimate.]
```

### Fragility / Direct Reporting of Divergent Findings（新增）

对应论文 Section D——当稳健性检验结果**不一致**时的诚实报告范式。

**稳健性检验结果不一致时的诚实报告**： 🔬 EXPERIMENTAL (Yuan et al. 2026 JOM Section D; 尚未经范文蒸馏验证) ⚠️ 保守替代: 通用 R7 段落（unchanged 表述）+ 在 Discussion 中讨论不一致

```text
[When some robustness checks yield divergent results — DO NOT hide behind "results are unchanged":]

Most robustness analyses preserve the [direction and significance] of the [focal relationship]: [summarize 2-3 supporting checks briefly]. Under [specific divergent test], however, the coefficient on [focal predictor] is [attenuated / not significant / directionally inconsistent] ([specific result]). This divergence bounds the relationship to [specific sample, measure, period, or analytical condition] and leaves [remaining uncertainty] unresolved. The overall evidence is therefore [qualified / mixed], despite [baseline verdict].

[When ALL major robustness checks are consistent — the standard happy path:]

Across all robustness analyses, the [focal coefficient] remains [direction] and statistically significant, regardless of [measurement choice / model specification / sample composition / preprocessing decision / covariate set / estimator]. The consistency of the findings across [N] distinct analytical alternatives substantially reduces concern that the results are artifacts of specific analytical choices. Table [X] provides a structured summary of all robustness tests, their rationale, and their results.
```

> **Fragility Reporting QC**:
> - Divergent findings MUST appear in both the main text AND any robustness summary table
> - Every divergent result needs a substantive interpretation (boundary condition / measurement sensitivity / theoretical contingency), not just "results differed"
> - If more than 50% of robustness checks diverge, the primary finding itself should be qualified (e.g., "the evidence is mixed" rather than "supported")
> - Journal space constraints are NOT a valid reason to hide divergent findings — use online supplements if needed (Yuan et al. 2026 REC C3)
