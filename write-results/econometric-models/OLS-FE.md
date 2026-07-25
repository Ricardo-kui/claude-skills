---
result_type: "OLS-FE"
status: 📋 TEMPLATE
source_papers:
  - "darby2026_faster_recalls_large_institutional_ownership_jom"
  - "eilert2017_recall_timing_automobile_jm"
  - "darby2023_ceo_stock_ownership_recall_timing_msom"
  - "zhao_ding_gaba_2023_positioning_digital_markets_orsc"
  - "mannor_wowak_bartkus_gomez-mejia_2016_heavy_lies_crown_smj (Strategic Management Journal): null main + significant interaction, one-side conditional slopes, ΔR² economic significance"
  - "bamberger_homburg_wielgos_2021_wage_inequality_jm (Journal of Marketing): marginal significance 90% CI dual-interval reporting"
  - "li_chiu_kong_cropanzano_ho_2026_jom (Journal of Management): interaction percentage economic significance, low-base-rate moderator histogram, five-threat labeled robustness with RIR+Oster+CEM"
  - "ahmadi_khanagha_berchicci_jansen_2017_jms (Journal of Management Studies): 7-model hierarchical regression table navigation, three-way interaction conditional decomposition, asymmetric findings narrative"
  - "cui_yang_vertinsky_smj_attacking_partners (Strategic Management Journal): inverted U-shape + curve moderation, Lind-Mehlum three-step test, turning-point CI, flatten/steepen graph language"
  - "chung_low_rust_2022_jams (Journal of the Academy of Marketing Science): model-free quartile opening, interquartile economic significance, Heckman two-stage table navigation, alternative-DV falsification, threat-by-threat endogeneity table"
  - "kim_lee_2026_putting_a_price_on_mission_smj (Strategic Management Journal): multi-stage same-IV pipeline attenuation profile, WTP coefficient-ratio economic significance, post-treatment selection caveat"
  - "pupovac_astvansh_carrillat_legoux_2026_pom (Production and Operations Management): cross-sectional OLS/FE on event-study CAR; Control Function + Heckman two-stage correction navigation"
  - "du_tsolmon_2024_post_ma_retention_structural_knowledge_orsc (Organization Science): selection three-step defense (descriptive→CEM→Heckman), null-finding-as-mechanism-evidence, heterogeneity-as-alternative-rebuttal, external-benchmark threshold discovery, downstream performance post hoc, 2x2 cross-diagonal typology comparison"
variants_count: 34
created: 2026-05-18
updated: 2026-07-25
---

# OLS-FE — Results 骨架

## 主骨架

参见 `write-results/SKILL.md` → 槽位骨架加载 → 本类型适用的 `references/slot-R*.md`（各 slot 文件内含 `OLS-FE` 专用变体）。

## 累积变体

### 变体 1: 按 Threat 分类的稳健性检验汇总矩阵 (Table 9 模板)
**来源论文**: Darby2026 JOM
**验证状态**: 通过 (1/5，但生成力极高)
**写入日期**: 2026-05-20
**槽位**: R7
**骨架**:
> We conducted [N] robustness checks to validate our findings and address potential concerns surrounding [threat_1], [threat_2], [threat_3], [threat_4], and [threat_5]. The robustness checks are detailed in the [Appendix_location], and [Table_reference] provides a summary of each approach, appendix and table numbers, and results. Taken together, these analyses illustrate the robustness of our results and provide additional support for all [N] hypotheses.
**与原骨架差异**: 当稳健性检验数量 ≥10 时，使用 Table 9 汇总矩阵按 threat 分类组织，每行包含：(1) 威胁类别；(2) 方法概述；(3) 附录位置；(4) 逐假设结果。这比逐段叙事更可审计。少量稳健性检验 (<5) 时使用叙事型更合适。

### 变体 2: 叙事型稳健性检验 — 逐 Threat 组织 (4/5 复现)
**来源论文**: Eilert2017 JM / Darby2025 JSCM / Darby2023 MSOM / Wowak2025 MS
**验证状态**: 通过
**写入日期**: 2026-05-20
**槽位**: R7
**骨架**:
> **[Threat 1 — Omitted Variables]**: One concern is that [threat_description]. To address this, we [method]. The results [are substantively unchanged / continue to support Hypothesis N].
>
> **[Threat 2 — Reverse Causality]**: [...]
>
> **[Threat 3 — Measurement Error]**: Given [data_concern], we used [alternative measure / PSM]. [Key result with economic significance].
>
> **[Threat 4 — Alternative Empirical Strategy]**: To ensure results are not dependent on [specific estimator], we replicated using [alternative_estimator_1] and [alternative_estimator_2]. The results are consistent with our primary findings.
**与原骨架差异**: 标准叙事型稳健性检验模板，按威胁（而非按表格）组织。每个威胁一个段落。与变体1 (Table 9 矩阵) 互补——5-10 个检验时用叙事型，10+ 时用矩阵型。

### 变体 3: 经济显著性的 Quartile Penalty Table (1/5 复现)
**来源论文**: Darby2023 MSOM
**验证状态**: 可选变体 (高价值)
**写入日期**: 2026-05-20
**槽位**: R5
**骨架**:
> We interpret the practical implications using the smallest ([window_1]) and largest ([window_2]) significant effect sizes to provide a range of the potential [penalty/benefit]. A one-standard-deviation increase in [DV] is associated with a [outcome] ranging from [min]% to [max]%. To further understand the practical implications, we examined how these [penalties] change across quartiles of the [DV] measure. The range of [penalties] is presented in [Table], which illustrates meaningful increases across quartiles. For example, moving from the first quartile ([N] [units]) to the second quartile ([N] [units])—[practical_interpretation]—is associated with an increase in the [outcome] ranging from [min]% to [max]%.
**与原骨架差异**: 将经济显著性从 "1 SD → X%" 升级为完整的 quartile-by-quartile 解释。Darby2023 的 Table 5 是标杆——从 Q1 (10 days) 到 Q4 (365 days) 的 penalty 递增清晰展示了非线性惩罚结构。

### 变体 4: 小样本/非显著结果的诚实声明 (1/5 复现)
**来源论文**: Darby2023 MSOM
**验证状态**: 可选变体 (所有研究都该用)
**写入日期**: 2026-05-20
**槽位**: R6
**骨架**:
> Although our theorizing supports [theoretical_explanation], we note that the [null/mixed] effect for [subset] could also simply be an artifact of the small sample size for [subset] ([N] observations).
**与原骨架差异**: 这是**非显著结果诚实报告**的标杆句式。不将 null finding 过度理论化（"CEOs care less"），而是在理论解释后立即补充统计功效的替代解释（"could also simply be an artifact of the small sample size"）。适用于任何小样本分组出现非显著结果的情况。

### 变体 5: Post Hoc — MCMC 显式中介分析 (1/5 复现)
**来源论文**: Darby2023 MSOM
**验证状态**: 可选变体
**写入日期**: 2026-05-20
**槽位**: R8
**骨架**:
> Our post hoc analysis addresses implied relationships—[IV] may influence [DV_2] through [DV_1]. To examine this, we used an explicit mediation approach that explores evidence of indirect effects ([citation]). The explicit mediation method simulates multiple draws of indirect effects that are the product of [coefficient_path_a] and [coefficient_path_b]. Evidence of mediation is identified by examining the 95% confidence interval for the mediation pathway. If the interval does not contain zero, mediation is supported. To conduct this analysis, we used a Markov Chain Monte Carlo (MCMC) simulation method with [N] draws ([citations]). The results indicate that [DV_1] partially mediates the relationship between [IV] and [DV_2] for [conditions]. Overall, as [IV] increases, [DV_1] increases, and this [change_in_DV_1] leads to greater [DV_2].
**与原骨架差异**: MCMC 显式中介（如 Imai et al. 或 Beer & Qi 2024 方法）替代了传统的 Baron & Kenny 三步法或 bootstrapping。关键要素：(1) 方法引用；(2) 模拟次数 (20,000 draws)；(3) 95% CI 不含 0 → mediation 成立；(4) "partially mediates" 而非 "fully mediates"（学术诚实）。

### 变体 6: 符号反转跨条件的诚实报告 — Sign Reversal Across Conditions with Theoretical Explanation (1/6 复现)
**来源论文**: Zhao/Ding/Gaba 2023 (Organization Science)
**验证状态**: 通过（单篇入库；corpus 此前仅有 null-finding 变体4，方向反转报告为真实空白，待第二篇交叉验证）
**写入日期**: 2026-06-17
**槽位**: R6
**骨架**:
> In the main analyses, [IV] is [pos/neg] and significant. ... These patterns do not hold for [condition/subsample]. Instead, in Model [X], [IV] has a [opposite-direction] and significant effect. The magnitudes are notably smaller, roughly [one-half to one-third] of those for [baseline condition]. In Model [Y], the interaction effect between [condition indicator] and [IV] is [opposite] and significant, suggesting that the [baseline] effect of [IV] is significantly attenuated in [condition].
>
> The sign reversal ... may also suggest a shift in how [actors] translate the same [signal] into actions, once they have accumulated [internal knowledge]. For [baseline condition], [actors] primarily seek [acquisition / first-order goal]. ... In [condition], [actors] can draw on [internal knowledge], and their objectives may shift toward [retention and monetization / second-order goal]. In that context, a high [IV] signal may be interpreted as [alternative meaning], [direction of revised behavior]. ... For [condition], [actors] no longer systematically [differentiate from / imitate] [reference] in response to [IV]. Taken together, [IV] strongly guides [baseline], but its influence diminishes as [actors] accumulate firsthand experience.
**与原骨架差异**: corpus 此前只有变体4（小样本 null finding 的诚实声明），未覆盖**同一 IV 在不同条件/阶段方向相反**的 nuanced finding。本变体的核心是"方向反转 + 幅度衰减 + 交互确认 + 反转的理论解释"四件套：(1) 先报主分析方向，再报反转方向；(2) 量化幅度衰减（one-half to one-third）；(3) 用交互项确认衰减显著；(4) **给反转一个理论解释**（不是 statistical artifact，而是 actors 的目标/信息基础随条件改变：acquisition vs retention）。关键：把反转定位为 **boundary condition**（"influence diminishes as..."），而非失败——既诚实又有理论增量。适用于任何"同 IV 跨样本/阶段/条件符号变化"的报告（如 initial vs subsequent、pre vs post、新进入者 vs 在位者、treated vs control 子群）。

### 变体 7: 替代 DV 作机制验证 — Alternative DV as Theoretical Validation (1/6 复现)
**来源论文**: Zhao/Ding/Gaba 2023 (Organization Science)
**验证状态**: 可选变体（中价值，扩展 R7 的理论功能）
**写入日期**: 2026-06-17
**槽位**: R7 / R8
**骨架**:
> [Our theory / Another relevant aspect] also involves [theoretical dimension not captured by main DV]. To examine this, we introduce an alternative dependent variable, [alt-DV], which captures [theoretical dimension] — [operational definition]. Because [each construct has a vector over the keyword dictionary], we first compute [pairwise distance metric, e.g., Jensen-Shannon] for all [constructs]; we then [rescale / aggregate] and calculate the [weighted distance] between [component A] and [component B]. [IV_1] has a [pos/neg] and significant effect on [alt-DV] (p < [thr]), whereas [IV_2] is insignificant. This suggests that, when [IV_1 condition], [actors] tend to [behavior]—consistent with a [theoretical-label] positioning. This provides additional evidence that [IV_1] is associated with [mechanism] not only through [primary channel] but also through [secondary channel].
**与原骨架差异**: 现有 R7 变体（变体1 Table 9、变体2 narrative）都把稳健性定位为**威胁缓解**（rule out confound / alternative estimator）。本变体扩展 R7 的理论功能：用替代 DV **corroborate 机制**而非缓解威胁——引入一个捕捉主 DV 未覆盖维度的替代结果变量（如"peripheral 与 core 的语义距离"），若与主 DV 同向则支持机制。关键区分：明确标 "to further understand / provides additional evidence that... not only through [primary] but also through [secondary]"，把它定位为机制验证而非稳健性。当理论含多个可分离的预测通道时尤其有用。

### 变体 8: 主效应不显著但调节显著 — 条件化再定位 (1篇高价值)
**来源论文**: Mannor, Wowak, Bartkus & Gomez-Mejia 2016 (Strategic Management Journal)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: R3+R4
**骨架**:
> Hypothesis [N] predicted a [positive/negative] relationship between [IV] and [DV]. In Model [X], the coefficient for [IV] was in the predicted direction but not statistically significant (β = [value], n.s.). Hypothesis [N] was thus not supported as a main effect. However, the interaction between [IV] and [moderator] in Model [Y] was [positive/negative] and significant (β = [value], p < [threshold]), lending support to Hypothesis [N+1]. Marginal effects at [±1 SD] of [moderator] revealed a significant effect of [IV] on [DV] under [low/high moderator] conditions (dy/dx = [value], p < [threshold]) but not under [opposite] conditions (dy/dx = [value], n.s.). This pattern suggests that [IV] does influence [DV], but primarily under [boundary condition].
**与原骨架差异**: 当主效应假设被拒绝、但交互效应支撑条件关系时，本骨架将"失败"重新框定为理论条件化——方向正确但不显著→交互显著→条件分解→"does influence, but primarily under"。关键技巧：(1) 先诚实承认 H1 不被支持；(2) 迅速过渡到"However..."；(3) 报告边际效应的条件显著性；(4) 最后一句"does influence... but primarily under" 将叙事从失败转向边界发现。诚实边界：事后将不显著主效应重新框定为边界条件需要理论支持——如果交互没有事前假设，不能这样做。

### 变体 9: 调节效应边际效应的单侧显著报告 (1篇高价值)
**来源论文**: Mannor, Wowak, Bartkus & Gomez-Mejia 2016 (Strategic Management Journal)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: R4
**骨架**:
> To further explore the nature of this interaction, we examined the conditional marginal effects of [IV] on [DV] at [low] and [high] levels of [moderator] (typically [±1 SD] from the mean). When [moderator] was [low/high], [IV] had a [positive/negative] and significant effect on [DV] (dy/dx = [value], p < [threshold]). In contrast, when [moderator] was [opposite level], the effect was not statistically different from zero (dy/dx = [value], n.s.). [Figure X] illustrates this pattern.
**与原骨架差异**: 标准交互报告通常报告两端的简单斜率，但当一侧显著、一侧不显著时，需要明确区分而非对称报告。本骨架使用"dy/dx"而非"simple slope"措辞（在 Stata 的 margins 框架下更自然），且明确将不显著侧标注为"not statistically different from zero"而非暗示有方向。

### 变体 10: ΔR² + 条件边际效应嵌入经济显著性 (1篇高价值)
**来源论文**: Mannor, Wowak, Bartkus & Gomez-Mejia 2016 (Strategic Management Journal)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: R5
**骨架**:
> We assessed the economic significance of [IV]'s effect by examining the incremental variance explained (ΔR²) when [IV] and its interaction with [moderator] were added to the baseline model. The addition of [IV] and [moderator × IV] increased R² by [Δvalue] ([F_stat], p < [threshold]), indicating that the conditional relationship accounts for meaningful variation in [DV] beyond the control variables. Under [condition_A] ([moderator] at [level_A]), a [1-SD/unit] increase in [IV] is associated with a [N]% change in [DV] relative to its mean, representing a substantively important shift. Under [condition_B] ([moderator] at [level_B]), the marginal effect is negligible ([value], n.s.).
**与原骨架差异**: 将 ΔR² 和条件边际效应百分比联合使用来论证经济显著性：(1) ΔR² 论证"模型改进显著"；(2) 条件分解论证"在特定条件下效应有实质意义"；(3) 不显著侧的 negligible 声明呼应变体9的单侧显著性。

### 变体 11: 边际显著 90% CI 双区间透明报告 (1篇高价值)
**来源论文**: Bamberger, Homburg & Wielgos 2021 (Journal of Marketing)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: R3/R8
**骨架**:
> The total effect of [IV] on [DV] is [directional] but reaches only marginal statistical significance (Est. = [value], p < .10, 95% CI: [[lower], [upper]] crosses 0, 90% CI: [[lower], [upper]] does not cross 0). This suggests that [theoretical claim] receives weak but directionally consistent support.
**与原骨架差异**: 与"p < .10"的简单声明相比——(1) 同时报告 95% 和 90% 两个 CI；(2) 明确指出哪个 CI crosses 0、哪个不跨；(3) "weak but directionally consistent support" 是标准措辞。诚实边界：p < .10 只能在有理论预测方向且与理论一致时使用；不能用于探索性分析。

### 变体 12: R7 补充分析作为跨样本稳健性复制 (1篇高价值)
**来源论文**: Mannor, Wowak, Bartkus & Gomez-Mejia 2016 (Strategic Management Journal)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: R7
**骨架**:
> We conducted a supplementary analysis using an alternative sample to examine whether our findings generalize beyond [primary_sample]. Specifically, we replicated our core models using [alternative_sample: e.g., a sample of public firms from the same industry / external survey data / a different time period]. The results ([Appendix Table]) indicate that [key findings: e.g., the main effect of IV on DV remains significant (β = [value], p < [threshold]); the interaction between IV and moderator remains significant (β = [value], p < [threshold])]. These supplementary findings increase confidence that our results are not idiosyncratic to [primary_sample] and generalize to [broader context].
**与原骨架差异**: 跨样本复制比替代测量复制更高级——不是同一数据的另一种测量方式，而是完全不同的数据源/样本。关键：(1) 明确标注为"supplementary"而非核心发现；(2) 声明目的（generalizability > robustness）；(3) 与主分析并行的 replica 结构（逐假设报告方向+显著性）。适用于主要分析受限于特定样本（如访谈/实验样本）的研究。

### 变体 13: R5 交互效应百分比经济显著性 — 联合变化的幅度解释 (1篇高价值)
**来源论文**: Li, Chiu, Kong, Cropanzano & Ho 2026 (Journal of Management)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: R5
**骨架**:
> A [N]% increase in [IV] and [moderator] was associated with a [N]% increase in [DV] around the [event]. / A [N]% increase in [IV] and [moderator] was associated with a decrease of [N] [units] in [DV].
**与原骨架差异**: 现有变体3（Darby Quartile Penalty Table）、变体10（Mannor ΔR²+条件边际效应）的经济显著性均针对主效应或调节效应的条件分解。本骨架针对的是**交互效应本身的联合经济含义**——当 IV 和 moderator 同时变化时的幅度翻译。Li et al. 的独特策略：(1) 将交互效应的经济显著性从"simple slope at ±1SD"翻译为"1% joint increase → Y% change"；(2) 对于不同的 DV 使用不同的翻译单位——百分比（ATV: "% increase"）和绝对单位（sentiment: "decrease of N units"）；(3) 嵌入在 R3 假设检验段落后立即给出，而非独立段落。适用于连续×连续的交互效应（特别是 LIWC 文本变量，其自然单位就是百分比）。
**诚实边界**: 联合变化的解释（"1% increase in X and M → Y% change in DV"）假设 IV 和 moderator 同时同方向变化，这在现实中可能不成立——应补充说明"when both increase by 1%"而非暗示它们总是共变。

### 变体 14: R4 低基础率调节变量的边际效应直方图 — 替代传统 ±1SD 线图 (1篇高价值)
**来源论文**: Li, Chiu, Kong, Cropanzano & Ho 2026 (Journal of Management)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: R4
**骨架**:
> We further plotted the marginal effects using histograms. Given that [moderator] has a low base rate ([N]%), for easier interpretation, we display different levels of [moderator] based on the actual counts of [moderator_unit] ([count_1], [count_2], [count_3], and [count_4] [units]). Figure [N] shows that [IV] was more [positive/negative] related to [DV] when [moderator] was higher. / For [DV_2], we graphed the interaction based on cases without [moderator_unit] and those containing such [units], since most observations with [moderator] in this sample used one [moderator_unit]. Figure [N] illustrates that [IV] [effect_description] under higher [moderator].
**与原骨架差异**: 传统交互效应图使用 ±1SD 线图，但低基础率变量（如 CEO 死亡词使用率 3.61%）的 ±1SD 可能落入负值区域或无实际对应的观测值。Li et al. 的解决方案：(1) 使用**边际效应直方图**替代传统线图——X轴为 moderator 的实际离散值（0, 1, 3, 5 词），Y轴为 IV 的边际效应；(2) 在极端低基础率时（如仅 0 vs ≥1），退化为二分类比较图——"cases without death words vs cases with death words"；(3) 图中附置信区间条。关键策略：不假装低基础率变量是连续的，而是**按实际取值离散化展示**。适用于任何稀有文本特征、罕见事件计数、或高度偏态的调节变量。
**诚实边界**: 边际效应直方图（或离散比较图）必须标注每个 bin 的观测数量——低基础率变量的某些 bin 可能仅包含极少数观测，此时边际效应估计不稳定。若某 bin N < 30，应在图中或注释中标记。

### 变体 15: R7 五威胁标签化稳健性序列 — RIR+Oster+CEM组合 (1篇高价值)
**来源论文**: Li, Chiu, Kong, Cropanzano & Ho 2026 (Journal of Management)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: R7
**骨架**:
> We conducted a series of supplementary analyses to determine the robustness of our findings. First, to rule out the possibility of [threat_1: omitted variable bias], we performed the [test_1: RIR test] and [test_2: Oster's delta test]. The results from these tests indicate that our empirical findings are robust against [threat_1] ([appendix_location]). Second, we checked whether [alternative_explanation: e.g., death communication type] interacted with [IV] and [moderator]; however, we found no meaningful moderating effect on [DV] (see [appendix_location]; also refer to our [prior_studies] for the [related_type] results related to this analysis). Third, it is likely that [specific_subsample: e.g., pharmaceutical firms] may [bias_direction: use more death-related language]; we tested our models by excluding [subsample] and found consistent results ([appendix_location]). Fourth, since recent studies have measured [construct] using [alternative_measure] ([citation_1]; [citation_2]), we substituted [original_measure] with [alternative_measure]. The results show no direct effect or interaction with [IV] across the models. Additionally, the findings remain consistent when [alternative_measure] is included as a control. Finally, given the low base rate ([N]%) of [condition], we employed coarsened exact matching (CEM) to create a matched sample to reduce potential bias in the analysis. For the matching criteria, we included [matching_variables: e.g., quarter, analyst recommendation, firm size, call length, CEO gender] ([citation_1]; [citation_2]; [citation_3]). The percentage of [condition] increased to [N]% in the matched sample, aligning closely with the main test results based on the full sample ([appendix_location]). A summary of our results is available online in [appendix_summary].
**与原骨架差异**: 现有变体2（叙事型逐威胁组织）提供了标准四威胁模板（omitted variables + reverse causality + measurement error + alternative estimator）。Li et al. 升级为**五威胁+两稀有检验组合**：(1) RIR + Oster's delta 联合处理遗漏变量——这是 recent 顶刊（特别是金融/会计领域）的 gold standard，替代传统的"add more controls"；(2) 死亡类型分析——将 moderator 分解为 literal vs pseudo 子类型并检验是否调节主交互，创建"null interaction on interaction"的 meta-robustness；(3) 制药企业排除——针对特定行业的混淆检验（pharma firms 可能更频繁使用死亡相关语言）；(4) 替代测量替换——独立董事死亡替代 CEO 死亡词（construct-level replication）；(5) CEM 匹配处理低基础率选择偏误——匹配后的 moderator 比率从 3.61% 升至 11.33%。最后以 "A summary of our results is available online in Appendix [N]" 收尾。
**诚实边界**: RIR + Oster 组合需要在 Methods 或 Appendix 中解释两个检验的选择参数（如 RIR 的 replacement threshold、Oster 的 δ 和 Rmax）。仅说 "results are robust to omitted variable bias" 而不报告参数 → 审稿人会要求补充。

### 变体 16: R2 7模型层次回归表导航 — 主效应→双向→三向递进 (1篇高价值)
**来源论文**: Ahmadi, Khanagha, Berchicci & Jansen 2017 (Journal of Management Studies)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: R2
**骨架**:
> [Table N] presents the descriptive statistics and correlations and [Table N+1] presents the results of the regression analyses. The power of the full model is above [N] per cent. Model 1 includes the main effects, the traits, and manipulations, to test hypotheses [H_labels]. We find that [control_finding_of_note: e.g., complexity has a direct and positive effect on DV, and this suggests that, when faced with complex decision-making tasks, managers tend to embrace exploratory activities]. Turning to our main independent variables, we find that [H_summary: e.g., the regulatory focus trait is associated with the DV]. [IV_1] is found to be [direction] associated with [DV] (B = [value], SE = [value], p < [threshold]), while [IV_2] is [direction] associated with it (B = [value], SE = [value], p < [threshold]). These findings are consistent with hypotheses [H_labels].
>
> To test hypothesis [H_interaction] relating to [moderator mechanism: e.g., regulatory fit], we followed [citation] and included the interaction of [moderator] and [IV_trait] in Models [N] to [N+n]. We find that the interaction between [condition_A] and [trait_A] is [significant/not statistically significant]. Thus, our hypothesis [H_label] is [supported/rejected]. However, the interaction between [condition_B] and [trait_B] is found to be [significant] (B = [value], SE = [value], p < [threshold]). The simple slope test confirms the difference between slopes (t = [value], p = [value]). To ease the interpretation, we plotted the interaction effect. Figure [N] shows that [condition_B] can intensify the [direction] effect of [trait_B] on [DV]. Model [N+final] includes both interaction terms.
>
> Model [N+final+1] shows the results of the three-way interaction between [moderator_1], [moderator_2], and [IV]. The coefficient is statistically significant (B = [value], SE = [value], p < [threshold]), which is consistent with hypothesis [H_3way]. Further, we tested the conditional effect of two-way interactions at the two values of [moderator_1]. The result confirmed that the two-way interaction is indeed significant (B = [value], p < [threshold]) under the high [moderator_1] condition, but non-significant (B = [value], p > [threshold]) under the low [moderator_1] condition. Moreover, we tested the difference between simple slopes. The difference is significant (t = [value], p < [threshold]) between the slope of the [condition_A]-high [moderator_1] condition and the slope of the [condition_B]-high [moderator_1] condition. However, a similar test on the difference between the slope of the [condition_A]-low [moderator_1] condition and the slope of the [condition_B]-low [moderator_1] condition proved to be non-significant (t = [value], p > [threshold]).
**与原骨架差异**: 本骨架是**实验层次回归的完整表导航模板**，适用于拥有多个特质IV、多个操纵调节变量、两向和三向交互的实验设计。Ahmadi et al. 使用7模型递进结构：(1) M1主效应（trait IV + manipulated variables）；(2) M2-M4两向交互（逐个添加交互项，Higgins et al. 2003范式）；(3) M5-M7三向交互（逐个添加三向项）。关键策略：(a) 将控制变量的显著发现也纳入叙事——"complexity has a direct and positive effect... this suggests that..."——即使不是假设的一部分，也为后续交互提供了情境锚定；(b) 逐个假设报告而非一次性报告所有模型——每段对应一个假设/一组假设，M1→H1a+b, M2-M4→H2a+b, M5-M7→H3a+b；(c) 三向交互的条件分解——在主效应中测试"在哪个调节水平上两向交互显著"，再用t-test比较跨条件的简单斜率差异。适用于任何含多个trait IV + 多个manipulated moderator的2×2实验设计。
**诚实边界**: 7模型表可能过于密集——必须在表注中明确每个模型包含哪些变量。若某些交互项的加入导致其他系数符号反转或显著性变化（如promotion focus从Model 1显著到Model 2不显著），必须在正文中讨论而非沉默。

### 变体 17: R3 主假设检验 — 倒 U 型关系（Lind-Mehlum 三步 + 转折点 CI + Cohen's d）(1篇高价值)
**来源论文**: Cui, Yang & Vertinsky (Strategic Management Journal)
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-08
**槽位**: R3
**骨架**:
> Hypothesis [x] predicted that [predictor] would have an inverted U-shaped relationship with [outcome]. In Model [y] of Table [z], we tested this hypothesis by introducing both the linear and quadratic terms of [predictor]. The result shows that [outcome] first increases significantly with [predictor] (b = [linear], p = [p-value]), then decreases significantly as [predictor] continues to increase (b = [quadratic], p = [p-value]). This result indicates a curvilinear relationship (inverted U-shape) between [predictor] and [outcome], with a [effect-size] effect size (Cohen's d = [value]).
>
> We examined the marginal effects of this relationship following the three steps suggested by Lind and Mehlum (2010). First, we examined whether the second-order term is significant and of the expected sign; this is confirmed by the result. Second, we tested whether the slope is indeed sufficiently steep at both ends of the data range of [predictor]. Using the "margins" command in [software], we confirmed that when [predictor] = [low_value], the slope dy/dx = [value] (p = [p-value]), and when [predictor] = [high_value], the slope dy/dx = [value] (p = [p-value]). Third, we tested whether the turning point is located within the data range of [predictor]. We confirmed this using the "nlcom" command in [software] by showing that the inverted U-shape turns when [predictor] = [turning_point] and that the 95% confidence interval for the turning point [[lower], [upper]] is within the value range of [predictor]. We provide additional support by plotting this relationship in Figure [X]. These findings suggest that Hypothesis [x] is supported.
**与原骨架差异**: OLS-FE.md 现有 16 个变体全部针对线性关系或线性交互，曲线关系报告完全空白。本骨架提供顶刊倒 U 型关系的标准协议：线性/二次系数 → 形状判断+效应量 → Lind-Mehlum 三步（二阶项符号、两端斜率、转折点在数据范围内）→ 转折点 95% CI → 图形 → 支持判断。**范式排他性**: 多项式 OLS/FE 专用；Logit/Probit 需替换为 predicted probability / odds ratio 解释。
**诚实边界**: 曲线关系的 Cohen's d 计算应说明基准（如基于二次项或简单斜率差异），不可直接套用线性交互的 d 公式；须在 Methods 或附录说明效应量计算方式。

### 变体 18: R4 曲线调节效应 — 倒 U 型被调节（二阶交互项符号 + Cohen's d + flatten/steepen 图形解释）(1篇高价值)
**来源论文**: Cui, Yang & Vertinsky (Strategic Management Journal)
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-08
**槽位**: R4
**骨架**:
> In Model [N], the interaction terms between [moderator] and both the linear and quadratic terms of [predictor] are introduced in order to test Hypothesis [N]: whether [moderator] [positively/negatively] moderates the inverted U-shaped relationship between [predictor] and [outcome]. This moderation effect is supported if the second-order interaction term is significantly [positive/negative] ([citation]). As confirmed by our results, the second-order interaction term is indeed [positive/negative] (b = [value], p = [p-value]), with a [small/medium/large] effect size (Cohen's d = [value]). Figure [N] illustrates this moderation effect, showing that the inverted U-shape is [flattened/steepened] when the value of [moderator] is higher, supporting Hypothesis [N].
>
> Model [N+1] is the full model, including all control, independent, and interaction variables; all results from Models [X] hold.
**与原骨架差异**: 现有 OLS-FE R4 变体（变体 9、10、13、14）均针对线性交互的边际效应或百分比解释，未覆盖二次项×调节变量的曲线调节。关键语言：**二阶交互项符号预期**（positive/negative）决定 flatten/steepen；**flattened/steepened** 描述整个曲线形状变化；**M6 全模型一句收尾**确认各独立模型结果在全模型中稳定。**范式排他性**: 二次项 × 连续调节变量专用；若调节变量为二分/类别需调整图示语言。
**诚实边界**: 曲线调节的 Cohen's d 计算应基于二阶交互项或简单斜率差异，不可直接套用线性交互的 d 公式；须在 Methods 或附录说明效应量计算方式。

### 变体 19: R2 模型序列 — 多项式主效应 + 多个曲线调节 (1篇高价值)
**来源论文**: Cui, Yang & Vertinsky (Strategic Management Journal)
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-08
**槽位**: R2
**骨架**:
> We ran [estimator] models following a hierarchical approach: Model 1 includes only the control variables, while Models 2 through [N-1] add the independent and interaction variables. Model [N] is the full model, including all independent and interaction variables. [Variance inflation factor (VIF) scores were calculated for all models; none of the maximum VIFs exceed [value], which is substantially lower than the rule-of-thumb cut-off of 10 ([citation]).] [We then used [procedure] in [software] to conduct [diagnostic test], which showed [result].] We also ran the [estimator] models using non-centered data; the results are consistent. Since centered estimations can make interpretation of the results less straightforward ([citation]), we report estimations using the original variable values in Table [z].
**与原骨架差异**: 与现有变体 16（Ahmadi et al. 7 模型 trait × manipulation × complexity 实验设计）不同，本结构是面板数据中的 M1 控制 → M2 多项式主效应 → M3-M5 分别加入不同曲线调节 → M6 全模型。关键：层次结构为理论服务，让读者既能看清每个假设的干净证据，又能验证结果在全模型中稳定。

### 变体 20: R1 描述性统计与诊断 — 多项式/交互模型 (1篇高价值)
**来源论文**: Cui, Yang & Vertinsky (Strategic Management Journal)
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-08
**槽位**: R1
**骨架**:
> Table [x] reports descriptive statistics and correlations for all variables, including the quadratic and interaction terms. We mean-centered the variables before creating quadratic and interaction terms in order to reduce non-essential ill-conditioning between independent variables and their higher-order terms ([citation]). The dependent and independent variables show considerable variance, and the correlation coefficients are consistent with our expectations.
>
> We ran [estimator] models following a hierarchical approach: Model 1 includes only the control variables, while Models 2 through [N-1] add the independent and interaction variables. Model [N] is the full model, including all independent and interaction variables. Variance inflation factor (VIF) scores were calculated for all models; none of the maximum VIFs exceed [value], which is substantially lower than the rule-of-thumb cut-off of 10 ([citation]). We then used [procedure] in [software] to conduct the [citation] multicollinearity diagnostic test, which showed that the condition number for our complete model is [value], well below the threshold of [threshold]. We also ran the [estimator] models using non-centered data; the results are consistent. Since centered estimations can make interpretation of the results less straightforward ([citation]), we report estimations using the original variable values in Table [z].
**与原骨架差异**: write-results SKILL.md 的 R1 通用段落未覆盖多项式/交互模型特有的 mean-centering、condition number 和非中心复制三重诊断。本文提供了完整且简洁的整合范例：诊断不是为了例行公事，而是为了说明"高阶项和交互项没有造成多重共线性问题"，并解释为何最终报告非中心化系数（便于解释）。

### 变体 21: R8 补充/事后分析 — 枚举清单 + 附录引用 (1篇高价值)
**来源论文**: Cui, Yang & Vertinsky (Strategic Management Journal)
**验证状态**: 可选变体（中价值）
**写入日期**: 2026-07-08
**槽位**: R8
**骨架**:
> We conducted [N] additional analyses, either as robustness checks or to gain additional insights into the primary relationships. These analyses investigated (a) [analysis_1]; (b) [analysis_2]; (c) [analysis_3]; (d) [analysis_4]; (e) [analysis_5]; and (f) [analysis_6]. Details of these analyses are available in [Appendix].
**与原骨架差异**: 现有 R8 变体 5 是 MCMC 中介的详细展开式。本文展示当稳健性/探索性分析条目较多时，正文可用枚举清单指向附录的简洁策略。关键：用 "either as robustness checks or to gain additional insights" 同时标注两类目标，但缺少逐条 threat 说明——若稳健性分析是核心识别策略的一部分，建议改用变体 1（Table 9 矩阵）或变体 2（叙事型逐 threat 组织）。
**诚实边界**: 将稳健性检验仅作为枚举清单可能削弱内部效度叙事；若可能，应在正文或附录中为每项分析标注其回应的具体威胁或探索性问题。

### 变体 22: R2 无模型证据开场 — 四分位均值/中位数单调性 (1篇高价值)
**来源论文**: Chung, Low & Rust 2022 (Journal of the Academy of Marketing Science)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-08
**槽位**: R2
**骨架**:
> We first present model-free evidence regarding the relationship between [IV] and [DV]. In the [web appendix / online supplement], we show the scatter plots of [DV] against [IV] for [subgroup description: e.g., the three industries with the most observations]. In Fig. [X], we divide our sample into [four quartiles / five quintiles] based on the level of [IV] and calculate the mean and median [DV] for observations in each [group]. Consistent with Hypothesis [N], there is a monotonic [increase / decrease] in [DV] from the first [group], where [IV] is lowest, to the [fourth / fifth] [group], where [IV] is highest. The mean (median) [DV] is significantly different across the [groups].
**与原骨架差异**: 在报告回归模型之前先用无模型证据建立模式的可信度，是 upper-echelons / 行为决策类论文的常用开场。关键四拍：(1) 声明"model-free evidence"；(2) 附录散点图 + 正文分组表/图；(3) 按 IV 分位数报告 DV 的均值/中位数单调趋势；(4) 跨组显著性检验。这为后续模型结果提供了视觉和描述性锚点，降低读者对复杂识别策略的认知门槛。
**诚实边界**: 无模型证据不能替代模型检验，也不能用于因果推断；必须在后续段落中明确过渡到控制混淆变量后的模型结果。
**跨 skill 对齐**: `../write-methods/econometric-models/面板数据-OLS.md` 变体20（M2.5 model-free evidence 预览）；`write-introduction/hooks/24-positive-trait-dark-side` 建立的读者预期在此得到实证承接。

### 变体 23: R5 四分位距经济显著性 — 从 P25 到 P75 的幅度翻译 (1篇高价值)
**来源论文**: Chung, Low & Rust 2022 (Journal of the Academy of Marketing Science)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-08
**槽位**: R3/R5
**骨架**:
> The coefficient for [IV] is [positive / negative] and statistically significant (β = [value], p < [threshold]). An interquartile move in [IV] from the 25th percentile to the 75th percentile is associated with a [N] [unit / percentage point] [increase / decrease] in [DV]. In untabulated tests, we also find support using [alternative sample / broader sample], with similar economic significance.
**与原骨架差异**: 现有经济显著性变体多用 "one-SD change → X%"，而本变体使用 **P25–P75 四分位距移动**作为幅度基准。这适用于 IV 分布偏斜、理论意义更对应"从中等偏低到中等偏高"情境的研究。关键：报告具体单位（如 0.29 percentage points）并在括号中说明是 percentage point 还是 percent，避免审稿人误解。
**诚实边界**: P25–P75 的解释隐含了 IV 在其分布中段的比较；若 IV 呈高度偏态或存在大量零值，应报告实际对应值（如 P25 = [value], P75 = [value]）而非仅说"interquartile"。
**跨 skill 对齐**: `../write-methods/econometric-models/micro-templates/interquartile-economic-significance.md`（M7/M8/M10 预告）；Results 在此兑现 Methods 中预告的经济显著性解释口径。

### 变体 24: R2 Heckman 两阶段表格导航 — 第一阶段 Table 3 → 第二阶段 Columns 1-4 (1篇高价值)
**来源论文**: Chung, Low & Rust 2022 (Journal of the Academy of Marketing Science)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-08
**槽位**: R2
**骨架**:
> Table [X] shows the results of the first-stage selection equation. Our exclusion restriction, [instrument], significantly and [positively / negatively] predicts [selection_DV] (β = [value], p < [threshold]), consistent with [theory / prior work: citation]. This confirms that [instrument] satisfies the relevance condition for identifying [selection_outcome]. Table [Y] reports the second-stage Heckman selection results. Column 1 tests Hypothesis [H1]: [IV] significantly and [positively / negatively] predicts [DV] (β = [value], p < [threshold]). Column 2 adds the two-way moderating relationships, providing support for Hypotheses [H2] and [H4]. Column 3 introduces the three-way interactions, supporting Hypotheses [H3] and [H5]. Column 4 shows that the results are robust to the inclusion of [firm fixed effects / alternative fixed-effect structure] instead of [industry fixed effects / original fixed-effect structure].
**与原骨架差异**: 现有 Heckman 导航（IV-2SLS.md 变体 r2_heckman_first_stage_navigation）侧重第一阶段排他性限制与相关性声明。本变体聚焦 **Results 正文中的两阶段表格递进导航**：先确认第一阶段排除限制显著（满足相关性），再逐列说明第二阶段四个模型分别检验哪些假设，使读者能清楚对应 Table 4 的列结构。适用于假设数量多、模型列数多、且使用 Heckman 选择模型的研究。
**诚实边界**: 若第一阶段工具变量不显著，不能进入第二阶段解释；必须报告逆米尔斯比（rho / lambda）的显著性，以判断选择偏误是否确实存在。
**跨 skill 对齐**: `../write-methods/econometric-models/两阶段模型.md` 变体3（Heckman 同行 prevalence 排他性限制）；`../write-methods/econometric-models/micro-templates/heckman-peer-prevalence-exclusion.md`（跨 segments 加权论证）。

### 变体 25: R7 替代 DV 证伪段落 — 领域外结果的预期不显著 (1篇高价值)
**来源论文**: Chung, Low & Rust 2022 (Journal of the Academy of Marketing Science)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-08
**槽位**: R7
**骨架**:
> An alternative way to establish causality is to provide a falsification test where we examine [alternative_DV], an outcome that is [not within / outside] the decision-making domain of [focal_actor]. We use the [estimator] specification in [Table X], Column [N], except that we replace [DV] with [alternative_DV] ([operational_definition_citation]). We find that [predicted_finding: e.g., the main effect or interaction of interest behaves as expected], which is consistent with [Hypothesis / mechanism]. As expected, the [interactions / effects] involving [actor-specific variables] are insignificant, because [alternative_DV] is not within the decision-making domain of [focal_actor]. Interestingly, [unexpected_but_theoretically_interpretable finding] suggests [interpretation clause].
**与原骨架差异**: 现有 R7 变体多关注稳健性（替换估计量、样本、测量），本变体扩展 R7 的 **falsification / 机制边界功能**：用理论预期之外不应出现效应的 DV 来确认主效应的因果解释。关键结构：(1) 明确说明替代 DV 不在某行为者的决策领域内；(2) 报告应显著的效应确实显著；(3) 报告不应显著的效应确实不显著；(4) 对意外发现给出理论化解释而非忽略。这比单纯"结果稳健"更能支持因果识别。
**诚实边界**: 替代 DV 必须与主 DV 有理论上的领域边界；不能事后挑选一个"不显著"的结果作为证伪。应在 Methods 或稳健性部分预先说明为何该 DV 是合适的 falsification 目标。
**跨 skill 对齐**: `../write-methods/econometric-models/micro-templates/alternative-dv-falsification.md`（M8/M10 预告替代 DV 设计与替代/转换解释）。

### 变体 26: R7 内生性稳健性表叙事 — threat-by-threat Table 7 汇总 (1篇高价值)
**来源论文**: Chung, Low & Rust 2022 (Journal of the Academy of Marketing Science)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-08
**槽位**: R7
**骨架**:
> Endogeneity is mainly caused by issues relating to omitted variables and simultaneity ([citation]). In our empirical model setup, we include [control_strategy: e.g., as many control variables as possible] to rule out omitted variables and use [temporal_strategy: e.g., lagged measures of IV] to ensure causal priority. We have also used the [DWH test / Hausman test] with strong instruments and [cannot reject / reject] the null hypothesis that [IV] is exogenous. This conclusion is also validated with the [instrument-free Gaussian copula estimation method / alternative instrument-free method].
>
> To complement these general endogeneity tests, we next look at specific sources of endogeneity and design tests to rule them out. We tabulate these tests in Table [X] and relegate the details to the [web appendix] for reasons of space. Our results are not due to [threat_1: reverse causality] because [test_1_result]. Nor are they driven by [threat_2: selection on observables / unobservables] because [test_2_result]. To rule out [threat_3: omitted executive / firm characteristics], we [test_3_method]; the results are generally similar. [threat_4: risk tolerance / alternative trait] is also unlikely to be driving the results, as we find robust results when [test_4_method]. The supporting evidence from all these complementary tests confirms the results of the [DWH / copula] test that there is little reason to believe that endogeneity issues are solely driving the results we observe.
**与原骨架差异**: 现有 R7 变体 1（Table 9 矩阵）和变体 2（叙事型逐 threat）分别适用于大量和小量稳健性检验。本变体是 **"一般性内生性检验 + threat-by-threat 表" 的复合结构**：先以 DWH / Gaussian copula 提供一般性证据，再用 Table 7 式矩阵逐项处理具体威胁（reverse causality, selection, omitted variables, alternative traits）。关键：最后一句用"little reason to believe that endogeneity issues are solely driving the results" 的谨慎措辞，避免过度因果断言。
**诚实边界**: 若 DWH 或 copula 结果不一致，必须诚实报告并讨论可能原因；不能仅因为"多数稳健性通过"就宣称完全排除内生性。"solely driving" 是审慎措辞，不应升级为"完全排除"。
**跨 skill 对齐**: `../write-methods/econometric-models/IV-2SLS.md` 变体5（DWH 检验 + Gaussian copula 内生性叙事）；`../write-methods/econometric-models/micro-templates/identification-exogeneity.md`（通用外生性论证）。

### 变体 27: 多阶段同 IV 管道衰减 profile — 同一 IV 跨序贯决策阶段的方向/显著性对比 (1篇高价值)
**来源论文**: Kim & Lee 2026 (Strategic Management Journal)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-22
**槽位**: R3+R9
**骨架**:
> [Stage 1 — Front-end] We begin by examining the association between [IV] and [stage-1 outcome]. Model [1] finds a [direction] association (p [relation] [threshold]); this remains stable in Model [2] with [controls]; Model [3] adds [fixed effects], estimating [within-unit] differences, and continues to find a [direction] association (p [relation] [threshold]) corresponding to [economic magnitude].
>
> [Stage 2 — Mid-pipeline] For the [stage-2] stage (unit = [stage-2 pair]), Model [4] estimates [direction] but imprecisely (p = [value]); Model [5] adds [characteristics]; Model [6] adds [fixed effects], producing a [stronger] association (p = [value]) [equivalent to magnitude]. Because the [within-unit] analysis is likely most informative, we interpret these as [suggestive evidence of ...].
>
> [Stage 3 — Back-end null] We use [Cox proportional hazards / estimator] for [stage-3 outcome]. Model [7] estimates [direction] and imprecise (p = [value]); Model [8] similar with [controls] (p = [value]); Model [9] with [full controls] turns the coefficient [opposite direction] but remains imprecise (p = [value]).
>
> [跨阶段对比句] In summary, we fail to find compelling evidence of an association between [IV] and [stage-3 outcome]. This lack of association contrasts with the advantages that [IV] appears to enjoy in the [stage-1] and [stage-2] stages, and is consistent with the possibility that [IV] advantages operate primarily through a [front-end / signaling mechanism] that attenuates once [actors gain direct experience]. A [signaling/attenuating mechanism] fits this pattern... We cannot definitively adjudicate, but the full-pipeline evidence suggests [mechanism that fits the front-significant/back-null pattern].
**与原骨架差异**: 区别于 多研究.md 的 cross-study synthesis（多研究独立样本收敛）——本变体是 **single-study single-IV multi-stage**：同一 IV 跨序贯决策阶段的衰减 profile。核心叙事装置是**跨阶段对比句**（"This lack of association contrasts with the advantages... in the [earlier] stages"）——把"前置显著 + 后置 null"从孤立报告提升为机制发现（用 null 在管道中的位置裁决竞争机制：signaling 随经验衰减 vs enduring preference 持续）。配套 write-methods 见 多研究.md 变体6（管道设计）；配套 post-treatment caveat 见 slot-R6（Slough 2023）。
**诚实边界**: post-treatment 样本递减让跨阶段估计量来自非随机子样本——后置 null 不可作"无效应"因果结论（见 slot-R6 Slough 变体）。机制裁决须诚实对冲（"cannot definitively adjudicate but full-pipeline evidence suggests"），不可过度断言。

### 变体 28: R2 — 截面 OLS/FE 中二元内生变量 + 样本选择的双阶段修正表导航 (1篇高价值)
**来源论文**: Pupovac, Astvansh, Carrillat & Legoux 2026 (Production and Operations Management)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-21
**槽位**: R2
**骨架**:
> Table [x] reports the estimates from the regression that assumes [endogenous_predictor] is exogenous. Columns II and III present estimates from the [control_function / Heckman] method, which controls for [endogeneity_type]. Column II shows that [instrument] is [positively/negatively] associated with [endogenous_predictor] (β = [value], p < [threshold]), consistent with [theory] and suggesting that the [relevance/exclusion] condition is likely satisfied. Column III reports the second-stage coefficient on [endogenous_predictor], which we use to test Hypothesis [x].
**与原骨架差异**: 现有 OLS-FE 变体 24 是 Heckman 两阶段表格导航（第一阶段 Table 3 → 第二阶段 Columns 1-4）。本论文同时使用 **Control Function（处理二元内生自变量）和 Heckman（处理样本选择）**，且两种方法的第一阶段结果都嵌入同一张表。本骨架提炼跨方法的通用 R2 导航：先报无修正列，再报第一阶段工具变量/排除限制相关性，最后报第二阶段核心系数。适用于截面 OLS/FE 中同时存在内生解释变量和选择偏误的研究。
**诚实边界**: 若第一阶段工具变量或排除限制不显著，不能进入第二阶段解释；必须报告控制函数残差项或逆米尔斯比的显著性，以判断内生性/选择偏误是否真实存在。

### 变体 29: R7 — 选择偏误三步防御：描述性模式 → CEM → Heckman + 关联非因果收尾 (1篇高价值)
**来源论文**: Du & Tsolmon 2024 (Organization Science)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-25
**槽位**: R7
**骨架**:
> (1) We recognize that [treatment/IV] decisions are not random. To explore the extent to which selection may be influencing our findings, we examine patterns of [IV] across different types of [units]. We find no strong evidence that [IV] is systematically driving [selection]: [percentages across categories]; the correlations between [IV] and [selection type] are near zero ([value]). (2) To more rigorously examine potential selection on observables, we employ a coarsened exact matching (CEM) strategy, matching on [covariates]. In the matched sample, [IV] remains [direction] associated with [outcome] (B = [value], p < [threshold]). (3) We also conduct a Heckman two-stage model for selection from unobservables, using [instrument] which predicts [selection] but is uncorrelated with [outcome] (correlation = [value], n.s.). (4) These analyses suggest our findings are not merely reflective of [selection mechanism]. We interpret our results as associational, consistent with the proposed theoretical mechanisms, but not as definitive causal evidence.
**与原骨架差异**: 区别于变体 24（Heckman 表格导航）与变体 26（一般性内生性 threat-by-threat）。本变体是 **selection-specific 的递进式防御**——model-free 描述性诊断（IV 不驱动选靶）→ CEM（可观测）→ Heckman（不可观测），每一步处理更深一层的选择来源，且以"associational not causal"诚实收尾。
**诚实边界**: 三步必须递进（不能只做 CEM 就收尾）；CEM 需报告匹配变量与平衡改善位置；Heckman 必须明确报告工具变量与结果不相关；收尾必须降权为 associational。

### 变体 30: R6/R8 — 预测性零结果作为机制证据：排除替代解释的 null-finding 反转 (1篇高价值)
**来源论文**: Du & Tsolmon 2024 (Organization Science)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-25
**槽位**: R6（零结果）/ R8（补充分析）
**骨架**:
> Interestingly, we find no statistically significant [market/early outcome] at [event time] (see [CAR/short-window] analyses in [table]). This null finding suggests that the observed associations with [long-run outcome] likely reflect [proposed mechanism] dynamics rather than [alternative explanation such as selection at event time].
**与原骨架差异**: 零结果不是失败，而是**排除替代解释的证据**——若 selection-at-event-time 成立，事件窗反应应显著；反应不显著 → 长期关联来自机制动态而非时点选择。区别于一般 R6 非显著处理（报方向→不显著→不解释幅度→不支持），本变体**主动反转利用**零结果。
**诚实边界**: 使用条件严格——零结果须被理论预测、替代解释须预测非零结果、零结果须嵌入在更大的显著结果模式中（不能孤立地用 null 论证机制）。

### 变体 31: R7 — 替代解释三连驳斥 + 异质性模式作为机制裁决收束 (1篇高价值)
**来源论文**: Du & Tsolmon 2024 (Organization Science)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-25
**槽位**: R7
**骨架**:
> We consider [N] alternative factors. First, [alternative 1] could drive both [selection] and [outcome]. Our [method 1, e.g., CEM matching on X/Y/Z] partially addresses this concern; the persistence of our findings in the matched sample suggests [alternative 1] alone may not explain our results. Second, [alternative 2]: our [method 2] helps control for [it]. Third, [alternative 3]: our [method 3] partially addresses this, and our finding that [IV] matters more for [high-moderator conditions] suggests our mechanism extends beyond simple selection on [alternative 3]. Although we cannot eliminate all alternative explanations given our observational design, our pattern of results—particularly heterogeneous effects by [moderator 1], [moderator 2], and [moderator 3]—aligns more closely with our [mechanism] than with these alternatives.
**与原骨架差异**: 每个替代解释用 "our [method] partially addresses this" 部分回应（不夸大为完全排除），收束句用**异质性模式本身**裁决——H3-H5 的调节显著性被二次利用为替代解释驳斥工具。关键是比较级措辞（"aligns more closely... than"）而非绝对排除。
**诚实边界**: 异质性裁决必须建立在已报告的调节显著性之上；"partially addresses" 的克制措辞不可省略；比较级收束（more closely than）不可替换为绝对断言（rules out）。

### 变体 32: R4 — 外部基准阈值分割 + 边际效应图阈值发现：连续调节的三层验证 (1篇高价值)
**来源论文**: Du & Tsolmon 2024 (Organization Science)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-25
**槽位**: R4
**骨架**:
> (1) The estimated coefficient on the interaction term between [continuous moderator] and [IV] is [direction] and [marginally] significant (B = [value], p = [value]). (2) We split the sample by the threshold of [N units], which corresponds to the definition of [external benchmark label] by [authoritative body]. The estimated coefficient is larger and significant in the [high-moderator] subsample (B = [value], p = [value]) than in the [low-moderator] subsample. (3) The marginal effects plot shows that the threshold at which [moderator] starts to matter is around [value], which corresponds to [external label corroboration].
**与原骨架差异**: 区别于变体 9（±1SD 条件边际效应）与变体 14（低基础率直方图）。本变体的核心是**阈值的外部锚定 + 数据发现的双向验证**——分割点来自权威基准（如 Census 定义）而非任意中位数，且边际效应图发现的阈值再用外部标签印证。
**诚实边界**: 外部基准必须真实存在且可引用；边际效应图发现的阈值与外部基准不能完全等同（本文 54.6 miles vs 50 miles benchmark——需说明对应关系）；跨子样本系数对比宜配 Wald 检验（本文缺失，见反模式）。

### 变体 33: R8 — 下游绩效事后分析：时间增长 + 多指标收敛 + 提示性收尾 (1篇高价值)
**来源论文**: Du & Tsolmon 2024 (Organization Science)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-25
**槽位**: R8
**骨架**:
> We examine whether [IV] is associated with improved [downstream outcome]. [Outcome] is measured as [Δ metric] from pre-[event] to [1-N year] post-[event] averages. Results show that [IV] is positively associated with [outcome] in [scope condition]. The positive relationship grows over time, with a one-SD increase in [IV] linked to a [X]% rise in [outcome] relative to the sample average by year [N]. These findings are robust to alternative measures ([BHAR / Tobin's Q]); additionally, [IV] is associated with lower likelihood of [negative marker]. We note that these analyses draw on a smaller subsample and treat these results as indicative rather than conclusive, offering suggestive but consistent evidence.
**与原骨架差异**: 区别于变体 5（MCMC 中介）与变体 21（枚举清单）。本变体展示**下游结果 post hoc 的完整展演**——时间动态（效应随时间增长）+ 多指标收敛（ROA/BHAR/Q/goodwill）+ 明确降权（indicative not conclusive）。
**诚实边界**: 下游绩效分析必须标注子样本缩小；"grows over time" 需有跨年数据支撑；提示性收尾（suggestive but consistent）不可省略，不可把 post hoc 绩效当 confirmatory 证据。

### 变体 34: R3 — 2×2 类型学交叉对角描述性比较：回归前的非参数类型对比 (1篇高价值)
**来源论文**: Du & Tsolmon 2024 (Organization Science)
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-25
**槽位**: R3
**骨架**:
> [Table] reports the share of [outcome] by [actor A type] and [actor B type] in [scope condition]. Mirroring our main results, [match cells] have the highest [outcome]. In the cross-diagonals, [X]% of [outcome] for [mismatch cell A] compared with [Y]% for [mismatch cell B] (the difference is significant at [level]). This pattern suggests that [theoretical interpretation: which mismatch direction is worse and why]. We examined this more formally in a regression model ([table]): the interaction term between [dissimilarity] and [type indicator] is [direction] and significant (B = [value], p = [value]).
**与原骨架差异**: 区别于变体 22（四分位单调性 model-free 开场）。本变体处理**类型学设计的非对称交叉对角**——理论载荷在"哪个错位方向更糟"（如 LM acquirer×MM target 比 MM acquirer×LM target 更差），用非参数单元格均值为回归交互提供直觉锚定。
**诚实边界**: 交叉对角差异的检验方法必须指明（t-test 类型——本文未指明，见反模式）；2×2 单元格均值只是描述性锚定，结论须由回归交互确认；理论解读须回应"为何这个错位方向更糟"。

## 反模式

| 反模式 | 表现 | 应做 |
|--------|------|------|
| **稳健性检验仅在 4.1 Post-hoc 枚举带过** | 正文未按 threat 组织稳健性叙事，仅列出分析名称 | 少量稳健性用变体 2 叙事型；大量稳健性用变体 1 Table 9 矩阵 |
| **曲线关系仅报线性+二次系数** | 倒 U 型关系未做 Lind-Mehlum 三步验证和转折点 CI | 使用变体 17 的完整协议 |
| **曲线调节只说交互显著** | 未解释二阶交互项符号、未用 flatten/steepen 描述曲线形状 | 使用变体 18 的图形语言 |
| **多项式/交互模型未报告 mean-centering 和 condition number** | 高阶项和交互项可能造成多重共线性但未诊断 | 使用变体 20 的三重诊断 |
| **显著性语言不一致** | 同一论文中 p=0.052 称 "significant" 而 p=0.071/0.075 称 "marginal" | p > 0.05 一律统一标 "marginally significant"（du_tsolmon2024 警示案例） |
| **Split-sample 系数对比无 Wald 检验** | 仅用 "larger vs smaller" 描述性断言跨子样本系数差异（0.190 vs 0.069），未检验系数相等性 | 跨子样本系数对比须配 Wald χ² / seemingly unrelated estimation 检验（du_tsolmon2024 警示案例） |

## 诚实边界

- **曲线关系效应量**：Cohen's d 的计算基准需在 Methods 或 Appendix 说明，不可直接套用线性公式。
- **转折点 CI**：转折点置信区间必须落在数据范围内，否则倒 U 型证据不足。
- **非中心复制**：mean-centering 后报告非中心化系数是可选策略，但需解释为何更便于解释；若中心与非中心结果不一致，需讨论。
- **Post-hoc 标签**：将 "robustness checks" 与 "additional insights" 并列时，应逐条标注哪些是确证性稳健性、哪些是探索性分析，避免审稿人质疑。
