# Output Format（Theory & Hypotheses 输出模板）

> 复原自 2026-07-24 前 SKILL.md 的 Output Format 节（653 行版），在 8a1551b 瘦身中丢失，2026-07-28 回归审计后补回。
> 用法：Phase 4 审计通过后，按本模板组织回复。方括号槽位必须具体化；引用性槽位指向 corpus 文件而非复制其内容（协议层不重复语料层）。

```
## Theory & Hypotheses 结构建议（[诊断类型] — [假设结构]）

### 架构决策
| 因素 | 诊断结果 | 结构含义 |
|------|---------|----------|
| 理论域数量 | [单/多] | [progressive coherence / integrated framework] |
| 构念新旧 | [新/已有] | [early placement / flexible] |
| 主角配置 | [IV/DV, 数量] | [DV-first / IV-first / interleaved] |
| 配角配置 | [角色, 数量] | [early / as story unfolds] |
| Context | [角色] | [early / throughout / late] |
| Figure | [类型] | [where discussed / after all hypotheses] |

→ 推荐段落序列: [P1 → P2 → ...]

### 通用 QC
- [ ] Theory IS NOT: [通过/需修复的陷阱]
- [ ] Construct Clarity: [通过/需补充的字段]
- [ ] Hypothesis Clarity: [通过/需补充的字段]
- [ ] Soundness: [最弱前提已防守/已降级/已转显式假设]

### 机制与条件化审计
| 假设 | 推理 moves（非变量数） | 主流简化机制能否推出同一预测 | 本机制的可区分预测 | Conditionality gate | 边界作用于哪一机制 |
|------|----------------------|--------------------------------|--------------------|---------------------|--------------------|
| [H1] | [前提→过程→结果] | [否/是，说明] | [额外预测] | [稳定主效应/条件关系优先] | [不适用/机制 ID] |

如果无法给出可区分预测，机制贡献降级为解释性补充；如果主效应只在特定条件下可推出，则重写为条件假设，不把 moderator 当作装饰性扩展。

### 跨 Section 对齐检查
[Phase 4 对齐输出块]

### 段落功能地图
[引用所选变体及分支的动态功能地图；B 型必须先标 B0 过程解释或 B1 正式中介，不复制不适用的中介槽位]

### 构念界定模板
[引用 `corpus/sentences/construct_definition.md` 推荐变体]

### 理论机制推演模板
[引用 `corpus/sentences/mechanism_chain.md` 与 `corpus/subprotocols/hypothesis_derivation_patterns.md` 的机制推演骨架]

### 假设陈述
[引用 `corpus/sentences/hypothesis_forms.md` 对应形式]

**storyline 绑定（强制，SKILL.md Story gate 要求）**：每个假设必须标注 `storyline_id`（对齐 `story.storylines[*].id`，供 write-methods / write-results 消费）。无对应 storyline 的假设要么挂到最近的 storyline，要么标注为"待补 storyline 契约"——后者触发 paper-state 不写入。

### 证据缺口
列出本次 Theory 构建中无法当场验证、需用户后续补的文献依赖项。每条至少包含：主张 / 需要的证据类型 / 当前状态（placeholder / 待查 / 已有引用但未核验）。
```
- [ ] [主张：机制步骤 N 的 "X 导致 Y"] | 需：[实证/理论文献支撑] | 状态：[placeholder——需用户提供具体引用]
- [ ] [主张：构念 A 与 B 的区分维度] | 需：[对比文献] | 状态：[待查]
```
所有标为 placeholder 的主张在正文中必须保留显式占位（如 `(CITATION NEEDED)`），不得以未验证引用冒充已证。

### paper-state.yaml 片段
按 `corpus/meta/paper_state_fragment.md` 的模板渲染，附在输出末尾供用户复制。字段须与 `paper-state-protocol` 权威 schema 对齐（含 `institutional_background_included`）；每个 hypothesis 带 `storyline_id`。

### 叙事弧线指南（Pollock 2025 Ch02）

Theory section 的 Rising Action 结构（Knot Inheritance→Deepening→Tying→自然收敛）、叙事节奏检查点和 Stroke/Glide 定性判断见 `corpus/storytelling/rising-action-protocol.md`；不得把比例或例子数量设成通过门槛。

**渲染时的附加要求**：
- 在每个段落标题后标注其 narrative function（如 `P1: 构念定义 | Knot Inheritance`）
- 在"提醒"中附加叙事检查点（P1 是否承接 knot？是否有阶段倒退？最后假设是否自然收敛？）

### 期刊适配建议
[基于 --journal 参数的适配建议]

### QC 检查点
- [ ] 每个假设前都有足够的 why-chain reasoning moves（非按变量数量凑步数）？
- [ ] 已在主效应前执行 conditionality gate？
- [ ] 每个 moderator 明确改变哪一机制，而非被强制复用机制全集？
- [ ] 构念界定包含 scope conditions + lineage + adjacent construct 区分？
- [ ] 假设形式匹配变量类型和理论关系？
- [ ] 最后一个假设/命题是否自然收束（非突然中断进入 METHODS）？
- [ ] [类型专属 QC 检查点...]

### 措辞润色建议
骨架与 QC 完成后、输出前默认执行（见 SKILL.md `## 措辞润色`）。按句位分区查 `corpus/sentences/` 与 write-introduction 的 phrasebank，**不覆盖原文**，只为关键句位（构念定义 / why-chain 步骤 / 假设句 / 让步反论 / 段首回扣句）提供 ≤2-3 个措辞变体 + hedging 强度校准。输出形式：
```
| 句位 | 原句（节选） | 候选变体 | 说明 |
|------|-------------|---------|------|
| [P3 why-chain step 2] | "[原句]" | ①…②… | [hedging 强度 / specificity gate 提示] |
```
纪律：骨架优先，语料库只提供措辞变体不替代论证结构；hedging 不突破 causal-hedging 设计家族上限。
```
