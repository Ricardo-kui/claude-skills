---
category: opening-anchors
description: 段首锚定短语——段落的第一个（或前几个）句子，明确告知读者本段的功能定位。
function: 导航性——读者只读段首句即可判断本段在做什么说服动作
slots: M1-M10
extracted_from: 21 design-type corpus files
created: 2026-05-22
updated: 2026-05-22
---

# 段首锚定短语（Opening Anchors）

## 使用说明

每个 Methods 段落应以单一功能开头。以下按槽位和说服动作分类，提供可替换的段首句式。

## M1 — 研究情境合法性论证

| 锚定句式 | 来源频率 | 设计类型 | 风险 |
|---------|---------|---------|------|
| `[Empirical setting] provides an appropriate context for examining [theoretical relationship] for [N] reasons.` | 高 (28/28) | 通用 | 安全 |
| `We examine [phenomenon] using [policy/event/institutional change] that altered [exposure] across [units] and time.` | 高 (5-8/28) | 自然实验/DiD | 安全 |
| `We test [theoretical claim] using a [laboratory/field/online] experiment.` | 中 (5-6/28) | 实验 | 安全 |
| `Our conceptual framework links [driver], [mechanisms], [outcome], and [downstream outcome].` | 低 (1-2/28) | 同时方程/SEM | 安全 |
| `Across [N] studies, we use complementary designs to test [theory] and address [validity concerns].` | 低 (1-2/28) | 多研究 | 安全 |

## M2 — 样本漏斗可审计性

| 锚定句式 | 来源频率 | 设计类型 | 风险 |
|---------|---------|---------|------|
| `We began with [starting population] from [source] over [period].` | 高 (28/28) | 通用 | 安全 |
| `Our primary sample consists of [units] observed from [period], drawn from [source] because it tracks [activity].` | 高 (5-8/28) | 自然实验/DiD | 安全 |
| `Because [outcome] is rare, a simple random sample would yield too few [cases] for meaningful analysis; we therefore used [sampling strategy].` | 低 (1-2/28) | 稀有结果 | 安全 |
| `No authoritative database exists for [empirical object], so we constructed the dataset from [trace/source].` | 低 (2-3/28) | 实证对象构建 | 安全 |
| `The intersection of these datasets resulted in a sample of [N] [phenomenon] across [N] firms from [year_start] to [year_end].` | 中 (3-4/28) | 面板数据 | 需注意：缺少逐层排除数字 |
| `We used a multisource, multimethod data collection approach to test our ideas.` | 低 (1-2/28) | 多源嵌套调查 | 安全 |

## M3 — 因变量操作化

| 锚定句式 | 来源频率 | 设计类型 | 风险 |
|---------|---------|---------|------|
| `Our dependent variable is [outcome construct], measured as [operational definition] using [source].` | 高 (28/28) | 通用 | 安全 |
| `Because the theory concerns both [positive actions] and mitigation of [negative actions], we construct [net outcome] from...` | 低 (1-2/28) | 面板数据 | 安全 |
| `We measure [market/stakeholder reaction] as [CAR/abnormal response] around [event], using [benchmark model]...` | 中 (3-4/28) | 事件研究 | 安全 |
| `We capture [outcome] behaviorally by [task/coding procedure], reducing reliance on self-reported intentions.` | 低 (3-4/28) | 实验 | 安全 |
| `Our dependent variable, [text-derived construct], is measured from [text source] using [method].` | 中 (3-4/28) | 文本构念 | 安全 |

## M4 — 自变量操作化

| 锚定句式 | 来源频率 | 设计类型 | 风险 |
|---------|---------|---------|------|
| `Our focal independent variable, [predictor name], is measured as [operation] based on [source/timing].` | 高 (28/28) | 通用 | 安全 |
| `The treatment indicator equals one for [unit-years/participants] exposed to [event/condition] and zero otherwise.` | 高 (5-8/28) | 自然实验/DiD | 安全 |
| `To test how [actors] resolve [uncertainty], we decompose [core construct] into [N] subgroups based on [criterion]...` | 低 (1-2/28) | 机制检验 | 安全 |
| `We define [focal construct] as occurring when [actor] simultaneously holds/links/participates in [two or more related units].` | 低 (1-2/28) | 网络/组合构念 | 安全 |
| `We construct [focal exposure] from [raw trace] by [aggregation rule].` | 低 (1-2/28) | 暴露/指数 | 安全 |
| `Our focal independent variable, [predictor name], is derived from [text source] using [method].` | 中 (2-3/28) | 文本构念 | 安全 |

## M5 — 调节/中介/机制变量

| 锚定句式 | 来源频率 | 设计类型 | 风险 |
|---------|---------|---------|------|
| `To capture [boundary/mechanism], we measure [moderator/mediator] as [operation].` | 高 (28/28) | 通用 | 安全 |
| `To capture the boundary condition of [moderator], we measure [moderator] using [classification].` | 低 (1-2/28) | 子样本分割 | 安全 |
| `To test the proposed mechanism, we decompose [predictor] by [actor type/horizon].` | 低 (1-2/28) | 机制分解 | 安全 |
| `We define [boundary condition] as contexts where [spillovers/externalities/stakeholder responses] are likely to be economically meaningful.` | 低 (1-2/28) | 边界条件 | 安全 |

## M6 — 控制变量与竞争性解释

| 锚定句式 | 来源频率 | 设计类型 | 风险 |
|---------|---------|---------|------|
| `We include controls for [threat family] because [alternative explanation].` | 高 (28/28) | 通用 | 安全 |
| `We included a broad set of control variables that influence [DV] directly and those that help address alternative explanations ([citation]).` | 中 (4/28) | 面板数据-OLS | 安全 |
| `Because some controls may be affected by [treatment], we first estimate a parsimonious model with fixed effects before adding controls.` | 中 (5-8/28) | 自然实验/DiD | 安全 |
| `For [equation/outcome family], we include controls that address [rival explanation].` | 低 (1-2/28) | 同时方程 | 安全 |
| `We control for [participant characteristics] because [rival explanation].` | 中 (3-4/28) | 实验 | 安全 |

## M7 — 模型规格与估计方法

| 锚定句式 | 来源频率 | 设计类型 | 风险 |
|---------|---------|---------|------|
| `Because [dependent variable] is [continuous/binary/ordinal/count/censored/time-to-event], we estimate [model].` | 高 (28/28) | 通用 | 安全 |
| `We employ [unit] fixed effects rather than random effects because the Hausman test rejects...` | 中 (15+/28) | 面板数据 | 安全 |
| `We estimate a difference-in-differences model in which [outcome] is regressed on [treatment]...` | 高 (5-8/28) | 自然实验/DiD | 安全 |
| `Because the shape of [event timing] is not known ex ante, we compare [candidate distributions] and select [distribution] based on [fit criterion].` | 低 (2-3/28) | 生存分析 | 安全 |
| `Because [dependent variable] is persistent and our panel is [short], fixed-effects estimation may be biased (Nickell bias).` | 低 (1-2/28) | 动态面板 | 安全 |

## M8 — 识别策略/效度/诊断检验

| 锚定句式 | 来源频率 | 设计类型 | 风险 |
|---------|---------|---------|------|
| `To address concerns about [threat], we [design feature/test].` | 高 (28/28) | 通用 | 安全 |
| `Our identification strategy relies on [source of variation].` | 高 (5-8/28) | 自然实验/DiD | 安全 |
| `To assess the [manipulation] manipulation, participants rated [check item].` | 中 (3-4/28) | 实验 | 安全 |
| `A threat to our IV strategy is that [instrument] may affect [outcome] through channels other than [endogenous predictor].` | 中 (3-4/28) | IV-2SLS | 安全 |
| `Because [network-based construct] may capture common shocks or sorting rather than true peer influence, we conduct falsification tests.` | 低 (1/28) | 同伴效应 | 安全 |

## M9 — 多研究过渡

| 锚定句式 | 来源频率 | 设计类型 | 风险 |
|---------|---------|---------|------|
| `Study [x] tests [hypothesis/effect] using [sample/design].` | 中 (2-3/28) | 多研究 | 安全 |
| `In Study [x], we sought to test [hypotheses] and address [limitation/gap] from [prior study/evidence].` | 低 (1-2/28) | 多研究 | 安全 |
| `Although Study [x] addresses [issue], it cannot establish [remaining need]. Study [x+1] therefore [design upgrade].` | 低 (1-2/28) | 多研究 | 安全 |

## M10 — Methods→Results 过渡

| 锚定句式 | 来源频率 | 设计类型 | 风险 |
|---------|---------|---------|------|
| `The Results section first reports [main tests] and then examines [validity/robustness checks].` | 高 (28/28 中 <10% 出现） | 通用 | 安全 |

---

## 跨槽位通用锚定（备用）

当上述槽位专用锚定不适用时，可使用以下通用功能声明句式：

| 说服动作 | 锚定句式 | 适用槽位 |
|---------|---------|---------|
| 合法性论证 | `[Setting/context] is well suited because [reason].` | M1 |
| 可审计性 | `The data construction proceeded as follows.` | M2, M3, M4 |
| 对齐性 | `This operationalization aligns with [theory/construct] because [logic].` | M3, M4, M5 |
| 抗辩性 | `A potential concern is that [rival explanation].` | M6, M8 |
| 可信性 | `Identification comes from [source of variation].` | M7, M8 |
| 导航性 | `Below, we first describe [procedure], then [next step].` | M9, M10 |
