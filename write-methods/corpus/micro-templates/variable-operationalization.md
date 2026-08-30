---
category: variable-operationalization
description: 变量操作化句式——构念→测量→来源→方向的表述方式。
function: 对齐性——建立 Theory 构念与 Methods 测量之间的映射
slots: M3, M4, M5
extracted_from: 21 design-type corpus files
created: 2026-05-22
updated: 2026-05-22
---

# 变量操作化句式（Variable Operationalization）

## 核心原则

每个变量的操作化段落要完成一个**四步论证**：
1. 构念声明（这是什么概念）
2. 操作化定义（如何测量）
3. 数据来源（从哪来）
4. 方向解释（高值/低值意味着什么）

## 标准句式

### 因变量（M3）

| 微模板 | 来源频率 | 风险 |
|--------|---------|------|
| `Our dependent variable is [outcome construct], measured as [operational definition] using [source].` | 高 (28/28) | 安全 |
| `This measure captures [construct] because [construct-validity logic].` | 高 (28/28) | 安全 |
| `Higher values indicate [interpretation direction].` | 高 (28/28) | 安全 |
| `Because [outcome] is [continuous/binary/ordinal/count/censored/time-to-event], we use [model] and interpret [coefficients/marginal effects/hazards/probabilities].` | 高 (28/28) | 安全 |

### 自变量（M4）

| 微模板 | 来源频率 | 风险 |
|--------|---------|------|
| `Our focal independent variable, [predictor name], is measured as [operation] based on [source/timing].` | 高 (28/28) | 安全 |
| `This variable corresponds to Hypothesis [x] because it captures [mechanism].` | 高 (28/28) | 安全 |
| `We present the focal variables in the order of the theory: [predictor A], [predictor B], and [moderator].` | 中 (15+/28) | 安全 |
| `The treatment indicator equals one for [unit-years/participants] exposed to [event/condition] and zero otherwise.` | 高 (5-8/28) | 安全 |

### 调节/中介变量（M5）

| 微模板 | 来源频率 | 风险 |
|--------|---------|------|
| `To capture [boundary/mechanism], we measure [moderator/mediator] as [operation].` | 高 (28/28) | 安全 |
| `We interact [predictor] with [moderator] to test whether [relationship] is stronger/weaker under [condition].` | 高 (28/28) | 安全 |
| `To test the proposed mechanism, we measured [mediator] and included [alternative mechanisms] as rival explanations.` | 中 (5-8/28) | 安全 |

---

## 特殊构念的操作化句式

### 文本构念测量

| 微模板 | 功能 | 风险 |
|--------|------|------|
| `Our dependent variable, [text-derived construct], is measured from [text source] using [method].` | 声明来源和方法 | 安全 |
| `We first [preprocessing: remove stop words / stem / lemmatize].` | 预处理步骤 | 安全 |
| `We then [measurement step: count semantic similarity / topic proportion].` | 测量步骤 | 安全 |
| `To validate the measure, we correlate it with [external benchmark]; the correlation is [value] (p [relation] [threshold]).` | 效度检验 | 安全 |
| `We also inspect [example excerpts] to confirm face validity.` | 表面效度 | 安全 |

### 网络/组合构念

| 微模板 | 功能 | 风险 |
|--------|------|------|
| `We define [focal construct] as occurring when [actor] simultaneously holds/links/participates in [two or more related units].` | 定义 | 安全 |
| `The pair-level measure captures [shared influence] between the focal unit and each same-category peer.` | 配对测量 | 安全 |
| `We aggregate the pair-level measure across all same-category peers to form a continuous focal-unit measure.` | 聚合 | 安全 |

### 行为编码构念

| 微模板 | 功能 | 风险 |
|--------|------|------|
| `We capture [outcome] behaviorally by [task/coding procedure], reducing reliance on self-reported intentions.` | 行为测量 | 安全 |
| `Blind coders rated [behavior] on [scale].` | 编码过程 | 安全 |
| `We averaged ratings because interrater reliability was [acceptable statistic].` | 信度检验 | 安全 |

---

## 方向解释的多样性

不要让所有变量都用 "Higher values indicate..." 结尾。以下为替代句式：

| 原始 | 替代 |
|------|------|
| `Higher values indicate greater [construct].` | `The measure ranges from [min] to [max], with higher values reflecting [state].` |
| `Higher values indicate greater [construct].` | `We reverse-coded [item] so that higher values consistently indicate [state].` |
| `Higher values indicate greater [construct].` | `The variable is coded as 1 if [condition] and 0 otherwise, capturing [binary state].` |
| `Higher values indicate greater [construct].` | `The index sums [N] items; each item is coded [scheme].` |

---

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| `X is measured as Y.`（单句） | 缺少构念效度和方向 | 扩展为四步论证 |
| `The data come from Compustat.` | 信息不足 | `...from Compustat North America, which reports [relevant items] for [population].` |
| `High values mean good.` | 口语化 | `Higher values indicate more favorable [construct] outcomes.` |
| 变量定义与 Results 表格不一致 | 跨 section 断裂 | 确保 Methods 中的变量名、测量方式与 Results 表格完全一致 |
