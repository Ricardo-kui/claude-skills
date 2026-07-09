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

