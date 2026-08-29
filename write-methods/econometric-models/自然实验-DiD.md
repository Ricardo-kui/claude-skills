---
design_type: "自然实验-DiD"
status: EMERGING
source_papers:
  - lee_wu_bednar_orsc_18968 (Organization Science; DOI 10.1287/orsc.2024.18968)
  - hoffmann_cheong_phan_zurbruegg2024_jm (Journal of Marketing; staggered UD-law DiD + conditional logit + binary recall)
  - Castellaneta_Conti_Kacperczyk_2017_SMJ (SMJ; staggered UTSA + PE buyout IRR ≈ DiD first difference)
  - moon_2026_the_impact_of_legal_protection_of_trade_secrets_on (Journal of Marketing)
variants_count: 15
created: 2026-05-18
updated: 2026-08-23
---
# 自然实验-DiD — Methods 骨架

## 变体速查表

> 检索辅助。状态词表（与 _evidence_registry.yaml 一致）：ROBUST > VERIFIED > EMERGING（含（可选）后缀）；LEGACY-DIAGNOSTIC 保留（工具诊断类）；召回主题条目按用户 2026-08-29 裁决单源 VERIFIED。完整骨架与诚实边界见下方变体正文。

### 槽位分布

| 槽位 | 变体数 | 变体编号 |
|---|---|---|
| M8 | 5 | 3、4、12、13、14 |
| M7 | 3 | 2、5、6 |
| M2 | 3 | 1、7、15 |
| M1 | 1 | 8 |
| M3 | 1 | 10 |
| M4 | 1 | 9 |
| M6 | 1 | 11 |

### M8（5）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 3 | 错位 DiD 三层诊断栈 + 现代估计诚实边界 | 错位实施 DiD 的可信度检查（按威胁组织） | 与变体 4 的界限：诊断（pretrend/置换/分解）vs 修复（异质性稳健估计） | EMERGING | Lee, Wu & Bednar (OS) |
| 4 | staggered DiD 识别栈（model-free → 机制 → pretrend → 安慰剂） | Marketing 准实验 staggered 采纳研究 | 区别于变体 3：加 model-free 证据 + 文献 manipulation check 四段式 | VERIFIED | Hoffmann et al. 2024 (JM) |
| 12 | 政治经济外生性电池（质性检索 + LPM/hazard + 供需零相关） | 政策采纳时点可能随政治经济条件内生 | 区别于变体 4：专攻"政治经济内生采纳"威胁 | EMERGING | Castellaneta et al. 2017 (SMJ) |
| 13 | 日历安慰剂 ±k 年（假处理弱于真处理） | 持有窗截面、难画标准 event-study 的设计 | 区别于变体 3/4（置换/重分配安慰剂）：固定错位 ±k 年 | EMERGING | Castellaneta et al. 2017 (SMJ) |
| 14 | 司法/监管冲击双假设外生性（awareness + 单位无影响） | 法院裁决/监管事件作外生冲击 | 区别于变体 12 政治经济电池：双前提叙事（awareness + 不受单位影响） | EMERGING | Moon et al. 2026 (JM) |

### M7（3）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 2 | 有符号计数衍生 DV → 线性 FE 估计器选择 | 计数派生但因正负相减可取负值的 DV | 先检查支持域再选模型，避免按来源标签机械用 count model | EMERGING | Lee, Wu & Bednar (OS) |
| 5 | rare outcome 下 year + industry FE（无法 firm FE） | rare binary outcome、单位内无 DV 变异的面板（副槽位 M8） | 纠正常见误写：是 always-zero → collinearity 而非 incidental parameters | VERIFIED | Hoffmann et al. 2024 (JM) |
| 6 | staggered adoption 下 POST 与 Treat×Post 共线性说明 | 州级法律 staggered 设计，预防"为何没控制 post"质疑 | 与变体 5 同类共线性代数，但针对 ever-treated×post 设计 | VERIFIED | Hoffmann et al. 2024 (JM) |

### M2（3）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 1 | 跨层级冲击映射 + 处理事件样本漏斗 | 冲击在地理/制度层、分析单位为企业的研究 | 只报最终 N 之外，增加"冲击层→暴露规则→事件减少"可审计映射链 | EMERGING | Lee, Wu & Bednar (OS) |
| 7 | 裁量权子样本 + 行业/event 扩展漏斗 | 需防遗漏"有缺陷信号但不作为"单位的召回/事件样本 | 区别于变体 1：漏斗含 assignment stability 排除 + 防遗漏行业扩展 + 理论子样本聚焦 | VERIFIED | Hoffmann et al. 2024 (JM) |
| 15 | always-treated 排除 + 处理组卫生（staggered DiD 样本构造） | 交错 DiD 排除 always-treated 单位、post-only 观测、预处理期不足事件 | 区别于变体 1/7 漏斗：专攻 staggered DiD 样本卫生 | EMERGING | Moon et al. 2026 (JM) |

### M1（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 8 | 重复交易情境（双重出售使价值变化可观测） | 研究问题要求观察同一资产的价值变化（buyout 等） | 把双重定价/重复交易写成理论检验前提，而非仅论证冲击外生 | EMERGING | Castellaneta et al. 2017 (SMJ) |

### M3（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 10 | ΔV/IRR 作为一阶差分 → 截面估计等价于 DiD | 只有单次观测、DV 已嵌一阶差分的截面设计（副槽位 M7、M8） | 区别于标准 unit-year TWFE（变体 3–4）：等价性叙事 + 数据约束诚实说明 | EMERGING | Castellaneta et al. 2017 (SMJ) |

### M4（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 9 | 持有窗内处理编码 + staggered 教学示例 | 持有窗（非日历年面板）处理赋值的 staggered 设计（副槽位 M8） | 区别于变体 6：单州示例 → staggered 重组两段叙事降低理解成本 | EMERGING | Castellaneta et al. 2017 (SMJ) |

### M6（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 11 | entry/exit 年 FE + 多维 FE + 冲击层级聚类 | 每单位一次观测的持有窗截面（副槽位 M7） | 区别于标准 unit FE + year FE：entry×exit 年 FE 吸收时长与两端冲击 | EMERGING | Castellaneta et al. 2017 (SMJ) |


## 主骨架

参见 `write-methods/SKILL.md` → 槽位骨架加载 → 本类型适用的 `references/slot-M*.md`（各 slot 文件内含 `自然实验-DiD` 专用变体）。

## 设计特征摘要

- 地理层级冲击必须明确映射到分析单位，并报告从原始事件到可识别处理组的样本漏斗。
- 估计器选择应服从因变量支持域；“由计数项目构造”不等于必须使用计数模型。
- 错位实施 DiD 的可信度检查应围绕识别威胁组织；传统 TWFE/Bacon 只能诊断，不能修复异质处理效应偏误。

## 累积变体

<!-- distill-methods-exemplar Phase 4 验证通过的变体写入此处 -->
<!-- 格式：
### 变体 N: [来源论文] (YYYY-MM-DD)
**验证状态**: 通过 / 需修正
**槽位**: M?
**骨架**:
> "..."
**与原骨架差异**: ...
-->

### 变体 1：跨层级冲击映射 + 处理事件样本漏斗（2026-08-02）

**来源论文**: Lee, Wu & Bednar, *Organization Science*, DOI 10.1287/orsc.2024.18968
**原始句锚点**: "While their analysis is at the county level, ours focuses on firms. As a result, our sample includes fewer instances of newspaper decline because not every affected county has a publicly traded firm."

**验证状态**: EMERGING（单篇；`section_variant`）

**槽位**: M2（Data and Sample）

**骨架**:
> "We observe [shock] at the [geographic/institutional] level and assign exposure to [analysis units] using [headquarters/operating-location rule]. This mapping explains why the number of treated [locations] in the analytical sample is smaller than the number in the original event database: only [locations meeting the unit-presence rule] contribute treated observations. Starting from [N0] affected locations, the final sample contains [N1] treated locations, [N2] units, and [N3] unit-period observations; we also report the distribution across [event subtypes]."

**与原骨架差异**: 不只报告最终 N；把“冲击发生在哪一层—谁被视为暴露—为何处理事件减少”写成可审计映射链。

**边界**:
- headquarters 映射必须有理论理由；若经营活动跨地区，需讨论 exposure misclassification。
- 同一单位可能受多个事件影响时，必须预先规定 first-event、stacked cohort 或风险集规则。

### 变体 2：有符号的计数衍生因变量 → 线性 FE 估计器选择（2026-08-02）

**来源论文**: Lee, Wu & Bednar, *Organization Science*, DOI 10.1287/orsc.2024.18968
**原始句锚点**: "Because our dependent variable contains negative values, fixed effects Poisson or negative binomial regressions are not applicable even though the measure is essentially count-based. Following prior studies employing similar measures (e.g., Qian et al. 2019, Jia et al. 2020, Wu et al. 2026), we therefore use fixed-effects linear regressions."

**验证状态**: EMERGING（单篇；`section_variant`）

**槽位**: M7（Model Specification）

**骨架**:
> "Although [outcome] is constructed from counts, it is defined as [positive component minus negative component] and can therefore take negative values. Poisson and negative-binomial models, which require a nonnegative outcome, are not appropriate for this signed measure. We estimate a linear [unit]-fixed-effects model with [time] fixed effects, lag [moderators/controls] by [k] period(s), and cluster standard errors at the level where treatment varies."

**与原骨架差异**: 先检查支持域，再选择模型；避免根据变量来源标签机械使用 count model。

**边界**:
- 负值支持域只是排除 Poisson/NB 的理由，不自动证明线性模型最优；仍需检查极端值、分布形态与替代构造。
- 聚类层级原则上不应低于处理赋值层级；处理簇很少时需小样本修正或随机化推断。

### 变体 3：错位 DiD 三层诊断栈 + 现代估计诚实边界（2026-08-02）

**来源论文**: Lee, Wu & Bednar, *Organization Science*, DOI 10.1287/orsc.2024.18968
**原始句锚点**: "The recent DiD literature has acknowledged that two-way fixed-effect estimators in staggered DiD design may introduce a "bad comparison" problem that differs from a violation of the parallel-trends assumption but is similarly problematic (Goodman-Bacon 2021), resulting in staggered DiD estimates subject to under-identification issues (Borusyak et al. 2016)."

**验证状态**: EMERGING / LEGACY-DIAGNOSTIC（可借用组织方式，不得把原估计方案当现代默认）

**槽位**: M8（Validity and Robustness）

**骨架**:
> "We organize design checks by threat. First, an event-study plot assesses pre-treatment dynamics. Second, a permutation exercise randomly reassigns treated units and treatment timing to evaluate whether similarly large estimates arise under placebo exposure. Third, a decomposition describes which treatment-group comparisons receive weight in the conventional TWFE estimate. Because decomposition diagnoses rather than removes contamination from heterogeneous cohort/time effects, the main analysis should additionally use a heterogeneity-robust staggered-DiD estimator (e.g., cohort-time ATT or interaction-weighted event study) and report sensitivity to deviations from parallel trends."

**与原骨架差异**: 把图、置换与权重分解分别绑定到 pretrend、偶然相关和污染比较三类威胁，并明确诊断与修复的差异。

**不可降级的现代要求**:
- Goodman–Bacon 分解不能替代 Callaway–Sant'Anna / Sun–Abraham 等异质性稳健估计。
- “处理前系数不显著”不是平行趋势成立的充分证据；应给联合检验、置信区间和图形，并在可行时做 HonestDiD/Rambachan–Roth 型敏感性分析。
- 随机置换必须保持真实处理设计的簇结构与实施时序约束；任意打乱会产生无意义的安慰剂分布。

### 变体 4：staggered DiD 识别栈 — model-free → 机制锚定 → pretrend → jurisdiction 安慰剂（2026-08-05）

**来源论文**: Hoffmann, Cheong, Phan & Zurbruegg 2024 (*Journal of Marketing*)
**原始句锚点**: "Before estimating our regression models, we present model-free evidence and explore the raw data to assess whether the quasi-experiment of the staggered adoption of UD laws appears to have an effect on the dependent variable, as per Goldfarb, Tucker, and Wang's (2022) recommendation."

**验证状态**: VERIFIED（单篇；`section_variant`）

**槽位**: M8（Identification Strategy）

**骨架**:
> "Before estimating regressions, we compare mean [outcome] for [unit-years] exposed versus unexposed to [law/policy], following [Goldfarb, Tucker & Wang 2022]. Although theory centers on [threat/mechanism construct], prior work shows that [observable manipulation outcome: e.g., lawsuit filings] declines after adoption ([citations]), supporting the shock channel. We then test parallel trends by interacting [TreatGroup] with pretreatment indicators [Pre(-3)], [Pre(-2)], and [Pre(-1)]; insignificant pretreatment interactions indicate no detectable pretrend. Finally, we conduct a falsification test by randomly reassigning each [unit]'s [jurisdiction attribute] to another [jurisdiction] with different adoption timing, reestimating the model, saving the test statistic, and repeating [N] times ([Janakiraman, Lim & Rishika 2018]). The placebo distribution relative to the true estimate supports that state-level confounds are unlikely to drive the results."

**与原骨架差异**: 变体3 强调 TWFE 诊断栈；本变体是 **Marketing quasi-experiment 四段式说服链**：无模型证据 → 文献 manipulation check → 事件窗 pretrend → 地理属性置换安慰剂。

**边界**:
- manipulation check 引用他人结果不等于本文 manipulation test；须明确是 external validation。
- jurisdiction 安慰剂须保持真实 adoption 时序结构，仅 shuffle assignment rule。
- 入库的是叙事组织，非对 Sun–Abraham 估计器的推荐。

### 变体 5：二元 rare outcome 下 year + industry FE，无法 firm FE（perfect collinearity）（2026-08-05）

**来源论文**: Hoffmann, Cheong, Phan & Zurbruegg 2024 (*Journal of Marketing*)
**原始句锚点**: "It is worth noting that it is not possible to include firm fixed effects because of the way our data is structured. That is, our sample includes a set of firms that never issue a recall but are in the same industries as the firms that do issue a recall."

**验证状态**: VERIFIED（单篇；`section_variant`）

**槽位**: M7 + M8

**骨架**:
> "We estimate a conditional logit panel model with year and industry fixed effects. We cannot include [unit] fixed effects because many [units] never experience the binary outcome, leaving no within-[unit] variation in the dependent variable; [unit] fixed effects would therefore be perfectly collinear with the outcome. We control for time-varying [unit] characteristics — [named controls] — and cite prior [outcome] studies using the same FE structure ([citation]). Industry fixed effects absorb heterogeneity such as [industry-specific baseline hazard example]."

**与原骨架差异**: 纠正常见误写：Hoffmann **不用 firm FE**，理由也不是 incidental parameters，而是 always-zero outcome → collinearity。

**边界**:
- 若样本中所有 unit 都有 outcome variation，此辩护不适用。
- industry FE 不能替代 firm FE；不得写 "fully addresses unobserved heterogeneity"。

### 变体 6：staggered adoption 下 POST 与 Treat×Post 共线性说明（2026-08-05）

**来源论文**: Hoffmann, Cheong, Phan & Zurbruegg 2024 (*Journal of Marketing*)
**原始句锚点**: "Because the interaction term UD_LAW × POST_ADOPTION would be perfectly collinear with the POST_ADOPTION indicator, the main effect of POST_ADOPTION drops out from our models."

**验证状态**: VERIFIED（单篇；`section_variant`）

**槽位**: M7

**骨架**:
> "In our staggered, [jurisdiction]-specific adoption design, there is no single event date; [Post] switches on only for [units] in adopting [jurisdictions] after the local adoption year and remains zero for [units] in never-adopting or not-yet-adopting [jurisdictions]. Because [Post] is perfectly collinear with [TreatGroup] × [Post], the standalone [Post] indicator drops from the model, consistent with prior staggered state-law DiD studies ([citations])."

**与原骨架差异**: 把 staggered DiD 的变量代数写进 Methods，预防 "为什么没控制 post period" 的审稿质疑。

**边界**:
- 仅适用于 ever-treated group × post indicator 的 state-law 设计。
- cohort-specific event study 设计需改写此叙事。

### 变体 7：裁量权子样本 + 行业/event 扩展漏斗（2026-08-05）

**来源论文**: Hoffmann, Cheong, Phan & Zurbruegg 2024 (*Journal of Marketing*)
**原始句锚点**: "To ensure that we do not omit observations where there might have been a need for a product recall (i.e., an instance of a defective product) but the firm decided not to issue one, we also include all firms from industries in which, during the sample period, there was an incident report filed by consumers with the CPSC through its "Safer Products" website, indicating that they experienced an issue with an unsafe product."

**验证状态**: VERIFIED（单篇；`section_variant`）

**槽位**: M2

**骨架**:
> "We begin with [starting universe] over [period]. We drop [units] that changed [assignment attribute: e.g., state of incorporation] during the window ([citation]). Following prior [outcome] DiD work ([citation]), we include all [units] in industries with at least one [outcome event] and also [units] in industries with consumer incident reports on [incident source], so we do not omit [units] that may have faced a defect signal but chose not to [outcome]. For the main test we focus on [events] without [prior harm condition] because [regulatory/legal pressure] removes [actor] discretion once [harm] materializes ([footnote/citation]). The final panel contains [N_units] [units] and [N_panel] [unit-years]."

**与原骨架差异**: 漏斗含 assignment stability exclusion、防遗漏 non-outcomers 的行业扩展、理论驱动子样本聚焦三层。

**边界**:
- 子样本聚焦须在 Results 报告全样本/替代子样本稳健性。
- incident-report 扩展假设报告可代理 latent defect need。

### 变体 8：重复交易情境（buyout dual-sale）使制度冲击前后价值变化可观测（2026-08-05）

**来源论文**: Castellaneta, Conti & Kacperczyk 2017 (*Strategic Management Journal*)
**原始句锚点**: "The ideal setting to test our theory would allow us to observe changes in company market value after an increase in the legal protection of trade secrets: that is, the same company would need to be sold twice—before and after the strengthening of trade secrecy protection."

**验证状态**: EMERGING（单篇；`section_variant`）

**槽位**: M1（Research Setting）

**骨架**:
> "The ideal setting to test [theoretical relationship] would allow us to observe changes in [unit market value / priced outcome] after an increase in [institutional protection]: that is, the same [unit] would need to be [sold/transacted] twice—before and after the strengthening of [protection]. While identifying such a context can be challenging, we leverage the [PE buyout / repeated-transaction] market. [Investors] make profits by buying and reselling [targets] over relatively short holding periods. This setting holds an important advantage because the great majority of [units] are [transacted] at least twice: once at [entry/acquisition] and again at [exit/resale]. Moreover, we can identify [units] acquired before the strengthening of [protection] and sold after, as well as [units] acquired and sold without any intervening change in [protection]."

**与原骨架差异**: 通用 DiD setting 只论证"冲击外生 + 可观测暴露"。本变体把 **重复定价/双重交易** 写成理论检验的前提条件，并用 buyout holding period 同时定义 treated（冲击落在持有窗内）与 untreated（持有窗内无冲击）的可观测性。

**边界**:
- 仅当研究问题要求观察 **同一资产的价值变化**（而非水平）时适用。
- Setting 优势不等于识别完成；仍需 jurisdiction assignment、外生性与对照构造。

### 变体 9：持有窗内处理编码 + staggered 教学示例（treatment/control 随时间重组）（2026-08-05）

**来源论文**: Castellaneta, Conti & Kacperczyk 2017 (*Strategic Management Journal*)
**原始句锚点**: "UTSA_{tbuy,tsell} is equal to 1 if the UTSA was enacted in the state where the company is incorporated during the period between t_buy (the year of its purchase by the PE company) and t_sell (the year of its sale by that company to another firm), and 0 otherwise."

**验证状态**: EMERGING（单篇；`section_variant`）

**槽位**: M4 / M8（Treatment definition + Identification）

**骨架**:
> "We use a quasi-experimental design with a treatment group of [units] in [jurisdictions] that adopted [law/policy] during the [holding/exposure] window between [t_entry] and [t_exit], and a control group of [units] in [jurisdictions] that did not. [Treatment] equals 1 if [law] was enacted in the [assignment jurisdiction: e.g., state of incorporation] between [t_entry] and [t_exit], and 0 otherwise. Identification can be illustrated with an example. Consider [Jurisdiction]'s [year] enactment. Treated [units] are those acquired before [year] and resold after [year] in [Jurisdiction]. Controls are similar [units] acquired before [year] and resold after [year] but located in [jurisdictions] where no [law] passed in that window. β is the difference in [Δoutcome] between treated and control groups. Relative to this single-event example, the regression accounts for staggered adoption: the composition of both treatment and control groups changes over time as progressively more [jurisdictions] become treated. This design mitigates the concern that treatment and control groups are systematically different ([citation: e.g., Bertrand & Mullainathan 2003]). We cluster standard errors at the [jurisdiction] level—the level of the shock."

**与原骨架差异**: 变体6 解决 POST 与 Treat×Post 共线性；本变体解决 **持有窗（非日历年面板）处理赋值**，并用单州示例→staggered 重组的两段叙事降低审稿人理解成本。

**边界**:
- Assignment jurisdiction（incorporation vs HQ vs operations）必须有制度理由；错配会污染处理。
- 教学示例不能替代平行趋势/异质性稳健估计的正式讨论（若数据允许 unit-time 面板）。

### 变体 10：ΔV/IRR 作为一阶差分 → 截面估计等价于 DiD 的识别叙事（2026-08-05）

**来源论文**: Castellaneta, Conti & Kacperczyk 2017 (*Strategic Management Journal*)
**原始句锚点**: "However, our empirical strategy is equivalent to the DiD framework to the extent that the IRR measures change in the target firm's market value, and so the dependent variable incorporates the first difference before and after the treatment."

**验证状态**: EMERGING（单篇；`section_variant`）

**槽位**: M3 / M7 / M8（Outcome + Identification equivalence）

**骨架**:
> "Our analysis is conducted at the single-[unit] level. The main dependent variable is [IRR / holding-period return / percentage change in market value], a standard performance measure in [buyout/private markets] ([citations]). There is a natural connection between [investor return] and [unit] market value: [investor] earns a positive return only if, during the holding period, the value of the [unit] exceeds the price initially paid. [ΔV measure] thus captures the [unit]'s percentage change in market value over the holding period ([citation/appendix]). Our approach is cross-sectional: each [unit] is a single observation. A full difference-in-differences regression would require observing [price/level] at least twice, before and after treatment. Because the data allow us to observe only the percentage change in [outcome]—not repeated levels—the DiD framework is difficult to implement fully. However, the strategy is equivalent to DiD to the extent that [ΔV measure] already incorporates the first difference before versus after treatment. We therefore estimate OLS of [ΔV_i] on [Treatment_{t_entry,t_exit}] and controls. Causal language ("effect of") is warranted only if treatment timing is plausibly exogenous."

**与原骨架差异**: corpus 此前无 **"outcome embeds first difference → cross-section ≈ DiD"** 叙事。区别于标准 unit-year TWFE DiD（变体3–4）。

**边界 / 诚实边界**:
- 等价性依赖于 [ΔV] 确实度量市场价值变化；杠杆、中期现金流、费用分摊、异常值截尾可能破坏该映射，须在 appendix或稳健性中处理。
- 此叙事 **不是** Callaway–Sant'Anna / Sun–Abraham 的替代品；当研究者拥有 unit-time 面板时，不应以此回避现代 staggered-DiD 估计器与平行趋势检验。
- 可将强度编码（binary vs continuous protection index）作为稳健性，而非主识别的唯一形式。

### 变体 11：entry/exit 年 FE + 多维 FE + 冲击层级聚类（持有窗截面）（2026-08-05）

**来源论文**: Castellaneta, Conti & Kacperczyk 2017 (*Strategic Management Journal*)
**原始句锚点**: "To address this concern, we include entry-year fixed effects, a dummy for the year t_buy of company purchase by the PE company, and exit-year fixed effects, a dummy for the year t_sell of company sale."

**验证状态**: EMERGING（单篇；`section_variant`）

**槽位**: M6 / M7（Controls + Specification）

**骨架**:
> "Although [policy shock] provides a quasi-experimental setting, we include controls to alleviate remaining concerns. We include [deal/investment size] because [larger deals may induce greater political monitoring or lobbying]. Longer holdings are more likely to experience institutional change, and by construction duration correlates with [ΔV]; we therefore include entry-year fixed effects for [t_entry] and exit-year fixed effects for [t_exit]. These absorb year-specific shocks at entry and exit and also control for holding duration ([t_exit] − [t_entry]). We include [investor/PE-firm] fixed effects for time-invariant [investor] characteristics (e.g., political connections), [industry] fixed effects, and [jurisdiction] fixed effects to mitigate concern that treatment is driven by [pro-business culture] that is hard to capture with observables. We also include indicators for [public-at-entry / exit mode: e.g., IPO]. Standard errors are clustered by [jurisdiction]—the level at which treatment varies ([citation])."

**与原骨架差异**: 标准面板 DiD 用 unit FE + year FE。本变体针对 **每单位一次观测的持有窗截面**：用 entry×exit 年 FE 同时吸收时长与两端宏观冲击，并用 investor FE 堵住"谁选择交易"的通道。

**边界**:
- Entry/exit FE 不能替代 jurisdiction 外生性论证。
- 高维 FE 在小样本或稀有处理下可能过度吸收；须报告处理份额与有效自由度意识。

### 变体 12：政治经济外生性电池 — 质性检索 + LPM/hazard 采纳时点 + 供需零相关（2026-08-05）

**来源论文**: Castellaneta, Conti & Kacperczyk 2017 (*Strategic Management Journal*)
**原始句锚点**: "Specifically, we search the Lexis-Nexis database for press releases indicating that PE firms actively lobbied for the UTSA statutes. Not surprisingly, we find no such evidence."

**验证状态**: EMERGING（单篇；`section_variant`）

**槽位**: M8（Validity / Exogeneity）

**骨架**:
> "Identification assumes that enactment of [law] is exogenous with respect to [unit] and [jurisdiction] characteristics associated with [outcome]. We address this threat in three steps. First, we search [press database] for evidence that [affected actors] actively lobbied for [law]; absence of such evidence is consistent with prior work arguing that adoption timing was unrelated to [jurisdiction] economic or political conditions ([citation]). Second, we estimate linear probability models in which the dependent variable is an indicator for the year of [law] enactment in a [jurisdiction], including lagged [investment/disposal volume], [GDP per capita], [number of firms], and [political party of governor]. These covariates should not significantly predict enactment if timing is as-good-as-random; we obtain similar nulls with discrete-time survival models (logistic hazard and proportional hazard). Third, because a shift in [investor] supply or demand could mechanically move [unit] value, we test whether [law] enactment correlates with (log) [number of firms] or with the value of [investor] investments and disposals; null associations mitigate this channel."

**与原骨架差异**: 变体4 是 Marketing 四段式（model-free→机制→pretrend→置换安慰剂）。本变体是 **政策时点外生性电池**：质性游说检索 + 采纳方程（LPM/hazard）+ 市场侧供需检验，专攻"政治经济内生采纳"威胁。

**边界**:
- 采纳方程的 null 不是外生性证明，只是与可观测州特征不相关的证据。
- 游说检索受媒体覆盖偏误限制；应与既有政治经济文献互证。

### 变体 13：日历安慰剂 ±k 年（假处理弱于真处理）（2026-08-05）

**来源论文**: Castellaneta, Conti & Kacperczyk 2017 (*Strategic Management Journal*)
**原始句锚点**: "To rule out the possibility that our treatment generates statistically significant results merely by chance, we next perform a series of robustness checks by creating a "placebo" treatment. In particular, we pretend that the change in trade secrets occurs five years before and five years after the real year of change."

**验证状态**: EMERGING（单篇；`section_variant`）

**槽位**: M8（Placebo / Falsification）

**骨架**:
> "To rule out the possibility that treatment generates statistically significant results merely by chance, we create placebo treatments by pretending that the change in [protection] occurs [k] years before and [k] years after the real year of change. We expect the fake treatment to have a weaker or null effect on [outcome] relative to the actual treatment—including null main effects and null interactions with [moderators]. Results are reported in [table/appendix]."

**与原骨架差异**: 变体3/4 的安慰剂是 **置换/重分配** jurisdiction 或处理时点；本变体是 **固定错位 ±k 年日历安慰剂**，更适合持有窗截面、难以画标准 event-study 的设计。

**边界**:
- ±k 的选择须事前或按惯例说明；k 太小会与真处理窗重叠。
- 安慰剂应在 Methods 预告位置（M8/M10）；仅塞进 Results 附录会削弱"设计内建"印象。


### 变体 14：M8_judicial_shock_two_assumption（moon2026）

**槽位**: M8

**模板/骨架**:
> "To identify the effect of [policy/legal change] on [outcome], we use [court ruling/regulatory event] as an exogenous shock. Considering [event] as an exogenous shock in our context rests on two assumptions. First, [decision-makers] should be aware of [the precedent-setting event], which becomes [institutional form]. Reassuringly, prior research shows that [actors] are likely to be aware of [event] because [dissemination channel] ([citation]). Second, [changes in the event] are not influenced by individual [units]. Indeed, prior work shows that [event] depend[s] on [case-specific circumstances/institutional discretion] and [are] thus largely independent of [unit] actions or lobbying efforts ([citation]). Therefore, considering the findings of prior work, [event] can be viewed as an exogenous shock."

来源：Moon et al. (2026, Journal of Marketing)。


### 变体 15：M2_staggered_did_always_treated_hygiene（moon2026）

**槽位**: M2

**模板/骨架**:
> "Recent research on staggered difference-in-differences (DiD) notes that always-treated units are a potential source of bias in identifying the treatment effect ([citation]). In this context, the DiD estimate is a variance-weighted average of the constituent 2x2 DiD estimates in the data, and one of the comparisons includes always-treated units as effective controls. As always-treated units reflect the treatment effect in the outcomes, the treatment effect estimated from the staggered DiD in this case may potentially introduce a negative weight and bias the estimate ([citation]). To address this concern, we exclude [units treated before the sample period]. In addition, we do not include [units with only posttreatment observations]. To allow for variation before the treatment, we consider [events] that provide at least [N] years of pretreatment periods for the treated [units]. Using this approach, our sample consists of [final N] ([treated N] in the treatment group; [control N] in the control group)."

来源：Moon et al. (2026, Journal of Marketing)。

## 反模式（Castellaneta 蒸馏补充）

| 反模式 | 问题 | 应改为 |
|--------|------|--------|
| **ΔV≈DiD 却省略等价条件** | 声称截面 IRR/回报"等价于 DiD"但不说明 DV 如何嵌入一阶差分、也不讨论现金流/截尾对映射的破坏 | 先写测量→一阶差分映射，再写"难以实施完整 DiD"的数据约束，并加诚实边界 |
| **持有窗处理无 assignment 规则** | 只说"州级法律"，不说明 incorporation / HQ / operations 哪一层映射到分析单位 | 显式声明 assignment jurisdiction + 文献/制度理由 |
| **外生性电池无 Methods 预告** | 政治经济 LPM、供需检验、±k 安慰剂全部首次出现在 Results，Methods 无位置预告 | 在 M8/M10 预告检验族与威胁对应关系 |

## 诚实边界（设计级）

- 本家族变体 8–13 服务 **交错州法 + 持有窗截面（非 unit-year 面板）**；不得默认迁移为现代 TWFE/CS-SA 面板 DiD 的主模板。
- Binary 政策编码忽略强度异质性时，须准备连续保护指数或强度稳健性。
- CEM / 政治经济 null / 日历安慰剂均不替代不可观测混淆的完整讨论。
