# cross-audience-construct — 二级骨架清单（跨受众构念对比）

> 本目录由脚本重建，手改会被覆盖；重建命令 = `python scripts/build_indices.py`（路径基准：以本 skill 目录（SKILL.md 所在目录）为基准）。
> **抽取规则（先定后抽）**：verbatim = 卡片 `**原始句锚点**` 内带引号/缩进的完整英文原句（有明确来源论文，逐字保留、含 `…` 不回填）+ `#### 原文锚定` 下 `- "..."` 英文句（id 后缀 .a/.b）；模板 = 卡片 `**骨架**` / `**骨架/框架**` 块或代码围栏内带 `[槽位]` 的填槽骨架。
> **citekey** 优先取卡片尾部 `<!-- wb:... -->` 标记，无则回退 `**来源论文**` 原文，两者皆无标 `未标注`（不编造）。**适配槽位** 取 `**槽位**:` 字段内 R1–R9（去重排序）；无字段时回退文件内「槽位分布」表；仍判断不了或含 F 槽位标 `通用`。
> **锚点** = `corpus/<文件名>#变体-<变体号>`（脚本自定义片段，指向 `### 变体 <N>` 标题；`--verify` 断言该标题存在）。
> 状态列：`verbatim` = 逐字底本（与源卡片逐字一致，不得改写/拼接/补全）；`模板` = 填槽骨架（不可当逐字底本引用）。

条目：verbatim 1 条 / 模板 1 条。

## Verbatim 底本

| id | 适配槽位 | citekey | 句子原文（或模板） | 卡片路径#锚点 | 状态 |
|---|---|---|---|---|---|
| `cross-audience-construct#1` | R3/R5 | 未标注 | The same ambiguity that makes organizations less appealing to consumers makes them more appealing to venture capitalists. These effects are illustrated in figure 2. | `corpus/跨受众构念对比.md#变体-1` | verbatim |

## 填槽模板

| id | 适配槽位 | citekey | 句子原文（或模板） | 卡片路径#锚点 | 状态 |
|---|---|---|---|---|---|
| `cross-audience-construct#T1` | R3/R5 | 未标注 | Models [M1]–[M2] test [audience A's] evaluations; these are [estimator A] models with [DV_A] as the dependent variable. [IV] has a [negative] effect on [DV_A], significant at *p* < [.001] (model [M1]). Models [M3]–[M4] test [audience B's] evaluations. These are [estimator B] models estimating [DV_B]. [IV] has a [positive] effect on [DV_B], significant at *p* < [.001] (model [M3]). [Substantive translation]: the same [IV] that makes [actors] less appealing to [audience A] makes them more appealing to [audience B]. These effects are illustrated in [Figure X]. [Economic significance per audience]: decreasing [IV] by one standard deviation from the mean results in [ΔDV_A]; an [actor] one standard deviation above the mean is [~1.5×] more likely to [DV_B]. | `corpus/跨受众构念对比.md#变体-1` | 模板 |
