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
pattern_id: simultaneously_recognize_leverage
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

---

<!--
pattern_id: neglected_lens_via_dominant_view_contrast
build_type: 机制推演型 / 视角选择
source_papers: ["lunetal2026"]
confidence: medium
status: ready_for_corpus
-->

## Pattern: Neglected Lens via Dominant-View Contrast（优势视角对照被忽视透镜）

**适用场景**: T2 开场需要把读者从过度复制的正向/优势视角转到对话内部已有、但被忽视的方差/实验透镜，再把抽象方差收成可观察下尾失败。不是辩证对立，也不是竞争假设——两条透镜可共存，作者选择被忽视的一条来兑现其蕴含。

**微观动作序列**: Dominant view（优势/均值上移）→ Implicit assumption named → Neglected lens（方差/实验）→ Concrete lower-tail object → Pivot to H1 mechanism

**范文来源**: Lun, Zurbruegg, Mount & Cheong (2026), *Entrepreneurship Theory and Practice*

**骨架**:
```
[Dominant view] [Construct] is commonly viewed as a [performance-enhancing orientation], [shifting the distribution upward] ([citations]). This view—the [label-as-advantage] perspective—"implicitly assumes that [construct] somehow provides an advantage" ([citation]).

[Neglected lens] Notwithstanding the benefits, [adjacent theory] highlights that the very mechanism through which value is generated necessarily widens the distribution of outcomes. This is consistent with the [variance-enhancing] logic of the [label-as-experimentation] perspective ([citation]).

[Contrast] Yet most research remains anchored in the [advantage] perspective, emphasizing benefits while overlooking downsides. Even within the smaller [experimentation] body, scholars have examined [dispersion around the mean] rather than the specific types of failure [construct] may produce.

[Pivot] Without theorizing how [construct] manifests as failure, we lack insight into the mechanisms through which exploratory tendencies produce harmful outcomes. To address this omission, we focus on [observable operational failure].
```

**原文锚定**:
> "Yet, most EO research remains anchored in the EO-as-advantage perspective, emphasizing its performance-enhancing benefits while overlooking its downsides."

**为什么有效**: 缺口不是"缺一篇调节论文"，而是优势透镜未兑现其自身蕴含的下尾；对照让机制修订显得内在而非外加。

**适用条件**: 对话内部必须真有可引用的 neglected lens；不能事后发明第二条理论来打稻草人。

**注意事项**:
- 不要写成 Incommensurability（两条不可通约的对立预测）
- 下尾对象必须可观察、可记录，不能停在 abstract failure / exit
- 与 Dual-Lens Main/Boundary 分工：本模式管 T2 视角选择；后者管主效应理论 vs 边界 taxonomy

**反模式**: 把 advantage vs experimentation 写成必须二选一的竞争假设；或对照之后仍用均值绩效当 DV。
pattern_id: audience_foil_then_focal_signal_single_H
build_type: 机制推演型（反直觉主效应）
source_papers: ["Chen_Ganesan_Liu_2009_JM"]
source: chenganesanliu2009
confidence: medium
status: VERIFIED
story_fidelity: section_variant
note: VERIFIED（expert_audit_override 2026-08-29 召回主题单源裁决，chenganesanliu2009 = 召回策略→财务价值）；勿升格为完整 G（成对受众假设）
-->

## Pattern: Audience-Foil then Focal-Signal (Single Comparative H)

**适用场景**: 文献默认受众 A 对行动 X 给**正评价**，但论文的 DV 由受众 B 定价；需要用 A 的正面解读作 **foil/concession**，再转折到 B 的负面信号链，收敛为**单一比较主效应**（非 Audience A/B 成对假设）。

**验证状态**: VERIFIED（召回主题单源裁决，chenganesanliu2009）

**微观动作序列**: Prior-work foil (audience A positive) → However pivot (audience B reads X differently) → Focal signal mechanism (+ loss aversion / ambiguity warrants) → Optional rarity/scrutiny amplifier → Therefore + single comparative H

**范文来源**: Chen, Ganesan, & Liu (2009), *Journal of Marketing*（consumer-positive foil → investor-negative signal → H1 comparative）

**骨架**:
```
[Foil] Prior work suggests [action X] has positive consequences for [audience A]
because [quality / trust / reputation signal].
[Pivot] However, [audience B] may view the implications of [X] differently from [audience A]:
observing [early / proactive / visible] moves, they infer [severity severity / forced disclosure / downside],
amplified by [loss aversion / ambiguity→worst-case].
[Amplifier — optional] Rarity of [X] further increases scrutiny.
[Convergence] Therefore, we propose that [X / strategy pole A] receives greater [evaluator B] attention
and is interpreted as a signal of [severe downside], so [DV_B] is affected more negatively when
[strategy A] than when [strategy B / contrast pole].
[H] [Strategy A] is more negatively related to [DV_B] than [Strategy B].
```

**与变体 G（辩证对立）的硬区分**:
| | Audience-foil → single H（本模式） | 变体 G 辩证对立 |
|---|---|---|
| DV | 单一（由受众 B 定价） | 常为多受众 / 成对 outcome |
| 假设 | **1 条比较主效应** | Audience A/B **成对**假设 |
| 受众 A 角色 | foil / concession（不成假设） | 独立机制 + 独立 H |
| 适用贡献 | 反直觉：同行动、异解读 → 对 B 更负 | 贡献对象就是异质受众对立评价 |

**为什么有效**: 保留文献正面预期的张力，却不把贡献漂移成双受众理论；why 靠「同行动、异解读」完成，而非堆 citation。

**配套句式**:
- 受众切换句 → `../sentences/acknowledgment_response.md`（Audience-Foil Pivot）
- 比较型主效应 H → `../sentences/hypothesis_forms.md`（Comparative Main Effect）

**注意事项**:
- foil 必须是读者真实会想到的默认正面解读，不能 straw man
- 焦点机制必须有独立 warrant（信号 + 行为金融/模糊处理等），不能只靠 However
- DV 必须明确由受众 B 定价；若贡献对象是双受众对立，改用变体 G

**反模式**:
- 强行写成 Audience A/B 成对假设（那是变体 G）
- 长制度/流程叙述冒充机制链（流程只提供 scope，不提供 X→Y warrant）
- 把能力/信任正面信号与 downside 信号并列却不裁决主导解读

**原文锚点** (Chen, Ganesan & Liu 2009, JM):
> "However, it is likely that the stock market and investors view the implications of a proactive product-recall strategy differently from consumers."



### 变体 A：T3_rival_prediction_rebuttal（moon2026）

**模板/骨架**:
> "However, it can be argued that [treatment] is likely to [opposite-signed prediction] because [rival mechanism]. Consistent with this logic, research finds that [supporting evidence for rival]. However, this is unlikely to be the case because [superordinate premise / salience hierarchy]. In fact, research consistently finds that [evidence for superordinate premise]. Therefore, we expect [directional main-effect prediction]."

来源：Moon et al. (2026, Journal of Marketing)。


### 变体 B：反预测排除段（Counter-Prediction Exclusion before H1，ball_2018 型）
**band**: 薄弱（single_source_verified；用户裁决单源可写）
**适用场景**: 主效应方向与直觉相反（或文献中存在相反预测）时，在假设句之前用专门段落排除反方向。
**骨架**:
One potential response to [IV] may be [opposite-direction mechanism]. However, we believe that this is less likely in our setting for two reasons. First, [prerequisite for the opposite mechanism is absent, with evidence]. Second, [cost/structural reason the opposite is suboptimal]. We therefore posit that instead of [opposite outcome], [IV] will be associated with [predicted direction].
**论证功能**: 把"为什么不是直觉方向"变成两步式排除（前提缺失 + 结构不经济），而非简单断言；与 rival_prediction_rebuttal 的差异在于它排除的是"同一 IV 的反方向机制"，而非 rival 理论。
**原文锚点**: "One potential response to heightened product competition may be to manufacture higher quality products. However, we believe that this is less likely in our setting for two reasons."
**配套证据型**: 排除理由需至少一条有实证 citation 支撑，不得全靠断言。


## Pattern: Decision-Rights Preamble → Indirect-Governance Chain（决策权前言→间接治理链）

**适用场景**: 上游治理主体（董事会/投资者/监管者）不直接执行 focal decision，而是通过周期性评审、反馈与默认期望影响下游决策者。在理论化上游主体属性之前，必须先用制度过程描述定位其影响入口——否则读者会把 X→Y 误读为直接干预。适用于间接治理、tone-setting、委托链条研究。

**结构**: 四源证据基础声明（文献+监管文件+业界访谈+监管者访谈）→ 决策权链条（谁监测→谁审议→谁建议→谁决定→谁评审）→ 上游主体角色定位（"不决定，但设定基调"）→ 反向默认对照的访谈轶事（见 paired_opposite_default_vignettes）→ 链条与后续两假设边际的对接

**完整决策链实录（wowak2020 §2，写作时按此粒度写足）**:
1. **监测**：product quality engineers 持续监测质量问题信号——内部（product testing / inspection results）+ 外部（customer / regulator complaints）
2. **召集**：系统性问题确认后，product quality manager 召集 managerial recall committee（manufacturing, R&D, quality, legal, clinical, regulatory 六职能 senior directors/managers）
3. **建议**：委员会讨论"是否需要召回"，向相应 VP 提出建议——通常由 VP of quality 做出最终召回决策
4. **评审**：VP of quality 周期性地把**已发起与未发起**的召回决策一并呈报董事会评审，董事会提供反馈与校准（feedback and calibration）
5. **角色定位**："boards do not make the recall decisions, but instead they set the tone and expectations for how managers are to make these decisions"——董事会不决定个案，管理层在董事会设定的默认期望下行使裁量
6. **默认期望的两端实证**（firm A）：3 天举证期内证明"无需召回"否则强制召回，默认=快而果断、客户安全优先，该期望由董事会确立，女性董事尤其追问客户伤害程度、其质询定调决策方式
7. **反向默认实证**（firm B）：举证责任反转（委员会须证明"召回绝对必要"否则不召回）、cost-benefit 优先于客户安全、该优先级由董事会驱动、男性董事追问"谁会被开除多快"、有经理的 board-approved 年度奖金（上限 $30,000 ≈ 年薪 25%）与"零召回"目标挂钩
8. **第三方验证**：FDA 高级主任确认此类离散普遍存在——FDA 人力资源有限 + 缺乏企业专有产品级失效数据，只能依赖企业自行决定召回时机与方式
9. **对接假设**：rule-following 期望作用于低严重度边际（是否发起，H1 计数）；stakeholder responsiveness 期望作用于高严重度边际（多快发起，H2 时长）——同一链条、两个决策窗口

**骨架**:
```
To articulate our hypothesized relationships, we first explain how [decision] is made.
[Evidence base: (1) literature; (2) regulator documents; (3) practitioner interviews; (4) regulator interview.]

[Decision-rights chain]
[Front-line actor] continuously monitors [signal sources]. When [trigger], [convening actor] convenes
[committee], tasked with discussing whether [action] is needed and making a recommendation to
[ultimate decision-maker]. On a recurring basis, [decision-maker] reviews [initiated and uninitiated
cases] with [upstream governor] so the board can provide feedback and calibration.

[Upstream role locution]
In other words, [upstream governor] does not make the [decision], but instead they set the tone
and expectations for how [downstream actors] are to make these decisions.
```

**为什么有效**: 在任何假设之前把"谁能决定什么"说清楚，使 X（上游主体属性）的作用点落在"期望设定"而非"直接命令"上；后续两个假设共享同一条间接链，机制不出层次。

**注意事项**:
- 必须有可核验的多源证据基础（本文用 4 源），否则制度过程描述会被视为臆测
- 决策权链条每一步都要有具名行动者（monitor→committee→VP→board）
- 上游角色句必须显式否定直接干预（"do not make... but instead..."）

**反模式**: 制度前言写成行业背景流水账；上游主体被默认写成直接决策者。

**与近邻模式区分**: vs minimal_pair_contrast_vignette（Cutolo & Ferriani）——那是 controlled-contrast 案例装置；本模式是决策权架构描述，案例对照由其后的轶事对完成。

**原文锚点**: "In other words, boards do not make the recall decisions, but instead they set the tone and expectations for how managers are to make these decisions."


### 变体 C：判别式替代解释排除（westphal_zajac_1998_symbolic_management 型）

**模板**:
> "We test whether [audience reactions] to [verbal accounts] reflect [actual organizational practices] by examining [reactions] when [X] is announced and implemented and when [X] is announced but not implemented. Observing [the predicted reaction] even when [adoption] is decoupled from [implementation] would provide stronger evidence that [the communication] represents [symbolic management] and not merely [rational communication or persuasion] (cf. [prior account])."

**来源**: westphal_zajac_1998_symbolic_management (ASQ), §2.2 P4

**原文锚定**:
> "Observing a positive market reaction to agency explanations even when LTIP adoption is decoupled from actual implementation would provide stronger evidence that verbal enhancement in proxy statements represents symbolic management and not merely rational communication or persuasion (cf. Porter, Allen, and Angle, 1981)."

**关键特征**:
- 把最强替代解释（语言属实/理性说服）直接转化为设计的判别条件：decoupling 子样本即"语言与事实不符仍获正面反应"的自然实验——排除动作不是脚注而是假设检验本身
- "would provide stronger evidence that X represents A and not merely B" 的"更强证据"措辞承认解释的或然性，比"proves"式排除更诚实且更难被攻击
- 与引言的 Inadequacy 次级 gap（"have not been able to rule out the possibility that language enhancements may actually fit the facts"）首尾闭环：Introduction 承认的排除不能，正文以设计兑现

**适用**: 符号/沟通/印象管理类自变量与"事实是否相符"存在天然混淆的研究；Inadequacy 型 gap（无法排除替代解释）承诺的正文兑现

**禁忌**: 判别条件必须在 Methods 真正可实现（本篇: 采纳未实施子样本），不能只作修辞假设；"not merely" 后的替代解释必须是文献中最强而非最弱的版本

**验证状态**: VERIFIED — expert_audit_override (user 2026-08-28: 单源足矣; paper_count=1)


### 变体 D：两极之间的假设声明段（westphal_zajac_1998_symbolic_management 型）

**模板**:
> "While we do not assume [strong-form extreme assumption], we also do not assume that [the system] is [irrational]. Rather, we assume that [audience members] are [intendedly but boundedly rational processors] who are interested in reducing [uncertainty] and therefore value [socially legitimate indications] that [the core problem] is being addressed."

**来源**: westphal_zajac_1998_symbolic_management (ASQ), §2.1 P7

**原文锚定**:
> "While we do not assume strong-form market efficiency, we also do not assume that markets are irrational. Rather, we assume that investors are intendedly but boundedly rational information processors who are interested in reducing uncertainty and therefore value socially legitimate indications that agency problems are being addressed."

**关键特征**:
- 在机制链中段（非文首）插入假设声明：双向否定两个极端（强式有效 vs 非理性），再用 "Rather, we assume" 给出中间立场——一次化解"你不信市场有效?"的双向审稿质疑
- 假设内容直接服务于机制（"interested in reducing uncertainty" 正是符号行动起效的心理前提），假设段即机制段而非免责声明
- "intendedly but boundedly" 的让步式限定把有限理性与 March/Simon 传统对齐，借用行为学派权威为符号机制供合法性

**适用**: 机制依赖"受众有限理性/信息处理约束"的理论；预测与主流有效市场或完全理性预设冲突、需中间立场假设的研究

**禁忌**: 两个被否定的极端必须真实对应文献中的对立阵营，不能立稻草人；假设声明应位于首次被需要的机制步骤之前，过晚则机制已带漏洞运行

**验证状态**: VERIFIED — expert_audit_override (user 2026-08-28: 单源足矣; paper_count=1)




<!--
pattern_id: transfer_plus_sorting_dual_warrant_signal
build_type: 机制推演型（信号/背书/声望类假设通用）
source_papers: ["higgins_2003_getting_off_to_a_good_start_the_effects_of_uppe"]
confidence: low-medium（单篇来源，EMERGING 待第二篇交叉验证）
-->

### 变体 E：传递 + 自选择双 warrant 信号推演（Transfer + Sorting Dual-Warrant Signal Derivation）

**适用场景**: 假设核心推理是"X 的某属性向第三方传递 Y 的质量信息"。单一传递论证（"他们在名组织习得了有价值的东西"）易被读作纯光环效应；叠加自选择论证（"有声誉的成员只挑有前景的企业加入"）后，该属性同时成为成员对企业质量的独立投票。
**适用模块**: T3 Mechanism Chain（每个类型分支的第二 warrant；与"类型学分解"架构模式配套使用亦可独立使用）
**范文来源**: Higgins & Gulati (2003), *Organization Science*

**骨架**:
```
[Transfer Warrant]
Having [carriers] who [originated at prominent organizations of type k] signals to
outsiders that [judgments/decisions/capabilities] are likely to be [appropriate/reliable],
given the valuable skills and knowledge they presumably acquired while working
for such firms.

[Sorting Warrant]
Moreover, [construct] affiliations with prominent [type-k] institutions can signal
to others that [quality aspect] is sound, since one would expect [carriers] with such
ties to join only firms that show [quality-aspect] promise. To assume otherwise would
be to believe that [carriers] engage in relationships with firms that are other than
reputation-enhancing.

[Convergence]
[Subject with many such ties] is likely to attract [endorsement outcome].
Therefore, H[k]: ...
```

**为什么有效**: 双 warrant 相互独立——传递 warrant 讲"资源可得"，自选择 warrant 讲"信息可靠性"；后者以反事实否定句式（"否则等于相信成员会做有损声誉的关联"）提前封堵逆向选择质疑，使信号推断不依赖对成员真实动机的额外假设。
**注意事项**:
- sorting warrant 是排他性论证，须与 transfer warrant 分别成句，不可熔成一句
- 反事实否定句式力量强，仅在确有理论前提（如声誉动机的一般假设）时使用
- sorting 逻辑同时隐含排除"成员随机散落"的零假设——这是它区别于单纯背书论证的增量
**反模式**: 把自选择逻辑写成"优秀的人都去好公司"式断言而无声誉动机前提——会被读作同义反复。
**原文锚点**: "To assume otherwise would be to believe that individuals engage in relationships with firms that are other than reputation-enhancing."（H1 推导段 sorting warrant）

<!-- wb:higgins_2003_getting_off_to_a_good_start_the_effects_of_uppe:transfer_plus_sorting_dual_warrant_signal -->

### 模式 E：同果近邻构念反号辨析型（westphal_bednar2005 型）

**模板**:
> "The literature ... clearly distinguishes [focal construct] from [rival construct], a mode of [shared failure] that has received more attention in the [home] literature. Though both may lead to [shared outcome], the determinants of each are distinct. [Shared factor W] is thought to exacerbate [rival], but our theoretical perspective suggests that [W] actually attenuates [focal construct]. With [rival], [actors] fail because [mechanism A]. With [focal construct], [actors] fail because [mechanism B], and these [biases] are enhanced by [low W]."

**来源**: westphal_bednar2005 (ASQ), Theory P13（小节收束段）

**原文锚定**:
> "Social cohesion among group members is thought to exacerbate the presence of groupthink, but our theoretical perspective suggests that social cohesion from friendship ties and demographic homogeneity actually attenuates pluralistic ignorance."
> "With groupthink, groups persist with failing strategies because ... With pluralistic ignorance, groups persist ... because individual members misperceive each other's beliefs"

**关键特征**:
- 辨析的不是定义而是"同一结局、不同机制、同一调节变量反号"——W（凝聚力）加剧 groupthink 但削弱 PI，反号本身就是区分度的证明
- "a mode of [failure] that has received more attention" 承认对手更知名，把自己定位为更精确的机制而非更大名气，姿态克制
- "With [rival], ... because A. With [focal], ... because B." 平行句式让两个机制逐步对照，最后半句用反号条件（enhanced by low W）钉死区分
- 放在小节末尾作收束：先讲完自己的假设再与近邻构念切割，避免开场就陷入概念辩护

**适用**: 引入的构念与某个更知名构念共享结果变量（决策失败、绩效下滑）时的辨析段；调节变量在两个构念中方向相反的对照性研究

**禁忌**: 反号主张必须与前文对 W 的论证一致（本篇前文确实论证了凝聚力降低 PI），临时反转会自相矛盾；对手机制必须以其最强形式陈述，不得偷换成稻草人

### 模式 F：机制前提→情境放大映射型（westphal_bednar2005 型）

**模板**:
> "Though [construct] has been observed in a variety of contexts ([citations]), it may be particularly likely to occur among [focal actors] in [setting]. On one level, [precondition 1: dissent的社会风险] exists because [setting feature] ([citations]). Thus [focal actors] are hesitant to [voice]. [In particular], [precondition 2: 难以发现共同关切] because [setting feature]. At the same time, [precondition 3: 相互可观察性] is high because [setting feature]. [Observing others' inaction] leads to the biased pattern of attributions noted above, resulting in [construct]."

**来源**: westphal_bednar2005 (ASQ), Theory P6

**原文锚定**:
> "Though pluralistic ignorance has been observed in a variety of contexts, it may be particularly likely to occur among outside directors on corporate boards."
> "At the same time, the traditional board-room configuration results in a high level of mutual observability."

**关键特征**:
- 把机制的每个成立前提逐项映射到情境特征（风险前提→声誉约束与低凝聚力；发现前提→会外互动少；归因前提→会议室高可观察性），完成"一般构念→本情境必然发生"的焊接
- "On one level... In particular... At the same time..." 分层标记词让三条前提各自独立成拍，读者可逐项核对
- 结尾句回指前文已建立的归因机制（"the biased pattern of attributions noted above"），情境段不另起机制，只做接线
- 与一般"context applies theory"段落的区别：不是给情境贴标签，而是证明情境恰好满足了机制的全部前提——每一项前提缺失都会削弱结论

**适用**: 机制推演型论文在导入外来构念后、假设推导前的"情境适配段"；构念的成立前提可分解为 2-3 项可观察条件时

**禁忌**: 前提映射必须穷尽机制的关键前提，只映射有利项会被质疑选择性适配；回指句必须真实回指前文机制，不得在情境段偷偷引入新机制
