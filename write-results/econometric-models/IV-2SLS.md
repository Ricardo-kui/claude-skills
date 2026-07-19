---
result_type: "IV-2SLS"
status: 📋 TEMPLATE
source_papers:
  - "wowak2025_tmt_political_ideology_ms"
  - "qiao_hiatt_sine2026 (SMJ, 2026): control-function residual as nonlinear DWH test + finite-sample-bias caveat"
variants_count: 4
created: 2026-05-18
updated: 2026-06-16
---

# IV-2SLS — Results 骨架

## 主骨架

参见 `write-results/SKILL.md` → 槽位骨架加载 → 本类型适用的 `references/slot-R*.md`（各 slot 文件内含 `IV-2SLS` 专用变体）。

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

### 变体 4: 非线性估计器下的 IV — 控制函数残差作 DWH 检验 + 有限样本偏误诚实提示 (1篇高价值)
**来源论文**: Qiao, Hiatt & Sine 2026 (SMJ)
**验证状态**: 通过 (单篇高价值，生存/有限因变量模型下内生性检验的标准做法 + 罕见的诚实提示)
**写入日期**: 2026-06-16
**槽位**: R2/R3
**骨架**:
> [Table, Column] shows that the instrument, [instrument], is [direction] related to [the endogenous regressor] (β = [value], p < [threshold]), and the first-stage F-statistic of [value] exceeds the cutoff for 10% maximal bias ([cutoff]) according to Stock and Yogo ([2005]). Because standard Durbin–Wu–Hausman tests rely on linear-model assumptions and are not valid for [nonlinear survival / limited-DV] models, we adopted a control-function approach in which the first-stage residual is included in the [second-stage hazard / outcome] equation; whether this residual is statistically distinguishable from zero constitutes the nonlinear analogue of a Durbin–Wu–Hausman test for endogeneity ([Terza et al., 2008]; [Wooldridge, 2010, 2015]). The residual term is significant (β = [value], p = [threshold]), indicating that [the un-instrumented specification] is subject to the endogeneity concerns Shaver ([2005]) raised. [Next column] then shows that the instrumented [treatment] is [direction] related to [outcome] (β = [value], p < [threshold]). This method, however, is sensitive to finite-sample bias, often inflating the coefficient on the instrumented variable, and should be interpreted with caution ([citation]).
**与原骨架差异**: 解决一个被普遍回避的问题——**非线性估计器（生存/Probit/Tobit）下如何检验内生性**。标准 DWH 假设线性，不能直接用于生存模型；本变体用 **control-function**：把第一阶段残差放入第二阶段风险方程，残差显著即内生性存在的非线性等价检验（Terza et al. 2008; Wooldridge）。关键诚实提示（**不可省略**）：control-function 对有限样本敏感，常**放大**工具变量系数，故 IV 系数应解读为方向性证据而非点估计。适用于任何非线性主模型 + IV 设计（生存分析、Probit、Tobit）。配合 `../write-methods/econometric-models/IV-2SLS.md` 变体 4（外部自然事件 IV）使用。
