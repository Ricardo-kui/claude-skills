# Common Method Bias Prevention 微模板

## 功能

当研究使用问卷数据且 IV/DV 来自同一来源时，预防 CMB 威胁的标准论证骨架。覆盖三种策略：时间分离、客观行为指标、统计诊断。

## 适用场景

- 使用 survey 数据且 IV 和 DV 为感知变量
- SEM / path model 估计
- JM / JMR / SMJ / AMJ 均要求 CMB 预防论证

---

## 变体 A：时间分离 + 客观行为指标（habel2016 型）

**模板**:
> Noting that our conceptual framework links several [perceptual] variables, we carefully designed the data collection to preclude common method bias: we separated the measurement of [IVs] and [DVs] by collecting data through [N] surveys with a time lag of [T weeks/months] and collected [objective behavioral measure] from [company records/archival data] for the [T]-[period] following the [second] survey ([Podsakoff et al. 2003]).

**来源**: habel2016 (JM), Study 2 Methods

**原文锚定**:
> "Noting that our conceptual framework links several customer perceptions, we carefully designed the data collection to preclude common method bias: we separated the measurement of independent and dependent variables by collecting data through two surveys with a time lag of eight weeks and collected customers' objective revenue from company records for the eight-week period following the second survey (Podsakoff et al. 2003)."

**关键特征**:
- 同时做三件事：(1) 时间分离 IV/DV (2) 客观行为指标 (3) 文献引用 (Podsakoff et al. 2003)
- "Noting that our conceptual framework links several [perceptual] variables" — 先承认 CMB 风险存在，再展示预防措施
- "carefully designed" — 传达方法论严谨性
- 客观行为指标来自公司记录而非自报——这是最强的 CMB 预防

**适用**: 有合作企业可获取客观行为数据的研究

---

## 变体 B：时间分离 + Harman 单因子检验

**模板**:
> To reduce the potential for common method variance, we collected data at two time points separated by [T weeks/months]. At Time 1, participants reported [IVs and controls]. At Time 2, they reported [DVs]. In addition, we conducted Harman's single-factor test by loading all items into an unrotated exploratory factor analysis. The results revealed [N] factors with eigenvalues greater than 1, with the first factor accounting for [X]% of the variance—well below the [50%] threshold, suggesting that common method variance is not a major concern ([Podsakoff et al. 2003]).

**适用**: 仅有问卷数据、无客观行为指标时的标准退路

---

## 变体 C：统计控制 + Marker Variable 技术

**模板**:
> We addressed common method bias through both design and statistical procedures. First, we assured respondents of anonymity and separated [IV] and [DV] measures in the survey. Second, we included a marker variable ([marker name]) theoretically unrelated to [core constructs] in the survey. Following [Lindell and Whitney 2001]/[Podsakoff et al. 2003], we computed the correlation between the marker and [core constructs] and adjusted all observed correlations accordingly. The pattern of significant results remained unchanged after this adjustment.

**适用**: 仅有单次截面问卷数据时的补救措施

---


## 变体 D：多源评价者分离 + Kappa 一致性链（carpenterwestphal2001 型）

**适用场景**: [DV] 与 [IV] 可从不同受访者/数据源获取时，用"来源分离"从设计上阻断共同方法偏差，再用一致性统计证明两个来源评价可比、可互换。

**骨架**:
```
[数据源分离] Data for our [DV constructs] were gathered through [respondent A] surveys, whereas [IV constructs] were obtained from [respondent B / archival sources].
[一致性检验] Further analyses were conducted to assess the interrater reliability of these measures: specifically, we compared [respondent A] and [respondent B] responses by calculating [kappa] coefficients for the [shared items].
[判读标准] Values exceeding [.75] are typically thought to indicate [excellent agreement beyond chance], and values between [.40] and [.75] are considered indicative of [fair to good agreement] ([citations]).
[子样本披露] The sample for this analysis included [units] with [both respondent types] (n = [188]).
[换源稳健收口] Given these high levels of interrater reliability, it is perhaps not surprising that the hypothesized effects presented below were substantively unchanged when [DV] was measured with [respondent B] responses rather than [respondent A] responses, or vice-versa.
```
**要点**:
- 五拍：分离声明 → 一致性系数 → 文献阈值判读 → 子样本 N 披露 → 换源互换稳健收口；第四拍把测量可靠性直接接到"结果稳健"，使测量效度论证与假设检验衔接
- "it is perhaps not surprising that..." 是效度证据→结果可信的优雅过渡句式，可直接迁移
- [kappa] 判读区间（Fleiss, 1981; Landis & Koch, 1977）照引文献，不空口断言
**诚实边界**: kappa 适用于条目级/分类一致性；连续量表换用 ICC 或组内相关，不要误贴统计量标签。
**范文锚点**: "Further analyses were conducted to assess the interrater reliability of these measures. Specifically, we compared CEO and outside director responses by calculating kappa coefficients for the monitoring and advice items. ... the hypothesized effects presented below were substantively unchanged when monitoring and advice interactions were measured with director responses rather than CEO responses, or vice-versa."

<!-- wb:carpenter_and_westphal_2001_strategic_context_of_external_ne:m3_multirater_kappa_separate_source_chain -->


### 变体 E：单波截面退路链——预试+Harman+验证子样本 congruence 审计（gulati_2007 型）

**适用场景**: 单波截面问卷、IV/DV 同源同测、无时间分离且无第二评价者来源时的 CMB 防御退路；关键构念存在企业内部档案对应指标时。

**骨架**:
```
[程序性预防] To ensure the reliability and discriminant validity of our constructs, we relied
primarily on items used in prior research and subjected them to a thorough pretest, eliminating
items that were unclear, ambiguous, or led to perceived overlaps in constructs.
[统计诊断] To control for the magnitude of the common-method variance problem characteristic of
survey-based research designs, we conducted [Harman's single-factor test], which generated a
clear multifactor solution with the most influential common factor explaining less than [20]
percent of variation in the data, far below the recommended [50] percent threshold ([citation]).
We thus concluded that common method variance was not a severe problem in our data.
[congruence 审计] Whenever possible, we tried to validate the survey-based measures by checking
their congruence with their objective underlying indicators: we drew a random subsample of
[p] percent of completed surveys ([n]), and asked our contacts at each of the firms to compare
survey responses with their internally collected archival measures of [focal constructs].
[判读收口] The accuracy of classification ... and the correlation coefficient ... both exceeded
[.90], suggesting the high reliability of our self-reported measures.
[合法性收尾] Some scholars have advocated using such perceptual measures, given that actors'
behaviors are ultimately driven by their definitions of the situation ([citations]).
```

**要点**:
- 五拍：程序性预防（预试+题项纯化）→ Harman 阈值判断（首因子方差占比 vs 推荐阈值，带出处）→ 验证子样本（随机 p% 由企业内部联系人对照档案指标）→ congruence 数字判读（>.90）→ 感知测量合法性引文收尾
- 与变体 A/B 的分界：无时间分离可依赖时的退路；与变体 C 的分界：不用标记变量，改用事后 congruence 审计；与变体 D 的分界：彼处双源同时采集+Kappa，本篇单源采集+事后随机子样本比对内部档案
- "far below the recommended [50] percent threshold"——阈值判断句必须带推荐阈值出处，不空口断言
- 验证子样本是本变体的差异拍：把"感知 vs 档案"的 congruence 从口头主张变成可审计数字（分类准确率/相关系数双口径）

**诚实边界**: Harman 通过≠CMB 解除——单波同期测量的时序威胁仍在，应显式承认 simultaneity 并声明更强技术（如 polynomial 分解）的不可行条件；验证子样本依赖企业配合，比对项须逐项声明口径（分类项报准确率、连续项报相关系数，不可混报一个">.90"）；"internally collected archival measures" 的可比性由内部联系人背书而非独立审计。

**范文锚点**: "We conducted Harman's (1967) single-factor test, which generated a clear multifactor solution with the most influential common factor explaining less than 20 percent of variation in the data, far below the recommended 50 percent threshold (Podsakoff and Organ, 1986)."（Measures 开篇段）〔跨段另锚，Joint dependence 段〕"we drew a random subsample of 20 percent of completed surveys (53 observations) and asking our contacts at each of the firms to compare survey responses with their internally collected archival measures of dependence."

<!-- wb:gulati_2007_dependence_asymmetry_and_joint_dependence_in_int:m3_cmv_singlewave_and_validation_subsample -->

## 组装规则

### 优先级
1. **变体 A**（时间分离 + 客观指标）> **变体 B**（时间分离 + Harman）> **变体 C**（统计控制）
2. 优先使用设计层面预防（procedural），统计诊断（statistical）仅作补充

### 必须引用
- Podsakoff, MacKenzie, Lee, and Podsakoff (2003) — CMB 预防的经典综述

### 反模式
- 只说 "we tested for CMB" 但不报告 Harman 检验结果 → 必须给出具体数字
- 时间分离 < 2 周 → 间隔太短无法有效预防
- "common method bias is not a concern" 无任何证据 → 必须有至少一种预防措施 + 一种诊断检验
