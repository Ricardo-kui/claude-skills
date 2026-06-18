---
result_type: "OLS-FE"
status: 📋 TEMPLATE
source_papers:
  - "darby2026_faster_recalls_large_institutional_ownership_jom"
  - "eilert2017_recall_timing_automobile_jm"
  - "darby2023_ceo_stock_ownership_recall_timing_msom"
  - "zhao_ding_gaba_2023_positioning_digital_markets_orsc"
variants_count: 7
created: 2026-05-18
updated: 2026-06-17
---

# OLS-FE — Results 骨架

## 主骨架

参见 `write-results/SKILL.md` → 填空段落骨架 → `OLS-FE`。

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
