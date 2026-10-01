# hawkes-process — 二级骨架清单（Hawkes过程（自激点过程聚类））

> 本目录由脚本重建，手改会被覆盖；重建命令 = `python scripts/build_indices.py`（路径基准：以本 skill 目录（SKILL.md 所在目录）为基准）。
> **抽取规则（先定后抽）**：verbatim = 卡片 `**原始句锚点**` 内带引号/缩进的完整英文原句（有明确来源论文，逐字保留、含 `…` 不回填）+ `#### 原文锚定` 下 `- "..."` 英文句（id 后缀 .a/.b）；模板 = 卡片 `**骨架**` / `**骨架/框架**` 块或代码围栏内带 `[槽位]` 的填槽骨架。
> **citekey** 优先取卡片尾部 `<!-- wb:... -->` 标记，无则回退 `**来源论文**` 原文，两者皆无标 `未标注`（不编造）。**适配槽位** 取 `**槽位**:` 字段内 R1–R9（去重排序）；无字段时回退文件内「槽位分布」表；仍判断不了或含 F 槽位标 `通用`。
> **锚点** = `corpus/<文件名>#变体-<变体号>`（脚本自定义片段，指向 `### 变体 <N>` 标题；`--verify` 断言该标题存在）。
> 状态列：`verbatim` = 逐字底本（与源卡片逐字一致，不得改写/拼接/补全）；`模板` = 填槽骨架（不可当逐字底本引用）。

条目：verbatim 1 条 / 模板 1 条。

## Verbatim 底本

| id | 适配槽位 | citekey | 句子原文（或模板） | 卡片路径#锚点 | 状态 |
|---|---|---|---|---|---|
| `hawkes-process#A.a` | 通用 | mukherjee_2022_hiding_in_the_herd_the_product_recall_cluster | If the recalls announced by firm f̃ indeed act as following recalls, then we would observe a statistically significant θ̂ for firm f̃ in this placebo test, making our Hawkes process model results questionable. ... As a caution, we repeated this placebo test 1,000 times ... There was not one instance in which the Hawkes process model led to a significant excitation parameter θ̂ for firm f̃. | `corpus/Hawkes过程.md#变体-A` | verbatim（原文锚定节） |

## 填槽模板

| id | 适配槽位 | citekey | 句子原文（或模板） | 卡片路径#锚点 | 状态 |
|---|---|---|---|---|---|
| `hawkes-process#TA` | 通用 | mukherjee_2022_hiding_in_the_herd_the_product_recall_cluster | Our first [mechanism] robustness check examines the validity of our [model approach] using a placebo test. We did so by creating a fictitious [unit], denoted [f̃]. For [f̃], we mirrored [a median real unit] by generating [the same number of subunits], matching [the profile of the mirrored unit], and randomly selected [matched share] to have no [events]. We then randomly assigned the [events] to the remaining [subunits] by drawing random samples from the per-[subunit] [event] distribution for [the mirrored unit]. Finally, we assigned random [event dates] for each [subunit] that had a positive number of [events]. We reestimated the [model] with [f̃] data added to the real data but constrained the [background behavior] of [f̃] to depend only on [its own covariates]. If the [events] attributed to [f̃] indeed act as [mechanism-consistent events], then we would observe a statistically significant [key parameter] for [f̃] in this placebo test, making our [model] results questionable. If not, this placebo test would indicate that [randomized events] do not lead to [the phenomenon] under the [model]. [Null result: parameters equal to (values), both not significant (p > [thresholds])]. As a caution, we repeated this placebo test [1,000] times where, in each repetition, we used new, randomly sampled [profile inputs] for [f̃]. There was not one instance in which the [model] led to a significant [key parameter] for [f̃]. This helps to build confidence in our choice of the [model] to examine [the phenomenon]. | `corpus/Hawkes过程.md#变体-A` | 模板 |
