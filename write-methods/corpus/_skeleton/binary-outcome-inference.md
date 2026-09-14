# binary-outcome-inference — 二级骨架清单（推断二元结果）

> 本目录由脚本重建，手改会被覆盖；重建命令 = `python scripts/build_indices.py`（在 `write-methods/` 目录下）。
> **抽取规则（先定后抽）**：verbatim = 卡片 `**原始句锚点**` / `[原始句锚点]` / `- **原始句锚点**（…）` 内带引号/缩进的完整英文原句（有明确来源论文，逐字保留、含 `…` 不回填）+ `**原文锚定**`/`**原文锚点**`（含 `- **原文锚定**` 子弹式）下 `- "..."` 英文句（id 后缀 .a/.b）；模板 = `**骨架**` / `**模板**` / `**模板/骨架**` / `**结构**` / `[骨架]` 块、代码围栏或紧随裸英文段内带 `[槽位]` 的填槽骨架。
> **citekey** 优先取卡片尾部 `<!-- wb:... -->` 标记，无则回退 `**来源论文**`/`**来源**`/裸 `来源：`/`- **出处**` 原文；EXTEND 子变体回退 `- **原文锚定**` 尾部 `（citekey, …）` 标注；皆无标 `未标注`（不编造）。**适配槽位** 取 `**槽位**`/`[适用槽位]` 字段内 M1–M10（含 M2.5）与 Q1–Q8（去重排序）；无字段或含 `M?` 标 `通用`。
> **锚点** = `corpus/<文件名>#变体-<变体号>`（脚本自定义片段，指向 `### 变体 <N>` 标题；不编号/EXTEND 变体指向其真实 `### 变体：`/`#### 变体：` 标题；`--verify` 断言标题存在）。
> 状态列：`verbatim` = 逐字底本（与源卡片逐字一致，不得改写/拼接/补全）；`模板` = 填槽骨架（不可当逐字底本引用）。`不编号变体`（fang2025 POM，不计入 342）与 `EXTEND子变体`（`####` 层，不计入 342）在 id 与状态列标注。

条目：verbatim 1 条 / 模板 1 条。

## Verbatim 底本

| id | 适配槽位 | citekey | 句子原文（或模板） | 卡片路径#锚点 | 状态 |
|---|---|---|---|---|---|
| `binary-outcome-inference#1` | M2/M3 | hoffmann_cheong_phan_zurbruegg2024_jm | For about 60% of the overall sample, namely 868 recalls, there are no prior injuries or deaths. This is where firms will have the greatest managerial discretion on whether or not to issue a recall, and from a theoretical perspective, this subset of recalls is therefore most appropriate for testing our hypotheses and will be the focus of our analyses. | `corpus/推断二元结果.md#变体-1` | verbatim |

## 填槽模板

| id | 适配槽位 | citekey | 句子原文（或模板） | 卡片路径#锚点 | 状态 |
|---|---|---|---|---|---|
| `binary-outcome-inference#T1` | M2/M3 | hoffmann_cheong_phan_zurbruegg2024_jm | Our dependent variable, [binary outcome], equals one if [unit] [action] in year t. Hand-collected [event descriptions] allow us to distinguish [events] with versus without [prior condition: e.g., prior injuries/deaths]. We focus the main analysis on [events] without [prior condition] because [institutional actor: e.g., regulator] pressure and [legal exposure] largely remove [actor] discretion once [harm] has materialized ([citation/footnote]). This subset is where [theorized mechanism: e.g., litigation risk vs. opportunism] should operate. We verify in supplemental analyses that [treatment] has no effect on [events] with [prior condition], consistent with the discretion logic. | `corpus/推断二元结果.md#变体-1` | 模板 |
