# write-theory 语料库索引

本索引提供 `write-theory` skill 语料文件的快速导航和决策入口。

---

## 证据注册表（模式验证状态，选择阶段查询）

[`_evidence_registry.yaml`](_evidence_registry.yaml) 登记每个语料模式的来源论文与验证状态：

- **ROBUST**（5+ 论文、2+ 子领域）：可作默认推荐
- **VERIFIED**（3+ 论文）：可推荐，无需标注
- **EMERGING**（1–2 来源）：可迁移但未跨论文验证——推荐时必须标注"单源/双源模式"，不得写成默认做法
- **structural**（协议/综合/句式 voice）：非单一论文蒸馏的结构性语料（决策表、验证协议、教科书框架应用），登记在 registry 的 `unattributed_corpus` 节，**不参与** VERIFIED/ROBUST 论文计数——可直接使用，无需"单源"标注
- `source_tier: auxiliary` 的来源（写作工艺书，如 Booth、G&L）只登记出处，不计入 VERIFIED/ROBUST 的论文计数

**两步读取**（与 write-introduction 一致）：选择阶段读本索引 + `_evidence_registry.yaml`（过滤/标注模式状态）；渲染阶段才读对应 corpus 文件。`next_batch_targets` 节列出距 VERIFIED 还差几篇论文的模式——蒸馏新论文时优先命中这些目标。

---

## 快速决策："我该看哪个文件？"

| 你的研究类型 | 先读这个 | 再读这些 |
|-------------|---------|---------|
| 核心贡献是区分两个易混淆构念 | [`variants/A_construct_differentiation.md`](variants/A_construct_differentiation.md) | [`subprotocols/construct_differentiation_patterns.md`](subprotocols/construct_differentiation_patterns.md), [`sentences/construct_definition.md`](sentences/construct_definition.md) |
| 核心贡献是论证为何选择 focal DV（而非构念区分本身） | [`variants/A_construct_differentiation.md`](variants/A_construct_differentiation.md)（DV选择论证子变体） | [`subprotocols/construct_differentiation_patterns.md`](subprotocols/construct_differentiation_patterns.md), [`sentences/construct_definition.md`](sentences/construct_definition.md) |
| 研究对象与相关现象机制不同但需借用文献 | [`subprotocols/argumentation_patterns.md`](subprotocols/argumentation_patterns.md)（Simultaneously Recognize X but Leverage Y） | [`subprotocols/construct_differentiation_patterns.md`](subprotocols/construct_differentiation_patterns.md) |
| 核心贡献是解释 X 如何影响 Y 的因果机制 | [`variants/B_mechanism_elaboration.md`](variants/B_mechanism_elaboration.md) | [`sentences/mechanism_chain.md`](sentences/mechanism_chain.md), [`sentences/hypothesis_forms.md`](sentences/hypothesis_forms.md), [`subprotocols/hypothesis_derivation_patterns.md`](subprotocols/hypothesis_derivation_patterns.md) |
| BACKGROUND/文献背景承载双通道机制 + 阶段衰减，且**无正式编号假设** | [`subprotocols/hypothesis_derivation_patterns.md`](subprotocols/hypothesis_derivation_patterns.md)（Background-as-Theory Dual-Channel + Stage Attenuation；EMERGING / B8） | [`variants/B_mechanism_elaboration.md`](variants/B_mechanism_elaboration.md) B0；勿路由到必须产出 H 表的默认模板 |
| 同一 IV 通过两条对立路径（benefit vs cost）影响同一 DV | [`variants/B_mechanism_elaboration.md`](variants/B_mechanism_elaboration.md) + [`sentences/mechanism_chain.md`](sentences/mechanism_chain.md)（辩证对立双路径；含 selective-path moderation） | 按条件作用点选择双路径共同重配或单路径选择性调节；不要路由到“双 IV 维度”的 B2 |
| 用不同知识位置的访谈对象分别建立制度功能与战略解释 | [`sentences/mechanism_chain.md`](sentences/mechanism_chain.md)（多角色访谈三角化；EMERGING） | [`variants/E_moderation.md`](variants/E_moderation.md) E4（若访谈导出 contingency） |
| 同一 IV 有多个角色分离的并行中介，且 direct/indirect 路径方向冲突并跨时间窗口比较 | [`subprotocols/hypothesis_organization_patterns.md`](subprotocols/hypothesis_organization_patterns.md)（Role-Separated Parallel Mediators → Effect Decomposition → Horizon Test；EMERGING） | [`variants/B_mechanism_elaboration.md`](variants/B_mechanism_elaboration.md) |
| 单一事件/构成 IV 触发两个概念独立的中介，各配对一个不同下游决策，双机制分流后汇于同一更高阶重构主张 | [`subprotocols/hypothesis_organization_patterns.md`](subprotocols/hypothesis_organization_patterns.md)（Mechanism-Matched Dual-Path → Shared Renewal Trunk；VERIFIED / `post_2022_women_tmt_strategic_renewal`） | [`sentences/hypothesis_forms.md`](sentences/hypothesis_forms.md)（t-Staged Delta 假设形式） |
| 理论预期 X→Y 是曲线关系（如 inverted U-shape / U-shape） | [`subprotocols/hypothesis_derivation_patterns.md`](subprotocols/hypothesis_derivation_patterns.md)（Curvilinear Two-Phase Argumentation） | [`subprotocols/hypothesis_derivation_patterns.md`](subprotocols/hypothesis_derivation_patterns.md)（Width-Type Parallel） |
| 同一构念的两个维度对两种 DV 类型产生对称反向效应 | [`subprotocols/hypothesis_organization_patterns.md`](subprotocols/hypothesis_organization_patterns.md)（2×2 对称矩阵） | [`sentences/mechanism_chain.md`](sentences/mechanism_chain.md) |
| 两个条件对同一组互补 DV 维度产生镜像反向效应 | [`subprotocols/hypothesis_derivation_patterns.md`](subprotocols/hypothesis_derivation_patterns.md)（对称反向双轨） | [`subprotocols/hypothesis_organization_patterns.md`](subprotocols/hypothesis_organization_patterns.md)（2×2 交叉反向子变体） |
| 群体因成员各自误判他人观点而集体沉默（个体局部理性→集体非理性；pluralistic ignorance 类构念） | [`subprotocols/argumentation_patterns.md`](subprotocols/argumentation_patterns.md)（机制前提→情境放大 模式F / 同果近邻构念反号辨析 模式E；VERIFIED / `westphal_bednar_2005_asq`） | [`sentences/mechanism_chain.md`](sentences/mechanism_chain.md)（自增强循环命名句 B / 个体规则→集体困局 C）；[`sentences/hypothesis_forms.md`](sentences/hypothesis_forms.md)（被中介调节两段式 D） |
| 调节者需按「改变行动意愿」vs「改变行动机会/成本」两轴组织（同一主干机制的多个前因调节） | [`subprotocols/moderator_selection_frameworks.md`](subprotocols/moderator_selection_frameworks.md)（意愿×机会双路径 框架B；VERIFIED / `westphal_bednar_2005_asq`） | [`subprotocols/board_governance_boundary_condition.md`](subprotocols/board_governance_boundary_condition.md)（行动者子群双理由圈定 模式A） |
| 需要主动管理读者/文献中的竞争预测 | [`subprotocols/argumentation_patterns.md`](subprotocols/argumentation_patterns.md)（Preemptive Competing Account Management） | — |
| 文献默认受众 A 对行动正向，但 DV 由受众 B 定价（反直觉比较主效应；**勿升格为 G**） | [`subprotocols/argumentation_patterns.md`](subprotocols/argumentation_patterns.md)（Audience-Foil then Focal-Signal；VERIFIED / `chenganesanliu2009`） | [`sentences/acknowledgment_response.md`](sentences/acknowledgment_response.md) §5b；[`sentences/hypothesis_forms.md`](sentences/hypothesis_forms.md) Comparative Main Effect |
| 需要从一个领域向另一个领域扩展理论机制 | [`subprotocols/argumentation_patterns.md`](subprotocols/argumentation_patterns.md)（Extension Logic） | — |
| 同一构念的两个维度产生相反/互补预测 | [`subprotocols/B2_dual_track.md`](subprotocols/B2_dual_track.md) | [`sentences/mechanism_chain.md`](sentences/mechanism_chain.md)（双轨并行部分） |
| 核心贡献是多层次/多条件的假设体系 | [`variants/C_hypothesis_tree.md`](variants/C_hypothesis_tree.md) | [`sentences/moderation.md`](sentences/moderation.md) |
| 核心贡献是揭示动态过程和时间演化 | [`variants/D_process_theory.md`](variants/D_process_theory.md) | — |
| 核心贡献是识别 boundary condition / contingency | [`variants/E_moderation.md`](variants/E_moderation.md) | [`sentences/moderation.md`](sentences/moderation.md), [`subprotocols/E1_categorical_moderation.md`](subprotocols/E1_categorical_moderation.md), [`subprotocols/bilateral_argumentation_templates.md`](subprotocols/bilateral_argumentation_templates.md), [`subprotocols/hypothesis_derivation_patterns.md`](subprotocols/hypothesis_derivation_patterns.md), [`subprotocols/argumentation_patterns.md`](subprotocols/argumentation_patterns.md)（Competing Baseline Resolution） |
| 偏差信念改变反馈更新，且生存/约束阈值使决策目标与方向发生反转 | [`subprotocols/hypothesis_derivation_patterns.md`](subprotocols/hypothesis_derivation_patterns.md)（Belief Updating → Attention-Threshold Reversal；EMERGING） | [`variants/E_moderation.md`](variants/E_moderation.md), [`sentences/moderation.md`](sentences/moderation.md) |
| 领域默认机制推出方向 A，但新机制应推出相反方向 | [`subprotocols/hypothesis_derivation_patterns.md`](subprotocols/hypothesis_derivation_patterns.md)（Counterintuitive Direction-Reversal via Mechanism Substitution；EMERGING） | [`variants/B_mechanism_elaboration.md`](variants/B_mechanism_elaboration.md), [`sentences/mechanism_chain.md`](sentences/mechanism_chain.md) |
| 从有害机制链反推一般干预，并以自我关联/诊断性强化同一干预 | [`subprotocols/hypothesis_derivation_patterns.md`](subprotocols/hypothesis_derivation_patterns.md)（Mechanism-Targeted Intervention Escalation；EMERGING） | [`variants/E_moderation.md`](variants/E_moderation.md), [`sentences/moderation.md`](sentences/moderation.md) |
| 宏观事件激活平时可压抑的身份/差异，并需同时解释事件后持续性 | [`variants/E_moderation.md`](variants/E_moderation.md) E7（EMERGING） | [`sentences/moderation.md`](sentences/moderation.md) |
| 双刃剑估值机制净效应不定，需异号增强/阻碍行业权变（无 unconditional 主效应 H） | [`variants/E_moderation.md`](variants/E_moderation.md) E8（EMERGING） | [`hypothesis_organization_patterns.md`](subprotocols/hypothesis_organization_patterns.md)；[`sentences/moderation.md`](sentences/moderation.md) |
| IV 是特质/倾向（有默认表现型主效应），moderator 是特质相关 cue 激活对立表现型作用于同一 DV | [`variants/E_moderation.md`](variants/E_moderation.md) E11（EMERGING，单源） | [`subprotocols/hypothesis_organization_patterns.md`](subprotocols/hypothesis_organization_patterns.md)（Per-Stakeholder Paired）；[`sentences/moderation.md`](sentences/moderation.md)（Mitigation via Manifestation-Switch）；[`subprotocols/bilateral_argumentation_templates.md`](subprotocols/bilateral_argumentation_templates.md)（Cue-Activation Carve-Out）；[`sentences/mechanism_chain.md`](sentences/mechanism_chain.md)（Threat-Processing Cascade） |
| 三向交互 (X x W1 x W2) | [`variants/E_moderation.md`](variants/E_moderation.md) | [`sentences/moderation.md`](sentences/moderation.md) |
| 有中介的调节 (Moderated Mediation) | [`variants/E_moderation.md`](variants/E_moderation.md) | [`subprotocols/hypothesis_derivation_patterns.md`](subprotocols/hypothesis_derivation_patterns.md)（Indirect Moderation / Mediated Moderation Derivation） |
| 多调节器按层次/维度分类 | [`variants/E_moderation.md`](variants/E_moderation.md) | [`subprotocols/moderator_selection_frameworks.md`](subprotocols/moderator_selection_frameworks.md) |
| 4+ 调节变量按机制要素分组（威胁→动机 / 机会→能力） | [`variants/E_moderation.md`](variants/E_moderation.md) E9 | [`subprotocols/moderator_selection_frameworks.md`](subprotocols/moderator_selection_frameworks.md)（Willing-and-Able Dual-Axis；EMERGING） |
| 主效应机制由 push+pull 双通道收敛（主动施加 + 被动迎合） | [`variants/B_mechanism_elaboration.md`](variants/B_mechanism_elaboration.md) B0 | [`subprotocols/hypothesis_derivation_patterns.md`](subprotocols/hypothesis_derivation_patterns.md)（Dual-Channel Convergence；EMERGING） |
| 假设后解释为何不预测相邻对象/方向（效应选择性） | [`variants/E_moderation.md`](variants/E_moderation.md) E1 Step 6 扩展 | [`subprotocols/hypothesis_derivation_patterns.md`](subprotocols/hypothesis_derivation_patterns.md)（Why-Not Reverse Boundary Declaration；EMERGING） |
| 同一理论预测两个竞争响应，用 moderator 裁决 | [`variants/E_moderation.md`](variants/E_moderation.md) E4 节 | [`subprotocols/argumentation_patterns.md`](subprotocols/argumentation_patterns.md)（Preemptive Competing Account Management） |
| 曲线主效应 + 多个 moderators 同时调节曲线形状 | [`variants/E_moderation.md`](variants/E_moderation.md) E5 节 | [`subprotocols/hypothesis_derivation_patterns.md`](subprotocols/hypothesis_derivation_patterns.md)（Curvilinear Two-Phase + Width-Type Parallel） |
| 需要解释为什么选这些 moderators | [`subprotocols/moderator_selection_frameworks.md`](subprotocols/moderator_selection_frameworks.md) | — |
| 恰好两个 moderators，均由单一 new-voice/新成员整合机制证成（能力侧 vs 难度侧），并同构调节多条中介路径 | [`subprotocols/moderator_selection_frameworks.md`](subprotocols/moderator_selection_frameworks.md)（Newcomer Voice-Integration Axis；VERIFIED / `post_2022_women_tmt_strategic_renewal`） | [`sentences/moderation.md`](sentences/moderation.md) |
| 结构移除使内部监督收益丧失，需把同一丧失态映射到多 outcome，并用外部监督作部分替代衰减 | [`subprotocols/hypothesis_organization_patterns.md`](subprotocols/hypothesis_organization_patterns.md)（Mechanism-Loss Trunk → Multi-Outcome Tree；EMERGING / B9） | [`sentences/mechanism_chain.md`](sentences/mechanism_chain.md)；[`sentences/moderation.md`](sentences/moderation.md) |
| 需要组织多个并行调节假设 | [`subprotocols/hypothesis_organization_patterns.md`](subprotocols/hypothesis_organization_patterns.md) | [`subprotocols/arrangement_patterns.md`](subprotocols/arrangement_patterns.md) |
| 需要论证假设段落内部如何摆证据 | [`subprotocols/evidence_patterns.md`](subprotocols/evidence_patterns.md) | [`subprotocols/argumentation_patterns.md`](subprotocols/argumentation_patterns.md) |
| 需要组织段落内部的论点-论据-总结布局（Topic→Reasoning→Tokens→Wrap + 文献/理论/案例三类论据决策） | [`subprotocols/paragraph_layout.md`](subprotocols/paragraph_layout.md) | [`subprotocols/evidence_patterns.md`](subprotocols/evidence_patterns.md), [`sentences/mechanism_chain.md`](sentences/mechanism_chain.md)（段内逻辑布局原则） |
| 核心贡献是裁决两种对立理论的竞争预测 | [`variants/F_competing_hypotheses.md`](variants/F_competing_hypotheses.md) | [`sentences/hypothesis_forms.md`](sentences/hypothesis_forms.md) |
| 调节假设的 moderator 由 DV 官方严重度分级实现（裁量不可观测，事件属性作代理，H 强/弱异号对） | [`variants/E_moderation.md`](variants/E_moderation.md)（Event-Attribute Split Bilateral Moderation Pair 变体B；VERIFIED / `ball_2018`） | [`subprotocols/evidence_patterns.md`](subprotocols/evidence_patterns.md)（Interview Non-Event Warrant 配套实例化） |
| IV 是抽象构念但行业有制度性二分类（审批路径/监管身份）可作组间测量锚 | [`variants/E_moderation.md`](variants/E_moderation.md)（Institutional-Regime Construct Anchor 变体A；VERIFIED / `ball_2018`） | — |
| H1 前需先排除相邻反预测（同一 IV 的反方向机制，两步式：前提缺失 + 结构不经济） | [`subprotocols/argumentation_patterns.md`](subprotocols/argumentation_patterns.md)（Counter-Prediction Exclusion before H1 变体B；VERIFIED / `ball_2018`） | — |
| 两条机制路径同号同终点，收敛为单一方向性假设（不拆竞争假设） | [`variants/B_mechanism_elaboration.md`](variants/B_mechanism_elaboration.md)（Dual-Path Convergence 变体A；VERIFIED / `ball_2018`） | [`subprotocols/hypothesis_derivation_patterns.md`](subprotocols/hypothesis_derivation_patterns.md)（Dual-Channel Convergence；EMERGING） |
| 双边论证中"未发生行为"一侧无公共记录，需知情者访谈证据化 | [`subprotocols/evidence_patterns.md`](subprotocols/evidence_patterns.md)（Interview Non-Event Warrant 变体A；VERIFIED / `ball_2018`） | — |
| 上游治理主体（董事会/监管者）不直接决定 focal decision，需先定位其影响入口再理论化主体属性 | [`subprotocols/argumentation_patterns.md`](subprotocols/argumentation_patterns.md)（Decision-Rights Preamble → Indirect-Governance Chain；VERIFIED / `wowak_2020`） | [`subprotocols/evidence_patterns.md`](subprotocols/evidence_patterns.md)（Paired Opposite-Default Vignettes 配套轶事对） |
| 同一前因作用于多个结果，但各结果决策边际不同（是否 vs 多快），由客观情境分级（severity）分配角色与机制——**不是调节** | [`subprotocols/hypothesis_organization_patterns.md`](subprotocols/hypothesis_organization_patterns.md)（Context-Assigned Decision-Margin Split；VERIFIED / `wowak_2020`，core_candidate 观察项） | [`variants/E_moderation.md`](variants/E_moderation.md)（对照：severity 调节单条 timing 关系）；[`sentences/hypothesis_forms.md`](sentences/hypothesis_forms.md)（边际内嵌 DV 句式） |
| 对成熟经济学/理性选择理论做符号/制度再诠释，每个假设小节需以"默认解释→社会视角再诠释"交替对立开题 | [`variants/B_mechanism_elaboration.md`](variants/B_mechanism_elaboration.md)（Symbolic Alternating Reframe 变体B；VERIFIED / `westphal_zajac_1998`） | [`variants/B_mechanism_elaboration.md`](variants/B_mechanism_elaboration.md)（Hard/Soft Signal Measurement Reframe 变体C，配套测量本体重构） |
| 最强替代解释（语言属实/理性说服）需在假设层内判别排除：decoupling 子样本即"形式与事实不符仍获反应"的自然实验 | [`subprotocols/argumentation_patterns.md`](subprotocols/argumentation_patterns.md)（Decoupling Discriminating Test 变体C；VERIFIED / `westphal_zajac_1998`） | [`sentences/hypothesis_forms.md`](sentences/hypothesis_forms.md)（Implementation-Contingency 从句假设形式，VERIFIED / `westphal_zajac_1998`；配套 [`sentences/moderation.md`](sentences/moderation.md) Numbered Dual-DV Interaction） |
| 需用访谈证据证明裁量空间真实存在、且默认由上游主体设定（反向默认对偶轶事） | [`subprotocols/evidence_patterns.md`](subprotocols/evidence_patterns.md)（Paired Opposite-Default Interview Vignettes；VERIFIED / `wowak_2020`） | [`subprotocols/argumentation_patterns.md`](subprotocols/argumentation_patterns.md)（决策权前言配套） |
| 低严重度行为计数须重标为裁量度量而非结果质量度量（count-as-discretion relabeling） | [`meta/product_safety_construct_lexicon.md`](meta/product_safety_construct_lexicon.md)（召回计数的裁量重标；VERIFIED / `wowak_2020`） | [`sentences/hypothesis_forms.md`](sentences/hypothesis_forms.md)（边际内嵌 DV 假设句式） |

---

## 变体文件（Variants）

| 文件 | 构建类型 | 核心内容 | 假设结构 |
|------|---------|---------|---------|
| [`A_construct_differentiation.md`](variants/A_construct_differentiation.md) | 构念辨析型 | 构念界定策略、差异化维度、对比论证 | 构念区分 + 可选因果预测 |
| [`B_mechanism_elaboration.md`](variants/B_mechanism_elaboration.md) | 机制推演型 | B0 理论过程解释 / B1 正式中介；why chain 与测量分离 | B0 可仅主效应；B1 才要求中介 |
| [`C_hypothesis_tree.md`](variants/C_hypothesis_tree.md) | 假设树型 | 条件化分叉、树状展开、 moderator 引入时机 | 主效应 + 多调节 |
| [`D_process_theory.md`](variants/D_process_theory.md) | 质性过程理论型 | 阶段序列、过渡条件、时间标记 | Proposition 为主 |
| [`E_moderation.md`](variants/E_moderation.md) | 调节效应型 | E1-E9 协议：同层/跨层调节、嵌入边界、竞争裁决、曲线多调节、序列嵌套调节、宏观事件激活与持续性、双刃剑异号增强/阻碍权变、**双侧镜像调节（同一构念 rival/target 侧镜像预测，DesJardine 2025，EMERGING）**、**E11 特质激活双表现型 cue 切换（trait→默认表现型主效应 + cue 激活对立表现型，Ridge 2024，EMERGING）** | 主效应 + 调节（含复杂交互、条件间接效应、无主效应异号权变、双侧镜像调节对、cue 切换缓解交互） |
| [`F_competing_hypotheses.md`](variants/F_competing_hypotheses.md) | 竞争假设型 | 对立预测呈现、非传统收敛信号、 net effect 论证 | 竞争假设对 |
| [`G_dialectical_opposition.md`](variants/G_dialectical_opposition.md) | 辩证对立型 | 双受众对称机制、dialectical turn 标记、theory-based reconciliation | 对立预测（方向反转） |

---

## 子协议（Subprotocols）

| 文件 | 父变体 | 适用场景 |
|------|--------|---------|
| [`construct_differentiation_patterns.md`](subprotocols/construct_differentiation_patterns.md) | A 构念辨析型 | 构念辨析的表格化定义、差异-借用过渡（Simultaneously Recognize X but Leverage Y）、**Invariant Discriminant Spine（不变判别主轴，Ridge 2024，EMERGING）** |
| [`B2_dual_track.md`](subprotocols/B2_dual_track.md) | B 机制推演型 | 同一构念两个维度产生相反预测（损失规避 vs 长期聚焦） |
| [`E1_categorical_moderation.md`](subprotocols/E1_categorical_moderation.md) | E 调节效应型 | Moderator 为分类变量（分组调节） |
| [`argumentation_patterns.md`](subprotocols/argumentation_patterns.md) | 跨类型 | **T2→T3 过渡段/非常规论证动作**：竞争解释管理（Preemptive Competing Account Management）、Extension Logic、双理论两阶段机制、行业情境限定、双机制汇聚、最小对对比 vignette、**Audience-Foil then Focal-Signal 单比较 H（chenganesanliu2009，VERIFIED；勿升格为 G）**。段落级假设推导骨架（Anchor→Mechanism→Warrant→Prediction）已归 `hypothesis_derivation_patterns.md`，间接调节论证亦在该文件 |
| [`hypothesis_derivation_patterns.md`](subprotocols/hypothesis_derivation_patterns.md) | 跨类型 | 假设推导段落的心脏模板：Anchor→Mechanism→Warrant→Prediction 完整序列，含宽度型并行机制、对称反向双轨、曲线关系双阶段论证、默认机制替换的方向反转、机制靶向干预递进 |
| [`reasoning_soundness_protocol.md`](subprotocols/reasoning_soundness_protocol.md) | 跨类型 | 论证可靠性（soundness）协议：前提三分法 [D]/[S]/[E] + 最弱环节防守（含 Booth warrant 五测试）+ 机制必要性门控（三问）+ 反例压力测试（六类 warrant 攻击面 + 第四种处置"承认但不回应"）+ warrant 明言/隐去表达纪律（Booth Ch8）；hypothesis_derivation_patterns 的 soundness 镜像，Phase 3 成稿后与 Phase 4 审计 4 使用 |
| [`arrangement_patterns.md`](subprotocols/arrangement_patterns.md) | 跨类型 | 论点-论据安排模式（Warrant-Embedded / Evidence-Contrast / Cumulative / Parallel） |
| [`evidence_patterns.md`](subprotocols/evidence_patterns.md) | 跨类型 | 证据类型、证据功能、文献引用三要素句式 |
| [`hypothesis_organization_patterns.md`](subprotocols/hypothesis_organization_patterns.md) | 跨类型 | 复杂假设体系的段落级组织（common trunk / dual branch / baseline→moderation / 2×2 对称矩阵 / 角色分离并行中介→效应分解→时间检验 / **机制丧失→多结果树→外部部分替代** / **Per-Stakeholder Paired (Main + Cue-Moderation) Parallel**，EMERGING） |
| [`bilateral_argumentation_templates.md`](subprotocols/bilateral_argumentation_templates.md) | E 调节效应型 | 调节假设的 high/low 双边论证句法；**Cue-Activation Carve-Out（硬约束 #11 例外：cue/activation moderator 的 low 态=主效应默认基线时，双边覆盖由主效应基线 + high 态机制论证满足）** |
| [`moderator_selection_frameworks.md`](subprotocols/moderator_selection_frameworks.md) | E 调节效应型 / C 假设树型 | 多 moderator 选择元框架 |
| [`intra_tmt_persuasion.md`](subprotocols/intra_tmt_persuasion.md) | E 调节效应型 / C 假设树型 | 下级高管如何通过信心启发式劝说上级决策者（含权力放大→三向交互） |
| [`board_governance_boundary_condition.md`](subprotocols/board_governance_boundary_condition.md) | E 调节效应型 | 董事会治理作为**放大型**边界条件（perverse pressure logic） |
| [`paragraph_layout.md`](subprotocols/paragraph_layout.md) | 跨类型（段内） | **段内**论点-论据-总结布局：Topic→Reasoning→Tokens→Wrap 四段位 + 文献/理论/案例三类论据决策矩阵 + 段内 12 项诊断清单（Dunleavy 段位病理 + IU coherence） |

---

## 句式语料（Sentences）

| 文件 | 功能 | 覆盖骨架 |
|------|------|---------|
| [`construct_definition.md`](sentences/construct_definition.md) | 构念界定 | 定义策略、scope conditions、lineage、adjacent construct 区分、辩论并置型构念界定 |
| [`mechanism_chain.md`](sentences/mechanism_chain.md) | 机制推演 | why chain 连接词、单步/两步/双轨/竞争/多理论/OM三三制/双刃剑/双中介并行/双DV并行/多层收窄型/替代机制排除/Ability-Motivation 框架/Iron Triangle三边机制/双视角对比框架整合/三层嵌套理论演进/Rhetorical-Question Pivot/联合必要性门控逻辑/**辩证对立双路径(habel2016)/Focus Group定性嵌入(habel2016，含多角色访谈三角化)/成本-收益计算机制链(chung2022)/威胁处理级联(ridge2024)** |
| [`cost_benefit_calculus.md`](sentences/cost_benefit_calculus.md) | 成本-收益机制 voice | 感知高收益 + 感知低成本 + 综合收敛 + 上下级激励差异对比 |
| [`moderation.md`](sentences/moderation.md) | 调节机制 | 机制修改论证、假设模板、修辞问句开场、Ability-Motivation 双路径调节、共享调节器反向调节、多调节器同向设计、双边论证调节推演、注意力基础观调节论证、不对称调节、**董事会放大型边界条件(chung2022)**、**Mitigation via Manifestation-Switch 缓解交互(ridge2024)** |
| [`hypothesis_forms.md`](sentences/hypothesis_forms.md) | 假设形式 | 各类假设的标准句法（主效应、**比较型主效应 A more negatively related than B（chenganesanliu2009，VERIFIED）**、中介、调节、三向交互、有中介的调节、配对假设a/b格式、条件假设Given格式） |
| [`acknowledgment_response.md`](sentences/acknowledgment_response.md) | 异议处置 voice | 承认与回应句式（Booth Ch9）：四类异议（替代解释/反例/证据局限/定义分歧）× 承认/回应标记词权重表 + 回应强度三级 + 承认但不回应三姿态；§5 Rogerian 四步对话结构（G&L 2017，高威胁异议的段落级降防御序列）；**§5b Audience-Foil Pivot 异质受众切换句（chenganesanliu2009，VERIFIED）**；与 reasoning_soundness_protocol §4 配套 |
| [`closure.md`](sentences/closure.md) | 收束/过渡 | **注意：管理学不要求独立 Closure 段。** 局部收束信号（"Therefore, we hypothesize:"）、段落收束→假设过渡（按论证类型）、**H1 收敛信号强制提醒** |
| [`leitmotif-section-opener.md`](sentences/leitmotif-section-opener.md) | 段首回扣句 | 多假设共享同一核心构念时的段首回扣句（leitmotif）；SKILL.md 措辞润色表"主导动机串联"句位查此文件 |

---

## 元数据文件（Meta）

| 文件 | 用途 |
|------|------|
| [`meta/routing_table.md`](meta/routing_table.md) | Introduction → Theory 快速路由表。根据 Gap 类型、Tension 模板、Makadok 维度推荐 Theory 变体 |
| [`meta/alignment_protocol.md`](meta/alignment_protocol.md) | 跨 Section 对齐检查协议（Introduction ↔ Theory ↔ Methods ↔ Results） |
| [`meta/product_safety_construct_lexicon.md`](meta/product_safety_construct_lexicon.md) | 产品安全、产品伤害危机、召回发生/时机/策略/严重度的构念边界与专业表达；写产品召回论文时用于术语校准 |

---

## 与 write-introduction 的交叉引用

| Introduction Tension | 推荐 Theory Variant | 说明 |
|---------------------|---------------------|------|
| `15-practical-puzzle` | **E 调节效应型** | 实践谜题 → "在什么条件下传统智慧成立/失效" |
| `14-debate-unresolved` | **E 调节效应型** 或 **C 假设树型** | 文献辩论 → "矛盾发现是因为忽略了 moderator" |
| `07-same-policy-opposite-effects` | **E 调节效应型** | 同一政策相反效应 → baseline 即交互假设（H1a+H1b），4 个 moderator 理论论证 |
| `01-despite-progress-unaddressed` | **B 机制推演型** | 遗漏解释 → 补足 why chain；仅当 M 被概念化且可检验时进入 B1 中介 |
| `02-implicit-assumption-wrong` | **B 机制推演型** | 假设错误 → 替换机制 |
| `03-structural-blindspot` | **B 机制推演型** | 系统遗漏 → 补充被忽略的机制路径 |
| `05-construct-confusion` | **A 构念辨析型** | 构念混淆 → 区分后产生不同预测 |
| `04-reality-contradicts-consensus` | **F 竞争假设型** 或 **A 构念辨析型** | 理论矛盾 → 竞争预测裁决或新构念整合 |
| `06-theoretical-imbalance` | **F 竞争假设型** | 理论不平衡 → 竞争预测 |
| `08-cost-vs-benefit` | **B 机制推演型** 或 **E 调节效应型** | 成本-收益矛盾 → 机制解释为何矛盾 或 边界条件解释何时哪个主导 |
| `16-threefold-gap` | **B 机制推演型** | 跨学科结构化 gap → 从母学科导入机制到目标学科 |

完整路由表见 [`meta/routing_table.md`](meta/routing_table.md)。

---

## 反模式速查

| 骨架 | 核心反模式 |
|------|-----------|
| 常识谚语作为机制 | 某个推理步骤用谚语/常识/folk wisdom（"don't fix something not broken"）替代理论文献支撑。实证风险极高——以此模式论证的假设在 shipilov_greve_rowley2019 中被反转 | 
| OM "三三制" | 三个原因概念重叠；子机制与主效应不对应；某原因仅基于常识 |
| 多理论整合 | 三理论沦为 citation list；理论间逻辑重叠；引入顺序混乱 |
| "双刃剑" | 好处面篇幅远大于坏处面；A vs B 区分不清；DV 定位模糊 |
| 双 DV 并行机制 | 两个 DV 由同一机制链接；第二条路径用 "Similarly" 开头；篇幅极端不对称 |
| 共享调节器反向调节 | 两个调节假设方向相同；调节论证只有一条路径充分解释；两条路径机制区分不清 |
| E3 三向交互 | W2 引入缺乏理论依据；未建立第一层交互；假设未说明条件化模式 |
| E4 有中介的调节 | 未建立基础中介链；未指明调节路径环节；假设形式化错误 |
| E5 多层调节器分类 | 分层缺乏理论依据；同层调节器过多（>3）；层级逻辑混用 |
| C 假设树型 假设间缺少逻辑递进 | 假设树型 4+ 假设后各假设独立无递进关系——理论碎片化。注意：管理学标准不要求独立 Closure 段，但每个假设推导必须有 "Therefore" 局部收束 |

完整反模式见各变体/语料文件中的 **反模式** 小节。
