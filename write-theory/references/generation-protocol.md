# Generation Protocol — 生成层协议（G1–G4）

> **单一事实源**：本文件是 leading word「底本」与「借句表」在 write-theory 的唯一权威定义处。`SKILL.md`、`outline-protocol.md` 只引用本协议，不复述其定义。
> **位置**：Phase 3 渲染之前、Phase 4 审计之前。上游 = 大纲表（`outline-protocol.md`）；下游 = Phase 4 QC（`references/phase-4-qc-alignment.md`）+ `corpus/storytelling/post-generation-validator.md`。
> **分工**：段落**论证角色**组装见 `../story-blueprints/v4/rhetoric-moves/_argument-grammar.md`；段内四段位见 `corpus/subprotocols/paragraph_layout.md`；**句子表达**细节（五病 / AI 腔 / specificity）见 `../pollock-qc/references/prose-pathology.md` 与 `../story-blueprints/v4/rhetoric-moves/_polish-protocol.md`。本协议只写「如何把底本变成最终句子」的步骤与产物 + coverage。
> **与 Hard constraints 的关系（平行层）**：本协议判据是**执行门**——回答「借句表是否产出、底本 id 是否可核、coverage 是否已算」。Hard constraints #1–16（见 SKILL.md）是**实质规则层**——回答「论证内容是否合规」。两者平行互补、互不复制：完成判据不替代 #1–16 逐条过。

## 触发分支

**任何要产出最终句子的请求都走本协议**——含完整 Theory、单假设、以及改稿（含"不够像范文"的返工）。触发不按篇幅判定；只请求诊断或大纲、不产出句子的请求不触发。

## 一、两个 leading word 的权威定义

### 底本（exemplar base）

底本 = 可 verbatim 借用的范文句骨架，附 `id`/`citekey`/`status`。唯一来源是骨架索引 `corpus/_skeleton/` 的 22 个子清单（路由见 `corpus/_skeleton/_index.md`）。

- 每条底本都带状态列：`verbatim`（逐字底本）或 `模板`（填槽骨架）。**`模板` 不可当逐字底本**，借用时按填槽处理。
- 底本借用 = **只替换来源特异内容，骨架节奏与结构词保留**。
- `citekey` 继承自卡片，索引不改写。遇到 `citekey`/`status` 为「未标注」的条目，**保留原样引用、不自行更正**，并在借句表「出处核对」列登记（见 G1）。

### 借句表（exemplar-borrowing table）

借句表 = 每段一行的七列表，进输出合同：

| 段落 | 主导功能 | 底本 id | 借用骨架 | 替换清单 | 保留节奏 | 出处核对 |
|---|---|---|---|---|---|---|
| P1 | … | `variants-E_moderation::e_moderation_joint_pressure_superadditivity_balanced_configuration.t1` 或 `self-drafted` | 模板骨架 | 专名/行业/样本/年份/数字 | 先主张后限定 | 未标注（已人工核对） |

- 底本 id 只能取自 `corpus/_skeleton/<子清单>.md`；无对应底本时填 `self-drafted`，并如实记录占比。
- 「保留节奏」从三型中选一并写死：**先主张后限定 / 先对立后裁定 / 先现象后理论**（指被借句的内部散文节奏；段级论证角色序列由 `_argument-grammar.md` 负责）。
- 「出处核对」列登记该底本 `citekey`/`status` 是否为「未标注」及是否已人工核对。

> 上表为格式示意，不是可套用的段落清单。

## 二、G1 借句表

1. 按大纲表逐段启动：每段先落借句表行，再渲染该段正文（先借句表，后正文）。
2. 底本 id 只允许引用 `corpus/_skeleton/<子清单>.md` 的 id；纯规则文件（见 G3 豁免表）只提供规则指针，不提供底本 id。
3. 无对应底本时填 `self-drafted`，并在表下记录其在全表占比（登记口径见 `outline-protocol.md` O3，不在此复述）。
4. **「未标注」与 `_unparsed` 条目**：可用，但须满足——(a) 在「出处核对」列登记 citekey/status 为「未标注」或来源为 `_unparsed`；(b) 人工核对出处后记录核对结果；(c) 不假装有完整溯源。`_unparsed` 条目（62 条，无块级 vid/pattern_id 可绑定）仅作参考句式，不填二级 id。
5. 借句表进输出合同固定位置，作为 G2 落句的准入产物。

**完成判据（是/否）**
- 借句表出现在每次生成输出的固定位置？
- 每段一行的底本 id 非空（二级 id 或 `self-drafted`）？
- 全部底本 id 可在 `corpus/_skeleton/<子清单>.md` 定位？
- 「未标注」/`_unparsed` 引用的段落已在出处核对列登记？

## 三、G2 落句

固定顺序（逐级执行）：
1. 取底本骨架；
2. 替换来源特异内容（专名 / 行业 / 样本 / 年份 / 数字）；
3. 填本文构念与方向；
4. 校验原句节奏（先主张后限定 / 先对立后裁定 / 先现象后理论）是否保留。

错误顺序 = 先写通用正确句，再"让它像范文"。

**完成判据（是/否）**
- 借句表逐段有底本 id（二级 id 或 `self-drafted`）？
- 每段「保留节奏」栏已填，且取值属三型之一？
- 每段「替换清单」栏非空，且来源特异内容已全部换成本文对象？

## 四、G3 coverage 计算

coverage = 有底本 id 的论证型段占比。每次生成输出末尾计算一次并记录。

- **分子**：论证型段中，借句表「底本 id」为二级 id（非 `self-drafted`）的段数。
- **分母**：论证型段总数，减去豁免段（功能仅由纯规则文件承接的段）。
- **论证型段** = 承担推理/假设推导功能的段（why-chain、构念定义论证、假设句、边界条件论证）；描述型段（如 Institutional Background 情境说明）不计入分母。
- **豁免口径（显式列出）**：以下文件未进 `_skeleton` 抽取范围，故其功能位永远不贡献底本 id，对应段不计入分母——
  - meta 5 文件：`routing_table` / `alignment_protocol` / `paper_state_fragment` / `product_safety_construct_lexicon` / `vault_evidence_retrieval`
  - storytelling 4 文件：`knot-continuity-check` / `plot-emergence-check` / `post-generation-validator` / `rising-action-protocol`
  - 10 个纯规则 subprotocols：`arrangement_patterns` / `B2_dual_track` / `board_governance_boundary_condition` / `character_ordering` / `E1_categorical_moderation` / `institutional_shock_lens` / `intra_tmt_persuasion` / `paragraph_layout` / `process_transition_operators` / `reasoning_soundness_protocol`
- `self-drafted` 段计入分母、不计入分子；coverage 偏低时触发重写/修补分支（返回大纲表补底本，或显式登记语料缺口，登记去向见 `corpus/_skill_design_feedback.yaml`）。

**完成判据（是/否）**
- coverage 已计算并在输出末尾记录？
- 豁免段的口径已按上表显式标注（而非默认排除）？
- `self-drafted` 段占比已记录，且 coverage 偏低已触发重写/修补或缺口登记？

## 五、G4 完成判据汇总

对任一次生成，以下每条都能用「是 / 否」回答：

1. 借句表已产出，且每段底本 id 非空（二级 id 或 `self-drafted`）？
2. 全部底本 id 可在 `corpus/_skeleton/<子清单>.md` 定位？
3. G2 四步顺序在借句表「替换清单 / 保留节奏」栏可核对？
4. 「未标注」/`_unparsed` 引用段落已在出处核对列登记？
5. coverage 已计算，豁免口径已显式标注，`self-drafted` 占比已记录？
6. Hard constraints #1–16 已逐条过（实质规则层，见 SKILL.md；本协议判据是其平行执行门，不替代）？

## 指针关系（互链不复制）

- **routing_table**（`corpus/meta/routing_table.md`）：Gap→A–G 路由。本协议不复制路由规则；一级轴由 Phase 1 锁定，G1 底本 id 的族名与之一致。
- **Hard constraints #1–16**（SKILL.md）：实质规则层，见 §头部「平行层」声明；本协议不重述。
- **Soundness 协议**（`corpus/subprotocols/reasoning_soundness_protocol.md`）：前提三分 + 最弱前提防守。G2 落句后由 Phase 4 审计 4 复核；本协议不复制其内容。
- **argument graph**（`references/phase-4-qc-alignment.md`）：construct→premise→why-chain→boundary/level/time→prediction。G2 产出的句段供其挂接；本协议不复制其边约束。
- **conditionality gate**（`references/phase-3-hypothesis-derivation.md` + `corpus/storytelling/post-generation-validator.md`）：G1 借句表启动前已由 Phase 3 执行；本协议不复制 gate 三问。
