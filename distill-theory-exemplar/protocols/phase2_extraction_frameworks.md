# Phase 2 提取框架（2.1.5–2.1.8）

> 外置自 `distill-theory-exemplar/SKILL.md`。何时加载：执行 Phase 2 深度提炼时加载。

---

### 2.1.5 论证节奏提炼（Argument Rhythm Distillation）

Theory 写作的核心单元不是模块，而是**段落内部的论证节奏**。借鉴 Results 的"四拍节奏"蒸馏逻辑（方向→显著性→幅度→支持判断），Theory 同样存在可量化的段落级论证节奏，但节奏形态因模块功能和构建类型而异。

#### 核心节奏：T3/T4 Hypothesis Development 段落交织式论证链（与 write-theory v3.3.0 对齐）

write-theory v3.3.0 将每个假设推导段落定义为**交织式论证链（Interwoven Logic Chain）**：
**Topic Sentence → Theoretical Reasoning + Literature Support（交织） → Hypothesis Transition**

文献引用与理论推理**交织**而非先后排列——这是管理学顶刊的默认写法。蒸馏中**最重要的节奏目标**是每个假设推导段落完成功能等价的论证：方向锚定、机制推演（文献锚定）、假设收敛。

```text
[拍1-方向]: Topic Sentence — 本段要证明什么
  → 功能：锚定段落论点，限定范围
  → 示例："Drawing on [theory], we argue that the effect of [X] on [Y] operates through [M]."
  → 失败信号：段首句只陈述事实不表达论点 / 只定义变量不预告要证明的关系

[拍2-机制+证据交织]: Reasoning & Literature Interwoven — 为什么 X 影响 Y
  → 功能：逐步展示因果链，每步由文献或理论依据锚定
  → 节奏模式：
     "Prior research has established that [X→state1] ([citation]). However, it remains 
     unclear how [state1] leads to [Y]. We argue that [state1] creates [state2] 
     because [theoretical justification]. Consequently, [state2] affects [Y] 
     through [final link]."
  → 失败信号：X→Y 直接跳跃无中间步骤 / 用 "obviously" 代替论证 / 只有 citation list 无机制 / 文献支撑与机制步骤脱节

[拍3-收敛]: Hypothesis Transition — 从机制到可检验预测
  → 功能：将机制推演固化为形式化假设
  → 标志词："Therefore, we hypothesize:" / "Thus:" / "Accordingly, we predict:"
  → 示例："Therefore, we hypothesize: Hypothesis 1: [X] is positively related to [M]."
  → 失败信号：Therefore 方向与机制推理方向矛盾 / 假设缺少方向或边界条件
```

**备选节奏：分离式（少数情况）**——当某一步的文献支持特别密集、需要单独展开时，可暂时将 [机制] 和 [文献] 分离。但整个段落的默认节奏是交织的。蒸馏时标记论文使用的是交织式还是分离式。

#### 交织式论证链各要素 QC 提取（与 write-theory v3.3.0 对齐）

对每个假设推导段落，提取以下 QC 指标：

| 要素 | 提取问题 | 失败信号 | 记录格式 |
|------|---------|---------|---------|
| **Topic Sentence 精准度** | 是否同时包含话题+核心观点+限定范围？是否使用 active verb + concrete subject？段首句是否在 15 词内说出核心判断？ | 段首句只陈述事实/只定义变量/无主语被动语态（"It is argued that"） | `{topic_sentence_quality: "高/中/低", word_count_to_core_claim: N, has_active_verb: true/false, has_concrete_subject: true/false}` |
| **Reasoning-Literature 交织度** | 文献引用是否嵌入在机制链步骤中？每个引用是否总结了 argument 并链接到 concrete finding？ | 独立的文献罗列段落；citation 与 mechanism 步骤脱节；citation 替代机制推演 | `{interwoven: true/false, citations_count: N, argument_summarized_count: N, concrete_finding_linked_count: N, citation_vs_mechanism_alignment: "高/中/低"}` |
| **Theoretical Reasoning 完整性** | 从 X 到 Y 的每一步因果推理是否明确写出？每步间是否有 explicit transition？ | 逻辑跳跃（省略关键步骤）；缺少 transition（从 A 直接跳到 C）；用 "obviously" 代替论证 | `{mechanism_steps_count: N, logical_jumps: ["从 X 到 M 缺少中间步骤"], transitions: ["Consequently", "Thus", "In turn"]}` |
| **Hypothesis Transition 收敛质量** | 收束句是否总结了推理链而非简单重复 "we hypothesize"？ | 无理论收束直接 "we hypothesize"；Therefore 方向与机制矛盾 | `{has_theoretical_closure: true/false, transition_phrase: "Therefore/Thus/Accordingly", hypothesis_direction_matches_mechanism: true/false}` |
| **Concrete Illustration（可选）** | 每个因果步骤后是否有 1 句 concrete illustration？ | 连续 2 个推理步骤无 illustration | `{illustration_count: N, illustration_types: ["案例", "场景", "比喻"], showing_gaps: ["步骤2无 illustration"]}` |
| **识别策略嵌入**（制度冲击类） | Theory 中是否嵌入了对识别假设的理论论证？ | Methods 描述了识别策略但 Theory 完全未提及 | `{identification_strategy_in_theory: true/false, iv_exclusion_restriction: "...", did_parallel_trends: "...", location: "P[段号]"}` |
| **节奏变体标记** | 论文使用的是交织式还是分离式？是否功能等价？ | 分离式但文献与机制无明确链接 | `{rhythm_variant: "interwoven / separated / hybrid", functional_equivalent: true/false}` |

**逻辑跳跃诊断**：逐句标记因果连接词（Consequently/Thus/Thereby/As a result/This leads to...）。缺少中间步骤 → 记录具体跳跃位置。

**Topic Sentence 反模式示例提取**：
- ❌ 被动语态例句："It is argued that CEO overconfidence affects firm risk." → 记录并标记为违反 Conversational Voice
- ✅ 主动语态例句："We argue that CEO overconfidence increases firm risk-taking because overconfident leaders systematically underestimate downside uncertainty." → 记录为优质模板

#### 段落论证节奏的构建类型变体

交织式节奏的形态因构建类型而异：

| 构建类型 | 机制+证据交织形态 | 收敛形态 | 节奏特征 |
|----------|-------------------|----------|---------|
| **机制推演型** | 多步因果链，每步嵌入 citation | "Therefore, H1: X→M; H2: M→Y" | 一个机制链收敛为一个或多个假设 |
| **构念辨析型** | 差异化维度对比，每个差异维度嵌入 citation | "Thus, A and B are distinct constructs that..." | 交织形态为对比+证据，收敛可能为命题而非假设 |
| **假设树型** | 主效应机制 → 条件化分叉，分叉处嵌入 citation | "Therefore, H1: X→Y; H2: X→Y moderated by W" | 基线机制与调节逻辑交织 |
| **质性过程理论型** | 阶段序列 (Phase 1→2→3) + 过渡条件，每阶段嵌入 citation | "Proposition 1: In Phase 1, [process] occurs" | 按时间/阶段展开 |
| **调节效应型** | X→Y 主机制 + W 如何改变该机制，嵌入调节方向 citation | "H1: X→Y positive; H2: X×W→Y [direction]" | 主效应与交互逻辑交织 |

#### 节奏变体记录

蒸馏时必须区分：
- **INTERWOVEN（默认）**：文献引用嵌入 why-chain 的每一步
- **SEPARATED（少数）**：机制段落先完整推演，再用单独段落密集支撑文献
- **HYBRID（混合）**：局部交织+局部分离

记录格式：
```yaml
rhythm_pattern:
  primary: "interwoven / separated / hybrid"
  evidence: "[具体段落位置与句式]"
  functional_equivalent: true/false  # 是否完成功能等价的论证
```

#### 其他模块的论证节奏

T1（Construct Definition）和 T2（Theoretical Lens）有各自的节奏模式：

**T1 构念定义节奏（三拍）**：
```text
[拍1-命名]: 构念名称 + 所属理论家族
  → "We define [construct] as [definition], drawing on [theoretical tradition]."

[拍2-维度]: 构念的构成维度或关键属性
  → "[Construct] comprises [N] dimensions: [dim1], [dim2], and [dim3]."

[拍3-范围]: Scope condition 或边界
  → "This conceptualization applies to [scope]; it does not capture [excluded aspect]."
```
（注：构念辨析型的 T1 变体为四拍：命名→A定义→B定义→区分维度→理论后果）

**T2 理论视角节奏（三拍）**：
```text
[拍1-来源]: 理论来源 + 核心洞察
  → "Drawing on [theory] ([citation]), we adopt the insight that [core premise]."

[拍2-适用性]: 该理论为什么适合解释本文的研究问题
  → "This lens is particularly appropriate because [fit with RQ / gap]."

[拍3-框架映射]: 该理论如何映射到本文的构念体系
  → "[Theory] suggests that [mapping to constructs], providing the foundation for our theoretical model."
```

#### 蒸馏任务：节奏完整性量化

对每个段落，评估其论证节奏的完整性：

| 模块 | 预期节奏单元 | 评分方式 | 纳入 Phase 3 DNA |
|------|-------------|---------|-----------------|
| T1 Construct Definition | 3-4 拍 | 每拍 0-1 分（存在且功能明确=1） | `t1_rhythm_completeness` |
| T2 Theoretical Lens | 3 拍 | 每拍 0-1 分 | `t2_rhythm_completeness` |
| T3/T4 Hypothesis Development | 交织式 3 单元（方向→机制/证据交织→收敛）/假设段落 | 每单元 0-1 分，多段落取均值；同时标记 rhythm variant | `t3t4_rhythm_completeness` |
| T5 Boundary Condition | 3 拍（条件引入→理论依据→预测修正） | 每拍 0-1 分 | `t5_rhythm_completeness` |
| T6 / Closure 策略 | 局部收束（必须）+ 可选框架总结 | 局部收束：有/无；框架总结：嵌入/Discussion/缺失 | `closure_strategy_completeness` |

**节奏完整性评分输出**：

```yaml
phase_2_1_5_rhythm_distillation:
  T1_construct_definition:
    paragraph_id: "P2"
    rhythm_type: "三拍定义"
    beat_1_naming: {score: 1, max: 1, evidence: "We define..."}
    beat_2_dimensions: {score: 1, max: 1, evidence: "comprises three dimensions"}
    beat_3_scope: {score: 0, max: 1, evidence: "未出现 scope condition"}
    completeness: "2/3"
    rhythm_quality: "△ — 缺少范围限定拍"
  T3T4_hypotheses:
    H1_paragraph:
      paragraph_id: "P4"
      rhythm_type: "交织式机制推演"
      beat_1_direction: {score: 1, max: 1, evidence: "Topic sentence 明确预测 X→M 关系"}
      beat_2_mechanism_literature_interwoven: {score: 1, max: 1, evidence: "两步因果链完整，citation 嵌入每一步 (X→state→M)"}
      beat_3_convergence: {score: 1, max: 1, evidence: "Therefore, H1: X positively related to M"}
      completeness: "3/3"
      rhythm_quality: "✓ — 完整交织节奏"
    H2_paragraph:
      paragraph_id: "P5"
      rhythm_type: "交织式机制推演"
      beat_1_direction: {score: 0, max: 1, evidence: "段首句只定义 M，未预告要证明 M→Y"}
      beat_2_mechanism_literature_interwoven: {score: 1, max: 1, evidence: "M→Y 机制链完整，citation 嵌入机制"}
      beat_3_convergence: {score: 1, max: 1, evidence: "Therefore, H2: M positively related to Y"}
      completeness: "2/3"
      rhythm_quality: "△ — 缺少方向拍（段首未锚定论点）"
    overall_t3t4_rhythm: "83.3% (5/6)"
  rhythm_pattern_notes:
    - "H1/H2 使用连续推导节奏：H1 的收敛句引出 M，H2 的机制+证据交织从 M 继续推演"
    - "citation 在两步机制中均匀分布（每步 1-2 个 citation），非堆砌"
    - "T1 缺少 scope condition 拍，在构念辨析型中这是致命伤，在机制推演型中风险较低"
```

#### 节奏质量评级

| 评级 | 标准 | 蒸馏动作 |
|------|------|---------|
| **FULL_RHYTHM** | 段落所有拍完整且功能明确 | 标记为高可信度范文段落，优先纳入 Phase 4 骨架库 |
| **RHYTHM_GAP** | 缺失 1 拍 | 记录缺失的具体拍和功能后果，纳入模仿风险提示 |
| **RHYTHM_BROKEN** | 缺失 ≥2 拍或拍顺序混乱 | 标记为不可模仿的反模式，提取其"修复后"骨架（补全缺失拍） |
| **RHYTHM_VARIANT** | 拍数或拍序与标准不同但功能等价 | 记录为节奏变体，丰富 Phase 4 的节奏模式库 |

### 2.1.6 假设论证微观动作提取框架（Micro-Moves for Hypothesis Argumentation）

交织式节奏回答了段落的**形态**，但没有回答作者在段落中具体执行了哪些**说服动作**。本节提供一个**分析透镜**，帮你在阅读顶刊范文时识别：作者是用哪几个动作完成从起点到假设的推导的。这些标注结果最终可用于对比多篇论文、归纳该构建类型的典型论证路径，并沉淀为 `write-theory` 的写作模式。

#### 标准微观动作序列（用于分析范文）

```text
[Anchor]        → 论文固定的论证起点： prior finding / theoretical premise / accepted scope condition
     ↓
[Gap/Puzzle]    → 论文指出的现有解释缺口、边界或反直觉之处
     ↓
[Mechanism Move]→ 论文提出的新因果步骤或条件化逻辑
     ↓
[Warrant]       → 论文用理论或文献说明该机制步骤为何成立
     ↓
[Prediction]    → 论文收敛到可检验假设的方式
```

**每个动作的识别信号**（蒸馏时从原文提取）：

| 动作 | 典型句法 | 在范文中的功能 | 标注为缺失的风险 |
|------|---------|--------------|----------------|
| **Anchor** | "Prior research has established that..." / "A long-standing assumption in the literature is..." | 让读者接受论证起点 | 起点是作者自己的断言而非学界共识 |
| **Gap/Puzzle** | "However, it remains unclear whether..." / "What remains less understood is..." | 制造认知张力 | 无 gap，直接 "we argue" |
| **Mechanism Move** | "We argue that [X] leads to [state] because..." | 提出新的因果机制 | X→Y 直接跳跃，无中间状态 |
| **Warrant** | "This is consistent with [theory], which posits that..." / "[Author] (year) found that..." | 为机制步骤提供合法性 | Warrant 只是 citation list，未与机制步骤链接 |
| **Prediction** | "Therefore, we hypothesize:..." | 把机制固化为假设 | 假设方向与机制推理矛盾 |

#### 蒸馏任务：微观动作标注

对每个假设推导段落，标注：

```yaml
phase_2_1_6_micro_moves:
  H1_paragraph:
    paragraph_id: "P4"
    moves_detected:
      - move: "Anchor"
        evidence: "Prior research has established that X increases state A (Smith, 2010)."
        source: "empirical_finding"
      - move: "Gap"
        evidence: "Yet how state A translates into Y remains unclear."
      - move: "Mechanism Move + Warrant"
        evidence: "We argue that state A creates state B because [theory] posits... (Jones, 2012)."
      - move: "Prediction"
        evidence: "Therefore, we hypothesize: H1: X is positively related to Y."
    missing_moves: []
    move_quality: "完整序列"
```

#### 双边论证提取（Bilateral Argumentation）

`write-theory` Constraint 20 规定：调节/边界条件段落应同时论证 "when M=high → effect" 和 "when M=low → effect"。蒸馏时记录范文是否遵守该规则，以及它是如何用具体句法完成双边论证的——这些句法可沉淀为 `write-theory` 的调节论证模板。

蒸馏时必须提取：

```yaml
bilateral_argumentation:
  moderator: "W"
  high_condition:
    present: true/false
    mechanism: "When W is high, X→Y is strengthened because..."
    evidence: "[citation supporting high-condition mechanism]"
  low_condition:
    present: true/false
    mechanism: "When W is low, X→Y is weakened because..."
    evidence: "[citation supporting low-condition mechanism]"
  symmetry: "完整 / 仅单边 / 缺失"
  note_for_corpus: "如完整，提取其 high/low 论证句法作为 write-theory 模板候选"
```

#### 替代解释排除（Ruling Out Alternatives）

提取范文如何处理 competing explanations——这是判断一篇 Theory 是否"self-aware"、是否提前回应审稿人质疑的关键。记录其排除策略和典型句法，可作为 `write-theory` 中竞争假设/反直觉预测型论文的写作参照。

| 排除策略 | 典型表达 | 蒸馏标记 |
|---------|---------|---------|
| **理论不一致** | "This alternative account would predict the opposite effect..." | `theoretical_inconsistency` |
| **范围条件** | "Such an explanation applies to [context], but our setting involves..." | `scope_condition` |
| **经验证据反例** | "Recent evidence, however, shows that..." | `empirical_counter` |
| **机制不可通约** | "While plausible, this mechanism does not explain why..." | `mechanism_incommensurable` |

记录格式：
```yaml
alternative_explanations:
  competing_accounts: ["account1", "account2"]
  ruling_out_strategy: ["theoretical_inconsistency", "scope_condition"]
  location: "P[段号]"
  completeness: "完整 / 部分 / 缺失"
```

### 2.1.7 论点-论据安排模式提取（Argument-Evidence Arrangement Patterns）

节奏和微观动作回答"段落内部发生什么"，安排模式回答"范文的论点和论据被组织成什么样的完整论证"。本节提供一套**分类框架**，帮你在对比多篇论文时识别：同一构建类型是否偏好某种安排方式？不同期刊/主题是否存在安排差异？这些模式可沉淀为 `write-theory` 的段落组织建议。

#### 五种标准安排模式（分类用）

| 模式 | 结构 | 适用场景 | 构建类型倾向 |
|------|------|---------|-------------|
| **Warrant-Embedded** | Claim → Reasoning + Evidence 交织 → Hypothesis | 默认；大多数机制推演型 | 机制推演型、假设树型 |
| **Warrant-First** | Claim → 密集理论依据 → 机制推演 → Hypothesis | 理论依据特别密集，需要单独展开 | 构念辨析型、理论密集型 |
| **Evidence-Contrast** | 反方证据 → 转折 → 自己的机制 → Hypothesis | 论文要挑战既有观点 | 反直觉预测型、辩证对立型 |
| **Cumulative** | H1 收敛 → H2 从 H1 的收敛点继续推演 | 假设间有逻辑依赖 | 中介链、两步机制 |
| **Parallel** | 共享同一理论框架的多个假设分别推导 | 假设间相互独立但同属一个理论 | 构念辨析型、多主效应 |

#### 蒸馏任务：安排模式识别

```yaml
phase_2_1_7_arrangement_pattern:
  primary_pattern: "Warrant-Embedded"
  secondary_pattern: "Cumulative"
  evidence: "H1 段末收敛到 M；H2 段首直接 'Building on this mechanism, we next argue M→Y'"
  paragraph_flow:
    - paragraph_id: "P4"
      function: "Anchor + Mechanism Move"
      arrangement: "Warrant-Embedded"
    - paragraph_id: "P5"
      function: "Cumulative extension from P4"
      arrangement: "Cumulative"
```

#### Concrete Illustration 提取

`write-theory` Phase 3（段落级 QC 检查表）把"不允许连续 2 个推理步骤无 illustration"作为写作规则。本节用于**提取范文如何执行这一规则**：它在哪些步骤放 illustration？用的是什么类型？哪些步骤省略了？这些提取结果可作为 `write-theory` Prose Craft 子协议的素材。

```yaml
concrete_illustration_pattern:
  illustration_density: "每个推理步骤后 1 句 / 每 2 步 1 句 / 稀疏"
  illustration_types:
    - type: "公司案例"
      example: "When Apple faced [situation], [mechanism] produced [outcome]."
    - type: "数字场景"
      example: "A 1-standard-deviation increase in X corresponds to..."
    - type: "比喻"
      example: "This is akin to..."
  missing_illustration_steps: ["步骤2", "步骤3"]
  note_for_corpus: "如某类 illustration 在同类论文中高频出现，可沉淀为 write-theory 推荐"
```

#### 复杂假设的段落安排

对假设树型、中介+调节混合、多调节型论文，提取其**段落级组织逻辑**。重点不是判断对错，而是记录：范文如何把多个假设编织进一个连贯叙事？假设之间靠什么连接词/逻辑关系衔接？这些信息可直接用于优化 `write-theory` 的复杂假设路由。

```yaml
complex_hypothesis_organization:
  pattern: "common_trunk → dual_branch"  # 或 baseline_first → moderation_second / mediation_chain
  common_trunk_paragraphs: ["P4"]
  branch_paragraphs:
    - branch_id: "H1"
      paragraph: "P5"
      relationship_to_trunk: "direct effect from common mechanism"
    - branch_id: "H2"
      paragraph: "P6"
      relationship_to_trunk: "moderation of trunk mechanism"
  relationship_between_hypotheses: "sequential / parallel / nested"
  clarity_risk: "如分支间关系不自明，需框架总结"
```

### 2.1.8 证据类型与功能编码（Evidence Typology & Function Coding）

`distill-theory-exemplar` 已经检查 citation 是否总结 argument 并链接 concrete finding，但还没有系统分析**范文把什么当证据、证据执行什么功能、如何与论点交织**。本节提供一个编码框架，帮你在阅读时识别：顶刊作者是用 empirical finding 支撑机制？用 theoretical argument 做 warrant？还是用 negative evidence 排除替代解释？编码结果可沉淀为 `write-theory` 的证据使用指南。

#### 证据类型学（用于编码范文中的证据）

| 证据类型 | 定义 | 典型来源 | 在 Theory 中的摆放位置 |
|---------|------|---------|---------------------|
| **Empirical Finding Evidence** | 前人研究的 concrete result | 实证论文 | 支撑机制步骤的 why chain |
| **Theoretical Argument Evidence** | 理论家的核心主张或理论逻辑 | 理论论文 | 为 mechanism move 提供合法性 |
| **Boundary Condition Evidence** | 说明某机制只在某范围内成立 | 边界条件研究 | 引出或支撑 T5 |
| **Negative Evidence** | 前人未发现或机制不成立的证据 | 零结果、反例研究 | 排除替代解释、强化 gap |
| **Analogical Evidence** | 比喻、类比、案例 | 案例研究、行业报告 | 在抽象机制后提供 concrete illustration |

#### 证据功能标注

每个 citation 必须标注其功能：

| 功能 | 作用 | 典型连接词 |
|------|------|----------|
| `support` | 直接支持当前机制步骤 | "Consistent with this logic..." |
| `qualify` | 限定机制的适用范围 | "However, this effect is limited to..." |
| `contrast` | 与当前机制形成对比，引出转折 | "In contrast, ..." / "Whereas ..." |
| `pave` | 为后续推理铺路 | "This raises the question of whether..." |
| `rebut` | 排除替代解释 | "This alternative account cannot explain..." |

#### 文献引用三要素模板

`write-theory` 要求每个引用总结 argument 并链接 concrete finding。提炼可复用的三要素句式：

```text
[Author] (year) found that [concrete finding] — [argument summary].
This suggests that [mechanism step], because [theoretical reason].
```

蒸馏时提取每个 citation 是否满足三要素：

```yaml
evidence_three_element_check:
  citation: "Smith (2010)"
  concrete_finding: "firms delaying recalls experienced 23% greater stock-price declines"
  argument_summary: "market punishes uncertainty more than bad news"
  link_to_current_mechanism: "consistent with our argument that X increases perceived uncertainty"
  three_elements_complete: true/false
```

#### 蒸馏任务：证据地图

为每个假设推导段落生成证据地图：

```yaml
phase_2_1_8_evidence_map:
  H1_paragraph:
    paragraph_id: "P4"
    evidence_items:
      - citation: "Smith (2010)"
        type: "empirical_finding"
        function: "support"
        mechanism_step: "X → state A"
        three_elements_complete: true
      - citation: "Jones (2012)"
        type: "theoretical_argument"
        function: "pave"
        mechanism_step: "state A → state B"
        three_elements_complete: true
    evidence_type_distribution: {"empirical_finding": 2, "theoretical_argument": 1}
    evidence_function_distribution: {"support": 2, "pave": 1}
    evidence_placement: "embedded_in_mechanism"  # 或 "separate_literature_block" / "front_loaded"
```
