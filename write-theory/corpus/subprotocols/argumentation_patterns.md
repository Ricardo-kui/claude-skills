# Argumentation Patterns

本文件收集 Theory 段落中可复用的论证微观动作组合。每个条目描述一个从 Anchor 到 Prediction 的完整或部分动作序列，供 write-theory Phase 2.5 调用。

---

<!-- 
pattern_id: theory_driven_anchor_efficiency_no_relationship
build_type: 机制推演型 / 反直觉预测型
source_papers: ["Singh_Grewal_2023_JMR"]
confidence: low
status: needs_validation
-->

## Pattern: Theory-Driven Anchor — "Efficiency Perspective Predicts No Relationship"

**适用场景**: 当研究挑战一个被默认接受的强理论直觉时使用。不是用经验发现锚定，而是用一个理论视角的预测作为论证起点。
**微观动作序列**: Anchor（理论前提）→ Gap/Puzzle（反直觉转折）→ Mechanism Move → Warrant → Prediction
**范文来源**: Singh and Grewal (2023), *Journal of Marketing Research*

**骨架**:
```
[Anchor] From an efficiency perspective, [IV] should not influence [DV] because [IV] does not alter [mechanism that determines DV].
[Gap/Puzzle] However, a [theory]-based perspective and associated [model/literature] suggest that [IV] [direction] [DV].
[Mechanism Move] We argue that [IV] influences [DV] through [mechanism].
[Warrant] This is consistent with [theory/model], which posits that [theoretical argument] ([citations]).
[Prediction] Therefore, we hypothesize: H1: [IV] is [direction] related to [DV].
```

**为什么有效**: 用一个读者默认接受的理论作为"稻草人"，然后反转，制造更强的认知张力。
**注意事项**: 
- 必须准确陈述效率视角的预测，不能 caricature
- 反转必须有独立的理论框架支撑，不能只靠 "however"
**反模式**: 如果效率视角本身在文献中并不占主导，不要用此 Anchor，否则会显得牵强。

---

<!-- 
pattern_id: three_mechanism_trunk_with_concrete_illustrations
build_type: 机制推演型 + 调节效应型
source_papers: ["Shen_Zhou_Wang_Zhang_2022_JOM"]
confidence: medium
status: ready_for_corpus
-->

## Pattern: Three-Mechanism Trunk with Parallel Concrete Illustrations

**适用场景**: 主效应有多个并行的中介/机制路径，且每个路径都需要让读者在经验世界中"看见"时。
**微观动作序列**: Anchor（构念定义）→ Mechanism Move 1/2/3（每个配 illustration）→ Warrant → Prediction
**范文来源**: Shen, Zhou, Wang, and Zhang (2022), *Journal of Operations Management*

**骨架**:
```
[Anchor] We suggest that [IV] may [direction] [DV] for three reasons.

[Mechanism Move 1] First, [IV] may induce [state 1], which [effect on DV].
[Concrete Illustration] For example, [company/context]...

[Mechanism Move 2] Second, [IV] may lead to [state 2], preventing firms from [action].
[Concrete Illustration] For instance, [company/context]...

[Mechanism Move 3] Third, [IV] may cause [state 3], decreasing firms' ability to [action].
[Concrete Illustration] [company/context]...

[Warrant] Taken together, these mechanisms suggest that [IV] undermines [DV].
[Prediction] Therefore, we hypothesize: H1: [IV] is [direction] related to [DV].
```

**为什么有效**: 多个机制并行展开，每个都有案例锚定，既展示理论深度又保持可读性。
**注意事项**: 
- 三个机制必须概念独立，不能是同一机制的不同标签
- 每个 illustration 必须对应其机制步骤，不能通用
**反模式**: 如果只有一个机制，不要硬拆成三个，会露出拼凑痕迹。

---

<!-- 
pattern_id: indirect_moderation_mediates_moderation
build_type: 假设树型 / 机制推演型
source_papers: ["Singh_Grewal_2023_JMR"]
confidence: low
status: needs_validation
-->

## Pattern: Indirect Moderation — "The Interaction of X and W2 Mediates the Moderating Effect of W1"

**适用场景**: 当理论预期一个 moderator 的调节作用本身被另一个变量中介时使用（mediated moderation）。
**微观动作序列**: Anchor（两个独立调节已建立）→ Mechanism Move（W2 传播 W1 的信息）→ Warrant（方法论文献 + 理论逻辑）→ Prediction
**范文来源**: Singh and Grewal (2023), *Journal of Marketing Research*

**骨架**:
```
[Anchor] As discussed, [W1] moderates the [IV]→[DV] relationship, and [W2] also moderates this relationship.
[Mechanism Move] We argue that [W2] mediates the moderating effect of [W1] on the [IV]→[DV] link because [W2] disseminates [information] about [W1], thereby shaping [actor]'s response.
[Warrant] This is consistent with [theory], which suggests that [argument] ([citation]). Model B in [methodology paper] captures this indirect moderation structure.
[Prediction] Therefore, we hypothesize: H[X]: The interaction of [W2] and [IV] mediates the moderating effect of [W1] on the relationship between [IV] and [DV].
```

**为什么有效**: 把复杂的统计模型（mediated moderation）转化为可理解的理论叙事。
**注意事项**: 
- 必须独立论证为什么 W2 会中介 W1 的调节作用，不能只引用方法论文献
- 建议在 H4 前用图示（Model A vs Model B）辅助
**反模式**: 如果 W2 只是另一个调节变量，不要硬说成间接调节。

---

<!-- 
pattern_id: preemptive_competing_account_management
build_type: 跨类型
source_papers: ["Gamache_McNamara_Mannor_Johnson_2020_SMJ", "Desai_2012_AMJ"]
confidence: high
status: ready_for_corpus
-->

## Pattern: Preemptive Competing Account Management in T2 Transition

**适用场景**: 当读者、文献或同一理论内部存在两个（或多个）看似合理的竞争预测，作者需要在 T2→T3 过渡段主动管理这些竞争解释时使用。
**微观动作序列**: Anchor（理论前提）→ Competing Prediction(s) → Resolution（直接拒绝 或 调节裁决）→ Pivot → Mechanism Move → Prediction
**范文来源**:
- Gamache, McNamara, Mannor, and Johnson (2020), *Strategic Management Journal*（直接拒绝型）
- Desai, V. M. (2012), *Academy of Management Journal*（调节裁决型）

**父模式骨架**:
```
[Anchor] Drawing on [theory], prior work suggests that [general relationship or pressure].
[Competing Prediction 1] One might expect that [prediction A].
[Competing Prediction 2] Alternatively, [prediction B].
[Resolution] 
  Option A (Direct Rejection): However, these accounts overlook [key mechanism / heterogeneity].
  Option B (Moderation Resolution): Yet existing theory does not specify when [A] rather than [B] occurs.
[Pivot] We argue that [correct prediction or resolution mechanism].
```

### 子变体 A：Direct Rejection（Gamache 型）

**适用构建类型**: 机制推演型 / 竞争假设型 / 反直觉预测型
**核心逻辑**: 完全拒绝竞争预测，提出正确预测

**骨架**:
```
[Alternative 1] One might intuitively expect that [intuitive prediction 1].
[Alternative 2] Alternatively, it might be argued that [intuitive prediction 2].
[Rejection] However, these accounts overlook [key mechanism / heterogeneity].
[Pivot] Drawing on [theory], we argue that [correct prediction].
```

### 子变体 B：Competing Baseline → Moderation Resolution（Desai 型）

**适用构建类型**: 调节效应型
**核心逻辑**: 不拒绝竞争预测，而是用 moderator 决定何时哪个预测成立

**骨架**:
```
[Competing Baseline] Institutional theory suggests at least two responses. First, [response A] because [reason]. On the other hand, [response B] because [reason].
[Puzzle] Therefore, it is important to determine the conditions under which [A] or [B] is more likely.
[Resolution] We argue that [moderator] determines which response prevails.
```

**为什么有效**: 在读者产生疑问之前先回答疑问，显示作者对 literature 的掌控；同时为后续假设推导清除障碍或建立边界条件议程。
**注意事项**: 
- 竞争预测必须是读者/文献真正会提出的，不能 straw man
- 拒绝或裁决必须基于理论，不能只靠 "however"
- 此模式适合放在 T2→T3 过渡段，不适合放在单个假设推导段内部
- 调节裁决型需要确保两个竞争响应都有独立理论依据
**反模式**: 如果竞争预测本身并不强，强行列出会显得冗余；如果 moderator 与两个响应的理论联系不对称，会显得牵强。

---

<!--
pattern_id: extension_logic_analogous_domain
build_type: 跨类型
source_papers: ["Desai_2012_AMJ"]
confidence: low
status: needs_validation
-->

## Pattern: Extension Logic from Analogous Domain

**适用场景**: 当目标研究领域的文献对某个行为/机制讨论较少，但相邻领域有丰富研究时，使用扩展逻辑将相邻领域的机制引入目标领域。
**微观动作序列**: Anchor（目标领域缺口）→ Analogous Domain Evidence → Mechanism Transfer → Prediction
**范文来源**: Desai, V. M. (2012), *Academy of Management Journal*

**骨架**:
```
[Anchor] Although little work in [target domain] addresses [behavior], [broader theoretical issue] is central to understanding [phenomenon].
[Analogous Domain] Research on [analogous domain] provides insight. [Author] (year) found that [concrete finding] — [argument summary].
[Mechanism Transfer] Extending this process to [target domain] suggests that [transferred mechanism].
[Prediction] Therefore, we hypothesize: H[X]: ...
```

**为什么有效**: 既承认了目标领域的文献缺口，又借用相邻领域的成熟研究为新假设提供合法性。
**注意事项**: 
- 必须明确说明相邻领域与目标领域的相似之处和差异
- 机制转移不能是简单类比，必须有理论依据
- 建议在转移后立即说明为什么目标领域的特殊性使得该机制适用
**反模式**: 如果相邻领域与目标领域在关键维度上不同，强行扩展会显得牵强。
