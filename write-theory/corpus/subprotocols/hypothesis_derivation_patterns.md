# Hypothesis Derivation Patterns

**核心定位**：假设推导段落（Hypothesis Derivation）是 Theory 部分的心脏。本文件集中管理“从理论到假设”的段落级推理模板：如何建立 Anchor、构造 Mechanism Move、安放 Warrant、收敛到 Prediction，以及段内逻辑推进的连接词布局。

> 使用原则：本文件不是收集“某种理论说什么”，而是收集“如何让一个假设从理论前提中自然生长出来”的论证组织方式。机制内容必须替换为用户自己的研究材料；骨架和连接策略可以直接复用。

> **导航 TOC**（本文件 1200+ 行 / 30 节，按需跳转，不要线性通读）。按推导类型分组；括注为锚定范文。职责边界见 `argumentation_patterns.md` 文件头（本文件=段落级骨架；该文件=T2→T3 过渡/非常规动作）。

| 组 | Pattern（行号） |
|----|----------------|
| **基础序列**（主效应段落骨架） | Anchor→Mechanism→Warrant→Prediction (L244) · Theory-Driven Anchor + Puzzle Turn（Singh&Grewal 2023）(L286) · Multi-Mechanism Trunk（Shen 2022）(L326) |
| **主效应推导**（单 IV→DV 变体） | Audience-Role Dichotomy + Mirrored Hypotheses（Pontikes 2012）(L27) · Sign-Flipping Boundary Condition（Pontikes 2012）(L78) · Three-Condition Framework for Information-Based Herding（Shi&Grewal 2021）(L117) · Width-Type Parallel Mechanism（2-3 独立理由）(L753) · Symmetric Opposing Dual-Track Mechanism（Zhao-Ding&Gaba）(L800) · Counterintuitive Anchor + Three Parallel Psychological Threats（Keeves 2017）(L494) · Parallel Dual-Source Antecedents Converging on One Mediator（Keeves 2017）(L532) · Emotion Action Tendency→Interpersonal Harm（Keeves 2017）(L567) · Cross-Disciplinary Theoretical Lens（Malshe&Agarwal 2015）(L603) · Four-Reason Parallel Mechanism Derivation（Malshe&Agarwal 2015）(L637) · Three Parallel Single-Step Mechanisms（Darby 2023）(L945) · Two-Levers Theory Progression（Darby 2026）(L980) · Embedded Prose Predictions in Conceptual Framework (L1011) |
| **调节推导**（moderation 段落） | Bilateral Moderation Derivation / high/low 双边论证（Shen 2022）(L374) · Indirect Moderation / Mediated Moderation Derivation（Singh&Grewal 2023）(L417) · Cumulative Moderation Build-Up（Singh&Grewal 2023）(L456) · Curvilinear Relationship — Two-Phase Argumentation（Cui 2026）(L838) · Additive Opposing Components → Inverted U（Fini 2017）(L991) · Sequential Nested Moderation（Chung/Low/Rust 2022）(L881) · Intangible Asset Real Options + Financial Constraint Distal Moderation（Malshe&Agarwal 2015）(L677) |
| **辩证 / 反转 / 时序不对称** | Dual-Logic Integration — Input vs Efficiency + Inverted U（Zhou 2017）(L189) · Institutional Shock as Theory Hook（Shi&Grewal 2021）(L157) · Counterintuitive Direction-Reversal via Mechanism Substitution (L1061) · Mismatch Subtype Refinement Hypothesis（主效应后递进）(L1096) · Developmental Reversal of Reciprocal-Causation Asymmetry（pollock2015 H1a/H1b）(L1143) · Differential Persistence / Lagged-DV Moderation（pollock2015 H2）(L1211) |
| **机制靶向干预** | Counterintuitive Direction-Reversal via Mechanism Substitution（Ilicic–Brennan 2026） · Mechanism-Targeted Intervention Escalation（Ilicic–Brennan 2026） |
| **元规则**（非 pattern，段落布局与文件关系） | 段内逻辑布局原则（连接词/段落长度/Warrant 摆放）(L705) · 与相邻语料文件的关系（validity vs soundness 分工）(L733) |

---

<!--
pattern_id: audience_role_dichotomy_mirrored_hypotheses
build_type: 构念辨析型 / 二元机制推演型
source_papers: ["Pontikes_2012_ASQ"]
confidence: high
status: ready_for_corpus
-->


## 变体速查表

> 检索辅助（2026-08-09 P0 补建）。状态列空白 = 正文未标注验证状态（旧 Pattern）。状态词表：通过（N/5 复现）> 通过（双篇/专家审计）> 通过（单篇）> 待第二篇交叉验证 > 可选变体。完整骨架、适用条件与诚实边界见下方变体正文。

| # | 变体 | 家族 | 适用场景 | 状态 | 来源 |
|---|---|---|---|---|---|
| 1 | Pattern: Audience-Role Dichotomy + Mirrore |  | 同一核心构念对至少两类受众/情境产生理论上相反的效果；不是强度差异，而是真正的方向反转。 |  | Pontikes (2012), *Administrati |
| 2 | Pattern: Sign-Flipping Boundary Condition | 反直觉/反转 | 同一 IV 对 DV 的方向因受众/情境/角色而异；需要用机制解释方向反转，而非仅做交互项。 |  | Pontikes (2012), *ASQ*（audienc |
| 3 | Pattern: Three-Condition Framework for Inf |  | 研究组织在不确定性决策中向同伴学习/模仿的现象；需要将经典信息级联理论转化为可检验的组织情境 |  | Shi, Grewal & Sridhar (2021), |
| 4 | Pattern: Institutional Shock as Theory Hoo |  | 政策/规则变化创造自然实验，观察组织行为模式变化；需要用制度冲击和 aggregate tr |  | Shi, Grewal & Sridhar (2021), |
| 5 | Pattern: Dual-Logic Integration — Input vs |  | 同一构念在文献中存在两种对立预测；两种逻辑作用于不同 facet（投入量 vs 转换效率）， |  | Zhou, Gao & Zhao (2017), *Admi |
| 6 | Pattern: Anchor → Mechanism Move(s) → Warr |  | 绝大多数 Theory 假设推导段落的基础结构。适用于主效应、中介、调节等所有假设类型。 |  | ： |
| 7 | Pattern: Theory-Driven Anchor + Puzzle Tur | 反直觉/反转 | 当文献中存在一个被默认接受的强理论直觉，而你的研究要挑战或反转它时使用。 |  | ：Singh and Grewal (2023), *Jou |
| 8 | Pattern: Multi-Mechanism Trunk |  | 主效应有多个并行的机制路径，后续调节假设需要分别回到这些机制上展开。 |  | ：Shen, Zhou, Wang, and Zhang ( |
| 9 | Pattern: Bilateral Moderation Derivation（h |  | 调节效应型论文中，需要同时论证 moderator 高值和低值条件下的机制变化。 |  | ：Shen, Zhou, Wang, and Zhang ( |
| 10 | Pattern: Indirect Moderation / Mediated Mo |  | 当理论预期一个 moderator 的调节作用本身被另一个变量中介时使用（mediated |  | ：Singh and Grewal (2023), *Jou |
| 11 | Pattern: Cumulative Moderation Build-Up |  | 后续调节假设建立在前面调节假设的基础上，形成累积式论证结构。 |  | ：Singh and Grewal (2023), *Jou |
| 12 | Pattern: Counterintuitive Anchor + Three P | 反直觉/反转 | 研究挑战文献共识，指出某一常见行为对某个目标对象有隐性负面后果；同一 DV 可由多个独立的心 |  | Keeves, Westphal & McDonald (2 |
| 13 | Pattern: Parallel Dual-Source Antecedents |  | 同一 mediator 可由 focal actor 自身行为和他人行为共同引发；需要分别推 |  | Keeves, Westphal & McDonald (2 |
| 14 | Pattern: Emotion Action Tendency → Interpe |  | 研究需要从情绪 mediator 延伸到具体的人际伤害行为后果；需要把抽象情绪与具体行为连接 |  | Keeves, Westphal & McDonald (2 |
| 15 | Pattern: Cross-Disciplinary Theoretical Le |  | 将金融/治理/制度变量引入营销、创新、CSR 等职能结果研究；需要先建立原领域理论，再论证跨 |  | Malshe & Agarwal (2015), *Jour |
| 16 | Pattern: Four-Reason Parallel Mechanism De | 多理由并行 | 解释为什么资源约束会导致某类长期投资/投入被削减；需要多个独立且互补的理由增强机制可信度。 |  | Malshe & Agarwal (2015), *JM*（ |
| 17 | Pattern: Intangible Asset Real Options + F |  | 无形资产（品牌资产、顾客满意度、专利/技术）通过增长期权创造价值，而该价值受融资约束/财务灵 |  | Malshe & Agarwal (2015), *JM*（ |
| 18 | Pattern: Dual-Channel Convergence（双通道收敛，De | 双通道/双轨 | 主效应机制由两条独立通道构成——①施动方主动施加影响（push 通道）；②中介方/接收方主动 |  | DesJardine, Li & Shi (2025), * |
| 19 | Pattern: Why-Not Reverse Boundary Declarat |  | 主效应假设后，立即解释为何不预测相邻方向/相邻对象的效应——把效应的"选择性"理论化（攻击方 |  | DesJardine, Li & Shi (2025), * |
| 20 | Pattern: Width-Type Parallel Mechanism | 多理由并行 | 当 X→Y 的关系不是通过单一中介链，而是通过多个（2–3 个）独立的理论理由共同支撑时使用 |  | - Gamache, McNamara, Mannor, a |
| 21 | Pattern: Symmetric Opposing Dual-Track Mec | 双通道/双轨 | 当同一理论框架下两个条件（或 IV 的两个维度）对同一组结果产生镜像反向效应时使用。 |  | Zhao-Ding and Gaba, *Organizat |
| 22 | Pattern: Curvilinear Relationship — Two-Ph | 曲线/拐点 | 当理论预期 IV 和 DV 之间存在曲线关系（如 inverted U-shape / U- |  | Cui, Yang, and Vertinsky, *Str |
| 23 | Pattern: Opposing Joint Prerequisites → Bo | 曲线/拐点 | Y 不是两条路径的简单净和，而是只有在两个共同必要条件都达到足够水平时才会提高；随着累计 X |  | Lee and Park (2024), *Strategi |
| 24 | Pattern: Sequential Nested Moderation（序列嵌套 | 嵌套/持久 | 研究包含两层边界条件：第一层 moderator（W1）直接影响 X→Y 关系；第二层 mo |  | Chung, Low, and Rust (2022), * |
| 25 | Pattern: Three Parallel Single-Step Mechan | 多理由并行 | 单一 IV 通过多个并行的、概念独立的微观路径影响同一 DV，且每条路径都有独立文献支撑。 |  | Darby, Ketchen, Ball & Mukherj |
| 26 | Pattern: Two-Levers Theory Progression |  | 核心理论（如 agency theory）提出多个机制/杠杆，已有文献覆盖其中一个，本文覆盖 |  | Darby, Wowak, Ketchen & Connel |
| 27 | Pattern: Embedded Prose Predictions in Con |  | 目标期刊偏好 Conceptual Framework 而非独立 Hypotheses 部分 |  | Grewal, Vana, and Stephen (202 |
| 28 | Pattern: Counterintuitive Direction-Revers | 反直觉/反转 | 论文主效应的方向符号（X→Y 是正还是负）与 field 默认机制推导出的预期相反；作者不凭 |  | Ilicic & Brennan (2026), *Jour |
| 29 | Pattern: Mechanism-Targeted Intervention E |  | 论文已经建立 X -> M1 -> M2 -> Y 的有害路径，需要从“解释现象”推进到“如 |  |  |
| 30 | Pattern: Mismatch Subtype Refinement Hypot |  | 当主效应是 match/similarity → outcome（如 H1: structu |  | Du and Tsolmon (2024), *Organi |
| 31 | Pattern: Developmental Reversal of Recipro | 嵌套/持久 | 两个构念相互因果（coevolution / simultaneous / reciproc |  | Pollock, Lee, Jin, and Lashley |
| 32 | Pattern: Differential Persistence / Lagged | 嵌套/持久 | 动态面板/自回归设计中，研究问题不是某 IV→DV 斜率被调节，而是两个构念的路径依赖（pa |  | Pollock, Lee, Jin, and Lashley |
| 33 | Pattern: Belief Updating → Attention-Thres |  | 行动者根据相对参考点的反馈选择风险/保守行动；稳定偏差改变其对未来状态的信念；当预期状态接近 |  | Schumacher, Keck, and Tang (20 |
| 34 | Pattern: Background-as-Theory Dual-Channel | 双通道/双轨 | 期刊/设计选择用 BACKGROUND（或同类 Literature/Conceptual |  | Kim & Lee (2026), *Strategic M |
| 35 | Pattern: Additive Opposing Components → I | 曲线/拐点 | 同一信号携带两条同时单调、方向相反、斜率不同的信息推理，逐点相加得倒 U（非阶段主导切换）；两分量全程并存、可被不同调节分别绑定 | EMERGING（单篇；待第二篇 | Fini, Jourdan & Perkmann (2017), *Academy of Management Journal* |

## Pattern: Audience-Role Dichotomy + Mirrored Hypotheses

**适用场景**: 同一核心构念对至少两类受众/情境产生理论上相反的效果；不是强度差异，而是真正的方向反转。
**微观动作序列**: Consensus（文献认为 [state] 有害）→ Audience distinction（market-takers vs market-makers）→ Mechanism A（对 audience A 有害）→ H1a/H1b → Dialectical turn → Mechanism B（对 audience B 有益）→ H2a/H2b → Reconciliation
**范文来源**: Pontikes (2012), *Administrative Science Quarterly*（ambiguous classification hurts consumers but helps VCs）

**骨架**:
```
[Consensus challenge] Although prior research finds [X] detrimental ([citations]), [X] persists. I suggest this depends on the evaluating audience.

[Role distinction] There are two roles: [role A], who [function A], and [role B], who [function B].

[Mechanism A] For [role A], [X] makes organizations unclear. [Path 1: search failure / exclusion from consideration set]. [Path 2: inappropriate criteria / expectations not met].
H1a: [X_dim1] is negatively related to [outcome A].
H1b: [X_dim2] is negatively related to [outcome A].

[Mechanism B] For [role B], [X] signals flexibility. [Path 1: new classification opportunity / potential to redefine market structures]. [Path 2: multivocality / interpretable from multiple perspectives]. [Path 3: flexibility / adaptability to shape label definitions].
H2a: [X_dim1] is positively related to [outcome B].
H2b: [X_dim2] is positively related to [outcome B].

[Integration] The same [X] has opposing consequences depending on the audience role.
```

**为什么有效**: 用受众制度角色解释表面矛盾，将异常转化为理论机会；镜像假设强化核心论点。
**注意事项**:
- 两种角色需有清晰功能差异，不能只是 demographic 分组
- 每个角色至少两条机制路径
- T4 首句必须使用 dialectical turn 标记："Despite research showing..., it persists."
- 两类受众机制步骤数应大致对称

**反模式**: 用"A 不喜欢所以 B 喜欢"作为唯一机制；方向反转未充分解释。

**扩展：two-stage complementary process reconciliation（pontikes2012 型）**——当两类受众对同一构念的偏好**方向相反**，会产生表面 irony（"VC 偏好消费者厌恶的"——但 VC 终究要投能吸引消费者的公司）。pontikes2012 在假设陈述后用一段 **temporal staging** 化解 irony：两类受众的相反偏好不矛盾，因为他们作用于**不同发展阶段**——market-maker（VC）在**早期**筛选难以理解但具潜力的组织，market-taker（consumer）在**后期**从存活者中选择。骨架：
```
[Irony statement] The above hypotheses propose that [X] makes [actors] seem [unclear] to [audience A] but [flexible] to [audience B], leading to opposing evaluations. This may seem ironic, given that [audience B]'s ultimate goal depends on [appealing to audience A].
[Temporal staging resolution] But [audience B] engages [actors] at [an earlier stage] than [audience A], so the two audiences' reactions may form a **complementary [N]-stage process**: [audience B] first [sorts/selects actors that are difficult to understand and chooses the most promising]; in the [second] stage, [audience A] [chooses from among the survivors].
```
**为什么有效**：把"相反偏好"从逻辑矛盾重新框定为**时间上互补的分工**——两类受众都对，但在不同阶段、用不同标准起作用。这预防审稿人"VC 偏好消费者厌恶的东西，那 VC 怎么赚钱？"的致命追问，并为 Discussion 的"两阶段过程"贡献奠基。
**适用**: 两类受众对同一构念偏好相反、且作用于 actor 不同生命阶段的研究（投资者 vs 客户、招聘方 vs 同事、评审 vs 受众、孵化器 vs 市场）。
**禁忌**: temporal staging 必须有理论或经验依据（两类受众确实作用于不同阶段），不可为化解 irony 而虚构阶段；若两受众**同时**评估同一阶段的同一 actor，则 irony 无法用 staging 化解，须用其他 resolution（如 audience-specific weights）。

---

<!--
pattern_id: sign_flipping_boundary_condition
build_type: 边界条件型 / 构念辨析型
source_papers: ["Pontikes_2012_ASQ"]
confidence: medium
status: ready_for_corpus
-->

## Pattern: Sign-Flipping Boundary Condition

**适用场景**: 同一 IV 对 DV 的方向因受众/情境/角色而异；需要用机制解释方向反转，而非仅做交互项。
**微观动作序列**: Boundary claim → Condition A mechanism（negative）→ Condition B mechanism（positive）→ Integration
**范文来源**: Pontikes (2012), *ASQ*（audience role switches the sign of ambiguity-evaluation relationship）

**骨架**:
```
[Boundary claim] The [IV]-[DV] relationship depends on [condition].

[Condition A] For [A], [IV] signals [interpretation A] → [negative DV].
[Path 1] ...
[Path 2] ...

[Condition B] For [B], [IV] signals [interpretation B] → [positive DV].
[Path 1] ...
[Path 2] ...

[Integration] These reactions are not contradictory because [A] and [B] occupy different positions in [system].
```

**为什么有效**: 用机制解释方向反转，而非仅报告交互项；integration 说明两类条件为何能同时成立。
**注意事项**:
- 必须解释不同条件为何产生不同解读
- 建议给出制度/功能互补理由
- 两类条件必须有理论基础，不能是事后分组

**反模式**: Theory 中仅说"调节"而不解释机制；integration 只是"不同视角"。

---

<!--
pattern_id: three_condition_information_herding
build_type: 机制推演型 / 条件框架型
source_papers: ["Shi_Grewal_Sridhar_2021_JMR"]
confidence: high
status: ready_for_corpus
-->

## Pattern: Three-Condition Framework for Information-Based Herding

**适用场景**: 研究组织在不确定性决策中向同伴学习/模仿的现象；需要将经典信息级联理论转化为可检验的组织情境机制。
**微观动作序列**: Theoretical lens（information cascade / Bayesian updating）→ Framework preview（motivation/opportunity/ability）→ Condition 1（motivation: uncertainty in two markets）→ Condition 2（opportunity: peer behavior credibility）→ Condition 3（ability: belief updating + information sources）→ Prediction
**范文来源**: Shi, Grewal & Sridhar (2021), *Journal of Marketing Research*（advertising spending disclosure herding）

**骨架**:
```
[Lens] [Phenomenon] occurs when an agent's utility of adopting a practice increases with the proportion of others who adopt it ([reviews]). When others' adoption does not add direct economic payoff but reduces uncertainty in the decision outcome, it represents [information-based herding] ([canonical theory]).

[Setting fit] In the context of [decision domain], it is unlikely that peers' [behavior] directly increases the focal agent's utility. Instead, we focus on whether the agent benefits from peers' [behavior] by lowering its own [decision uncertainty]. Thus, we focus on [information-based herding] in [context].

[Framework] [Theory A] and [Theory B] laid a theoretical foundation, suggesting that agents reduce decision uncertainty by incorporating information from other agents' decisions in a Bayesian updating manner. This stream provides three conditions under which [information-based herding] is likely: (1) motivation, (2) opportunity, and (3) ability.

[Condition 1: Motivation] Payoffs from [decision] are uncertain because [market A reason 1, 2, 3] and [market B reason 1, 2].
[Condition 2: Opportunity] Peers' [behaviors] are credible because [institutional enforcement / litigation costs] ([citation]).
[Condition 3: Ability] Agents update beliefs based on peers' [behaviors] because [learning evidence] ([citation]). We identify two plausible information sources: [benchmark leaders] and [similar peers].

[Prediction] Therefore, [IV: peer behavior] should positively affect [DV: focal behavior].
```

**为什么有效**: 三条件框架将抽象的信息级联理论转化为可检验的组织情境机制；三个条件逻辑独立且共同必要。
**注意事项**:
- 三个条件必须逻辑独立且共同必要
- 每个条件需有具体的市场/制度/行为证据支撑
- 避免将三条件写成三个独立假设而无 convergence
- ability condition 可自然延伸到信息源比较

**反模式**: 三条件实为同一机制的不同标签；condition 之间缺乏 convergence。

---

<!--
pattern_id: institutional_shock_as_hook
build_type: 机制推演型
source_papers: ["Shi_Grewal_Sridhar_2021_JMR"]
confidence: medium
status: ready_for_corpus
-->

## Pattern: Institutional Shock as Theory Hook

**适用场景**: 政策/规则变化创造自然实验，观察组织行为模式变化；需要用制度冲击和 aggregate trend 建立现象张力。
**微观动作序列**: Phenomenon（政策改变规则）→ Trend（aggregate behavior 变化）→ Puzzle（机制解释 vs 共同因素）→ Theory bridge
**范文来源**: Shi, Grewal & Sridhar (2021), *JMR*（FRR44 改变广告支出披露规则）

**骨架**:
```
[Phenomenon] [Policy/regulation] changed [rule] in [year], transforming [behavior] from [status A] to [status B].
[Trend] As shown in [Figure], [aggregate behavior] changed from [X%] to [Y%].
[Puzzle] Is this relationship caused by [mechanism] or by [common factors]? What information sources do agents rely on?
[Theory bridge] We use [theory] to explain [mechanism].
```

**为什么有效**: 制度冲击提供外生变化，使机制论证与识别策略自然衔接；趋势图提供可视化张力。
**注意事项**:
- 趋势图需清晰展示变化
- 必须明确比较机制解释与共同因素解释
- 制度冲击需连接到核心机制，而非仅作为背景

**反模式**: 将制度冲击仅作为背景，未连接到核心机制；未排除共同因素解释。

---

<!--
pattern_id: dual_logic_input_efficiency_inverted_u
build_type: 辩证对立 / 双重逻辑整合型
source_papers: ["Zhou_2017_ASQ"]
confidence: high
status: ready_for_corpus
-->

## Pattern: Dual-Logic Integration — Input vs. Efficiency + Inverted U

**适用场景**: 同一构念在文献中存在两种对立预测；两种逻辑作用于不同 facet（投入量 vs 转换效率），最终产生最优中间值。
**微观动作序列**: Lens A（制度逻辑：IV 增加投入）→ H1a → Lens B（效率逻辑：IV 降低投入→产出效率）→ H1b → Integration（倒 U 形合成）→ H1c
**范文来源**: Zhou, Gao & Zhao (2017), *Administrative Science Quarterly*（state ownership → R&D input vs R&D efficiency → innovation）

**骨架**:
```
[Lens A] [Theory A] focuses on the interaction between [environmental feature] and organizations and emphasizes how firms are shaped by [external forces]. In [context], [environmental feature] creates constraints that hinder [outcome], and one way to address them is to [form relationship]. As [government-backed actors], [focal actors] enjoy privileges that enable them to [access resource].

We propose that [IV] should enable firms to gain more resources to invest in [mediator]. [Outcome] often requires substantial resources, but access to [resource type] in [context] is heavily controlled by the government. [IV] helps a firm to [access], [borrow], and [obtain subsidies], enabling it to spend more on [mediator].
H[X]a: [IV] has a positive effect on [mediator].

[Lens B] The conventional economic view is that [IV] is incompatible with [outcome]. According to [Theory B], as long as [condition], [problem] arises because [agent] may take advantage of [position].

[Actors] in [alternative setting] may not always succeed, but [focal actors] likely suffer more from [problem]. First, [problem dimension 1: undefined principal]. [Theoretical justification]. Second, [problem dimension 2: political appointments]. [Theoretical justification]. As a result, [managers] lack [capabilities/motivations], reducing the efficiency of converting [input] into [outcome].
H[X]b: [IV] negatively moderates the effect of [mediator] on [outcome].

[Integration] Whereas [Lens A] emphasizes the [advantage] brought by [IV], [Lens B] highlights the [disadvantage]. Because both views offer valid arguments, we need to consider both. A firm may be [category 1], [category 2], or [category 3], and the varying degree of [IV] can make [Lens A] or [Lens B] more or less salient.

When [IV] increases from zero to [moderate level], [Lens A effect] becomes more salient yet [Lens B problem] is relatively minor. As a result, the impact of [moderate IV] should be positive.

As [IV] moves from [moderate] to [high], however, [additional advantage] increases incrementally, but [control shift]. Accordingly, [Lens B problem] becomes evident.
H[X]c: [IV] has an inverted U-shaped impact on [outcome], such that [moderate level] generates the most [outcome].
```

**为什么有效**: 将两种对立逻辑分解到不同 facet，再用所有权水平整合为倒 U 形预测；避免零和博弈式理论裁决。
**注意事项**:
- 两种逻辑必须指向不同 facet
- 必须解释拐点为何在中间
- 建议配套边界条件解释何时某一逻辑被削弱
- 倒 U 形假设措辞必须明确

**反模式**: 两种逻辑指向同一 facet 导致矛盾；拐点缺乏理论依据；边界条件只是事后补丁。

**扩展：moderator-as-remedy（H3/H4，zhou2017 型）**——当 dual-logic 中的"负面逻辑"（如 H1b 效率诅咒）识别出一个 dys-function，后续调节假设可把 moderator 理论化为**该 dys-function 的解药**。zhou2017 的 H3/H4 即此：H1b 指出 state ownership 引发 dual agency problem 导致 R&D→innovation 效率低；H3（工业竞争）与 H4（start-up 状态）则论证**外部治理控制**（竞争作为外部 monitor、start-up 的生存压力）能缓解该 agency problem，使 SOE 更有效率地转化 R&D。
骨架：
```
[Problem recap] As argued in [H1b / the negative logic], [IV] creates [dys-function—e.g., dual agency problem] that reduces [efficiency].
[Remedy mechanism] [Moderator] can attenuate this [dys-function] because [theoretical reason—e.g., competition is a salient external governance control that forces inefficient firms to exit; start-ups face liabilities of newness that discipline managers].
[Specific channels] First, [moderator] reduces [channel 1—e.g., political interference]. Second, [moderator] increases [channel 2—e.g., managerial motivation/accountability].
[Prediction] H[N]: The [negative] moderating effect of [IV] on the [M]→[Y] relationship is [less negative] when [moderator] is [high/present].
```
**为什么有效**：把 moderator 选择**锚定到已识别的理论问题**（不是任意 boundary condition），使调节假设成为理论论证的有机延伸而非"再补两个交互项"。moderator 不是"何时主效应更强"，而是"**什么条件下负面机制被抵消**"——对 agency/governance/institution 类研究特别有力（竞争、监管、上市、所有权结构作为治理机制）。
**注意事项**：moderator-as-remedy 须明确指向 H1b 的**具体 dys-function 机制**（不可泛泛说"improves efficiency"）；须排除"moderator 直接影响 DV"的替代解释（论证 moderator 是通过缓解 dys-function 而非独立起作用）；多个 remedy moderator 应共享同一治理逻辑（竞争与 start-up 都属"外部纪律"），形成理论一致性。

---

<!--
pattern_id: anchor_then_mechanism_then_prediction
build_type: 跨类型
source_papers: ["Singh_Grewal_2023_JMR", "Shen_Zhou_Wang_Zhang_2022_JOM"]
confidence: high
-->

## Pattern: Anchor → Mechanism Move(s) → Warrant → Prediction

**适用场景**：绝大多数 Theory 假设推导段落的基础结构。适用于主效应、中介、调节等所有假设类型。

**微观动作序列**：
1. **Anchor**：锚定一个读者已接受的理论前提、构念定义或经验事实
2. **Mechanism Move**：提出新的因果步骤或状态转换（“We argue that...”）
3. **Warrant**：用文献、理论、案例或反事实推理支撑机制步骤
4. **Prediction**：收敛到正式假设

**骨架**：
```
[Anchor] [理论前提 / 构念定义 / 经验事实].
[Mechanism Move] We argue that [IV] influences [DV] by [mechanism step].
[Warrant 1] This is because [theoretical reason] ([citation]).
[Warrant 2] For example, [concrete illustration].
[Prediction] Therefore, we hypothesize: H[X]: [正式假设].
```

**范文来源**：
- Singh and Grewal (2023), *Journal of Marketing Research*（H1：效率视角 Anchor → 合法性视角反转 → 机制）
- Shen, Zhou, Wang, and Zhang (2022), *Journal of Operations Management*（H1：构念定义 Anchor → 三机制并行）

**为什么有效**：四动作序列符合读者的认知推进：先确认共同起点，再引入新因果主张，接着给出信任依据，最后导出可检验预测。

**注意事项**：
- Anchor 必须与后续 Mechanism Move 存在逻辑承接，不能悬空
- Warrant 的数量和类型要与 Mechanism Move 的争议程度匹配：越反直觉，Warrant 越密集
- Prediction 必须能从 Mechanism Move 直接推出，避免“因此”跳跃

**反模式**：如果 Mechanism Move 只是重复 Anchor 的内容（例如 Anchor 说 X 影响 Y，Mechanism Move 又说 X 影响 Y），则推导塌陷为同义反复。

---

<!--
pattern_id: theory_driven_anchor_with_puzzle_turn
build_type: 机制推演型 / 假设树型 / 竞争假设型
source_papers: ["Singh_Grewal_2023_JMR"]
confidence: medium
status: needs_validation
-->

## Pattern: Theory-Driven Anchor + Puzzle Turn

**适用场景**：当文献中存在一个被默认接受的强理论直觉，而你的研究要挑战或反转它时使用。

**微观动作序列**：
1. **Anchor（理论前提）**：陈述主流理论的预测
2. **Gap/Puzzle（反直觉转折）**：指出另一种理论视角给出不同预测
3. **Mechanism Move**：解释为什么第二种预测成立
4. **Warrant**：用文献或案例支撑
5. **Prediction**：导出假设

**骨架**：
```
[Anchor] From an [established theory] perspective, [IV] should not influence [DV] because [IV] does not alter [mechanism that determines DV].
[Puzzle] However, a [alternative theory]-based perspective and the associated [model/literature] suggest that [IV] [direction] [DV].
[Mechanism Move] We argue that [IV] influences [DV] through [mechanism].
[Warrant] This is consistent with [theory], which posits that [theoretical argument] ([citation]).
[Prediction] Therefore, we hypothesize: H1: [IV] is [direction] related to [DV].
```

**范文来源**：Singh and Grewal (2023), *Journal of Marketing Research*

**为什么有效**：用一个读者接受的理论作为“稻草人”，然后反转，制造更强的认知张力，让新假设显得不仅新颖而且必要。

**注意事项**：
- 必须准确陈述主流理论的预测，不能 caricature
- 反转必须有独立的理论框架支撑，不能只靠 “however”
- 如果主流理论在文献中并不占主导，此 Anchor 会显得牵强

**反模式**：如果效率视角本身在文献中不占主导，不要用此 Anchor。

---

<!--
pattern_id: multi_mechanism_trunk
build_type: 机制推演型 + 调节效应型
source_papers: ["Shen_Zhou_Wang_Zhang_2022_JOM"]
confidence: high
-->

## Pattern: Multi-Mechanism Trunk

**适用场景**：主效应有多个并行的机制路径，后续调节假设需要分别回到这些机制上展开。

**微观动作序列**：
1. **Anchor**：预告“有三个原因”
2. **Mechanism Move 1/2/3**：每个机制独立展开
3. **Concrete Illustration（可选）**：为每个机制配案例
4. **Warrant**：收束机制群
5. **Prediction**：导出 H1

**骨架**：
```
[Anchor] We suggest that [IV] may [direction] [DV] for three reasons.

[Mechanism Move 1] First, [IV] may induce [state 1], which [effect on DV].
[Illustration 1] For example, [company/context]...

[Mechanism Move 2] Second, [IV] may lead to [state 2], preventing firms from [action].
[Illustration 2] For instance, [company/context]...

[Mechanism Move 3] Third, [IV] may cause [state 3], decreasing firms' ability to [action].
[Illustration 3] [company/context]...

[Warrant] Taken together, these mechanisms suggest that [IV] undermines [DV].
[Prediction] Therefore, we hypothesize: H1: [IV] is [direction] related to [DV].
```

**范文来源**：Shen, Zhou, Wang, and Zhang (2022), *Journal of Operations Management*

**为什么有效**：多个机制并行展开，展示理论深度；后续 moderator 可以分别回到这三个机制上，形成 Parallel 结构。

**注意事项**：
- 三个机制必须概念独立，不能是同一机制的不同标签
- 每个 illustration 必须对应其机制步骤，不能通用
- 后续调节假设段落必须明确引用 trunk 中的具体机制

**反模式**：如果只有一个机制，不要硬拆成三个；如果 moderator 段落不回到 trunk 的具体机制，parallel 结构名存实亡。

---

<!--
pattern_id: bilateral_moderation_derivation
build_type: 调节效应型 / 假设树型
source_papers: ["Shen_Zhou_Wang_Zhang_2022_JOM"]
confidence: high
-->

## Pattern: Bilateral Moderation Derivation（high/low 双边论证）

**适用场景**：调节效应型论文中，需要同时论证 moderator 高值和低值条件下的机制变化。

**微观动作序列**：
1. **Anchor**：引入 moderator 作为 boundary condition
2. **High-condition Mechanism Move**：论证高 moderator 下机制如何变化
3. **Low-condition Mechanism Move**：论证低 moderator 下机制如何变化（可用 “By contrast” / “When... is low”）
4. **Warrant**：用文献或制度逻辑支撑两边
5. **Prediction**：导出调节假设

**骨架**：
```
[Anchor] The above relationship, however, is contingent on [W].

[High condition] When [W] is high, [mechanism 1] is weakened because ...; [mechanism 2] is reduced because ...; and [mechanism 3] is overcome because ....
[Low condition] By contrast, when [W] is low, [mechanism 1] remains strong because ...; [mechanism 2] persists because ...; and [mechanism 3] dominates because ....

[Warrant] Thus, [theory/literature] suggests that [W] buffers/attenuates the negative effect of [IV] on [DV].
[Prediction] Therefore, we hypothesize: H[X]: The negative relationship between [IV] and [DV] is weaker when [W] is high rather than low.
```

**范文来源**：Shen, Zhou, Wang, and Zhang (2022), *Journal of Operations Management*（H2–H5）

**为什么有效**：双边论证让读者看到调节变量在两种极端状态下的完整因果图景，避免只论证一边导致的 selection bias 感。

**注意事项**：
- 不能只论证高条件然后默认低条件是反过来的
- 两边的机制变化必须对称地回到 trunk 机制
- 连接词要清晰：high 用 “When... is high” / “Under high...”; low 用 “By contrast” / “Conversely” / “When... is low”

**反模式**：如果 moderator 是分类变量或只有一侧有理论意义，不要硬凑双边论证。

---

<!--
pattern_id: indirect_moderation_derivation
build_type: 假设树型 / 机制推演型
source_papers: ["Singh_Grewal_2023_JMR"]
confidence: low
status: needs_validation
-->

## Pattern: Indirect Moderation / Mediated Moderation Derivation

**适用场景**：当理论预期一个 moderator 的调节作用本身被另一个变量中介时使用（mediated moderation）。

**微观动作序列**：
1. **Anchor**：两个独立调节假设已经建立
2. **Mechanism Move**：解释第二个 moderator 如何传播第一个 moderator 的信息/效果
3. **Warrant**：理论文献 + 方法学模型引用
4. **Prediction**：导出间接调节假设

**骨架**：
```
[Anchor] As discussed, [W1] moderates the [IV]→[DV] relationship, and [W2] also moderates this relationship.
[Mechanism Move] We argue that [W2] mediates the moderating effect of [W1] on the [IV]→[DV] link because [W2] disseminates [information] about [W1], thereby shaping [actor]'s response.
[Warrant] This is consistent with [theory], which suggests that [argument] ([citation]). Model B in [methodology paper] captures this indirect moderation structure.
[Prediction] Therefore, we hypothesize: H[X]: The interaction of [W2] and [IV] mediates the moderating effect of [W1] on the relationship between [IV] and [DV].
```

**范文来源**：Singh and Grewal (2023), *Journal of Marketing Research*

**为什么有效**：把复杂的统计模型（mediated moderation）转化为可理解的理论叙事。

**注意事项**：
- 必须独立论证为什么 W2 会中介 W1 的调节作用，不能只引用方法论文献
- 建议在 H4 前用图示（Model A vs Model B）辅助
- Warrant 中理论文献应占主导，方法论文献只起辅助说明作用

**反模式**：如果 W2 只是另一个调节变量，不要硬说成间接调节。

---

<!--
pattern_id: cumulative_moderation_build_up
build_type: 假设树型 / 机制推演型
source_papers: ["Singh_Grewal_2023_JMR"]
confidence: medium
status: needs_validation
-->

## Pattern: Cumulative Moderation Build-Up

**适用场景**：后续调节假设建立在前面调节假设的基础上，形成累积式论证结构。

**微观动作序列**：
1. **Anchor**：回顾前面已建立的调节关系
2. **Mechanism Move**：说明两个调节变量如何交互或如何共同塑造信息环境
3. **Warrant**：信息传播理论 / 注意力理论
4. **Prediction**：导出更复杂的调节假设

**骨架**：
```
[Anchor] As established, [W1] shapes how [IV] influences [DV] by altering [mechanism]. [W2] further alters this relationship by [second mechanism].
[Mechanism Move] We argue that these two moderating effects are not independent; rather, [W2] transmits or amplifies the information conveyed by [W1].
[Warrant] This is because [theory] posits that [argument] ([citation]).
[Prediction] Therefore, we hypothesize: H[X]: [complex moderation hypothesis].
```

**范文来源**：Singh and Grewal (2023), *Journal of Marketing Research*

**为什么有效**：通过累积而非平行组织，展示理论层次的递进；适合 JMR 等偏好复杂理论模型的期刊。

**注意事项**：
- 每个前置假设必须足够稳固，否则累积会塌陷
- 必须清晰说明两个 moderator 的交互或层级关系，不能简单并列

**反模式**：如果两个 moderator 之间没有理论交互，不要硬用 cumulative 结构。

---

<!--
pattern_id: counterintuitive_anchor_three_parallel_threats
build_type: 机制推演型 / 反直觉预测型
source_papers: ["Keeves_2017_ASQ"]
confidence: high
status: ready_for_corpus
-->

## Pattern: Counterintuitive Anchor + Three Parallel Psychological Threats

**适用场景**: 研究挑战文献共识，指出某一常见行为对某个目标对象有隐性负面后果；同一 DV 可由多个独立的心理路径共同引发。
**微观动作序列**: Evidence-Contrast（主流观点认为 IV 有益）→ Mechanism premise（IV 威胁心理状态）→ Three parallel threats（每条路径独立展开）→ Convergence（威胁汇聚到同一 mediator）→ Prediction
**范文来源**: Keeves, Westphal & McDonald (2017), *Academy of Management Journal*（ingratiation 通常构建 social capital，但本文指出其引发 resentment）

**骨架**:
```
[Contrast] Although prior research has focused almost entirely on the beneficial outcomes of [IV] for [actor who performs it], [IV] can also have different and even opposing consequences for [target].
[Mechanism premise] We suggest that [IV] threatens [psychological state] by violating [ideal 1], [ideal 2], and [ideal 3].

[Threat 1] The first reason that [IV] threatens [psychological state] is that it violates [ideal 1]. [Theoretical justification + citation]. Thus [IV] threatens [psychological state] by violating [ideal 1].
[Threat 2] Second, [IV] threatens [psychological state] because it is an act of [attribute 2] that compromises [psychological need]. [Theoretical justification + citation].
[Threat 3] Third, [IV] violates [ideal 3]. [Theoretical justification + citation].

[Convergence] The tendency for [IV] to threaten [psychological state] may prompt [mediator]. [Cognitive bias] exacerbates this effect by causing [actor] to externalize blame to [target]. [Theoretical justification + citation].
[Prediction] Therefore, we hypothesize: H[X]: [IV] is positively related to [mediator].
```

**为什么有效**: 多条独立心理路径汇聚到同一后果，增强反直觉主张的可信度；读者即使不接受某一条路径，也可通过其他路径接受假设。
**注意事项**:
- 三条威胁路径必须概念独立，不能是同一机制的不同标签
- 每条路径后需有理论或文献支撑
- 必须解释为什么这些威胁会 externalize 到目标而非内化
- 适用于心理机制/OB/upper echelons 研究

**反模式**: 三条路径实为同一机制的不同表述；只罗列威胁而无汇聚到同一 mediator 的逻辑。

---

<!--
pattern_id: parallel_dual_source_same_mediator
build_type: 机制推演型
source_papers: ["Keeves_2017_ASQ"]
confidence: medium
status: ready_for_corpus
-->

## Pattern: Parallel Dual-Source Antecedents (Self + Others) Converging on One Mediator

**适用场景**: 同一 mediator 可由 focal actor 自身行为和他人行为共同引发；需要分别推导两条并行动因路径。
**微观动作序列**: Self-path anchor → Self-path mechanism → H[X]a → Other-path anchor → Other-path mechanism → H[X]b
**范文来源**: Keeves, Westphal & McDonald (2017), *ASQ*（H1a: self-ingratiation → resentment; H1b: others' ingratiation toward target → resentment）

**骨架**:
```
[Self-path anchor] A salient object of blame for one's [behavior] is the recipient; most people respond positively to [behavioral components], so the focal actor can easily attribute his or her [behavior] to the preferences of the communication partner.
[Self-path mechanism] This leads to [mediator] because [theoretical reason] ([citation]).
[Prediction a] H[X]a: [IV_self] is positively associated with [mediator].

[Other-path anchor] [Actor] may also feel [mediator] toward [target] for the [behavioral components] that [target] receives from [other actors]. When [actors] observe others engaging in [IV], they assume such behavior is rewarded by [target].
[Other-path mechanism] [Theoretical justification]. Moreover, such [mediator] is amplified by [psychological bias 1] and [psychological bias 2].
[Prediction b] H[X]b: [IV_other] is positively associated with [mediator].
```

**为什么有效**: 从两个来源同时论证 mediator 的成因，增强理论的全面性；a/b 配对暗示两条路径共享同一心理机制。
**注意事项**:
- 两条路径必须指向同一 mediator 的不同来源
- 他人路径需解释观察者如何推断奖励机制
- 两条路径篇幅应大致对称

**反模式**: 两条路径实为同一来源的不同表述；他人路径只是“同理可证”。

---

<!--
pattern_id: emotion_action_tendency_consequence
build_type: 机制推演型
source_papers: ["Keeves_2017_ASQ"]
confidence: medium
status: ready_for_corpus
-->

## Pattern: Emotion Action Tendency → Interpersonal Harm

**适用场景**: 研究需要从情绪 mediator 延伸到具体的人际伤害行为后果；需要把抽象情绪与具体行为连接起来。
**微观动作序列**: Anchor（情绪有负面后果）→ Theory（情绪行动倾向）→ Mechanism（情绪的认知/情感特征 → 行动倾向）→ Behavioral channel（具体行为形式）→ Matching rule（伤害形式与怨恨来源匹配）→ Illustration（案例/引语）→ Prediction
**范文来源**: Keeves, Westphal & McDonald (2017), *ASQ*（resentment → social undermining via negative commentary to journalists）

**骨架**:
```
[Anchor] [Mediator] can also have negative repercussions for [target] outside the firm; feelings of [mediator] toward [target] could prompt [actor] to engage in [DV].
[Theory] [Emotion theory] indicates that discrete emotions have distinctive action tendencies ([citation]).
[Mechanism] [Mediator] has a distinctive profile of negative thoughts, feelings, and action tendencies. [Theoretical justification + citations].
[Behavioral channel] [DV] by [actor] may take the form of [concrete behavior] in communicating with [third party]. [Theoretical justification].
[Matching rule] The tendency to [DV] someone perceived to have benefitted unfairly follows a "matching rule": the form of harm is similar in kind to the source of ill will.
[Illustration] [Concrete illustration from interviews or cases].
[Prediction] Thus our final hypothesis posits that [mediator] will be positively associated with [DV]. This prediction is formally equivalent to hypothesizing that [mediator] mediates effects of [IV] on [DV]:
H[X]: [Mediator] is positively associated with [DV].
```

**为什么有效**: 将抽象情绪与具体行为通过 action tendency 和 matching rule 连接，避免"情绪直接影响行为"的黑箱；案例/引语增强 human face。
**注意事项**:
- 必须引用情绪理论说明 action tendency
- 必须有 concrete illustration（案例/引语）增强可信度
- 必须说明伤害渠道为何与情绪来源"匹配"

**反模式**: 只说"resentment leads to harm"而不解释行动倾向、伤害渠道和匹配规则。

---

<!--
pattern_id: finance_to_marketing_crossover_t2
build_type: 机制推演型 / 跨界嫁接型
source_papers: ["Malshe_Agarwal_2015_JM"]
confidence: high
status: ready_for_corpus
-->

## Pattern: Cross-Disciplinary Theoretical Lens (Finance → Functional Outcome)

**适用场景**: 将金融/治理/制度变量引入营销、创新、CSR 等职能结果研究；需要先建立原领域理论，再论证跨界传导。
**微观动作序列**: Classic theorem anchor（完美市场无关性）→ Imperfect-market reality（成本/收益清单）→ Crossover claim（成本如何传导到职能领域）→ Mechanism preview
**范文来源**: Malshe & Agarwal (2015), *Journal of Marketing*（financial leverage → customer satisfaction）

**骨架**:
```
[Classic theorem] In perfect markets, [financial/governance decision] should not affect [functional outcome] ([classic finance citation]).
[Imperfect reality] However, in imperfect markets, [decision] creates both benefits and costs that shape [managerial behavior] ([finance citations]).

[Cost enumeration] One major cost is [cost 1]: higher [financial leverage] increases [risk A] and reduces [slack B] ([citation]). A second cost is [cost 2]: the pressure to meet [fixed obligations] makes managers [myopic behavior] ([citation]). A third cost is [cost 3]: stakeholders who fear breach of implicit contracts reduce their engagement with the firm ([citation]).

[Crossover claim] We argue that these pressures are transmitted to [functional domain]. Specifically, [functional managers] respond by [short-term action], which hurts [marketing outcome].
```

**为什么有效**: 明确本文在理论框架中的位置，避免"另起炉灶"；让读者看到 contribution 是理论的自然延伸。
**注意事项**:
- 两个领域必须有真实的逻辑连接，不能硬凑
- 成本/收益清单必须来自原领域经典文献
- 必须说明为什么职能结果值得金融变量关注

**反模式**: 两个领域实际来自不同理论框架；或只是用金融变量作为控制变量，没有机制推演。

---

<!--
pattern_id: four_reason_mechanism_chain
build_type: 机制推演型
source_papers: ["Malshe_Agarwal_2015_JM"]
confidence: high
status: ready_for_corpus
-->

## Pattern: Four-Reason Parallel Mechanism Derivation

**适用场景**: 解释为什么资源约束会导致某类长期投资/投入被削减；需要多个独立且互补的理由增强机制可信度。
**微观动作序列**: Pressure statement → "[Action] is likely to decline for four reasons" → Reason 1/2/3/4（每个独立展开）→ Convergence to hypothesis
**范文来源**: Malshe & Agarwal (2015), *JM*（why leverage reduces advertising/R&D）

**骨架**:
```
[Pressure] Firms with higher [financial leverage] face [pressure 1] to service debt and [pressure 2] to conserve cash ([citation]). We argue that [functional managers] respond to this pressure by [action 1] rather than [long-term action 1].

[Four reasons] [Action 1] is likely to decline for four reasons.
First, [action 1] is discretionary and is commonly cut to meet short-term cash needs ([citation]).
Second, [action 1] builds [intangible asset], whose returns are uncertain in the near term ([citation]).
Third, [intangible asset] is firm-specific and loses value in financial distress ([citation]).
Fourth, high leverage creates an [underinvestment problem] because future benefits may accrue to debt holders rather than shareholders ([citation]).

[Outcome link] [Outcome] depends on [antecedent 1], [antecedent 2], and [antecedent 3] ([citation]). [Action 1] positively affects [antecedent 1] and [antecedent 2] by [mechanism] ([citations]). [Action 2] positively affects [antecedent 2] by [mechanism] ([citation]). Therefore, lower [action 1] and [action 2] reduce [outcome].

[Prediction] Following this discussion, we propose that higher [IV] is likely to reduce [mediator 1] and [mediator 2], and this in turn will lower [DV].
H[X]: The impact of [IV] on [DV] is mediated by (a) [mediator 1] and (b) [mediator 2].
```

**为什么有效**: 多理由并行提供论证密度；即使读者只接受部分理由，也能接受最终假设。
**注意事项**:
- 四个理由必须概念独立，避免 overlap
- 每个理由后需有 citation 或案例支撑
- 理由与最终假设之间的收敛信号必须清晰

**反模式**: 四个理由实为同一机制的不同标签；或收敛句只提最后一个理由。

---

<!--
pattern_id: intangible_asset_real_options_distal_moderation
build_type: 机制推演型 / 调节效应型
source_papers: ["Malshe_Agarwal_2015_JM"]
confidence: high
status: ready_for_corpus
-->

## Pattern: Intangible Asset Real Options + Financial Constraint Distal Moderation

**适用场景**: 无形资产（品牌资产、顾客满意度、专利/技术）通过增长期权创造价值，而该价值受融资约束/财务灵活性调节。
**微观动作序列**: Intangible asset creates growth options → Real options framing → Moderator reduces financial flexibility → Option value shrinks → Prediction
**范文来源**: Malshe & Agarwal (2015), *JM*（customer satisfaction → firm value, weakened by leverage）

**骨架**:
```
[DV value base] A large body of research has shown that [M] leads to [DV] ([citations]). [M] produces value in two ways: [immediate cash flow channel] and [growth option channel] ([citations]).

[Real options framing] Marketing scholars argue that [intangible asset] provides firms with growth options ([citations]). We treat these options as [real options] ([citations]). The value of these options depends on the firm's [capability], which partly depends on [moderator] ([citation]).

[Moderator mechanism] When firms increase [moderator], [mechanism 1: reduced ability to raise future debt] and [mechanism 2: higher cost of capital] reduce financial flexibility. Higher [moderator] also increases the required return threshold for growth projects, shrinking the set of viable options ([citation]).

[Prediction] Therefore:
H[X]: The impact of [M] on [DV] is [weaker/more negative] for firms with [high/low] [moderator].
```

**为什么有效**: 将无形资产价值置于 real options 框架下，使远端调节变量（leverage）有明确的理论机制。
**注意事项**:
- 必须说明为什么无形资产包含增长期权
- 必须解释 moderator 如何具体影响 option value
- 区分 immediate cash flow channel 和 growth option channel

**反模式**: 只说"leverage matters"而不解释它如何改变 option value；或将 real options 术语作为装饰。

---

## Pattern: Dual-Channel Convergence（双通道收敛，DesJardine–Li–Shi 2025 型）

**适用场景**: 主效应机制由**两条独立通道**构成——①施动方主动施加影响（push 通道）；②中介方/接收方主动迎合（pull 通道）——两条通道**收敛于同一预测**，用于加固主效应机制而非裁决。

**微观动作序列**: 通道 1（主动施加：讨论/反馈/游说）→ "On the other side of the equation" 通道 2（被动迎合：讨好/忌惮）→ "Importantly" 可行性条件（不透明性/低检测风险）→ 假设

**范文来源**: DesJardine, Li & Shi (2025), *Academy of Management Journal*（H1：投资者讨论反馈 + 评级机构高管迎合 + 评级过程不透明）

**原文锚点**:
> "Influence begins with the discussions that occur between common owners and rating agency executives, and, sometimes, analysts."
>
> "On the other side of the equation, executives of rating agencies may cater to the interests of their major institutional investors."
>
> "Importantly, the opacity of the ESG rating process facilitates these opportunities for rating influence while decreasing the risk of detection for both institutional investors and rating agency insiders."

**骨架**:
```
[通道 1：主动施加] Influence begins with the [channel 1: discussions between attackers and intermediary executives]. [Intermediary] analysts and executives struggle to [access/understand target's activities], and are at times limited by the information they can collect from [data source] ([citation]). One information source [intermediaries] might value is [attackers], who may be perceived as competent and informed ([citation]). In these discussions, [attackers] may naturally speak more positively about [their portfolio firms], and more negatively about those firms' competitors—the 'target' firms. [Intermediary] executives and analysts could consciously or subconsciously use this feedback to inform their [assessments] ([citation]).

[通道 2：被动迎合] On the other side of the equation, executives of [intermediaries] may cater to the interests of their major institutional investors. Prior studies show that executives sometimes go to great lengths to appease their investors ([citation]), partially because losing or upsetting investors can cause financial and reputational harm to executives ([citation]). To reduce that risk, standard [protocols] advise executives to pay close attention to major investors' holdings in other companies and try to account for those investors' economic interests ([citation]).

[可行性条件] Importantly, the [opacity] of the [assessment] process facilitates these opportunities for influence while decreasing the risk of detection for both [attackers] and [intermediary] insiders. The theorized channel through which [attackers] influence [intermediaries] is legal. The subjectivity of [assessments] not only gives [intermediaries] latitude in their evaluations, but also gives their executives and analysts flexibility to adjust [assessments] based on an [attacker's] advice. Thus, if [attackers] go to great lengths to directly coordinate activities among multiple portfolio firms ([citation]), it seems plausible that they use their ownership influence in [intermediaries] to shape [assessments] for their own benefit, and that some [intermediary] executives are open to that influence.

[H 收敛] We expect [targets] to receive less favorable [assessments] from [intermediaries] in which their rivals' institutional investors have greater ownership. Formally:
H1. The level of [IV] is negatively associated with [DV].
```

**为什么有效**:
- **push + pull 双通道加固**: 主动施加（施动方有动机和手段）+ 被动迎合（接收方有忌惮和利益）——两条独立通道都指向同一预测，机制可信度高于单通道
- **与 B2（双轨机制）的判别**: B2 要求两条路径产生**不同**的可检验预测、时间轨迹或条件反应；本模式两条通道**收敛于同一预测**——用于加固主效应而非裁决。若两条通道预测相反（如一条增强一条减弱），改用 B2/F
- **可行性作为第三环**: 动机（willing）+ 手段（able）之外，**不透明性/低检测风险**是影响发生的第三前提——"hidden" 维度：机制在何种条件下能隐蔽运作
- **合法性声明**: "The theorized channel... is legal"——明确影响渠道合法，防审稿人质疑伦理/合法性
- **三节拍连接词**: 通道 1（无标记）→ "On the other side of the equation" → "Importantly"——每节拍一个显式连接，无跳跃

**反模式**: 两条通道实际是同一机制的同义改写（一个说"投资者施加影响"一个说"高管接受影响"而无独立机制步）——必须是概念独立的两条通道；可行性条件写成无关的稳健性注释而非机制环节；把双通道写成 B2 双轨（预测不同）。

---

## Pattern: Why-Not Reverse Boundary Declaration（"why not" 反向边界声明，DesJardine–Li–Shi 2025 型）

**适用场景**: 主效应假设后，立即解释**为何不预测相邻方向/相邻对象的效应**——把效应的"选择性"理论化（攻击方为何选择受害方而非自己人），防止读者追问，同时深化机制。

**微观动作序列**: 假设 H1 → "There are two related reasons why we do not hypothesize that..." → First（检测/暴露风险）→ Second（相对效应/比较逻辑）→ 收束（双重逻辑合并）

**范文来源**: DesJardine, Li & Shi (2025), *Academy of Management Journal*（H1 后：为何不预测影响自己的组合企业）

**原文锚点**:
> "There are two related reasons why we do not hypothesize that institutional investors seek to influence the ratings of their own portfolio firms. First, as warnings about the anticompetitive effects of common owners have been raised among regulators, common owners can decrease their risk of detection by procuring worse ESG ratings for firms not in their portfolios. Second, by handicapping a target firm that competes with their portfolio firms, common owners can realize improved investment prospects among several of their portfolio firms."

**骨架**:
```
There are two related reasons why we do not hypothesize that [attackers] seek to influence the [assessments] of their own portfolio firms. First, as warnings about the [anticompetitive effects] of [attackers] have been raised among [regulators], [attackers] can decrease their risk of detection by procuring worse [assessments] for firms not in their portfolios. Second, by handicapping a target firm that competes with their portfolio firms, [attackers] can realize improved investment prospects among several of their portfolio firms. This relative effect occurs because [standards] differ widely between industries, forcing stakeholders and investors to make comparisons on a within-[unit] basis. Taken together, by negatively influencing their portfolio firms' rivals, [attackers] can realize the rewards of their [influence] while decreasing the risk of their influence being detected.
```

**为什么有效**:
- **反向边界声明**: 不预测什么 + 为什么——把选择性本身理论化（检测风险最小化 + 相对效应最大化），而非留白
- **两理由结构**: First（检测风险/暴露）→ Second（相对效应 + 单元内比较）→ 收束（rewards + detection 双重逻辑合并）——理由之间有张力（一个说"减少暴露"一个说"增加收益"），收束句将两者统一
- **相对比较嵌入**: "comparisons on a within-industry basis"——用评估的序数/相对性质解释为何选择"别人的企业"
- **与 E1 Step 6（排除反向交互）的关系**: 排除反向交互是"为什么是 Z 调节 X→Y"；本模式是"为什么 X 不作用于相邻对象"——选择性效应辩护

**反模式**: 假设后没有边界声明但读者会追问相邻对象——边界声明缺失；理由之间矛盾（一个说"减少暴露"一个说"增加收益"却不收束统一）；把边界声明写成第二个假设（"我们同样预测..."）而非排除。

---

## 段内逻辑布局原则

### 1. 连接词的功能分类

| 功能 | 常用连接词 | 使用位置 |
|------|-----------|---------|
| 引入机制 | “We argue that...”, “Specifically,...”, “The mechanism underlying this relationship is...” | Mechanism Move 开头 |
| 递进机制 | “First... Second... Third...”, “Moreover,...”, “In addition,...” | 多机制 trunk 内部 |
| 转折/反直觉 | “However,...”, “Yet,...”, “Contrary to this intuition,...” | Anchor → Puzzle 之间 |
| 条件化 | “When... is high...”, “Under conditions of...”, “Conversely,...” | 双边论证中 |
| 收束假设 | “Therefore, we hypothesize:”, “Taken together, these arguments suggest:” | Prediction 前 |

### 2. 段落长度与动作密度

- 一个标准假设推导段落建议包含 **1 个 Anchor + 1–3 个 Mechanism Move + 2–4 个 Warrant + 1 个 Prediction**
- 调节假设段落建议额外包含 **High/Low 两个条件分支**
- 间接调节/复杂调节段落建议拆分为 **2 个段落**：第一段建立两个独立调节，第二段论证交互/中介

### 3. Warrant 的三种摆放策略

| 策略 | 适用场景 | 范文 |
|------|---------|------|
| Warrant-Embedded（嵌入机制后） | 每个机制步骤后紧跟文献/案例 | Shen et al. (JOM) H1 |
| Warrant-Clustered（机制后集中） | 多个机制共享同一理论背景 | Singh & Grewal (JMR) H1 |
| Warrant-Contrasted（正反并举） | 竞争解释或对立机制 | 竞争假设型论文 |

---

## 与相邻语料文件的关系

- [`argumentation_patterns.md`](argumentation_patterns.md)：聚焦微观动作组合（Anchor/Gap/Mechanism/Warrant/Prediction）
- [`arrangement_patterns.md`](arrangement_patterns.md)：聚焦论点-论据的空间安排（Parallel / Cumulative / Evidence-Contrast）
- [`evidence_patterns.md`](evidence_patterns.md)：聚焦证据类型、功能和文献引用三要素
- [`bilateral_argumentation_templates.md`](bilateral_argumentation_templates.md)：聚焦调节假设的 high/low 句法
- [`hypothesis_organization_patterns.md`](hypothesis_organization_patterns.md)：聚焦多个假设之间的体系级组织（common trunk / dual branch）

> **使用顺序**：先查本文件确定假设推导段落的整体动作序列 → 再查 arrangement_patterns 确定段落内部布局 → 再查 evidence_patterns 填充 Warrant → 最后查 hypothesis_forms 输出正式假设。

---

<!--
pattern_id: width_type_parallel_mechanism
build_type: 机制推演型 / 调节效应型
source_papers: ["Gamache_McNamara_Mannor_Johnson_2020_SMJ", "Cui_Yang_Vertinsky_SMJ"]
confidence: high
status: ready_for_corpus
-->

## Pattern: Width-Type Parallel Mechanism

**适用场景**: 当 X→Y 的关系不是通过单一中介链，而是通过多个（2–3 个）独立的理论理由共同支撑时使用；可支撑线性主效应、曲线关系的某一阶段，或调节假设的某一边。
**家族判别（多理由并行三兄弟）**: 与 Three Parallel Single-Step Mechanisms、Four-Reason Parallel Mechanism Derivation 同属『多理由并行』家族，差异在抽象层级——本模式（Width-Type）最通用（理由可支撑任何假设的任意一边，2-3 条）；Three Parallel 是『单一 IV 的多个概念独立微观路径』（每条路径有独立文献，Darby 2023）；Four-Reason 是『压力情境下的显式枚举收敛』（decline for N reasons，Malshe 2015）。机制路径可检验时用 Three Parallel；压力→枚举时用 Four-Reason；通用理由支撑时用本模式。
**微观动作序列**: Anchor（理论前提）→ Mechanism Move 1 + Warrant 1 → Mechanism Move 2 + Warrant 2 → [Mechanism Move 3 + Warrant 3] → Prediction
**范文来源**:
- Gamache, McNamara, Mannor, and Johnson (2020), *Strategic Management Journal*（3 个理由支撑线性主效应）
- Cui, Yang, and Vertinsky, *Strategic Management Journal*（2 个理由支撑曲线关系的递增段/递减段，以及调节假设的每一边）

**骨架（通用）**:
```
[Anchor] Drawing on [theory], we argue that [IV] [direction] [DV].
[Reason 1] First, [theoretical reason 1]. [Warrant 1]
[Reason 2] Additionally/Second, [theoretical reason 2]. [Warrant 2]
[Reason 3 — optional] Finally, [theoretical reason 3]. [Warrant 3]
[Prediction] Therefore, we hypothesize: H[X]: [正式假设].
```

**子变体 A：三理由线性主效应（Gamache 型）**

三个理由并行支撑同一方向的线性主效应。

**子变体 B：双理由曲线阶段（Cui et al. 型）**

两个理由并行支撑曲线关系的某一个阶段（递增段或递减段）。完整曲线需要两个这样的阶段组合。

**子变体 C：双理由调节一边（Cui et al. 型）**

在调节假设段落中，用两个理由论证 moderator 在 curve 低-中段的作用，再用两个理由论证其在高段的作用。

**为什么有效**: 多个独立理由并行支撑，展示理论论证的宽度和稳健性；每个理由都简短，避免深度链的复杂；读者容易跟随"First... Second..."的节奏。
**注意事项**: 
- 2–3 个理由必须概念独立，不能是同一理由的重复
- 每个理由后必须有 citation 支撑
- 适合单步机制关系或曲线关系的某一阶段，不适合需要解释完整"如何"发生的过程
- 用于调节假设时，必须对称地论证曲线的两边
**反模式**: 如果理由之间高度相关，会显得冗赘；如果研究问题需要解释过程机制，不要用宽度型代替深度链。不要为了让理由凑成 3 个而拆分本可合并的机制。

---

<!--
pattern_id: symmetric_opposing_dual_track
build_type: 机制推演型
source_papers: ["Zhao-Ding_Gaba_ORSC"]
confidence: medium
status: needs_validation
-->

## Pattern: Symmetric Opposing Dual-Track Mechanism

**适用场景**: 当同一理论框架下两个条件（或 IV 的两个维度）对同一组结果产生镜像反向效应时使用。
**微观动作序列**: Anchor（条件 1）→ Mechanism Move A1 + Mechanism Move A2（反向对）→ Prediction H1a/H1b → Anchor（条件 2）→ Mechanism Move B1 + Mechanism Move B2（镜像反向对）→ Prediction H2a/H2b
**范文来源**: Zhao-Ding and Gaba, *Organization Science*

**骨架**:
```
[Track 1: Condition A]
[Anchor] When [condition A] is high, [actor] faces [theoretical state].
[Mechanism Move A1] We argue that under [condition A], [IV] increases [DV_dimension_1] because [theoretical reason].
[Mechanism Move A2] Conversely, under [condition A], [IV] decreases [DV_dimension_2] because [theoretical reason].
[Prediction] Therefore, we hypothesize: H1a: ...; H1b: ...

[Track 2: Condition B — Mirror Reversal]
[Anchor] When [condition B] is high, [actor] faces [opposite theoretical state].
[Mechanism Move B1] We argue that under [condition B], [IV] decreases [DV_dimension_1] because [theoretical reason].
[Mechanism Move B2] Conversely, under [condition B], [IV] increases [DV_dimension_2] because [theoretical reason].
[Prediction] Therefore, we hypothesize: H2a: ...; H2b: ...
```

**为什么有效**: 两条机制链结构完全平行但方向相反，读者在理解第一条后，第二条只需"镜像反转"，大幅降低认知负荷；同时展示理论的系统性。
**注意事项**: 
- 两条 track 的机制必须在结构上真正对称，不能只名字对称
- 反向效应必须有独立理论依据，不能为了对称而硬凑
- 适合 DV 是两个互补维度（如 focus vs breadth, core vs overlap）的情境
**反模式**: 如果两个条件不是理论上的镜像，或 DV 两个维度不是互补关系，不要强行对称。

---

<!--
pattern_id: curvilinear_relationship_two_phase_argumentation
build_type: 机制推演型 / 调节效应型
source_papers: ["Cui_Yang_Vertinsky_SMJ", "Bendig_Hensellek_Schulte_2024_ETP", "Anderson_Reeb_2004_ASQ"]
confidence: high
status: verified_three_paper
-->

## Pattern: Curvilinear Relationship — Two-Phase Argumentation

**适用场景**: 当理论预期 IV 和 DV 之间存在曲线关系（如 inverted U-shape / U-shape）时，需要分别论证曲线两个阶段的机制。
**微观动作序列**: Anchor（曲线预测）→ Phase 1 递增/递减段（2 个理由）→ Transition（转折点机制）→ Phase 2 递减/递增段（2 个理由）→ Prediction
**范文来源**: Cui, Yang, and Vertinsky, *Strategic Management Journal*；Bendig, Hensellek, and Schulte (2024), *Entrepreneurship Theory and Practice*；Anderson and Reeb (2004), *Administrative Science Quarterly*

**骨架**:
```
[Anchor] We expect [IV] to have a [curve direction] relationship with [DV].

[Phase 1: Increasing/decreasing segment]
When [IV] is [low/high], [DV] [increases/decreases] as [IV] increases, for two reasons.
[Reason 1] First, [theoretical mechanism 1]. [Warrant]
[Reason 2] Second, [theoretical mechanism 2]. [Warrant]

[Transition] However, as [IV] continues to increase, [theoretical turning point condition] occurs.

[Phase 2: Decreasing/increasing segment]
When [IV] is [high/low], [DV] [decreases/increases] as [IV] increases, for two reasons.
[Reason 1] First, [theoretical mechanism 1]. [Warrant]
[Reason 2] Second, [theoretical mechanism 2]. [Warrant]

[Prediction] Therefore, we hypothesize: H1: There is a [curve shape] relationship between [IV] and [DV].
```

**为什么有效**: 曲线关系需要分别解释为什么先增后减（或先减后增），每个阶段用独立理由支撑，避免"因此是曲线"的跳跃；同时展示理论对关系全区间的掌控。

**三种经验证的 dominance schedule**:

1. **正向 Y：收益先占优、约束后占优**。低至中 X 主要激活资源或协同收益；高 X 出现过载、竞争或协调成本，形成正向 Y 的倒 U。
2. **负向 Y：成本先占优、学习后占优**。低至中 X 的搜索、协调与整合成本先提高失败/伤害；更高 X 形成惯例、能力和经验学习，继而降低负向 Y，同样形成倒 U。
3. **相对权力型 X：治理收益先占优、侵占成本后占优**。当行动者 A 相对行动者 B 的代表性较低时，增加 A 可补充信息、承诺或监督；当 A 的相对权力过高时，B 的制衡能力下降，侵占、固化或能力损失开始占优。此时 X 是有理论含义的相对配置，不能只把比例的高低当作未经解释的强度。

因此，**曲线形态不识别机制顺序**。写作时应先标记 Y 的规范方向，再说明哪个过程在何区间增长更快；不得因“倒 U”三个字自动套用“收益递减”故事。
**注意事项**:
- 必须明确转折点（turning point）的理论依据
- 两个阶段的机制不能互相矛盾，必须有统一的成本-收益或激励-约束框架
- 每个阶段使用足以建立该阶段必然性的概念独立理由；理由数量由论证负荷决定，不设固定配额
- 建议在预测句中明确 curve shape（inverted U-shape / U-shape）
- 对 negative/adverse Y，必须明确“曲线顶点是风险最高点”而非“最优中间值”
- 对 ratio/configuration X，必须分别说明分子与分母的理论角色，并用成分变量、替代规格或区间检验排除同值异构问题
**反模式**: 如果只有一个阶段的机制强，另一个阶段只是"反向论证"或"常识推断"，会显得薄弱；如果两个阶段的理由没有统一框架，会像是两个独立假设硬凑。

---

<!--
pattern_id: curvilinear_additive_opposing_components
build_type: 机制推演型 / 调节效应型
source_papers: ["Fini_Jourdan_Perkmann_2017_AMJ_Social_Valuation"]
confidence: emerging
status: needs_cross_paper_validation
story_fidelity: section_variant
-->

## Pattern: Additive Opposing Components → Inverted U（双同时单调分量相抵）

**适用场景**: 当理论预期 IV 和 DV 之间存在曲线关系，且曲线的必要性不是来自"两个阶段先后主导"（Two-Phase），而是来自**两个同时存在、方向相反、斜率不同的单调分量在每一点相加**时使用。典型情形：同一可观察信号对焦点受众同时携带两条信息推理（如能力信号 → 正、身份契合信号 → 负），二者随 IV 累积以不同速率变化，其代数和在每一点上即曲线值。

**与 Two-Phase 的判别（决定性）**:
| | Two-Phase Argumentation | Additive Opposing Components |
|---|---|---|
| 曲线来源 | 阶段主导权切换（Phase 1 机制先占优，转 Phase 2） | 两个分量**同时存在**，逐点相加（SUM） |
| 机制时态 | 时态先后（先增后减/先减后增） | 同时性（一条线性正 + 一条加速负） |
| 转折点依据 | 显式转折条件（transition condition） | 两分量边际变化率相等的点 |
| 分量可得性 | 阶段内各自主导 | 两个分量全程并存、可被不同调节变量分别绑定 |
| 范文 | Cui (SMJ), Bendig (ETP), Anderson-Reeb (ASQ) | Fini, Jourdan & Perkmann (2017, *AMJ*) |

**微观动作序列**: Anchor（信号携带双信息）→ Channel A（ability 正线性）→ Channel B（identity conformance 加速负）→ Sum（正线性 a offset 由加速负 b = 倒 U，Haans et al. 2015 分解）→ Prediction
**范文来源**: Fini, Jourdan & Perkmann (2017), *Academy of Management Journal*（industry evaluation → peer evaluation of scientists，倒 U）

**骨架**:
```
[Anchor — dual information] [Signal] provides two types of information to evaluators:
indices of [ability], and indices of [identity conformance].

[Channel A — positive, linear] First, as an index of [ability], [signal] is positively
related to [valuation], because [capability mechanism]; this effect is linear.

[Channel B — negative, accelerating] Second, as an index of [identity conformance],
[signal] is negatively related to [valuation], because [identity-deviation mechanism];
this penalty becomes increasingly salient as [signal] accumulates.

[Sum] The combination of two distinct effects—a positive linear [ability] effect (a)
offset by an increasingly negative [identity] effect (b)—results in a curvilinear,
inverted U-shaped relationship (c) ([Haans et al. 2015 citation]).

[Prediction] Therefore, we hypothesize: H[N]: There is an inverted U-shape relationship
between [signal] and [valuation].
```

**为什么有效**: 曲线由两个已有理论支撑的单调分量相加生成，转折点是分量边际变化率的相等点，而非需要另找的"转折机制"；同时——关键设计优势——**两个分量全程并存，允许后续不同的调节变量分别绑定其中一个分量**，为调节假设提供了"选择性绑定 + 不变性声明"的天然抓手（见 `paired_geometric_hypotheses_per_moderator` 与 `selective_component_invariance_declaration`）。

**注意事项**:
- 必须明确两个分量以不同速率变化（一个线性、一个加速），否则相加仍是单调，推不出倒 U。
- 两个分量必须是**同一信号**的两种信息读法、作用于**同一焦点评价者**；不是两个独立 IV。
- 引用 Haans, Pieters & He (2016) 的分解：倒 U 可由"正线性 + 加速负"合成，且分量的相对强弱决定顶点位置。
- 与机制链句级模板的关系：本模式是**架构级段落骨架**；`sentences/mechanism_chain.md` 的 `cross_audience_dual_signal_curvilinear_inference` 是**句级模板**，二者配套。
**反模式**: 只有"有正有负两条机制"而无速率差异说明 → 推不出倒 U；把两个同时分量误写成阶段先后主导（Two-Phase）→ 丢失"分量可被分别绑定"的调节抓手；把两个分量写成两个独立 IV 的平行效应 → 不是同一信号的分解。
**诚实边界**: 单篇 EMERGING（Fini et al. 2017 AMJ），需第二篇跨论文验证；不得据此改变 write-theory 的通用曲线路由。

---

<!--
pattern_id: opposing_joint_prerequisites_bottleneck_switch
build_type: 辩证对立 / 机制推演型 / 曲线关系
source_papers: ["Lee_Park_2024_SMJ"]
confidence: medium
status: emerging_single_paper
-->

## Pattern: Opposing Joint Prerequisites → Bottleneck Switch（共同必要条件反向变化—短板切换）

**适用场景**: Y 不是两条路径的简单净和，而是只有在两个共同必要条件都达到足够水平时才会提高；随着累计 X 增加，一个条件改善、另一个条件恶化，因此限制 Y 的短板从 A 切换到 B。

**微观动作序列**: Joint-necessity rule → A 随 X 改善 → B 随 X 恶化 → low/middle/high 三状态表 → binding constraint 切换 → 曲线预测。

**骨架**:
```text
[Joint necessity] [Y] requires sufficient levels of both [A] and [B]; abundance in one cannot fully compensate for scarcity in the other.

[A path] As [cumulative X] increases, [A] rises because [reasoning chain and warrant].
[B path] In parallel, [B] declines because [distinct reasoning chain and warrant].

[Low X] When X is low, A is the binding constraint even though B remains high, so Y is low.
[Middle X] At moderate X, both prerequisites remain sufficiently available, so Y reaches its highest level.
[High X] Beyond [turning condition], B becomes the binding constraint despite abundant A, so Y declines.

[Prediction] H[N]: X has an inverted-U relationship with Y: Y rises until the binding constraint shifts from A to B and falls thereafter.
```

**为什么有效**:
- 先声明组合规则，再分阶段；倒 U 不是从“两条相反机制”自动跳出。
- 三状态表让读者看见每个区间中哪一条件稀缺，避免含糊的“收益先大于成本、后来反之”。
- 允许机制保持 B0 理论过程；若未直接测量 A/B，Results 与 Discussion 不得声称中介已验证。

**与 `curvilinear_relationship_two_phase_argumentation` 的关系**: 这是其 L2 可选架构，不替代通用两阶段骨架。通用骨架适用于净收益/净成本或 dominance schedule；本架构仅适用于 A、B 都是 Y 的共同必要条件且存在明确的 bottleneck switch。

**范文来源**: Lee and Park (2024), *Strategic Management Journal*：累计失败扩大可学习信息，却逐步侵蚀学习动机；学习需要机会与动机同时充足。

**禁忌**:
- 不要把任意正负机制重命名为“共同必要条件”；必须说明为何一方不足时另一方不能补偿。
- 中间区间不能仅靠“适中最好”的直觉；须说明两个条件为何在该区间同时足够。
- 若 X、Y、层级或时间范围在两条路径间变化，冲突不属于 R3 的正式锁定。

---

<!--
pattern_id: sequential_nested_moderation
build_type: 调节效应型 / 假设树型
source_papers: ["Chung_Low_Rust_2022_JAMS", "lunetal2026_ETP"]
confidence: medium
status: emerging (2p)
-->

## Pattern: Sequential Nested Moderation（序列嵌套调节）

**适用场景**: 研究包含**两层边界条件**：第一层 moderator（W1）直接影响 X→Y 关系；第二层 moderator（W2）调节 W1 的调节效应，形成三向交互（X × W1 × W2）。典型于 upper echelons：下级劝说被相对权力放大（Chung 2022），或功能高管的注意治理缓冲被任务负荷再调节（Lun et al. 2026）。

**微观动作序列**:
1. **Anchor**：建立 X→Y 基线机制（H1）
2. **Mechanism Move 1**：引入 W1，论证 W1 如何 modify X→Y（H2: X × W1）
3. **Warrant 1**：文献/理论支撑 W1 的调节机制
4. **Mechanism Move 2**：引入 W2，论证 W2 如何 modify W1 的调节作用（H3: X × W1 × W2）
5. **Warrant 2**：文献/理论支撑第二层嵌套机制
6. **Prediction**：导出 two-way 和三向交互假设

**骨架**:
```
[Anchor] As discussed, [IV] [increases/decreases] [DV] because [baseline mechanism]. 
Therefore, we hypothesize: H1: [IV] is [direction] related to [DV].

[Mechanism Move 1] We expect [W1] to [buffer/amplify] the [positive/negative] effect 
of [IV] on [DV]. When [W1] is high, [mechanism that modifies baseline].
[Warrant 1] This is because [theoretical reason] ([citation]).
[Prediction 2] Therefore, we hypothesize: H2: The [positive/negative] effect of [IV] 
on [DV] is [weaker/stronger] when [W1] is high.

[Mechanism Move 2] Whether [W1] can effectively [buffer/amplify] the [IV]→[DV] 
relationship is likely to depend on [W2]. When [W2] is high, the 
[buffering/amplifying] effect of [W1] becomes [stronger/weaker] because [nested 
mechanism].
[Warrant 2] This is consistent with [theory], which posits that [argument] ([citation]).
[Prediction 3] Therefore, we hypothesize: H3: The [buffering/amplifying] effect of 
[W1] on the relationship between [IV] and [DV] is [stronger/weaker] when [W2] is high.
```

**范文来源**:
- Chung, Low, and Rust (2022), *Journal of the Academy of Marketing Science*（CEO confidence × CMO confidence × CMO power; CEO confidence × board independence × CMO confidence）
- Lun, Zurbruegg, Mount & Cheong (2026), *Entrepreneurship Theory and Practice*（EO × COO power × product life cycle；W2 = 注意带宽 / 任务负荷）

**为什么有效**: 通过"先建立 two-way，再在其上叠加 three-way"的递进结构，让读者理解三向交互不是统计补丁，而是有理论层次的边界条件。每一层都有独立的机制解释，避免了一次性抛出复杂交互的认知超载。

**注意事项**:
- 必须先建立 H2 two-way 再进入 H3 three-way，不能跳跃
- W2 必须调节 W1 的调节作用，而不仅仅是另一个独立 moderator
- 两层调节都需要具体机制，不能用 "the effect is stronger when..." 敷衍
- 若研究包含多个 three-way，每个都应遵循相同的序列结构

**反模式**:
- 未建立 H2 直接进入 H3 → 读者不知道三向交互建立在什么基础之上
- W2 只是另一个 two-way moderator → 变成 E3 嵌入型边界条件，不是 E6
- 三向交互缺乏具体机制 → 审稿人会质疑是否为数据驱动
- 两层调节使用相同理论但无递进 → 显得重复而非嵌套

**调用语料**:
- `corpus/variants/E_moderation.md`（E6 序列嵌套调节变体）
- `corpus/subprotocols/intra_tmt_persuasion.md`（下级劝说上级 + 权力放大）
- `corpus/subprotocols/board_governance_boundary_condition.md`（董事会放大型边界条件）
- `corpus/sentences/cost_benefit_calculus.md`（成本-收益计算机制 voice）

---

<!--
pattern_id: multi_source_parallel_mechanism_three_reasons
build_type: 机制推演型
source_papers: ["Darby_2023_MSOM"]
confidence: high
status: ready_for_corpus
-->

## Pattern: Three Parallel Single-Step Mechanisms

**适用场景**: 单一 IV 通过多个并行的、概念独立的微观路径影响同一 DV，且每条路径都有独立文献支撑。
**家族判别（多理由并行三兄弟）**: 与 Width-Type Parallel Mechanism（通用理由 2-3 条）、Four-Reason Parallel Mechanism Derivation（压力枚举）同族——本模式强调『微观机制路径』：每条路径有独立文献且概念独立（Darby 2023: financial interests / CEO power / personal interests）。机制路径须可区分（否则并入 Width-Type）。
**微观动作序列**: Anchor（IV 对 DV 的影响已被初步接受）→ Mechanism Move 1/2/3（每个路径独立展开，配 citation + illustration）→ Prediction
**范文来源**: Darby, Ketchen, Ball & Mukherjee (2023), *Manufacturing & Service Operations Management*（CEO stock ownership → slower recalls via firm-financial interests / CEO power / personal financial interests）

**骨架**:
```
[Anchor] [Prior research / theory] suggests that [IV] may influence [DV], but the specific mechanisms remain underexplored.

[Mechanism Move 1] First, [IV] may influence [DV] because [theoretical reason 1]. [Concrete illustration].
[Mechanism Move 2] Second, [IV] may influence [DV] because [theoretical reason 2]. [Concrete illustration].
[Mechanism Move 3] Third, [IV] may influence [DV] because [theoretical reason 3]. [Concrete illustration].

[Prediction] Overall, whether [mechanism 1], [mechanism 2], or [mechanism 3], we posit:
H[X]: [IV] is [direction] related to [DV].
```

**为什么有效**: 多条机制并行呈现，避免单一路径被审稿人质疑；读者可选择最符合其直觉的路径接受假设。
**注意事项**:
- 三条机制必须概念独立，避免 overlap
- 每个机制后需有 concrete illustration 或 citation
- 若机制间存在因果依赖，应改为 Cumulative 而非 Parallel
**反模式**: 三条机制实为同一路径的不同标签，或仅第一条有理论支撑，其余为“同理可证”。

---

<!--
pattern_id: two_levers_theory_progression
build_type: 机制推演型
source_papers: ["Darby_2026_JOM"]
confidence: high
status: ready_for_corpus
-->

## Pattern: Two-Levers Theory Progression

**适用场景**: 核心理论（如 agency theory）提出多个机制/杠杆，已有文献覆盖其中一个，本文覆盖另一个。
**微观动作序列**: Anchor（理论提出两个杠杆）→ Literature Review（lever 1 已被研究）→ Gap（lever 2 未被研究）→ Mechanism Move（lever 2 如何运作）→ Prediction
**范文来源**: Darby, Wowak, Ketchen & Connelly (2026), *Journal of Operations Management*（agency theory: executive compensation vs monitoring/control；本文研究 monitoring by large institutional investors）

**骨架**:
```
[Anchor] [Theory] suggests that [actors] have [N] key levers to mitigate [problem]: (i) [lever 1] and (ii) [lever 2] ([citation]).
[Literature Review] Extant research has already examined [lever 1] in [context] ([citations]).
[Gap] So we take a logical next step by examining [lever 2].
[Mechanism Move] When engaging in [lever 2], [actors] pay careful attention to whether [agents] make choices aligned with [goals] ([citation]).
[Prediction] Therefore, we hypothesize: H[X]: [prediction].
```

**为什么有效**: 明确本文在理论框架中的位置，避免“另起炉灶”；让读者看到 contribution 是理论的自然延伸。
**注意事项**:
- 两个杠杆必须确实来自同一理论
- 需说明为什么 lever 2 之前被忽视但在本文情境中重要
**反模式**: 两个杠杆实际来自不同理论，或 lever 2 只是 lever 1 的重新包装。

---

<!--
pattern_id: embedded_prose_hypotheses
build_type: 跨类型
source_papers: ["Grewal_Vana_Stephen_2025_JM", "Pupovac_Astvansh_Carrillat_Legoux_2026_POM"]
confidence: medium
status: ready_for_corpus
-->

## Pattern: Embedded Prose Predictions in Conceptual Framework

**适用场景**: 目标期刊偏好 Conceptual Framework 而非独立 Hypotheses 部分；预测数量较多且关系复杂，以散文形式嵌入可保持叙事连贯。
**微观动作序列**: Mechanism Move → Warrant → Embedded Prediction（"we posit/propose/anticipate/predict"）→ Optional Moderator Extension
**范文来源**: Grewal, Vana, and Stephen (2025), *Journal of Marketing*（brand safety: no numbered hypotheses, predictions embedded throughout Conceptual Framework）; Pupovac, Astvansh, Carrillat, and Legoux (2026), *Production and Operations Management*（two-stage screening with asymmetric embedded predictions）

**骨架**:
```
[Mechanism Move] Building on studies that describe [theoretical process] ([citation]), we propose that [IV] serves as information about [mediator antecedent].
[Warrant] Specifically, when [IV condition], [actor] [cognitive/affective response], because [theoretical justification]. Consequently, [mediator state] [direction], which [final mechanism link].
[Embedded Prediction] In detail, because [theoretical reason], we [posit/propose/anticipate/predict] that when [IV condition], [mediator] [direction], which [direction] [DV].
[Optional Moderator Extension] This [effect] also might be moderated by [moderator], such that [conditional prediction].
```

**子变体：两阶段不对称嵌入式预测**

**适用场景**: Conceptual Framework 中使用散文式预测，且预测涉及按顺序展开的两个 screen，其效应方向相反。

**骨架**:
```
[Stage 1 Mechanism] [Cue 1] [direction 1] [outcome] because [mechanism].
[Embedded Prediction 1] Therefore, we [propose/anticipate/predict] that [cue 1] [direction 1] [outcome].

[Stage 2 Transition] In contrast, when [condition], [cue 2] reveals [state].
[Embedded Prediction 2] Thus, we [propose/anticipate/predict] that [cue 2] [direction 2] [outcome].
```

**为什么有效**:
- 保持 Conceptual Framework 叙事连贯性，避免独立假设列表打断理论推演
- 适合 JM/JMR/JCR 等消费者行为期刊的文体偏好
- 每个预测都紧跟其机制依据，降低 "假设从天而降" 感

**注意事项**:
- 每个预测需有明确的方向和条件
- 建议在 Methods 或 Overview of Studies 中明确列出待检验预测，避免读者遗漏
- 散文式预测仍需使用 "we posit/propose/anticipate/predict" 等收敛信号
- 若预测数量过多，建议配合图示（Figure 1）展示整体框架

**反模式**: 若目标期刊要求显式编号假设（如 AMJ/SMJ/ASQ），不要使用此模式；若散文式预测没有明确方向和条件，会变成模糊断言。

---

<!--
pattern_id: counterintuitive_direction_reversal_via_mechanism_substitution
build_type: 机制推演型 / 反直觉预测型（方向反转子类）
source_papers: ["Ilicic_Brennan_2026_JM"]
confidence: medium
status: needs_validation
-->

## Pattern: Counterintuitive Direction-Reversal via Mechanism Substitution

**适用场景**: 论文主效应的方向符号（X→Y 是正还是负）与 field 默认机制推导出的预期相反；作者不凭直觉反转，而是指出默认机制（M_old）错误，替换为新机制（M_new），再由 M_new 内生推导出反转方向。区别于 "Counterintuitive Anchor + Three Parallel Psychological Threats"（tfr_095 / Keeves 2017）：tfr_095 反转的是"同一 IV 对不同 target 有 opposing consequences"（揭露对另一对象的隐藏后果，3 条并行路径收敛到 1 mediator）；本模式反转的是"X→Y 本身的方向符号"，通过 M_new 替换 M_old 解释方向为何反转。

**微观动作序列**: Default-prediction（field 默认机制 M_old 推导出方向 D_default）→ Reversal claim（"this research challenges these assumptions: 实际方向 D_reversed"）→ Mechanism substitution（M_old 错误 → 替换为 M_new）→ Endogenous derivation（M_new 自然推导出 D_reversed）→ Prediction（H1）

**范文来源**: Ilicic & Brennan (2026), *Journal of Marketing*（conservatism 通常 risk-averse → 应更少消费成瘾品；但本文发现 conservatives 更 favorable，因为 sense of agency → 降低 perceived danger）

**骨架**:
```
[Default-prediction] While previous research would suggest that [Group A], who are [trait from default theory M_old], should have [direction-default] responses to [outcome], and [Group B], who are [opposite trait], should have [opposite-default] responses...
[Reversal claim] ...this research challenges these assumptions: [Group A] is linked to [REVERSED direction] responses to [outcome].
[Mechanism substitution] We argue that this is because [Group A] is associated with [new mechanism M_new], which [direction] [mediator], [direction] [outcome]. [Theoretical justification for why M_new, not M_old, governs this domain + citation].
[Endogenous derivation] Because [M_new mechanism], [Group A]'s [mediator state] leads to [direction] [outcome] — the opposite of what [M_old] would predict.
[Prediction] Therefore, we hypothesize: H1: [Group A] is associated with [reversed-direction] [outcome].
```

**为什么有效**: 方向反转比"揭露隐藏副作用"更具签名冲击力——Hook 和 Theory Opener 上立刻抓住读者。但反转的合法性必须由"替换后的机制内生推导"提供：不是任性反转，而是 M_old 在本域不适用 → M_new 适用 → M_new 推出反转方向。审稿人接受反转的前提是接受机制替换。

**注意事项**:
- 反转的方向必须由替换后的 M_new 内生推导，不能是"先有反转再找机制"
- 必须显式命名并否定 M_old（"previous research would suggest... based on M_old"），否则反转显得无的放矢
- M_new 必须有独立理论依据（citation），不能仅为反转而构造
- 适用于 risk/disposition × outcome、moral foundations、political ideology 等有强默认预期的领域

**反模式**: 只声明方向反转而不替换机制（"we find the opposite, trust us"）；用 M_old 同时解释正反两方向（机制过载）；反转方向缺乏理论必然性（M_new 推不出 D_reversed）。

---

<!--
pattern_id: mechanism_targeted_intervention_escalation
build_type: 机制推演型 / 调节效应型 / 干预设计子类
source_papers: ["Ilicic_Brennan_2026_JM"]
confidence: medium
status: needs_validation
-->

## Pattern: Mechanism-Targeted Intervention Escalation（机制靶向干预递进）

**适用场景**: 论文已经建立 `X -> M1 -> M2 -> Y` 的有害路径，需要从“解释现象”推进到“如何削弱现象”。第一层干预改变驱动路径的近端机制 M1；第二层不是另一个任意 moderator，而是提高同一干预的自我关联、显著性或诊断力。Ilicic–Brennan 的结构是：威胁信息把注意从行动转向后果，削弱 agency；第二人称语言进一步增强自我指向，使这一机制干预更强。

**微观动作序列**:
1. **Restate harmful chain**：重申 X 如何经 M1、M2 导致 Y。
2. **Locate intervention point**：解释为何干预应攻击 M1，而非仅要求 Y 改变。
3. **Derive first contrast**：无干预 vs 一般干预，预测 M1、M2 与 Y 的联动变化。
4. **Add relevance intensifier**：说明何种信息形式让同一干预更直接地作用于行动者。
5. **Derive nested contrast**：个人指向/高关联干预相对于一般干预产生更强衰减。
6. **Preserve bilateral logic**：说明效应主要改变哪一组，以及另一组为何相对稳定。

**骨架**:
```
[Baseline chain] [Group A / high-X actors] ordinarily exhibit [high M1], which lowers [M2] and increases [harmful Y].
[Intervention point] [Intervention W] redirects attention from [action/control] to [negative consequences], thereby weakening [M1].
[First contrast] As [M1] falls, [M2] should rise and the Group A–Group B difference in [Y] should narrow.
[Relevance intensifier] This disruption should be stronger when the message uses [self-relevant form], because [attention/self-reference warrant].
[Nested contrast] Thus, [personally directed/high-relevance W] should attenuate the focal pathway more than [generic W], especially for [Group A]; [Group B] is expected to change less because [bilateral rationale].
```

**为什么有效**: 干预不是 Theory 末尾突然追加的实践建议，而是从核心机制反推而来：先定位哪条路径可被改变，再说明信息形式如何提高对该路径的命中率。这样，“what can be done”成为机制理论的边界检验，而不只是 managerial add-on。

**统计映射边界**:
- 若设计只有“无威胁 / 一般威胁 / 个人指向威胁”三个条件，它通常是一个三水平处理及预设 contrasts，不是 `X × W1 × W2` 三向交互。
- H3a/H3b 若同时包含组间差异、组内变化和序列中介，应在 Methods/Results 预先拆成清晰的可检验命题，避免一个假设承担过多统计判断。
- 干预对 M1 的因果作用需由随机化和操纵检验支持；测量到的 M1→M2→Y 路径仍需额外的时间或操纵证据。

**反模式**: 直接操纵结果变量而声称“机制干预”；第二层只换文案但没有自我关联理论；用“一组显著、另一组不显著”代替正式的组间/contrast 差异检验；将三水平处理误称为三向交互。

---

<!--
pattern_id: mismatch_subtype_refinement_hypothesis
build_type: 机制推演型 / 假设树型
source_papers: ["Du_Tsolmon_2024_ORSC"]
confidence: low
status: needs_validation
-->

## Pattern: Mismatch Subtype Refinement Hypothesis (主效应后的 mismatch 子类型递进)

**适用场景**: 当主效应是 match/similarity → outcome（如 H1: structural similarity → retention），且 mismatch 内部存在可理论化的类型差异时（哪种 mismatch 类型的 actor 更有价值）。适用于 fit/match 类研究的精细化假设设计。
**结构**: Main Effect (H1: match → outcome) → Subtype Consideration (type of construct under mismatch) → Mechanism-Based Type Advantage → H2 (mismatch → type A outcome)
**范文来源**: Du and Tsolmon (2024), *Organization Science*（H2: mismatch 中 LM managers 比 MM managers 更易留存，因 PAI 需要协调能力）

**骨架**:
```
[Subtype consideration] Next, we consider how the type of [construct] may shape 
[outcome] when [match condition] is misaligned. In such [situations], the degree of 
misalignment of [construct] may differ for [actor] with [type A] or [type B] [construct].

[Mechanism-based type advantage] Because [outcome process] requires [capability X], 
[type A actor] may be better equipped to [support process]. As a result, when 
[structures are misaligned], [type A actor] may be relatively more valuable to 
[decision maker] than [type B actor], whose experience emphasizes [B's focus] 
rather than [A's focus].

[Hypothesis] H[N]. [Mismatch condition] is positively associated with [outcome] 
for [type A actor].
```

**连接词要求**:
- 开启细化: "Next, we consider how the type of [construct] may shape [outcome] when [misaligned]."
- 机制反推: "Because [process] requires [capability], [type A] may be better equipped..."
- 对比强化: "whose experience emphasizes [B's focus] rather than [A's focus]."

**为什么有效**: H2 不是 H1 的调节，而是 H1 在 mismatch 情境下的**子类型精细化**——假设体系有层次感；用机制需求反推类型优势（整合需要协调 → LM 擅长协调 → LM 在 mismatch 中有价值），比"可能更好"的推测更有理论力。

**注意事项**:
- 子类型优势必须有独立的机制论证（不能只是"可能更好"）——用[过程]需要什么能力反推哪类 actor 擅长该能力
- type A vs type B 的区分必须基于真实的构念差异
- mismatch 子类型假设不能与主效应矛盾（H1 说 match 好，H2 不能说 mismatch 更好，只能说"在 mismatch 中 type A 相对好"）
- 主效应假设（H1）必须先建立，子类型假设（H2）才有递进的基础

**反模式**: 子类型优势无机制论证（"type A may be more valuable" 无 because）；类型区分是操作化差异而非构念差异；H2 与 H1 方向冲突（暗示 mismatch 反而更好）。

---

<!--
pattern_id: developmental_reversal_reciprocal_asymmetry
build_type: 机制推演型 / 共演互构型
source_papers: ["Pollock_Lee_Jin_Lashley_2015_ASQ"]
confidence: high
status: ready_for_corpus
-->

## Pattern: Developmental Reversal of Reciprocal-Causation Asymmetry（pollock2015 H1a/H1b 型）

**适用场景**: 两个构念相互因果（coevolution / simultaneous / reciprocal causation），研究问题不是任一构念的绝对效应，而是**两个构念相互影响的不对称方向**——且这个不对称方向**随一个发展性连续调节变量（如年龄、经验、阶段）而反转**。典型于 status↔reputation、legitimacy↔performance、learning↔performance 等共演/互构关系。

**与相邻模式的区别**:
- 不同于 **Sign-Flipping Boundary Condition**（Pontikes）：后者是同一 IV→DV 的符号因受众反转；本模式反转的是**两个构念间相互因果的相对大小**，不是单一关系 的符号
- 不同于 **Counterintuitive Direction-Reversal via Mechanism Substitution**（Ilicic & Brennan）：后者通过替换机制反转 X→Y 符号；本模式不替换机制，而是用两个构念的**时变态特性差异**（malleability / stickiness / equilibrium tendency）内生解释不对称方向为何随发展反转
- 不同于 **Symmetric Opposing Dual-Track**（Zhao-Ding & Gaba）：后者是两个离散条件产生镜像效应；本模式是一个**连续发展变量**在两端的非对称反转

**微观动作序列**:
1. **Coevolution baseline**（两个构念正向互构，"unsurprising" 故不立正式假设）
2. **Asymmetry anchor**（引入两构念的时变态特性差异：A 更 malleable / B 更 sticky）
3. **Early-stage mechanism**（发展早期：A 必须先于 B 建立 → A 对 B 的影响更大）
4. **H1a**（早期不对称方向）
5. **Late-stage mechanism**（发展后期：B 达到 equilibrium 稳定 → B 对 A 的影响更大）
6. **H1b**（后期不对称方向反转）

**范文来源**: Pollock, Lee, Jin, and Lashley (2015), *Administrative Science Quarterly*（status↔reputation coevolution; age reverses which construct drives the other）

**骨架**:
```
[Coevolution baseline] Because both [construct A] and [construct B] provide benefits that
aid in developing the other construct, we expect them to have a positive relationship as
they coevolve. As this expectation is unsurprising, we do not present a formal hypothesis,
but it does form our baseline assumption.

[Asymmetry anchor] Though we expect [A] and [B] to positively influence each other, we do
not expect the nature of this relationship to remain constant over time. [Theoretical
property: e.g., A is more malleable and must be continually reinforced, whereas B, once
established, is sticky and tends toward equilibrium].

[Early-stage mechanism] During its early years, [actor] has little [B]; what [B] it has is
largely inherited from [founder/source]. To enhance [B], [actor] must first build [A] via
[action]. [Theoretical justification of why A must precede B]. Thus, while [A] and [B]
enhance each other, [A] needs to be developed before [B] can be changed.
[Early prediction] H1a: When [actors] are young, [A] will have a greater effect on [B] than
[B] will have on [A].

[Late-stage mechanism] But as [actor] ages and its [B] increases as a function of its [A],
[actor] should be able to access the [B-benefits] that make it easier to continue being
successful, thereby enhancing [A]. To the extent that a new [B-equilibrium] is established,
over time [actor]'s [B] should stabilize and be less susceptible to changes in [A].
[Late prediction] H1b: When [actors] are older, [B] will have a greater effect on [A] than
[A] will have on [B].
```

**为什么有效**: 把"哪个构念驱动哪个"这一共演核心问题，与一个可观测的发展变量（年龄）绑定，使不对称方向**可检验且可反转**——比静态的"A 影响 B"更有理论精度。早期/后期机制各自由两构念的**时变态特性差异**内生推出（malleability → A 先行；equilibrium → B 后稳），无需替换机制即可解释反转。

**配套——"unsurprising baseline, no formal hypothesis" 子动作**: 共演/互构论文通常有一个 trivially-true 的正向互构基线。用 "As this expectation is unsurprising, we do not present a formal hypothesis, but it does form our baseline assumption" **显式拒绝把它立成假设**，把理论精力与假设编号集中到非平凡的不对称方向上。这是 coevolution 论文的标准 baseline 处理，可单独迁移到任何 reciprocal-causation 设计。

**注意事项**:
- 必须先论证两构念的**时变态特性差异**（stickiness / malleability / reinforcement need / equilibrium tendency），这是反转的内生依据
- 早期与后期机制必须**各自独立**（不能后期只是"反之亦然"），且都从同一组构念特性推出
- 适用于 simultaneous-equation / reciprocal-causation / coevolution 设计；H1a/H1b 需配合**跨方程系数比较检验**（Wald χ²，参见 write-methods 同时方程 / write-results 跨模型系数比较）
- 同架构可复用于第三变量的 DV-条件效应随发展翻转（pollock2015 H3a/H3b：blockbuster deals 影响 status 当年轻、影响 reputation 当年老——因 visibility 是 reputation 的核心但非 status 的核心，且 status 随年龄稳定）

**反模式**: 反转缺乏内生依据（"年纪大了就反过来"无机制）；早期/后期机制不对称（一边详证一边默认）；把正向 baseline 也立成假设（浪费编号且稀释理论焦点）。

---

<!--
pattern_id: differential_persistence_lagged_dv_moderation
build_type: 调节效应型 / 动态面板共演型
source_papers: ["Pollock_Lee_Jin_Lashley_2015_ASQ"]
confidence: high
status: ready_for_corpus
-->

## Pattern: Differential Persistence / Lagged-DV Moderation（pollock2015 H2 型）

**适用场景**: 动态面板/自回归设计中，研究问题不是某 IV→DV 斜率被调节，而是**两个构念的路径依赖（path dependence，即滞后因变量系数 ρ）被一个发展变量差异化调节**——一个构念的 ρ 随发展减弱，另一个不变。理论依据是两构念的**持久性特性差异**（一个 sticky / toward equilibrium，一个须不断 reinforcement）。

**与标准调节（E1）的区别**: 标准 E1 调节的是 IV→DV 斜率；本模式调节的是**滞后因变量（LDV）系数 ρ**——即构念对其自身过去值的依赖程度。这要求动态面板设定（lagged DV as regressor），并把一个理论特性（stickiness vs reinforcement）映射到一个计量参数（persistence）。

**微观动作序列**:
1. **Persistence-property anchor**（两构念的持久性特性差异：A sticky / toward equilibrium，B must be continually reinforced）
2. **Moderator-on-ρ mechanism**（发展变量如何差异化改变两构念的 ρ：A 的 ρ 随发展减弱因 equilibrium 稳定；B 的 ρ 不变因始终需 reinforcement）
3. **Differential prediction**（H2: age 弱化 A 的 ρ，但不影响 B 的 ρ）

**范文来源**: Pollock, Lee, Jin, and Lashley (2015), *Administrative Science Quarterly*（H2: age weakens status persistence but not reputation persistence）

**骨架**:
```
[Persistence-property anchor] Prior research suggests that [construct A] tends to be
"stickier" than [construct B] ([citations]). Once established, [A] orders are relatively
stable and self-reinforcing; [A] tends toward equilibrium over time ([citations]). In
contrast, [B] must be constantly reinforced ([citations]) and therefore changes more easily.

[Moderator-on-ρ mechanism] This suggests that though prior [A] and [B] are positively
related to current [A] and [B], the strength of that relationship may change as [actors]
age and their [A] becomes stabilized. As [actors] age, their [A] standing will achieve
equilibrium and stabilize; while changes in [A] can still occur, [older actors] will more
quickly reestablish a new equilibrium, so [A]-changes in the prior period will have a weaker
effect on [A] in the current period when [actors] are older. In contrast, because [B] needs
to be continually reinforced, it is always susceptible to changes in prior [B]; thus the
effect of changes in prior [B] on current [B] will not weaken as the [actor] ages.

[Differential prediction] H[N]: [A] in one period will have a weaker influence on [A] in
the next period as [actors] age, but the relationship between an [actor]'s past [B] and its
current [B] will be unaffected by its age.
```

**为什么有效**: 把一个抽象理论特性（stickiness / reinforcement asymmetry）**直接映射到一个可估计的计量参数**（LDV 系数 ρ 的差异化变化），使"status 比 reputation 更 sticky"这一长期被声称但难检验的理论命题获得**动态面板层面的可检验形式**。假设措辞本身就是"差异化调节"（一个 ρ 减弱，一个不变），比单一方向调节更精确。

**注意事项**:
- 必须先建立两构念的**持久性特性差异**（stickiness / equilibrium / reinforcement need），这是差异化预测的理论依据
- 调节对象是**滞后因变量系数 ρ**，不是 IV→DV 斜率——需在 Methods 中用动态面板（Arellano–Bond / GMM）估计，在 Results 中报告 ρ 随 age 的交互（参见 write-methods 动态面板-GMM / write-results OLS-FE 路径依赖解释）
- "differentiated moderation"（一减一不变）措辞必须精确——不能写成两个都减弱或两个都不变
- **零结果**（B 的 ρ 不随 age 变化）需在 Results 中做统计功效分析（如 Monte Carlo power analysis）以排除 type II error（参见 write-results 零结果功效分析）

**反模式**: 声称持久性差异但不映射到 ρ（停留在"status 更 sticky"的口号）；差异化预测缺乏理论依据（为何一个减弱一个不变）；零结果不报告功效分析即下结论。

---

<!--
pattern_id: belief_updating_attention_threshold_reversal
build_type: 机制推演型 / 调节效应型（阈值反转子类）
source_papers: ["Schumacher_Keck_Tang_2020_SMJ"]
confidence: high
status: needs_validation
-->

## Pattern: Belief Updating → Attention-Threshold Reversal（Schumacher–Keck–Tang 2020 型）

**适用场景**: 行动者根据相对参考点的反馈选择风险/保守行动；稳定偏差改变其对未来状态的信念；当预期状态接近生存、合规或资源约束阈值时，行动目标会从“达到抱负”切换为“避免失败”。研究要解释的是：偏差既如何改变常规区间的反馈反应，又为何在临界区间导致条件关系反转。

**微观动作序列**: Baseline target choice → Bias inserted into belief parameter → Feedback updating → Ordinary two-sided response → New threshold changes decision objective → Bias displaces threshold crossing → Conditional direction reversal → Prediction.

**范文来源**: Schumacher, Keck, and Tang (2020), *Strategic Management Journal*（CEO 能力高估改变绩效反馈解释；接近生存水平时注意目标切换，过度自信使切换发生得更晚）。

**骨架**:
```text
[Baseline target choice] [Actor] chooses between [risky] and [conservative] actions to maximize the chance of exceeding [aspiration/reference target].

[Bias insertion] [Biased actor] overestimates [own ability/resource], so the same observed feedback produces a more favorable posterior belief about future performance than it does for [unbiased actor].

[Ordinary regime: negative side] Below the aspiration target, this favorable bias reduces the perceived need to adopt the risky action; only sufficiently negative feedback makes risk attractive.
[Prediction 1] Thus, [bias] attenuates the positive relationship between negative feedback and risk taking.

[Ordinary regime: positive side] Above the aspiration target, the same favorable bias makes the conservative action attractive at a less positive feedback level.
[Prediction 2] Thus, [bias] strengthens the negative relationship between positive feedback and risk taking.

[Threshold introduction] When expected performance approaches [survival/constraint threshold], the decision objective changes from reaching aspirations to avoiding failure. Under this objective, conserving variance rather than increasing upside becomes attractive.

[Threshold displacement] Because biased actors overestimate their distance from failure, they cross the attention-switch threshold later than unbiased actors.

[Reversal] Under severe negative feedback, unbiased actors may already conserve to protect survival while biased actors still pursue the aspiration target through risk.
[Prediction 3] Therefore, near [threshold], the conditional effect of [bias] differs from—and may reverse—the ordinary-regime pattern.
```

**为什么有效**:
- 偏差进入一个明确的信念参数，而不是停留在性格标签。
- 正、负反馈分别推导，避免用一句“feedback matters differently”掩盖两侧机制。
- 反转来自**决策目标切换 + 阈值跨越顺序差异**，不要求同一机制同时解释正反方向。
- 模型构件可逐一映射到实证变量：反馈方向、偏差信念、行为选择、外部阈值。

**与邻近模式的区别**:
- 区别于 `counterintuitive_direction_reversal_via_mechanism_substitution`：这里不否定并替换旧机制，而是在临界状态改变当前目标。
- 区别于普通 buffering/enhancing：偏差改变的是何时进入另一决策区间，不只是斜率大小。
- 区别于 competing hypotheses：三条预测由同一模型在不同状态区间统一推出。

**注意事项**:
- 必须独立论证“接近阈值会改变决策目标”；仅有统计 cutoff 不足以建立注意切换。
- 阈值应有外部理论或制度依据，不能为了制造反转从样本中事后搜索。
- 若阈值区间内的斜率本身不显著，应把结论限定为组间异质性，并直接检验系数差异。
- 正式模型只证明在假设成立时的逻辑结果；不能据此宣称行动者真实使用该更新规则。

**反模式**: 用危机 dummy 随意翻转交互方向；在没有目标切换机制时宣称 threshold reversal；只比较“一组显著、另一组不显著”而不做系数差异检验；把模型可导出性误写成机制已被直接观察。

---

<!--
pattern_id: background_as_theory_dual_channel_stage_attenuation
build_type: 机制推演型 (B0)
source_papers: ["Kim_Lee_2026_SMJ"]
confidence: medium
status: EMERGING
story_fidelity: section_variant
related: dual_mechanism_same_direction (argumentation_patterns.md) — 后者收敛到正式 H；本模式允许无正式编号假设
-->

## Pattern: Background-as-Theory Dual-Channel + Stage Attenuation（无正式 H）

**适用场景**: 期刊/设计选择用 **BACKGROUND**（或同类 Literature/Conceptual Background）承载 rising-action 理论工作，**不立正式编号假设**；核心是 (1) 两条同向、概念独立的 B0 机制通道解释 pre-outcome 优势；(2) 其中一条通道带**信息稀缺依赖**的阶段衰减预测；(3) 用 stakes/external-validity 论证把既有低成本证据定位为 incompleteness；(4) 用构念对比限定 post-outcome 文献的可外推性。实证问题由 pipeline 阶段自然承接，而非 H1/H2 列表。

**微观动作序列**: Evaluation setting → Channel A (preference/taste) → Channel B (signaling of unobservables) → Stage-attenuation warrant → Evidence synthesis (support) → External-validity incompleteness → Adjacent-construct contrast for later-stage claims → Open empirical agenda (no numbered H)

**范文来源**: Kim & Lee (2026), *Strategic Management Journal*（employer social-responsibility orientation → attraction/selection advantages；signaling 随一手信息增加而衰减；retention 证据有限）

**骨架**:
```text
[Setting] [Actor] evaluations of [employer/offer] are intense at [early stage] and again at [choice stage].

[Channel A — preference] [Attribute X] may be valued as a nonpecuniary job feature because [taste/norm warrant]. Thus seekers may show a [directional preference] for [X] employers.

[Channel B — signaling] Separately, visible [X] can signal [unobservable valued traits] when direct information is scarce. Under this account, [X] positively distinguishes employers in [pre-outcome] choices.

[Stage attenuation] Because signaling is most informative when firsthand information is scarce, advantages tied to Channel B are expected to [attenuate/weaken] after [actors] gain direct experience—implying weaker [post-outcome attachment] predictions from the same attribute.

[Evidence synthesis] Prior [survey/platform/gig/hypothetical] studies support [pre-outcome] advantages for [X] employers [citations].

[External-validity incompleteness] Those settings may overstate [X] advantages: lab/low-stakes preferences need not translate when opportunity costs rise, and [warm-glow-type] responses may weaken as stakes increase. Whether [X] advantages hold in [high-stakes full-time] markets therefore remains open.

[Adjacent-construct contrast] Evidence that [optional activity/program participation] raises retention answers a different question than whether [X-as-employer-attribute] improves retention; the latter remains limited.

[No formal H closure] The section therefore motivates multi-stage empirical questions without numbered hypotheses; Methods/Results carry stage-specific tests.
```

**为什么有效**:
- 双通道同向收敛解释 pre-outcome，却用**信息条件**把 durability 写成可证伪的阶段边界，而不是硬写成无条件的 retention 主效应。
- External-validity 段把 Intro 的 Incompleteness knot 钉在 Theory 内，避免变成单纯文献综述。
- 活动 vs 雇主属性对比防止用错误文献填补 retention 缺口。
- 无正式 H 时仍完成 rising action：机制 → 阶段预测 → 证据边界 → 开放议程。

**与邻近模式的区别**:
- 区别于 `dual_mechanism_same_direction`：后者以 “Accordingly, we hypothesize: H[N]” 收束；本模式**禁止伪造 H**。
- 区别于 B2 双轨：B2 要求两维度产生**差异化/对称反向**预测；本模式两通道对 pre-outcome **同向**，差异在**阶段耐久性**。
- 区别于调节效应型 E：衰减是信息阶段边界，不是正式 W×X 交互假设。
- 区别于质性过程理论 D：不建立 Phase1→Phase2 过渡条件模型；阶段来自就业 pipeline，非过程理论化。

**诚实边界（Background-as-Theory）**:
- 仅当期刊惯例/设计明确允许无编号假设（常见于部分 SMJ empirical、自然实验/描述性 pipeline 文）时使用。
- 不得把“开放问题”改写成假的 H1–Hn 以迎合 write-theory 默认模板。
- 不得声称已检验 mediation；通道保持 B0。
- 若作者实际立了正式 H，应改用 `dual_mechanism_same_direction` 或标准 B0 收束，不调用本模式。
- write-theory 生成时：输出“阶段研究问题 / empirical agenda”映射表，而非强制 `storyline_id` 假设表；paper-state 可用 `hypotheses: []` + `empirical_agenda` 字段（若 schema 尚未支持，保留 provisional 注释）。

**注意事项**:
- Channel A 与 Channel B 必须概念独立；若只是同义改写，删并为一通道。
- 阶段衰减必须锚定在**信息稀缺逻辑**，不能仅说 “effects may differ over time”。
- External-validity 段是 incompleteness 论证，不是 Inadequacy（勿声称既有机制“错误”）。
- Retention 对比段只限定可外推边界，不自动推出“无 retention 效应”假设。

**反模式**: 无机制双通道却写成长文献综述；把活动参与文献直接当作雇主属性预测；为通过模板伪造编号假设；把 signaling 衰减写成已验证中介消失；把 stakes 关切标成 Inadequacy-primary。
