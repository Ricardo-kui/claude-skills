# Arrangement Patterns

本文件收集 Theory **多个假设段落之间**的组织方式（段间结构：common trunk → parallel branches、evidence-contrast、cumulative）。每个条目描述一个完整的段间安排模式，供 write-theory Phase 3.2 根据用户输入自动选择。

> **段内布局见 [`paragraph_layout.md`](paragraph_layout.md)**（一个假设推导段内部的 Topic→Reasoning→Tokens→Wrap 四段位 + 三类论据决策）。本文件 = 段间；该文件 = 段内。

---

<!-- 
pattern_id: parallel_branches_from_common_trunk
build_type: 机制推演型 + 调节效应型
source_papers: ["Shen_Zhou_Wang_Zhang_2022_JOM"]
confidence: medium
status: ready_for_corpus
-->

## Pattern: Parallel Branches from a Common Trunk

**适用场景**: 主效应有清晰的多个机制路径，需要用多个 moderators 分别检验每条路径的边界条件。
**结构**: Common Trunk (H1) → Parallel Branches (H2, H3, H4, H5...)
**范文来源**: Shen, Zhou, Wang, and Zhang (2022), *Journal of Operations Management*

**骨架**:
```
[Common Trunk — H1]
We argue that [IV] [direction] [DV] through three mechanisms: 
(1) [mechanism 1], (2) [mechanism 2], and (3) [mechanism 3].
Therefore, H1: ...

[Branch 1 — H2]
These effects, however, are contingent on [W1]. 
When [W1] is high, [mechanism 1]: ...; [mechanism 2]: ...; [mechanism 3]: ...
When [W1] is low, [mechanism 1]: ...; [mechanism 2]: ...; [mechanism 3]: ...
Therefore, H2: ...

[Branch 2 — H3]
Similarly, [W2] alters the relationship because ...
When [W2] is high, ...
When [W2] is low, ...
Therefore, H3: ...
```

**为什么有效**: 
- 读者只需在 H1 理解一次机制 trunk
- 每个 moderator 段落结构相同，降低认知负荷
- 便于用元框架（environmental/organizational）组织多个 moderators

**注意事项**: 
- 每个 branch 必须明确回到 trunk 的三个机制
- 如果 moderators 之间没有 conceptual 联系，需要另一个元框架（如 resource supply/demand）
- 四个及以上 branches 时，考虑合并或分组，避免段落冗长

**反模式**: 如果 moderator 改变的是机制本身而非同一路径的不同强度，不要用 Parallel，应改用假设树型的分叉结构。

---

<!-- 
pattern_id: evidence_contrast_then_warrant_embedded
build_type: 机制推演型 / 反直觉预测型
source_papers: ["Singh_Grewal_2023_JMR"]
confidence: low
status: needs_validation
-->

## Pattern: Evidence-Contrast → Warrant-Embedded

**适用场景**: 论文要挑战一个既有理论观点时。先摆出反方理论预测，再转折提出自己的机制和假设。
**结构**: Claim → Opposing Evidence（理论） → Pivot → Own Mechanism + Evidence 交织 → Hypothesis
**范文来源**: Singh and Grewal (2023), *Journal of Marketing Research*

**骨架**:
```
[Claim/Anchor]
From an [established theory] perspective, [IV] should not influence [DV] because [reason].

[Opposing Evidence]
[Theory] implies that [prediction]. [Citation] supports this view by showing [finding].

[Pivot]
However, a [alternative theory] perspective and associated [model/literature] suggest a different prediction.

[Own Mechanism + Evidence 交织]
We argue that [IV] influences [DV] through [mechanism]. 
This is because [theoretical reason] ([citation]). 
Specifically, [mechanism step] ([citation]).
Consequently, [final step].

[Prediction]
Therefore, we hypothesize: H1: ...
```

**为什么有效**: 通过先承认对立观点，增强转折后的说服力；读者会觉得新机制不是作者臆断，而是对现有理论的补充/修正。

**注意事项**: 
- 反方观点必须被准确、公平地陈述
- pivot 必须有明确的理论或经验依据，不能只是 "however"
- 适用于理论冲突明显的研究问题

**反模式**: 如果文献中没有明确的对立理论预测，不要人为制造 Evidence-Contrast，会显得做作。

---

<!-- 
pattern_id: cumulative_indirect_moderation
build_type: 假设树型 / 机制推演型
source_papers: ["Singh_Grewal_2023_JMR"]
confidence: low
status: needs_validation
-->

## Pattern: Cumulative — Indirect Moderation Built on Prior Moderators

**适用场景**: 当 H4 不是独立的调节假设，而是建立在 H2/H3 两个调节假设基础上的复杂交互（如 mediated moderation）时使用。
**结构**: H1 (Main Effect) → H2 (Moderation 1) → H3 (Moderation 2) → H4 (Indirect Moderation of H2 by H3)
**范文来源**: Singh and Grewal (2023), *Journal of Marketing Research*

**骨架**:
```
[H1 Main Effect]
[IV] [direction] [DV]. Therefore, H1: ...

[H2 Moderation 1]
[W1] moderates this relationship because ... Therefore, H2: ...

[H3 Moderation 2]
[W2] also moderates this relationship because ... Therefore, H3: ...

[H4 Indirect Moderation]
Building on the logic of H2 and H3, we argue that [W2] mediates the moderating effect of [W1].
Specifically, [W2] disseminates information about [W1], making [actor] more/less likely to [action].
Therefore, H4: The interaction of [IV] and [W2] mediates the moderating effect of [W1] on [IV]→[DV].
```

**为什么有效**: 把最复杂的假设放在最后，让读者先理解两个简单调节，再接受它们的组合。

**注意事项**: 
- H4 必须有独立的理论机制，不能只靠 "building on H2 and H3"
- 建议配 Model A / Model B 图示
- H4 的 Warrant 需要实质性理论，避免过度依赖方法论文献

**反模式**: 如果 H4 只是三向交互（three-way interaction）而非 mediated moderation，不要用此模式。


### 变体 A：反假设驳斥式开场（Counter-Assumption Refutation Opening）

<!--
pattern_id: counter_assumption_refutation_opening
build_type: 跨类型（机制推演型/调节效应型的开场段）
source_papers: ["carpenterwestphal2001_AMJ"]
confidence: high
status: VERIFIED — expert_audit_override (Westphal 系裁决: 用户点名最爱学者,引言/理论单源足矣)
-->

**适用场景**: 现有文献对 [IV]→[DV] 存在一边倒的方向性共识（通常是负面预测），而本文要反转或条件化该共识——用"暴露共识的隐含假设"开门，比直接宣称相反结论更有说服力。
**排列模式**: Evidence-Contrast（反方观点 → 隐含假设暴露 → 己方机制反转）
**范文来源**: Carpenter & Westphal (2001, AMJ)

**骨架**:
```
[文献共识] [Field] critics have typically argued that [IV] reduces [DV] ([citations]).
[假设暴露] Such an argument assumes that [hidden_assumption underlying the consensus].
[视角反转] In contrast, our [perspective_name] indicates how [IV] can enhance or
diminish [DV], by [reframing mechanism that turns the hidden assumption into
an empirical question].
[路径预告] [可选 1 句：预告后文将引入的条件/情境，把"是否"转化为"何时"。]
```

**为什么有效**: 不正面否定共识，而是把共识降格为"一个未经验证的假设"，使反转成为逻辑必然而非立场之争；"can enhance or diminish" 的双向措辞把争论从方向之争转向条件之争，为后文情境化假设集铺路。
**注意事项**: 隐含假设必须真实存在于被引文献的论证中且可被自己的视角证伪，否则是稻草人；反转句必须给出机制性理由（本文是知识结构/图式机制），不能只靠 "In contrast" 完成转折。
**反模式**: 夸大对方观点以制造靶子；只宣布"我们发现相反结果"而无机制解释；把隐含假设暴露写成长段文献批判（1-2 句即可）。

**原文锚定**:
> "Such an argument assumes that the knowledge and perspective gained on other boards are largely irrelevant to decision making at the focal firm."
> "In contrast, our sociocognitive perspective indicates how experience on other boards can enhance or diminish directors' ability to contribute to strategy"

<!-- wb:carpenter_and_westphal_2001_strategic_context_of_external_ne:theory_counter_assumption_refutation_opening -->
