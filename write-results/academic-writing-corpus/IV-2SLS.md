---
result_type: "IV-2SLS"
status: 📋 TEMPLATE
source_papers:
  - "wowak2025_tmt_political_ideology_ms"
variants_count: 3
created: 2026-05-18
updated: 2026-05-20
---

# IV-2SLS — Results 骨架

## 主骨架

参见 `write-results/SKILL.md` → 填空段落骨架 → `IV-2SLS`。

## 证据节奏摘要

- **竞争假设节奏**: 并列双可能性 → 宣布赢家 → 幅度 → 支持判断
- **第一阶段报告**: Partial F-statistic + Sargan/Hansen + Pagan-Hall 嵌入 R3 正文
- **因果语言**: "influence" / "effect" (IV 设计允许)
- **经济显著性**: 1 SD → N-unit change in DV

## 累积变体

### 变体 1: 竞争假设的赢家报告模式 (1/5 复现)
**来源论文**: Wowak2025 MS
**验证状态**: 通过 (竞争假设设计的标准模板)
**写入日期**: 2026-05-20
**槽位**: R3
**骨架**:
> [Table] displays the [stage] regression results of our [estimator] models. [Columns] are the controls-only models for [DV_1] and [DV_2], respectively. [Column] provides our estimates corresponding to Hypotheses [competing_pair]. A [positive] coefficient suggests that [interpretation_for_positive], whereas a [negative] coefficient indicates [interpretation_for_negative].
>
> The results in [Column] indicate that [IV] is a significant [direction] predictor of [DV_1] (β = [value]; p < [threshold]). This finding suggests that [interpretation_supporting_winner], lending support to Hypothesis [winner]. To put this in perspective, our model predicts that [units] one SD more [IV_pole] than the mean [outcome_magnitude].
>
> In [Column], we explore the effect of [IV] on [DV_2], which corresponds to the competing predictions in Hypotheses [competing_pair_2]. A positive coefficient indicates [interpretation_A], whereas a negative coefficient indicates [interpretation_B]. The results imply the [former/latter] (β = [value]; p < [threshold]), such that [interpretation_supporting_winner]. Our estimator predicts that [units] one SD more [IV_pole] than the mean [outcome_magnitude]. Thus, our results support Hypothesis [winner].
**与原骨架差异**: 竞争假设 (如 H1a vs H1b) 需要在 R3 中同时报告两个方向的可能性，然后用显著性决定"赢家"。关键句式："A positive coefficient suggests... whereas a negative coefficient indicates..." → "The results imply the former/latter"。单一方向假设不需要此骨架。

### 变体 2: Model-Free Evidence 预览 (1/5 复现)
**来源论文**: Wowak2025 MS
**验证状态**: 可选变体
**写入日期**: 2026-05-20
**槽位**: R1/R3 (在正式回归之前)
**骨架**:
> Before discussing regression results, we first explore model-free support for our hypotheses. The mean [DV_1] for [group_A] is [value], whereas it is [value] for [group_B], suggesting that [preliminary_pattern]. By contrast, the mean [DV_2] for [group_A] is [value], but [group_B] tend to [different_pattern].
**与原骨架差异**: 在 IV/2SLS 因果识别之前先用简单均值分组比较建立初步直觉。这降低了读者对"完全依赖复杂计量技术"的疑虑。适用于任何设计——尤其是因果识别设计——但仅在 Wowak2025 中出现。

### 变体 3: IV 第一阶段诊断嵌入 R3 (1/5 复现)
**来源论文**: Wowak2025 MS
**验证状态**: 可选变体 (IV 研究的最佳实践)
**写入日期**: 2026-05-20
**槽位**: R2/R3
**骨架**:
> [Our instruments conform to diagnostic tests]. The partial F-statistic exceeds the relevance threshold (partial F-stat = [value]; p < [threshold]), and the [identification_test] does not contain zero [[lower], [upper]]. Diagnostic tests for exogeneity suggest our instruments are unrelated to the structural error terms (Sargan χ² = [value]; p = [threshold]). [For Lewbel: The Pagan-Hall diagnostic fails to reject the null (p > [threshold]), and Breusch-Pagan rejects homoskedasticity (p < [threshold]), upholding both Lewbel assumptions.]
**与原骨架差异**: IV 诊断统计量（partial F, Sargan, Pagan-Hall, Breusch-Pagan）嵌入 R3 正文，而非 relegating 到脚注或 Methods 中。这是因果识别研究的最佳实践——让读者在阅读结果时同时看到识别策略的有效性。

## 句式素材

<!-- 由 distill-results-exemplar Phase 4 自动沉淀的 sentence-level 骨架。填入占位符后可嵌入段落。 -->

### R2 — 模型序列 / 表格导航

**句式 1: `r2_sentence_iv_first_stage_significance`**

> The first-stage results in [Table X] show that our instrument is a significant predictor of [IV] (coefficient = [value], p < [threshold]), and the F-test rejects the null hypothesis of weak instruments (F = [value], p < [threshold]).

**句式 2: `r2_sentence_iv_endogeneity_test`**

> A Wu-Hausman test rejects the null hypothesis of no endogeneity (statistic = [value], p < [threshold]), suggesting that [estimator] is appropriate.

**句式 3: `r2_sentence_iv_overidentification`**

> A Sargan-Hansen test does not reject the null hypothesis that the instruments are exogenous (statistic = [value], n.s.), supporting their validity.

**句式 4: `r2_sentence_progressive_model_sequence`**

> Column [1] of [Table X] shows the results when we run a [estimator] with [IV] and [control variables]. We then add [additional variables] by entering [variable group]. As we report in Column [2] of [Table X], [exogenous peer characteristics] are significant, including [examples]. However, the endogenous [effect] estimate does not change much (β = [value], p < [threshold]).


### R3 — 主假设检验

**句式 1: `r3_sentence_coefficient_significance_iv`**

> Consistent with [Hypothesis X], the coefficient for the predicted value of [IV] is [negative/positive] and statistically significant (β = [value], p < [threshold]).

**句式 2: `r3_sentence_control_variable_direction`**

> [Control_i] displays a significant and [negative/positive] relationship with [DV] (β = [value], p < [threshold]); [interpretation clause].

**句式 3: `r3_sentence_2sls_coefficient_significance`**

> The [estimator] results in Column [Y] of [Table X] show that the coefficient for [IV] is [positive/negative] and statistically significant (β = [value], p < [threshold]), indicating that [interpretation in probability terms].

**句式 4: `r3_sentence_first_stage_diagnostics`**

> The first-stage regression ([Table X], Column [Y]) shows that [number] of [number] instruments have significant effects on the endogenous variable. The R-square of the first-stage regression is [value]; the joint significance test for the instrumental variables is significant (F([df1], [df2]) = [value], p < [threshold]), indicating that we do not have a problem of weak instruments.

**句式 5: `r3_sentence_hansen_j`**

> The Hansen J-statistic for the [estimator] specification (Column [Y] in [Table X]) is [value] (p > [threshold]), indicating that the model is not overidentified.


### R4 — 交互效应 / 条件效应

**句式 1: `r4_sentence_interaction_significance`**

> [Moderator] moderates the effect of [IV] on [DV] (β = [value], p < [threshold]); consistent with [Hypothesis X], [interpretation of direction].

**句式 2: `r4_sentence_indirect_moderation`**

> We find empirical evidence of a [full/partial] indirect moderation effect (β = [value], p < [threshold]); the interaction between [mediator] and [IV] mediates the moderating effect of [moderator].

**句式 3: `r4_sentence_subgroup_coefficient_comparison`**

> The effect of the [subgroup A] is highest (β = [value], p < [threshold]), followed by [subgroup B] (β = [value], p < [threshold]), [subgroup C] (β = [value], p < [threshold]), and [subgroup D] (β = [value], n.s.).

**句式 4: `r4_sentence_wald_test_difference`**

> The Wald test for the difference between the [subgroup A] and [subgroup B] coefficients is statistically significant (F-statistic = [value], p < [threshold]).

**句式 5: `r4_sentence_control_function`**

> We implement a control function approach in which we regress [endogenous variable] on [instruments] and other variables in the first stage and add the error terms from the first stage to [Equation X] as endogeneity correction terms. The endogeneity-corrected estimates (Column [Y] of [Table X]) remain robust, indicating that [conclusion].


### R5 — 经济 / 实质显著性

**句式 1: `r5_sentence_unit_translation`**

> Approximately $[value] more in [IV] is associated with one fewer [DV], assuming a typical average [DV] of [unit].

**句式 2: `r5_sentence_back_of_envelope`**

> If we assume an average, conservative cost of $[value] per [unit] of [DV], one fewer [DV] implies nearly $[value] in savings.

**句式 3: `r5_sentence_probability_change_magnitude`**

> If [IV] increases by [value]%, a [unit]'s [DV] increases by [value]%–[value]%.


### R6 — 非显著 / 混合 / 意外发现

**句式 1: `r6_sentence_null_effect_credibility`**

> We find no [effect] (β = [value], p > [threshold]), as detailed in Column [Y] of [Table X] (i.e., a null effect lends credibility to our argument that [interpretation]).


### R7 — 稳健性 / 效度 / 敏感性

**句式 1: `r7_sentence_threat_positioning`**

> One concern is that our findings depend on [specific threat].

**句式 2: `r7_sentence_test_action`**

> To address this concern, we re-estimate our models using [method].

**句式 3: `r7_sentence_result_unchanged`**

> The results are substantively unchanged (β = [value], p < [threshold]), reducing concerns that [threat] drives the findings.

**句式 4: `r7_sentence_simultaneous_equation`**

> We incorporate the potential correlation of the model errors for [entity A] and [entity B], while also correcting for endogeneity using [estimator].

**句式 5: `r7_sentence_nonlinear_endogeneity`**

> We account for the discrete, ordered nature of [DV] using [nonlinear model], accompanied by a linear model for the endogenous variable [IV].

**句式 6: `r7_sentence_robustness_confirmation`**

> We [still/find] [robust/significant] [effect] ([coefficient], p < [threshold], Column [Y], [Table X]).

**句式 7: `r7_sentence_heterogeneity_attenuation`**

> The interaction between [IV] and [moderator] is [positive/negative] and significant (β = [value], p < [threshold]), indicating that [effect] attenuates as [moderator] increases.

**句式 8: `r7_sentence_multiple_sd_heterogeneity`**

> To see the existence of [effect] at high levels of [moderator], we calculate the [effect] when [moderator] is at mean, one standard deviation above mean, [one and a half] standard deviations above the mean, and two standard deviations above the mean. The effect sizes are [value] (p < [threshold]), [value] (p < [threshold]), [value] (p < [threshold]), and [value] (p < [threshold]), respectively, providing evidence for heterogeneity in [effect] across [moderator] levels.


### R8 — 补充 / 事后 / 机制

**句式 1: `r8_sentence_followup_question`**

> We next investigate how [mechanism] varies, depending on [dimension 1] and [dimension 2].

**句式 2: `r8_sentence_relative_importance`**

> In summary, we find evidence that, on average, [units] [mimic/follow] [peer type A] more so than [peer type B].


