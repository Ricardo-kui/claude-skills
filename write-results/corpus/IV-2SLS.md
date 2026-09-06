---
result_type: "IV-2SLS"
status: 📋 TEMPLATE
source_papers:
  - "wowak2025_tmt_political_ideology_ms"
  - "qiao_hiatt_sine2026 (SMJ, 2026): control-function residual as nonlinear DWH test + finite-sample-bias caveat"
  - "moon_tuli_mukherjee_2023_jm (Journal of Marketing): robustness exception ledger distinguishing stable, form-sensitive, and fragile inferences"
  - "Zorn_Shropshire_Martin_Combs_Ketchen_2017_SMJ (Strategic Management Journal): multi-DV parallel IV climax + selective moderation attenuation + kind-vs-degree construct battery"
variants_count: 10
created: 2026-05-18
updated: 2026-08-05
---
# IV-2SLS — Results 骨架

## 变体速查表

> 检索辅助。状态词表（与 _evidence_registry.yaml 一致）：ROBUST > VERIFIED > EMERGING（含（可选）后缀）；LEGACY-DIAGNOSTIC 保留（工具诊断类）；召回主题条目按用户 2026-08-29 裁决单源 VERIFIED。完整骨架与诚实边界见下方变体正文。

槽位分布：

| 槽位 | 变体数 | 变体编号 |
|---|---|---|
| R1 | 1 | 2 |
| R2 | 2 | 3, 4 |
| R3 | 2 | 1, 8 |
| R4 | 1 | 9 |
| R6 | 1 | 7 |
| R7 | 2 | 5, 10 |
| R8 | 1 | 6 |

### R1（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 2 | Model-Free Evidence 预览 | 正式回归前用均值分组比较建立初步直觉，降低读者对"完全依赖复杂计量技术"的疑虑（副槽位 R3） | 区别于直接进入 IV 报告——先给模型无关证据预览 | VERIFIED | Wowak 2025 MS |

### R2（2）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 3 | IV 第一阶段诊断嵌入 R3 | 因果识别研究：partial F / Sargan / Pagan-Hall / Breusch-Pagan 嵌入结果正文而非脚注（副槽位 R3） | 区别于诊断放脚注/Methods——让读者读结果时同步看到识别有效性 | VERIFIED | Wowak 2025 MS |
| 4 | 非线性估计器下 IV：控制函数残差作 DWH | 生存/Probit/Tobit 主模型的内生性检验：一阶段残差入二阶段方程作 DWH 非线性类比 + 有限样本偏误诚实提示（副槽位 R3） | 区别于线性 DWH——非线性模型下标准 DWH 无效；须加系数被放大 caveat | EMERGING | Qiao, Hiatt & Sine 2026 SMJ |

### R3（2）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 1 | 竞争假设的赢家报告模式 | 并列双可能性假设（H1a vs H1b）在 R3 同时报告两方向解释，用显著性决定"赢家" | 区别于单方向假设——"A positive… whereas a negative…"→"imply the former/latter" | VERIFIED | Wowak 2025 MS |
| 8 | 多 DV 平行 climax | 同一内生结构的多结果家族（薪酬/违规/绩效）：按假设逐 DV 平行四拍，幅度翻译按估计器匹配（%/货币/OR），诊断嵌入表注 | 区别于变体 1（竞争赢家）——多 DV 平行；因果动词按估计器分级，货币翻译锚定样本均值 | EMERGING | Zorn et al. 2017 SMJ |

### R4（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 9 | 调节衰减：mean/±1SD 条件斜率 + 跨 DV 选择性 null | IV 主效应后双外部治理调节：交互项+条件斜率+图+"marginal support"措辞，选择性 null 提升为理论边界（副槽位 R6） | 区别于 OLS-FE 单侧边际效应变体——IV 场景强制全套条件斜率；不得把 p≈.06–.08 升级为 full support | EMERGING | Zorn et al. 2017 SMJ |

### R6（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 7 | 稳健性例外账本 | 替代测量/工具族/分类下把稳健性分三层报告：stable headline / 形式敏感 / 脆弱边界（副槽位 R7） | 区别于"results remain unchanged"抹平差异——分层的证据权重更新，符号反转须升级为 substantive inconsistency | EMERGING | Moon, Tuli & Mukherjee 2023 JM |

### R7（2）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 5 | "去 IV" 稳健性（非工具变量估计示偏误低） | 移除 IV 重跑，用 IV 与非 IV 估计一致反向论证内生性偏误低（识别策略的 meta-robustness，配合 abundance of caution 叙事） | 区别于"加 IV 防御"——移除识别策略反向证明；IV 与非 IV 差异大时禁止使用 | VERIFIED | Wowak 2025 MS |
| 10 | kind-vs-degree 构念电池 | 二元"极端结构"须证明不可还原为连续梯度：dual-category 反转/连续独立性子样本/Chow 跳跃检验 | 区别于按估计器/样本/测量威胁组织的常见 R7——构念操作化威胁专用电池 | EMERGING | Zorn et al. 2017 SMJ |

### R8（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 6 | 离散度 post hoc（best of both 调和） | 主结果两对立群体各赢一个维度时，用群体内离散度（CV）作可操作干预的调和型事后分析 | 区别于 mediation post hoc（解释"为什么"）——焦点从均值转向离散度，"best of both"框架回答"该怎么办" | VERIFIED | Wowak 2025 MS |

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
**原始句锚点**: The results in column (IV) imply the former (β = 0.453; p < 0.01), such that firms with more liberal TMTs are slower to initiate recalls than firms with more conservative TMTs.
**验证状态**: VERIFIED（竞争假设设计的标准模板）
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
**原始句锚点**: Before discussing regression results, we first explore model-free support for our hypotheses. The mean number of recalls for firms with more liberal TMTs is 3.78, whereas it is 5.73 for firms with more conservative TMTs, suggesting that firms with more liberal TMTs tend to issue fewer recalls in any given year.
**验证状态**: VERIFIED
**写入日期**: 2026-05-20
**槽位**: R1/R3 (在正式回归之前)
**骨架**:
> Before discussing regression results, we first explore model-free support for our hypotheses. The mean [DV_1] for [group_A] is [value], whereas it is [value] for [group_B], suggesting that [preliminary_pattern]. By contrast, the mean [DV_2] for [group_A] is [value], but [group_B] tend to [different_pattern].
**与原骨架差异**: 在 IV/2SLS 因果识别之前先用简单均值分组比较建立初步直觉。这降低了读者对"完全依赖复杂计量技术"的疑虑。适用于任何设计——尤其是因果识别设计——但仅在 Wowak2025 中出现。

### 变体 3: IV 第一阶段诊断嵌入 R3 (1/5 复现)
**来源论文**: Wowak2025 MS
**原始句锚点**: Indeed, the partial F-statistic exceeds the thresholds that scholars suggest represent relevance (partial F-stat = 59.534; p < 0.001), and the two-step identification test from Andrews (2018) does not contain zero [-15.390, -3.943], reflecting relevant instruments (Stock et al. 2002).
**验证状态**: VERIFIED（IV 研究的最佳实践）
**写入日期**: 2026-05-20
**槽位**: R2/R3
**骨架**:
> [Our instruments conform to diagnostic tests]. The partial F-statistic exceeds the relevance threshold (partial F-stat = [value]; p < [threshold]), and the [identification_test] does not contain zero [[lower], [upper]]. Diagnostic tests for exogeneity suggest our instruments are unrelated to the structural error terms (Sargan χ² = [value]; p = [threshold]). [For Lewbel: The Pagan-Hall diagnostic fails to reject the null (p > [threshold]), and Breusch-Pagan rejects homoskedasticity (p < [threshold]), upholding both Lewbel assumptions.]
**与原骨架差异**: IV 诊断统计量（partial F, Sargan, Pagan-Hall, Breusch-Pagan）嵌入 R3 正文，而非 relegating 到脚注或 Methods 中。这是因果识别研究的最佳实践——让读者在阅读结果时同时看到识别策略的有效性。

### 变体 4: 非线性估计器下的 IV — 控制函数残差作 DWH 检验 + 有限样本偏误诚实提示 (1篇高价值)
**来源论文**: Qiao, Hiatt & Sine 2026 (SMJ)
**原始句锚点**: Further, because standard Durbin–Wu–Hausman tests rely on linear-model assumptions and are not valid for nonlinear survival models, we adopted a control-function approach in which the first-stage residual is included in the hazard equation and the examination of whether the residual is statistically significant constitutes the nonlinear analogue of a Durbin–Wu–Hausman test for endogeneity (Terza et al., 2008; Wooldridge, 2010, 2015).
**验证状态**: EMERGING（单篇高价值，生存/有限因变量模型下内生性检验的标准做法 + 罕见的诚实提示）
**写入日期**: 2026-06-16
**槽位**: R2/R3
**骨架**:
> [Table, Column] shows that the instrument, [instrument], is [direction] related to [the endogenous regressor] (β = [value], p < [threshold]), and the first-stage F-statistic of [value] exceeds the cutoff for 10% maximal bias ([cutoff]) according to Stock and Yogo ([2005]). Because standard Durbin–Wu–Hausman tests rely on linear-model assumptions and are not valid for [nonlinear survival / limited-DV] models, we adopted a control-function approach in which the first-stage residual is included in the [second-stage hazard / outcome] equation; whether this residual is statistically distinguishable from zero constitutes the nonlinear analogue of a Durbin–Wu–Hausman test for endogeneity ([Terza et al., 2008]; [Wooldridge, 2010, 2015]). The residual term is significant (β = [value], p = [threshold]), indicating that [the un-instrumented specification] is subject to the endogeneity concerns Shaver ([2005]) raised. [Next column] then shows that the instrumented [treatment] is [direction] related to [outcome] (β = [value], p < [threshold]). This method, however, is sensitive to finite-sample bias, often inflating the coefficient on the instrumented variable, and should be interpreted with caution ([citation]).
**与原骨架差异**: 解决一个被普遍回避的问题——**非线性估计器（生存/Probit/Tobit）下如何检验内生性**。标准 DWH 假设线性，不能直接用于生存模型；本变体用 **control-function**：把第一阶段残差放入第二阶段风险方程，残差显著即内生性存在的非线性等价检验（Terza et al. 2008; Wooldridge）。关键诚实提示（**不可省略**）：control-function 对有限样本敏感，常**放大**工具变量系数，故 IV 系数应解读为方向性证据而非点估计。适用于任何非线性主模型 + IV 设计（生存分析、Probit、Tobit）。配合 `../write-methods/corpus/IV-2SLS.md` 变体 4（外部自然事件 IV）使用。

[功能标签]: R4 调节效应 — 内生调节变量的 2SLS fitted-value 交互
[骨架]: "Because the [moderator] is likely endogenous to [outcome], we estimate a two-stage least squares (2SLS) regression to correct for the endogeneity of [moderator] ([citation]). ... We interact the fitted value of [moderator] with [treatment] to test whether [moderator] moderates the effect of [treatment] on [outcome] ([citation]). ... Column [II] reports that an increase in [moderator] [weakens/strengthens] the [positive/negative] [treatment] effect (β [value], p < [threshold]). On average, a one-unit (in [unit scale]) increase in [moderator] [changes] [outcome] by [X]% ([value] ÷ [base])."
[关键特征]: 调节变量内生时不直接用原始测量交互，而是第一阶段方程拟合值进入交互项（两方程编号连续呈现）；弱工具 F-stat 作为表内专行逐列报告；交互解释保持 ÷base 百分比口径；机制直觉句（'Such unfavorable comparisons boost contagion'）+ 管理启示回扣主结果（'Our previous result suggests that managers are indeed making the right decision'）
[适用]: 调节变量与结果互为因果（广告支出↔销量、投资↔绩效类）的调节设计；处理效应×策略强度交互
[节奏标记]: [内生性定位][2SLS 两阶段方程][fitted-value 交互][交互系数+显著性][÷base % 翻译][机制直觉][回扣主结果]
**原始句锚点**: "Column II reports that an increase in the substitute's total spending on advertising weakens the positive spillover effect (β −4.685, p < 0.01)."
**来源**: fang_et_al_2025_rival_recall_ad_spend (POM), §4.3

### 变体 12：R7 弱识别检验的临界值协议报告（Cragg-Donald vs Stock-Yogo 10%）（wowak2020 型）
[功能标签]: R7/R2 — IV 相关性（relevance）的临界值对照式报告
[骨架]: "A commonly used means to examine IV relevance is to report a Cragg-Donald Wald F-statistic ([citations]), which is a 'weak identification' test statistic, and compare it to the 10% critical value of Stock and Yogo (2005). The critical value we are required to use is [value], which comes from [table reference] as we have [one IV for one potentially exogenous regressor]. This means that, to have no more than 10% of the bias of the regression estimate come from our main [FE] analyses in Tables [x] and [y], our Cragg-Donald Wald F-statistic needs to be larger than [value]. The Cragg-Donald Wald F-statistic for the IV analysis is [value], which indicates that our IV is relevant and unlikely to be weak, at least from a statistical standpoint, similar to previous studies that have used this instrument ([citations])."
[关键特征]: 三拍临界值协议——先报要用的临界值及其出处与适用条件（"as we have [identification structure]"），再解释该临界值控制什么偏差（"to have no more than 10% of the bias ... come from our main analyses"），最后报实测 F 并加 "at least from a statistical standpoint" 限度语；以同工具先例研究收尾交叉校准
[适用]: 单工具/少工具 IV 的弱识别报告；须说明临界值对应的识别结构与偏差上界
[禁忌]: 只报 F 值不报临界值出处与含义；用强 F 声称识别完备（排他性不由此保证）
**原文锚定**: "The critical value we are required to use is 16.38, which comes from table 5.2 in Stock and Yogo (2005) as we have one IV for one potentially exogenous regressor. ... The Cragg-Donald Wald F-statistic for the IV analysis is 378.163, which indicates that our IV is relevant and unlikely to be weak, at least from a statistical standpoint."
**来源**: wowak_2020_female_directors_recalls (M&SOM), §5.1.1

### 变体 5: R7 "去 IV" 稳健性 — 用非工具变量估计展示内生性偏误低 (1篇高价值)
**来源论文**: Wowak2025 MS
**原始句锚点**: Although we employed IVs that met the relevance and exclusion criteria in our main analysis, the consistency of our results from the noninstrumented approach indicates that bias from endogeneity may be relatively low in our setting.
**验证状态**: VERIFIED（单篇高价值；corpus 此前无"移除识别策略以反向论证偏误低"的元稳健性变体）
**写入日期**: 2026-07-25
**槽位**: R7
**骨架**:
> We next repeat our analyses without instrumental variables. [Table], columns [X] and [Y] suggest that [IV] is [negatively] related to [DV_1] (β = [value]; p < [threshold]) and [positively] associated with [DV_2] (β = [value]; p < [threshold]). Although we employed IVs that met the relevance and exclusion criteria in our main analysis, the consistency of our results from the noninstrumented approach indicates that bias from endogeneity may be relatively low in our setting.
**与原骨架差异**: 与"加 IV 防御内生性"的标准逻辑相反——本稳健性**移除 IV**重跑，用"非工具变量估计与工具变量估计一致"反向论证内生性偏误不大。这是对识别策略本身的**元稳健性**（meta-robustness about the identification strategy），完成两个说服动作：(1) 验证 IV 不是在扭曲估计（IV 与非 IV 系数一致 → IV 未引入偏误）；(2) 安抚读者即使没有重型识别机器，核心结论也成立。与变体 3（IV 诊断嵌入 R3）互补——变体 3 证明 IV *有效*，本变体证明 IV *非必需但仍用*（abundance of caution 的实证呼应，见 write-methods IV-2SLS 变体 9）。
**适用**: IV/2SLS 主分析研究中，IV 估计与非 IV 估计方向/显著性可比时；展示方法选择（是否用 IV）不影响核心结论。配合 write-methods IV-2SLS 变体 9（"abundance of caution" 叙事）形成完整的 IV 防御闭环。
**禁忌**: 若 IV 与非 IV 估计差异大，本稳健性会**暴露问题**——此时必须解释差异（如内生性真实存在 → IV 估计才是可信的），不能声称"偏误低"；本变性**不能**用作 IV 诊断缺失的借口——仍须报告完整 IV 诊断（变体 3）；"relatively low" 是谨慎措辞，不可升级为 "no endogeneity"。

### 变体 6: R8 离散度 post hoc — "best of both" 调和型事后分析 (1篇高价值)
**来源论文**: Wowak2025 MS
**原始句锚点**: A logical conclusion from our research is that firms may seek to diversify their TMTs politically in the hopes of having both fewer recalls and faster ones.
**验证状态**: VERIFIED（单篇高价值；corpus 此前无"焦点构念从均值转向离散度、并框架为调和两极张力"的 post hoc 变体）
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
**原始句锚点**: Considering Models 10a–10c, we find that analyst uncertainty completely mediates the effect of disclosure of advertising spending on idiosyncratic risk.
**验证状态**: EMERGING（单篇高价值 reference-level 变体）
**写入日期**: 2026-08-03
**槽位**: R6/R7
**骨架**:
> We assess the sensitivity of our conclusions to [alternative measurement], [alternative instrument families], [alternative classification], and [additional omitted-information control]. The headline conclusions for [core hypotheses] remain consistent. Two qualifications are important. First, the mediation inference changes from [partial] to [complete/stronger] because [the direct path becomes weaker/nonsignificant] under [specification]. Second, the evidence for [weakly supported moderator] becomes nonsignificant under [alternative specification]. We therefore treat [headline effect] as robust, the exact form of [mediation] as specification-sensitive, and [moderator hypothesis] as weaker evidence.

**与原骨架差异**: 常见 R7 用 “results remain unchanged” 抹平所有规格差异；本变体把稳健性结论分成三层：(1) 方向与显著性稳定的 headline；(2) 结论仍成立但**形式改变**的机制（partial ↔ complete mediation）；(3) 在合理替代规格下消失的脆弱边界。稳健性段因此既维护核心发现，也更新证据权重。

**诚实边界**: partial→complete mediation 不能简单称为“更强”，而应标记为机制分解的规格敏感性；基准模型仅边际显著、替代模型为 null 的假设不可继续写成普遍支持；若符号反转或核心主效应消失，应升级为 substantive inconsistency，而非 qualification。

**适用**: IV/2SLS、control-function、mediation 或多 moderator 研究；替代工具、分类或测量可能改变路径形态但不必推翻全部 headline 的情境。

### 变体 8: R3 多 DV 平行 climax — 同 IV、设计匹配幅度翻译（% / 货币 / OR）(EMERGING)

**来源论文**: Zorn, Shropshire, Martin, Combs & Ketchen (2017, SMJ)
**原始句锚点**: Lone-insider CEOs received roughly 82% greater pay than their non-lone-insider peers. Practically speaking, given the mean value of total pay in our sample of $5.7 million, results suggest that lone-insider CEOs receive $4.7 million in excess pay.
**验证状态**: EMERGING（单篇）
**写入日期**: 2026-08-05
**槽位**: R3
**骨架**:
> Table [X] presents the main effects of [endogenous structure] on [DV_family_1], [DV_family_2], and [DV_family_3] (Hypotheses [H_set]). Hypothesis [Ha] predicted that [structure] would [increase/decrease] [DV_a]. Results in Model [1] support Hypothesis [Ha] (b = [value], p = [exact_p]). [Instrumented continuous translation:] [Units] with [structure] [received / exhibited] roughly [percentage] [greater/lower] [DV_a] than peers; given mean [pay/level] of [currency_mean], this implies about [currency_delta] in [excess/gap]. Hypothesis [Hb] predicted a larger [gap_DV]; Model [2] supports this claim (b = [value], p = [exact_p]), a [currency_delta] larger gap relative to the sample mean gap of [currency_mean]. [Optional mechanism check:] We find no relationship between [structure] and [component_DV], suggesting the gap arises from higher [focal actor] [pay] rather than lower [peer group] [pay]. Hypothesis [H_binary] predicted greater [rare event] likelihood. Model [3] supports Hypothesis [H_binary] (b = [value], p = [exact_p]); the odds ratio implies [structure] [units] are [OR] times as likely to experience [rare event]. Hypothesis [H_perf] anticipated weaker [performance]. Models [4]–[5] support Hypothesis [H_perf] ([perf_1]: b = [value], p = [exact_p]; [perf_2]: b = [value], p = [exact_p]). In practical terms, [perf_1] is roughly [percentage] lower for [structure] [units], corresponding to about [currency_delta] less [net income] at the sample mean. [First-stage diagnostics appear in the table notes / text: first-stage F = [values]; Hansen J = [values], failing to reject exogeneity.]

**与原骨架差异**: 变体 1 是竞争假设赢家报告；变体 4 是非线性 IV；本变体是**同一内生结构、多结果家族的平行四拍**，且幅度翻译按估计器匹配（2SLS 连续 → %/货币；Logit → OR；绩效 → % + 绝对美元）。诚实边界：稀有二元主分析若非 IV，因果动词须弱于 instrumented 连续结果；不可把所有 DV 写成同等 “effect of”；货币翻译须锚定样本均值并标明假设（“given mean…”）。

**适用**: 治理/组织设计同时影响薪酬、违规与绩效等多结果的 IV/2SLS 面板。

**节奏标记**: [假设提醒][系数+精确p][设计匹配幅度][支持判断] × N 个 DV；诊断嵌入表注。

### 变体 9: R4/R6 调节衰减 — 交互项 → mean/±1SD 条件斜率 → 边际支持诚实 → 跨 DV 选择性 null (EMERGING)

**来源论文**: Zorn, Shropshire, Martin, Combs & Ketchen (2017, SMJ)
**原始句锚点**: Next, we examine whether the conditional effect of lone-insider boards is different from zero depending on the amount of analyst coverage. The slope of the relationship between lone-insider boards and excess pay at the mean value of analyst coverage (approximately 12 analysts) is marginal (b = 5.59, p =.08).
**验证状态**: EMERGING（单篇）
**写入日期**: 2026-08-05
**槽位**: R4 / R6
**骨架**:
> Table [Y] reports moderation by [external monitor_1] and [external monitor_2] (Hypotheses [H4–H5]). We discuss each interaction and then whether the conditional effect of [structure] differs from zero at different levels of the moderator ([citation for conditional-effects protocol]). Hypothesis [H4a-i] predicted that [monitor_1] attenuates the positive association between [structure] and [DV_a]. The interaction in Model [1] is [direction] (b = [value], p = [exact_p]). The slope of [structure] at the mean of [monitor_1] ([mean_level]) is [marginal/significant] (b = [value], p = [exact_p]). As shown in Figure [1], the slope at −1 SD ([low_level]) is [b, p] and at +1 SD ([high_level]) is [b, p]. Overall, Hypothesis [H4a-i] received [marginal / full] support. Hypothesis [H4a-ii] predicted attenuation for [gap_DV]; this hypothesis was not supported (b = [value], p = [exact_p]). Hypothesis [H4b] for [rare_DV] was not supported (b = [value], p = [exact_p]). Hypothesis [H4c] for [performance] is supported: the interaction predicts [perf_1] (b = [value], p = [exact_p]) and [perf_2] (b = [value], p = [exact_p]); conditional slopes at the mean and at ±1 SD remain [meaningful/marginal] and are plotted in Figure [2]. [Repeat parallel block for monitor_2.] To summarize, [structure] harms [DV_set_supported], but negative effects on [attenuated_DVs] are reduced when [external monitors] are stronger; we do not find attenuation for [null_DVs], suggesting external actors may be selective in where they exert pressure—or that pressure is not always effective.

**与原骨架差异**: OLS-FE 变体 9 给单侧边际效应；变体 11 给边际显著 90% CI；Moon 变体 7 是稳健性例外账本。本变体专用于 **IV 主效应之后的双外部治理调节**：强制 (1) 交互项；(2) mean/±1SD 条件斜率；(3) 图；(4) 「marginal support」诚实措辞（不得把 p≈.06–.08 升级为 full support）；(5) 跨 DV **选择性 null** 提升为理论边界而非遗漏。诚实边界：条件斜率在调节模型中系数尺度可能膨胀——须同时报告交互显著性与条件斜率，不可只挑显著端；null 调节不可事后改写成“支持部分路径”而不改假设判定。

**适用**: 内部治理弱点 × 外部监督（分析师、机构投资者、媒体、审计）衰减假说；多 DV 时预期衰减并非均匀。

**节奏标记**: [交互][条件斜率 mean][±1SD+图][marginal/full/not supported][跨DV选择性收束]

### 变体 10: R7 kind-vs-degree 构念电池 — dual-category 反转 / 连续独立性子样本 / Chow 跳跃检验 (EMERGING)

**来源论文**: Zorn, Shropshire, Martin, Combs & Ketchen (2017, SMJ)
**原始句锚点**: Taken together, these results support our theorizing that having at least one non-CEO insider represents a change in kind rather than degree.
**验证状态**: EMERGING（单篇）
**写入日期**: 2026-08-05
**槽位**: R7
**骨架**:
> We theorized that [focal structure] is categorically different from other [board/organizational] types—a change in kind rather than degree. Accordingly, we verify that results are not simply a linear relationship in which each additional [insider / continuous unit] improves outcomes by similar amounts. First, the practical range of [count variable] is narrow: only [pct_3]% have [three], [pct_4]% have [four], and fewer than [pct_5]% have [five or more], so little information is lost by dichotomizing beyond [focal category]. Second, a quadratic in [count] yields no curvilinear effects, consistent with categorical uniqueness. Third, replacing [focal indicator] with [adjacent category: e.g., dual-insider boards] produces a distinct pattern: [adjacent category] is [not positively related / negatively related] to [DV_a] (b = [value], p = [exact_p]), [direction] for [gap_DV] (b = [value], p = [exact_p]), [reversed] for [rare_DV] (b = [value], p = [exact_p]), and [null/weak] for [performance]—across outcomes, having at least one [non-focal insider] appears beneficial relative to [focal structure]. Fourth, in the subsample of non-[focal-structure] [units], a continuous measure of [independence / insider count] becomes insignificant for [DV_a], [gap_DV], and [rare_DV], though not for [performance]; Chow tests show that moving from [one] to [two] [insiders] has significantly larger effects than moving from [two] to [three or more] (F = [value_1] and [value_2] for [perf_1] and [perf_2]). Taken together, these results support treating [focal structure] as an empirically unique phenomenon rather than a point on a linear [independence] gradient.

**与原骨架差异**: 常见 R7 按估计器/样本/测量威胁组织；本变体是**构念操作化威胁**专用电池——证明二元「极端结构」不可还原为 continuous majority-independence / count。诚实边界：dual-category 模型须报告自身 first-stage 诊断（不可借用主模型 F）；Chow / 子样本检验是构念辩护而非主假设的额外支持；若连续测量在非焦点子样本仍显著且无跳跃，应削弱 kind 主张。

**适用**: Methods 已声明 kind ≠ degree 的离散治理/组织结构研究（见 write-methods 面板数据-OLS 变体 32）。

### 变体 11：R7 排他性约束的量化暴露占比辩护（wowak2020 型）
[功能标签]: R7 稳健性 — IV 排他性约束的三层辩护（先例复用→机制反驳→量化暴露占比）
[骨架]: "Although the exclusion criteria cannot be explicitly tested, we propose that [instrument] is unlikely to be directly correlated with our dependent variables. First, [instrument] has been used in prior [predictor] studies that predict similar dependent variables ([citations]). Second, a direct correlation between [instrument] and [outcome] is less likely due to the characteristics of the [source channels] that [generate the instrument]. More specifically, the argument for nonexclusivity would be that [channel mechanism] not only influences [first-stage channel], but also influences how [actors] set [decision tone] and thereby predicts our [outcome] measures. Although we cannot completely rule out this possibility, we believe the risk of this is low based upon the small percentage of [source channels] that are [outcome-relevant domain]. In particular, there are [N_total] [source channels] across the time period of our panel. Of those, only [N_exposed] are [outcome-relevant entities], which is only [share]% of them. In other words, well over [100−share]% of the [source channels] are from [unrelated domains] in which [outcome] decisions as examined in our study are very uncommon."
[关键特征]: 排他性不可检验时先用先例复用（prior studies）与机制反驳（命名非排他性通路再逐项拆解），最后落到可数的暴露占比（"only [N] are [relevant], which is only [share]%"）把辩护从口头转为算术；"Although we cannot completely rule out this possibility" 保留诚实让步再压低风险
[适用]: 工具变量经第三方网络/渠道生成的排他性辩护；有可数暴露面（外部关联实体行业构成）的 IV 设计
[禁忌]: 暴露占比仅当可从数据直接清点时使用；不得把占比辩护写成排他性已被检验
**原文锚定**: "Of those, only 50 are medical products firms, which is only 8.6% of them. In other words, well over 90% of the 'other boards' are from nonmedical product industries in which recall decisions as examined in our study are very uncommon."
**来源**: wowak_2020_female_directors_recalls (M&SOM), §5.1.1

[功能标签]: R7 稳健性 — 排他性约束的理论论证 + 安慰剂回归双重辩护
[骨架]: "The instrumental variable (IV) must meet the relevance criterion and exclusion restriction ([citations]). That is, the instrument should correlate with [endogenous variable] but should not directly influence [outcome]. ... [理论论证两段：机制 A 降低接入成本/强化竞争 → 支出↑；机制 B 排他与本地经济状况的直接关联，引城市文化—经济二分文献]. Empirically, we provide evidence showing that our instrument is not directly related to [proxy for local economic conditions], which could affect [outcome]. ... The insignificant effect suggests that our IV variable likely meets the exclusion restriction ([citations])."
[关键特征]: 与变体 11 的量化暴露占比辩护不同，本变体在理论论证之外**追加一张安慰剂回归表**：工具变量对'本地经济代理变量'（全部新注册企业数）回归，以不显著作为排他性的经验证据；辩护结构为 relevance 预期方向声明 → 排他性理论论证 → 排他性安慰剂检验三层递进
[适用]: 工具为地方供给面变量（新企业进入、设施密度）而结果为需求面结果的设计；审稿人质疑排他性时
[节奏标记]: [IV 双准则声明][相关性理论论证][排他性理论论证][排他性安慰剂回归][不显著即合格]
**原始句锚点**: "The insignificant effect suggests that our IV variable likely meets the exclusion restriction (Liu et al., 2017; Narang and Shankar, 2019)."
**来源**: fang_et_al_2025_rival_recall_ad_spend (POM), §4.3

### 变体 13：R7 非线性主模型下的线性 2SLS 稳健性轨（wowak2020 型）
[功能标签]: R7 稳健性 — 非线性主估计器（负二项 FE）+ 线性 2SLS 内生性检验轨的适配性辩护
[骨架]: "Although Equation ([main]), which is used to examine support for Hypothesis [N], is a nonlinear [count model] regression, we use linear 2SLS for our IV analysis. We do so because nonlinear IV modeling approaches are nonstandardized and there is significantly less consistency in how to implement such models ([citation]) compared with linear 2SLS analyses. However, the linear 2SLS analysis leads to highly consistent results for both our [DV1] and [DV2] analyses, as described below. ... In column (1) of Table [z], we report how our control variables and [instrument] predict [endogenous predictor]. [Instrument] is highly predictive of [endogenous predictor], as shown not only by the significant coefficient for [instrument] (β = [value], p < [threshold]) predicting [endogenous predictor], but also due to the large [weak-id statistic] in column (1). In each of the next [six] columns of Table [z], we use the instrumented [endogenous predictor] in the second stage of the 2SLS regression as a predictor variable in our [DV1] and [DV2] analyses. We find nearly identical results when comparing columns [c2]–[c7] of Table [z] with columns [c3]–[c5] of Table [x] and columns [c3]–[c4] of Table [y]. ... The results in Table [z] indicate that [time-variant omitted variable bias] is unlikely creating significant endogeneity problems in our analysis."
[关键特征]: 主模型非线性而 IV 轨线性的适配性辩护（"nonlinear IV ... nonstandardized ... less consistency"，引 Wooldridge 2010）；第一阶段与第二阶段列布局共享一张表；跨表精确映射（"comparing columns ... of Table [z] with columns ... of Tables [x] and [y]"）替代含糊的 "results robust"；收束句把 threat（time-variant omitted variables）显式点名
[适用]: 计数/非线性主模型 + 线性 2SLS 内生性稳健性的组合；双 DV 主结果表的 IV 复制
[禁忌]: 不得把线性 2SLS 系数与非线性主系数直接比大小；线性化须给方法论引证而非默认
**原文锚定**: "Although Equation (1), which is used to examine support for Hypothesis 1, is a nonlinear negative binomial regression, we use linear 2SLS for our IV analysis. We do so because nonlinear IV modeling approaches are nonstandardized and there is significantly less consistency in how to implement such models (Wooldridge 2010) compared with linear 2SLS analyses."
**来源**: wowak_2020_female_directors_recalls (M&SOM), §5.1.1

[功能标签]: R7 稳健性 — 控制变量内生性的三步递进辩护
[骨架]: "One may be concerned that our control variables (e.g., [control]) are endogenous. We address this concern with the following three steps. First, we estimate a regression that excludes [controls]. The estimates (Table [C1]) are consistent with our main analyses (Table [X]). Second, prior literature ([citation]) has suggested that it is common for control variables to also function as dependent variables. ... the inclusion of additional variables produces estimates that are lower than or equal to the estimates produced after their inclusion. The insight is that including the controls leads to conservative estimates. Third, following prior literature ([citations]), we used these controls' one-period-lagged values as instruments. The estimates (Table [C2]) were consistent with the results, further reducing the endogenous concern."
[关键特征]: 针对 'bad controls' 质疑的三步梯度：(1) 剔除可疑控制的复制；(2) Cinelli 式保守性论证——含控制估计 ≤ 不含控制估计，故结论方向不受威胁；(3) 滞后一期值作工具的复制；每步各有独立表格指针且收束句强度递增（consistent → conservative → further reducing）
[适用]: 控制变量与 DV 同源或同期决定（媒体支出、研发、人力资本类）的面板设计；审稿人质疑 bad controls 时
[节奏标记]: [威胁定位][第一步剔除复制][第二步保守性论证][第三步滞后 IV 复制][递进收束]
**原始句锚点**: "One may be concerned that our control variables (e.g., Internet Ad) are endogenous. We address this concern with the following three steps."
**来源**: fang_et_al_2025_rival_recall_ad_spend (POM), §4.2



<!--
pattern_id: switching_reg_selection_diagnostics_null_hazard_positive_hausman
estimator_family: switching regression / endogenous switching（选择修正诊断收束）
slot: R7（自选择修正诊断，收尾型）
source_papers: ["gulati2005-adaptation-vertical"]
confidence: VERIFIED — expert_audit_override（user 2026-09-06：Pollock/Westphal/Gulati 系单源即 VERIFIED）
-->



### 变体 16：恰好识别系统下的工具双条件散文审计 + 不可检验项诚实边界（gulati_sytch2007 型）

**适用场景**: 联立方程/IV 系统**恰好识别**（工具数 = 内生变量数）时的工具有效性报告。此时无自由度做 Cragg-Donald 弱识别统计量之外的过度识别检验（Sargan/Hansen），也无多余工具做排他性安慰剂回归——工具辩护只能走"相关性已验证 + 排他性理论预设+经验核查"的散文审计路线。

**报告节奏**: [双工具引入+各自相关性机制预期] → [排他性预设：无 a priori 理由存在直接效应] → [相关性条件核验：跨全部模型规格保持显著→系统始终可识别] → [排他性条件核验：对非对应内生变量无直接效应（已验证）] → [诚实边界：恰好识别故过度识别检验不可行]

**骨架**:
```
We used [two] instrumental variables to help uniquely identify the [outcome] and
[predictor] models in the system of simultaneous equations. For the [predictor] model,
we used [instrument_1]. We expected levels of [instrument_1] to lead to higher degrees
of [predictor] due to [mechanism]. To uniquely identify the [outcome] equation, we
[created/used] [instrument_2]. We expected [instrument_2] to be [positively] correlated
with [outcome]. We had no a priori theoretical reasons to expect [instrument_1] to have
a direct effect on [outcome] and [instrument_2] to have a direct effect on [predictor].

It is essential to note that both of our instruments ([instrument_1] and [instrument_2])
remain significant across all model specifications, which is a first essential
requirement of instrumental variables and ensures that our system of equations remains
identified at all times. We further empirically verified that our instruments met the
second condition of instrumental variables and had no partial direct effect on their
non-respective endogenous variables: thus, controlling for other variables in the
system, [instrument_2] had no direct effect on [predictor], and [instrument_1] had no
direct effect on [outcome] ([citation]).

Because our system is just identified (we have equal numbers of endogenous variables
and instruments), we could not formally check for the absence of correlation between
the instrumental variables and the structural errors by testing for overidentifying
restrictions ([citation]).
```

**为什么有效**: 在统计量最少的识别设定下，把工具辩护拆成两条可核查的命题（跨规格相关性 / 无非对应直接效应）并各自给出验证动作，使"工具有效"从断言变成审计记录；结尾的不可检验声明把"恰好识别"从技术细节升格为诚实边界，堵住"为何没有 Sargan/Hansen"的审稿疑问。

**与已有变体的分工**: 变体11（量化暴露占比辩护，VERIFIED）与 Fang 2025 双重辩护变体面向**过度识别/有暴露面**的工具；变体12（Cragg-Donald vs Stock-Yogo 临界值协议，VERIFIED）依赖可报的弱识别统计量。本变体覆盖的是它们都无法服务的**恰好识别**设定：无过度识别自由度、排他性只能靠理论预设+经验核查。三者按识别结构互补而非替换。

**注意事项**: "remain significant across all model specifications" 只在工具于每个规格中都报告时才可写；"no partial direct effect" 必须是实际估计核查的结论而非纯断言（本文引 Wooldridge [year: page] 支撑该核查逻辑）；诚实边界句不可删——它是整套散文审计的合法性来源。

**反模式**: 恰好识别时假装排他性"已被检验"；只报相关性不提排他性；用过度识别检验话术包装恰好识别系统。

**验证状态**: VERIFIED — expert_audit_override（user 2026-09-06：Pollock/Westphal/Gulati 系单源即 VERIFIED）

**原文锚定**: "Because our system is just identified (we have equal numbers of endogenous variables and instruments), we could not formally check for the absence of correlation between the instrumental variables and the structural errors by testing for overidentifying restrictions (Hausman, 1978)."

**范文来源**: Gulati & Sytch (2007), *Administrative Science Quarterly* 52(1) — Results 节工具有效性两段。

<!-- wb:gulati_2007_dependence_asymmetry_and_joint_dependence_in_int:r2_instrument_dual_condition_audit_just_identified_boundary -->

<!-- wb:gulati_2007_dependence_asymmetry_and_joint_dependence_in_int:r2_instrument_dual_condition_audit_just_identified_boundary_gulati_sytch2007 -->

### 变体 15：互为因果双内生系统的 3SLS 主估计导航（gulati_sytch2007 型）

**适用场景**: 理论上两个核心构念互为因果（X→Y 且 Y→X 均成立）的截面/关系数据设计。区别于单向内生修正（工具变量只救一个内生回归元）——此处 [predictor] 与 [outcome] 同时内生，必须以联立方程系统为主估计器，而非作为稳健性附录。

**报告节奏**: [反向因果让步开框（先替对手把话说了）] → [联立性偏误命名] → [Hausman 预检实证确认] → [OLS 不适用论证] → [3SLS 系统陈述+估计三步程序] → [系统表导航（每表=两方程成对）+ OLS 基线例外]

**骨架**:
```
Yet it is also plausible to argue that [outcome] will lead [partners] to allocate more
[business] to each other, hence increasing levels of [predictor]. This potential
reciprocally causal relationship resulted in a simultaneous-equation bias in our
research design ([citation]). In line with the expectations of a simultaneous-equation
bias, the [Hausman (year)] test did indicate the presence of endogeneity in the
[predictor] measure (p = [value]). A simple ordinary least squares (OLS) estimator is
inapplicable for a simultaneity bias because the endogenous variables are correlated
with the disturbance term, hence rendering OLS estimates inconsistent. To account for
the possible simultaneity between [predictor] and [outcome], we used a [three-stage
least squares] variation of simultaneous equation modeling ([citation]), which allowed
us to estimate [outcome] simultaneously as a function of [predictor] and [predictor]
as a function of [outcome].

[系统表导航段] The table reports systems of equations, where each system comprises two
equations or models that are estimated simultaneously: the first one reflects [outcome]
as a function of [predictor] and various exogenous predictors, and the second one
estimates [predictor] as a function of [outcome] along with the set of exogenous
variables. Model [1] in table [X] represents an exception, since we used a simple OLS
model with robust standard errors to test the baseline [outcome] model. The
simultaneity bias is not an issue here because the measure of [predictor] is excluded
from the model.
```

**为什么有效**: 让步式开框把审稿人最可能的反向因果攻击变成作者自己的铺垫；随后每个动作（Hausman→弃 OLS→3SLS）都有明确的触发理由，读者无需自行补全识别逻辑。系统表导航句让双方程成对呈现的表格变得可读，OLS 基线例外句预先堵住"为什么第一列不是 3SLS"的疑问。

**与已有变体的分工**: 变体3（IV 第一阶段诊断嵌入 R3，VERIFIED）与变体4（非线性主模型控制函数 DWH，EMERGING）均为**单向**内生修正——一个内生回归元、工具只为其服务；本变体的最小识别单元是**双内生方程组**，表格导航与基线例外句均系统级。互为因果设计优先本变体，再按需叠加变体3的诊断嵌入。

**注意事项**: Hausman 预检 p 值须如实报告（本文 p = .078 为边缘显著，仍构成使用 3SLS 的依据——边缘性本身就是诚实信息）；反向因果让步段不可省略，它是系统级估计器（而非常规 IV）的正当性来源；估计三步程序（工具化→跨方程协方差→SUR 堆叠）可引 Greene ([year]: [page]) 而非全文复述。

**反模式**: 把 3SLS 藏进稳健性小节而主表仍用 OLS（联立性偏误未被控制却宣称因果）；系统表只导航性能方程不提对应方程；省略基线例外句导致读者误读 Model 1。

**验证状态**: VERIFIED — expert_audit_override（user 2026-09-06：Pollock/Westphal/Gulati 系单源即 VERIFIED）

**原文锚定**: "The table reports systems of equations, where each system comprises two equations or models that are estimated simultaneously: the first one reflects performance as a function of joint dependence ... and the second one estimates joint dependence as a function of performance along with the set of exogenous variables."

**范文来源**: Gulati & Sytch (2007), *Administrative Science Quarterly* 52(1) — Analysis 节 + Results Table 8 导航段。

<!-- wb:gulati_2007_dependence_asymmetry_and_joint_dependence_in_int:r2_reciprocal_3sls_system_navigation -->

<!-- wb:gulati_2007_dependence_asymmetry_and_joint_dependence_in_int:r2_reciprocal_3sls_system_navigation_gulati_sytch2007 -->

### 变体 14：选择修正项不显著 + Hausman 显著的双信号诚实收束（Null Correction Term with Significant Hausman）

**适用场景**: 选择修正/自选择担忧的收尾诊断。修正项（non-selection hazard）自身不显著——敏锐的读者会据此推断"无需修正"；但设定检验（Hausman 对比含/不含修正项的两组估计）显著。两信号并存时的报告节奏：既承认修正项 null，又不放弃选择存在性结论，同时对量化精度保持谦逊。

**报告节奏**: [修正项 null 陈述] → [转折：Hausman 显著] → [存在性结论（已被控制）] → [精度谦逊 + 文献旁证]

**骨架**:
```
[修正项 null 陈述] Finally, we note that the [correction term] is not significant in our
models.
[转折] However, a [Hausman] specification test indicates that the coefficients in the models
change significantly on the inclusion of the [correction term].
[存在性结论] This suggests that effects due to [self-selection] of [treatment category] are
operating in our data (and we have controlled for them),
[精度谦逊] though we may have been unable to quantify them precisely (see also [citation], for
similar findings in the context of [domain]).
```

**为什么有效**: 这是自选择诊断最容易被写坏的地方——修正项不显著要么被藏起来，要么被用来宣称"没有自选择问题"。本文同时呈现两个信号并给出分层的结论（存在且受控，但不可精确量化），把"不能证明没有"与"不能精确度量"分开，是审稿人视角下最稳健的表述。

**注意事项**: Hausman 显著性的方向解释必须与修正项 null 并置（否则读者只取其一）；"unable to quantify precisely"的谦逊句不可省略，它是两个信号并存时结论的合法性来源；文献旁证（如 Shaver 1998 同类发现）用于表明该信号组合在领域内已有先例。

**反模式**: 修正项不显著即删去或宣称无选择问题（忽略 Hausman）；或只报 Hausman 显著不报修正项 null（选择证据被夸大）；把"已控制自选择"写成"已消除自选择"。

**原文锚点**: "This suggests that effects due to self-selection of procurement modes are operating in our data (and we have controlled for them), though we may have been unable to quantify them precisely (see also Shaver, 1998, for similar findings in the context of international expansion)."

**范文来源**: Gulati, Lawrence & Puranam (2005), *Strategic Management Journal* — RESULTS 收尾段（控制变量与自选择诊断）。

<!-- wb:gulati2005-adaptation-vertical:switching_reg_selection_diagnostics_null_hazard_positive_hausman -->


### 变体 17：3SLS 无稳健 SE 时的按簇 bootstrap 推断替代（gulati_sytch2007 型）

**适用场景**: 主估计器为 3SLS/联立方程且软件不提供直接的异方差稳健/聚类 SE 调整，同时数据存在簇结构（同一供应商/企业多条关系）与异方差（Breusch-Pagan 拒绝同方差）。推断基础设施缺口必须以重抽样方法补齐时。

**报告节奏**: [威胁定位：BP 检验拒绝同方差] → [成因诊断：观测非独立/簇结构] → [约束声明：3SLS 无直接 SE 调整] → [替代动作：非参数 bootstrap（偏差修正系数+SE）] → [簇感知设计：重抽样本规模=簇数] → [重复次数+不变结论]

**骨架**:
```
The [Breusch-Pagan] test ([citation]) for heteroskedasticity led us to reject the null
hypothesis of homoskedastic error variance ... One possible reason for this may be the
non-independence of observations, as certain [clusters] in our sample [supply more than
one unit] ... Similar to OLS, heteroskedasticity poses a problem in [3SLS] estimation
because it can bias the standard errors of the estimated coefficients. Because the
direct adjustment of standard errors is not available in [3SLS] [software] estimation,
we used a nonparametric bootstrap method to extract the bias-corrected coefficient
estimates and standard errors ([citations]). ... In implementing the bootstrap, we made
provisions for the clustered structure of our data, subsequently setting the size of
repeated random samples equal to the number of clusters. ... Our estimates are based on
[1,000] random samples ([citation]). Results remained qualitatively unchanged.
```

**为什么有效**: 威胁（异方差）与成因（簇结构）分开诊断，使推断补救显得有的放矢而非仪式性；"direct adjustment ... not available" 的约束声明把 bootstrap 从偏好升级为必需；簇感知重抽细节（样本规模=簇数）让懂行的审稿人确认重抽单位正确；结论句只声称 qualitatively unchanged，不夸大为完全相同。

**与已有变体的分工**: 目标文件 R7 现有变体均为识别/排他性辩护（变体5/10/11/12/13/14），无推断基础设施变体；registry 计数模型 R7 bootstrap_se（ball_2018）面向 generated regressor 的 SE 低效，本变体面向**估计器能力约束**（3SLS 无聚类稳健 SE 可调）——触发条件、实现细节（按簇等规模重抽）与措辞均不同。IV/联立方程族用本变体补推断层。

**注意事项**: "bias-corrected" 须与所用 bootstrap 修偏程序一致；簇感知重抽（cluster bootstrap）与逐观测重抽不可混写；重复次数须报（本文 1,000）；结论强度限定在 qualitatively unchanged——若系数幅度有明显移动须如实说明。

**反模式**: 3SLS 下直接照搬 OLS 的 cluster-robust SE 话术（该选项并不存在）；省略簇感知重抽细节使读者无法判断推断单位；把 bootstrap 结果写成 identical。

**验证状态**: VERIFIED — expert_audit_override（user 2026-09-06：Pollock/Westphal/Gulati 系单源即 VERIFIED）

**原文锚定**: "Because the direct adjustment of standard errors is not available in 3SLS Stata estimation, we used a nonparametric bootstrap method to extract the bias-corrected coefficient estimates and standard errors (Efron, 1981, 1982)."

**范文来源**: Gulati & Sytch (2007), *Administrative Science Quarterly* 52(1) — Results 节推断基础设施段。

<!-- wb:gulati_2007_dependence_asymmetry_and_joint_dependence_in_int:r7_3sls_cluster_bootstrap_inference_workaround -->

<!-- wb:gulati_2007_dependence_asymmetry_and_joint_dependence_in_int:r7_3sls_cluster_bootstrap_inference_workaround_gulati_sytch2007 -->
