---
category: model-selection-comparison
description: 模型选择比较表相关句法——在 Methods 中报告分布、连接函数或规格比较时的叙事单元。
function: 可信性——用统计比较而非纯文字论证模型选择的合理性
slots: M7
extracted_from: eilert2017_jm / malshe2015_jm / kashmiri_nicol_arora_2017_jams
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

## 类型 7：多结果变量的“测量属性 → 估计器”路由表

**功能**：当同一理论模型包含多个测量尺度不同的结果变量时，逐一说明数据生成过程、估计器与解释尺度，避免把模型清单写成方法拼盘。

| 结果属性 | Methods 句式骨架 | 结果解释 |
|----------|-----------------|----------|
| 连续、跨单位且核心 IV 近似时间不变 | `Because [Y1] is continuous and [IV] has limited within-unit variation, we estimate [pooled OLS / correlated RE], with [clustered/robust] standard errors.` | 关联性单位变化；说明为何 FE 不能识别或不符合 estimand |
| 非负计数且过度离散 | `Because [Y2] counts [events] and exhibits overdispersion, we estimate [RE negative binomial] rather than Poisson.` | IRR、预期计数或 AME |
| 0–1 比例（端点可取） | `Because [Y3] is a fractional response bounded in [0,1], we use fractional logit with [robust/clustered] inference.` | 预测比例或 AME，不把 logit 系数当线性百分点 |
| 二元事件 | `Because [Y4] records whether [event] occurred, we estimate [RE/FE logit] and report probability-scale quantities.` | AME、预测概率或 odds ratio |

**组合模板**:
> The outcomes differ in their measurement properties, so a common linear specification would target incompatible data-generating processes. We therefore map each outcome to an estimator before presenting the equations: [Y1 → estimator/reason], [Y2 → estimator/reason], [Y3 → estimator/reason], and [Y4 → estimator/reason]. Across models, the estimand remains [association/within-unit change/between-unit difference], and inference accounts for [panel dependence].

**来源**: Kashmiri, Nicol, and Arora (2017), JAMS（pooled OLS、RE negative binomial、fractional logit、RE logistic 对应四类 outcome）。

**诚实边界**:
- “IV 时间不变”只解释 FE 无法估计该系数，不自动证明 RE 独立性；应报告 correlated RE/Mundlak、Hausman 诊断或更谨慎的关联性措辞。
- 多个估计器不能自动生成可比较的 effect size；跨结果比较应转到预测概率、标准化变化或清晰的结果专属尺度。
- 某比例只在分母大于零时定义时，必须报告零分母观测的处理及由此产生的样本选择。

---

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| `We use Weibull because it is common.` | 无统计论证，仅诉诸惯例 | `We compare Exponential, Log-normal, Log-logistic, and Weibull; Weibull offers the best fit based on BIC (Table X).` |
| `The model fits well.` | 无比较基准 | `The Weibull specification has the lowest BIC (706.89), outperforming the next-best alternative by [margin].` |
| `We tried several models and picked the best one.` | 显得数据挖掘 | `To overcome misspecification bias, we compare [candidates]; [winner] offers the best fit based on [criterion].` |
| `We used OLS, negative binomial, fractional logit, and logit as appropriate.` | 只报模型名称，未连接每个 DV 的测量属性与 estimand | 逐结果给出 `measurement property → estimator → interpretation scale` 路由表 |
