# matched-did — 二级骨架清单（匹配 DiD）

> 本目录由脚本重建，手改会被覆盖；重建命令 = `python scripts/build_indices.py`（在 `write-results/` 目录下）。
> **抽取规则（先定后抽）**：verbatim = 卡片 `**原始句锚点**` 内带引号/缩进的完整英文原句（有明确来源论文，逐字保留、含 `…` 不回填）+ `#### 原文锚定` 下 `- "..."` 英文句（id 后缀 .a/.b）；模板 = 卡片 `**骨架**` / `**骨架/框架**` 块或代码围栏内带 `[槽位]` 的填槽骨架。
> **citekey** 优先取卡片尾部 `<!-- wb:... -->` 标记，无则回退 `**来源论文**` 原文，两者皆无标 `未标注`（不编造）。**适配槽位** 取 `**槽位**:` 字段内 R1–R9（去重排序）；无字段时回退文件内「槽位分布」表；仍判断不了或含 F 槽位标 `通用`。
> **锚点** = `corpus/<文件名>#变体-<变体号>`（脚本自定义片段，指向 `### 变体 <N>` 标题；`--verify` 断言该标题存在）。
> 状态列：`verbatim` = 逐字底本（与源卡片逐字一致，不得改写/拼接/补全）；`模板` = 填槽骨架（不可当逐字底本引用）。

条目：verbatim 1 条 / 模板 1 条。

## Verbatim 底本

| id | 适配槽位 | citekey | 句子原文（或模板） | 卡片路径#锚点 | 状态 |
|---|---|---|---|---|---|
| `matched-did#1` | R7 | Castellaneta_Conti_Kacperczyk_2017_SMJ | We used a coarsened exact matching (CEM) approach as developed by Iacus, King, and Porro (2009) to perform a match between treatment and control. As shown in Table S2, our results remain robust. | `corpus/匹配DiD.md#变体-1` | verbatim |

## 填槽模板

| id | 适配槽位 | citekey | 句子原文（或模板） | 卡片路径#锚点 | 状态 |
|---|---|---|---|---|---|
| `matched-did#T1` | R7 | Castellaneta_Conti_Kacperczyk_2017_SMJ | In a quasi-experimental setting, random assignment is less likely to hold, which is a concern if treated [units] differ ex ante from controls on characteristics that correlate with both [treatment] and [outcome]. For instance, [ex-ante value] or [business risk] may correlate with policymakers' effort to enact [policy] or with subsequent [outcome] change. To account for such potential confounders, we re-estimate the baseline specifications while matching treatment and control on [value proxy] and [risk proxy]. We use coarsened exact matching (CEM) (Iacus, King, and Porro, 2009). As shown in [appendix balance/results table], our results remain robust. | `corpus/匹配DiD.md#变体-1` | 模板 |
