---
category: robustness-foreshadowing
description: 稳健性检验预告——在 Methods 或 M10 过渡段中预告 Results 将报告的稳健性检验。
function: 可信性——表明稳健性不是事后补充，而是研究设计的有机组成部分
slots: M8, M10
extracted_from: 21 design-type corpus files
created: 2026-05-22
updated: 2026-05-22
---

# 稳健性检验预告（Robustness Foreshadowing）

## 核心原则

顶刊现在将稳健性视为**系统性期望**而非事后补充。
在 Methods 中预告稳健性检验，表明这些是研究设计的有机组成部分，而非结果不显著后才找的借口。

## 标准预告句式

| 微模板 | 功能 | 风险 |
|--------|------|------|
| `To ensure that our findings are not driven by [specific modeling choice / measure definition / sample composition], we conduct a series of robustness checks.` | 总起句 | 安全 |
| `First, we re-estimate our models using [alternative estimator / distribution] and find that [key results] remain [status].` | 模型选择稳健性 | 需注意：不要在 Methods 中报告结果 |
| `Second, we test alternative operationalizations of [construct] using [alternative measure / cutoff] and obtain [consistent / qualitatively similar] results.` | 测量敏感性 | 需注意：不要在 Methods 中报告结果 |
| `Third, we address potential selection concerns by [matching / weighting / subsample analysis] and confirm that [focal effect] is robust.` | 样本选择稳健性 | 需注意：不要在 Methods 中报告结果 |
| `Fourth, to mitigate reverse causality concerns, we [lag structure / control function / lead-lag test] and find [result].` | 反向因果稳健性 | 需注意：不要在 Methods 中报告结果 |
| `Finally, we rule out [alternative explanation] by [test design]; the [null / nonsignificant] result supports our preferred interpretation.` | 替代解释稳健性 | 需注意：不要在 Methods 中报告结果 |

## 按稳健性类别分类

### 模型选择（Model Selection）

| 微模板 | 适用情境 |
|--------|---------|
| `We also considered [alternative estimator]; results using this approach are reported as [robustness/supplement].` | 通用替代估计器 |
| `We demonstrate that results are robust to [alternative distributions: e.g., Weibull and Gompertz].` | 生存分析分布选择 |
| `We report Probit/Logit IV only as robustness.` | 二元 DV + IV |

### 测量敏感性（Measure Sensitivity）

| 微模板 | 适用情境 |
|--------|---------|
| `We test alternative operationalizations of [construct] using [alternative measure / cutoff].` | 变量操作化 |
| `We examine [top/bottom 20%, 30%, 40% vs. quartile] as alternative thresholds.` | 分位数/阈值 |
| `We use [raw count vs. relative percentage] as alternative measures.` | 测量单位 |

### 样本选择（Sample Selection）

| 微模板 | 适用情境 |
|--------|---------|
| `We address potential selection concerns by [matching / weighting / subsample analysis].` | 选择偏差 |
| `We restrict the sample to [subsample criteria] to ensure [robustness condition].` | 子样本 |
| `We compare [attrition analysis] to assess whether sample loss is systematic.` |  attrition |


**补充变体（westphal_bednar2005 型）：问卷非应答双重防御链（K-S + Heckman）**
> To assess the representativeness of the sample, we compared [units] in the final sample with those excluded due to [non-response/missing data], using the [Kolmogorov-Smirnov two-sample test], which determines whether the distribution of a given variable is different for [units] in the final sample versus others in the sample frame (i.e., including differences in kurtosis, skewness, and other features of the distribution, as well as differences in central tendency). There were no significant differences with respect to [variables examined in the study]; p-values ranged from [X] to [Y]. In separate analyses, we also tested for sample selection bias with a multivariate approach, using the [Heckman sample selection model]; the selection equations included [archival variables], as well as [features of the data-collection process itself (e.g., survey wave)]. The results were very similar to those presented below, and the selection parameter was not significant.
- 双层防御：分布形状级单变量检验（K-S，强调峰度/偏度等分布特征而非仅均值，报 p 值区间）→ 多变量 Heckman 选择模型（选择方程含档案变量 + 调查设计特征）；双收口 = 结果与主模型一致 + 选择参数不显著
- 与 heckman-peer-prevalence-exclusion.md 互补：彼处 Heckman 服务于同行 prevalence 排除限制识别；本链服务于调查非应答/缺失数据的样本选择防御

### 反向因果（Reverse Causality）

| 微模板 | 适用情境 |
|--------|---------|
| `To mitigate reverse causality concerns, we [lag structure / control function / lead-lag test].` | 时序内生性 |
| `We lag [predictor] by [one/two] year(s) to preserve temporal ordering.` | 滞后结构 |
| `We conduct Granger causality tests to assess whether [X] precedes [Y].` | 格兰杰因果 |

### 替代解释（Alternative Explanations）

| 微模板 | 适用情境 |
|--------|---------|
| `We rule out [alternative explanation] by [test design].` | 竞争性理论 |
| `We include [alternative mechanism] as a rival explanation.` | 机制竞争 |
| `We exploit a [regime change] as a falsification test.` | 制度安慰剂 |

---

## M10 过渡段中的稳健性预告

在 M10（Methods→Results 过渡段）中，稳健性预告可以与 Results 预告合并：

```text
The Results section first reports [main tests] and then examines
[validity/robustness checks]. Because [measure/design] raises [concern],
we address this issue in supplemental analyses using [test].
```

---

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| `Results are robust.`（在 Methods 中） | 在 Methods 中报告结果 | 改为 `We conduct robustness checks using [methods], reported in [location].` |
| 完全不提及稳健性 | 审稿人质疑是否做过 | 至少预告 2–3 类稳健性检验 |
| `We did many robustness checks.` | 模糊 | 具体列出检验类别和方法 |
| 稳健性检验与主分析设计不一致 | 逻辑断裂 | 确保稳健性检验针对的是主分析的同一个识别关切 |
