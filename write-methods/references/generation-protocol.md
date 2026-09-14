# Generation Protocol — 生成层协议（G1–G3）

> **单一事实源**：本文件是 leading word「底本」「借句表」「coverage」在 write-methods 内的唯一权威定义处。`SKILL.md`、`outline-protocol.md` 只引用本协议，不复述其定义。
> **位置**：大纲（`outline-protocol.md`）之后、渲染与措辞（SKILL.md 渲染节）之前。上游 = 大纲表；下游 = 渲染。
> **分工**：槽位内部骨架见 `slot-*.md`；设计类型变体句式见 `corpus/[设计类型].md`；语态纪律见 `draft-revision-protocol.md` §5。本协议只写「如何把底本变成最终段落」的步骤与产物。

## 一、两个 leading word 的权威定义

### 底本（exemplar base）

底本 = 可 verbatim 借用的范文句骨架，附 id 与 citekey。唯一来源是二级骨架清单 `corpus/_skeleton/<设计类型>.md`（路由见 `corpus/_skeleton/_index.md`）。

- 每条底本带状态列：`verbatim`（逐字）或 `模板`（填槽骨架）。**`模板` 不可当逐字底本**，借用时按填槽处理。
- 底本借用 = **只替换来源特异内容（专名/样本/年份/数字/机构），骨架节奏与结构词保留**。
- citekey 继承自卡片，索引不改写；冲突（`未标注` 等）保留状态列原样引用、不自行更正，并在借句表备注登记。

### 借句表（exemplar-borrowing table）

借句表 = 每段一行的六列表，进输出合同：

| 段/槽位 | 主导功能 | 底本 id | 借用骨架 | 替换清单 | 审计语态 |
|---|---|---|---|---|---|
| M2 | 样本漏斗 | `panel-ols#7` 或 `self-drafted` 或 `framing-exempt` | 底本原句 / 模板骨架 | 专名/样本/年份/数字 | 主动过去时 |

- 底本 id 只能取自 `corpus/_skeleton/<设计类型>.md`；无对应底本填 `self-drafted`；程序性段填 `framing-exempt`（口径见 `outline-protocol.md` §六）。
- 替换清单逐项列出被替换的来源特异内容（专名 / 样本 / 年份 / 数字 / 机构）。
- 审计语态从二型选一：**主动过去时**（完成的研究程序）/ **现在时**（定义、公式符号、惯例）。

> 上表为格式示意，不是可套用的段落清单。

## 二、G1 借句表

1. 按大纲表逐段启动：每段先落借句表行，再渲染该段正文（先借句表，后正文）。
2. 底本 id 只允许引用二级清单的 id；无对应底本填 `self-drafted`，并**登记语料变体需求**（append_variant 意向；登记去向见 `feedback-protocol.md`，本协议不重复登记格式）。
3. 借句表进输出合同固定位置，作为 G2 的准入产物。

**完成判据（是/否）**
- 借句表出现在每次生成输出的固定位置？
- 每段一行的底本 id 非空（二级清单 id / `self-drafted` / `framing-exempt`）？
- 全部非空 id 可在 `corpus/_skeleton/<设计类型>.md` 定位？

## 三、G2 渲染

固定顺序（逐级执行）：
1. 取底本骨架；
2. 替换来源特异内容（专名 / 样本 / 年份 / 数字 / 机构）；
3. 填 `[placeholder]`（变量名、模型规格、检验名）；
4. 校验审计语态（主动过去时 / 现在时）与设计家族匹配。

错误顺序 = 先写通用正确段，再「让它像范文」。

**完成判据（是/否）**
- 每段「替换清单」非空，来源特异内容已全部换成本文对象？
- 每段「审计语态」已填且属二型之一？
- `[placeholder]` 无机构/政策名残留？

## 四、coverage 定义

`coverage = 引用了二级底本 id 的论证型槽位/段数 ÷ 论证型槽位/段总数`

- 分母只含**论证型**槽位/段；程序性内容（`outline-protocol.md` §六）记 `framing-exempt`，**不进分母**。
- `self-drafted` 属论证型但无底本 → 进分母、不计入分子，压低 coverage。
- coverage 不设硬阈值；低 coverage 不是失败，但须如实记录并触发「语料变体需求」登记。

**完成判据（是/否）**
- coverage 已计算，分母只含论证型槽位/段？
- 程序性段已记 `framing-exempt`、未进分母？
- 低 coverage 的 `self-drafted` 段已登记语料变体需求？

## 五、完成判据汇总（是/否）

1. 借句表已产出，每段底本 id 非空且取值合法？
2. 全部非空 id 可在二级清单定位？
3. G2 四步顺序在「替换清单 / 审计语态」栏可核对？
4. coverage 已按 §四 计算，豁免段未进分母？
5. 段落语态与 `draft-revision-protocol.md` §5 一致？
6. **待真实验证（用户在场）**：跑一次真实 Methods 生成，人工抽查审计语态是否顶刊自然——抽查点：M2 段首是否为 starting population 动作而非数据源宣传；M7 公式与文字是否交替、无防御性收尾。
