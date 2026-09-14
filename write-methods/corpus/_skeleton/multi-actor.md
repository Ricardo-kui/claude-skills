# multi-actor — 二级骨架清单（多行为者设计）

> 本目录由脚本重建，手改会被覆盖；重建命令 = `python scripts/build_indices.py`（路径基准：以本 skill 目录（SKILL.md 所在目录）为基准）。
> **抽取规则（先定后抽）**：verbatim = 卡片 `**原始句锚点**` / `[原始句锚点]` / `- **原始句锚点**（…）` 内带引号/缩进的完整英文原句（有明确来源论文，逐字保留、含 `…` 不回填）+ `**原文锚定**`/`**原文锚点**`（含 `- **原文锚定**` 子弹式）下 `- "..."` 英文句（id 后缀 .a/.b）；模板 = `**骨架**` / `**模板**` / `**模板/骨架**` / `**结构**` / `[骨架]` 块、代码围栏或紧随裸英文段内带 `[槽位]` 的填槽骨架。
> **citekey** 优先取卡片尾部 `<!-- wb:... -->` 标记，无则回退 `**来源论文**`/`**来源**`/裸 `来源：`/`- **出处**` 原文；EXTEND 子变体回退 `- **原文锚定**` 尾部 `（citekey, …）` 标注；皆无标 `未标注`（不编造）。**适配槽位** 取 `**槽位**`/`[适用槽位]` 字段内 M1–M10（含 M2.5）与 Q1–Q8（去重排序）；无字段或含 `M?` 标 `通用`。
> **锚点** = `corpus/<文件名>#变体-<变体号>`（脚本自定义片段，指向 `### 变体 <N>` 标题；不编号/EXTEND 变体指向其真实 `### 变体：`/`#### 变体：` 标题；`--verify` 断言标题存在）。
> 状态列：`verbatim` = 逐字底本（与源卡片逐字一致，不得改写/拼接/补全）；`模板` = 填槽骨架（不可当逐字底本引用）。`不编号变体`（fang2025 POM，不计入 342）与 `EXTEND子变体`（`####` 层，不计入 342）在 id 与状态列标注。

条目：verbatim 2 条 / 模板 3 条。

## Verbatim 底本

| id | 适配槽位 | citekey | 句子原文（或模板） | 卡片路径#锚点 | 状态 |
|---|---|---|---|---|---|
| `multi-actor#1` | M2/M6 | Cui, Yang & Vertinsky (Strategic Management Journal) | In cases where an alliance includes more than two firms, we split the alliance into a set of dyads. Empirically, this may result in a confounding effect with structural embeddedness (i.e., number of common ties). | `corpus/多行为者设计.md#变体-1` | verbatim |
| `multi-actor#2` | M8 | westphal_bednar_2005_asq | Thus we calculated the $r_{wg}$ index, a measure of within-group agreement, as well as the intraclass correlation coefficient (ICC), which estimates the proportion of total variance that can be explained by group membership. | `corpus/多行为者设计.md#变体-2` | verbatim |

## 填槽模板

| id | 适配槽位 | citekey | 句子原文（或模板） | 卡片路径#锚点 | 状态 |
|---|---|---|---|---|---|
| `multi-actor#T1` | M2/M6 | Cui, Yang & Vertinsky (Strategic Management Journal) | In cases where a [relationship] includes more than two [actors], we split the [relationship] into a set of [dyads]. Empirically, this may result in a confounding effect with [other_variable]. We parceled out the possible confounding effect caused by [multiparty_relationships] by including a control variable ([Variable]) that measures [definition]. We also ran the models using a sample excluding [multiparty_relationships]; the results are robust. | `corpus/多行为者设计.md#变体-1` | 模板 |
| `multi-actor#T2` | M8 | westphal_bednar_2005_asq | Although [construct] is typically defined at the [group] level, [our theoretical perspective suggests that the biases/perceptions of individual members are interdependent: if others are less biased than a focal person about [X], then they should [behavior], thus lessening the focal person's bias]. Thus we would expect limited variance within [groups] in [individual-level variable of interest]. In this respect, the relationship between [construct] and individual-level perceptions is a kind of consensus composition model ([Chan, 1998]). Thus we calculated the [r_wg] index, a measure of within-group agreement, as well as the [intraclass correlation coefficient (ICC)], which estimates the proportion of total variance that can be explained by [group] membership. The [r_wg] index was [value] for [variable], well above the [.70] threshold commonly used to justify aggregation ([George, 1990]). [When using the ICC procedure,] a significant F-test is commonly used to justify the aggregation of data to the [group] level ([Klein et al., 2001]). These results support our theoretical expectations and suggest that within-[group] variance in [perceptions] is sufficiently small to warrant aggregation to the [group] level. | `corpus/多行为者设计.md#变体-2` | 模板 |
| `multi-actor#T3` | 通用 | carpenter_and_westphal_2001_strategic_context_of_external_ne | [同构计算] To test these hypotheses, we developed a set of aggregate variables for [the construct] across all [members] on a [group]; for analyses conducted at the level of the [individual], the variables were calculated for the particular [individual]. [等价声明] In our measures of [the construct], [subgroups within units] were combined, as separate analyses revealed no significant differences in results when we distinguished between [them]. [口径注] (note that this [group]-level measure excludes duplicate [ties to the same counterpart]) | `corpus/多行为者设计.md#变体-3` | 模板 |
