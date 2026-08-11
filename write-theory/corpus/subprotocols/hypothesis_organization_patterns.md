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

> 检索辅助（2026-08-09 P0 补建）。状态列空白 = 正文未标注验证状态（旧 Pattern）。状态词表：通过（N/5 复现）> 通过（双篇/专家审计）> 通过（单篇）> 待第二篇交叉验证 > 可选变体。完整骨架、适用条件与诚实边界见下方变体正文。

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
pattern_id: temporal_dual_role_same_variable
build_type: 机制推演型 / 边界条件型
source_papers: ["Thirumalai_Sinha_2011_MS"]
confidence: low
status: needs_validation
story_fidelity: section_variant
-->

## Pattern: Temporal Dual-Role — Same Variable as Ex Ante Antecedent × Ex Post Buffer

**适用场景**: 同一企业特征变量在时间线上扮演**符号相反的双重角色**——ex ante 它是现象的前因（提高事件发生概率，有害），ex post 它是事件的缓冲（减轻事件后果，有益）；两个角色分别进入两套独立假设（不同 DV、不同模型），由 Discussion 整合为 trade-off。

**结构**: Consequence block（X 作为 buffer 调节 event→performance，H_buffer）→ Antecedent block（X 作为 IV 预测 event likelihood，H_driver）→ Discussion trade-off 整合（两角色符号相反 → 最优水平权衡）。

**范文来源**: Thirumalai and Sinha (2011), *Management Science*（product scope：H2 中作 buffer——更多 scope → 召回的市场惩罚更轻；H7 中作 driver——更多 scope → 聚焦稀释 → 召回可能性更高；Discussion 整合为 product diversification trade-off："firms need to find an appropriate level of product diversification in order to minimize the trade-off"）。

**骨架**:
```text
[Consequence block — X as buffer]
Firms with higher [X] can fall back on [alternative resources/options] when [event] occurs,
ceteris paribus; market confidence in recovery is stronger.
H[buffer]: The [negative consequence] of [event] is less severe for firms with greater [X].

[Antecedent block — X as driver]
However, greater [X] lowers [focus/attention] on each [unit].
Given resource constraints, firms with higher [X] are drawn thin in their ability to
[design/produce/monitor] individual [units]; the likelihood of errors is greater.
H[driver]: The greater the [X], the greater the likelihood of [event].

[Discussion trade-off integration — 义务]
This indicates the presence of a trade-off as [X] increases—between [benefit of high X:
market coverage + attenuated event penalties] on one hand, and [cost of high X: decreased
focus + increased event likelihood] on the other hand. Firms need to find an appropriate
level of [X] to minimize the trade-off.
```

**为什么有效**:
- 同一变量服务两个研究问题（后果异质性 + 前因异质性），在变量层面建立论文统一性——审稿人不会问"为什么后果模型和前因模型都有 X"，因为双重角色本身就是理论陈述。
- 符号相反的角色（有益 buffer × 有害 driver）自动生成 Discussion 的 trade-off 框架——"最优水平"问题是实践含义的天然载体。
- 与双 DV 设计（同一 IV 对 Y1/Y2）不同：本模式的两个假设位于**不同时间位置**（事件发生前 vs 事件发生后），可进不同模型、不同样本而不产生共线性或概念重叠。

**与近邻模式区分**:
- vs B2 双轨并行（malik2025）：B2 是同一构念的**两个维度**（current/prospective wealth）对同一 DV；本模式是**同一变量**对两个时间位置的不同结果。
- vs Dual-Edged Trunk（castellaneta2017）：双刃是同一时点上异号权变（enhancing/hindering moderators 共享 trunk）；本模式是时间分离的双重角色（antecedent vs consequence-side），无双刃 trunk、无交互假设。
- vs F 竞争假设（wowak2025）：F 是两个理论对同一关系的对立预测、读者裁判；本模式无理论对立——两个角色都被假设且都被支持，张力在规范含义（如何权衡）而非理论真伪。

**注意事项**:
- 两个角色的假设必须分属**不同的实证模型**（本文：H2 在 event-study CAR 横截面回归，H7 在 conditional FE negative binomial panel）——同一模型内同变量既是 IV 又是 moderator 会导致解释混乱。
- Discussion 的 trade-off 整合是**义务不是选项**——若两个假设分别支持却不整合，读者无法回答"那企业到底该不该扩大 X"。
- 双重角色的两个机制必须有独立理论依据（本文：buffer 角色引 Girotra et al. 2007 产品替代逻辑；driver 角色引 Skinner 1974 focused factory 文献），不可共享同一段推导。
- 符号相反是本质特征——若两个角色同向（如 X 既减少事件又减轻惩罚），则无 trade-off，退化为普通的多重好处论证，不适用本模式。

**反模式**:
- 把同一变量塞进两个假设却不承认角色差异（"we also examine X as a moderator"——事后添加感，违反 hb_no_ad_hoc_moderator 精神）。
- Discussion 只报告两个支持的假设而不整合 trade-off——留给读者"所以最优 X 是多少"的悬空问题。
- 前因角色借用后果角色的机制（如用"市场信心"解释事件发生）——两个角色的机制必须各自植根于对应时间位置的文献。

---

<!--
pattern_id: competing_theories_sectioned_horse_race
build_type: 理论对垒型 / 假设组织型
source_papers: ["Haunschild_Rhee_2004_MS"]
confidence: low
status: needs_validation
-->

## Pattern: Competing-Theories Sectioned Architecture — Mirrored Rival Subsections × Sequential Competing Hypotheses

**适用场景**: Incommensurability × **R1（X 分类）为主、经验赛马为 staging** 的理论节组织——先把伞形 X 拆成理论上优先的 X₁/X₂（如 volition：自愿 vs 非自愿），再让两个理论阵营对**哪一类 X 成员更能促进 Y** 给出方向相反的预测；Resolution Operator 是 X-side differentiation，分节竞争假设是分类之后的裁决装置（不是 Lee–Park 式 R3 共存调度）。需要把冲突从"提到有争议"升级为"正式赛马"。

**结构**: 共享 RQ 总起（"[Literature] provide[s] conflicting answers to this question. Theories of [camp A] suggest... Theories of [camp B] suggest..."）→ 镜像小节 A（steelman 阵营 A：文献 + 机制链 → 收束句 → H[N]）→ 镜像小节 B（steelman 阵营 B：同构推导 → 同一收束句 → H[N+1]，方向与 H[N] 互斥）→ 机制子假设（H[N]A：为胜方机制提供过程证据的可观察蕴含）→ 经验裁决 → Discussion 解释败方机制为何在此情境失效。

**范文来源**: Haunschild and Rhee (2004), *Management Science*（volition 阵营 [autonomy→commitment→深度学习] vs attention 阵营 [mandate→salience→克服惯性]；§Voluntary Learning → H2 "Voluntary recalls will lower the subsequent recall rate"，§Involuntary Learning → H3 "Involuntary recalls will lower the subsequent recall rate"，两小节以完全相同的收束句 "According to these arguments, then, ... This leads to the following hypothesis." 收束；H2A 检验浅学习过程作为机制证据；结果 H2 胜 H3 负）。

**骨架**:
```text
[Shared RQ + conflicting answers]
What is the role of [property P] in [outcome]? [Literature] provide[s] conflicting answers
to this question. Theories of [camp A] suggest [actor] will [benefit more from X1] ([citations]).
Theories of [camp B] suggest that they will [benefit more from X2] ([citations]).
In the following sections, we outline these competing theories and hypotheses.

[Subsection A — steelman camp A]
[Strongest-form derivation: citations + mechanism chain for why X1 → more Y]
According to these arguments, then, [mechanism summary] will result in [outcome].
This leads to the following hypothesis.
HYPOTHESIS [N]. [X1] will [direction] the [Y].

[Subsection B — steelman camp B, mirrored structure]
[Strongest-form derivation; premise defense via named case / mini-analysis where load-bearing]
According to these arguments, then, [mechanism summary] will result in [outcome].
This leads to the following hypothesis.
HYPOTHESIS [N+1]. [X2] will [direction] the [Y].

[Mechanism sub-hypothesis — observable implication of camp A's process]
If this is true, then we should see evidence for [process trace].
HYPOTHESIS [N]A. [X2] will result in [shallower/weaker process indicator] than [X1].

[Adjudication + Discussion]
[One wins, one loses] → Discussion explains why the losing mechanism is weaker in this context.
```

**为什么有效**:
- 镜像小节结构**强迫**双方获得同等篇幅与推导深度——steelman 义务由结构保证，而非依赖作者自律；审稿人无法指控稻草人。
- 互斥方向假设把理论冲突转化为一次 crucial test：经验结果直接更新两派理论的相对可信度，贡献是裁决而非"又一个调节效应"。
- 镜像收束句（两小节逐字相同）向读者发送对称信号，降低认知负荷。

**与近邻模式区分**:
- vs Audience-Role Dichotomy（pontikes2012）：受众对立双方**同时成立**（H1a/H1b 负 × H2a/H2b 正都被假设且都被支持）；本模式双方**互斥**，经验上只有一方获胜。
- vs Symmetric Opposing Dual-Track（zhao-ding）：双 track 作用于同一 DV 的两个互补维度；本模式是同一 DV 上的方向互斥。
- vs 竞争假设字母对（wowak2025, hypothesis_forms.md）：H1a/H1b 共享编号、通常在相邻段落快速对峙；本模式用序数编号（H2/H3）并各占独立小节配完整 steelman——正式赛马架构。
- vs equivocal nondirectional（kalaignanam2013）：模糊双边论证以非方向性假设**回避**裁决；本模式以互斥方向假设**强制**裁决。

**注意事项**:
- Formal lock 义务（Incommensurability routing Stage B）：进入假设推导前必须锁定具体 X、Y、unit/level、horizon、estimand——只允许机制阵营/类型变化（本文：X=前三年自愿/非自愿召回，Y=年度严重召回数，unit=automaker-year，estimand=conditional FE 负二项系数）。
- 败方机制不得抛弃：Discussion 必须解释它为何在此情境更弱（本文：强制召回诱发防御性浅反应——H2A 的报告页数与问题解决率证据承担了此解释）。
- 承重前提的防御义务：阵营 B 的显著性前提（"非自愿召回更引人注目"）用原创小型分析（新闻计数 χ² 检验）支撑；情境例外异议（"安全问题不会有惯性"）用具名案例（Firestone/Ford）反驳——两者见 evidence_patterns.md 对应模式。
- 镜像收束句必须逐字相同才有标记功能；近义改写会削弱对称信号。

**反模式**:
- 只写 "we test competing hypotheses" 却不给双方各建小节——退化为单薄字母对，steelman 不足。
- 一小节三页、另一小节一段——结构偏袒比公开选边更损害可信度。
- 宣布胜者后不解释败方机制为何失效——读者无法完成理论更新，裁决退化为"碰巧显著"。

---

<!--
pattern_id: sibling_ivs_mechanism_division_shared_buffer
build_type: 构念辨析型 → 机制推演型 → 边界条件型
source_papers: ["Li_Bapuji_Talluri_Singh_Venkataraman_2026_POM"]
confidence: low
status: needs_validation
related: B2_dual_track（同构念异号维度）；dual_mechanism_same_direction（单 IV 双机制）；geometric_sibling_construct_minimal_pair（可分证明）
-->

## Pattern: Sibling IVs — Mechanism Division + Shared Buffer Moderator

**适用场景**: 伞形构念下两个**兄弟 IV**（如 distance vs dispersion）经 Intro/T1 辨析后，各自绑定**不同主导机制**，对**同一 DV、同向**立主效应假设；再用一个共享缓冲调节器（如 vertical integration）对称削弱两条轨道（H3a/H3b）。

**结构**:
1. T1 可分证明（几何最小对或定义对）
2. Track A：IV_A → mechanism_A → Y（H1）
3. Track B：IV_B → mechanism_B → Y（H2；同向）
4. Shared buffer W attenuates both tracks（H3a/H3b）

**范文来源**: Li et al. (2026), POM（distance→monitoring→quality risk；dispersion→coordination→quality risk；VI weakens both — H3b 实证相反，属 Results 诚实解释，不改变 Theory 组织骨架）

**骨架**:
```text
[Division preamble]
We theorize that [umbrella] is positively related to [Y] because it heightens
[monitoring and coordination] challenges. However, [IV_A] and [IV_B] trigger
distinct aspects of these challenges. Specifically, [IV_A] increases [mechanism_A].
In contrast, [IV_B] exacerbates [mechanism_B]. Thus [IV_A] and [IV_B] increase [Y]
through different mechanisms. Further, [W] can mitigate both challenges.

[Track A — §]
We posit that [IV_A] increases [Y] by raising [mechanism_A challenges] ([citations]).
[Why-chain for mechanism_A…]
H1: [IV_A] is positively related to [Y].

[Track B — §]
Although [IV_B] may also pose [secondary challenge], we posit that it primarily
creates [Y] by increasing [mechanism_B costs] ([citations]).
[Why-chain for mechanism_B…]
H2: [IV_B] is positively related to [Y].

[Shared buffer — §]
We argue that [W] can mitigate the [mechanism_A and mechanism_B] challenges caused
by [IV_A] and [IV_B] for two reasons.
First, [W] reduces [information asymmetry / monitoring friction] associated with [IV_A]…
Second, [W] eases [coordination / conflict] across [IV_B]…
H3a: [W] weakens the relationship between [IV_A] and [Y].
H3b: [W] weakens the relationship between [IV_B] and [Y].
```

**为什么有效**:
- 机制分工把"可分构念"兑现为可检验的不同路径，避免审稿人说"只是两个相关控制变量"
- 同向双主效应 + 共享缓冲，比 B2 异号轨道更适合运营/供应链风险构念（两维度都"有害"）
- H3a/H3b 对称编号强制 Theory 对两条机制都给出缓冲逻辑，不能只调一条轨道

**与近邻模式区分**:
- vs B2（Malik）：B2 = **同一构念两维度**，常异号/异行为；本模式 = **兄弟 IV**，同向同 DV
- vs `dual_mechanism_same_direction`（Ball / li_bapuji_talluri_singh_narayanan_2026_jscm）：单 IV 经两条中介汇聚到一个 H；本模式是**两个 IV、两个 H**，每条一机制
- vs `dual_mechanism_convergent_moderation`（li_bapuji_talluri_singh_narayanan_2026_jscm）：一个 moderator 经双机制通道收敛；本模式是**一个 W 分别缓冲两条已分工的轨道**（对称 H3a/H3b），不是 moderator×mechanism 矩阵
- vs `geometric_sibling_construct_minimal_pair`：本模式的前置可分装置，不替代机制节

**注意事项**:
- Track A/B 的主导机制必须概念独立；次要机制可承认（"Although dispersion may also pose monitoring challenges..."）但必须标明 **primarily**
- 共享缓冲的两理由应分别对接 mechanism_A 与 mechanism_B，禁止用同一句空话覆盖两条轨道
- 实证若一条主效应 null 或调节反向（li_venkataraman_2026_pom: H1 null；H3b contrary），Theory 骨架仍成立——用 Results R6 变体诚实解释，不要回改 Theory 组织

**反模式**:
- 两轨道写相同机制只换 IV 名——机制分工失效，退化为相关控制变量堆砌
- 只立 H3 对一条轨道、另一条口头带过——破坏共享缓冲对称
- 跳过 T1 可分证明直接双轨——审稿人仍可说 A/B 不可识别

---