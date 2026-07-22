# Bilateral Argumentation Templates

本文件收集调节效应/边界条件假设中同时论证 high-condition 和 low-condition 的句法模板。

---

<!--
pattern_id: social_identity_boundary_condition
build_type: 调节效应型 / 机制推演型
source_papers: ["Keeves_2017_AMJ"]
confidence: high
status: ready_for_corpus
-->

## Pattern: Group Identity as Boundary Condition

**适用场景**: moderator 涉及社会类别（race/gender/status），需要用社会心理学理论解释为什么边界条件改变机制强度。
**微观动作序列**: Theory anchor（self-categorization / intergroup bias）→ Mechanism（out-group target 被视为 less deserving）→ Other-path amplification → Prediction
**范文来源**: Keeves, Westphal & McDonald (2017), *Academy of Management Journal*（white male managers observing ingratiation toward minority/female CEOs）

**骨架**:
```
[Theory] Social psychological research on self-categorization indicates that people classify each other into social categories automatically ([citation]). Because categories that include the self tend to be held in positive regard, social categorization fosters [bias], a systematic tendency to evaluate [in-group] more positively than [out-group] ([citations]).

[Mechanism] One manifestation of [bias] is [specific stereotype]. Thus [bias] may cause [actor] to perceive a given level of [behavioral component] that affirms [target]'s status as relatively undeserved when [target] is [out-group characteristic]. Accordingly, [IV] toward [target with out-group characteristic] is especially likely to elicit [mediator].

[Other-path] There is also reason to believe that [bias] should increase [actor]'s [mediator] toward [target with out-group characteristic] for the [behavioral components] [target] receives from others. [Theoretical justification].
[Prediction] Thus we hypothesize:
H[X]: The relationship between [IV] and [mediator] will be more positive when [actor] is [in-group] and [target] is [out-group].
```

**为什么有效**: 将社会心理学理论嵌入机制推演，使调节变量不是事后添加；同时覆盖 self-path 和 other-path。
**注意事项**:
- 必须解释为什么 out-group 目标会改变机制强度
- 需明确 in-group / out-group 的理论定义，而非简单 demographic 分组
- 建议同时论证 self-path 和 other-path（如适用）

**反模式**: 只说"歧视会增强效应"而不解释具体心理机制；用 demographic 分组替代理论定义。

---

<!--
pattern_id: benchmark_leader_vs_similar_peer
build_type: 机制推演型 / 边界条件型
source_papers: ["Shi_Grewal_Sridhar_2021_JMR"]
confidence: medium
status: ready_for_corpus
-->

## Pattern: Benchmark Leaders vs. Similar Peers as Information Sources

**适用场景**: 同一 peer 行为可由不同类型 peer 引发，需预测哪类信息源占主导。
**微观动作序列**: Ability condition anchor（agents learn from peers）→ Benchmark leaders path（knowledge advantage）→ Similar peers path（relevance + investor expectations）→ Prediction
**范文来源**: Shi, Grewal & Sridhar (2021), *Journal of Marketing Research*（advertising spending disclosure herding: similar peers dominate）

**骨架**:
```
[Ability condition anchor] Rational agents update beliefs using information from peers. We identify two plausible sources: [benchmark leaders] and [similar peers].

[Benchmark leaders path] Leaders occupy superior positions in [market], so their [behaviors] signal valuable knowledge about [outcome] ([citation]). In addition, [peers leading in another market] are probably perceived as knowledgeable with regard to how [stakeholders] would respond to disclosed information.

[Similar peers path] For an agent, the level of similarity in terms of [key dimensions] varies across peers. [Example contrasting two peers with different similarity levels]. Agents may find it beneficial to learn from similar peers because similar peers occupy comparable positions on some important [market dimensions]. Specifically, an agent may perceive that the private information of similar peers is more relevant for its decisions than such information from disparate firms.

Furthermore, similar peers' [behaviors] are relevant in [market B] because comparison with similar firms can drive [stakeholder] expectations. When more similar firms [disclose], [stakeholders] are more likely to expect the focal agent to [disclose]; if the agent does not [disclose], [stakeholders] tend to revise [valuation] downward ([citation]). Recognizing [stakeholders]' reasoning processes, the agent should be more likely to follow the [behaviors] of similar peers to avoid a severe discount on its [valuation].

[Prediction] We predict [similar peers / benchmark leaders] will have a stronger influence because [theoretical rationale].
```

**为什么有效**: 将 peer type 从单纯控制变量提升为理论驱动的信息源比较。
**注意事项**:
- 必须同时论证两类 peer 的合理机制
- 预测需有明确的理论方向
- 必须解释为什么 chosen source 在本文情境下占主导

**反模式**: 只说"similar peers matter more"而不解释为什么 leaders 也可能重要。

---

<!--
pattern_id: competition_as_external_governance_remedy
build_type: 调节效应型 / 代理理论型
source_papers: ["Zhou_2017_ASQ"]
confidence: high
status: ready_for_corpus
-->

## Pattern: Boundary Condition as Remedy for Agency Inefficiency

**适用场景**: IV 通过双重代理问题降低资源转换效率；边界条件（竞争、新创身份、制度发展）通过外部治理/生存压力/目标清晰化削弱代理问题，从而缓解 IV 的负面调节。
**微观动作序列**: Baseline negative moderation（IV × input → output）→ Boundary variable → Mechanism（boundary reduces political interference / improves accountability）→ Prediction
**范文来源**: Zhou, Gao & Zhao (2017), *ASQ*（institutional development, industrial competition, start-up status weaken negative moderation of state ownership on R&D→innovation）

**骨架（竞争作为外部治理）**:
```
[Theory] [Theory] posits that aligning [actors] reduces [problem]. Among external controls, [contingency] is the most salient because it forces inefficient firms to exit. [Competition] creates clear performance benchmarks and increases manager termination risk; politicians must stop self-dealing or [focal actors] will fail.

[Mechanism] When [contingency] is high, [IV]'s negative effect on [input → output efficiency] is reduced because [mechanism 1: exit threat] and [mechanism 2: performance benchmarks].
H[X]: The moderating effect of [IV] on [mediator → outcome] is less negative when [contingency] is higher.
```

**骨架（新创企业身份）**:
```
[Actor type] are more innovative because they identify opportunities and respond promptly. When [government] sets up [actor type], they aim to [objective] and scrutinize them closely, reducing politician self-dealing. [Actor type] also bear fewer [legacy burdens] and can build flexible, performance-based structures.
H[X]: The moderating effect of [IV] on [mediator → outcome] is less negative for [actor type] than for [established actors].
```

**为什么有效**: 将边界条件定位为"补救机制"而非简单调节，使 H2-H4 与 H1b 形成理论对话。
**注意事项**:
- 边界条件必须与代理问题的具体机制对应
- 多个 boundary 条件需要说明它们分别作用于哪条机制
- 避免 boundary 条件成为数据驱动的稳健性检验

**反模式**: 边界条件只是"又一个调节变量"，没有说明如何"修复"代理问题。

---

<!-- 
pattern_id: bilateral_high_low_three_mechanisms
build_type: 调节效应型 / 机制推演型
source_papers: ["Shen_Zhou_Wang_Zhang_2022_JOM"]
confidence: medium
status: ready_for_corpus
-->

## Pattern: Bilateral Argumentation — High/Low Conditions Across Three Mechanisms

**适用场景**: 当 moderator 影响主效应的三个并行机制时，分别论证 high 和 low 条件下每个机制如何变化。
**范文来源**: Shen, Zhou, Wang, and Zhang (2022), *Journal of Operations Management*

**骨架**:
```
We predict that [W] [weakens/strengthens] the negative impact of [IV] on [DV].

First, when [W] is high, [mechanism 1] is [weakened/strengthened] because ...
However, when [W] is low, [mechanism 1] is [strengthened/weakened] because ...

Second, when [W] is high, [mechanism 2] is [weakened/strengthened] because ...
However, when [W] is low, [mechanism 2] is [strengthened/weakened] because ...

Third, when [W] is high, [mechanism 3] is [weakened/strengthened] because ...
However, when [W] is low, [mechanism 3] is [strengthened/weakened] because ...

Therefore, H[X]: The [direction] relationship between [IV] and [DV] is [weaker/stronger] when [W] is high rather than low.
```

**为什么有效**: 
- 每个机制都双边论证，避免只讲增强方向
- "When ... However, when ..." 的对称结构让逻辑清晰

**注意事项**: 
- low-condition 论证不能只是 "相反"，必须有独立的理论逻辑
- 三个机制的 high/low 论证可以合并为一个段落，也可以分开

**反模式**: 只说 "when W is high, effect is stronger" 而不解释 low-condition。

---

<!-- 
pattern_id: bilateral_with_boundary_condition
build_type: 调节效应型
source_papers: ["Shen_Zhou_Wang_Zhang_2022_JOM"]
confidence: medium
status: ready_for_corpus
-->

## Pattern: Bilateral Argumentation with Boundary Condition

**适用场景**: 当 moderator 的 high/low 条件对应不同的制度/市场环境时，把边界条件嵌入双边论证。
**范文来源**: Shen, Zhou, Wang, and Zhang (2022), *Journal of Operations Management*

**骨架**:
```
In [low-W context], firms rely heavily on [IV] for [resource], so [mechanism] is strong.
As a result, [IV] has a [strong negative/positive] effect on [DV].

In contrast, in [high-W context], [IV] becomes less important because [alternative resource channel].
Firms therefore shift attention to [action], reducing [mechanism].
As a result, [IV] has a [weaker negative/positive] effect on [DV].

Therefore, H[X]: ...
```

**为什么有效**: 把 high/low 条件与具体的制度/组织情境绑定，增强论证的 concrete-ness。

**注意事项**: 
- 必须明确 high-W 和 low-W 对应的具体情境
- 避免把 moderator 简单等同于 "good/bad" 环境

**反模式**: high/low 论证只是数值大小的变化，没有实质性的理论差异。

---

<!--
pattern_id: categorical_severity_moderation_embedded
build_type: 机制推演型 / 调节效应型
source_papers: ["Darby_2023_MSOM"]
confidence: high
status: ready_for_corpus
-->

## Pattern: Categorical Severity Moderation — High vs Low

**适用场景**: moderator 为分类变量（如 high-severity vs low-severity recalls），且需论证两边机制差异。
**范文来源**: Darby, Ketchen, Ball & Mukherjee (2023), *Manufacturing & Service Operations Management*

**骨架**:
```
We now examine whether the effect of [IV] on [DV] differs for [category A] and [category B]. This aligns with [citation], which treated [A] and [B] not on a continuum, but as different categories.

[Category A — High] [Category A] involves [concrete risk], leading to [costs]. From [theory] perspective, [psychological mechanism] suggests the effect will be stronger because [reason].
[Concrete scenario] For example, [case illustration].

[Category B — Low] In contrast, [Category B] is less of a threat because [reason]. [Concrete scenario]. Thus, [lower impact].

[Prediction] We thus posit: H[X]: The [direction] effect of [IV] on [DV] is stronger for [Category A] than for [Category B].
```

**为什么有效**: 分类调节必须同时呈现两边的具体情境与理论逻辑，避免只论证增强方向。
**注意事项**:
- 两边案例需对称（各 1-2 个）
- 理论依据需解释“为什么分类变量改变机制强度”而非仅说“不同类别影响不同”
**反模式**: 只说 “when severity is high, the effect is stronger” 而不解释 low-severity 情况。

---

<!--
pattern_id: categorical_device_class_bilateral
build_type: 调节效应型
source_papers: ["Darby_2026_JOM"]
confidence: high
status: ready_for_corpus
-->

## Pattern: Categorical Risk Moderation — Low vs High Risk Devices

**适用场景**: moderator 为产品风险分类（如 FDA Class I/II vs Class III），需论证两边信息不对称差异。
**范文来源**: Darby, Wowak, Ketchen & Connelly (2026), *Journal of Operations Management*

**骨架**:
```
[Regulator] classifies [products] into [categories] depending on [criterion] ([citation]). [Category A] poses [risk level], whereas [Category B] poses [risk level].

[Category A — Low/Moderate] When defects arise in [Category A], the ramifications are straightforward to understand. For example, [low-risk scenario]. The low [core concept] makes it easier for [actor] to fulfill the monitoring function.

[Category B — High] However, when defects arise in [Category B], it becomes increasingly challenging to evaluate. Consider, for example, [high-risk scenario]. [Agent] possess [specific knowledge] difficult for outsiders to understand.

[Prediction] We thus expect that [moderator] will weaken the [direction] association between [IV] and [DV].
```

**为什么有效**: 分类调节必须同时呈现两边的具体风险与信息不对称差异。
**注意事项**:
- 案例需覆盖两类
- 需强调分类标准（如 risk vs complexity）
**反模式**: 只说高风险的特殊性，不解释低风险为何信息对称。

---

<!-- 
pattern_id: inverted_u_bilateral_moderation
build_type: 调节效应型 / 机制推演型
source_papers: ["Cui_Yang_Vertinsky_SMJ"]
confidence: high
status: ready_for_corpus
-->

## Pattern: Inverted-U Moderation — High/Low Bilateral Argumentation

**适用场景**: moderator 改变倒U型关系的曲率（flatten 或 steepen），需要分别论证曲线上升段（low to medium IV）和下降段（medium to high IV）的机制如何被 moderator 改变。

**微观动作序列**: Baseline inverted-U mechanism → moderator impact on ascending side → moderator impact on descending side → curvature prediction

**范文来源**: Cui, Yang, and Vertinsky (SMJ) — relative exploration × relational/positional/structural embeddedness

**骨架（负向调节 / flatten）**:
```
We argue that [moderator] attenuates the inverted U-shaped relationship between [IV] and [DV] by (a) lowering [actor]'s incentive to [opportunistic action] when the partnership is more [state A], and (b) increasing the cost of [aggressive action] when the partnership is more [state B].

Specifically, at low to medium levels of [IV] (i.e., more [state A]), the effect of [IV] on [DV] is smaller when [moderator] is higher, for two reasons. First, [mechanism 1 reducing incentive]. Second, [mechanism 2 reducing incentive].

At medium to high levels of [IV] (i.e., more [state B]), too, the effect of [IV] on [DV] is reduced by [moderator], as [moderator] increases the cost of [action] in this type of partnership. First, [mechanism 1 increasing cost]. Second, [mechanism 2 increasing cost].

To summarize, [actor]'s incentive to [DV] is reduced at low to medium levels of [IV], while the cost of [DV] is enlarged at medium to high levels of [IV], when [moderator] is higher. The effect of [IV] on [DV] is thus attenuated at both sides of the inverted U-shape. The overall slope of the relationship is likely to be flattened, with the peak of the slope becoming lower.

H[X]: [Moderator] negatively moderates the relationship between [IV] and [DV], such that the inverted U-shape is flattened when [moderator] is higher.
```

**骨架（正向调节 / steepen）**:
```
[Actor]'s [positional attribute] affects [resource access], which represents [power source] ([citation]). [Relative positional construct] therefore reflects [imbalance]. We argue that [relative advantage] intensifies the inverted U-shaped relationship between [IV] and [DV]: it further enhances [actor]'s incentive to [action] when the partnership is more [state A], and also reduces the costs of [aggressive action] when the partnership is more [state B].

At low to medium levels of [IV], [relative advantage] enhances [DV], for two reasons. First, [information advantage]. Second, [adaptation advantage].

At medium to high levels of [IV], [relative advantage] reduces the cost of [DV], for two reasons. First, [dependence asymmetry]. Second, [retaliation risk asymmetry].

To summarize, [incentive] is enhanced at low to medium levels of [IV], while [cost] is reduced at medium to high levels of [IV]. At both sides of the inverted U-shape, the effect of [IV] on [DV] is enlarged. The slope is likely to be steeper, and the peak higher.

H[X]: [Relative advantage] positively moderates the relationship between [IV] and [DV], such that the inverted U-shape is steepened when [relative advantage] is higher.
```

**为什么有效**:
- 倒U型关系的调节不能只说 "W moderates X→Y"，必须说明 moderator 如何改变曲线的**两侧**。
- "low to medium" / "medium to high" 的分段论证让二次交互有清晰的理论对应。
- flatten/steepen 的图形化语言降低读者认知负荷。

**注意事项**:
- 两侧论证必须对称（各两个子机制），不能一侧充分、一侧薄弱。
- 必须解释为什么 moderator 在上升段影响 incentive，在下降段影响 cost。
- 预测方向（flatten vs steepen）必须与二次交互项系数符号一致。

**反模式**: 只说 "when W is high, the effect is stronger" 而不分别论证 low/medium 和 medium/high 两段；将倒U型调节简化为线性调节。

---

<!-- 
pattern_id: dual_mechanism_convergent_moderation
build_type: 机制推演型 + 调节边界（双机制主效应）
source_papers: ["Li_Bapuji_Talluri_Singh_Narayanan_2025_JSCM"]
confidence: high
status: ready_for_corpus
related_intro_lens: write-introduction/academic-writing-corpus/theory-lens/08-dual-metaphor-stream-reconciliation.md
-->

## Pattern: Dual-Mechanism Convergent Moderation (with moderator×mechanism matrix)

**适用场景**: 当主效应建立在**两个互补机制**上（如 pipes/prisms、资源获取/资源利用、合法性/效率），每个调节变量需通过**两个机制通道**分别推理，并论证两通道**同向收敛**，从而合法地写出一个带符号的调节假设（strengthens / weakens）。是 dual-metaphor / dual-mechanism 主效应理论的天然调节推导伴侣。

**微观动作序列**: Dual-mechanism main effect（H1 经双机制收敛推导）→ Moderator framework setup（为何选这些 moderator，通常 framing 为"扩展网络/多重利益相关者"）→ Per-moderator dual-channel reasoning（通道 1 + 通道 2）→ Convergence claim（两通道同向）→ Signed hypothesis

**范文来源**: Li, Bapuji, Talluri, Singh & Narayanan (2025), *Journal of Supply Chain Management*（vertical spillover of product recalls: H1 pipes+prisms 主效应；H2-H4 common business ties / common institutional ownership / common analyst coverage 各经 cash-flow 通道 + impression 通道收敛推导）

**骨架（主效应 H1 — 双机制收敛推导）**:
```
[Channel 1] As [metaphor 1 / mechanism 1], [connective construct] [logic], resulting in [sub-effect 1] (i.e., [label 1]).
[Channel 2] As [metaphor 2 / mechanism 2], [connective construct] [logic], leading to [sub-effect 2] (i.e., [label 2]).
[Convergence → prediction] Given [sub-effect 1] and [sub-effect 2], [decision-makers] may be uncertain about [outcome]. Although [caveat: effect may not fully manifest short-run], [uncertainty / combined pressure] may prompt [decision-makers] to [lower evaluations / adjust behavior], resulting in [main effect].
H1: [IV] leads to [main effect on DV].
```

**骨架（调节 H2-H4 — 每个 moderator 双通道收敛 + 矩阵表）**:
```
[Framework] [Theory] suggests the [metaphor 1] and [metaphor 2] shaping [main effect] are influenced by [network structure] ([citation]). We focus on [N] [market stakeholders / network actors] that form the [direct and extended] social network acting as additional [metaphor 1] and [metaphor 2]: [W1], [W2], and [W3].

[Moderator W — dual-channel convergence]
As [metaphor 1], [W] [channel-1 logic], thereby [strengthening / weakening] the [main effect].
As [metaphor 2], [W] [channel-2 logic], thereby [strengthening / weakening] the [main effect].
Because both channels push in the [same] direction, [W] [strengthens / weakens] the [main effect].
H[X]: The [main effect] is [strengthened / weakened] by [W].
```

**呈现装置 — moderator×mechanism 矩阵表**:
```
|              | [Metaphor 1] ([sub-effect 1])        | [Metaphor 2] ([sub-effect 2])         |
|--------------|--------------------------------------|---------------------------------------|
| [W1]         | [channel-1 logic for W1]             | [channel-2 logic for W1]              |
| [W2]         | [channel-1 logic for W2]             | [channel-2 logic for W2]              |
| [W3]         | [channel-1 logic for W3]             | [channel-2 logic for W3]              |
```
（范文用一个 4 行 × 2 列表把"理论论证 + 3 moderator × 双通道"一次性呈现，读者与审稿人可逐格核验每个 moderator 是否真覆盖了双通道。）

**为什么有效**:
- 主效应若建立在双机制上，调节变量必须经**两个通道**分别推理，否则审稿人会问"这个 moderator 作用于哪条机制？为何忽略另一条？"
- 显式论证两通道**同向收敛**（convergent）才能用一个带符号假设（strengthens / weakens）合法概括双机制——这是 dual-mechanism 理论写带符号调节假设的理论牌照
- 矩阵表把 N moderator × 2 通道的推理**一次性可见化**，降低读者认知负荷，并使"每个 moderator 都覆盖双通道"可被逐格核验
- moderator framework（"direct + extended social network / 三类市场利益相关者"）把多个 moderator 从"事后添加"提升为"扩展网络边界"的理论推导

**注意事项**:
- 两通道必须**真的同向收敛**才能写带符号假设；若两通道反向，必须披露并改用 competing/ambiguous hypothesis（参见 write-theory C14 竞争假设收敛信号）
- 矩阵表每个 cell 必须有**独立的机制逻辑**，不能只填关键词；空 cell = 该 moderator 未覆盖该通道 = 调节论证缺口
- **H1 与 H2-H4 的机制基础必须一致**：H1 也应经双机制收敛推导，保证主效应与调节共用同一套机制语言
- moderator framework 的"扩展网络/多重利益相关者"framing 必须在引入第一个 moderator 之前就说明，否则矩阵显得 arbitrary

**反模式**:
- 只论证 moderator 作用于**一个**通道（如只讲 prism/categorization，漏掉 pipe/cash flow）→ 双机制理论的调节论证不完整，矩阵出现空 cell
- 把矩阵表当装饰——cell 里只有关键词而无机制逻辑
- 主效应 H1 单机制推导、调节变量却双机制推理 → 机制基础不一致，审稿人质疑"为什么 H1 不需要双机制而 H2 需要"
- 把本应收敛的两通道写成对立却不解释 → 应改 competing hypothesis 而非强行写带符号假设

<!--
pattern_id: asymmetric_disposition_context_moderation
build_type: 调节效应型 / 假设树型 (disposition × context)
source_papers: ["abdurakhmonov_ingram_ridge_2026_jom"]
status: EMERGING (1 篇)
related: 与 dual_mechanism_convergent_moderation (Li 2025) 概念正交：
         Li = moderator × 双机制矩阵（对称收敛，同一 moderator 经两条同向机制）；
         本 pattern = moderator × disposition-pole 矩阵（不对称，每个 moderator 对两极的机制不同）。
-->

## Pattern: Asymmetric Disposition×Context Moderation（多 moderator 同向、各异不对称机制作用于 disposition 两极）

**适用场景**: 主效应为 "[disposition trait] → [outcome]"，且 disposition 有两个对立极（pole A = high-trait，pole B = low-trait；如 liberal vs conservative CEO、promotion vs prevention focus、optimist vs pessimist）。理论贡献要求解释为什么**多个 contextual moderators 都同向削弱（或都同向增强）**该主效应，**但每个 moderator 经由不同的不对称机制分别作用于两个极**。与 dual_mechanism_convergent_moderation 互补：后者关注"一个 moderator 经两条机制同向收敛"；本 pattern 关注"多个 moderator 同向 moderates 但每个对两极的不对称机制彼此不同"。

**微观动作序列**: Disposition×outcome baseline（H1 已论证 pole-A → outcome vs pole-B → outcome 的对立）→ Meta-framework（统一框架，如 managerial discretion / latitude of action，在引入第一个 moderator 之前声明）→ Per-moderator asymmetric reasoning（pole-A 通道 + pole-B 通道，每个通道有**独立**机制）→ Convergence on signed moderation hypothesis

**范文来源**: Abdurakhmonov, Ingram & Ridge (2026), *Journal of Management*（CEO liberalism → corporate political transparency；三个边界条件 firm political uncertainty / industry transparency norms / industry concentration 全部 weaken 主效应，但每个经不同不对称机制作用于 liberal vs conservative CEO）

**骨架（per-moderator asymmetric reasoning — 三种已观察到的子变体）**:

```text
[Meta-framework] Drawing on and extending [meta-theory of discretion / latitude of action],
we argue that the extent to which [disposition trait] shapes [outcome] depends on the
latitude of action available. We examine [N] contextual contingencies that shape this
latitude: [W1], [W2], and [W3].

[Sub-variant 1 — Dampen-and-Maintain（一极被压制、另一极被维持在 baseline）]
[W1 = risk-elevating condition]
When [W1] is high, the risks associated with [outcome] increase because [mechanism A].
[Meta-theory] predicts that strong situational threats constrain the expression of
[disposition trait], because survival concerns override value expression ([citations]).
Under such conditions, even [pole-A actors] who would otherwise express [value-driven
outcome] become more cautious — [W1] thus SUPPRESSES [pole-A]'s distinctive
disposition-driven behavior. For [pole-B actors], [outcome] is already viewed as
[undesirable], and [W1] REINFORCES rather than alters that perspective — it simply
MAINTAINS [pole-B] at their already low [outcome] baseline.
→ [W1] weakens the positive relationship between [pole-A disposition] and [outcome].

[Sub-variant 2 — Floor+Ceiling Compression（两侧同时挤压：限高 + 托底）]
[W2 = institutional-norm condition]
When [W2] is strong, institutional conformity pressures reduce the distinctiveness of
additional [outcome] by [pole-A actors] — strong norms set a de facto "ceiling" on how
much [pole-A] can differentiate through greater [outcome] ([citations]). The same strong
[W2] simultaneously raises legitimacy costs for [pole-B actors] remaining [at the
opposite extreme], raising the minimum [outcome] "floor" they must adopt ([citations]).
→ [W2] compresses disposition-driven variance by limiting [pole-A]'s upside AND raising
[pole-B]'s floor, weakening the net [disposition]→[outcome] relationship.

[Sub-variant 3 — Equilibrium Lock-In（集体行动 / 寡头相互依赖锁定低均衡）]
[W3 = structural-interdependence condition]
[W3] creates structural interdependence among [actors], such that deviation from the
industry-equilibrium [outcome] by any single actor threatens [collective strategy] and
exposes [strategic information] to [rivals] ([citations]) — a collective-action problem:
while mutual deviation might benefit all, the first mover faces [retaliation / competitive
vulnerability] ([citation]). For [pole-A actors], this imposes structural disincentives
to break from the [low-outcome] equilibrium regardless of personal disposition; for
[pole-B actors], [W3] locks in their preferred [low-outcome] state, while fragmented
[low-W3] contexts allow gradual norm shifts that can elevate baseline [outcome] even
among disposition-resistant actors.
→ [W3] locks in the existing [low-outcome] equilibrium, weakening the [disposition]→[outcome] link.

[Prediction — 三个 moderator 同号]
H[X]:   [W1] weakens the positive relationship between [disposition] and [outcome].
H[X+1]: [W2] weakens the positive relationship between [disposition] and [outcome].
H[X+2]: [W3] weakens the positive relationship between [disposition] and [outcome].
```

**呈现装置 — moderator×disposition-pole reasoning table（可选，与 Li 2025 的 moderator×mechanism 矩阵互补）**:

| | Pole A (high-trait) channel | Pole B (low-trait) channel |
|---|---|---|
| **[W1] risk** | SUPPRESSES: 情境威胁压过价值表达 | MAINTAINS: 强化既有 baseline 偏好 |
| **[W2] norms** | CEILING: 从众限制差异化上限 | FLOOR: 合法性成本抬高最低阈值 |
| **[W3] structure** | LOCK-OUT: 结构性偏离 disincentive | LOCK-IN: 均衡维持偏好状态 |

（Li 2025 矩阵的 cell = 同一 moderator 的两条机制；本矩阵的 cell = 同一 moderator 对两极的不同机制。）

**为什么有效**:
- 当主效应建立在两极 disposition 上时，每个 moderator 对两极的约束机制通常不同。若只写 "W weakens X→Y" 而不分别论证两极，审稿人会问"这个 moderator 是压制了 pole-A 的发挥，还是托底了 pole-B 的反向倾向？机制是什么？"
- 显式论证 "all moderators weaken, but via different asymmetric mechanisms" 让读者理解为何需要多个 moderator 而非一个：每个 moderator 揭示 disposition×context 的一个不同侧面
- Meta-framework（如 managerial discretion / latitude of action）让多个不对称机制不显 ad-hoc，而是同一理论概念的不同具体化
- 三个子变体（dampen-and-maintain / floor+ceiling compression / equilibrium lock-in）覆盖目前观察到的三种不对称机制类型，可作为未来论文的参照模板

**注意事项**:
- **必须为每个 moderator 分别论证 pole-A 与 pole-B 的机制**，不能只说 "weakens"；pole-A 与 pole-B 的机制必须概念上不同（不对称是本 pattern 的核心）
- **多个 moderator 的不对称机制必须彼此不同**：若两个 moderator 经相同不对称机制，则其中一个是冗余的
- **meta-framework 必须在引入第一个 moderator 之前就声明**（"latitude of action" / "managerial discretion"），否则多个不对称机制显得拼凑
- **H1 与 H2-H4 的 disposition 基础必须一致**：H1 也应建立在 pole-A vs pole-B 的对立上，保证主效应与调节共用同一 disposition 框架
- **假设形式仍是标准 Buffering / Enhancing**（"weakens the positive relationship"），不对称机制体现在 theory text 而非 hypothesis statement——这与管理学顶刊规范一致（见范文 H2-H4 均用对称句式，不对称推理落在每节 prose）

**反模式**:
- 把本应不对称的两极写成对称（"both poles are equally constrained by W"）→ 失去本 pattern 的核心贡献，退化为标准 bilateral high/low
- 多个 moderator 的不对称机制实际相同（如全部是 risk-override）→ 应合并为单一 moderator
- meta-framework 引入太晚或太弱（"we also examine several moderators"）→ 失去 theoretical organizing function
- H1 单一方向论证（只讲 pole-A → outcome）而 H2-H4 突然引入两极不对称 → 机制基础不一致

