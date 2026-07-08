# Hypothesis Derivation Patterns

**核心定位**：假设推导段落（Hypothesis Derivation）是 Theory 部分的心脏。本文件集中管理“从理论到假设”的段落级推理模板：如何建立 Anchor、构造 Mechanism Move、安放 Warrant、收敛到 Prediction，以及段内逻辑推进的连接词布局。

> 使用原则：本文件不是收集“某种理论说什么”，而是收集“如何让一个假设从理论前提中自然生长出来”的论证组织方式。机制内容必须替换为用户自己的研究材料；骨架和连接策略可以直接复用。

---

<!--
pattern_id: anchor_then_mechanism_then_prediction
build_type: 跨类型
source_papers: ["Singh_Grewal_2023_JMR", "Shen_Zhou_Wang_Zhang_2022_JOM"]
confidence: high
-->

## Pattern: Anchor → Mechanism Move(s) → Warrant → Prediction

**适用场景**：绝大多数 Theory 假设推导段落的基础结构。适用于主效应、中介、调节等所有假设类型。

**微观动作序列**：
1. **Anchor**：锚定一个读者已接受的理论前提、构念定义或经验事实
2. **Mechanism Move**：提出新的因果步骤或状态转换（“We argue that...”）
3. **Warrant**：用文献、理论、案例或反事实推理支撑机制步骤
4. **Prediction**：收敛到正式假设

**骨架**：
```
[Anchor] [理论前提 / 构念定义 / 经验事实].
[Mechanism Move] We argue that [IV] influences [DV] by [mechanism step].
[Warrant 1] This is because [theoretical reason] ([citation]).
[Warrant 2] For example, [concrete illustration].
[Prediction] Therefore, we hypothesize: H[X]: [正式假设].
```

**范文来源**：
- Singh and Grewal (2023), *Journal of Marketing Research*（H1：效率视角 Anchor → 合法性视角反转 → 机制）
- Shen, Zhou, Wang, and Zhang (2022), *Journal of Operations Management*（H1：构念定义 Anchor → 三机制并行）

**为什么有效**：四动作序列符合读者的认知推进：先确认共同起点，再引入新因果主张，接着给出信任依据，最后导出可检验预测。

**注意事项**：
- Anchor 必须与后续 Mechanism Move 存在逻辑承接，不能悬空
- Warrant 的数量和类型要与 Mechanism Move 的争议程度匹配：越反直觉，Warrant 越密集
- Prediction 必须能从 Mechanism Move 直接推出，避免“因此”跳跃

**反模式**：如果 Mechanism Move 只是重复 Anchor 的内容（例如 Anchor 说 X 影响 Y，Mechanism Move 又说 X 影响 Y），则推导塌陷为同义反复。

---

<!--
pattern_id: theory_driven_anchor_with_puzzle_turn
build_type: 机制推演型 / 假设树型 / 竞争假设型
source_papers: ["Singh_Grewal_2023_JMR"]
confidence: medium
status: needs_validation
-->

## Pattern: Theory-Driven Anchor + Puzzle Turn

**适用场景**：当文献中存在一个被默认接受的强理论直觉，而你的研究要挑战或反转它时使用。

**微观动作序列**：
1. **Anchor（理论前提）**：陈述主流理论的预测
2. **Gap/Puzzle（反直觉转折）**：指出另一种理论视角给出不同预测
3. **Mechanism Move**：解释为什么第二种预测成立
4. **Warrant**：用文献或案例支撑
5. **Prediction**：导出假设

**骨架**：
```
[Anchor] From an [established theory] perspective, [IV] should not influence [DV] because [IV] does not alter [mechanism that determines DV].
[Puzzle] However, a [alternative theory]-based perspective and the associated [model/literature] suggest that [IV] [direction] [DV].
[Mechanism Move] We argue that [IV] influences [DV] through [mechanism].
[Warrant] This is consistent with [theory], which posits that [theoretical argument] ([citation]).
[Prediction] Therefore, we hypothesize: H1: [IV] is [direction] related to [DV].
```

**范文来源**：Singh and Grewal (2023), *Journal of Marketing Research*

**为什么有效**：用一个读者接受的理论作为“稻草人”，然后反转，制造更强的认知张力，让新假设显得不仅新颖而且必要。

**注意事项**：
- 必须准确陈述主流理论的预测，不能 caricature
- 反转必须有独立的理论框架支撑，不能只靠 “however”
- 如果主流理论在文献中并不占主导，此 Anchor 会显得牵强

**反模式**：如果效率视角本身在文献中不占主导，不要用此 Anchor。

---

<!--
pattern_id: multi_mechanism_trunk
build_type: 机制推演型 + 调节效应型
source_papers: ["Shen_Zhou_Wang_Zhang_2022_JOM"]
confidence: high
-->

## Pattern: Multi-Mechanism Trunk

**适用场景**：主效应有多个并行的机制路径，后续调节假设需要分别回到这些机制上展开。

**微观动作序列**：
1. **Anchor**：预告“有三个原因”
2. **Mechanism Move 1/2/3**：每个机制独立展开
3. **Concrete Illustration（可选）**：为每个机制配案例
4. **Warrant**：收束机制群
5. **Prediction**：导出 H1

**骨架**：
```
[Anchor] We suggest that [IV] may [direction] [DV] for three reasons.

[Mechanism Move 1] First, [IV] may induce [state 1], which [effect on DV].
[Illustration 1] For example, [company/context]...

[Mechanism Move 2] Second, [IV] may lead to [state 2], preventing firms from [action].
[Illustration 2] For instance, [company/context]...

[Mechanism Move 3] Third, [IV] may cause [state 3], decreasing firms' ability to [action].
[Illustration 3] [company/context]...

[Warrant] Taken together, these mechanisms suggest that [IV] undermines [DV].
[Prediction] Therefore, we hypothesize: H1: [IV] is [direction] related to [DV].
```

**范文来源**：Shen, Zhou, Wang, and Zhang (2022), *Journal of Operations Management*

**为什么有效**：多个机制并行展开，展示理论深度；后续 moderator 可以分别回到这三个机制上，形成 Parallel 结构。

**注意事项**：
- 三个机制必须概念独立，不能是同一机制的不同标签
- 每个 illustration 必须对应其机制步骤，不能通用
- 后续调节假设段落必须明确引用 trunk 中的具体机制

**反模式**：如果只有一个机制，不要硬拆成三个；如果 moderator 段落不回到 trunk 的具体机制，parallel 结构名存实亡。

---

<!--
pattern_id: bilateral_moderation_derivation
build_type: 调节效应型 / 假设树型
source_papers: ["Shen_Zhou_Wang_Zhang_2022_JOM"]
confidence: high
-->

## Pattern: Bilateral Moderation Derivation（high/low 双边论证）

**适用场景**：调节效应型论文中，需要同时论证 moderator 高值和低值条件下的机制变化。

**微观动作序列**：
1. **Anchor**：引入 moderator 作为 boundary condition
2. **High-condition Mechanism Move**：论证高 moderator 下机制如何变化
3. **Low-condition Mechanism Move**：论证低 moderator 下机制如何变化（可用 “By contrast” / “When... is low”）
4. **Warrant**：用文献或制度逻辑支撑两边
5. **Prediction**：导出调节假设

**骨架**：
```
[Anchor] The above relationship, however, is contingent on [W].

[High condition] When [W] is high, [mechanism 1] is weakened because ...; [mechanism 2] is reduced because ...; and [mechanism 3] is overcome because ....
[Low condition] By contrast, when [W] is low, [mechanism 1] remains strong because ...; [mechanism 2] persists because ...; and [mechanism 3] dominates because ....

[Warrant] Thus, [theory/literature] suggests that [W] buffers/attenuates the negative effect of [IV] on [DV].
[Prediction] Therefore, we hypothesize: H[X]: The negative relationship between [IV] and [DV] is weaker when [W] is high rather than low.
```

**范文来源**：Shen, Zhou, Wang, and Zhang (2022), *Journal of Operations Management*（H2–H5）

**为什么有效**：双边论证让读者看到调节变量在两种极端状态下的完整因果图景，避免只论证一边导致的 selection bias 感。

**注意事项**：
- 不能只论证高条件然后默认低条件是反过来的
- 两边的机制变化必须对称地回到 trunk 机制
- 连接词要清晰：high 用 “When... is high” / “Under high...”; low 用 “By contrast” / “Conversely” / “When... is low”

**反模式**：如果 moderator 是分类变量或只有一侧有理论意义，不要硬凑双边论证。

---

<!--
pattern_id: indirect_moderation_derivation
build_type: 假设树型 / 机制推演型
source_papers: ["Singh_Grewal_2023_JMR"]
confidence: low
status: needs_validation
-->

## Pattern: Indirect Moderation / Mediated Moderation Derivation

**适用场景**：当理论预期一个 moderator 的调节作用本身被另一个变量中介时使用（mediated moderation）。

**微观动作序列**：
1. **Anchor**：两个独立调节假设已经建立
2. **Mechanism Move**：解释第二个 moderator 如何传播第一个 moderator 的信息/效果
3. **Warrant**：理论文献 + 方法学模型引用
4. **Prediction**：导出间接调节假设

**骨架**：
```
[Anchor] As discussed, [W1] moderates the [IV]→[DV] relationship, and [W2] also moderates this relationship.
[Mechanism Move] We argue that [W2] mediates the moderating effect of [W1] on the [IV]→[DV] link because [W2] disseminates [information] about [W1], thereby shaping [actor]'s response.
[Warrant] This is consistent with [theory], which suggests that [argument] ([citation]). Model B in [methodology paper] captures this indirect moderation structure.
[Prediction] Therefore, we hypothesize: H[X]: The interaction of [W2] and [IV] mediates the moderating effect of [W1] on the relationship between [IV] and [DV].
```

**范文来源**：Singh and Grewal (2023), *Journal of Marketing Research*

**为什么有效**：把复杂的统计模型（mediated moderation）转化为可理解的理论叙事。

**注意事项**：
- 必须独立论证为什么 W2 会中介 W1 的调节作用，不能只引用方法论文献
- 建议在 H4 前用图示（Model A vs Model B）辅助
- Warrant 中理论文献应占主导，方法论文献只起辅助说明作用

**反模式**：如果 W2 只是另一个调节变量，不要硬说成间接调节。

---

<!--
pattern_id: cumulative_moderation_build_up
build_type: 假设树型 / 机制推演型
source_papers: ["Singh_Grewal_2023_JMR"]
confidence: medium
status: needs_validation
-->

## Pattern: Cumulative Moderation Build-Up

**适用场景**：后续调节假设建立在前面调节假设的基础上，形成累积式论证结构。

**微观动作序列**：
1. **Anchor**：回顾前面已建立的调节关系
2. **Mechanism Move**：说明两个调节变量如何交互或如何共同塑造信息环境
3. **Warrant**：信息传播理论 / 注意力理论
4. **Prediction**：导出更复杂的调节假设

**骨架**：
```
[Anchor] As established, [W1] shapes how [IV] influences [DV] by altering [mechanism]. [W2] further alters this relationship by [second mechanism].
[Mechanism Move] We argue that these two moderating effects are not independent; rather, [W2] transmits or amplifies the information conveyed by [W1].
[Warrant] This is because [theory] posits that [argument] ([citation]).
[Prediction] Therefore, we hypothesize: H[X]: [complex moderation hypothesis].
```

**范文来源**：Singh and Grewal (2023), *Journal of Marketing Research*

**为什么有效**：通过累积而非平行组织，展示理论层次的递进；适合 JMR 等偏好复杂理论模型的期刊。

**注意事项**：
- 每个前置假设必须足够稳固，否则累积会塌陷
- 必须清晰说明两个 moderator 的交互或层级关系，不能简单并列

**反模式**：如果两个 moderator 之间没有理论交互，不要硬用 cumulative 结构。

---

## 段内逻辑布局原则

### 1. 连接词的功能分类

| 功能 | 常用连接词 | 使用位置 |
|------|-----------|---------|
| 引入机制 | “We argue that...”, “Specifically,...”, “The mechanism underlying this relationship is...” | Mechanism Move 开头 |
| 递进机制 | “First... Second... Third...”, “Moreover,...”, “In addition,...” | 多机制 trunk 内部 |
| 转折/反直觉 | “However,...”, “Yet,...”, “Contrary to this intuition,...” | Anchor → Puzzle 之间 |
| 条件化 | “When... is high...”, “Under conditions of...”, “Conversely,...” | 双边论证中 |
| 收束假设 | “Therefore, we hypothesize:”, “Taken together, these arguments suggest:” | Prediction 前 |

### 2. 段落长度与动作密度

- 一个标准假设推导段落建议包含 **1 个 Anchor + 1–3 个 Mechanism Move + 2–4 个 Warrant + 1 个 Prediction**
- 调节假设段落建议额外包含 **High/Low 两个条件分支**
- 间接调节/复杂调节段落建议拆分为 **2 个段落**：第一段建立两个独立调节，第二段论证交互/中介

### 3. Warrant 的三种摆放策略

| 策略 | 适用场景 | 范文 |
|------|---------|------|
| Warrant-Embedded（嵌入机制后） | 每个机制步骤后紧跟文献/案例 | Shen et al. (JOM) H1 |
| Warrant-Clustered（机制后集中） | 多个机制共享同一理论背景 | Singh & Grewal (JMR) H1 |
| Warrant-Contrasted（正反并举） | 竞争解释或对立机制 | 竞争假设型论文 |

---

## 与相邻语料文件的关系

- [`argumentation_patterns.md`](argumentation_patterns.md)：聚焦微观动作组合（Anchor/Gap/Mechanism/Warrant/Prediction）
- [`arrangement_patterns.md`](arrangement_patterns.md)：聚焦论点-论据的空间安排（Parallel / Cumulative / Evidence-Contrast）
- [`evidence_patterns.md`](evidence_patterns.md)：聚焦证据类型、功能和文献引用三要素
- [`bilateral_argumentation_templates.md`](bilateral_argumentation_templates.md)：聚焦调节假设的 high/low 句法
- [`hypothesis_organization_patterns.md`](hypothesis_organization_patterns.md)：聚焦多个假设之间的体系级组织（common trunk / dual branch）

> **使用顺序**：先查本文件确定假设推导段落的整体动作序列 → 再查 arrangement_patterns 确定段落内部布局 → 再查 evidence_patterns 填充 Warrant → 最后查 hypothesis_forms 输出正式假设。

---

<!--
pattern_id: width_type_parallel_mechanism
build_type: 机制推演型 / 调节效应型
source_papers: ["Gamache_McNamara_Mannor_Johnson_2020_SMJ", "Cui_Yang_Vertinsky_SMJ"]
confidence: high
status: ready_for_corpus
-->

## Pattern: Width-Type Parallel Mechanism

**适用场景**: 当 X→Y 的关系不是通过单一中介链，而是通过多个（2–3 个）独立的理论理由共同支撑时使用；可支撑线性主效应、曲线关系的某一阶段，或调节假设的某一边。
**微观动作序列**: Anchor（理论前提）→ Mechanism Move 1 + Warrant 1 → Mechanism Move 2 + Warrant 2 → [Mechanism Move 3 + Warrant 3] → Prediction
**范文来源**:
- Gamache, McNamara, Mannor, and Johnson (2020), *Strategic Management Journal*（3 个理由支撑线性主效应）
- Cui, Yang, and Vertinsky, *Strategic Management Journal*（2 个理由支撑曲线关系的递增段/递减段，以及调节假设的每一边）

**骨架（通用）**:
```
[Anchor] Drawing on [theory], we argue that [IV] [direction] [DV].
[Reason 1] First, [theoretical reason 1]. [Warrant 1]
[Reason 2] Additionally/Second, [theoretical reason 2]. [Warrant 2]
[Reason 3 — optional] Finally, [theoretical reason 3]. [Warrant 3]
[Prediction] Therefore, we hypothesize: H[X]: [正式假设].
```

**子变体 A：三理由线性主效应（Gamache 型）**

三个理由并行支撑同一方向的线性主效应。

**子变体 B：双理由曲线阶段（Cui et al. 型）**

两个理由并行支撑曲线关系的某一个阶段（递增段或递减段）。完整曲线需要两个这样的阶段组合。

**子变体 C：双理由调节一边（Cui et al. 型）**

在调节假设段落中，用两个理由论证 moderator 在 curve 低-中段的作用，再用两个理由论证其在高段的作用。

**为什么有效**: 多个独立理由并行支撑，展示理论论证的宽度和稳健性；每个理由都简短，避免深度链的复杂；读者容易跟随"First... Second..."的节奏。
**注意事项**: 
- 2–3 个理由必须概念独立，不能是同一理由的重复
- 每个理由后必须有 citation 支撑
- 适合单步机制关系或曲线关系的某一阶段，不适合需要解释完整"如何"发生的过程
- 用于调节假设时，必须对称地论证曲线的两边
**反模式**: 如果理由之间高度相关，会显得冗赘；如果研究问题需要解释过程机制，不要用宽度型代替深度链。不要为了让理由凑成 3 个而拆分本可合并的机制。

---

<!--
pattern_id: symmetric_opposing_dual_track
build_type: 机制推演型
source_papers: ["Zhao-Ding_Gaba_ORSC"]
confidence: medium
status: needs_validation
-->

## Pattern: Symmetric Opposing Dual-Track Mechanism

**适用场景**: 当同一理论框架下两个条件（或 IV 的两个维度）对同一组结果产生镜像反向效应时使用。
**微观动作序列**: Anchor（条件 1）→ Mechanism Move A1 + Mechanism Move A2（反向对）→ Prediction H1a/H1b → Anchor（条件 2）→ Mechanism Move B1 + Mechanism Move B2（镜像反向对）→ Prediction H2a/H2b
**范文来源**: Zhao-Ding and Gaba, *Organization Science*

**骨架**:
```
[Track 1: Condition A]
[Anchor] When [condition A] is high, [actor] faces [theoretical state].
[Mechanism Move A1] We argue that under [condition A], [IV] increases [DV_dimension_1] because [theoretical reason].
[Mechanism Move A2] Conversely, under [condition A], [IV] decreases [DV_dimension_2] because [theoretical reason].
[Prediction] Therefore, we hypothesize: H1a: ...; H1b: ...

[Track 2: Condition B — Mirror Reversal]
[Anchor] When [condition B] is high, [actor] faces [opposite theoretical state].
[Mechanism Move B1] We argue that under [condition B], [IV] decreases [DV_dimension_1] because [theoretical reason].
[Mechanism Move B2] Conversely, under [condition B], [IV] increases [DV_dimension_2] because [theoretical reason].
[Prediction] Therefore, we hypothesize: H2a: ...; H2b: ...
```

**为什么有效**: 两条机制链结构完全平行但方向相反，读者在理解第一条后，第二条只需"镜像反转"，大幅降低认知负荷；同时展示理论的系统性。
**注意事项**: 
- 两条 track 的机制必须在结构上真正对称，不能只名字对称
- 反向效应必须有独立理论依据，不能为了对称而硬凑
- 适合 DV 是两个互补维度（如 focus vs breadth, core vs overlap）的情境
**反模式**: 如果两个条件不是理论上的镜像，或 DV 两个维度不是互补关系，不要强行对称。

---

<!--
pattern_id: curvilinear_relationship_two_phase_argumentation
build_type: 机制推演型 / 调节效应型
source_papers: ["Cui_Yang_Vertinsky_SMJ"]
confidence: medium
status: needs_validation
-->

## Pattern: Curvilinear Relationship — Two-Phase Argumentation

**适用场景**: 当理论预期 IV 和 DV 之间存在曲线关系（如 inverted U-shape / U-shape）时，需要分别论证曲线两个阶段的机制。
**微观动作序列**: Anchor（曲线预测）→ Phase 1 递增/递减段（2 个理由）→ Transition（转折点机制）→ Phase 2 递减/递增段（2 个理由）→ Prediction
**范文来源**: Cui, Yang, and Vertinsky, *Strategic Management Journal*

**骨架**:
```
[Anchor] We expect [IV] to have a [curve direction] relationship with [DV].

[Phase 1: Increasing/decreasing segment]
When [IV] is [low/high], [DV] [increases/decreases] as [IV] increases, for two reasons.
[Reason 1] First, [theoretical mechanism 1]. [Warrant]
[Reason 2] Second, [theoretical mechanism 2]. [Warrant]

[Transition] However, as [IV] continues to increase, [theoretical turning point condition] occurs.

[Phase 2: Decreasing/increasing segment]
When [IV] is [high/low], [DV] [decreases/increases] as [IV] increases, for two reasons.
[Reason 1] First, [theoretical mechanism 1]. [Warrant]
[Reason 2] Second, [theoretical mechanism 2]. [Warrant]

[Prediction] Therefore, we hypothesize: H1: There is a [curve shape] relationship between [IV] and [DV].
```

**为什么有效**: 曲线关系需要分别解释为什么先增后减（或先减后增），每个阶段用独立理由支撑，避免"因此是曲线"的跳跃；同时展示理论对关系全区间的掌控。
**注意事项**:
- 必须明确转折点（turning point）的理论依据
- 两个阶段的机制不能互相矛盾，必须有统一的成本-收益或激励-约束框架
- 每个阶段的 2-3 个理由必须概念独立
- 建议在预测句中明确 curve shape（inverted U-shape / U-shape）
**反模式**: 如果只有一个阶段的机制强，另一个阶段只是"反向论证"或"常识推断"，会显得薄弱；如果两个阶段的理由没有统一框架，会像是两个独立假设硬凑。
