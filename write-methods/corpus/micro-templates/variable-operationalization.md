---
category: variable-operationalization
description: 变量操作化句式——构念→测量→来源→方向的表述方式。
function: 对齐性——建立 Theory 构念与 Methods 测量之间的映射
slots: M3, M4, M5
extracted_from: 21 design-type corpus files
created: 2026-05-22
updated: 2026-09-23
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


### 档案字段测量构造（M6）

从监管公告页等档案文档字段构造控制变量时，逐条声明**可审计构造规则**，不让读者猜字段如何变成变量：

| 微模板 | 功能 | 风险 |
|--------|------|------|
| `[Source] provides two [fields] on the [announcement] page: [field A] and [field B].` | 声明来源文档的字段结构 | 安全 |
| `[Field A] is when [the unit first entered]. If there are multiple [variants] with different [Field A values], we adopted the [earliest].` | 并列/多值时的 tie-breaking 规则 | 安全 |
| `We then calculated the [difference between field A and field B] to measure [how many days had passed].` | 字段→变量的计算式 | 安全 |
| `A set of [category] dummies following [the regulator's] categorization are included: [D1] for [...], ..., [Dk] for [...]. [Remaining categories] are classified in the holdout (base) category.` | 类别固定效应 + 基准组显式声明 | 安全 |
| `These [category] fixed effects control for the different natures of [units] that could influence [DV]. Such differences could be caused by factors like [factor 1] and [factor 2].` | 基准组之后的实质 because（类别差异的两个具体来源） | 安全 |

反模式：只写 `[X] is the logged number of days...` 而不声明 tie-breaking 规则——多值字段下的构造不可复现；类别 dummy 列了各档却不声明哪档是基准组——系数解释失去参照。

<!-- wb:liuliuluo2016:m6_archival_field_measurement_construction_rules -->
<!-- wb-meta: gap=Incompleteness status=EMERGING -->


### 滞后存量构造（M4：carryover 修正）

解释变量具有跨期延续效应时，当年流量口径可用有限分布滞后存量一句话修正，并以外部基准校验高零占比：

| 微模板 | 功能 | 风险 |
|--------|------|------|
| `As [the predictor] has carryover effects ([citation]), we use a finite distributed lag model to compute [the predictor] stock, with earlier years of [activity] receiving a lower weight.` | 存量构造的存在理由（carryover）+ 方法命名 | 安全 |
| `We use a decay parameter (δ) of [0.50]. Specifically, [the predictor] for year t is defined as the sum over k=t-[2] to k=t of δ^(t-k) [activity]_k ([estimator citation]), relative to [the scaling base] in year t ([scaling citation]).` | 衰减参数 + 求和定义式 + 规模化基准三件套 | 安全 |
| `We subsequently establish the sensitivity of results to alternative decay parameters.` | 衰减参数敏感性预告（一句话，Results 兑现） | 安全 |
| `The variable has a high incidence of zeros ([83.62]%) which is consistent with past research that most [population units] ([90]%) do not [engage in the activity] ([citation]).` | 零值占比外部基准校验——用总体统计量证明高零占比是现象属性而非测量缺陷 | 安全 |

反模式：只写"取存量"而不给衰减参数与求和窗——构造不可复现；零值密集的解释变量只描述零占比而不引外部基准——读者无法区分数据缺陷与现象稀疏。

<!-- wb:giannetti_2022_corporate_lobbying_and_product_recalls_an_inv:methods_m4_fdl_carryover_stock_zero_benchmark -->
<!-- wb-meta: gap=Incompleteness status=EMERGING -->


### 事件计数去重规则（M3：档案计数 DV）

以档案事件计数为 DV 时，同一事件的重复登记会让计数膨胀；用一条去重规则（附先例引用）封口：

| 微模板 | 功能 | 风险 |
|--------|------|------|
| `Building on past research ([citation]), to avoid overcounting [events], we only retain one [event] when a [unit] experiences more than one [event] with the same "[root-cause field]" on the same [day].` | 去重规则：同一单位 + 同一根因字段 + 同一时间戳 → 计一次，先例引用背书 | 安全 |

反模式：直接报告"事件总数"而不声明重复事件的处理规则——计数 DV 口径不可复现；去重所用字段（根因/类别/编号）必须来自数据源自带字段，不得事后主观归类。

<!-- wb:giannetti_2022_corporate_lobbying_and_product_recalls_an_inv:methods_m3_event_dedup_root_cause_rule -->
<!-- wb-meta: gap=Incompleteness status=EMERGING -->


### 调查补测控制变量构造（M6：专用小样本调查）

[功能标签]: M6 — 档案数据缺口的控制变量用独立小样本调查补测时的程序性辩护

[骨架]: "[N] [country]-based, '[panel_provider] approved participants' (approval rate >[threshold], <[max_studies] studies completed) participated in the study (M_age = [age], [pct]% female). To avoid fatigue, each participant only rated [k] different [objects]. Each [object] was rated by at least [m] participants. We asked participants [the control question]. The answer choices were '[option_1],' '[option_2],' and '[option_3].' [Because sentence linking control to outcome]."

[结构要点]: 四个可信度锚点一次给全——样本量与人口构成、质量控制门槛（approval rate / 完成研究数上限）、疲劳管理（每人评 k 个）、每个对象的最低评分人数下限；随后立即接 because 句把控制变量与 DV 的预期方向挂钩

[原文锚点]: "To avoid fatigue, each participant only rated 15 different products. Each product was rated by at least 100 participants."

[可迁移性]: 中 — 只在档案数据无法直接观测控制变量、需专门补测时使用

[范式排他性]: 中 — 服务于档案+调查混合设计，纯实验或纯档案设计不需要

[设计变体]: 构念为主变量时此模板扩为完整测量节；作控制变量时压缩为一段并保留 because 句

[区别于既有 variable-operationalization 条目]: 既有条目覆盖构念→测量→来源→方向句式与档案字段构造；本模板补"为控制变量专门发起小样本调查"的程序性辩护细节（疲劳管理+覆盖下限+质量门槛）

<!-- wb:raithel_2024_product_recall_effectiveness_and_consumers_part:m6_control_purpose_built_mini_survey -->
<!-- wb-meta: gap=Incompleteness status=EMERGING -->
