# Skeleton Index — 骨架索引路由

> **两层结构**：本路由 + 每模块一份子索引。先读本文件的「何时读它」定位模块，再整份读入对应子索引。
> 由 `scripts/build_indices.py` 生成；底本来源为 corpus 段级卡「原文锚定」块、phrasebank 借句行、micro-templates 范文锚定行。
> **单源纪律**：verbatim 底本只存在子索引里；形状包（`../packs/`）与借句表只引 `id`。
> 状态列：`verbatim` = 逐字底本（无槽位、与源文件逐字一致）；`模板` = 含 `[槽位]` 的填槽骨架（不可当逐字底本）。

| 子索引 | verbatim | 模板 | 行数 | 一行说明 | 何时读它 |
|---|---|---|---|---|---|
| [`hooks.md`](hooks.md) | 80 | 80 | 179 | 开篇 Hook 的逐字底本（数据冲击 / 悖论 / 范式挑战 / 轶事等）与填槽模板 | 要写 Hook、换 Hook 类型，或 Hook 只有信息没有张力时 |
| [`tensions.md`](tensions.md) | 98 | 113 | 230 | 问题化 / Gap 张力句底本与填槽模板 | 要把 Gap 写成张力，或 Gap 强度不足、像 few-studies 套话时 |
| [`stakes.md`](stakes.md) | 31 | 39 | 89 | 研究重要性 / stakes 句底本与填槽模板 | 要论证为什么重要，或 stakes 与 Hook 单调重复时 |
| [`literature-turns.md`](literature-turns.md) | 26 | 39 | 84 | 文献对话组织句底本（progressive / synthesized / non-coherence） | 要定位文献关系、写 Literature Turn 时 |
| [`theory-lens.md`](theory-lens.md) | 25 | 17 | 61 | 理论透镜引入句底本与填槽模板 | 要引入理论透镜，或 theory 声明与机制脱节时 |
| [`previews.md`](previews.md) | 46 | 60 | 125 | 研究设计 / 发现预览句底本与填槽模板 | 要预告假设、样本、量级、稳健性或边界时 |
| [`contributions.md`](contributions.md) | 34 | 31 | 84 | 贡献声明句底本与填槽模板 | 要写 Contribution 段，或贡献与 tension 脱节时 |
| [`research-questions.md`](research-questions.md) | 9 | 6 | 34 | Research Question 句底本与填槽模板 | 要写 RQ，或 RQ 与 gap 不对应时 |
| [`transitions.md`](transitions.md) | 28 | 49 | 96 | 模块间过渡（Hook→Literature Turn 等）底本与填槽模板 | 段落之间跳跃、需要模块级过渡时 |
| [`differentiation.md`](differentiation.md) | 1 | 1 | 21 | 与最近文献划界句底本与填槽模板 | 要写 Differentiation，或与 closest paper 未区分时 |
| [`phrasebank.md`](phrasebank.md) | 5 | 91 | 115 | Morley 措辞库借句（单研究批判 / hedging 强度 / 过程与数值描述） | G2 落句后需要换说法或校准声明强度时 |
| [`micro-templates.md`](micro-templates.md) | 7 | 30 | 56 | 句级骨架、范文 key line、过渡信号词与 thesis 模型 | 需要句法骨架、句级 transition 或 thesis 定位模型时 |

合计：verbatim 390 条 / 模板 556 条 / 1174 行。

## 核对记录

- `未标注` citekey 实测 **53 条**（hooks 3、tensions 8、literature-turns 2、previews 5、contributions 4、transitions 1、micro-templates 30）；生成物逐行实测值，非估算。

## 待补录

- [`_unparsed.md`](_unparsed.md)：16 条未自动命中或疑似误抽 + 1 条人工剔除（合计 17 条），**待补录 / 待人工判定**。任何模块的子索引条目在被人工核对前都视为草稿。
- 人工剔除记录：`scripts/skeleton_exclusions.txt`（重跑脚本时保留剔除，保证幂等）。
