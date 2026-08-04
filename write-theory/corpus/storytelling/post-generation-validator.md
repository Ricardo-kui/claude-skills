---
type: validator
canonical_id: "theory-post-generation-validator"
source: "Pollock 2025 Ch02-Ch06 + reasoning soundness protocol"
created: 2026-06-01
updated: 2026-08-03
version: 2.0.0
---

# Theory 后生成验证器 v2

## 目的与触发

完整 Theory & Hypotheses 骨架生成后必须执行。本验证器审查故事连续性、构念清晰度、机制解释力、条件化、假设可检验性与跨章节契约。它不按关键词、固定段落数、变量数量或修辞配额替代理论判断。

状态：

- **PASS**：关键条件满足。
- **WARN**：可以输出，但须标出局限与修复建议。
- **FAIL**：故事契约、核心推理或假设形式存在会使后续 Methods/Results 失真的问题；修复后再写入 paper-state。
- **N/A**：该检查不适用，必须说明理由。

## 规范输入

优先读取：

```yaml
story:
  central_knot: ...
  protagonist: ...
  contribution_claims: [...]
  storylines:
    - id: ...
      question: ...
      promised_mechanism: ...
theory:
  paragraphs:
    - id: P1
      dominant_function: knot_inheritance | construct_definition | mechanism | boundary | competing_logic | hypothesis_derivation
      text: ...
  constructs: [...]
  hypotheses:
    - id: H1
      storyline_id: ...
      statement: ...
      derivation_paragraphs: [...]
  mechanism_chains: [...]
```

旧字段（如 `central_knot_statement`、`protagonist_construct`）只能经 `paper-story-contract` 的 migration map 临时迁移；验证输出和 paper-state 只写 canonical `story`。没有 canonical story 时，只允许 local-only 诊断，不更新 paper-state。

## 验证 1：Story contract 与 storyline 绑定

检查：

- Theory 开篇是否继承 `story.central_knot` 的实质问题，而非仅重复相同词语？
- protagonist、核心关系与 contribution claims 是否一致？
- 每个 H/Proposition 是否有有效 `storyline_id`？
- 新增主角、结果或理论承诺是否已更新 story contract？
- Theory 的段落功能是否总体呈现 knot inheritance → deepening → tying；不要求固定 P1/P2–P4 槽位。

判定：缺 story 或孤立假设为 FAIL；措辞不同但实质一致不扣分；只靠承接信号词不能 PASS。

## 验证 2：构念角色、顺序与清晰度

对每个核心构念记录：

| 构念 | 角色 | 层级 | Definition | Scope | Lineage | Adjacent differentiation | 新构念 justification |
|------|------|------|------------|-------|---------|--------------------------|----------------------|

规则：

- 主角先于依赖它才能理解的机制/边界出场；实际顺序按理论任务动态决定。
- 定义不得循环，也不得把 antecedent 或 consequence 写进定义。
- 跨层关系必须说明 focal unit、nesting 与传递机制。
- 新构念缺 definition、differentiation 或 justification 任一项为 FAIL；既有构念缺必要 scope 为 WARN/FAIL，取决于是否改变预测。

## 验证 3：Hypothesis derivation trace

为每个假设建立 trace：

```text
理论前提 → 行动者/过程状态变化 → 结果或条件预测 → 正式假设
```

一个 reasoning move 是有内容、可质疑的推理转换，不是变量数、箭头数、连接词数或同义改写。检查：

- 是否至少有足够的 moves 将前提连接到预测（常见最低为 2；简单但充分的链不因未满固定数字失败）？
- 每个 move 的 warrant/证据承担什么功能？
- 相邻 moves 是否遗漏必要的行动者、层级或时间转换？
- 假设句是否确实由 trace 收敛，而非在最后改变方向、形状或条件？

只列 findings、模型变量或引用为 FAIL。连接词存在不等于推理成立。

## 验证 4：机制必要性与可区分性

对声称贡献的每条机制执行三问：

1. 领域内更简单或主流的机制能否推出同一核心预测？
2. 本机制是否导出至少一个额外、可区分的预测（边界、时间、结果维度、非线性、行动者差异等）？
3. 删除本机制后，故事和假设是否几乎不变？

判定：

- 三问均显示机制做了独特理论工作 → PASS。
- 机制增强解释但尚无可区分预测 → WARN，并将“机制贡献”降级为解释性补充。
- 删除后无影响或只是给路径改名 → FAIL；删掉装饰性机制或重建预测。

同时检查最弱前提与替代机制，具体按 `../subprotocols/reasoning_soundness_protocol.md` 输出 Soundness Card。

## 验证 5：Conditionality 与 boundary gate

在审查主效应及每个 moderator 前回答：

1. 核心机制是否有理论依据在声明 scope 内稳定运作？
2. 是否有条件改变暴露、注意、能力、动机、解释或约束？
3. 该条件是否改变预测的方向、强度、形状或有效性？
4. 去掉条件后，仍能推出有内容的平均关系吗？

决策：

- 1=是、4=是：主效应可作 trunk；边界假设按需增加。
- 2–3=是、4=否：条件关系必须是主预测；无条件主效应仅可作为有依据的基线。
- 2 或 3 无依据：moderator 为装饰性变量，FAIL。
- 识别出边界不等于必须新增假设；若不在贡献与设计范围内，可写 scope condition，并记录未检验边界。

## 验证 6：假设形式、可检验性与竞争逻辑

每个 H/Proposition 检查：

- IV/DV 或比较对象明确；方向、形状、条件、时间窗和分析层级按需明确。
- 形式与构念类型和测量尺度匹配；不把 differential validity 写成 differential prediction。
- 理论关系与拟检验关系一致；统计实现留给 write-methods。
- 反命题具有可争辩性；纯主题、显然事实或伪争议不得作为假设。
- 竞争假设公平呈现双方的强版本，并能由设计裁决。

收敛语句按语境判断：单向推导可用 `Therefore/Accordingly`；竞争预测应用 `Given these competing arguments...` 等并列信号。不要仅用关键词扫描判定。

## 验证 7：段落功能与 prose 风险

按 `dominant_function` 动态审查每段，而非假定固定 P2–P4：

- 每段是否有一个主导理论任务？
- topic sentence 是否尽早给出本段主张，证据是否服务于该主张，段末是否完成推理或过渡？
- 是否出现 references/data/variable lists/diagram/hypotheses as theory？
- 是否有 burying the lead、sentence stuffing、read-my-mind、术语漂移或防御性技术说明文风？
- concrete illustration 是否在跨层、反直觉或抽象处真正降低理解负担？

词数、15/30 词阈值、stroke/glide 比例、例子数量均为诊断提示，不是自动 FAIL 条件。没有例子不自动失败；用案例替代理论或证据则失败。

## 验证 8：跨假设机制映射

适用于多个假设共享 trunk 的结构。先为 trunk 机制赋 ID，再记录：

| 假设 | 使用/改变的机制 ID | 作用点 | 方向 | 未触及机制的处理 | 可区分预测 |
|------|-------------------|--------|------|------------------|------------|

规则：

- 后续假设必须明确回到它实际使用或改变的 trunk 机制。
- **不要求**每个 moderator 复用 trunk 的全部机制。选择性改变一条路径常常正是理论贡献。
- 选择性复用时须解释为什么该条件作用于这条机制而非另一条；未触及路径只有在会影响净预测时才需显式处理。
- 若文字声称“改变整个关系”却只论证一条路径，或净方向无法从路径组合推出，为 FAIL。

## 验证 9：跨 Section 契约与 paper-state

检查 Introduction → Theory → Methods/Results 的接口：

- 每个 contribution claim 是否有 Theory 模块承担？
- 每个 promised mechanism/boundary 是否被实现或显式修订？
- construct 名称、角色、层级、关系形式是否稳定？
- figure 中每条路径是否标 hypothesis ID？
- `paper-state.yaml` 中每个 hypothesis 是否含 `storyline_id`、statement、construct roles、relationship form 与 mechanism mapping？

未解决的契约冲突为 FAIL；仅措辞差异为 WARN/修订建议。

## 输出格式

```markdown
### Theory 后生成验证

| # | 检查 | 状态 | 证据（段落/假设） | 诊断 | 最小修复 |
|---|------|------|------------------|------|----------|
| 1 | Story contract | PASS/WARN/FAIL | [...] | [...] | [...] |
| 2 | Construct clarity | ... | ... | ... | ... |
| 3 | Derivation trace | ... | ... | ... | ... |
| 4 | Mechanism necessity | ... | ... | ... | ... |
| 5 | Conditionality | ... | ... | ... | ... |
| 6 | Hypothesis form | ... | ... | ... | ... |
| 7 | Paragraph/prose | ... | ... | ... | ... |
| 8 | Cross-H mechanism map | ... | ... | ... | ... |
| 9 | Cross-section contract | ... | ... | ... | ... |

**总状态**：[PASS / WARN / FAIL]
**最高优先级修复**：[只列最能恢复理论有效性的一项]
**paper-state**：[可写入 / 暂停写入及原因]
```

## 修复优先级

1. story/lineage 和孤立假设；
2. 推理断裂、装饰性机制、无依据主效应或 moderator；
3. 假设形式与测量/层级不匹配；
4. 跨假设、图和跨章节不一致；
5. 段落节奏与措辞。

不得用 prose 润色掩盖前四类问题。

## 更新日志

- **v2.0.0** (2026-08-03): 改用 canonical story 与动态段落功能；将机制深度从变量数量中分离；加入 mechanism necessity、conditionality/boundary、form-measurement 与契约审计；修正“所有 moderator 必须复用全部 trunk 机制”的错误规则；取消关键词、固定槽位和修辞配额式自动判定。
- **v1.0.0** (2026-06-01): 初始验证器。
