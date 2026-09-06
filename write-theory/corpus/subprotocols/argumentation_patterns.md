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




### Pattern: Dual-Regime Context Comparison with Suitability Bridge（双体制语境对照 + 情境适配桥，Fini 2017 型）

**模块**: Theory 内的语境建制段（Institutional Background 作为可选前置模块的功能化用法），位于 Gap 提问之后、机制推演之前。

**适用场景**: 研究问题依赖**两类评价/交易体制的可比性**时，在 Theory 内先做对称的制度刻画（谁授予、判据、流程、交付物、匿名性/前瞻性），再点出关键的交叉信息可得性特征，把情境特征显式桥接为研究问题的适配性声明。与 Background-as-Theory 双通道（kim_lee_2026：同向双 B0 通道 + 阶段/信息衰减、无编号假设）判别：本模式双体制**判据相反**（贡献知识 vs 服务 R&D 议程）、且桥接的是**信息跨受众可得**这一方法学前提而非机制衰减；与单纯 Institutional Background 段判别：本模式以适配桥收束，背景段落承担理论前提功能。

**骨架**:
```
[体制A刻画] [Resource A] is almost always provided in the form of [instrument A], awarded by [audience A] with the purpose of [cognitive goal]; [process features: no formal deliverables, flexible focus], because [system rationale] ([citation]).
[体制A评审安排] [Audience A] have delegated allocation to [process A]; [anonymity/identity feature] ([citation]).
[体制B刻画] Conversely, [Resource B] is commissioned by [user organizations] because they require [applied purpose rather than frontier knowledge]; [process features: specific deliverables, applied] ([citation]).
[体制B评审安排] [Process B] differs markedly: [evaluation by internal experts, forward-looking, non-anonymous]; the main criterion is [B's yardstick]. This differs from the yardstick applied to [A], which prioritises [A's yardstick].
[对称收束] Overall, [A and B] are awarded by two distinct audiences, each using their own process and criteria to [value the candidate].
[适配桥] Crucially, [key context feature: information on previous evaluations by one audience is available to the other]. This feature makes this empirical context suitable to address our research question.
```

**关键特征**:
- **逐维对称刻画**: 两体制按同一维度序列（授予者/目的/判据/流程/身份可得性）对照，而非各自成段孤立描述——可比性由结构保证
- **判据句对撞**: "This differs from the yardstick applied to [A], which prioritises..." 一句显式对撞两类判据，为后续"同一信号在两类受众下读法不同"埋设前提
- **适配桥收束**: 用 "Crucially, ... This feature makes this empirical context suitable to address our research question" 把背景段钉回研究问题，防止背景漂浮

**原文锚点** (Fini, Jourdan & Perkmann 2017, AMJ):
> "Crucially, information on previous evaluations made by one audience is likely to be available to the other audience for evaluation decisions. ... This feature makes this empirical context suitable to address our research question."

**注意事项**:
- 双体制刻画必须每一维都有文献/数据支撑，不得仅凭直觉对比
- 适配桥点出的情境特征必须正是机制（跨受众信息推理）赖以成立的特征，否则桥接失效
- 若两类体制判据并无实质差异，本模式退化为冗长背景

**反模式**: 把体制刻画写成文献综述（无判据对撞、无适配桥）；或在 Results 前才补体制差异说明。

<!-- wb:fini_jourdan_perkmann_2017_amj:dual_regime_context_comparison_suitability_bridge -->

<!-- wb:fini_2017_social_valuation_across_multiple_audiences_the_int:dual_regime_context_comparison_suitability_bridge -->


## Pattern: Prior-Limitation Departure Bridge（前作局限出发桥：静态→动态理论增益，DesJardine–Li–Shi 2025 型）

**适用场景**: 理论核心建立在作者（或邻近团队）的一篇具体前作之上，且前作的"局限"被显式命名为本文理论的出发点——不绕开前作，而是"承接种性 + 修复静态性"：指出前作的静态/单次观与现象动态性之间的 misalignment，导出"潜在影响 + 触发窗口"的时序化理论，并为后续成对调节假设提供共同理论伞。

**微观动作序列**: 承认前作贡献（"Providing some evidence of this possibility, [prior study] found..."）→ 局限命名（"Yet, their study offers a notable limitation, which we use as a departure point to enrich a theory of..."）→ misalignment 论证（"this static view does not fully align with research showing that..."）→ 必要性声明（"For models of ... to be accurate, it is imperative to account for..."）→ 时序化重述（"our theory ... accounts for how shifts ... trigger ..."）

**范文来源**: DesJardine, Li & Shi (2025), *Academy of Management Journal*（自引 DesJardine, Shi & Cheng 2023 的静态观 → 触发窗口式信息竞争理论）

**原文锚点**:
> "Yet, their study offers a notable limitation, which we use as a departure point to enrich a theory of information-based competition."
>
> "By not examining the changes in competitive dynamics that firms are so frequently subjected to, DesJardine, Shi, and Cheng (2023) offered a static view of information-based competition. However, this static view does not fully align with research showing that competitive threats and opportunities regularly evolve in ways that shape an actor's motivation and capability to initiate competitive moves."

**骨架**:
```
[承接] Providing some evidence of this possibility, [prior study] found that [prior finding] ([self-citation]).

[局限命名] Yet, their study offers a notable limitation, which we use as a departure point to enrich a theory of [focal phenomenon].

[misalignment] By not examining [the dynamic aspect] that [actors] are so frequently subjected to, [prior study] offered a static view of [the phenomenon]. However, this static view does not fully align with research showing that [threats and opportunities] regularly evolve in ways that shape [an actor's motivation and capability] to act ([citation]).

[必要性声明] For models of [the phenomenon] to be accurate, it is imperative to account for [its temporal nature].

[时序化重述] Thus, our theory of [the phenomenon] accounts for how shifts in [the landscape] ([via threats or opportunities]) trigger [actors] to exert [their latent influence].

[伞式下传] 该触发逻辑为后续成对调节假设提供共同伞：[threat → motivation] 与 [opportunity → ability] 各自落到一条 moderator 轴上（可与 willing-and-able 双轴框架衔接）。
```

**为什么有效**:
- **局限即出发点**：把前作局限显式命名为 "departure point"，既化解"自我重复"质疑，又把前作从竞争文献变成承重结构——静态→动态的升级路径一眼可见
- **misalignment 句式**："static view does not fully align with research showing..."——用文献共识界定前作的适用域缺口，而非指责前作错误；对自引前作口吻可以直接，对他人前作需更中立
- **潜在影响 + 触发窗口**：把"是否有影响"改写为"何时行使影响"——主效应保持不变，而全部调节假设获得统一理论根（不再是并列附录）；回答"为什么现在需要调节"而非"又多了一个调节"
- **与 willing_able_dual_axis 的分工**：桥给出"为什么需要调节"（现象的时序性）；双轴框架给出"调节怎么选轴"（威胁→动机 / 机会→能力）

**反模式**: 局限写成泛泛的 "more research is needed"（无具体 misalignment 内容）；修复后触发逻辑没有下传到 moderator 选取（桥与调节假设脱钩）；对非自引前作用"notable limitation"式直白口吻（他人前作局限需文献共识背书）。

<!--
pattern_id: prior_limitation_departure_bridge
build_type: 机制推演型（论证组织）
source_papers: ["desjardine_li_shi_2025_amj"]
confidence: high
status: EMERGING — 单篇来源；wb 批次 E
-->

<!-- wb:desjardine_2025_information_based_competition_the_case_of_ri:prior_limitation_departure_bridge -->



### 变体 E：共享盲区批判开场（Gulati_1998 综述文型）

**模板**:
> [让步开场] Prior research on [领域] has led to valuable insights on [它做对了什么].
> [共享倾向清点] [N] related themes run across these prior efforts. First, [共享倾向1：分析单位选择]. A second and related theme has been [共享倾向2：语境被非社会化处理]. Finally, [共享倾向3：因子集截断——focused primarily on [A侧] and not on [B侧]].
> [盲区命名] The focus on [倾向1] and [倾向2] has typically assumed [共享的隐含假设]. Viewed from this standpoint, much of the research on [领域] represents an [现成标签] account of [行动者] behavior.
> [空间转化] In recent years there has been a growing interest in [被忽略的语境]... my focus in this paper will be on [透镜的一个切面]——完成边界划定。

**来源**: Gulati_1998_SMJ, Theory P1-P5（"A Brief Critique of Prior Research on Alliances"）

**原文锚点**:
> "Three related themes run across these prior efforts." ... "Viewed from this standpoint, much of the research on strategic alliances represents an undersocialized account of firm behavior."

**关键特征**:
- 批判对象不是单项研究而是跨文献的共享假设，三条倾向逐条举证（每条后跟 exemplar 引文）后一次性收束命名
- 命名借用透镜文献的现成标签（undersocialized，出自 Granovetter 传统）——外部权威替代自创术语，批判自带理论合法性
- 批判段先于透镜出场：读者先感到缺口再见到工具，视角引入获得结构性空间
- 倾向3 的句式是"聚焦了 A 侧而非 B 侧"（competence side vs opportunity side），比"没研究 X"更精确地指认盲区形状
**适用**: 综述文/视角文的_critique_and_lens_前置段；为引入与在位文献不同范式的新视角造空间
**禁忌**: 三条倾向必须真是"跨文献共享"（各有多个文献家族佐证），不得为凑三而拆分单一文献的缺陷；现成标签必须真出自透镜文献，不得自造标签冒充

<!-- wb:gulati_1998_alliances_and_networks:review_essay_blind_spot_critique_opener -->


### 变体 F：透镜-议程六拍循环（Gulati_1998 综述文型）

**模板**:
> [路标句] The section is organized around the [N] key questions... For each question, I first discuss [在位层次上的既有研究], followed by an examination of how introducing a [透镜] perspective opens up an additional set of issues.
> [议题循环 × N，每循环六拍]
> 拍1 已知盘点：[按理论家族组织的既有研究走到哪里]
> 拍2 内在盲区：[点破共享隐含假设——"Implicit in such accounts is the assumption that..." / "An important shortcoming... has been their implicit treatment of..."]
> 拍3 情境激活：[透镜变得切题的具体处境——机会主义、appropriation、协调成本]
> 拍4 视角重析+证据：[透镜重解该议题；prior studies + own studies + 田野引语三班证据]
> 拍5 互补整合：[新解释不推翻旧解释——必要不充分式收束]
> 拍6 开放议程：["has yet to be examined" / "remains an open question" / "Two natural extensions..."]

**来源**: Gulati_1998_SMJ, Theory P39-P157（"Key Issues in Alliances" 五议题：形成/治理/演化/联盟绩效/企业绩效）

**原文锚点**:
> "For each question, I first discuss some of the current research and debates at the firm and dyadic levels, followed by an examination of how introducing a social network perspective opens up an additional set of issues that can be considered."

**关键特征**:
- 把抽象视角转成可操作研究议程的机制 = 固定六拍循环：每次先付"已知"的诚意，再点破隐含假设制造缺口，用透镜填补，最后把"视角暗示但没人做过"的问题显式列表
- 路标句提前宣布节奏，N 次循环形成阅读预期，每次只需增量理解
- 拍2 的盲区句式有固定语法：implicit treatment / implicit assumption——指认"假设"而非"错误"，为拍5 互补整合留后路
- 拍6 的开放问题都带具体扩展方向（换网络类型/换层次/加时间维度），不是泛泛的"未来可研究"
**适用**: 综述文/视角文主体架构；领域有多个成熟子议题且每个都能被同一透镜重析时
**禁忌**: 议题间必须有真差异（不同因变量/层次），否则循环沦为重复；拍1 综述必须 generous（对手最强形式），稻草人式盘点会被审稿人反噬；五循环中拍5 句式需措辞换装，防公式化

<!-- wb:gulati_1998_alliances_and_networks:lens_agenda_six_beat_cycle -->


### 变体 G：前提分解→瓶颈命名 setup（Gulati_1999 型）

<!--
pattern_id: precondition_decomposition_hurdle_setup
build_type: 跨类型（机制 setup 微动作；T3 开篇、主效应假设前置）
source_papers: ["gulati_1999_network_location_and_learning_the_influence_of_n"]
verification_status: VERIFIED — expert_audit_override (user 2026-09-05: 用户点名 Gulati 为最喜爱学者之一，其论文蒸馏单源即 VERIFIED)
-->

**适用场景**: 主效应假设的 IV 是某种"降低门槛的资源/能力"时，在机制推演开篇先分解行为发生的**双边前提**（双方各自需要什么信息/资源），再把瓶颈统一命名为一个 hurdle 构念——使 IV（恰好降低该瓶颈者）与 DV 的联系变成分析必然而非断言。

**微观动作序列**: 双边前提列举（first/second + Simultaneously 对方侧）→ 风险具体化（moral hazard 的失败模式）→ 瓶颈命名（"All these conditions create a significant [X] hurdle"）→ IV 引入（access to [IV] can lower [hurdle]）。

**骨架**:
```
[双边前提] For [actors] to [focal behavior] that [meets needs] while minimizing [risk], they must first [precondition 1] and, second, [precondition 2] ([citation]). Simultaneously, [counterparty] must also have [mirror precondition on the focal actor].
[风险具体化] [Actors] face considerable [risk type] concerns because of [sources of unpredictability]... A [counterparty] may either [failure mode 1: free-ride] or simply [failure mode 2: opportunism]. Such concerns are further compounded by [aggravator].
[瓶颈命名] All these conditions create a significant [named hurdle] for [the behavior].
[IV 引入] Given the [uncertainty], access to [IV resource] can lower [search costs] and alleviate some of the [risks], making [actors] more likely to [behavior].
```

**为什么有效**: 前提分解把行为发生写成清单（哪一方缺什么都不行），瓶颈命名把清单压缩成一个可命名的构念，IV 随即以"瓶颈解除者"身份出场——why chain 的第一步不再需要断言，IV 与 DV 的关系已由前提结构注定；对方侧镜像前提（"Simultaneously, those potential partners must also…"）还预先覆盖了"被选中方"的机制方向。

**注意事项**: 前提必须真是双边/多维（单侧前提直接单步机制即可）；瓶颈命名构念应与 IV 的理论属性同纲（信息瓶颈↔信息资源；成本瓶颈↔成本优势）；风险具体化要给出失败模式，不能只说 risky。

**反模式**: 前提清单与 IV 属性不同纲（成本瓶颈用信息资源解除）；命名后弃用（后续机制不回扣 hurdle）。

**原文锚点** (Gulati 1999, SMJ):
> "For firms to build alliances that effectively address their needs while minimizing the risks posed by moral hazard concerns, they must first be aware of the existence of potential partners and have an idea of their needs and requirements and, second, have information about the reliability of those partners."

**原文锚点**（瓶颈命名句）:
> "All these conditions create a significant informational hurdle for the creation of alliances."

<!-- wb:gulati_1999_network_location_and_learning_the_influence_of_n:precondition_decomposition_hurdle_setup -->


### 变体 H：单透镜双极镜像机制链（One-Lens Bipolar Mirror Chains，Gulati_Westphal_1999 型）

<!--
pattern_id: one_lens_bipolar_mirror_chains
build_type: 机制推演型（两极反向主效应）
source_papers: ["gulati_westphal_1999_cooperative_or_controlling (ASQ)"]
confidence: high
status: VERIFIED — expert_audit_override (Gulati/Westphal 系单源裁定 2026-09-06, paper_count=1)
-->

**适用场景**: 核心前因有两个相反极（如控制型 vs 合作型关系内容），两极各自推导反向 DV 效应，且同一理论透镜可以双向运行时。
**结构**: 极 A 小节：透镜 L → [极 A 构型] → [机制 M−] → [DV 反向]；极 B 小节：显式复用 L → [极 B 构型] → [机制 M+] → [DV 正向]；镜像句收束对称性

**骨架**:
```
[极 A 小节] Applying [lens L] to [context], we expect that [极 A configuration]
→ [M−: 分化/消耗型中介] → [DV 反向].

[极 B 小节]
[透镜复用句] The connection between [极 B] and [中介] can also be understood
by considering [同一透镜 L 的证据].
[镜像句] In effect, just as [M−] is a basic and powerful human response,
[极 B] can engender [M+], leading to [DV 正向].
```

**为什么有效**: 第二极不重新进口理论，只"换向运行"第一极的透镜——理论装置减半、两极对称性本身成为论证（读者用第一极的认知惯性理解第二极）；镜像句 "just as..., ... can engender..." 把对称性明示为理论主张而非巧合。
**注意事项**: 前提是透镜 L 真能双向运行（L 对两极给出对称机制，而非只解释一极）；第二极仍需补足 L 之外的新步骤（本文极 B 补 Simmel 互动-信任步）；两极的中介要同构（同一信任构念反向）才能镜像。
**反模式**: 两极各找一个不同理论硬凑（透镜拼贴，对称性消失）；把镜像句写成机械对仗但机制不同构。
**与近亲变体的区分**: "镜像配对比较假设组（Pfarrer 2010 型）"镜像的是假设陈述组（构念辨析后的成对 H），本变体镜像的是机制推导链（透镜复用发生在论证层，假设仍逐条独立陈述）；"同果近邻构念反号辨析（westphal_bednar2005 型）"辨析的是两个构念+同一调节变量反号，本变体是同一构念的内容两极+同一透镜换向。
**原文锚点**:
> "The connection between cooperative interactions in CEO-board relationships and the extent of trust between managers can also be understood by considering some of the evidence from research on intergroup relations." / "In effect, just as negative affect and distrust toward an independent, controlling group is a basic and powerful human response, cooperation between group members can engender in-group biases that lead to positive affect."


<!-- wb:gulati_westphal_1999_cooperative_or_controlling:argumentation_one_lens_bipolar_mirror_chains -->


### 变体 I：默认透镜资格审查-更替（Lens Scope Disqualification & Replacement，Gulati_Westphal_1999 型）

<!--
pattern_id: lens_scope_disqualification_replacement
build_type: 机制推演型 / 调节效应型（moderator 透镜选择段）
source_papers: ["gulati_westphal_1999_cooperative_or_controlling (ASQ)"]
confidence: high
status: VERIFIED — expert_audit_override (Gulati/Westphal 系单源裁定 2026-09-06, paper_count=1)
-->

**适用场景**: 为边界/调节机制选择理论透镜时，读者对"默认透镜应当如何预测"有强先见（如第三方关系→声誉强制→更多信任），而 focal 情境恰好不满足默认透镜的范围前提。
**微观动作序列**: 默认预测 → 前提显性化 → 情境失配 → 失效结论 → "more germane perspective" 更替 → 新透镜机制

**骨架**:
```
[默认预测] It is typically supposed that [默认透镜] will [预测 X]
by [默认机制] ([citations]).
[前提显性化] The claim that [默认机制] assumes that [范围前提 P].
[情境失配] In [focal context], however, [P 不成立/规范模糊],
because [情境条件]. Accordingly, [默认透镜] may not necessarily
[预测 X] in this setting.
[更替] While traditional perspectives on [X] may not apply to [context],
recent research suggests a more germane perspective: [新透镜] ([citations]).
[新机制] [新透镜] proposes [机制 M]，据此推出调节预测.
```

**为什么有效**: 先把默认透镜的隐含范围前提拎出来逐一对照情境，失效是"论证出来"的而非宣布的——透镜更替显得是情境逼出来的必然选择，预先解除审稿人"标准理论明明说…"的质疑。
**注意事项**: 前提 P 必须是默认透镜自身的核心假设（可引原文），不能偷换成稻草人；失配论证要有情境证据（本文引规范模糊 + 董事选任实证证据）；更替透镜需能覆盖默认透镜解释不了的那部分变异。
**反模式**: 不给默认透镜出场机会直接换透镜；或失配论证只靠 "however" 无前提对照。
**与近亲变体的区分**: "Preemptive Competing Account Management"管理的是竞争预测（预测层，用拒绝或 moderator 裁决收场）；"Neglected Lens via Dominant-View Contrast"是 T2 开场的视角选择（两条透镜共存）；本变体在调节段对单一默认透镜做范围前提审查后更替（透镜层、前提失效驱动），三者层次不同。
**原文锚点**:
> "The claim that third-party ties enforce cooperation through reputational effects assumes that noncooperative behavior is illegitimate or non-normative." / "While traditional perspectives on indirect network ties may not apply to board interlocks, recent research on the effects of third-party ties suggests a more germane perspective."


<!-- wb:gulati_westphal_1999_cooperative_or_controlling:argumentation_lens_scope_disqualification_replacement -->


### 变体 J：增长谜题→双问句架构预告（Growth-Puzzle Double-Question Forecast，Gulati_1999_AJS 型）

<!--
pattern_id: growth_puzzle_double_question_forecast
build_type: 跨类型（理论章开场宏观架构动作）
source_papers: ["gulati_1999_where_do_interorganizational_networks (AJS)"]
verification_status: VERIFIED — expert_audit_override (Gulati 系单源裁定 2026-09-06, paper_count=1)
story_fidelity: section_variant
-->

**适用场景**: 理论章开场（现象定义与风险铺垫之后、任何假设之前），用"反常增长"制造谜题，再以两个问句分别预告论文的两大部分——机制问题与后果/动态问题。

**骨架**:
```
[现象与障碍] [现象] 的爆发式增长发生在 [显著障碍/风险] 之下……
[障碍命名] The paucity of [关键要素] create a significant [hurdle] for [actors] that consider [行为].（可复用变体 G 的瓶颈命名句）
[谜题句] Yet, the explosive growth of [现象] suggests that [actors] are able to overcome such hurdles.
[双问句预告] How do they do it? And what consequences does their behavior have for [更大的系统/context]?
```

**为什么有效**: 双问句是全文架构合同：第一问由形成理论回答（机制），第二问由动态理论回答（行动对结构的反馈）——读者在读到任何假设前已持有两大部分的分工地图；谜题句把"障碍与增长并存"的反常转成求知张力，比直线式 gap 陈述推进力更强；第二问（后果）为论文后半的动态/反馈理论拿到入场券，静态机制论文常缺这一问。

**注意事项**: 两问必须真的对应后文两大部分且顺序一致；第二问不可省略——它把理论从静态推向动态；障碍命名与变体 G 同源时可只用其命名句，落点仍是问句而非 IV 引入。

**反模式**: 问句只装饰不兑现（后文无对应部分）；只问机制不问后果（理论停在静态）；问句前无反常铺垫（谜题感不足）。

**与近亲变体的区分**: 变体 G（前提分解→瓶颈命名）是 T3 机制 setup 微动作，落点=IV 以瓶颈解除者身份出场；句式 B（How then might...）是单段推导起点的机制枢纽问句；本变体是理论章宏观架构动作，落点=双问句合同，瓶颈命名可作其内部垫段。

**原文锚点** (Gulati 1999, AJS):
> "Yet, the explosive growth of strategic alliances suggests that organizations are able to overcome such hurdles and enter alliances. How do they do it? And what consequences does their behavior have for the social context in which new strategic alliances take place?"

<!-- wb:gulati_1999_where_do_interorganizational_networks:c3_growth_puzzle_double_question_forecast -->

### 模式 G：现象先行定位模块（Research-Setting Staging before Constructs）

<!-- pattern_id: setting_first_materiality_staging; build_type: 跨类型; source_papers: ["Pfarrer_Pollock_Rindova_2010_AMJ"]; confidence: medium -->

**适用场景**: 结果域（DV 现象）本身需要论证"为什么值得理论化"（反常、有后果梯度、触发理论机制）时，在构念定义前安排一个研究情境模块为结果域设 stakes。
**句位/位置**: Theory 开篇、T1 之前的前置模块
**范文来源**: Pfarrer, Pollock, and Rindova (2010), AMJ

**骨架**:
```
[常态锚定] [Outcome] is the norm: actors strive to avoid [outcome] because [why the
norm matters for market/field efficiency] ([citations]).

[反常引入] Yet [outcomes] do happen. They occur for [reasons: actor actions and events
beyond control], e.g., [1-2 vivid instances].

[梯度界定] [Outcomes] also differ in the extent to which they [deviate/vary]. Larger
deviations—[operational threshold class]—are considered "[term]" and are more
consequential for both [actors] ([citations]). [Term] [outcomes], given their rarer
occurrence and greater salience, therefore have greater potential to [engage the
theorized mechanism].

[过渡桥接] In the next section we discuss [how the focal constructs arise] in order to
develop the theoretical foundation for our hypotheses predicting their effects on
[outcome domains].
```

**为什么有效**: 把 DV 的理论重要性（反常性、后果梯度、机制触发潜力）在 X 出场前建立，后续"构念→行为倾向"假设的意义空间先被撑开；过渡句显式宣告 setting→构念→假设的分工，避免读者把情境段当文献综述。
**注意事项**: 情境段必须落在"为什么该结果域对理论机制重要"，不是行业背景科普；梯度界定段（何为 material）同时为实证操作化铺垫。
**反模式**: 情境段写成现象描述堆砌（只列举发生原因的例子），不回收"这为何激发本文的理论机制"。
**原文锚点** (Pfarrer et al. 2010, AMJ):
> "Material earnings surprises, given their rarer occurrence and greater salience, therefore have greater potential than smaller surprises to engage investors in active sensemaking and reevaluation of a firm." ... "In the next section we discuss how reputation and celebrity are gained in order to develop the theoretical foundation for our hypotheses predicting their effects on firms' propensities to announce surprises and on investors' reactions to these surprises."

<!-- wb:pfarrer_pollock_and_rindova_2010:setting_first_materiality_staging -->
<!--
pattern_id: transfer_plus_sorting_dual_warrant_signal
build_type: 机制推演型（信号/背书/声望类假设通用）
source_papers: ["higgins_2003_getting_off_to_a_good_start_the_effects_of_uppe"]
confidence: VERIFIED — expert_audit_override（user 2026-09-06：Pollock/Westphal/Gulati 系单源即 VERIFIED）
-->

### 变体 K：传递 + 自选择双 warrant 信号推演（Transfer + Sorting Dual-Warrant Signal Derivation）

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


### 变体 L：轻攻门域循环·透镜横切框架复用型（gulati_nohria_zaheer_2000 综述文型）

> 论证角色：Framing（以"基线域→透镜精化→框架电池复用→例证→互补收束"的域循环，把一个透镜横切到 N 个既有理论域并跨层复用同一分析框架）

**模板**:
> [域循环 × N，每循环五拍]
> 拍1 基线礼让：The [X] school, which has had a major impact on [field], began with [baseline model] and argued that [baseline claim] ([citation]).
> 拍2 精化提案：We propose that a consideration of [lens] allows a more refined understanding of [domain]—since [participants] can be seen as embedded in [lens flows].
> 拍3 框架电池复用：we consider [N] types of [frame characteristics]: [A]... [B]... [C]...；跨层复用声明：this time at the level of [level], we can use the same conceptual frame as we have above—in terms of [A], [B], and [C].
> 拍4 机制例证：[Frame dimension] can affect [outcome]. For instance, [mechanism] ([citation]). Research by [authors] shows how [finding]. Similarly, research by [authors] illustrates how [finding].
> 拍5 互补三步收束：Overall, using [lens concepts] in this manner provides a valuable complement to explanations that simply focus on [baseline factors]. They expand... Furthermore, [lens] extends the underlying mechanisms beyond conventional notions of [baseline mechanism].

**来源**: Gulati, Nohria & Zaheer 2000 (SMJ), Theory 五节循环（Industry Structure / Intra-Industry / Inimitable Resources / Contracting Costs / Network Dynamics）

**原文锚定**:
> "We propose that a consideration of strategic networks allows a more refined understanding of industry structure—since industry participants can be seen as embedded in networks of resources, information, and other flows."

**关键特征**:
- 轻攻门：域内不点破共享隐含假设（无 Gulati_1998 变体 F 六拍的"内在盲区/情境激活"拍），基线回顾以"精化提案"一句直转——适用于透镜合法性已由引言建立、正文只需展示横切收益的综述
- 同一分析框架一次定义、跨层显式复用（industry→firm："this time at the level of the firm, we can use the same conceptual frame as we have above"）——框架即综述的章法骨架
- 每域以互补三步收束（complement→expand→extend mechanisms），不推翻基线、不产开放议程（区别于变体 F 的拍5 互补整合+拍6 开放议程）
- 例证链节奏：机制主张→For instance 机制例→"Research by X shows / Similarly, research by Y illustrates"双实证例证锚定
- 例示性免责：机制对命名后接 "intended to be illustrative rather than comprehensive"，预防清单式综述批评

**适用**: 综述文/概念界定文把一个透镜横切到 N≥3 个既有理论域、透镜合法性已在引言建立的正文组织。与同文件变体 F（Gulati_1998 透镜-议程六拍循环）的区别：变体 F 每议题先付"已知诚意"再点破隐含假设并以开放议程收尾；本变体跳过盲区/议程拍，以"精化提案+框架复用+互补收束"的更轻循环重复 N 次，并新增跨层框架复用声明。

**禁忌**: 各域必须真的复用同一框架（至少一个维度跨域/跨层回用），否则域循环退化为五个独立小综述；透镜合法性未建立时先补盲区拍（用变体 F）；域收束对象必须具体（baseline factors/mechanism 点名），空转即废话骨架。

**风格画像来源**: gulati_nohria_zaheer_2000 (SMJ)

<!-- wb:gulati_nohria_zaheer_2000_strategic_networks:domain_loop_lens_frame_reuse -->


### 变体 M：部落冲突归因诊断段（gulati_2007_tent_poles 型）

> 论证角色：Reason（两层归因：启发式标签→(1)部落间冲突+(2)部落内范式战→结构双重身份根源，为消解立场供社会机制）

**模板**:
> "It is unfortunate how easily [field members] label each others' [research enterprises], often with little evidence. Sometimes [members] define [value A] as use of [the narrow paradigm of theories, methods, and analyses they themselves would use]. I argue that the use of [simple heuristics and stereotypes] to define [value A] has resulted in (1) [a broad conflict between field tribes labeled by the opposed values] and (2) [subtribe paradigm clashes within these groups] based on [members'] identifying with [specific paradigmatic commitments], which in turn [discourages boundary-crossing work]. At the roots of these [identity clashes] is an inherent duality in [field members]: most of us are [professional identity X] employed by [professional institutions Y]. [Institutional history] then hardened this duality into [tribal boundaries], and [covert arbiters] conferring [badges of honor or shame] on work regardless of its impact [mask tribal behavior as impartiality]."

**来源**: gulati_2007_tent_poles (AMJ), Causes of Tribalism P1-P5

**原文锚定**:
> "I argue that the use of simple heuristics and stereotypes to define rigor has resulted in (1) a broad conflict between management researcher tribes labeled as rigorous and relevant and (2) subtribe paradigm clashes within these two groups, particularly in the rigor camp"

**关键特征**:
- 两层效应编号归因（(1) 部落间 + (2) 部落内），一句 "I argue that..." 同时完成立场布防与机制清单——产出的是可核查的社会机制主张，不是纯断言
- 归因下探结构性根源（科学家受雇于专业学院的双重身份）+ 制度史（1960s 学科化进位）——把"谁、经什么机制建构了对立"落实为可指认的主体与历史
- 第三拍隐蔽仲裁者机制（badge of honor or shame、"masked as impartiality"）预防"评审中立"反驳，把冲突从观点分歧改写为守门行为
- 与实证文的假设推导相反：本段的"预测"是社会机制命题，证据地位是修辞-历史的（评论体立场布防签名动作）

**适用**: 评论/论坛体理论文对领域级对立（rigor-relevance、quant-qual、micro-macro）做归因诊断；Incommensurability x Mode/Question 中"对立由谁建构"的正文兑现段；需要立场宣告但不流于断言的场景

**禁忌**: 编号机制主张必须每层可核查（有历史事件或可点名观察者支撑），否则退化为立场断言；守门人类机制点名时避免滑向阴谋论修辞（原文 "invisible politburo" 为风格签名，慎仿）；实证假设论文勿用——无此论证任务

<!-- wb:gulati_2007_tent_poles:tribalism_cause_diagnosis -->


### 变体 N：开山者典范反讽论证段（gulati_2007_tent_poles 型）

> 论证角色：Evidence（三学科开山者实践-理论键合实例链，以反讽句起、以"失落根源"反转句收，为消解立场供历史证据）

**模板**:
> "Perhaps the greatest irony of [the field's multidimensional conflicts] is that the [founders and schools of thought] providing the foundations of [the field] represent strong bonds between [value A] and [value B], between [theory] and [application]. Take the [value-A] side of the equation. In [discipline 1], [founder] [direct practice engagement], all of which [shaped his writings], which, in turn, [shaped public practice]. [Discipline 2] founders are also well represented among [theorist-practitioners]... Among [discipline 3 forefathers] the story is the same... So it would be safe to suggest that [those who take the either/or approach] have lost touch with their roots... [The founders] seemed to have no trouble crossing this divide to see themselves as both."

**来源**: gulati_2007_tent_poles (AMJ), Historical Exemplars of Rigor and Relevance in the Social Sciences P1-P4

**原文锚定**:
> "Perhaps the greatest irony of these multidimensional tribal wars is that the theorists and schools of thought providing the foundations of modern management research represent strong bonds between rigor and relevance, between theory and application."

**关键特征**:
- 反讽总起（"Perhaps the greatest irony..."）：把对立营垒自称继承的学科开山者征用为本方证据——史实选择即论证
- 三学科 × 每人一句"实践介入→反哺理论→影响公共实践"的微缩链；人名密度高但句式严格复用（parallel exemplar roster），阅读负荷被节奏抵消
- 收束两拍：反转结论（"lost touch with their roots"——营垒立场与学科根源相悖）+ 身份诊断（开山者"see themselves as both"，对立是当代身份建构而非学科宿命）
- 评论体特有"以史为证"：不用数据用谱系，为 Mode/Question 型贡献供正当性；本篇还引 Roethlisberger 自传作单点深化，防名单 flat

**适用**: 评论/概念文为"对立是建构而非本质"类主张供历史证据；领域有公认开山者谱系且其实践介入可核查时；需要把身份诊断锚进学科史的场景

**禁忌**: 典范选择必须可核查——全 favorable-case 选样在实证场域会被攻破（本篇为评论体豁免，模仿时注意体裁前提）；每人"实践介入→理论反哺"方向必须真实，不得把轶事拔高为因果；不用于假设推导文——证据地位是修辞性的，不承担 H 式承重

<!-- wb:gulati_2007_tent_poles:founder_exemplar_irony_reversal -->


### 变体 O：大帐篷正和重构+编号规范程序段（gulati_2007_tent_poles 型）

> 论证角色：Warrant（把消解命题兑现为可执行规范程序：正和重构+隐喻包+编号步骤链，每步配典范引证与限定）

**模板**:
> "The more challenging question, then, is whether [the field] can [emerge from under small, private umbrellas to erect tall and thick poles to prop up a big tent shielding it from the charges of poor A, low B, and X deficits]. This will mean [existing in a new domain] that replaces '[either-or]' with '[and]'. The solution... is to accept that [value A] and [value B] are not opposites after all... If we can view [A and B] as [outcomes to be simultaneously maximized], we can pursue true synergy. Let me offer several [normative suggestions]... In the aggregate, [they] are a multistep process for [performing the conjunctive work]. (I present discrete steps, but it is important to note that one doesn't have to follow them in this sequence.) [Step N, imperative]: [action]. [Exemplar anecdote or citation]. [Qualification/boundary]."

**来源**: gulati_2007_tent_poles (AMJ), Bridging Rigor and Relevance: A Big Tent View + Steps in an Integrative Process

**原文锚定**:
> "The solution, as I suggest below, is to accept that rigor and relevance are not opposites after all." ... "(I present discrete steps, but it is important to note that one doesn't have to follow them in this sequence.)"

**关键特征**:
- 消解命题→可执行程序的兑现拍：先宣言 "not opposites after all" + 正和重构（outcomes to be simultaneously maximized），再隐喻包（umbrella/big tent）给纲领命名——贡献即收束（T6 closure-as-contribution）
- 编号祈使句步骤链，每步三拍：祈使动作→典范引证（Ghoshal "sizzle"、Siggelkow "talking pigs"、Doz 合作轶事）→限定语（"Discovery is interactive" / "need not go so far"）
- 显式非顺序免责（"doesn't have to follow them in this sequence"）+ 适用范围免责（"regardless of the publishing outlets"）——防清单式规范被读成线性阶段模型
- 步骤自带升级梯度（bilingual translators→co-create 知识共创），收束借对立营垒引语（Weick：practitioners 亦须担责）完成双边化，预防单向归责

**适用**: Incommensurability x Mode 评论/概念文的贡献兑现段——把"对立消解"落为研究实践规范模型；以编号程序组织建议时；正文收束=贡献本身的场景

**禁忌**: 编号步骤必须每步配引证或轶事，裸祈使句清单即废话骨架；非顺序免责不可省（否则暴露无过渡条件、被读作伪过程模型）；实证假设文勿用——此为 Mode 型贡献专用组织，不产生可检验预测

<!-- wb:gulati_2007_tent_poles:normative_conjunctive_program -->

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
