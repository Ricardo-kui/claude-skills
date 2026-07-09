# Hypothesis Organization Patterns

本文件收集复杂假设体系（多调节、中介+调节、间接调节等）的段落级组织模式。

---

<!--
pattern_id: triple_boundary_conditions
build_type: 假设树型 / 调节效应型
source_papers: ["Malshe_Agarwal_2015_JM"]
confidence: medium
status: ready_for_corpus
-->

## Pattern: Triple Parallel Boundary Conditions

**适用场景**: 主效应明确后，需要系统检验三类来自不同理论角度的情境异质性；调节变量之间没有统一元框架，但各自有独立理论依据。
**微观动作序列**: Preview（预告 k 个 moderators 及预期方向）→ Subsection 1（理论 + 假设）→ Subsection 2 → Subsection 3
**范文来源**: Malshe & Agarwal (2015), *Journal of Marketing*（service intensity, competitive intensity, sales growth）

**骨架**:
```
[Preview] In this section, we propose [number] potential moderators that can influence the [IV-DV] link: [moderator 1], [moderator 2], and [moderator 3]. We expect a more negative effect of [IV] on [DV] for [condition 1], [condition 2], and [condition 3].

[Moderator 1]. [Theory/literature] proposes that [trade-off] is sharper in [condition 1] because [reason] ([citation]). [Additional support]. Therefore:
H[X]a: The negative effect of [IV] on [DV] is more negative for [condition 1] than for [baseline].

[Moderator 2]. In [condition 2], [marginal benefit logic] implies that [IV] will lead managers to cut the activity with lower marginal benefits ([citation]). Thus:
H[X]b: The negative impact of [IV] on [DV] is more pronounced for [condition 2].

[Moderator 3]. Firms with [condition 3] face [cash flow logic], so [IV] exacerbates the pressure ([citation]). Accordingly:
H[X]c: [IV] affects [DV] more negatively for [condition 3].
```

**为什么有效**: 结构平行，便于读者比较；每个 moderator 都有独立理论依据，避免"fishing"印象。
**注意事项**:
- 三个 moderators 应来自不同理论角度，避免概念重叠
- 每个 subsection 篇幅应大致对称
- 若无统一元框架，需在 preview 中说明它们共同检验"主效应的异质性"

**反模式**: 三个 moderator 实为同一机制的不同操作化；preview 后各小节结构差异过大。

---

<!-- 
pattern_id: common_trunk_parallel_branches
build_type: 机制推演型 + 调节效应型
source_papers: ["Shen_Zhou_Wang_Zhang_2022_JOM"]
confidence: medium
status: ready_for_corpus
-->

## Pattern: Common Trunk → Parallel Branches

**适用场景**: 主效应有多个并行的机制路径，每个 moderator 都通过影响这些路径来调节主效应。
**结构**: H1 (trunk) → H2 (branch 1) → H3 (branch 2) → H4 (branch 3) → H5 (branch 4)
**范文来源**: Shen, Zhou, Wang, and Zhang (2022), *Journal of Operations Management*

**骨架**:
```
[Trunk — H1]
[IV] [direction] [DV] through [mechanism 1], [mechanism 2], and [mechanism 3].
H1: [IV] is [direction] related to [DV].

[Branch 1 — H2]
[W1] moderates this relationship.
When [W1] is high, [mechanism 1] is weakened because ...
When [W1] is low, [mechanism 1] is strengthened because ...
H2: The [direction] relationship between [IV] and [DV] is [weaker/stronger] when [W1] is high.

[Branch 2 — H3]
[W2] moderates this relationship.
When [W2] is high, [mechanism 2] is strengthened because ...
When [W2] is low, [mechanism 2] is weakened because ...
H3: ...
```

**连接词要求**: 
- Trunk → Branch 1: "These effects, however, are contingent on..."
- Branch 1 → Branch 2: "Similarly, ..." / "In a related vein, ..."

**为什么有效**: 读者只需理解一次机制 trunk，后续每个 branch 都是同一结构的应用。

**注意事项**: 
- 每个 branch 必须回到 trunk 的机制分别论证
- 建议用元框架把 branches 分组（如 environmental vs organizational）

**反模式**: 如果 moderators 影响的是不同机制而非同一机制的不同强度，不要用此模式。

---

<!-- 
pattern_id: baseline_dual_path_then_contingency_branches
build_type: 假设树型
source_papers: ["Singh_Grewal_2023_JMR"]
confidence: low
status: needs_validation
-->

## Pattern: Baseline Mechanism → Dual Path → Contingency Branches

**适用场景**: 主效应机制清晰，但有两个相对独立的 moderators，最后还有一个建立在前两者基础上的复杂交互。
**结构**: H1 (baseline) → H2 (moderation 1) → H3 (moderation 2) → H4 (indirect moderation)
**范文来源**: Singh and Grewal (2023), *Journal of Marketing Research*

**骨架**:
```
[H1 Baseline]
[IV] [direction] [DV] through [mechanism].
H1: ...

[H2 Contingency 1]
[W1] moderates this relationship because ...
H2: ...

[H3 Contingency 2]
[W2] also moderates this relationship because ...
H3: ...

[H4 Indirect Moderation]
Building on H2 and H3, [W2] mediates the moderating effect of [W1].
H4: ...
```

**为什么有效**: 逐步升级复杂度，避免一次性抛出复杂模型。

**注意事项**: 
- H4 必须有独立的理论机制
- 建议用 Figure 展示 Model A / Model B
- H2 和 H3 的论证要充分，否则 H4 会显得空中楼阁

**反模式**: 如果 H4 只是三向交互，不要用 "mediates the moderating effect" 的表述。

---

<!--
pattern_id: two_by_two_symmetric_matrix
build_type: 机制推演型
source_papers: ["Gamache_McNamara_Mannor_Johnson_2020_SMJ", "Zhao-Ding_Gaba_ORSC"]
confidence: high
status: ready_for_corpus
-->

## Pattern: 2×2 Symmetric Hypothesis Matrix

**适用场景**: IV 有两个互补/对立的维度或条件，DV 有两种相关类型或维度，理论预期两个 IV 值对两个 DV 值产生系统性反向效应。
**排列模式**: Parallel + Evidence-Contrast
**范文来源**:
- Gamache, McNamara, Mannor, and Johnson (2020), *Strategic Management Journal*（简单反向型）
- Zhao-Ding and Gaba, *Organization Science*（交叉反向型）

**骨架（通用）**:
```
[Define DV types/dimensions in T1a]
[Define IV dimensions/conditions in T1b + embed T2]

[Row 1: IV dimension A]
[Mechanism logic for DV_type_1]
Therefore, H1: [IV_A] is [direction_1] related to [DV_type_1].
[Mechanism logic for DV_type_2]
Therefore, H2: [IV_A] is [direction_2] related to [DV_type_2].

[Row 2: IV dimension B]
[Mechanism logic for DV_type_1 — reversed/altered from Row 1]
Therefore, H3: [IV_B] is [direction_3] related to [DV_type_1].
[Mechanism logic for DV_type_2 — reversed/altered from Row 1]
Therefore, H4: [IV_B] is [direction_4] related to [DV_type_2].
```

**子变体 A：简单反向 2×2（Simple Reversal）**

*范文来源*: Gamache et al. (2020, SMJ)

方向模式：
```
IV_A → DV_type_1: +    IV_A → DV_type_2: +
IV_B → DV_type_1: -    IV_B → DV_type_2: -
```

段落内部：每个 row 使用多个并行理由（如 Width-Type Three-Reason Parallel）。

**子变体 B：交叉反向 2×2（Cross Reversal）**

*范文来源*: Zhao-Ding & Gaba (ORSC)

方向模式：
```
IV_A → DV_type_1: +    IV_A → DV_type_2: -
IV_B → DV_type_1: -    IV_B → DV_type_2: +
```

段落内部：每个 row 内用 "Conversely" 连接两个 DV 维度的反向预测。

**为什么有效**: 读者通过 row 1 理解机制后，row 2 只需说明反向/交叉逻辑，高效利用认知惯性。
**注意事项**:
- 四个假设必须有独立理论依据，不能为了矩阵完整而硬凑
- 反向效应必须是真的方向反转或系统性交叉，不只是强度变化
- H4 如果与 H3 论证过度重叠，可能导致实证支持不足（见 Gamache et al. H4 p=.104 的教训）
**反模式**: 如果 IV 两个维度不对称，或 DV 两个类型在理论上不并列，不要硬凑 2×2。
