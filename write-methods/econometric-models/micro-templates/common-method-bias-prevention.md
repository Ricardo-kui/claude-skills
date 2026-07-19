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
