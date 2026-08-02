# Phase 4.5 — 回写提醒

> 外置自 `distill-theory-exemplar/SKILL.md`。何时加载：Phase 4.5 执行回写时加载。

---

## Phase 4.5 — 回写提醒

当 Phase 2–4 的蒸馏产出满足以下全部条件时，在报告末尾生成回写提醒，建议用户将新发现的模式手动沉淀到 `write-theory` 的模块库：

### 触发条件

1. **骨架通过生成力验证**（Phase 2.4 裁决为"通过"）
2. **跨论文复现 ≥ 2 篇**（或批量模式下同一构建类型内 ≥ 2 篇）
3. **构建类型明确**（非 "ambiguous between X and Y"）
4. **模块功能归属明确**（T1–T6 或 T6-Variant 之一，非 "unclassified"）
5. **与当前 write-theory v3.3.0 不冲突**——回写前必须对照 write-theory 当前版本的约束（如 T6 Closure 非强制、文献引用以交织式为默认等）

**不触发回写提醒的情况**：
- 仅 1 篇论文中出现的模式 → 留存为 Vault 参考注释，积累到 ≥3 篇后再提醒
- 构建类型模糊的论文 → 标记为 "pending_type_clarification"
- 骨架批评家裁决为"需修正/不纳入" → 不回写
- **与 write-theory 当前版本核心约束冲突** → 标记为 "pending_protocol_revision"，先更新 write-theory 或降级为"可选变体"，不回写为默认规则

### 回写分类：默认规则 vs 可选变体

| 类型 | 判断标准 | 回写位置 |
|------|---------|---------|
| **默认规则** | ≥3 篇跨期刊论文一致，且与 write-theory 当前约束兼容 | 更新 `SKILL.md` Constraints / Phase 默认结构 |
| **可选变体（架构级）** | 2-3 篇论文一致但存在期刊/类型特异性，或与当前约束不完全兼容 | 写入 `corpus/variants/` 或 `corpus/subprotocols/` 作为变体 |
| **可选变体（句式级）** | 2-3 篇论文一致的句位级措辞（topic 句 / why-chain transition / 假设句 / Wrap 句写法，见 Phase 2.2b） | 写入 `corpus/sentences/[对应文件]`（见下表"句式级回写落点"） |
| **待审阅** | 仅 1 篇出现，或样本有偏 | 只入 Vault 注释，不入 skill |
| **不采纳** | 与已验证的顶刊惯例明显冲突（如独立 T6 段落） | 不写入，仅记录为反模式 |

#### 句式级回写落点（sentences/ 文件路由）

句位级句式变体（Phase 2.2b 提炼）按句位路由到 write-theory 的 `corpus/sentences/` 对应文件：

| 句位（Phase 2.2b） | 回写文件 | 现有内容示例 |
|-------------------|---------|-------------|
| Topic 句（段首论点句写法） | `sentences/leitmotif-section-opener.md`（多假设共享构念的段首回扣）/ `sentences/construct_definition.md`（T1 构念定义段 topic） | "We argue that [IV] [direction] [DV] through [mechanism]" |
| Why-chain transition 句（机制步骤间过渡） | `sentences/mechanism_chain.md`（连接词谱系 + 步骤过渡句式） | "Consequently, ... This in turn ..." |
| 假设句（H 陈述形式） | `sentences/hypothesis_forms.md`（决策矩阵 + 模板句） | 见该文件 1-3 节决策表 |
| Wrap 句（段末总结/收束） | `sentences/closure.md`（局部收束信号） | "Taken together, these arguments suggest ..." |
| 让步-回应句（异议处置） | `sentences/acknowledgment_response.md` | "One might argue that ... However, ..." |
| 调节机制句（high/low 条件论证） | `sentences/moderation.md` | "When [W] is high, ... ; when [W] is low, ..." |

> **与架构级回写的分工**：架构级（variants/subprotocols）回写"段落/假设怎么组织"（如 common trunk → parallel branches）；句式级（sentences）回写"每一句怎么写"。同一篇论文的蒸馏产出可能同时含两类——架构骨架入 subprotocols，句式变体入 sentences，不要混放。

**回写前冲突检查清单**：
- [ ] T6 相关骨架：是否与 write-theory "不要求独立 Closure 段" 兼容？
- [ ] 文献引用节奏：是否支持"交织式"而非"分离式四段式"？
- [ ] 模块标签：是否允许无 "Theory and Hypotheses" 标题的主题标题进入？
- [ ] Institutional Background：是否作为可选前置模块而非 Theory 的一部分？
- [ ] Closure 信号：是否区分"假设段局部收束"与"全文独立 Closure 段"？

### 回写操作（手动 + 结构化预览）

满足条件后，蒸馏报告会在 `corpus_recommendations` 区块中为每个可沉淀模式生成一个**可直接 append 到 write-theory corpus 的 markdown 条目预览**。用户执行：

1. 对照报告中的 `pattern_id` 和 Vault 中已有条目，判断是否重复
2. 确认 `corpus_path`、`build_type`、`confidence` 标注正确
3. 复制 `entry_preview` 到对应 corpus 文件末尾
4. 更新 `write-theory` 的模块索引（如适用）

**生成的条目必须包含**：
- `pattern_id`（唯一标识）
- `build_type`（适用构建类型）
- `source_papers`（来源论文）
- `适用场景`（一句话说明）
- `骨架`（可填充的句法结构）
- `为什么有效`（说服逻辑）
- `注意事项`（边界和风险）
- `反模式`（不该用的情况）

**不自动执行写入**。模型只生成预览，最终写入由用户审核后完成。

**示例条目预览格式**（以 Shen_etal_2022_JOM 的 Parallel Moderation 为例）：

```markdown
<!-- 
pattern_id: parallel_moderation_from_three_mechanism_trunk
build_type: 机制推演型 + 调节效应型
source_papers: ["Shen_Zhou_Wang_Zhang_2022_JOM"]
confidence: medium
-->

### Parallel Moderation from a Three-Mechanism Trunk

**适用场景**: 主效应有多个并行的机制路径，需要用多个 moderators 分别检验每条路径的边界条件。
**排列模式**: Common Trunk → Parallel Branches
**范文来源**: Shen, Zhou, Wang, and Zhang (2022), *Journal of Operations Management*

**骨架**:
```
[Mechanism Trunk]
We argue that [IV] [direction] [DV] through three mechanisms: 
(1) [mechanism 1], (2) [mechanism 2], and (3) [mechanism 3].

[Branch for Moderator W1]
These effects, however, are contingent on [W1]. When [W1] is high, 
[mechanism 1]: ...; [mechanism 2]: ...; [mechanism 3]: ...
Therefore, H[X]: ...

[Branch for Moderator W2]
Similarly, [W2] alters the relationship because ...
[mechanism 1]: ...; [mechanism 2]: ...; [mechanism 3]: ...
Therefore, H[X+1]: ...
```

**为什么有效**: 读者先在 H1 理解完整的机制 trunk，之后每个 moderator 只需说明它如何改变 trunk 的每个分支，避免重复建立新机制。
**注意事项**: 
- 每个 branch 必须回到 trunk 的机制分别论证，不能只笼统说 "W moderates the relationship"
- 建议用元框架（如 environmental/organizational 或 supply/demand）组织多个 moderators
**反模式**: 如果 moderators 之间没有 conceptual 联系，不要强行 parallel，应改为假设树型逐个引入。
```

**句式级回写条目预览格式**（以 Phase 2.2b 提炼的 why-chain transition 句式为例，回写到 `write-theory/corpus/sentences/mechanism_chain.md`）：

```markdown
<!-- 
pattern_id: why_chain_step_chaining_this_in_turn
build_type: 跨类型（句式级）
source_papers: ["Shen_etal_2022_JOM", "Keeves_etal_2017_AMJ"]
confidence: medium（2 篇复现，待第 3 篇升 VERIFIED）
sentence_position: why_chain_transition
-->

### Why-Chain 步骤链接句式："This, in turn, ..."

**句位**: 假设推导段 Topic→Reasoning 内，多步机制链的步骤间过渡（区别于因果收敛的 "Therefore"）。

**句式骨架**:
```
[Step 1] [IV] creates [state 1], which [effect].
[Transition] This, in turn, [step 2: how state 1 produces state 2] because [reason].
[Transition] Consequently, [final step to DV].
```

**变体**（同句位的 2-3 个措辞候选）:
- "This, in turn, ..." — 标记链式递进（比 "Furthermore" 更精确，强调因果传递）
- "Through this process, ..." — 标记机制过程性
- "These dynamics suggest that ..." — 标记从机制动态到预测的桥接

**为什么有效**: "This, in turn" 显式标记前一步的输出是后一步的输入，防止 read-my-mind 跳跃；比泛用 "Moreover" 更精确地传递因果链而非简单并列。

**注意事项**: 仅用于真正的链式因果（step 1 → step 2 → step 3）；若是并列多机制（width-type），应用 "First... Second... Third..." 而非 "in turn"。

**反模式**: 用 "This, in turn" 连接两个无因果传递的并列机制（伪装并列为链式）。
```

> **句式级条目 vs 架构级条目的格式差异**：句式级条目多了 `sentence_position` 字段（标明 Phase 2.2b 的句位）和"变体"小节（同句位的 2-3 个措辞候选，供 write-theory 措辞润色阶段选用）；骨架更短（单句级而非段落级）。生成力验证（Phase 2.4）同样适用——占位符填充后应能生成功能等价的句子。

### 构建类型分桶

新发现的骨架必须在同一构建类型内比较和累积：

| 构建类型 | 分桶 | 聚类依据 | 示例 |
|----------|--------|---------|------|
| 构念辨析型 | `bucket_construct` | "Whereas A..., B..." 对比句式 | T1 构念区分骨架 |
| 机制推演型 | `bucket_mechanism` | "X creates M—a [state]—that [action]" 因果链 | T3 两步中介骨架 |
| 假设树型 | `bucket_tree` | "not uniform; rather, contingent on" 条件化 | T5 调节引入骨架 |
| 质性过程理论型 | `bucket_process` | "Phase 1... Phase 2..." 时间阶段 | T3 过程阶段骨架 |
| 调节效应型 | `bucket_moderation` | "when W is high/low" 条件预测 | T4 交互假设骨架 |

**跨桶规则**：
- 同一骨架被多个构建类型的论文使用（如局部收束信号 "Therefore, we hypothesize:"），标记为 `跨类型`，可跨桶回写
- 范式排他性骨架（如构念辨析型的 "differentiation dimensions"）**绝不**跨桶回写
- **注意**：write-theory v3.3.0 已取消"T6 Closure 作为独立模块"的强制要求。回写时，"Taken together, our theory posits..." 类骨架只能作为"嵌入最后假设段末尾的可选 2-3 句框架总结"标记，不能作为独立 T6 段落推荐。

### 诚实边界（回写专用）

- **不将单篇模式写入推荐列表**：仅 1 篇论文中出现的模式留在 Vault 参考注释中，标注为"待审阅"，不进入 `write-theory` 的推荐映射
- **不覆盖已有模块**：遇到同名或同功能模块时，生成 `_alt` 变体条目，由用户决定合并或保留
- **不虚构跨论文复现**：来源论文数基于 Vault 中实际 narrative 文件数，如有偏（如某领域论文过多）应如实注明
- **必须人工确认构建类型标注**：Phase 0 分类推断可能错误，用户必须逐条检查
- **不回流机制内容**：骨架中嵌入特定论文机制名称的，必须清理后再写入
- **跨桶回写必须标记**：`跨类型` 骨架在模块索引中标注 `[跨类型]`，提醒该骨架的普适性尚未在所有构建类型中验证
- **句式级回写遵守 dedup_status**（Phase 2.2b 比对结果）：`existing_match` 仅追加 source_papers（凑 VERIFIED 篇数），**不重复回写句式条目**；`new_variant` 按门槛回写为新增；`near_dup` 标注与现有句式的差异点，由用户决定合并为变体还是单列。同源分流：Phase 2.2b 已判定某句式归架构级（variants/subprotocols）还是句式级（sentences）——归架构级的，句式级只回写措辞变体部分，不整句重复。

---
