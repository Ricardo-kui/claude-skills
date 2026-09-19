# Generation Protocol — 生成层协议（G1–G3）

> **单一事实源**：本文件是 leading word「底本」「借句表」「coverage」在 write-results 内的唯一权威定义处。`SKILL.md`、`outline-protocol.md` 只引用本协议，不复述其定义。
> **位置**：大纲（`outline-protocol.md`）之后、渲染与措辞（SKILL.md 渲染节）之前。上游 = 大纲表；下游 = 渲染。
> **分工**：claim 句层级校准见 `claim-calibration.md`（七级 ladder）；双层支持判断见 `hypothesis-fulfillment-map.md`；分析单元六问见 `draft-revision-protocol.md` §4。本协议只写「如何把底本变成最终段落」的步骤与产物，与上述文件**互链不重复**。

## 一、两个 leading word 的权威定义

### 底本（exemplar base）

底本 = 可 verbatim 借用的范文句骨架，附 id 与 citekey。唯一来源是二级骨架清单 `corpus/_skeleton/<模型族>.md`（路由见 `corpus/_skeleton/_index.md`）。

- 每条底本带状态列：`verbatim`（逐字）或 `模板`（填槽骨架）。**`模板` 不可当逐字底本**，借用时按填槽处理。
- 底本借用 = **只替换来源特异内容（数字/表号/系数/专名），骨架与证据功能结构保留**。
- citekey 继承自卡片，索引不改写；冲突（`未标注` 等）保留状态列原样引用、不自行更正，并在借句表备注登记。
- 底本状态为 EMERGING（单源）时，借句表该行加「单篇来源」标记，正文采用处保持该认知（不得当已验证惯例使用；三带判据见 registry/INDEX）。

### 借句表（exemplar-borrowing table）

借句表 = 每段一行的六列表，进输出合同：

| 段/证据功能 | 主导功能 | 底本 id | 借用骨架 | 替换清单 | 事实直陈校验 |
|---|---|---|---|---|---|
| R3 | 主假设检验 | `ols-fe#12` 或 `self-drafted` 或 `framing-exempt` | 底本原句 / 模板骨架 | 数字/表号/系数/变量 | 方向→显著性→幅度→支持判断 |

- 底本 id 只能取自 `corpus/_skeleton/<模型族>.md`；无对应底本填 `self-drafted`；程序性段填 `framing-exempt`（口径见 `outline-protocol.md` §六）。
- 替换清单逐项列出被替换的来源特异内容（数字 / 表号 / 系数 / 专名 / 样本）。
- 「事实直陈校验」从四拍选一：**方向 / 显著性 / 幅度 / 支持判断**——该段至少兑现其中之一。

> 上表为格式示意，不是可套用的段落清单。

## 二、G1 借句表

1. 按大纲表逐段启动：每段先落借句表行，再渲染该段正文（先借句表，后正文）。
2. 底本 id 只允许引用二级清单的 id；无对应底本填 `self-drafted`，并**登记语料变体需求**（append_variant 意向；登记去向见 `feedback-protocol.md`，本协议不重复登记格式）。
3. 借句表进输出合同固定位置，作为 G2 的准入产物。

**完成判据（是/否）**
- 借句表出现在每次生成输出的固定位置？
- 每段一行的底本 id 非空（二级清单 id / `self-drafted` / `framing-exempt`）？
- 全部非空 id 可在 `corpus/_skeleton/<模型族>.md` 定位？

## 三、G2 渲染

固定顺序（逐级执行）：
1. 取底本骨架；
2. 替换来源特异内容（数字 / 表号 / 系数 / 专名）；
3. 填本文事实（方向、显著性、幅度）并绑定 verdict；
4. 校验事实直陈四拍完整（方向→显著性→幅度→支持判断），不把支持判断写成四句模板。

错误顺序 = 先写通用正确段，再「让它像范文」。

**完成判据（是/否）**
- 每段「替换清单」非空，数字/表号/系数已换成本文对象？
- 每段「事实直陈校验」已填且属四拍之一？
- claim 句已按 `claim-calibration.md` 校准（L 层未越过证据层级）？（指针，定义见该文件）

## 四、coverage 定义

`coverage = 引用了二级底本 id 的论证型槽位/段数 ÷ 论证型槽位/段总数`

- 分母只含**论证型**槽位/段；程序性内容（`outline-protocol.md` §六）记 `framing-exempt`，**不进分母**。
- `self-drafted` 属论证型但无底本 → 进分母、不计入分子，压低 coverage。
- coverage 不设硬阈值；低 coverage 不是失败，但须如实记录并触发「语料变体需求」登记。

**完成判据（是/否）**
- coverage 已计算，分母只含论证型槽位/段？
- 程序性段已记 `framing-exempt`、未进分母？
- 低 coverage 的 `self-drafted` 段已登记语料变体需求？

## 五、与既有文件互链（指针，不复制）

- **`claim-calibration.md`（七级 ladder L1–L7）**：写 R3 claim 句 / R5 经济显著性 / Discussion implication 前校准主张层级。借句表「事实直陈校验」若填「支持判断」，该句的 L 层由 `claim-calibration.md` 判，本协议只留指针。
- **`hypothesis-fulfillment-map.md`（双层支持判断）**：借句表 verdict 只填 `baseline_verdict`；`overall_evidence`（stable/qualified/mixed/unresolved）由该文件的映射表跨检验后填，不得在借句表内混用两层。定义见该文件，本协议不重复。
- **`draft-revision-protocol.md` §4（分析单元六问）**：R7/R8 每威胁一段的内部逻辑（问题路径→受影响推断→诊断含义→检验→证据→裁决）见该文件；借句表只负责该段的底本来源。
- **`design-branches.md`（R1–R9 顺序）**：槽位定序见该文件，本协议不重复。

## 六、完成判据汇总（是/否）

1. 借句表已产出，每段底本 id 非空且取值合法？
2. 全部非空 id 可在二级清单定位？
3. G2 四步顺序在「替换清单 / 事实直陈校验」栏可核对？
4. coverage 已按 §四 计算，豁免段未进分母？
5. 借句表 verdict 只填 baseline_verdict，未混入 overall_evidence？
6. claim 句 L 层已按 `claim-calibration.md` 校准？
7. **待真实验证（用户在场）**：跑一次真实 Results 生成，人工抽查四拍是否自然融合而非四句模板——抽查点：R3 段是否把方向/显著性/幅度/支持判断织成证据链而非四句并列；R7 威胁段是否按六问组织而非模板流水。
