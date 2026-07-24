# Phase 2: theory extraction

> Imported from the upstream protocol. Resolve relative resource paths from this reference file's directory.

## Phase 2 — 深度提炼：模块功能、表达骨架、Theory Logic

对 Phase 1 定位到的每个功能模块，执行五重提炼：模块功能 → 论证节奏 → 表达骨架 → Theory Logic → 连接词模式。2.4 骨架批评家对所有提炼出的骨架执行生成力验证。

> **核心聚焦：假设推导段落（Hypothesis Derivation）是 Theory 部分的心脏。**
> 
> T1 和 T2 是为假设推导服务的舞台搭建，T3/T4 是假设推导的本体，T5 是假设推导的边界精确化，T6（局部收束）是假设推导的自然终点。本 skill 的绝大多数提炼资源应投向 **T3/T4 假设推导段落**：如何构建严密的 why chain、如何安排论点与论据、如何用词和连接词推进段内逻辑、如何让假设从机制中自然收敛。
> 
> 因此，Phase 2.1.5–2.1.8（论证节奏、微观动作、安排模式、证据编码）不是并列的附加模块，而是**假设推导过程的四个分析维度**。

### 2.1 模块功能提炼（Persuasive Action）

回答：这个模块完成了什么**理论说服动作**？

| 说服动作 | 适用模块 | 示例 |
|----------|----------|------|
| 概念锚定 | T1 Construct Definition | 让读者明确知道"我们在讨论什么"，排除歧义 |
| 解释框架建构 | T2 Theoretical Lens | 建立"用什么理论视角看问题"的认知框架 |
| 因果逻辑推演 | T3 Mechanism Chain | 逐步展示"为什么 X 导致 Y"，让读者跟随推理 |
| 预测形式化 | T4 Hypothesis Derivation | 将机制推演固化为可检验的预测声明 |
| 适用范围限定 | T5 Boundary Condition | 防止过度概括，增加理论精确性 |
| 整体框架锁定 | T6 Closure | 将分散的假设整合为统一的理论叙事 |

> **论证节奏提炼（2.1.5）、假设论证微观动作提取（2.1.6）、论点-论据安排模式提取（2.1.7）、证据类型与功能编码（2.1.8）** 四个提取框架已外置：见 `../protocols/phase2_extraction_frameworks.md`。执行 Phase 2 深度提炼时加载。

### 2.2 表达骨架提炼（Expression Skeleton）

**即时捕获原则（Inline Capture）**：借鉴 grill-with-docs "Update CONTEXT.md right there. Don't batch these up"——在 Phase 2 阅读到每个模块时，**立即提炼骨架**，不等到 Phase 4 再汇总。这防止模式遗忘和细节流失。

将具体措辞抽象为**可填充的句法结构**。**注意**：Theory 的骨架是模块级的推理模式，不是段落级的——同一功能模块可以在不同论文中由不同数量的段落完成。

**骨架格式**：
```text
[功能标签]: T3 Mechanism Chain — 两步中介机制（机制推演型）
[骨架]: Drawing on [theory] ([citation]), we argue that [IV] creates [mechanism state]—a [definition of mechanism state]—that [action/implication]. Specifically, [step 1: how IV creates mechanism state]. [Theoretical justification]. Consequently, [step 2: how mechanism state affects DV]. [Theoretical justification]. Therefore:
[假设嵌入]: [Hypothesis]: [IV] is [positively/negatively] related to [mediator].
[可迁移性]: 高 — 出现在 8/28 篇机制推演型范文中
[范式排他性]: 机制推演型专用，构念辨析型不应使用此骨架
[构建类型变体]:
  - 构念辨析型: "We differentiate [Construct A] from [Construct B]. Whereas [A] entails [definition], [B] involves [definition]. This distinction matters because [theoretical consequence]."
  - 假设树型: "The effect of [IV] on [DV] is not uniform; rather, it is contingent on [moderator]. When [moderator condition], [theoretical mechanism] suggests that [prediction]."
  - 质性过程理论型: "The relationship between [IV] and [DV] unfolds through [N] phases. In Phase 1, [process]. As [transition condition], the process shifts to Phase 2, where [process]."
[问题对应]: Dorobantu Q — "WHY should we expect these relationships between constructs (mechanisms)?"
```

**必须记录的信息**：
- 骨架句法（用方括号标记占位符）
- 可迁移性评分（高/中/低）及证据（出现频次）
- 范式排他性（该骨架是否只为某类构建类型所需）
- 构建类型变体（同类骨架在不同构建类型中的改写模式）
- **问题对应**：该骨架回答 Dorobantu et al. (2024) 研究设计问题链中的哪个问题

### 2.3 Theory Logic 提炼

提取该 Theory 如何处理三类理论论证问题：

| 理论问题 | 提炼问题 | 对应 Dorobantu 问题 |
|----------|----------|---------------------|
| Why Chain 完整性 | 从构念到假设的推理是否每一步都有理论依据？是否有"常识跳跃"？ | "WHY should we expect these relationships?" |
| Construct Clarity | 构念定义是否包含 scope condition？是否区分了易混淆构念？ | "WHAT are the key constructs?" |
| Theory-Citation Relationship | Citation 是支持故事还是构成故事？是否存在 citation list 代替机制？ | "What theoretical lens orients the framework?" |

输出格式：
```yaml
phase_2_distillation:
  T3_mechanism_chain:
    persuasive_action: "因果逻辑推演"
    expression_skeletons:
      - skeleton: "..."
        transferability: "高 (8/28)"
        paradigm_exclusivity: "机制推演型专用"
        build_type_variants: ["构念辨析型版本", "假设树型版本", "过程理论型版本"]
        dorobantu_question: "WHY should we expect these relationships between constructs?"
    theory_logic:
      why_chain_integrity: "..."
      construct_clarity: "..."
      theory_citation_relationship: "..."
  # ... 其余模块
```

### 2.4 骨架生成力验证

每个 Phase 2.2 提炼出的骨架必须经过**生成力验证**，才能进入 Phase 3。

**验证流程**：

1. **占位符填充测试（Generativity Test）**
   - 将骨架中的 `[占位符]` 填入该论文的具体内容（构念名、理论名、机制名）
   - 生成一个"模拟段落"
   - 对比模拟段落与原文段落：是否保留了相同的**理论说服动作**？
   - 如果填入后生成的段落与原文功能等价 → 通过；如果丢失了关键说服动作 → 需修正

2. **机制内容污染检查（Mechanism-Content Test）**
   - 骨架中是否嵌入了该论文特有的具体机制内容（如 "performative tension"）而非组织方式？
   - 是否将具体理论发现提炼成了"通常使用三步链"等伪规则？
   - 如果有 → 需修正，保留组织方式，去除机制内容

3. **构建类型匹配检查（Type-Fidelity Test）**
   - 骨架的推理模式是否与判定的构建类型匹配？
   - 例如：构念辨析型骨架中出现了因果链语言 → 不纳入（模式错配）

**裁决格式**：

```yaml
phase_2_4_skeleton_check:
  skeleton_id: "T3_mechanism_chain_mediation"
  verdict: "通过 / 需修正 / 不纳入"
  verdict_reason: "..."
  generativity_test:
    mock_paragraph_generated: true/false
    persuasive_action_preserved: true/false
    notes: "..."
  mechanism_content_test:
    content_contamination: ["performative tension", "absorptive capacity"]
    contamination_cleared: true/false
  type_fidelity_test:
    build_type_match: true/false
    mismatch_details: "..."
```

**裁决标准**：

| 裁决 | 条件 | 后续动作 |
|------|------|----------|
| **通过** | 三项测试全部通过 | 骨架进入 Phase 3 和 Phase 4 |
| **需修正** | 生成力或机制内容测试未通过，但可通过改写修复 | 标记后在 Phase 4 中尝试改写后重新验证 |
| **不纳入** | 构建类型错配，或过度抽象失去生成力 | 丢弃，不进入语料库 |

**注意**：裁决记录存入 Vault 的 `vault_enrichment`，供 Phase 4 跨论文聚合使用。

> **连接词使用模式提炼（2.5）**已外置：见 `../protocols/connector_patterns.md`。Phase 2 骨架提炼完成后执行连接词分析时加载。
