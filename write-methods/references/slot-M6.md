<!-- write-methods 槽位骨架 M6：由 SKILL.md「槽位骨架加载」按路由决策加载。内容为原 SKILL.md 该槽位段落骨架（通用 + 设计类型变体 + QC），未做语义修改。 -->

### M6. 控制变量与竞争性解释

**通用填空段落**：

```text
We include controls for [threat family 1] because [alternative explanation 1]. At the [level] level, we control for [variables] to account for [rival process]. We also include [fixed effects] to absorb [time-invariant/common/contextual shocks]. All time-varying predictors are measured at [lag/timing] to preserve temporal ordering. We lag the control variables by [period] to reduce simultaneity concerns.
```

**自然实验/Bad Control 变体**： ✓ STANDARD（5-8 篇自然实验/DiD 范文复现）
```text
Because some controls may be affected by [treatment], we first estimate a parsimonious model with fixed effects before adding controls. We do not include [variable] because it may be post-treatment / mechanically related to [outcome].
```

**同时方程/方程特定控制变体**： 🔬 EXPERIMENTAL（1-2 篇范文）⚠️ 保守替代：通用 M6 段落
```text
For [equation/outcome family], we include controls that address [rival explanation]. For [mediator equation], we further control for [industry benchmark] because firms may align [decision] with industry norms. In the [downstream outcome] equation, we control for [profitability], [growth], and [market position] because each may independently affect [value outcome]. In the [financial choice] equation, we include known determinants such as [industry norm], [asset structure], [firm size], and [profitability].
```

**实验变体**：
```text
We control for [participant characteristics] because [rival explanation]. Random assignment allows us to isolate the effect of [manipulation] on [outcome] within the experimental context.
```

**竞争焦点互控变体**（Haunschild et al. 2015 ORSC 模式）： 🔬 EXPERIMENTAL（1 篇范文）⚠️ 保守替代：通用 M6 段落
```text
The analysis controls for potential sources of heterogeneity across observations that might influence both the independent and dependent variables. In models estimating [DV1], we controlled for [DV2]; conversely, in models estimating [DV2], we controlled for [DV1]. This allows us to examine whether [focal IV] influences [DV1] and [DV2] net of each other, rather than merely reflecting [alternative explanation: e.g., a common third variable driving both foci]. To ensure that findings were not driven by collinearity involving the respective variables, we also ran models dropping the alternative focus from the equation.
```

**表格化控制变量 + 每行 Rationale + Data source 变体**（Li et al. 2025 JSCM 型）： 🔬 EXPERIMENTAL（1 篇范文）— 当控制变量 ≥10 且各对应不同竞争解释、各来自不同数据库时尤为有效
```text
This study controlled for [event / recall], [focal-actor firm], and [relationship] characteristics that may covary with the independent variables and affect [decision-makers]' reactions to [event] (summarized in Table [N]).

[Table format — 四列：Variable | Measure | Rationale for inclusion | Data source；行按特征族分组，如：
  - Recall characteristics: recall volume / source of recall / OEM firm value loss
  - Focal-actor (supplier) characteristics: firm size / financial leverage / book-to-market / ROE / institutional ownership / responsibility / media sentiment / number of customers
  - Relationship characteristics: relationship tenure / vertical relatedness / geographic distance]

First, [event/recall] characteristics are key determinants of [decision-makers' perception] of the [event] impact ([citation]). This study included [N] such characteristics: (1) [variable 1], measured by [operation]; (2) [variable 2], [operation]; (3) [variable 3], [operation]. Second, this study included [M] [focal-actor] characteristics that affect [evaluation]: [list]. Third, this study controlled for [relationship] characteristics that might affect [main effect] and the independent variable simultaneously, including [list].
```
**关键特征**:
- **表格强制每个控制变量都配一行 Rationale + Data source**——把"为什么控制这个"（指向具体竞争解释/替代机制）和"数据从哪来"一次性可见化，审稿人可逐行核验每个控制是否对应一个真实的 rival explanation
- **按特征族分组行**（event / focal-actor / relationship）——控制变量按理论相关性聚类，而非随机罗列；分组本身显示作者对 confounding 结构的系统性思考
- **表格 + 文字双重呈现**——表格给全貌与可追溯性，正文按族复述关键控制并给文献支撑（citation 锚定 rationale）
- **每行 Data source 与 M2 数据来源一一对应**——多数据库合并研究中，表格让每个变量的来源可追溯，降低"数据从哪来"的审稿质疑

**适用**: 控制变量较多（≥10）、每个对应不同竞争解释的实证研究；多数据库合并的研究（每个控制 data source 不同）；event study / 二手面板数据研究（JSCM/JOM/MSOM/MS 风格）

**禁忌**:
- Rationale 列不能只写泛泛的 "affects DV"——必须指向具体的竞争解释或替代机制（如 "Massive recalls are more likely to be penalized by the stock market"）
- 不要用表格**替代**正文的理论论证——表格是索引与可追溯性，正文仍需对关键控制给文献支撑
- Data source 列必须与 M2 数据来源描述一致，不可出现表格未在 M2 交代的新数据源
- 若某控制无法写出有意义的 Rationale，说明它可能是 bad control / post-treatment——应删除而非硬塞进表
