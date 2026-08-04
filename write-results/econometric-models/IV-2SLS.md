---
result_type: "IV-2SLS"
status: 📋 TEMPLATE
source_papers:
  - "wowak2025_tmt_political_ideology_ms"
  - "qiao_hiatt_sine2026 (SMJ, 2026): control-function residual as nonlinear DWH test + finite-sample-bias caveat"
  - "moon_tuli_mukherjee_2023_jm (Journal of Marketing): robustness exception ledger distinguishing stable, form-sensitive, and fragile inferences"
variants_count: 7
created: 2026-05-18
updated: 2026-08-03
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

### 变体 5: R7 "去 IV" 稳健性 — 用非工具变量估计展示内生性偏误低 (1篇高价值)
**来源论文**: Wowak2025 MS
**验证状态**: 通过（单篇高价值；corpus 此前无"移除识别策略以反向论证偏误低"的元稳健性变体）
**写入日期**: 2026-07-25
**槽位**: R7
**骨架**:
> We next repeat our analyses without instrumental variables. [Table], columns [X] and [Y] suggest that [IV] is [negatively] related to [DV_1] (β = [value]; p < [threshold]) and [positively] associated with [DV_2] (β = [value]; p < [threshold]). Although we employed IVs that met the relevance and exclusion criteria in our main analysis, the consistency of our results from the noninstrumented approach indicates that bias from endogeneity may be relatively low in our setting.
**与原骨架差异**: 与"加 IV 防御内生性"的标准逻辑相反——本稳健性**移除 IV**重跑，用"非工具变量估计与工具变量估计一致"反向论证内生性偏误不大。这是对识别策略本身的**元稳健性**（meta-robustness about the identification strategy），完成两个说服动作：(1) 验证 IV 不是在扭曲估计（IV 与非 IV 系数一致 → IV 未引入偏误）；(2) 安抚读者即使没有重型识别机器，核心结论也成立。与变体 3（IV 诊断嵌入 R3）互补——变体 3 证明 IV *有效*，本变体证明 IV *非必需但仍用*（abundance of caution 的实证呼应，见 write-methods IV-2SLS 变体 9）。
**适用**: IV/2SLS 主分析研究中，IV 估计与非 IV 估计方向/显著性可比时；展示方法选择（是否用 IV）不影响核心结论。配合 write-methods IV-2SLS 变体 9（"abundance of caution" 叙事）形成完整的 IV 防御闭环。
**禁忌**: 若 IV 与非 IV 估计差异大，本稳健性会**暴露问题**——此时必须解释差异（如内生性真实存在 → IV 估计才是可信的），不能声称"偏误低"；本变性**不能**用作 IV 诊断缺失的借口——仍须报告完整 IV 诊断（变体 3）；"relatively low" 是谨慎措辞，不可升级为 "no endogeneity"。

### 变体 6: R8 离散度 post hoc — "best of both" 调和型事后分析 (1篇高价值)
**来源论文**: Wowak2025 MS
**验证状态**: 通过（单篇高价值；corpus 此前无"焦点构念从均值转向离散度、并框架为调和两极张力"的 post hoc 变体）
**写入日期**: 2026-07-25
**槽位**: R8
**骨架**:
> A logical conclusion from our research is that [actors] may [action—e.g., diversify the group] in the hopes of having both [benefit_1] and [benefit_2]. In this post hoc analysis, we examine the influence of [dispersion construct] on both [DV_1] and [DV_2] in order to provide actionable and tested managerial implications. Following research precedence on capturing dispersion within a group ([citations]), we measure [dispersion construct] using the standard deviation of [members]' [trait] in each [unit-time], scaled by the mean [trait] of the [group]—the coefficient of variation of [trait]. Thus, [dispersion construct] takes larger values when the [trait] of the [group members] are more dispersed away from a central tendency and smaller values when [members] tend to share [trait]. [Illustrative contrast: two units with the same mean trait but different dispersion—e.g., equal staunch [pole_A] and ardent [pole_B] vs. all members with similar trait.]
>
> The results from our [estimator] models specified with [dispersion construct] for both [DV_1] and [DV_2] are shown in [Table]. Consistent with the implication from our study, our estimators suggest that [dispersion] is associated with both [benefit_1 outcome] and [benefit_2 outcome], capturing the positive aspects of both [pole_A] and [pole_B], as [dispersion construct] is [negatively] related to [DV_1] (β = [value]; p < [threshold]) and [DV_2] (β = [value]; p < [threshold]).
**与原骨架差异**: 区别于变体 3（mediation post hoc 解释"为什么"）——本变体是**离散度（coefficient of variation）作为新焦点预测变量的 post hoc**，回答"该怎么办"（actionable mitigation）。三个关键转移：(1) **焦点构念从均值（trait level）转向离散度（trait dispersion/diversity）**——同一数据生成完全不同的理论构念；(2) **"best of both" 框架**——调和主结果中两极各赢一个维度的张力（[pole_A] wins on DV_1, [pole_B] wins on DV_2 → dispersion captures both benefits）；(3) 用同估计器对两 DV 重复，展示离散度**同时改善两维度**。CV = SD/mean 的测量选择有方法论引用支撑（Baginski et al. 1993; Busenbark et al. 2017）。诚实边界：post hoc 性质须明确标注（非 confirmatory hypothesis），且须包含低阶构成项（mean + SD）以满足 ratio 变量规范。
**适用**: 主结果发现两个对立群体/条件各赢一个维度（如 liberal 更少召回 + conservative 更快召回；exploration 创新 + exploitation 效率）的研究；任何用群体内离散度/多样性作为可操作干预杠杆的 post hoc；需要 "actionable + tested" 管理含义、把"发现"转化为"干预"的研究。
**禁忌**: 离散度必须是**可操作的管理干预**（如 TMT 构成、团队组合可调整）——不可操作的稳定特质不适用；"best of both" 框架要求主结果中两极**确实各赢一个维度**（若一极全胜则无 "both" 可言，应换框架）；CV 测量须引用离散度测量文献且报告低阶构成项；post hoc 须标注为探索性，不可包装成 confirmatory（见反模式"事后分析未标记"）。

### 变体 7: R6/R7 稳健性例外账本——稳定结论、形态变化与脆弱边界分层报告

**来源论文**: Moon, Tuli & Mukherjee (2023, *Journal of Marketing*)
**验证状态**: 单篇高价值 reference-level 变体，待跨论文验证
**写入日期**: 2026-08-03
**槽位**: R6/R7
**骨架**:
> We assess the sensitivity of our conclusions to [alternative measurement], [alternative instrument families], [alternative classification], and [additional omitted-information control]. The headline conclusions for [core hypotheses] remain consistent. Two qualifications are important. First, the mediation inference changes from [partial] to [complete/stronger] because [the direct path becomes weaker/nonsignificant] under [specification]. Second, the evidence for [weakly supported moderator] becomes nonsignificant under [alternative specification]. We therefore treat [headline effect] as robust, the exact form of [mediation] as specification-sensitive, and [moderator hypothesis] as weaker evidence.

**与原骨架差异**: 常见 R7 用 “results remain unchanged” 抹平所有规格差异；本变体把稳健性结论分成三层：(1) 方向与显著性稳定的 headline；(2) 结论仍成立但**形式改变**的机制（partial ↔ complete mediation）；(3) 在合理替代规格下消失的脆弱边界。稳健性段因此既维护核心发现，也更新证据权重。

**诚实边界**: partial→complete mediation 不能简单称为“更强”，而应标记为机制分解的规格敏感性；基准模型仅边际显著、替代模型为 null 的假设不可继续写成普遍支持；若符号反转或核心主效应消失，应升级为 substantive inconsistency，而非 qualification。

**适用**: IV/2SLS、control-function、mediation 或多 moderator 研究；替代工具、分类或测量可能改变路径形态但不必推翻全部 headline 的情境。
