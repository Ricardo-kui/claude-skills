<!-- write-methods 槽位骨架 M4：由 SKILL.md「槽位骨架加载」按路由决策加载。内容为原 SKILL.md 该槽位段落骨架（通用 + 设计类型变体 + QC），未做语义修改。 -->

### M4. 自变量 / 核心预测变量

**通用填空段落（每预测变量一段）**：

```text
Our focal independent variable, [predictor name], is measured as [operation] based on [source/timing]. This variable corresponds to Hypothesis [x] because it captures [mechanism]. We present the focal variables in the order of the theory: [predictor A], [predictor B], and [moderator].
```

**自然实验/处理变量变体**：
```text
The treatment indicator equals one for [unit-years/participants] exposed to [event/condition] and zero otherwise. [Treatment] equals 1 for [unit-years] after [policy/event] becomes effective in [jurisdiction/group], and 0 otherwise.
```

**处理分配稳定性补充**（DiD 可选）： 🔬 EXPERIMENTAL（2-3 篇范文）⚠️ 保守替代：省略此段
```text
During our sample period, [percentage] of [units] changed their [treatment-relevant characteristic, e.g., headquarters location]. We use [historical/fixed] [characteristic] information to maintain consistent treatment assignment.
```

**竞争机制预测变量变体**（机制测试中分解核心构念时）： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M4 段落
```text
To test how [actors] resolve [uncertainty], we decompose [core construct] into [N] subgroups based on [criterion]: [variable 1], [variable 2], [variable 3], and [variable 4]. We restrict the mechanism test subsample to [criteria] to ensure sufficient variation across the subgroups. These variables correspond to [RQ/Prediction x] because they distinguish [mechanism A] versus [mechanism B].
```

**实验操纵变体**：
```text
To manipulate [construct], participants were shown/told [condition-specific cue], while [other information] was held constant.
```

**网络/组合/配对构念变体**：
```text
We define [focal construct] as occurring when [actor] simultaneously holds/links/participates in [two or more related units]. The pair-level measure captures [shared influence/exposure] between the focal unit and each same-category peer. The numerator sums [shared holdings/links/exposure]; the denominator adds [non-focal holdings/relationships] so the measure reflects [focal actor influence] relative to [other actors]. We aggregate the pair-level measure across all same-category peers to form a continuous focal-unit measure. We require [minimum stake/link/intensity] so that the focal actor has sufficient incentive and ability to influence [unit].
```

**同伴效应/网络效应变体**：
```text
Our focal independent variable, [network-based construct], is defined using [network boundary: same industry / same board / same supply chain / geographic proximity]. We calculate [focal exposure] as the [average / weighted average] of [peer outcome/characteristic] among [peers], excluding the focal unit. Formally, [network variable]_{i,t} = Σ_{j≠i} [weight]_{ij,t} × [peer characteristic]_{j,t} / Σ_{j≠i} [weight]_{ij,t}. Because peer outcomes may reflect common shocks rather than true influence, we instrument [network variable] with [instrument: lagged peer characteristic / network from different layer / exogenous network formation] and report falsification tests in M8.
```

**构造暴露/指数变体**（用于堆叠扩散或媒体暴露）：
```text
We construct [focal exposure] from [raw trace] by [aggregation rule]. The measure equals [formula: count / proportion / intensity] of [event/type] per [unit-time]. To account for [scale differences / coverage variation], we normalize by [denominator]. We require [minimum threshold] to ensure that [spurious zeros / noise] do not drive the results.
```

**文本构念预测变量变体**（当预测变量来自文本分析，如 earnings calls、10-K、媒体、访谈时）：
```text
Our focal independent variable, [predictor name], is derived from [text source, e.g., earnings call transcripts / 10-K filings / media coverage] using [method: LIWC dictionary / custom dictionary / machine-learning classifier]. We chose this source because [theoretical reason for text reflecting construct]. The dictionary includes [N] words/phrases capturing [theoretical dimension], validated by [human coding / prior literature / expert review]. To ensure convergent validity, we correlate the text-based measure with [alternative measure, e.g., survey / archival proxy]; the correlation is [value] (p [relation] [threshold]), supporting construct validity. We standardize the text score to mean zero and standard deviation one to facilitate coefficient interpretation. Because text-based measures may capture noise unrelated to [construct], we control for [general text characteristics: length / sentiment / formality] in all specifications.
```

**同时方程变体**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M7 段落
```text
Equation [x] predicts [primary outcome] as a function of [focal predictor], [mechanisms], [moderators], interactions, and controls. Equations [y–z] model [mediator A] and [mediator B], allowing us to test whether [focal predictor] affects the mechanisms implied by the theory. Equation [w] predicts [downstream outcome] using [focal outcome], [focal predictor], their interaction, and value-relevant controls. We include an additional equation for [potentially endogenous choice] to account for the possibility that [anticipated need/reverse path] influences [focal predictor].
```

> **M4 段落级体裁 QC**（审计体裁）:
> - **Hypothesis anchor 强制**：每段含 "corresponds to Hypothesis [x]" 或等效锚点；无锚点的预测变量段是 audit-genre 的 orphaned claim
> - **理论顺序优先**：变量段排列按 Theory 假设顺序，不按字母序或表格列序；与既有"变量按理论顺序排列"检查互补（那是 Completeness，这是段间 sequence）
