---
result_type: "Logit-Probit-Ordered-Probit"
status: 📋 TEMPLATE
source_papers: []
variants_count: 0
created: 2026-05-18
updated: 2026-05-18
---

# Logit-Probit-Ordered-Probit — Results 骨架

## 主骨架

参见 `write-results/SKILL.md` → 填空段落骨架 → `Logit-Probit-Ordered-Probit`。

## 证据节奏摘要

<!-- 由 distill-results-exemplar 首次蒸馏后填充 -->

## 累积变体

<!-- distill-results-exemplar Phase 4 验证通过的变体写入此处 -->
<!-- 格式：
### 变体 N: [来源论文] (YYYY-MM-DD)
**验证状态**: 通过 / 需修正
**槽位**: R?
**骨架**:
> "..."
**与原骨架差异**: ...
-->

## 句式素材

<!-- 由 distill-results-exemplar Phase 4 自动沉淀的 sentence-level 骨架。填入占位符后可嵌入段落。 -->

### R3 — 主假设检验

**句式 1: `r3_sentence_ame_justification_probit`**

> Due to the difficulty in directly interpreting regression coefficients and significance levels in probability models, and as hypotheses should not be tested solely by examining p-values, the average marginal effect is visualized in [Figure X].

**句式 2: `r3_sentence_probability_magnitude_probit`**

> A one-standard-deviation increase in [IV] from the mean value ([from] to [to]) [increased/decreased] the probability of [DV] from [base]% to [new]%.

**句式 3: `r3_sentence_coefficient_significance_probit`**

> Model [Y] reports that the coefficient for [IV] is [positive/negative] and significant (b = [value], p = [threshold]).

**句式 4: `r3_sentence_logit_odds_likelihood`**

> [Table X] shows that [IV] had an odds ratio of [value] (p [threshold]), which means [IV] firms were [less/more] likely to [DV] than [reference group].

**句式 5: `r3_sentence_nonsignificant_inline`**

> However, [Table X] shows that [IV] did not have a significant effect on the likelihood of [DV]. Thus, Hypothesis [x] was not supported.


### R4 — 交互效应 / 条件效应

**句式 1: `r4_sentence_interaction_coefficient`**

> Model [Y] adds the interaction term between [moderator] and [IV], yielding a [positive/negative] coefficient for [DV] (b = [value], p = [threshold]).

**句式 2: `r4_sentence_region_significance_partial`**

> Although this interaction term is not statistically significant at the conventional p = [threshold] threshold, [Figure X] indicates that the marginal effect of [IV] is significant for [moderator] levels below [value]. Thus, Hypothesis [x] is partially supported.

**句式 3: `r4_sentence_subgroup_comparison_significance`**

> The [outcome]s for the [condition A] ([value] [unit]) and [condition B] ([value] [unit]) categories were significantly [larger/smaller] than the [outcome] for the [reference] category ([value] [unit]), and the [outcome] for [condition B] was significantly [larger/smaller] than the [outcome] for [condition A] (p [threshold]).

**句式 4: `r4_sentence_mixed_support_inline`**

> The nonparametric tests indicated that the [outcome]s for [condition A] and [condition B] were not significantly different from their predicted values, but the [outcome]s for the [reference] category were significantly different. The t-tests showed that the mean [outcome]s for [condition A] and [condition B] were significantly different from the [reference] category's mean [outcome] and that the [outcome]s for [condition A] and [condition B] were not significantly different from one another. Thus, Hypotheses [x] and [y] were supported, and Hypothesis [z] was not.


### R7 — 稳健性 / 效度 / 敏感性

**句式 1: `r7_sentence_threat_endogeneity`**

> Unobservable [unit]-level factors could affect [IV] and [DV]. Some of these factors may introduce the possibility of reverse causality, omitted variable bias, or both, leading to potential endogeneity in our study.

**句式 2: `r7_sentence_iv_validity`**

> The [test name] results suggest that our instruments are exogenous ([statistic], p = [threshold]). Furthermore, the second-stage regression models produced results consistent with those of Models [Y] and [Z].

**句式 3: `r7_sentence_heckman_two_stage`**

> Using [author_year]'s criteria to select the appropriate estimation approach, we employed a Heckman correction model. We included predictor variables in the first-stage models that were significantly associated with [DV], but not with [outcome]. The first-stage models were highly significant in predicting [DV], but the selection correction instrument was not significant when entered into the second-stage models. Thus, endogeneity did not appear to be a significant problem in our study.

**句式 4: `r7_sentence_supplemental_regression_caveat`**

> It is important to note that these regressions do not directly test Hypotheses [x–y], which address the performance of [group A] and [group B] relative to each other and relative to [reference]. Instead, the regressions examined if [IV_1] and [IV_2] had direct relationships with the magnitude of [outcome].


