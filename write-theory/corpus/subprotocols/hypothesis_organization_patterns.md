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


## 变体速查表

> 检索辅助（2026-08-09 P0 补建）。状态列空白 = 正文未标注验证状态（旧 Pattern）。状态词表（2026-08-29 统一，与 _evidence_registry.yaml 一致）：ROBUST > VERIFIED > EMERGING（含（可选）后缀）；LEGACY-DIAGNOSTIC 保留（工具诊断类）；召回主题条目按用户 2026-08-29 裁决单源 VERIFIED。完整骨架、适用条件与诚实边界见下方变体正文。

| # | 变体 | 适用场景 | 状态 | 来源 |
|---|---|---|---|---|
| 1 | Pattern: Triple Parallel Boundary Conditio | 主效应明确后，需要系统检验三类来自不同理论角度的情境异质性；调节变量之间没有统一元框架，但各 |  | Malshe & Agarwal (2015), *Jour |
| 2 | Pattern: Common Trunk → Parallel Branches | 主效应有多个并行的机制路径，每个 moderator 都通过影响这些路径来调节主效应。 |  | Shen, Zhou, Wang, and Zhang (2 |
| 3 | Pattern: Common Trunk → Role-Separated Par | 同一结构性自变量通过多个可区分的组织行为/文化路径影响近端利益相关者结果，并且还可能存在方向 | EMERGING（单篇来源，待第 |  |
| 4 | Pattern: Baseline Mechanism → Dual Path →  | 主效应机制清晰，但有两个相对独立的 moderators，最后还有一个建立在前两者基础上的复 |  | Singh and Grewal (2023), *Jour |
| 5 | Pattern: 2×2 Symmetric Hypothesis Matrix | IV 有两个互补/对立的维度或条件，DV 有两种相关类型或维度，理论预期两个 IV 值对两个 |  | - Gamache, McNamara, Mannor, a |
| 6 | Pattern: Sequential Two-Stage Screening wi | 当理论中的理想信息/线索（ideal screen）因制度、成本或隐私原因不可得时，acto |  | Pupovac, Astvansh, Carrillat,  |
| 7 | Pattern: 2×2 Combination Enumeration to In | 当主效应是 match/fit/similarity → positive outcome， |  | Du and Tsolmon (2024), *Organi |
| 8 | Pattern: Shared Orientation → Divergent Ou | 同一 actor trait 先塑造一种组织导向，该导向再关联多个战略结果；部分结果有益、部 |  | Kashmiri, Nicol, and Arora (20 |
| 9 | Pattern: Dual-Edged Trunk → Signed Enhanci | 主效应净方向事先不定（双刃剑）；理论用一组异号权变分别强化升值机制与贬值机制；不设 unco |  | Castellaneta, Conti, and Kacpe |
| 10 | Pattern: Mechanism-Loss Trunk → Multi-Outc | 拥挤的治理/结构文献中，IV 不是“又一个 board/TMT characteristic |  | Zorn, Shropshire, Martin, Comb |
| 11 | Pattern: Per-Stakeholder Paired (Main + Cue-M | 同一特质 IV 对多个外部利益相关者各产生“主效应（默认表现型）+ cue 切换（对立表现型）”配对；贡献=同一特质在多个 stakeholder 关系中的切换节律 | EMERGING（单篇来源，待第 | Ridge, Hill, Ingram, Kolomeitsev |
| 12 | Pattern: Dual-Role IV → Shared-Logic Compressed T5 | 对立力量 trunk 后，同一组 W 先立主效应，再用共享短/长期逻辑压缩全部交互，而非每 moderator 独立嵌入 | EMERGING（单篇来源，待第二篇） | Liu, Liu & Luo (2016), *Journal of Marketing* |

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

**验证状态**: EMERGING（单源）

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

<!--
pattern_id: shared_orientation_divergent_outcomes_selective_remedy
build_type: 机制推演型 + 假设树型 + 调节效应型
source_papers: ["Kashmiri_Nicol_Arora_2017_JAMS"]
confidence: low
status: needs_validation
-->

## Pattern: Shared Orientation → Divergent Outcome Portfolio → Selective Remedy

**适用场景**: 同一 actor trait 先塑造一种组织导向，该导向再关联多个战略结果；部分结果有益、部分有害，且一个内部治理力量只针对有害分支发挥缓冲作用。

**结构**: Actor trait → organizational orientation（H1）→ parallel outcome branches（direct + mediated hypotheses）→ harmful branch only → direct countervailing moderation + mechanism-bearing indirect moderation。

**范文来源**: Kashmiri, Nicol, and Arora (2017), *Journal of the Academy of Marketing Science*（CEO narcissism → competitive aggressiveness → innovation speed / novelty / product-harm crisis；marketing power → customer orientation → product-safety buffering）。

**骨架**:
```text
[Common trunk]
[Actor trait] channels attention, interpretation, and organizational control toward
[organizational orientation]. Therefore, H1 predicts [trait → orientation].

[Beneficial branch 1]
The trait directly changes [risk/visibility calculus], while the orientation accelerates
[process], jointly predicting [beneficial outcome 1]. State the direct and indirect
predictions separately.

[Beneficial branch 2]
Rebuild the branch-specific why-chain for [beneficial outcome 2]. Do not assume that
because the same orientation appears in branch 1, it automatically transmits this branch.

[Harmful branch]
The trait reallocates attention away from [less visible safeguard], and the orientation
compresses [testing/deliberation time], increasing [harmful outcome].

[Selective remedy]
[Countervailing internal actor/resource] has both the motive and influence to protect
[stake/asset harmed by the outcome]. It buffers the harmful branch directly and, where
measured, strengthens [protective orientation] that carries part of the buffering process.
```

**为什么有效**:
- 一个共同主干降低认知负荷，三个结果分支又各自保留 outcome-specific warrant，避免“同一中介万能化”。
- 结果的正负效价形成 rising action：先交付战略收益，再揭示安全代价，最后给出可治理的选择性制衡。
- Remedy 不是附加管理启示，而是从受损资产、内部角色动机与权力来源推演出的正式边界条件。

**注意事项**:
- 每个分支必须独立通过 why-chain audit；共享 antecedent 或 mediator 不等于共享全部机制。
- 若某个间接效应不成立，Results 与 Discussion 必须保留失败分支，并缩窄“shared mechanism”措辞。
- 调节段应分别解释强/弱治理条件；Kashmiri et al. 对高营销权力的论证较充分，对低权力条件的显式双边推演较弱，模仿时应补齐。
- 不同测量尺度的结果可组成理论 portfolio，但除非联合模型真实估计 trade-off，否则不能声称净收益或净损失。

**反模式**:
- 为了假设编号对称，让同一中介机械地解释全部结果。
- 没有角色动机与影响力来源，仅把任意部门权力写成“checks and balances”。
- 将 safety controversy、product-harm crisis、recall occurrence、recall timing 和 recall strategy 混为同一构念。

---

<!--
pattern_id: dual_edged_signed_enhancing_hindering_branches
build_type: 调节效应型
source_papers: ["Castellaneta_Conti_Kacperczyk_2017_SMJ"]
confidence: medium
status: EMERGING
story_fidelity: section_variant
-->

## Pattern: Dual-Edged Trunk → Signed Enhancing/Hindering Branches

**适用场景**: 主效应净方向事先不定（双刃剑）；理论用一组**异号**权变分别强化升值机制与贬值机制；不设 unconditional 主效应假设。
**排列模式**: Dual-blade common trunk → Enhancing branch → Hindering branch(es)
**范文来源**: Castellaneta, Conti, and Kacperczyk (2017), *Strategic Management Journal*

**骨架**:
```
[Dual-blade trunk]
[X] may raise [Y] by [enhancing mechanism toward rivals].
[X] may lower [Y] by [hindering mechanism toward buyers].
Net effect of [X] on [Y] is a priori ambiguous.

[Enhancing branch]
When [W_enhance] is high, the enhancing blade dominates because [amplification logic].
H[e]: impact of [X] on [Y] is more positive when [W_enhance] is higher.

[Hindering branch]
When [W_hinder] is high, the hindering blade dominates because [amplification logic].
H[h]: impact of [X] on [Y] is more negative when [W_hinder] is higher.
[Optional] H[h2] for a second hinder-side industry contingency sharing the same blade.
```

**为什么有效**:
- 先锁定双刃张力，再分节给出异号预测，读者不会把正/负交互当成论证不一致。
- Enhancing / Hindering 分节标题本身就是假设体系的导航装置。
- 允许多个 hindering moderators 共享贬值刃，只要各自入口构念可区分（如评估不确定性 vs lemons 风险）。

**注意事项**:
- 每个 hindering moderator 必须有独立 why-chain，不能只重复 “information asymmetry → discount”。
- 若实证出现同号交互，Results 需收窄“双刃”措辞，不能事后改写成单刃。
- 与 E4（竞争响应裁决）近亲：E4 裁决的是 response repertoire；本模式裁决的是 valuation blade。

**反模式**:
- 双刃只在 Introduction 出现，Theory 假设全是同号调节。
- 无 trunk 直接写三个行业交互 → 像变量清单而非理论故事。
- 把 buyer-side 与 rival-side 信息机制混成同一句话而不分刃。

---

<!--
pattern_id: mechanism_loss_trunk_multi_outcome_external_substitute
build_type: 机制推演型
source_papers: ["Zorn_Shropshire_Martin_Combs_Ketchen_2017_SMJ"]
confidence: low
status: needs_validation
story_fidelity: section_variant
-->

## Pattern: Mechanism-Loss Trunk → Multi-Outcome Tree → External Partial-Substitute Boundary

**适用场景**: 拥挤的治理/结构文献中，IV 不是“又一个 board/TMT characteristic”，而是**某类内部行动者被结构移除后，其原本提供的监督收益丧失**；同一丧失状态映射到多个近端/远端治理结果，再用外部监督力量作为**部分替代**边界（衰减而非完全替换）。

**结构**: Benefit inventory（T 提供什么）→ Loss under structure S → Parallel outcome branches（Y1…Yn）→ External monitors W1/W2 attenuate S→Y across the portfolio。

**范文来源**: Zorn, Shropshire, Martin, Combs, and Ketchen (2017), *Strategic Management Journal*（lone-insider boards；CEO pay / misconduct / performance；analysts & institutional owners）。

**骨架**:
```text
[Benefit inventory — common trunk]
Drawing on [counter-stream within the dominant lens], members of [removed actor class]
enable [remaining monitors] by supplying (1) [Benefit1: information channel] and
(2) [Benefit2: contestation / succession threat].

[Mechanism loss]
Under [structure S], these benefits are lost. [Focal agent] therefore gains discretion
for self-serving action at [principal]'s expense.

[Outcome portfolio — parallel branches]
The same loss state implies:
- Y1 via [outcome-specific warrant tied to Benefit1/2] → H[a]
- Y2 via [distinct warrant] → H[b]
- Y3 via [distinct warrant] → H[c]
Do not invent a new master mechanism per DV; rebuild only the branch warrant.

[External partial-substitute boundary]
[W] does not restore [removed actor class], but injects substitute [scrutiny/information]
that raises [board/monitor] awareness when internal monitoring is weak.
Hence each S→Y link is attenuated as W increases → H[mod] family.
```

**为什么有效**:
- 把 IV 从“结构标签”改写为“机制丧失状态”，在拥挤文献中重新打开贡献空间。
- 读者只学一次 trunk，多 outcome 成为同一 knot 的证据组合，而非变量清单。
- 外部边界承认治理束（governance bundle），又明确 **partial substitute**，避免“外部监督可完全替代董事会”的过度主张。

**与近邻模式区分**:
- vs `common_trunk_parallel_branches`：后者分支主要是 **同一 DV 上的 moderators**；本模式先分支 **多个 DVs**，再挂跨组合的衰减调节。
- vs `shared_orientation_divergent_outcomes_selective_remedy`：后者是 trait→orientation→正负结果，remedy **选择性打击有害支**；本模式是 **结构缺失→收益丧失**，外部 W **同向衰减整个结果族**。
- vs `board_governance_boundary_condition`：后者董事会 independence **放大**短视压力；本模式外部监督 **衰减**内部机制丧失的危害。

**注意事项**:
- 每个 outcome 分支仍需独立 warrant；禁止“丧失状态万能解释”而无分支论证。
- Benefit 清单应短（通常 2 项）且理论可追溯；不要为了凑数扩成五项。
- 调节段应写明 W **不能替换**被移除行动者，只能部分补偿信息/压力。
- 单篇 EMERGING：未验证前不要作为 write-theory 默认路由。

**反模式**:
- 把任意 board dummy 都写成 what-is-lost，却说不清被移除者原先提供的具体收益。
- 多 DV 共用一段机制、假设处只换因变量名。
- 将 analysts/institutions 写成完全替代董事会的治理机制。

---

<!--
pattern_id: per_stakeholder_paired_main_cue_moderation
build_type: 调节效应型
source_papers: ["Ridge_Hill_Ingram_Kolomeitsev_Worrell_2024_AMJ"]
confidence: emerging
status: needs_cross_paper_validation
story_fidelity: section_variant
-->

## Pattern: Per-Stakeholder Paired (Main + Cue-Moderation) Parallel

**适用场景**: 同一特质/倾向 IV 面对**多个外部利益相关者**（如 regulators、acquiring firms），理论预期对每个 stakeholder 关系都存在"主效应（默认表现型）+ cue 切换（对立表现型）"的配对结构。论文贡献=同一特质在多条 stakeholder 关系中呈现一致的"默认→切换"节律。区别于把每个 stakeholder 写成一个独立 moderator 的堆叠：这里的**每对 main+cue-moderation 共享同一特质机制**，配对架构让读者看到"同一个 trait 逻辑在不同 stakeholder 上复现"。

**微观动作序列**: Trait default manifestation（一次）→ 对每个 stakeholder：主效应（默认表现型应用到该关系）→ cue 定义（该 stakeholder 的什么动作是"默认失效"证据）→ 切换假设（cue 激活对立表现型）
**范文来源**: Ridge, Hill, Ingram, Kolomeitsev & Worrell (2024), *Academy of Management Journal*（CEO paranoia → lobbying breadth（regulators）、M&A activity（acquirers）；paranoia-relevant cues 激活 aggression）

**骨架**:
```
[特质默认表现型（全局一次，避免每个 stakeholder 重复）]
[IV trait] is strongly associated with [default manifestation]—which [function]. Individuals higher in [trait] [scan/monitor] and [attribute malintent], leading them to [default behavior] toward external entities.

[Per-Stakeholder 1: 主效应（默认表现型）]
Stakeholder 1 是 [regulator/actor type]。Organizations with CEOs higher in [trait] will tend to [default manifestation toward stakeholder 1] to prevent antagonizing them and eliciting negative repercussions. Thus:
H1: [Trait] is [negatively] related to [DV 1] (engagement with stakeholder 1).

[Per-Stakeholder 1: cue 定义 + 切换]
Actions by [stakeholder 1] that target the [CEO/firm] are [trait]-relevant cues—evidence that [default manifestation] has not provided protection. When such cues accumulate (e.g., [cue intensity] increases), CEOs higher in [trait] shift from [default manifestation] to [opposing manifestation], directly engaging [stakeholder 1]. Thus:
H2: There will be a positive interaction effect of [trait] and [cue 1] on [DV 1], such that the negative relationship between [trait] and [DV 1] is mitigated as [cue 1] increases and prompts more [opposing manifestation] action.

[Per-Stakeholder 2: 同构配对（复用 trait 逻辑，仅换 stakeholder 与 DV）]
Stakeholder 2 是 [another actor type]. The same logic applies: [trait] defaults to [default manifestation toward stakeholder 2]... Thus:
H3: [Trait] is [negatively] related to [DV 2].
H4: The positive interaction effect of [trait] and [cue 2] on [DV 2] mitigates the negative relationship as [cue 2] increases.
```

**为什么有效**: 特质机制只论证一次（默认表现型全局 opener），每个 stakeholder 段落只需应用+切换——避免"每个 DV 重推同一 trait 机制"的重复；配对结构把"默认→切换"的节律做成可复现的节奏，审稿人看到的是同一理论逻辑的多点验证而非变量清单。

**与近邻模式区分**:
- vs `triple_parallel_boundary_conditions`：后者是**多个独立 moderator** 各改主效应强度（无 trait-default 配对、无切换）；本模式是**同一特质**在每个 stakeholder 上的 main+cue 配对。
- vs `common_trunk_parallel_branches`：后者分支是**同一 DV 上的多机制/moderator**；本模式分支是**多个 stakeholder 关系**，每个关系内部是主效应+cue 切换的两步。
- vs `dual_edged_trunk_signed_enhancing_hindering`（E8）：后者是双刃剑**净效应不定、可无主效应**；本模式必须有主效应（默认表现型）。
- vs `shared_orientation_divergent_outcomes`：后者是 trait→orientation→多结果；本模式是 trait→每个 stakeholder 的默认表现型 + cue 切换。

**注意事项**:
- 特质默认表现型的机制论证应**只做一次**（全局 opener），各 stakeholder 段落引用即可，不要重复推演。
- 每个 stakeholder 的 cue 必须具体（"什么动作是默认失效的证据"），不能写成泛化的情境强度。
- 配对假设句式必须同构（"negative relationship ... mitigated as [cue] increases"），否则失去平行节律。
- 单篇 EMERGING：未验证前不要作为 write-theory 默认路由。

**反模式**:
- 每个 stakeholder 都重推一遍 trait 机制 → 冗长且失去全局统一性。
- 只有主效应、没有 cue 切换，或切换假设写成 buffering（机制削弱）而非 manifestation-switch。
- 把不同 stakeholder 写成不同 trait 机制（机制不一致）→ 配对架构崩塌。
- cue 与该 stakeholder 关系脱钩（泛化情境）→ 切换逻辑失去证据基础。

---

<!--
pattern_id: dual_role_iv_then_shared_logic_compressed_t5
build_type: 机制推演型 + 调节效应型
source_papers: ["Liu_Liu_Luo_2016_JM"]
confidence: medium
status: EMERGING
-->

## Pattern: Dual-Role IV → Shared-Logic Compressed T5

**适用场景**: 两条对立力量构成 trunk；同一组行动者特征既有独立主效应，又调节 trunk 上的每条力量；交互数量多（≥4）且共享同一短/长期逻辑，不宜每条交互独立成节。
**结构**: H1–H2 (opposing-force trunk) → H3–H4 (W 独立主效应) → H5–H8 (同一逻辑压缩全部 W×X 交互)
**范文来源**: Liu, Liu & Luo (2016), *Journal of Marketing*

**骨架**:
```
We first discuss two basic [event] characteristics, [cost] and [harm], which form the base for [choice]. We then discuss how the [actor]'s personal interests may influence a [unit]'s [choice], both directly and indirectly through interactions with [cost] and [harm].

[Trunk — H1/H2]
[Cost] reduces the likelihood of [complete option] because [short-term earnings logic]. [Harm] increases that likelihood because [long-term trust logic].

[Dual-role W — H3/H4]
[Cash] tilts [actor] toward short-term earnings and therefore away from [complete option]. [Equity] tilts [actor] toward long-term value and therefore toward [complete option]. [Tenure] [entrenchment / short-horizon logic].

[Compressed T5]
Based on similar theoretical reasoning, we now explore how the [k] [actor] characteristics might moderate the impact of the two [event] characteristics on [choice]. Because of the short- versus long-term orientation of [cash] versus [equity], these two characteristics should moderate the impact of [event] characteristics in opposite directions.
```

**为什么有效**: 把 W 写成双角色预测变量（先主效应、再权重调节），再用 similar theoretical reasoning 避免六条交互各写一遍 why-chain；读者看到的是同一短/长期逻辑在两条对立基线上的倾斜，而不是假设树或平行嵌入。

**与近邻模式区分**:
- vs `common_trunk_parallel_branches`：后者分支是同一 DV 上的多机制路径；本模式 trunk 是两条对立 IV，W 既是第三组 IV 又是调节。
- vs E3 每 moderator 独立嵌入：E3 要求每 W 单独成节；本模式用共享逻辑压缩 T5。
- vs E1 Step 4 把 Z→Y 标为可选：本模式强制先写 W 的独立主效应，再写交互。

**注意事项**:
- 压缩过度时双边论证会变薄（C20）；每条交互至少要有方向句，不能只写"similar reasoning"然后列假设。
- 单篇 EMERGING：未验证前不要作为 write-theory 默认路由。

**反模式**:
- 把双角色写成假设树（每个 W 一个子树）。
- 交互节重写主效应 why-chain。
- 把成本与伤害写成不可通约的对立理论。

**原文锚点**: "We then discuss how the CEO's personal interests may influence a company's remedy decision, both directly and indirectly through interactions with remedy cost and consumer harm."


## Pattern: Context-Assigned Decision-Margin Split（情境分配决策边际拆分）

**验证状态**: VERIFIED（expert_audit_override 2026-08-28：产品召回为主研究领域，单源足矣）

**适用场景**: 同一前因（X）理论上影响多个结果，但各结果的**决策边际不同**（是否行动 vs 多快行动），且由一个**情境构念**（severity / urgency / reversibility 等客观分级）——而非事后 subgrouping——分配各边际。X 在各边际被赋予**不同理论角色与不同机制**，预测方向可以对齐。

**与近邻模式区分**（关键：不是调节）:
- vs categorical_severity_moderation_embedded（Darby 2023 MSOM, tfr_088）：那是严重度调节**同一条** X→timing 关系的强度；本模式中情境构念**不调节任何单一关系**，而是把结果空间切成两个决策窗口，各配独立 DV 与独立机制
- vs shared_orientation_divergent_outcomes（Kashmiri 2017）：后者 trait→orientation→多结果共用一个中介主干；本模式无中介主干假设，机制按边际分配（rule-following vs stakeholder responsiveness）
- vs per_stakeholder_paired（Ridge 2024）：后者按 stakeholder 配对 main+cue 切换；本模式按决策边际（whether/when）分配角色
- vs 2×2 Symmetric Matrix：本模式只有一个 IV 与一个情境分级，不构成 IV 维度×DV 类型矩阵

**微观动作序列**: 开篇边际划分声明（"Recalls differ in severity, which leads to variation in if and when..."）→ 边际 1 小节（确立该边际存在裁量空间→配对案例证明→边际专属机制→H1）→ 边际 2 小节（转折语 "We now transition to... little discretion in whether, but nonetheless contain discretion in when"→案例→专属机制→H2）

**决策链→边际分配实录（wowak2020 §2+§3，与 decision_rights_preamble 配套使用）**:
- 同一条间接治理链（工程师→召回委员会→VP of quality→董事会周期评审反馈）承载两个假设；董事会设定的默认期望不落在"是否召回"本身，而落在管理层于各边际行使的裁量上
- **低严重度边际 = 是否发起**：class 3 缺陷可隐藏不召回（ Boston Scientific 照章召回说明书缺失 vs 匿名企业标注错误仅修后续批次），故 class-3 计数被重标为裁量度量而非质量度量；董事会 rule-following 期望（女性董事更"go by the book"，且少数地位+高不确定性下该差异放大）→ H1: 计数上升
- **高严重度边际 = 多快发起**：class 1 缺陷危及生命（St. Jude 电池故障除颤器 / Pfizer 玻璃微粒注射液），召回几乎不可避免；但企业常先于 FDA 与客户发现缺陷，裁量转移到时点——立即行动暴露最大财务与客户忠诚代价，形成两难；董事会 stakeholder responsiveness 期望（女性董事 community influencer / 慈善经验 / care orientation / 对延迟后果概率判断更高）→ H2: time-to-recall 缩短
- 两机制的层次一致（均在 board-tone 层），内容不同；DV 措辞内嵌边际（count=whether / time-to-recall=when）

**骨架**:
```
[Margin partition opener]
[Outcomes] differ in [contextual construct], which leads to variation in [if] and [when]
[actors] act. This distinction underlies our hypotheses, as we contend that [X] will have
a varying influence on [decisions] contingent upon [context].

[Margin 1: discretion over whether]
We begin with [low-stakes class of outcomes]. This type can be [hidden/not acted upon]
if the firm opts for such an approach. Consequently, we treat [DV 1 count] as a measurement
of [decision discretion] and not as [surface construct] per se.
[Paired examples proving discretion space exists: one acted + one not acted].
We theorize that [X] will be more likely to [act] for these [low-stakes] issues.
[Margin-specific mechanism bundle]. Taken together, these arguments bring us to:
H1: [X] is positively associated with [count of margin-1 acts].

[Margin 2: discretion over when]
We now transition to [high-stakes class] that have little discretion in [whether],
but nonetheless contain discretion in [when]. [Example(s) where stakes force action].
In both cases, the firm's decision is less about if and more about how quickly.
[Margin-specific mechanism bundle]. Combining these arguments leads us to:
H2: [X] is negatively associated with [time-to-act] for [high-stakes class].
```

**为什么有效**: DV 的措辞直接编码决策边际（count=whether；time=when），读者在假设句层面就看到两个不可互换的决策窗口；机制不出层次（都通过 board-set expectations），避免"同一机制万能化"与"多结果凑显著"两种指控。

**注意事项**:
- 情境构念必须在理论化之前（最好有制度/监管依据）确立"边际不同"——不能事后按结果分组编故事
- 每个边际必须证明裁量空间真实存在（本文用 paired 案例：一例照章召回、一例应召未召）
- 两个机制的层次必须一致（都在 board-tone 层），只是内容不同
- DV 操作化必须与边际对应（count 对 whether、awareness-to-initiation 时长对 when），否则边际拆分沦为修辞

**反模式**: 情境变量写成 moderation（"severity strengthens the effect"）却保留两个 DV；或两个边际共用同一段机制只换 DV 名。

**原文锚点**: "This distinction underlies our hypotheses, as we contend that adding female directors will have a varying influence on recall decisions contingent upon the severity of product defects."


### 变体 A：受众异质性 pivot 至调节假设（westphal_zajac_1998_symbolic_management 型）

**模板**:
> "While our discussion thus far has treated [stakeholders] as having homogeneous [preferences], [subgroup] represent an important [subset] of [stakeholders] who typically [hold systematically larger stakes]. One important implication of [their position] is that for dissatisfied [subgroup members], the option of 'exit' is somewhat more difficult and costly, hence leading to the greater exercise of 'voice'. [Given that constrained exit makes reform salient to them], it is not surprising that much of [the pressure for reform] has been generated by [subgroup]... this tendency should be diminished to the extent that [symbolic substitutes] are provided."

**来源**: westphal_zajac_1998_symbolic_management (ASQ), §2.4 P1

**原文锚定**:
> "One important implication of holding such large equity stakes is that for dissatisfied institutional investors, the option of 'exit' (i.e., selling the stock) is somewhat more difficult and costly, hence leading to the greater exercise of 'voice' (Hirschman, 1970; Jensen, 1989; Kim and Ocasio, 1995)."

**关键特征**:
- "While our discussion thus far has treated [actors] as homogeneous" 是零成本 pivot 句：主动承认前文简化假设，把"引入调节变量"从补丁升格为修正——与 C18 元框架功能等价（选择该 moderator 的理由即其位置特性）
- 用 exit/voice（Hirschman）给 moderator 提供独立理论依据：机构投资者因退出成本高而对治理信号更敏感——调节方向的预测力来自位置而非常识
- pivot 段直接生成一对平行交互假设（H3a/H4a 与 H3/H4 同构），保持假设族的 2×2 对称结构不因扩展而破碎

**适用**: 假设族需按受众/行动者异质性扩展的研究；调节变量是"谁在看"而非"什么条件"的受众类 moderator；系列假设需保持矩阵对称

**禁忌**: pivot 的异质性必须产生可论证的机制差异（退出成本→敏感性），只说"他们不同"不够；subgroup 的行为偏好需有文献锚定，不能按需要假设

**验证状态**: VERIFIED — expert_audit_override (user 2026-08-28: 单源足矣; paper_count=1)


## Pattern B: Mechanism-Matched Dual-Path → Shared Renewal Trunk（中介配对分流→共享重构主干，what_changes_after_women_enter_top_manage_2020 型）

**验证状态**: VERIFIED (expert_audit_override 2026-08-29: 用户点名喜爱本篇，单源足矣)

**适用场景**: 单一事件/构成 IV 理论上触发两个概念独立的中介机制，且两个机制各自通向一个不同的下游决策/结局（mediator–DV 配对），双路径共同指向同一更高阶重构主张。区别于"同一结局的多机制分解"与"同一构念双维度双轨"。

**与近邻模式区分**:
- vs `B2_dual_track`（Malik 2025）：B2 的双轨是**同一构念的两个维度**各自经不同机制产生行为效应；本模式双中介是**两个独立构念**，由单一 IV 同时触发
- vs `parallel_mediators_effect_decomposition_horizon`（Bamberger 2021）：后者平行中介汇于**同一近端结果**再做 direct/indirect 分解；本模式每个中介配对一个**不同 DV**，不做效应分解
- vs `shared_orientation_divergent_outcomes`（Kashmiri 2017）：后者是 trait→orientation→多结果的**单中介主干**；本模式无统一 orientation，两机制分立发展
- vs `2×2 Symmetric Matrix`：两 DV 风险-能见度画像不同质、不构成对称矩阵时用本模式

**骨架**:
```
[区分证成段]
Because [M1] and [M2] are conceptually distinct, we argue that they have
distinctive effects on [domain]. [区分三重证成: 定义维度对比 + 心理构成清单互斥
+ 已有文献同时检验两构念的差异化效应].

[结局配对证成段]
We focus concurrently on changes in [Y1] and changes in [Y2] as indicators
of shifts in [higher-order domain], for two reasons. [理由1: 双结局代表两种
不同战略决策且风险/能见度画像不同]. [理由2: 文献显示结局相对投入随前因认知而变].
These foundational insights lead us to theorize distinct dynamic trajectories
from [X] to [Y1] and [Y2], via shifts in [M2] and in [M1], respectively.

[配对机制分支 1]
[X] → [M1 位移] (H1/H2 各配 ≥2 条独立理由). [M1 的理论属性 ↔ Y1 的属性匹配论证]
→ [Y1 位移] (H6 型: the greater the change in [M1], the greater the subsequent
change in [Y1]).

[配对机制分支 2]
[X] → [M2 反向位移]. [M2 属性 ↔ Y2 属性匹配论证] → [Y2 反向位移] (H7 型).

[共享重构]
双路径共同指向 [更高阶重构主张: 从 A 途径转向 B 途径]——由总模型段+Figure 前置锁定.
```

**原文锚定**: "Because TMT change orientation and TMT risk-taking propensity are
conceptually distinct, we argue that they have distinctive effects on strategic
renewal. ... We focus concurrently on changes in M&A and changes in R&D as
indicators of shifts in renewal strategies ... These foundational insights lead
us to theorize distinct dynamic trajectories of strategic renewal from female
TMT appointment to changes in M&A and R&D, via shifts in TMT risk-taking
propensity and in TMT change orientation, respectively."

**为什么有效**:
- 'conceptually distinct → distinctive effects' 一句话完成双中介的合法性证成与分流的必要性——读者不会问 "why two mediators"
- 区分证成用外部文献互斥清单（某综述明示构念 A 不在构念 B 的心理属性清单内）+ 同文献差异化效应证据，比自说自话的界定更硬
- mediator–DV 配对论证让每个中介的属性（长期取向/保障需求）与对应结局的属性（可逆性/财务风险）逐项咬合，避免"同一中介万能化"与"多结局凑显著"两种指控
- 双路径汇于同一更高阶重构，使两条相反方向的预测（Y1↑, Y2↓）成为同一故事的证据组合而非论证不一致

**注意事项**:
- 两中介的概念区分必须在假设推导之前完成，且要有至少一条外部文献证据（互斥清单或同检验文献）
- 每个分支的 M→Y 论证必须重建 branch-specific why-chain——共享 antecedent 不等于共享机制
- 配对方向必须可证伪： ideally 每个中介对其"非配对"结局无预测（交叉零约束），实证章节应能检验
- 双路径的汇合点（更高阶重构）要在总模型段显式命名，不能只靠读者自行归纳

**反模式**:
- 为了假设编号对称让同一中介机械解释两个结局
- 双中介区分段缺失，直接并排推 H1/H2
- 两 DV 仅因数据可得而配对，无属性匹配论证
