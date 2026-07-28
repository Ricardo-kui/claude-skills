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

### 跨 Section 对齐检查
[Phase 4 对齐输出块]

### 段落功能地图
[引用所选调型 corpus/variants/ 文件中的段落功能地图]

### 构念界定模板
[引用 `corpus/sentences/construct_definition.md` 推荐变体]

### 理论机制推演模板
[引用 `corpus/sentences/mechanism_chain.md` 与 `corpus/subprotocols/hypothesis_derivation_patterns.md` 的机制推演骨架]

### 假设陈述
[引用 `corpus/sentences/hypothesis_forms.md` 对应形式]

### 叙事弧线指南（Pollock 2025 Ch02）

Theory section 的 Rising Action 结构（Knot Inheritance→Deepening→Tying→自然收敛）、叙事节奏检查点和 Stroke/Glide 比例指南见 `corpus/storytelling/rising-action-protocol.md`。

**渲染时的附加要求**：
- 在每个段落标题后标注其 narrative function（如 `P1: 构念定义 | Knot Inheritance`）
- 在"提醒"中附加叙事检查点（P1 是否承接 knot？是否有阶段倒退？最后假设是否自然收敛？）

### 期刊适配建议
[基于 --journal 参数的适配建议]

### QC 检查点
- [ ] 每个假设前都有 why chain？
- [ ] 构念界定包含 scope conditions + lineage + adjacent construct 区分？
- [ ] 假设形式匹配变量类型和理论关系？
- [ ] 最后一个假设/命题是否自然收束（非突然中断进入 METHODS）？
- [ ] [类型专属 QC 检查点...]
```
