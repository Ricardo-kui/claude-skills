# Outline Protocol — 段级大纲协议（O1–O3）

> **单一事实源**：本文件是 leading word「大纲」（outline）与「来源列」在 write-results 内的唯一权威定义处。`SKILL.md` 与其余 reference 只引用本协议，不复述其定义。
> **位置**：槽位序列确定（`design-branches.md` 分支 + `hypothesis-fulfillment-map.md` 映射）之后、`generation-protocol.md` G1 借句表之前。上游 = `design-branches.md`（R1–R9 顺序）+ `hypothesis-fulfillment-map.md`（假设→槽位）+ `corpus/_skeleton/_index.md`（21 模型族路由）；下游 = G1 借句表。
> **分工**：槽位内部骨架见 `slot-R*.md`；假设-结果映射与双层支持判断见 `hypothesis-fulfillment-map.md`；结果类型变体句式见 `corpus/[结果类型].md`。本协议只负责**段序列的取材、合成与来源登记**，不复制上述内容。

## 一、大纲是什么

大纲 = 一张四列表，逐段记录「这一段属哪个证据功能、承担什么功能、依据什么底本」。一级轴 = 模型族（21 项，`corpus/_skeleton/_index.md`）。它是槽位序列确定后的段级产物，是 G1 借句表的准入前提。

| 段/证据功能 | 主导功能 | 承载信息 | 来源 |
|---|---|---|---|
| R3 | 主假设检验 | 方向→显著性→幅度→支持判断 | `ols-fe#12` |
| R2 | 表格导航 | 哪个模型在哪张表 | `framing-exempt` |
| R4 | 控制变量叙述 | 控制变量系数流水账 | `framing-exempt` |
| R7 | 稳健性威胁 | 威胁→诊断→证据→裁决 | `self-drafted` |

> 上表为格式示意，不是可套用的段落清单。

**大纲不是**：槽位骨架（`slot-R*.md`）、假设-结果映射表（`hypothesis-fulfillment-map.md`）、句子底本（G1/G2 负责）。

## 二、O1 取材

1. 读 `references/design-branches.md`，确定结果类型的 R1–R9 顺序（观察性默认顺序或特殊分支）。
2. 读 `references/hypothesis-fulfillment-map.md`，建立假设 → 槽位 → baseline verdict 映射（只消费，不复制该表）。
3. 读 `corpus/_skeleton/_index.md`「一级轴 = 模型族」表，定位该模型族对应的二级清单文件（21 项之一）。
4. 整份读入二级清单 `corpus/_skeleton/<模型族>.md`，取「适配槽位」命中当前证据功能的底本 id（`<模型族>#<N>` / `<模型族>#T<N>`）。

## 三、O2 合成

1. 把 R1–R9 顺序 + hypothesis-fulfillment-map 展开为段序列（每假设一段 R3，每威胁一段 R7，交互假设加 R4）。
2. **来源列**：每段填二级底本 id 或 `self-drafted`；程序性内容（§六豁免清单）填 `framing-exempt`。
3. 段内既含论证又含程序性陈述时，拆成两段，或按主导功能判一类（论证优先）。

## 四、O3 登记

1. 逐段登记四列表，每段「来源」非空且取值合法（§五）。
2. `self-drafted` 段如实记录占比，并登记语料变体需求（去向见 `generation-protocol.md` G1）。
3. 跳过/压缩的槽位在对应段标 `[skipped: 理由类型]`。
4. 大纲表进入 G1 借句表的准入产物。

## 五、来源取值枚举

| 取值 | 含义 | 何时使用 |
|---|---|---|
| `<模型族>#<N>` | verbatim 底本 id，取自二级清单「Verbatim 底本」表 | 有逐字底本 |
| `<模型族>#T<N>` | 模板底本 id，取自二级清单「填槽模板」表 | 有填槽骨架（按填槽处理，不当逐字） |
| `self-drafted` | 无底本，本文自拟 | 前两种来源都无对应 |
| `framing-exempt` | 程序性/审计性内容，不进 coverage 分母 | §六豁免清单 |

## 六、程序性内容豁免清单（framing 豁免）

以下**审计性内容**填 `framing-exempt`，不进 coverage 分母：

- **R4 控制变量叙述**（控制变量系数的逐项报告、符号与显著性流水账，不含对聚焦预测的解释）
- **R1 描述性统计**（均值/标准差/相关矩阵的叙述）
- **R2 表格导航与样本量陈述**（「Table X reports…」导航句、N 的陈述）
- **表号/系数的机械转述**（不含解释的引用）
- **非聚焦变量的定义回溯句**（对 Methods 已定义变量的复述）

> 判据：这段是否可被审稿人机械核对（数字、表号、系数）而无须理解证据链？是 → 豁免；否 → 论证型，需底本 id。

## 七、完成判据（是/否）

- 大纲表四列齐全，每段「来源」非空且取值合法？
- `self-drafted` 占比已如实记录？
- 程序性内容已按 §六填 `framing-exempt`，未混入 coverage 分母？
- 假设 → 槽位映射覆盖 Theory 全部假设（含非显著假设，R3/R6）？
- 槽位顺序与 `design-branches.md` 一致（含分支理由）？
