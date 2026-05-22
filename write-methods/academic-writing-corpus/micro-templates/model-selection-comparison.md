---
category: model-selection-comparison
description: 模型选择比较表相关句法——在 Methods 中报告分布、连接函数或规格比较时的叙事单元。
function: 可信性——用统计比较而非纯文字论证模型选择的合理性
slots: M7
extracted_from: eilert2017_jm / malshe2015_jm
created: 2026-05-22
updated: 2026-05-22
---

# 模型选择比较表（Model Selection Comparison）

## 设计原则

当理论未明确指定分布或函数形式时，顶刊用**统计比较表**（BIC/AIC/Log-likelihood）完成模型选择，而非纯文字声明。这类叙述需要清晰的"比较→选择→理由"三步结构。

---

## 类型 1：比较表引入句

**功能**：说明为什么要比较多个候选模型。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `Not much theory or empirical evidence is available to predict the shape of [process].` | 安全 | M7 |
| `No established theory predicts the [functional form / link function / distribution] of [process].` | 安全 | M7 |
| `Because [theory] is silent on the [functional form / distribution] of [process], misspecification bias is a concern.` | 安全 | M7 |
| `The [functional form / distribution] of [process] is not known ex ante.` | 安全 | M7 |

---

## 类型 2：比较动机句

**功能**：解释为什么需要克服误设偏误。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `Therefore, to overcome misspecification bias, we compare several [distributions / specifications].` | 安全 | M7 |
| `To guard against misspecification, we estimate [model] under alternative [distributions / link functions].` | 安全 | M7 |
| `We therefore compare [N] candidate [distributions / specifications] to ensure that our conclusions are not driven by a single functional-form assumption.` | 安全 | M7 |

---

## 类型 3：候选说明句

**功能**：列出比较的候选并简要说明原因。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `These distributions are [continuous] because [reason: the event could occur at any time].` | 安全 | M7（生存分析） |
| `These link functions are candidates because they are the most commonly used [forms] for [outcome type].` | 安全 | M7（非线性模型） |
| `In particular, we estimate [model] incorporating [distribution_1], [distribution_2], [distribution_3], and [distribution_4].` | 安全 | M7 |
| `We estimate [model] with [specification_1], [specification_2], and [specification_3] to ensure comparability.` | 安全 | M7 |

---

## 类型 4：表格引用与选择句

**功能**：引用比较表并宣布选择结果。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `[Table_reference] reports the model fit for these distributions.` | 安全 | M7 |
| `As [table_reference] shows, the [winning_distribution] offers the best fit based on the [BIC / AIC] statistic.` | 安全 | M7 |
| `The [winning_distribution] has the lowest [BIC] value ([value]), followed by [second_best] ([value]).` | 安全 | M7 |
| `Accordingly, we use a [winning_distribution] [model] for [process].` | 安全 | M7 |

---

## 类型 5：Table Notes 模板

**功能**：为模型比较表提供标准化的脚注/注释。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `The [BIC] balances goodness-of-fit with model parsimony; lower values indicate better fit.` | 安全 | M7（表注） |
| `All models include the same [covariates / fixed effects] to ensure comparability.` | 安全 | M7（表注） |
| `The [log-likelihood] is reported for reference; differences across specifications are [small / substantial].` | 安全 | M7（表注） |

---

## 类型 6：方法选择诊断句（简单 vs 复杂估计器）

**功能**：在用诊断检验在两种估计器之间做选择时的叙述。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `We follow the established procedure of estimating both and selecting the preferred estimator based on the [Durbin-Wu-Hausman / Hausman] test.` | 安全 | M7 |
| `The [nonsignificant] test statistic (χ² = [value], p > [threshold]) indicates that [simple estimator] is preferred and [complex estimator] does not provide efficiency gains.` | 安全 | M7 |
| `The [significant] test statistic (χ² = [value], p < [threshold]) rejects [simple estimator], indicating that [complex estimator] is necessary to address [endogeneity concern].` | 安全 | M7 |
| `We report the [SUR] estimator as our preferred specification; results using [3SLS] are reported in [Appendix / robustness section].` | 安全 | M7 |

---

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| `We use Weibull because it is common.` | 无统计论证，仅诉诸惯例 | `We compare Exponential, Log-normal, Log-logistic, and Weibull; Weibull offers the best fit based on BIC (Table X).` |
| `The model fits well.` | 无比较基准 | `The Weibull specification has the lowest BIC (706.89), outperforming the next-best alternative by [margin].` |
| `We tried several models and picked the best one.` | 显得数据挖掘 | `To overcome misspecification bias, we compare [candidates]; [winner] offers the best fit based on [criterion].` |
