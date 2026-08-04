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
[抽象层级]: "L0 invariant / L1 route / L2 optional architecture / L3 model signature"
[Incommensurability 路由适配]: "R1 / R2 / R3 / R4 / cross-route / n.a."
[范式排他性]: 机制推演型专用，构念辨析型不应使用此骨架
[构建类型变体]:
  - 构念辨析型: "We differentiate [Construct A] from [Construct B]. Whereas [A] entails [definition], [B] involves [definition]. This distinction matters because [theoretical consequence]."
  - 假设树型: "The effect of [IV] on [DV] is not uniform; rather, it is contingent on [moderator]. When [moderator condition], [theoretical mechanism] suggests that [prediction]."
  - 质性过程理论型: "The relationship between [IV] and [DV] unfolds through [N] phases. In Phase 1, [process]. As [transition condition], the process shifts to Phase 2, where [process]."
[问题对应]: Dorobantu Q — "WHY should we expect these relationships between constructs (mechanisms)?"
```

### Incommensurability 反过拟合抽象

先用 `../../write-theory/references/incommensurability-resolution-routes.md` 生成 L0–L3 profile，再提炼 T3/T4：

1. L0 只保留 rival-account chains、exact incompatibility、resolution operator、combination rule 与 distinguishing prediction。
2. L1 用 R1–R4 缩小可比较范文范围，不直接选择 A–G。
3. L2 记录 paired/differential/competing/nonlinear/conditional/proposition 等架构，并写 `necessity_warrant` 与被排除的更简单形式。
4. L3 记录具体构念、理论、H 编号/数量、mediator/moderator、方程和测量；L3 仅作 evidence anchor。
5. 执行 construct substitution、hypothesis-count invariance、model-form necessity、simpler architecture、discriminating prediction、measurement firewall 六项检验。

若一个骨架只能复现来源论文的变量图而不能迁移其推理操作，降为 L3。若多篇同路线论文复现相同架构但跨路线并非必要，保留为 L2 optional architecture。只有跨路线复现的推理功能才可成为 L0 core candidate。

**必须记录的信息**：
- 骨架句法（用方括号标记占位符）
- 可迁移性评分（高/中/低）及证据（出现频次）
- 范式排他性（该骨架是否只为某类构建类型所需）
- 构建类型变体（同类骨架在不同构建类型中的改写模式）
- **问题对应**：该骨架回答 Dorobantu et al. (2024) 研究设计问题链中的哪个问题

### 2.2b 句位级句式提炼（Sentence-Position Expression Variants）

> **为什么需要 2.2b**：Phase 2.2 提炼的是**模块级骨架**（一个功能模块怎么组织）。但顶刊的"句式表达"优势常在**句子级**——同一个 Topic 句位、同一个 why-chain transition，不同论文有不同的高质量措辞。2.2b 提炼这些句位级变体，使其能回写到 `write-theory/corpus/sentences/`（2.2 模块级骨架回写 variants/subprotocols，层次不同，不能混）。对应 write-theory 的段内四段位（Topic→Reasoning→Tokens→Wrap，见 `write-theory/corpus/subprotocols/paragraph_layout.md`）。

**即时捕获原则**：与 2.2 相同，阅读到高质量句式时**立即记录**，不等到 Phase 4。

**提取前提——先比对现有 sentences（防重复提炼）**：开始提炼前，按本论文构建类型预判可能命中的句位，load write-theory 对应 `corpus/sentences/` 文件（如机制推演型预 load `mechanism_chain.md` + `hypothesis_forms.md`；调节效应型加 load `moderation.md`）。提炼每个句式变体时**标注其与现有内容的去重新旧**：
- `status: existing_match` —— sentences 文件已有同义句式（如已有 "We argue that [IV] [direction] [DV]"），本篇仅作复现印证，**不重复回写**，只在 Phase 4 的 source_papers 追加本篇（凑 VERIFIED 篇数）
- `status: new_variant` —— 现有文件无此句式（措辞或句法结构不同），标注为新增候选，按 writeback_reminders 句式级门槛回写
- `status: near_dup` —— 与现有句式高度相似但有细微措辞差异（如 "We propose" vs "We argue"），标注差异点，由 Phase 4 决定合并为变体还是单列

> 此步骤确保 2.2b 不提炼已有句式的重复副本。Phase 4 的跨论文验证仍照常执行（复现计数），但"已有"判定提前到提取阶段。

**同源分流规则（架构级 vs 句式级，防同源内容双提）**：当一句式既是段落级骨架的核心句（Phase 2.2 架构级）、又是句位级措辞变体（Phase 2.2b）时，按以下优先级分流，避免同源内容双提：
- **优先归架构级**：若该句式是某架构骨架（variants/subprotocols）的标志性开场/收束（如 G 辩证对立型的 reconciliation 句"To resolve... we theorize that [logic A] and [logic B] pertain to different facets of [construct]"），归 Phase 2.2 架构级，**2.2b 不再整句提炼**，只取其**措辞变体部分**（如 "pertain to different facets" / "integrate... by" 等可替换短语）作为句式级补充
- **句式级独立留存**：若该句式不是任何架构骨架的标志句（只是通用段位句式），归 Phase 2.2b 句式级独立提炼
- **判定问句**："去掉这句话，某个 variants/subprotocols 骨架会缺一个标志性动作吗？" 是 → 架构级；否 → 句式级

**四个句位 × 提炼要求**：

| 句位 | 对应 write-theory 段位 | 提炼什么 | 回写目标（见 writeback_reminders 句式级落点表） |
|------|----------------------|---------|----------------------------------------------|
| **Topic 句**（段首论点句） | Topic | 段首句如何用 active verb + concrete subject 给出核心判断；非元评论、非作者名开头的写法 | `sentences/leitmotif-section-opener.md` / `sentences/construct_definition.md` |
| **Why-chain transition 句**（机制步骤间过渡） | Reasoning | 步骤间用什么连接词/句式标记因果传递（"This, in turn" / "Consequently" / "Through this process"）；与 Phase 2.5 连接词分析互补——2.5 计密度，2.2b 提具体句式变体 | `sentences/mechanism_chain.md` |
| **假设句**（H 陈述） | Wrap（收敛终点） | 假设陈述的措辞形式（if-then / continuous / curvilinear / difference）；方向与形式的精确表达 | `sentences/hypothesis_forms.md` |
| **Wrap 句**（段末总结/收束） | Wrap | 段末如何回扣 Topic 并引出假设（"Taken together, these arguments suggest..."）；区分局部收束与全文 Closure | `sentences/closure.md` |

**提炼格式**（每个句位，提炼 2-3 个措辞变体）：
```yaml
phase_2_2b_sentence_variants:
  topic_sentence:
    position: "段首论点句"
    variants:
      - variant: "We argue that [IV] [direction] [DV] through [mechanism]."
        source_papers: ["Shen_etal_2022_JOM", "Singh_Grewal_2023_JMR"]
        why_effective: "active verb + concrete subject + 方向 + 机制预告，一句话给出本段核心判断"
        build_type_fit: "机制推演型"
        dedup_status: existing_match  # sentences/leitmotif-section-opener.md 已有类似；仅复现印证，Phase 4 追加 source_papers
      - variant: "[Construct A] differs from [Construct B] in that [dimension]."
        source_papers: ["Pollock_2015_ASQ"]
        why_effective: "直接给出辨析维度，不铺垫"
        build_type_fit: "构念辨析型"
        dedup_status: new_variant  # 现有 sentences 无此句式 → 新增候选
    anti_pattern: "It is argued that..." （无主语被动）/ "Smith (2020) showed..." （作者名开头，读者降级）
  why_chain_transition:
    position: "机制步骤间过渡"
    variants:
      - variant: "This, in turn, [next step] because [reason]."
        source_papers: ["Shen_etal_2022_JOM"]
        why_effective: "标记链式因果传递（前步输出=后步输入），比 'Furthermore' 精确"
        dedup_status: near_dup  # 与 mechanism_chain.md 现有 "Consequently" 相似但更精确；标注差异=链式 vs 单步
      - variant: "Consequently, [next step]."
        source_papers: ["Singh_Grewal_2023_JMR"]
        why_effective: "标准因果收敛"
        dedup_status: existing_match
    anti_pattern: 用 "This, in turn" 连接并列机制（伪装并列为链式）
  # hypothesis_sentence / wrap_sentence 同结构
```

**生成力验证（Phase 2.4 同样适用）**：每个句式变体填入该论文的具体内容后，应能生成功能等价的句子。若填入后与原文功能不等价（如丢失"方向性"），标记为"需修正"。

**与 Phase 2.5 连接词分析的分工**：
- Phase 2.5（connector_patterns）：统计连接词**密度与分布**（因果类多少、条件类多少），输出 DNA 指标
- Phase 2.2b（本节）：提炼连接词的**具体句式变体**（"This, in turn" 这个写法好在哪里），输出可回写的措辞候选
- 两者互补：2.5 发现"条件连接词占比异常"→ 2.2b 提供该论文条件句的具体写法供回写

**回写门槛**（与 writeback_reminders 一致）：
- 单篇句式 → Vault 注释，不入 skill（标注 sentence_position + 待审阅）
- ≥2 篇复现同句位同写法 → 可选变体（句式级），回写 `corpus/sentences/[对应文件]`
- ≥3 篇跨期刊 → 升 VERIFIED，可在 write-theory 措辞润色阶段作默认推荐

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
        abstraction_level: "L0 / L1 / L2 / L3"
        incommensurability_route_fit: "R1 / R2 / R3 / R4 / cross-route / n.a."
        architecture_necessity: "[为何该假设形式不可由更简单形式替代]"
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

4. **架构必要性检查（Architecture-Necessity Test；Incommensurability 必做）**
   - route 是否真的要求 paired hypotheses、mediator、moderator、competing hypotheses 或曲线？
   - 一个更简单的 differential/conditional hypothesis 能否表达相同 contribution？
   - 若复杂度只来自来源论文的估计模型 → 降为 L3，不进入架构语料。

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
  architecture_necessity_test:
    complex_form_required: true/false/n.a.
    simpler_alternative: "[更简单形式或 null]"
    verdict_effect: "[保留 L2 / 降为 L3 / n.a.]"
```

**裁决标准**：

| 裁决 | 条件 | 后续动作 |
|------|------|----------|
| **通过** | 通用三项测试通过；Incommensurability 还须通过架构必要性检查 | 骨架进入 Phase 3 和 Phase 4 |
| **需修正** | 生成力或机制内容测试未通过，但可通过改写修复 | 标记后在 Phase 4 中尝试改写后重新验证 |
| **不纳入** | 构建类型错配，或过度抽象失去生成力 | 丢弃，不进入语料库 |

**注意**：裁决记录存入 Vault 的 `vault_enrichment`，供 Phase 4 跨论文聚合使用。

> **连接词使用模式提炼（2.5）**已外置：见 `../protocols/connector_patterns.md`。Phase 2 骨架提炼完成后执行连接词分析时加载。
