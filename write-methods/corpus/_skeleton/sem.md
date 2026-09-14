# sem — 二级骨架清单（SEM）

> 本目录由脚本重建，手改会被覆盖；重建命令 = `python scripts/build_indices.py`（路径基准：以本 skill 目录（SKILL.md 所在目录）为基准）。
> **抽取规则（先定后抽）**：verbatim = 卡片 `**原始句锚点**` / `[原始句锚点]` / `- **原始句锚点**（…）` 内带引号/缩进的完整英文原句（有明确来源论文，逐字保留、含 `…` 不回填）+ `**原文锚定**`/`**原文锚点**`（含 `- **原文锚定**` 子弹式）下 `- "..."` 英文句（id 后缀 .a/.b）；模板 = `**骨架**` / `**模板**` / `**模板/骨架**` / `**结构**` / `[骨架]` 块、代码围栏或紧随裸英文段内带 `[槽位]` 的填槽骨架。
> **citekey** 优先取卡片尾部 `<!-- wb:... -->` 标记，无则回退 `**来源论文**`/`**来源**`/裸 `来源：`/`- **出处**` 原文；EXTEND 子变体回退 `- **原文锚定**` 尾部 `（citekey, …）` 标注；皆无标 `未标注`（不编造）。**适配槽位** 取 `**槽位**`/`[适用槽位]` 字段内 M1–M10（含 M2.5）与 Q1–Q8（去重排序）；无字段或含 `M?` 标 `通用`。
> **锚点** = `corpus/<文件名>#变体-<变体号>`（脚本自定义片段，指向 `### 变体 <N>` 标题；不编号/EXTEND 变体指向其真实 `### 变体：`/`#### 变体：` 标题；`--verify` 断言标题存在）。
> 状态列：`verbatim` = 逐字底本（与源卡片逐字一致，不得改写/拼接/补全）；`模板` = 填槽骨架（不可当逐字底本引用）。`不编号变体`（fang2025 POM，不计入 342）与 `EXTEND子变体`（`####` 层，不计入 342）在 id 与状态列标注。

条目：verbatim 4 条 / 模板 4 条。

## Verbatim 底本

| id | 适配槽位 | citekey | 句子原文（或模板） | 卡片路径#锚点 | 状态 |
|---|---|---|---|---|---|
| `sem#1` | M7 | vadakkepatt2022 | We have multiple equations in which the errors across them can be correlated, so we estimate the equations jointly using a structural equation model approach with correlated errors. | `corpus/SEM.md#变体-1` | verbatim |
| `sem#2` | M8 | vadakkepatt2022 | Prior to specifying our models, we conducted panel Granger causality tests to examine whether lobbying Granger-causes customer satisfaction or vice versa. They reveal that lobbying Granger-causes customer satisfaction (χ² = 5.04, p < .10) and not the reverse. | `corpus/SEM.md#变体-2` | verbatim |
| `sem#3` | M7 | vadakkepatt2022 | In addition, to rule out multicollinearity concerns for the interaction terms (with r > .70), we residual-centered the interaction of lobbying with product market lobbying. | `corpus/SEM.md#变体-3` | verbatim |
| `sem#4` | M3/M4 | vadakkepatt2022 | Customer satisfaction, advertising spend, and R&D spend are widely used variables, so we do not detail their construction here, beyond the information provided in Table 2. Instead, we focus on the variables that require additional explanation or coding or are unique to our research. | `corpus/SEM.md#变体-4` | verbatim |

## 填槽模板

| id | 适配槽位 | citekey | 句子原文（或模板） | 卡片路径#锚点 | 状态 |
|---|---|---|---|---|---|
| `sem#T1` | M7 | vadakkepatt2022 | We estimate [N] systems of equations. The first (Equations [1], [2], and [4]) tests [Hypotheses_set_A], whereas the second system (Equations [1], [3], and [4]) tests [Hypotheses_set_B]. We have multiple equations in which the errors across them can be correlated, so we estimate the equations jointly using a structural equation model approach with correlated errors. Joint estimation across multiple equations yields more efficient estimates ([citation]), accounts for endogeneity due to common omitted variable bias ([citation]), and has been used to test mediation, moderation, and moderated mediation relationships in the presence of endogenous regressors ([citations]). | `corpus/SEM.md#变体-1` | 模板 |
| `sem#T2` | M8 | vadakkepatt2022 | Prior to specifying our models, we conducted panel Granger causality tests to examine whether [IV] Granger-causes [DV] or vice versa. They reveal that [IV] Granger-causes [DV] (χ² = [value], p < [threshold]) and not the reverse. Next, we examine independent variable stationarity with panel unit root tests. A lack of stationarity dictates how the variables enter the model. The [test_name] rejects the null hypothesis that the variables contain unit roots (p < [threshold]). We conclude the variable is mean-stationary and specify it in terms of levels. | `corpus/SEM.md#变体-2` | 模板 |
| `sem#T3` | M7 | vadakkepatt2022 | To rule out multicollinearity concerns for the interaction terms (with r > [threshold]), we residual-centered the interaction of [IV] with [moderator]. Residual centering has been shown to reduce multicollinearity between an interaction term and its first-order effect term, to provide stable and unbiased results ([citation]), and has been used in recent literature ([citations]). | `corpus/SEM.md#变体-3` | 模板 |
| `sem#T4` | M3/M4 | vadakkepatt2022 | Table [X] details the variables, operationalizations, references, and data sources. [Well-known variables A, B, C] are widely used, so we focus on variables that require additional explanation or coding. First, [unique_variable_1: operationalization + source + justification]. Second, [unique_variable_2: coding procedure + interrater reliability]. Third, [unique_variable_3]. | `corpus/SEM.md#变体-4` | 模板 |
