---
design_type: "PSM匹配面板"
status: 📋 TEMPLATE
source_papers:
  - "darby2026_faster_recalls_large_institutional_ownership"
  - "darby2023_ceo_stock_ownership_recall_timing_msom"
variants_count: 2
created: 2026-05-18
updated: 2026-05-20
---

# PSM匹配面板 — Methods 骨架

## 主骨架

参见 `write-methods/SKILL.md` → 填空段落骨架 → `PSM匹配面板`。

## 设计特征摘要

- **匹配方法**: CEM (Coarsened Exact Matching) / PSM (Propensity Score Matching)
- **平衡检验**: L1 measure / common support / mean differences
- **适用场景**: 处理可观测选择偏差，建立处理组与对照组的可比性
- **诚实边界**: CEM不能替代对不可观测混淆的讨论，需在Limitations中说明残余威胁
- **跨论文复现率**: CEM在 2/4 产品召回论文中出现——Darby2026 (主分析) / Darby2023 (稳健性检验)

## 累积变体

### 变体 1: CEM 五步论证链 (主分析版本)
**来源论文**: Darby2026 JOM / Darby2023 MSOM
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
