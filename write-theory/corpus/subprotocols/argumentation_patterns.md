# Argumentation Patterns

本文件收集 Theory 段落中**非常规论证动作**——主要是 T2→T3 过渡段、竞争解释管理、跨域借用、行业情境限定等"非标准段落骨架"动作。

> **与 `hypothesis_derivation_patterns.md` 的分工**（两文件 self-description 曾不可区分，已澄清）：
> - `hypothesis_derivation_patterns.md` = **段落级假设推导骨架**（Anchor→Mechanism→Warrant→Prediction 完整序列及其变体）——一个假设推导段怎么写
> - 本文件（argumentation_patterns）= **过渡段/非常规动作**（竞争解释管理、Extension Logic、双理论分期、行业情境、双机制汇聚、最小对对比）——标准段落骨架之外的特殊论证动作

---

<!-- 
pattern_id: theory_driven_anchor_efficiency_no_relationship
build_type: 机制推演型 / 反直觉预测型
source_papers: ["Singh_Grewal_2023_JMR"]
confidence: low
status: needs_validation
DEPRECATED: 重复 pattern。权威版在 hypothesis_derivation_patterns.md（Theory-Driven Anchor + Puzzle Turn，更详且为 VERIFIED pattern home_file）。本条保留为指针。
-->

→ **Theory-Driven Anchor** 见 `hypothesis_derivation_patterns.md`（Pattern: Theory-Driven Anchor + Puzzle Turn）

---

<!-- 
pattern_id: three_mechanism_trunk_with_concrete_illustrations
build_type: 机制推演型 + 调节效应型
source_papers: ["Shen_Zhou_Wang_Zhang_2022_JOM"]
confidence: medium
status: ready_for_corpus
DEPRECATED: 重复 pattern。权威版在 hypothesis_derivation_patterns.md（Multi-Mechanism Trunk，更详且含 downstream moderator linkage，为 VERIFIED pattern home_file）。
-->

→ **Three-Mechanism / Multi-Mechanism Trunk** 见 `hypothesis_derivation_patterns.md`（Pattern: Multi-Mechanism Trunk）

---

<!-- 
pattern_id: indirect_moderation_mediates_moderation
build_type: 假设树型 / 机制推演型
source_papers: ["Singh_Grewal_2023_JMR"]
confidence: low
status: needs_validation
DEPRECATED: 重复 pattern。权威版在 hypothesis_derivation_patterns.md（Indirect Moderation / Mediated Moderation Derivation，更详）。
-->

→ **Indirect Moderation / Mediated Moderation** 见 `hypothesis_derivation_patterns.md`（Pattern: Indirect Moderation / Mediated Moderation Derivation）

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

---

<!--
pattern_id: dual_theory_two_stage_iv
build_type: 机制推演型
source_papers: ["Mayo_2022_POM"]
confidence: high
status: ready_for_corpus
-->

## Pattern: Dual-Theory Two-Stage Mechanism

**适用场景**: 同一 IV 在不同阶段/区间产生不同方向或不同机制效应，单一理论无法覆盖。
**微观动作序列**: Anchor（理论总体适用）→ Stage 1 Theory + Mechanism + Prediction → Stage 2 Theory + Mechanism + Prediction
**范文来源**: Mayo, Ball & Mills (2022), *Production and Operations Management*（CEO tenure: attribution theory for early tenure; signaling theory for late tenure）

**骨架**:
```
[Anchor] We leverage [Theory A] to explain the relationship between [IV] and [DV] in [stage 1]. [Theory A] explains [mechanism A] ([citation]).
[Stage 1 Prediction] H1: [direction] relationship in [stage 1].

[Stage 1 Boundary] This effect is stronger when [moderator 1] because [reason] ([citation]).
H2: [boundary prediction for stage 1].

[Stage 2 Theory] Theoretical support for [stage 2] is found in [Theory B]. [Theory B] suggests [mechanism B] ([citation]).
[Stage 2 Prediction] H3: [boundary prediction for stage 2].
```

**为什么有效**: 避免“一个理论硬套全程”的牵强；两个阶段各有独立的理论基础和边界条件。
**注意事项**:
- 两个理论必须有清晰的分工边界
- 每个阶段的 moderator 必须理论上与对应机制匹配
- 需处理“中间阶段”行为（若 IV 为连续变量）
**反模式**: 两个理论实际上预测同一机制，或阶段划分缺乏理论依据。

---

<!--
pattern_id: industry_context_as_scope_condition
build_type: 机制推演型
source_papers: ["Mayo_2022_POM"]
confidence: medium
status: ready_for_corpus
-->

## Pattern: Industry Context as Scope Condition

**适用场景**: 研究某一行业，需要论证该行业的特殊制度/频率/监管环境使机制更显著。
**微观动作序列**: Anchor（目标行业特征）→ Contrast（与其他行业比较）→ Regulatory Comparison → Mechanism Link
**范文来源**: Mayo, Ball & Mills (2022), *Production and Operations Management*（consumer products vs auto/medical device/pharma/food recalls）

**骨架**:
```
[Context A] is [attribute], occurring only [frequency] in our study ([citation]). This is in contrast with [Context B]: [frequency 1]; [Context C]: [frequency 2].

The regulatory strategy of [Regulator A] is [attribute] compared to [Regulator B/C]. For example, [specific regulation difference].

The [attribute] of [Context A], combined with [second attribute], creates an environment in which [actors] are tempted to [behavior].
```

**为什么有效**: 将机制嵌入具体制度环境，增强外部效度主张。
**注意事项**:
- 比较数据需准确且有来源
- 比较行业需在理论上相关
**反模式**: 堆砌行业数据但无明确机制链接。

---

<!--
pattern_id: dual_mechanism_same_direction
build_type: 机制推演型
source_papers: ["Ball_2018_JOM"]
confidence: medium
status: ready_for_corpus
-->

## Pattern: Dual Mechanism Convergence

**适用场景**: IV 可能通过两个概念独立的中介路径影响 DV，但两条路径均预测同一方向。
**微观动作序列**: Anchor（IV 影响 DV）→ Mechanism A → Mechanism B → Convergence → Prediction
**范文来源**: Ball, Shah & Donohue (2018), *Journal of Operations Management*（defect detectability → lower recall likelihood via perceived harm OR perceived cost）

**骨架**:
```
[Mechanism A] [IV] may influence [DV] through [mediator A] because [reason] ([citation]).
[Mechanism B] It is also possible that [IV] influences [DV] through [mediator B] because [reason] ([citation]).
[Convergence] Whether [mediator A] or [mediator B], we expect [direction] relationship.
[Prediction] Accordingly, we hypothesize: H[X]: [prediction].
```

**为什么有效**: 在主效应阶段承认机制多元性，为后续中介分析留空间。
**注意事项**:
- 两个机制必须均指向同一方向
- 后续 Methods 应计划检验中介
**反模式**: 两个机制方向矛盾却强行合并为一个假设。

---

<!--
legacy_pattern_id: simultaneously_recognize_leverage
build_type: 跨类型
source_papers: ["Grewal_Vana_Stephen_2025_JM"]
confidence: medium
status: ready_for_corpus
DEPRECATED: 跨文件重复。权威 home 是 construct_differentiation_patterns.md（该 pattern 属构念辨析的过渡论证，且该文件 self-reference 它）。本条保留为指针。
-->

→ **Simultaneously Recognize X but Leverage Y** 见 `construct_differentiation_patterns.md`（Pattern: Simultaneously Recognize X but Leverage Y——该文件是此 pattern 的权威 home）

---

<!--
pattern_id: minimal_pair_contrast_vignette
build_type: 机制推演型 / 构念辨析型（prose-craft showing device）
source_papers: ["Cutolo_Ferriani_2024_JOM"]
confidence: high
status: ready_for_corpus
related: 与 "Multi-Mechanism Trunk"（见 hypothesis_derivation_patterns.md）互补——后者给"例子"，本模式给"受控对比"
-->

## Pattern: Minimal-Pair Contrast Vignette (受控最小对对比)

**适用场景**: 当机制的核心变量是一个**可沿连续维度变化的语言/表征特征**（abstraction、concreteness、active/passive voice、frame strength 等），需要让读者"看见"该变量如何改变机制输出时。借鉴语言学的 minimal-pair（最小对立体）方法：构造**仅在该理论变量上不同、其余完全相同**的两个句子/案例并置对比，从而把抽象机制**隔离并显形化**。

**微观动作序列**: Introduce a stylized atypical actor → present minimal pair (low vs high on the theoretical variable) → analyze what each version evokes → conclude how the variable drives the mechanism

**范文来源**: Cutolo & Ferriani (2024), *Journal of Management*（用 "Leah is a painter and a musician" vs "Leah is an artist" 隔离 abstraction 对 atypicality-processing 的作用）

**骨架**:
```
To illustrate, consider a [typical case of the phenomenon]: an actor ([name]) who [description that makes the actor atypical]. Now consider the following two [sentences/claims] that differ in [theoretical variable]:

> [Version LOW on theoretical variable]: [sentence/claim]
> [Version HIGH on theoretical variable]: [sentence/claim]

The [words/elements] in the LOW version evoke [a network of specific features / detailed expectations] associated with [basic-level category], [list the specific attributes triggered]. To convey the value of [atypical combination], a narrative using the LOW version must therefore [spell out the elaborate strategy needed] — this combination is unlikely to make sense due to [the difficulty the mechanism predicts].

In contrast, the HIGH version [drops the specific features / moves to a superordinate level] and retains only [shared/general attributes] such as [general features]. Hence the HIGH version evokes [broader, more encompassing meanings] that help [decision-makers] draw on a more [inclusive/encompassing category], [resulting in the eased processing / mechanism output the theory predicts].
```

**原文锚定**:
> "consider a 'typical' case of atypicality: an actor (let us call her Leah) trying to broaden her identity by taking on multiple and unrelated professional roles... Now consider the following two sentences with different levels of abstraction: *Leah is an extraordinary painter and a talented musician.* / *Leah is an extraordinary artist.* The nouns *painter* and *musician* evoke a network of attributes... [whereas] *artist* reflects a superordinate-level (i.e., more abstract) category... the more abstract word *artist* evokes general features and broader meanings such as creativity, self-expression, and perseverance..."

**关键特征**:
- **受控对比（minimal pair）而非单纯举例**：两个版本**只在该理论变量上不同、其余受控相同**——这是实验设计的 logic 移植到 prose，使读者能干净地把机制输出归因于该变量（而非其他混淆）
- **并置呈现（side-by-side blockquote）**：两个版本用引用块紧邻排版，视觉上强制对比，降低读者认知负担
- **逐版本拆解 evoked attributes**：不只说"A 抽象 B 具体"，而是**枚举每个版本触发的具体属性网络**（painter/musician → 艺术运动/乐器/工具；artist → 创造力/自我表达/毅力），让"机制如何运作"变得可感
- **从 vignette 自然回到假设**：vignette 收束后用 "these arguments suggest..." 回到正式假设，illustration 不喧宾夺主

**为什么有效**: 
- 机制段最大的失败模式是"抽象论述抽象"——读者读完 why chain 仍不知道机制在现实中长什么样。minimal pair 用最小成本把机制**显形**
- 与 "Three-Mechanism Trunk with Parallel Concrete Illustrations" 互补：后者为**多条并行机制各配一个例子**（举例型）；本模式为**单条机制的核心变量做受控对比**（隔离型）

**注意事项**:
- 两个版本**必须只在该理论变量上不同**——若同时变了多个特征，对比不"minimal"，读者无法归因
- 拆解 evoked attributes 时要**具体到可枚举**（艺术运动、乐器、工具名），不能泛泛说"更具体/更抽象"
- vignette 的 stylized actor（如 Leah）应是**中性的虚构例子**，不要用真实具名公司/人（避免事实争议），除非该真实案例本身是论文的现象焦点
- 一个机制段最多用 **1 个** minimal pair——多个会打断 why chain 的推演节奏

**反模式**: 把 minimal pair 写成"例子堆砌"（两个版本各举一堆不对应的具体公司），失去受控对比的隔离力；或用真实知名公司做对比引入事实争议；或在每条假设前都加 vignette 导致节奏破碎。

> **近邻**: 若最小对服务的是**兄弟构念可分离性**（固定维度 A 的标量、只变维度 B 的空间/结构构型），见 `construct_differentiation_patterns.md`::`geometric_sibling_construct_minimal_pair`（Li et al. 2026 POM Figure 1）——不要硬套本语言 vignette 骨架。

---

<!--
pattern_id: dual_lens_main_boundary_division
build_type: 机制推演型 + 调节效应型
source_papers: ["Hoffmann_2024_JM"]
confidence: medium
status: ready_for_corpus
-->

## Pattern: Dual-Lens Main/Boundary Division

**适用场景**: 主效应有成熟的核心理论（如 agency theory），但边界/调节变量的选择需要另一套 organizing framework（如 business ethics taxonomy），且后者**不**参与主效应机制推演。

**与 Dual-Theory Two-Stage / Dual-Theory Architecture 的区分**:
| | Dual-Lens Main/Boundary | Dual-Theory Two-Stage | Dual-Theory Architecture |
|---|---|---|---|
| 第二理论角色 | 仅选 moderator + 解释边界 | 同一 IV 不同阶段 | 两理论解释同一 outcome |
| 出现位置 | T2 并列宣告；T5 才启用第二透镜 | T3 分阶段切换 | T2–T3 全程双理论 |
| 假设分工 | H1=透镜1；H2/H3=透镜2 | H1/H2 vs H3/H4 分阶段 | 两理论共同支撑主效应 |

**骨架**:
```
[T2 Opening] In developing our conceptual framework, we rely on arguments from 
[primary theory] ([citation]) and the [secondary literature domain] ([citation]).

[T3 Main Effect — primary lens only]
[Agency/mechanism chain using primary theory] → H1.

[T5 Boundary — secondary lens activated]
Given the argument that [primary-mechanism logic] underlie[s] [main effect], 
our investigation of boundary conditions will be guided by insights from 
[secondary literature] on [mechanisms that mitigate the core conflict] ([citation]).

[Secondary organizing framework taxonomy] → map to moderator 1 → H2; moderator 2 → H3.
```

**为什么有效**: 避免用主理论硬推 moderator（显得 ad-hoc），也避免双理论全程并行（喧宾夺主）；第二透镜只在"选哪些边界变量"时出场，理论分工清晰。

**语料锚定**: Hoffmann, Cheong, Phan & Zurbruegg (2024, JM) — agency theory (H1 trade-off/shock) + Husted (2007) business ethics (H2 customer culture, H3 institutional monitoring).

**注意事项**:
- 第二理论必须是真实文献分类系统，不能是作者自创二分法
- T2 必须预告双透镜分工，否则 T5 引入第二理论显得突兀
- 主效应段落不得偷用第二理论的构念

**反模式**: 两个理论都解释主效应（应合并或改用 Dual-Theory Architecture）；第二理论只在 Discussion 出现、Theory 无预告。

