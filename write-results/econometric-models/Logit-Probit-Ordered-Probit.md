---
result_type: "Logit-Probit-Ordered-Probit"
status: 📋 TEMPLATE
source_papers:
  - "pfarrer_pollock_rindova_2010_tale_of_two_assets_amj (Academy of Management Journal): RE logit odds-ratio reporting, matched-pair hypotheses across positive/negative surprise tables, event-study CAR subgroup comparisons"
  - "malik_wang_martin_gomez-mejia_2025_mixed_gambles_jm (Journal of Management): Heckman probit two-stage + marginal effects CI-based testing + 1-SD→percentage point economic significance + dual DV parallel reporting"
  - "bendig_hensellek_schulte_2024_etp (Entrepreneurship Theory and Practice): binary-GEE inverted-U formal test + conditional probability curves + probability-to-cost benchmark + threat-indexed robustness"
  - "lee_park_2024_giving_up_learning_smj (Strategic Management Journal): fractional-logit inverted-U evidence chain + turning-point-shift moderation + selective-path mechanism corroboration"
variants_count: 13
created: 2026-05-18
updated: 2026-08-04
---

# Logit-Probit-Ordered-Probit — Results 骨架

## 主骨架

参见 `write-results/SKILL.md` → 槽位骨架加载 → 本类型适用的 `references/slot-R*.md`（各 slot 文件内含 `Logit-Probit-Ordered-Probit` 专用变体）。

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

### 变体 9: R3 Binary-GEE 曲线完整检验链 — 二次项→端点斜率→Fieller 区间 (1篇高价值)
**来源论文**: Bendig, Hensellek & Schulte (2024, Entrepreneurship Theory and Practice)
**验证状态**: VERIFIED（Bendig 2024 与经用户专家审计的 Lee & Park 2024 构成跨估计器验证）
**写入日期**: 2026-08-04
**槽位**: R3
**骨架**:
> Hypothesis [x] predicted a [U/inverted-U] relationship between [X] and the probability of [binary Y]. The squared term has the predicted sign and is statistically significant in Model [m] (b = [value], p [threshold]), providing the first indication of the hypothesized shape. A formal U-test further shows that the slope at the lower bound of X is significantly [positive/negative], whereas the slope at the upper bound is significantly [opposite]. The estimated turning point is [value], and its [Fieller/bootstrap] confidence interval falls within the observed support of X. Taken together, these joint restrictions support Hypothesis [x]. Figure [f] then plots predicted probabilities across X; coefficients from the logit-link model are not interpreted as probability changes directly.

**与原骨架差异**: 变体2只处理线性 logit 主效应；OLS-FE 的曲线变体要求同类三步，但不能直接搬用线性系数解释。本变体为二元 GEE/logit 明确区分：(1) 链接函数上的系数形状证据；(2) 正式端点斜率与拐点区间；(3) 预测概率展示。

**诚实边界**: 二次项显著不是充分证据；拐点须在有观测支持的范围内。形状检验不能确认理论机制，极端区间稀疏时应展示观测密度或置信带。

### 变体 10: R4/R5 条件曲线几何翻译 + 概率—成本—价值 benchmark (1篇高价值)
**来源论文**: Bendig, Hensellek & Schulte (2024, Entrepreneurship Theory and Practice)
**验证状态**: 通过（单篇高价值，待第二篇概率曲线研究交叉验证）
**写入日期**: 2026-08-04
**槽位**: R4 / R5
**骨架**:
> The interaction between [W] and the squared term of [X] is [direction] and significant (b = [value], p [threshold]). Figure [f] shows what this means geometrically: at high W the curve [shifts upward/downward / becomes steeper/flatter], with its vertex at [X, predicted probability], whereas at low W the curve [contrasting shape]. Thus W changes [risk level / learning rate / turning-point location], supporting Hypothesis [x].
>
> To assess substantive magnitude, moving from [baseline X] to [curve location] changes the predicted probability of Y by [Δ percentage points]. Using an externally sourced average event cost of [C] as a transparent benchmark, this probability difference corresponds to an expected-cost magnitude of [Δp × C]. Relative to the average value of one [activity/deal], the implied risk cost is approximately [share]. This calculation illustrates scale; it is not a firm-specific realized-loss estimate.

**与原骨架差异**: 不把曲线调节压缩为“二次交互显著”。先用几何词汇说明究竟是上移、变陡或拐点移动，再把预测概率接到成本与活动价值 benchmark，形成从统计形状到管理后果的完整接力。

**诚实边界**: 外部平均成本包含情境与测量误差，必须披露来源和假设；不得把期望成本写成已观察因果损失。若 ±1 SD 超出 X/W 支持范围，应使用实际分位数或范围内百分比。

### 变体 11: R7 曲线关系的六威胁稳健性梯 (1篇高价值)
**来源论文**: Bendig, Hensellek & Schulte (2024, Entrepreneurship Theory and Practice)
**验证状态**: 通过（单篇高价值，待交叉验证）
**写入日期**: 2026-08-04
**槽位**: R7
**骨架**:
> We organize robustness checks by the inferential threat they address. To assess [lag choice], we use [alternative lags/windows]. To preserve information lost by the binary outcome, we estimate [count DV/alternative distribution]. To evaluate estimator dependence, we use [alternative panel estimator]. To assess focal-variable measurement, we replace [count] with [value/alternative proxy]. To test setting dependence, we expand the sample to [additional regulator/industry]. Finally, to probe omitted-variable endogeneity, we estimate [IV/control-function] models and report instrument diagnostics. The curve direction remains stable across these checks, although [specific branch] weakens to [threshold], which we report as reduced evidence strength rather than full invariance.

**与原骨架差异**: 不是按 Table 5/6/7 罗列模型，而是把每项检查映射到时间、DV、估计器、IV 测量、样本边界和内生性六种威胁。特别保留显著性降档，避免选择性胜利。

**诚实边界**: 未报告的工具变量结果只能作为补充，不能承担决定性识别；significance 从 5% 降至 10% 应如实说明。

### 变体 12: R4 转折点位置型调节 — 条件顶点 + 直接差异检验 (1篇高价值)
**来源论文**: Lee & Park 2024 (Strategic Management Journal)
**验证状态**: VERIFIED（Lee & Park 2024 经用户专家审计为位置型曲线调节的典型范文；与变体 10 的一般曲线几何翻译互补）
**写入日期**: 2026-08-04
**槽位**: R4
**骨架**:
> Hypothesis [x] predicted that [W] would move the turning point of the [U/inverted-U] relationship to a [later/earlier] value of X. Model [m] includes both X×W and X²×W; these coefficients determine the conditional curves but do not by themselves adjudicate the hypothesis. The estimated turning point is [x₀, CI] under [condition 0] and [x₁, CI] under [condition 1]. Their difference is [Δx, test statistic/CI, p value], in the predicted direction, and both estimates lie within data-supported regions. Figure [f] plots the conditional predictions on the [response/link] scale with that scale named explicitly. Taken together, this evidence [supports/partially supports/does not support] Hypothesis [x].
**与原骨架差异**: 变体 10 允许一般的曲线平移、变陡或顶点移动；本变体只处理理论明确预测的 `turning-point location moderation`，并强制报告两个顶点、差值与直接检验。它把统计交互降为原料，把几何比较提升为结果段主句。
**诚实边界**: 不得从两个交互项的单独 p 值推断顶点差异；不得只写“更晚（p=...）”而省略两端顶点估计。若完整模型的证据弱于单独模型，应明确写“attenuated/mixed evidence”，不能概括为“all supported”。

### 变体 13: R8 曲线机制的选择性路径辨析 — 激活一条机制而不激活另一条 (1篇高价值)
**来源论文**: Lee & Park 2024 (Strategic Management Journal)
**验证状态**: EMERGING（单篇机制辨析写法）
**写入日期**: 2026-08-04
**槽位**: R8
**骨架**:
> Our theory attributes the rising portion of the curve to [mechanism A] and the declining portion to [mechanism B]. As a mechanism-discriminating analysis, we examine [comparison exposure], which should activate A without imposing the same burden on B. Consistent with this distinction, the linear association with [Y] is [positive/negative] ([estimate/test]), whereas the squared term is not statistically distinguishable from zero ([estimate/test]). This contrast is consistent with the proposed division of mechanisms, but it does not constitute a mediation test because A and B are not directly measured or experimentally isolated.
**与原骨架差异**: 不用泛化的 additional analysis 堆叠更多相关性，而是选择一个能“保留机会、移除动机损耗”的对照暴露，使补充证据对应曲线两段的机制分工。
**诚实边界**: 该写法只允许 `consistent with`、`corroborates` 或 `helps distinguish`；访谈、替代暴露和 null quadratic 均不能升级为因果中介证据。

## 曲线结果写作反模式

- **正式 U 棔验后置**：在主结果只凭二次项宣称支持、再把端点斜率与转折点区间埋进 robustness，会让核心结论先于核心证据。正式形状检验应紧邻假设判断。
- **交互项替代几何比较**：若假设预测顶点位置，必须比较顶点；若预测陡峭度或垂直位移，则应改用相应几何与预测量。
- **尺度未标注**：logit-link 上的预测值不能被写成原始概率或结果单位变化；图与正文必须说明 response scale 或 link scale。
- **无效 p 值格式**：不得写 `p = .00` 或 `p < .00`，应写 `p < .001` 或报告可用的准确值。
- **选择性支持总结**：单独模型显著、完整模型仅边际显著时，应报告证据衰减，而不是用一句“全部支持”抹平差异。
