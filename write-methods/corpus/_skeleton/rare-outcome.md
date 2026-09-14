# rare-outcome — 二级骨架清单（稀有结果）

> 本目录由脚本重建，手改会被覆盖；重建命令 = `python scripts/build_indices.py`（路径基准：以本 skill 目录（SKILL.md 所在目录）为基准）。
> **抽取规则（先定后抽）**：verbatim = 卡片 `**原始句锚点**` / `[原始句锚点]` / `- **原始句锚点**（…）` 内带引号/缩进的完整英文原句（有明确来源论文，逐字保留、含 `…` 不回填）+ `**原文锚定**`/`**原文锚点**`（含 `- **原文锚定**` 子弹式）下 `- "..."` 英文句（id 后缀 .a/.b）；模板 = `**骨架**` / `**模板**` / `**模板/骨架**` / `**结构**` / `[骨架]` 块、代码围栏或紧随裸英文段内带 `[槽位]` 的填槽骨架。
> **citekey** 优先取卡片尾部 `<!-- wb:... -->` 标记，无则回退 `**来源论文**`/`**来源**`/裸 `来源：`/`- **出处**` 原文；EXTEND 子变体回退 `- **原文锚定**` 尾部 `（citekey, …）` 标注；皆无标 `未标注`（不编造）。**适配槽位** 取 `**槽位**`/`[适用槽位]` 字段内 M1–M10（含 M2.5）与 Q1–Q8（去重排序）；无字段或含 `M?` 标 `通用`。
> **锚点** = `corpus/<文件名>#变体-<变体号>`（脚本自定义片段，指向 `### 变体 <N>` 标题；不编号/EXTEND 变体指向其真实 `### 变体：`/`#### 变体：` 标题；`--verify` 断言标题存在）。
> 状态列：`verbatim` = 逐字底本（与源卡片逐字一致，不得改写/拼接/补全）；`模板` = 填槽骨架（不可当逐字底本引用）。`不编号变体`（fang2025 POM，不计入 342）与 `EXTEND子变体`（`####` 层，不计入 342）在 id 与状态列标注。

条目：verbatim 3 条 / 模板 3 条。

## Verbatim 底本

| id | 适配槽位 | citekey | 句子原文（或模板） | 卡片路径#锚点 | 状态 |
|---|---|---|---|---|---|
| `rare-outcome#1` | M7 | zorn_shropshire_martin_combs_ketchen_2017_smj | Given the low base rate occurrence of financial restatement (i.e., many firms never restate), fixed effects models drop a significant number of observations due to lack of variance in the dependent variable. Thus, in modeling the likelihood of financial misconduct, we control for firm effects by clustered standard errors (Long & Freese, 2014). | `corpus/稀有结果.md#变体-1` | verbatim |
| `rare-outcome#2` | M2 | lun_zurbruegg_mount_2026_etp | This yielded a comprehensive sample of firms exposed to product recall risk, irrespective of whether a recall occurred during the study period. | `corpus/稀有结果.md#变体-2` | verbatim |
| `rare-outcome#3` | M3 | lun_zurbruegg_mount_2026_etp | Thus, 97.5% of our observations fall within the 0 to 1 recall range, indicating most variation occurs at the extensive margin—whether a recall occurs—rather than the intensive margin. | `corpus/稀有结果.md#变体-3` | verbatim |

## 填槽模板

| id | 适配槽位 | citekey | 句子原文（或模板） | 卡片路径#锚点 | 状态 |
|---|---|---|---|---|---|
| `rare-outcome#T1` | M7 | zorn_shropshire_martin_combs_ketchen_2017_smj | To model [rare binary DV], which is a low base-rate event (many [units] never experience [the event]), we use [logistic / probit] regression with [time] dummies and robust standard errors clustered by [unit] ([citation]). Fixed-effects models would drop a significant number of observations due to lack of variance in the dependent variable within [units] that never [experience the event]. We therefore control for [unit]-level dependence through clustered standard errors rather than conditional fixed effects ([citation]). [Optional identification bridge:] Because an exact [logistic] analogue of 2SLS is unavailable, we confirm these results using an instrumental-variable [bivariate probit / IV-probit] model in robustness checks. | `corpus/稀有结果.md#变体-1` | 模板 |
| `rare-outcome#T2` | M2 | lun_zurbruegg_mount_2026_etp | To test [hypotheses], we constructed a panel spanning [start] through [end] by integrating data from multiple sources. We began by identifying all [units] operating in [regulatory domain that generates the outcome]. This yielded a comprehensive sample of [units] exposed to [outcome] risk, irrespective of whether [the event] occurred during the study period. We then matched [event registry] to these [units] to identify [events]. Our final sample includes both [event] and non-[event] observations. After merging these data, and removing observations outside the sample window or missing [outcome] data, the final panel comprised [N] [unit-period] observations across [N_units] [units]. | `corpus/稀有结果.md#变体-2` | 模板 |
| `rare-outcome#T3` | M3 | lun_zurbruegg_mount_2026_etp | [Events] are rare events. Of the [N] [unit-period] observations, [p0]% experienced no [event], [p1]% experienced one, and [p2]% experienced multiple [events]. Thus, [p_zero_or_one]% of observations fall within the 0 to 1 range, indicating most variation occurs at the extensive margin—whether [the event] occurs—rather than the intensive margin—how many occur conditional on one taking place. Accordingly, our primary analysis uses [panel conditional logit], consistent with prior studies ([citations]). We code [DV] as a binary indicator equal to [1] if the [unit] experienced at least one [event] in a given [period], and [0] otherwise. This specification aligns with our theoretical focus on whether [IV] is associated with the likelihood of [observable failure]. | `corpus/稀有结果.md#变体-3` | 模板 |
