# Bilateral Argumentation Templates

本文件收集调节效应/边界条件假设中同时论证 high-condition 和 low-condition 的句法模板。

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

