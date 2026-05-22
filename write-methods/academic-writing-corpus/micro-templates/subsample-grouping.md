---
category: subsample-grouping
description: 子样本分组与平行方程叙述句法——描述如何将样本按类型/方程分别估计，以及多方程并行呈现的结构。
function: 导航性/对齐性——让读者理解为什么需要分组估计或平行方程
slots: M4, M5, M7
extracted_from: singh2023_jmr / mayo2023_poms
created: 2026-05-22
updated: 2026-05-22
---

# 子样本分组与平行方程（Subsample Grouping）

## 设计原则

当论文需要按类型分别估计（如 voluntary/mandatory recalls, low/high discretion, inattentive/silence）或并行报告多个方程时，Methods 需要清晰的**分组逻辑声明**和**方程间关系说明**。这类句法避免读者误以为结果是不同样本的拼凑。

---

## 类型 1：子样本分组总起句

**功能**：说明为什么要将样本分组估计。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `We estimate separate models for [category A] and [category B] because [theoretical reason: e.g., the decision-making process differs across entity types].` | 安全 | M7 |
| `Because [theory] suggests that [mechanism] operates differently for [category A] versus [category B], we estimate [model] separately for each [category].` | 安全 | M7 |
| `We split the sample by [moderator] into [category A] and [category B] to test whether [relationship] differs across [categories].` | 安全 | M5 |
| `To evaluate [hypothesis], we create subgroups of the full model delineating [category A] and [category B].` | 安全 | M7 |

---

## 类型 2：分组比较逻辑句

**功能**：说明如何在分组之间比较系数。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `We compare the size and significance of the [coefficient] for [columns] using a [Wald chi-square test] to determine whether [relationship] differs across [categories].` | 安全 | M7 |
| `Column [x] duplicates column [y] for ease of model comparison.` | 安全 | M7（表格导航） |
| `The coefficient for [variable] in column [x] is statistically different from and [greater/less] in magnitude than the coefficient in column [y] (Wald chi-square test p < [threshold]).` | 安全 | M7 |

---

## 类型 3：平行方程总起句

**功能**：说明为什么需要同时估计多个方程。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `We estimate [model] for [outcome A] and [outcome B] because [theoretical reason: e.g., the two outcomes are determined by different decision-makers].` | 安全 | M7 |
| `The [model] specification for [entity A] is as follows: [equation]. The specification for [entity B] is: [equation].` | 安全 | M7 |
| `We represent [theoretical relationship] with a set of equations (for ease of presentation, we do not include control variables): [equation system].` | 安全 | M7 |

---

## 类型 4：方程间关系说明句

**功能**：解释平行方程之间的逻辑联系。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `[Equation x] captures the [effect] of [predictor] on [outcome A]; [equation y] captures the [effect] on [outcome B].` | 安全 | M7 |
| `[Equation x] represents the moderating effect of [moderator 1]; [equation y] represents the moderating effect of [moderator 2].` | 安全 | M7 |
| `[Equation z] models the relationship between [moderator 1] and [mediator].` | 安全 | M7 |
| `Finally, [equation w] represents the full system with both moderators and the mediator.` | 安全 | M7 |

---

## 类型 5：间接调节检验逻辑句

**功能**：在间接调节（mediated moderation）设计中说明检验步骤。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `We test for [indirect moderation / mediated moderation] through [mediator] according to whether: (1) [moderator 1] functions as a moderator when [mediator] is not considered (β₁₃ ≠ 0); (2) [moderator 1] influences [mediator] (β₃₁ ≠ 0); (3) [mediator] moderates the effect of [predictor] on [outcome] (β₄₅ ≠ 0); and (4) the coefficient on the original interaction term in the full system (β₄₃) indicates [full/partial] indirect moderation.` | 安全 | M7 |
| `β₄₃ = 0 indicates full indirect moderation; β₄₃ ≠ 0 and |β₄₃| < |β₁₃| indicates partial indirect moderation.` | 安全 | M7 |

---

## 类型 6：Model-Free Evidence 前置句

**功能**：在进入正式模型前，用无模型证据展示基本模式。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `We begin by presenting model-free evidence for the relationship between [predictor] and [outcome].` | 安全 | M1/M7/M8 |
| `We split the sample into [low] and [high] groups based on [threshold] and compare [outcome] across groups.` | 安全 | M7/M8 |
| `A [t-test] (M_high = [value], M_low = [value], p < [threshold]) suggests that [pattern], representing model-free evidence of [relationship].` | 安全 | M7/M8 |
| `The pattern in [figure] suggests a relationship between [predictor] and [outcome].` | 安全 | M7/M8 |

---

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| `We ran separate models.` | 未说明为什么需要分组 | `We estimate separate models for voluntary and mandatory recalls because the decision-making processes differ: firms choose voluntary recalls, whereas regulators choose mandatory recalls.` |
| `The results for both groups are shown in Table X.` | 未说明组间比较方法 | `We compare the lobbying coefficients across voluntary and mandatory equations using a Wald test to assess whether the effect differs by recall type.` |
| `We look at high and low discretion separately.` | 未说明分组标准 | `We classify recalls as low discretion (mentioned in 10-K) or high discretion (not mentioned) and estimate hazard models separately for each subgroup.` |
