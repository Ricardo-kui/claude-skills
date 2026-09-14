# matched-did — 二级骨架清单（匹配DiD-广义DiD）

> 本目录由脚本重建，手改会被覆盖；重建命令 = `python scripts/build_indices.py`（路径基准：以本 skill 目录（SKILL.md 所在目录）为基准）。
> **抽取规则（先定后抽）**：verbatim = 卡片 `**原始句锚点**` / `[原始句锚点]` / `- **原始句锚点**（…）` 内带引号/缩进的完整英文原句（有明确来源论文，逐字保留、含 `…` 不回填）+ `**原文锚定**`/`**原文锚点**`（含 `- **原文锚定**` 子弹式）下 `- "..."` 英文句（id 后缀 .a/.b）；模板 = `**骨架**` / `**模板**` / `**模板/骨架**` / `**结构**` / `[骨架]` 块、代码围栏或紧随裸英文段内带 `[槽位]` 的填槽骨架。
> **citekey** 优先取卡片尾部 `<!-- wb:... -->` 标记，无则回退 `**来源论文**`/`**来源**`/裸 `来源：`/`- **出处**` 原文；EXTEND 子变体回退 `- **原文锚定**` 尾部 `（citekey, …）` 标注；皆无标 `未标注`（不编造）。**适配槽位** 取 `**槽位**`/`[适用槽位]` 字段内 M1–M10（含 M2.5）与 Q1–Q8（去重排序）；无字段或含 `M?` 标 `通用`。
> **锚点** = `corpus/<文件名>#变体-<变体号>`（脚本自定义片段，指向 `### 变体 <N>` 标题；不编号/EXTEND 变体指向其真实 `### 变体：`/`#### 变体：` 标题；`--verify` 断言标题存在）。
> 状态列：`verbatim` = 逐字底本（与源卡片逐字一致，不得改写/拼接/补全）；`模板` = 填槽骨架（不可当逐字底本引用）。`不编号变体`（fang2025 POM，不计入 342）与 `EXTEND子变体`（`####` 层，不计入 342）在 id 与状态列标注。

条目：verbatim 2 条 / 模板 2 条。

## Verbatim 底本

| id | 适配槽位 | citekey | 句子原文（或模板） | 卡片路径#锚点 | 状态 |
|---|---|---|---|---|---|
| `matched-did#1` | M8 | Castellaneta_Conti_Kacperczyk_2017_SMJ | In a quasi-experimental setting, this ideal condition is less likely to hold, which could be a concern if the treated firms are ex ante different from control firms along some characteristics that correlate with both our treatment (i.e., UTSA enactment) and our outcome (i.e., change in firm market value). To account for such potential confounders, we reestimate the baseline specifications, while also matching the treatment and control firms on the basis of ex ante investment size, which proxies for the target's ex ante value, and industry resource–value uncertainty, which proxies for the target's business riskiness (Acharya et al., 2013; Castellaneta and Zollo, 2015; Shepherd, 1999). | `corpus/匹配DiD-广义DiD.md#变体-1` | verbatim |
| `matched-did#2.a` | 通用 | lu_et_al_2022_frenemies_corporate_advertising | To control for differences in the investment and stock picking styles of the merging institutions, we construct the control group as the firms that are simultaneously owned by at least one of the merging institutions but do not experience a change in common ownership. | `corpus/匹配DiD-广义DiD.md#变体-2` | verbatim（原文锚定节） |

## 填槽模板

| id | 适配槽位 | citekey | 句子原文（或模板） | 卡片路径#锚点 | 状态 |
|---|---|---|---|---|---|
| `matched-did#T1` | M8 | Castellaneta_Conti_Kacperczyk_2017_SMJ | In any experimental setting, random assignment establishes ex ante symmetry between treatment and control groups. In a quasi-experimental setting, this ideal is less likely to hold if treated [units] differ ex ante along characteristics that correlate with both treatment ([law/policy] enactment) and [Δoutcome]. Importantly, either the level of ex ante [risk] or the expected [value] of a [unit] may correlate with the change in [outcome] or with policymakers' effort to enact [law]—for instance, to protect riskier or more valuable [units]. To account for such confounders, we reestimate the baseline specifications while matching treatment and control on ex ante [investment size / value proxy] and [industry resource-value uncertainty / risk proxy] ([citations]). We use coarsened exact matching (CEM) as developed by [Iacus, King & Porro / citation]. Results remain robust on the matched sample ([table/appendix]). | `corpus/匹配DiD-广义DiD.md#变体-1` | 模板 |
| `matched-did#T2` | 通用 | lu_et_al_2022_frenemies_corporate_advertising | [动机句——点名被吸收的混淆源] To control for differences in the [selection styles] of the [shock actors], we construct the control group as the [units] that are simultaneously [held] by at least one of the [shock actors] but do not experience a change in [treatment]. [编号双条件——锚定事件前时点] Specifically, to be included in the control sample, a [unit] must satisfy two conditions in the [quarter] before the [event announcement]. First, the [unit] must be [held] by the same [actor] that [holds] a treated [unit]. Second, [the other actor] must not [hold] any [peer units] from the same [category]. [warrant 收口] Thus, the [event] does not affect the [treatment status] of control [units], and yet, these [units] are [held] by the [combined actors]. | `corpus/匹配DiD-广义DiD.md#变体-2` | 模板 |
