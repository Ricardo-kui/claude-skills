---
design_type: "PSM匹配面板"
status: 📋 TEMPLATE
source_papers:
  - "darby2026_faster_recalls_large_institutional_ownership"
  - "darby2023_ceo_stock_ownership_recall_timing_msom"
  - "qiao_hiatt_sine2026 (SMJ, 2026): entropy balancing (EBM) — reweights control moments, keeps all observations"
variants_count: 3
created: 2026-05-18
updated: 2026-06-16
---
# PSM匹配面板 — Methods 骨架

## 变体速查表

> 检索辅助。状态词表：通过（N/5 复现）> 通过（双篇/专家审计）> 通过（单篇）> 待第二篇交叉验证 > 可选变体。完整骨架与诚实边界见下方变体正文。

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 1 | CEM 五步论证链（主分析版本） | 匹配作为主识别流程、需完整五步论证（目标与威胁→方法原理→协变量选择→匹配结果→平衡检验）时（槽位 M8/M2） | — | 通过（2/4 复现） | Darby2026 JOM / Darby2023 MSOM |
| 2 | CEM 作为外生冲击的稳健性验证 | 匹配作为稳健性检验、处理变量是外生冲击（如 CEO 变更）而非内生变量本身时（槽位 M8） | 与变体 1 的关键区别：处理变量是外生冲击；关键时点规则确保 treatment exposure 完整；CEM 出现在稳健性而非主分析 | 可选 | Darby2023 MSOM |
| 3 | Entropy Balancing (EBM) — 重加权、保留全部观测 | 处理组样本稀少需保留全部观测（CEM/PSM 丢弃后效力不足）、或需维持生存分析事件历史结构时（槽位 M8） | 与变体 1（CEM 五步链）区别：不丢观测，对控制组重加权使其协变量矩匹配处理组 | 通过（单篇） | Qiao, Hiatt & Sine 2026 SMJ |


## 主骨架

参见 `write-methods/SKILL.md` → 槽位骨架加载 → 本类型适用的 `references/slot-M*.md`（各 slot 文件内含 `PSM匹配面板` 专用变体）。

## 设计特征摘要

- **匹配方法**: CEM (Coarsened Exact Matching) / PSM (Propensity Score Matching)
- **平衡检验**: L1 measure / common support / mean differences
- **适用场景**: 处理可观测选择偏差，建立处理组与对照组的可比性
- **诚实边界**: CEM不能替代对不可观测混淆的讨论，需在Limitations中说明残余威胁
- **跨论文复现率**: CEM在 2/4 产品召回论文中出现——Darby2026 (主分析) / Darby2023 (稳健性检验)

## 累积变体

### 变体 1: CEM 五步论证链 (主分析版本)
**来源论文**: Darby2026 JOM / Darby2023 MSOM
**原始句锚点**: While AFT models account for the fact that the likelihood of an event (i.e., a recall) changes with the passage of time due to underlying factors (Bhattacharjee et al. 2007), they may not account for characteristics that influence a firm’s ownership stakes and the time-to-recall. To address concerns related to selection on observable characteristics, we first processed our data using CEM (Yılmaz et al. 2024).
**验证状态**: 通过 (2/4 复现)
**写入日期**: 2026-05-19
**更新日期**: 2026-05-20 (新增 Darby2023 MSOM 复现)
**槽位**: M8 / M2
**骨架**:
> While [base_estimator] account for [capability_1], they may not account for [threat]. To address concerns related to [threat_type], we first processed our data using [method] ([citation]).
>
> The underlying goal of [method] is to [objective] by [mechanism] ([citation]). Following previous research (e.g., [citations]), we used a [split_type] of the focal variable ([IV]) for the treatment. The treatment group consists of [definition], whereas the control group consists of [definition].
>
> We selected [covariate] as the primary matching covariate to address [concern] that may influence [treatment] as well as [outcome]. The underlying rationale is that [theoretical_reason_for_correlation], and [additional_reason] ([citation]). For the primary analysis, the aim was to [tradeoff_objective]—in other words, "[quote_about_tradeoff]" ([citation], [page]). As described in the robustness checks, we [verification_strategy].
>
> The primary matching covariate, [covariate], was coarsened using [algorithm] ([citations]). This process yielded [N] matched strata containing [N_treated] treated observations and [N_control] control observations for a total of [N_total] observations. [Weights] then were used to [weight_application] ([citation]).
>
> Unlike other matching techniques (e.g., [alternative_method]), there is "[quote_about_method_property]" for [method] ([citation], [page]). However, [balance_measure] is often used to [purpose]. This measure is "[quote_about_interpretation]" ([citation], [page]). The overall [measure] [value_before] before matching to [value_after] after matching, which indicates [interpretation]. [Table_reference] presents the [details]. The [changes] suggest [conclusion] ([citations]).
**与原骨架差异**: 这是CEM的**完整五步论证链**。关键要素：(1) 目标与威胁声明；(2) 方法原理；(3) 协变量选择与理论依据；(4) 匹配结果；(5) 平衡检验。Darby2026将此结构用于主分析（M2/M7），Darby2023将其简化为稳健性检验中的一段（M8）。PSM版本需替换为propensity score估计和common support检查。

### 变体 2: CEM 作为外生冲击的稳健性验证
**来源论文**: Darby2023 MSOM
**原始句锚点**: We address this endogeneity concern by exploiting an exogenous shock in our data—a change in a firm’s CEO. A change in the CEO is an exogenous shock to the amount of stock owned by a CEO, contingent upon one key criterion: Past recalls should not predict the likelihood of the previous CEO’s departure.
**验证状态**: 可选变体 (1/4，将CEM置于稳健性检验的新位置)
**写入日期**: 2026-05-20
**槽位**: M8
**骨架**:
> Our finding that [IV_effect_summary] may be subject to endogeneity. It is possible that [endogeneity_threat]. We address this endogeneity concern by exploiting an exogenous shock in our data—[exogenous_event]. [Event] is an exogenous shock to [treatment], contingent upon one key criterion: [exclusion_condition]. This ensures that [exogeneity_rationale].
>
> To test this, we first used [method] ([citation]). In our study, the treatment group consists of [definition_when_exogenous_event_occurred], whereas the control group consists of [definition_when_not]. To use this treatment, we first needed to identify [units] in which there was [exogenous_event]. We assign the variable [treatment_var] as a one for all [observations] in which [condition] and zero otherwise. Importantly, we only assigned this measure as a one if [timing_condition]—not [alternative_timing]. This distinction ensures that our treatment group only captures [observations] in which [treatment_exposure_was_complete].
>
> We matched each observation in the treatment group to those in the control group based on [N] pretreatment variables—[var_list]—that address [rationale] ([citations]). This process yielded [N] matched strata containing [N_treated] treated observations and [N_control] control observations for a total of [N_total] observations across [N] firms from [year_start] to [year_end]; [N_excluded] observations were not matched in any stratum and thus were excluded from the analysis.
**与原骨架差异**: 与变体1(主分析CEM)的关键区别：(1) **处理变量是外生冲击**（如CEO变更）而非内生变量本身（如CEO持股）；(2) 关键时点规则确保treatment exposure完整（"CEO was in the role prior to defect awareness date, not recall initiation date"）；(3) CEM在稳健性检验而非主分析中出现，用于验证内生变量效应的稳健性。这为匹配方法创造了一种新的使用位置——不仅是建立可比样本，更是**外生冲击验证工具**。

### 变体 3: Entropy Balancing (EBM) — 重加权、保留全部观测 (1篇高价值)
**来源论文**: Qiao, Hiatt & Sine 2026 (SMJ)
**原始句锚点**: Table S2 shows the covariate balancing results after EBM: after matching, the differences of all control variables, in terms of their means, between the treatment and control groups become negligible. These results suggest that the treatment we have can be seen as random to the extent that we have ruled out selection on these observable variables.
**验证状态**: 通过 (单篇高价值，EBM 区别于 CEM/PSM 的关键卖点论证清晰)
**写入日期**: 2026-06-16
**槽位**: M8
**骨架**:
> We employed the entropy balancing matching (EBM) approach ([citation]). Like propensity score matching (PSM) and coarsened exact matching (CEM), EBM matches [treated and control units] on covariates. However, whereas [PSM and CEM drop a significant portion of observations], EBM does not drop observations but reweights the control group so that the statistical moments (mean, standard deviation, skewness, and even kurtosis) of the covariates are similar between the treatment and control groups. [Table] shows the covariate balancing results after EBM: after matching, the differences of all control variables, in terms of their means, between the treatment and control groups become negligible. These results suggest that the treatment can be seen as random to the extent that we have ruled out selection on these observable variables.
**与原骨架差异**: 与变体 1（CEM 五步链）的关键区别——EBM **不丢弃任何观测**，通过对控制组重加权使其协变量分布（均值/标准差/偏度/峰度）匹配处理组，而非分层后保留共同支持区。适用场景：(1) 处理组样本本就稀少（如创始军方关联的航空公司），CEM/PSM 丢弃后统计效力不足；(2) 需要保留全样本以维持生存分析的事件历史结构。诚实边界：EBM 仍只处理可观测选择偏差，不可观测混淆需配合 IV/RDD；重加权可能放大少数观测的影响，应在结果稳健性中检验。本论文将 EBM 与 time-based RDD（WWII 断点）+ 外生子样本（军方内部诞生的航空公司）并用，三重识别策略互补。
