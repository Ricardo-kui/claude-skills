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
