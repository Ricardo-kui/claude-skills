---
category: identification-foreshadowing
description: 识别策略预告——在 Methods 中提前告知审稿人 Results 将如何处理关键识别假设。
function: 可信性——让审稿人相信因果推断会在 Results 中得到充分论证
slots: M8
extracted_from: 21 design-type corpus files
created: 2026-05-22
updated: 2026-05-22
---

# 识别策略预告（Identification Foreshadowing）

## 核心原则

不要在 Methods 中**报告**检验结果，但要**预告**检验的位置和方法。
这是顶刊 Methods 的 ritual 规范——让审稿人知道你会在 Results 中兑现识别承诺。

## 按设计类型分类

### 自然实验 / DiD

| 微模板 | 功能 | 风险 |
|--------|------|------|
| `The key identifying assumption is that [treated and control units] would have followed similar trends absent [treatment]. We assess this assumption in the Results section using [event-study/leads-lags] specifications.` | 平行趋势预告 | 安全 |
| `We first estimate a parsimonious specification because [controls] may be affected by [treatment].` | Bad Control 规避预告 | 安全 |
| `We also conduct permutation tests by randomly assigning [treatment status/timing] across [N] iterations.` | 置换检验预告 | 安全 |
| `We assess whether [unobserved characteristics] could drive our results through [test].` | 安慰剂检验预告 | 安全 |

### IV / 2SLS

| 微模板 | 功能 | 风险 |
|--------|------|------|
| `It satisfies the exclusion restriction because [theoretical argument for why instrument affects outcome only through predictor].` | 排他性约束理论论证 | 安全 |
| `[IF overidentified:] We report the Sargan / Hansen J overidentification test ([value], p = [value]), which does not reject the null that all instruments are valid.` | 过度识别检验预告 | 安全 |
| `[IF just-identified:] Because the model is just-identified, overidentification tests are infeasible. We therefore rely on theoretical arguments for the exclusion restriction and conduct placebo tests / sensitivity analyses.` | 恰好识别时的替代策略 | 安全 |
| `The first-stage F-statistic is [value], exceeding the Stock-Yogo threshold, indicating that [instrument] is not weak.` | 弱工具变量检验 | 安全 |

### 实验

| 微模板 | 功能 | 风险 |
|--------|------|------|
| `To assess the [manipulation] manipulation, participants rated [check item].` | 操纵检验预告 | 安全 |
| `Participants in the [condition] condition perceived [construct] as [higher/lower] than those in the [comparison] condition.` | 操纵检验预期结果 | 需注意：不要在 Methods 中报告实际结果 |
| `Results were [unchanged/qualified] when [attention-check/manipulation-check exclusion] was applied.` | 稳健性到操纵检验 | 需注意：不要在 Methods 中报告实际结果 |

### 匹配 / PSM

| 微模板 | 功能 | 风险 |
|--------|------|------|
| `We verify overlap by plotting [propensity-score distributions / covariate balance] before and after matching; the [common support region] covers [percentage]% of the sample.` | 共同支撑域预告 | 安全 |
| `The pre-treatment coefficients are [individually / jointly] insignificant ([test statistic] = [value], p = [value]), suggesting no detectable pre-treatment divergence.` | 匹配后平衡检验预告 | 需注意：不要在 Methods 中报告实际结果 |

### 同伴效应 / 网络效应

| 微模板 | 功能 | 风险 |
|--------|------|------|
| `Because [network-based construct] may capture common shocks rather than true peer influence, we conduct falsification tests.` | 反事实网络检验预告 | 安全 |
| `We re-estimate our models using [placebo network: random peers / future peers / peers from unrelated network layer] as the independent variable.` | 安慰剂网络检验 | 安全 |

---

## 通用诊断检验预告句式

| 微模板 | 功能 | 风险 |
|--------|------|------|
| `We conduct several diagnostic tests. First, [test 1]. Second, [test 2].` | 多检验预告 | 安全 |
| `We report the results in [Results/Table/Appendix].` | 结果位置预告 | 安全 |
| `Although [assumption] cannot be directly tested, the evidence below helps reduce concerns about [threat].` | 不可检验假设的诚实处理 | 安全 |

---

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| `The parallel trends test shows p = 0.34.` | 在 Methods 中报告结果 | 改为 `We assess parallel trends in the Results section using event-study specifications.` |
| `The F-statistic is 23.5, so IV is valid.` | 在 Methods 中报告结果 | 改为 `We report first-stage F-statistics and overidentification tests in Table X.` |
| `Manipulation check was successful.` | 在 Methods 中报告结果 | 改为 `To assess the manipulation, participants rated [check item].` |
| 完全不提及识别假设 | Methods 缺少可信性支撑 | 必须至少预告检验方法和位置 |
