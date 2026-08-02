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
