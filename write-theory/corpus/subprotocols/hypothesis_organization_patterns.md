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
pattern_id: parallel_mediators_effect_decomposition_horizon
build_type: 机制推演型 + Mode
source_papers: ["Bamberger_Homburg_Wielgos_2021_JM"]
confidence: low
status: needs_validation
-->

## Pattern: Common Trunk → Role-Separated Parallel Mediators → Effect Decomposition → Horizon Test

**验证状态**: EMERGING（单篇来源，待第二篇交叉验证）

**适用场景**: 同一结构性自变量通过多个可区分的组织行为/文化路径影响近端利益相关者结果，并且还可能存在方向相反的直接绩效路径；研究进一步比较短期与长期绩效。

**结构**:
```
[Theoretical trunk]
X changes [competitive/collaborative incentive structure].

[Parallel mediator branches]
X -> M1 [discretionary effort channel] -> Y
X -> M2 [opportunism channel] -> Y
X -> M3 [shared-culture channel] -> Y

[Effect decomposition]
X -> P (direct, possibly positive)
X -> M1/M2/M3 -> Y -> P (indirect, possibly negative)

[Horizon test]
P_short: direct and indirect paths may coexist
P_long: test whether the direct path persists while the relational path accumulates
```

**假设组织骨架**:
> "Drawing on [theory], we first argue that [X] changes [common incentive/collaboration condition]. We then derive three role-distinct pathways: [M1] captures what actors voluntarily invest, [M2] captures what they appropriate or withhold, and [M3] captures the shared norms that coordinate customer-facing behavior. Each pathway culminates in [proximal stakeholder outcome]. We next separate the direct association between [X] and [performance] from the indirect association transmitted through [stakeholder outcome]. Finally, we test whether these components differ between [short] and [long] horizons."

**为什么有效**:
- 共同主干只解释一次，减少三个中介段落重复。
- 用“投入—侵占—共享规范”等角色标签建立机制间排他性。
- direct / indirect / total effect 的区分把看似冲突的绩效文献转化为可检验的构成问题。
- 时间视野不是附加稳健性，而是裁决哪条路径更持久的理论测试。

**诚实边界**:
- 观察性 SEM/FE 只能支持 associated with / predicts；路径图本身不建立因果。
- “长期无直接效应”若仅依据不显著系数，只能写为未发现持续直接关联；若要支持真正的零效应假设，需等效性检验、区间界限或模型比较。
- 三个中介若概念或测量高度重叠，应合并或建立高阶构念，不能为了形成“机制簇”而硬拆。
- 必须报告 direct、各 specific indirect、aggregated indirect 与 total effect；只报告其中有利于故事的部分会制造选择性叙事。

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

---

<!--
pattern_id: sequential_two_stage_screening_asymmetric
build_type: 机制推演型
source_papers: ["Pupovac_Astvansh_Carrillat_Legoux_2026_POM"]
confidence: low
status: needs_validation
-->

## Pattern: Sequential Two-Stage Screening with Asymmetric Branches

**适用场景**: 当理论中的理想信息/线索（ideal screen）因制度、成本或隐私原因不可得时，actors 采用阶段性替代筛查，且不同阶段的替代线索对同一 outcome 产生理论上相反或不对称的效应。
**结构**: Common Trunk（recall/uncertainty→screening→reaction）→ Stage 1 Screen → Stage 2 Screen（conditional）→ Contextual Screens
**范文来源**: Pupovac, Astvansh, Carrillat, and Legoux (2026), *Production and Operations Management*（supplier shareholders use voluntary customer disclosure as Stage 1 screen and revenue dependence as Stage 2 screen after manufacturer recalls）

**骨架**:
```
The ideal screen for [actor] is [preferred cue], which reveals [state] ([citations]). 
However, [institutional/regulatory/cost reason] makes this cue unavailable. 
Therefore, [actor] adopts a [N]-stage screening process. 
In Stage 1, [actor] checks [observable cue 1]. 
If [condition for proceeding], in Stage 2, [actor] uses [observable cue 2]. 

We propose that [cue 1] [direction 1] [outcome] because [mechanism 1]. 
In contrast, [cue 2] [direction 2] [outcome] because [mechanism 2].
```

**连接词要求**:
- 理想 screen→制度缺口: "However, [reason] makes this cue unavailable."
- Stage 1→Stage 2: "If the answer is affirmative, [actor] proceeds to..."
- 不对称效应: "In contrast, ..."

**为什么有效**: 把制度可得性转化为主动理论机制，而不是背景噪音；两阶段结构既解释了为什么使用替代 screen，也解释了不同阶段为何产生相反效应。

**注意事项**:
- 必须论证理想 screen 为何不可得，且该不可得性是理论驱动的，而非数据限制
- 两个阶段必须概念独立；第一阶段决定是否进入第二阶段
- 相反效应必须有各自独立的机制，不能只是 "more vs less"

**反模式**: 如果两个阶段实为同一 screen 的不同操作化，或第二阶段无条件可用，不要用此模式。

<!--
pattern_id: typology_2x2_enumeration_main_effect
build_type: 机制推演型
source_papers: ["Du_Tsolmon_2024_ORSC"]
confidence: low
status: needs_validation
-->

## Pattern: 2×2 Combination Enumeration to Induce Main Effect

**适用场景**: 当主效应是 match/fit/similarity → positive outcome，需要通过"逐组合论证 match 优于 mismatch"来推导主效应时。适用于 fit/alignment/similarity 类研究（M&A 整合、联盟匹配、高管-组织匹配、技术-结构匹配），特别是有 2×2 或可枚举组合的双主体关系研究。
**结构**: Combination Enumeration（声明 N 种组合）→ Cell-by-Cell（机制+真实案例）→ Meta-Insight 归纳（match 优于 mismatch）→ H1
**范文来源**: Du and Tsolmon (2024), *Organization Science*（acquirer/target × LM/MM 四组合论证 structural similarity → retention）

**骨架**:
```
We conceptualize [N] types of [dimension] combinations between [actor A] and [actor B] 
based on whether each is [high/low on dimension]. We differentiate between [cell 1], 
[cell 2], [cell 3], and [cell 4]. Examining these combinations helps clarify how 
[match/mismatch] affects [outcome].

[Cell 1—match]: [mechanism]. [Real-world example].
[Cell 2—match]: [mechanism]. [Real-world example].
[Cell 3—mismatch]: [mechanism of friction]. [Real-world example].
[Cell 4—mismatch]: [mechanism of friction]. [Real-world example].

The analysis highlights that [meta-insight: when both are similar, actors are better 
positioned to facilitate X; conversely, misalignments may increase turnover]. 
Accordingly, we propose:
H1. [Match/similarity] is positively associated with [outcome].
```

**连接词要求**:
- 枚举开场: "We conceptualize [N] types of combinations..."
- 逐 cell 过渡: 每个 cell 用独立小节标题（如 "[Type A] Acquirer–[Type B] Target"）
- 归纳收敛: "The analysis highlights that... Accordingly, we propose:"

**为什么有效**: 把抽象的 similarity/fit 转化为 4 个可想象的组合，每个组合有真实案例——读者能"看见"理论；对角线对称（match cells 论证 retention 价值，mismatch cells 论证 turnover 风险）形成完整的归纳逻辑。

**注意事项**:
- 4 个 cell 的论证必须对称（每个 cell 都有机制 + 真实案例），不能厚此薄彼
- match/mismatch 的二分必须有理论依据（不能是为了凑 2×2 而强行二分）
- 真实案例必须与 cell 的机制逻辑一致，不能只是贴标签
- 配一张 Table 并列 4 个 cell 的 [integration focus / actor role / knowledge relevance / outcome implication]——可视化 typology 的论证结构

**反模式**: 把 2×2 当成假设组织框架（产生 4 个假设）而非主效应推导装置——本模式的力量在于 4 条路径归纳出 1 个主效应，若每 cell 各出一个假设则退化为对称矩阵模式。
