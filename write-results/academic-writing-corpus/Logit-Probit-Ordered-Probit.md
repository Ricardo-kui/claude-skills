---
result_type: "Logit-Probit-Ordered-Probit"
status: 📋 TEMPLATE
source_papers:
  - "pfarrer_pollock_rindova_2010_tale_of_two_assets_amj (Academy of Management Journal): RE logit odds-ratio reporting, matched-pair hypotheses across positive/negative surprise tables, event-study CAR subgroup comparisons"
  - "malik_wang_martin_gomez-mejia_2025_mixed_gambles_jm (Journal of Management): Heckman probit two-stage + marginal effects CI-based testing + 1-SD→percentage point economic significance + dual DV parallel reporting"
variants_count: 8
created: 2026-05-18
updated: 2026-07-07
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

### 变体 1: R1 四合一密集开场 — 描述统计+诊断+估计器+报告惯例 (1篇高价值)
**来源论文**: Pfarrer, Pollock & Rindova 2010 (Academy of Management Journal)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: R1
**骨架**:
> [Table X] presents descriptive statistics and a correlation matrix for the variables used in testing our hypotheses. The means and standard deviations reflect values for raw rather than transformed measures. All variance inflation factors were below [threshold], with an average of [value]. Thus, multicollinearity is not a concern. We estimated [random-effects logit] because [justification]. We report odds ratios to allow easier interpretation. An odds ratio greater than one indicates the likelihood increases with a one-unit increase in the independent variable; an odds ratio less than one indicates the likelihood decreases.
**与原骨架差异**: AMJ 风格的高密度 R1——将描述统计、诊断、估计器声明、报告惯例四合一压缩为一段。适用于篇幅受限的顶刊。

### 变体 2: R3 Logit 主效应四拍 — odds ratio + likelihood 翻译 (1篇高价值)
**来源论文**: Pfarrer, Pollock & Rindova 2010 (Academy of Management Journal)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: R3
**骨架**:
> Hypothesis [N] predicted that [IV] would be [positive/negative] associated with [DV]. [Table X] shows that [IV] had an odds ratio of [value] (p < [threshold]), which means [IV] firms were [less/more] likely to [DV] than [reference group]. Thus, Hypothesis [N] was supported.
**与原骨架差异**: Logit 专用 R3。四拍：(1) 方向→(2) odds ratio + p →(3) likelihood 翻译（"were less/more likely"）→(4) 支持判断。非显著版本缩减为三拍：方向→不显著→不支持，省略 likelihood 翻译。

### 变体 3: R4 事件研究 CAR 分组比较 — 非参数验证+t检验替代回归交互 (1篇高价值)
**来源论文**: Pfarrer, Pollock & Rindova 2010 (Academy of Management Journal)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: R4
**骨架**:
> Initial nonparametric tests ([test names]) indicated that [market/audience] viewed [positive outcome] favorably (p < [threshold]) and perceived [negative outcome] as bad news (p < [threshold]). This pattern is consistent with previous studies. [Table Y] presents the size of each subsample category, the mean [outcome] for [condition A], [condition B], and [reference], the pairwise differences between means, and the significance of these differences based on paired t-tests of unequal variances. The [outcome]s for [condition A] ([value]) and [condition B] ([value]) were significantly [larger/smaller] than the [outcome] for [reference] ([value]). Thus, Hypotheses [X] and [Y] were supported.
**与原骨架差异**: 当理论预测离散类别间的序位差异（high/medium/low）而非连续交互时，分组均值比较+paired t-test 是有效替代——不需要回归交互项。先做非参数验证（Patell Z + generalized sign）确认事件研究指标行为正常，再做子组 t 检验。

### 变体 4: R7 GEE 补充回归 + Heckman 两阶段内生性纠正 (1篇高价值)
**来源论文**: Pfarrer, Pollock & Rindova 2010 (Academy of Management Journal)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: R7
**骨架**:
> Because our [primary] tests did not allow us to control for other factors that can affect the [size/magnitude] of [outcome], we ran [alternative estimator] regressions that predicted the [magnitude] of [outcome] while controlling for [factors]. It is important to note that these regressions do not directly test Hypotheses [X–Y], which address [original theoretical comparison]. Instead, the regressions examined if [IV_1] and [IV_2] had direct relationships with [outcome_magnitude]. We found that [IV_1] (b = [value], p < [threshold]) and [IV_2] (b = [value], p < [threshold]) had [positive/negative], significant relationships with [outcome], and their inclusion significantly improved the fit of the model.
>
> We also investigated whether endogeneity due to unobserved variables might have influenced our results. Using [Author_Year]'s criteria to select the appropriate estimation approach, we employed a [Heckman/two-stage] correction model. We included predictor variables in the first-stage models that were significantly associated with [selection_DV], but not with [outcome_DV]. The first-stage models were highly significant in predicting [selection_DV], but the selection correction instrument was not significant when entered into the second-stage models. Thus, endogeneity did not appear to be a significant problem in our study.
**与原骨架差异**: Pfarrer 的 R7 展现了两段式稳健性结构：补充回归的诚实声明 + Heckman 两阶段标准报告。两个段落的共同特征是在呈现补充证据时都保留了诚实声明。

### 变体 5: R2 Heckman 第一阶段表格 + 逆米尔斯比率进入第二阶段 (1篇高价值)
**来源论文**: Malik, Wang, Martin & Gomez-Mejia 2025 (Journal of Management)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: R2
**骨架**:
> [Table X] presents the first-stage results, where the [instrument] variable exhibits a robust [positive/negative] coefficient (b = [value], p < [threshold]), confirming that [instrument] is highly relevant for predicting [selection event]. Therefore, the instrument is both conceptually valid and statistically significant for isolating the selection effect. Next, we included the predicted inverse Mills ratio in our regression models. Since our dependent variable is binary, we used [probit/logit] regressions. Following [citation], we employed a clustered correlation structure grouped by [cluster_level] and used robust standard errors.
**与原骨架差异**: Heckman 作为主识别策略时，R2 必须完成三件事：(1) 第一阶段表格（含 instrument 系数+显著性）；(2) 确认 instrument relevance；(3) 声明逆米尔斯比率已纳入第二阶段。与 OLS/FE 的 R2（"Table X Model 1→2→3"）结构完全不同。

### 变体 6: R3 Probit 边际效应 CI 检验 — "CI does not cross zero" 作为支持标准 (1篇高价值)
**来源论文**: Malik, Wang, Martin & Gomez-Mejia 2025 (Journal of Management)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: R3
**骨架**:
> Due to the difficulty in directly interpreting regression coefficients and significance levels in probability models ([citation]), and as hypotheses should not be tested solely by examining p-values ([citation]), the average marginal effect is visualized in [Figure X]. The confidence intervals (CIs) of the marginal effects do not cross zero, thus supporting Hypothesis [N]. A one-standard-deviation increase in [IV] from the mean value ([mean] to [mean+1SD] [units]) [increased/decreased] the probability of [DV] from [X]% to [Y]%.
**与原骨架差异**: Malik 的证据展演有三个独特点：(1) 先引用 Busenbark et al. (2022) 和 Wiersema & Bowen (2009) 建立"probit 系数不可直接解释"的权威背书；(2) 将检验从 p-value 移到 AME 图的 CI——"the CIs do not cross zero, thus supporting H1"；(3) 经济显著性嵌入同一句：1-SD → X%→Y% 概率变化。

### 变体 7: R5 Probit 经济显著性 — 1-SD → 概率百分点变化 (1篇高价值)
**来源论文**: Malik, Wang, Martin & Gomez-Mejia 2025 (Journal of Management)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: R5
**骨架**:
> A one-standard-deviation increase in [IV] from the mean value ([mean] to [mean+1SD] [units]) [increased/decreased] the probability of [DV] from [X]% to [Y]%.
**与原骨架差异**: 与 OLS 的 "1-SD → N unit change" 或计数的 "e^β−1 = N%" 不同——probit/logit 的经济显著性应翻译为**概率百分点变化**（从 X% 到 Y%），同时给出均值和均值+1SD 的绝对值以锚定读者。一句完成，不需要独立段落。

### 变体 8: R3 双 DV 平行对称报告 (1篇高价值)
**来源论文**: Malik, Wang, Martin & Gomez-Mejia 2025 (Journal of Management)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: R3
**骨架**:
> As Model [N] ([Table Y]) reports, the coefficient for [IV_1] was [positive/negative] and significant (b = [value], p < [threshold]). [Figure X] plots the marginal effect, supporting Hypothesis [Na]. A one-SD increase... [changed probability from A% to B%]. Furthermore, the coefficient for [IV_2] was [opposite_sign] and significant (b = [value], p < [threshold]). [Figure Y] visualizes the marginal effect, supporting Hypothesis [Nb]. A one-SD increase... [changed probability from C% to D%].
**与原骨架差异**: 当两个 IV 对同一 DV 有对称反向预测时，在同一段内平行报告——读者无需在表格间跳转。关键：对称的句法（"the coefficient for X was positive... the coefficient for Y was negative"），对称的经济显著性翻译，对称的图示引用。
