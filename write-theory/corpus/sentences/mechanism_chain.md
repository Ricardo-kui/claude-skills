# 机制推演句语料库

## Why chain 连接词谱系

```
"X affects Y because [mechanism]." 
→ "[First-order effect] occurs when [condition]."
→ "This in turn generates [second-order effect] because [reason]."
→ "Consequently, [DV] [increases/decreases/changes] through [final mechanism step]."
```

**因果链信号词**：
"Consequently," / "As a result," / "This in turn" / "Thereby" / "Thus" / 
"Through this process," / "These dynamics suggest that" / "Building on this logic,"

---

## 单步机制链（基础）

**模板**：
```
"When [IV condition holds], [first-order consequence] occurs because [mechanism step 1]. 
Consequently, [DV outcome] emerges through [final link]. Thus:"
```

**语料锚定**：
- Darby 2024 (MSOM) — recall speed → spillover 单步链

---

## 两步机制链（标准）

**模板**：
```
"When [IV condition holds], [first-order consequence] occurs because [mechanism step 1]. 
This [first-order consequence] in turn generates [second-order consequence] because 
[mechanism step 2]. Consequently, [DV outcome] emerges through [mechanism step 3]. 
Thus:"
```

**语料锚定**：
- Wu 2025 (OrgSci) — digital transformation → routine updating → innovation
- Keeves 2017 (AMJ) — 标准两步链范式

---

## 双轨并行机制链（Track A / Track B）

**Track A（损失规避/保护路径）**：
```
"[X_A] reflects '[定义]' ([文献]). However, this [状态] remains vulnerable to 
[威胁]. Since [机制] are highly sensitive to [波动源], even small changes can 
dramatically alter their worth, creating powerful incentives for [主体] to protect 
[X_A] ([文献]). To illustrate, consider [具体数字例子]."

"According to [理论]'s focus on [心理机制A], [主体] are likely to take actions 
to minimize these losses. More specifically, we propose that [主体] might [行为]. 
Therefore: H[N]: [X_A] → [Y] (+)"
```

**Track B（追求/增益路径）**：
```
"[X_B] reflects '[定义]' ([文献]). [高X_B主体] are oriented toward [长期目标]. 
[文献] supported this distinction, demonstrating that [证据]."

"We argue that [高X_B主体] are more likely to prioritize [长期目标] by opting 
for [开放行为]. While [情境] may have short-term negative impacts, [正面重framing]. 
[短期行为] might yield short-term benefits. However, as information emerges, these 
tactics are likely to be revealed, reducing their effectiveness. Furthermore, 
[开放行为] can help [主体] engage [利益相关者], leading to [积极结果]."

"In summary, high [X_B] reduces [主体]'s reliance on short-term [Y]. Therefore: 
H[M]: [X_B] → [Y] (-)"
```

**语料锚定**：
- Malik 2025 (JM) — current wealth (loss aversion) vs prospective wealth (long-term focus)

**轨道切换信号词**：
"Conversely" / "In contrast" / "Whereas" / "On the other hand"

---

## 辩证对立双路径机制（Dialectical Opposing Indirect Effects, habel2016 型）

**适用**: 同一 IV 通过两条方向相反的中介路径影响同一 DV——正面路径（benefit/gain）和负面路径（cost/loss）同时运作，哪条路径占优取决于调节变量。核心理论贡献是揭示"看似统一的关系实则是两条对立路径的净效应"。

**与已有双轨变体的区分**:
| | 辩证对立双路径 (habel2016) | 双轨并行 (malik2025) | 对称反向双轨 (zhao-ding_gaba) | 竞争机制链 |
|---|---|---|---|---|
| IV | 同一 IV | 两个不同 constructs | 同一 construct 的两个维度 | 同一 IV |
| 中介 | 两个方向相反的 M | 两个独立 M | 两个 DV | 两种竞争理论 |
| DV | 同一 DV | 同一 DV | 两个 DV | 同一 DV |
| 调节 | 嵌入双路径推演 | 无 | 无 | 无 |
| 理论框架 | 单一理论统摄双路径 | 两个理论分别驱动 | 同一 construct 分维度 | 两种理论竞争 |

**模板**:
```
[Theory] suggests that [IV] potentially affects [DV] through two opposing mechanisms. 
On one hand, [IV] increases [DV] through [positive path: IV → M1 (benefit) → DV]—
specifically, [step 1a: how IV increases perceived benefit], which in turn [step 1b: 
how benefit improves DV]. On the other hand, [IV] decreases [DV] through [negative 
path: IV → M2 (cost) → DV]—specifically, [step 2a: how IV increases perceived cost], 
which in turn [step 2b: how cost deteriorates DV].

[Optional: Focus group / qualitative evidence as empirical grounding]
All [qualitative study] participants acknowledged [evidence for positive path]. For 
example, [Respondent A] noted, "[quote supporting benefit]." However, participants 
also brought up and critically discussed [evidence for negative path]. [Respondent B] 
asserted, "[quote supporting cost]."

[Moderation embedded in dual-path reasoning]
We argue that which path prevails depends on [moderator]. When [moderator = high], 
[positive path logic: why benefit path strengthens]. When [moderator = low], [negative 
path logic: why cost path strengthens].

[Convergence to hypotheses]
In line with this reasoning, we derive [N] formal hypotheses:
H1: [Moderated overall effect of IV on DV]
H2a: [Positive indirect effect through M1, moderated by W]
H2b: [Negative indirect effect through M2, moderated by W]
```

**语料锚定**:
- habel2016 (JM) — CSR engagement → perceived benefit (warm glow) / perceived price markup → price fairness; attribution moderates which path prevails

**关键特征**:
- **"two opposing mechanisms" / "opposing indirect effects"** — 核心标记词，明确告知读者这不是单一机制
- **双路径共享同一理论框架** — benefit 和 cost 都来自 distributive justice 的 benefit-cost comparison，不是两个不同理论
- **调节嵌入双路径推演** — attribution 不是假设后补丁，而是在 T3 机制推演中自然出现："which path prevails depends on..."
- **Focus group 引述作为 empirical grounding** — 在正式假设前插入定性证据，增强双路径的可信度
- **H2a/H2b 成对假设** — 两个间接效应假设对称呈现，共享同一 moderator 但方向相反

**Focus group 引述句式**:
```
All [N] focus groups participants acknowledged [evidence for path A]. For example, 
[Respondent ID] noted, "[direct quote]." However, participants also brought up and 
critically discussed [evidence for path B]. [Respondent ID] asserted, "[direct quote]."
```

**可迁移性**: **极高** — 适用于任何"正面效应被负面副作用削弱"的研究场景：
- CSR/ESG → mixed effects (benefit vs cost/greenwashing)
- 制度压力 → compliance vs decoupling
- 技术采纳 → empowerment vs threat
- 多元化 → creativity vs conflict
- 并购 → synergies vs integration costs

**适用期刊**: JM, JMR, JCR (消费者行为); SMJ (制度/CSR); MSOM (运营trade-off)

**反模式**:
- 两条路径来自不同理论框架 → 审稿人质疑 "为什么不统一？"——必须有 overarching theory 统摄
- 调节变量无独立理论依据段落 → 必须在 T3 中有 attribution theory / signaling theory 等支撑
- Focus group 引述替代理论推演 → 定性证据是支撑而非替代——每条路径仍需独立的理论论证
- 只呈现显著路径的结果 → 必须同时报告正负两条间接效应，即使某条不显著

---

## Focus Group / 定性证据嵌入机制推演（habel2016 型）

**适用**: 在正式假设推导前，用 focus group / 访谈引述为双路径机制提供 empirical grounding。特别适合消费者行为、营销学、组织行为研究中"直觉路径需要现实证据支撑"的场景。

**模板（正路径支撑）**:
```
All [N] focus group participants acknowledged [evidence for positive path]. In the eyes 
of the focus group participants, these benefits range from [benefit range description]. 
For example, [Respondent ID] noted, "[direct quote supporting benefit]." [Respondent 
ID] elaborated, "[elaboration quote]."
```

**模板（负路径支撑）**:
```
In all [N] focus groups, participants brought up and critically discussed the question 
of [cost dimension]. Participants agreed that [cost inference description]. For example, 
[Respondent ID] asserted, "[direct quote supporting cost]." Similarly, [Respondent ID] 
noted, "[elaboration quote]."
```

**模板（路径竞争转折）**:
```
As outlined previously, [IV] potentially increases both the benefits and the costs 
[actors] associate with [outcome], leading to opposing indirect effects of [IV] on [DV]. 
We argue that the strengths of these effects depend on [moderator]. In other words, 
under certain circumstances the positive effect... might prevail, while under other 
circumstances the negative effect... might prevail.
```

**语料锚定**:
- habel2016 (JM) — T3 "Perceived benefits" 和 "Perceived costs" 段落中嵌入 6 段 focus group 引述（Respondent B, Q, G, F, A, K）

**关键特征**:
- **Respondent ID 匿名化** — "Respondent B" / "Respondent Q" 而非真名，保护隐私
- **正负路径各有独立引述段** — 不是在同一段中混杂，而是分 "Perceived benefits" 和 "Perceived costs" 子节
- **"brought up and critically discussed"** — 表示负路径不是研究者引导的，而是参与者自发提出的
- **引述后立即回到理论** — "How do these benefit perceptions translate into [DV]? As we have discussed, [theory] suggests..." — 定性证据不替代理论推演

**使用条件**:
- 必须先完成 focus group / 访谈，且引述是真实的（不可编造）
- 引述数量适中（每条路径 2-3 个），不过多占用 Theory 篇幅
- 方法论细节移至 Web Appendix，Theory 中只保留关键引述

**反模式**:
- Focus group 引述篇幅过长（>500 词）→ 压缩为 2-3 个最有力引述
- 引述后无理论回归 → 必须用 "How do these perceptions translate into [DV]?" 等句式回到理论推演
- 只有正路径有引述、负路径无引述 → 对称性要求双路径都有 empirical grounding
- 用引述替代理论论证 → 引述是支撑，不是替代；每条路径仍需独立的理论论证

## 对称分组双路径调节机制（Group-Based Dual Track for Moderation）

**适用**：同一自变量（X）对两个不同群体（Group A / Group B）产生相反效应的交互假设推导。不同于"竞争机制链"（两种理论竞争），这里是**同一理论框架下两个对称子群体的独立机制推演**。

**模板**：
```
We theorize that [IV] differentially influences [DV] because of [overarching theoretical mechanism] 
([citations]).

[Group A path]: [Group A], who [core characteristic A], tend to [value/priority A] ([citations]). 
[Specific reasoning: why IV signals alignment with Group A's values]. [Additional mechanism/logic 
with citation]. Thus, [Group A] should feel [DV outcome A] when [IV condition].

[Group B path]: In contrast, [Group B], who [core characteristic B], tend to [value/priority B] 
([citations]). [Specific reasoning: why IV signals misalignment with Group B's values]. 
[Additional mechanism/logic, e.g., reactance theory, with citation]. Thus, [Group B] should feel 
[DV outcome B] when [IV condition].

In light of the [tension type] we have explicated, we hypothesize the following interaction:

H[N]. [IV] (a) [increases/decreases] [DV] for [Group A] and (b) [decreases/increases] [DV] 
for [Group B].
```

**语料锚定**：
- employee_free_speech (OS) — censorship increases psychological safety for liberals (value congruence with safeguards) but decreases for conservatives (psychological reactance to autonomy threat)

**关键特征**：
- 两组论证完全对称，各占相近篇幅（避免一方充分、一方浅薄）
- 每组都有独立的理论依据和文献支撑
-  overarching theoretical mechanism 统摄两组（如 ideological differences）
- 假设形式为交互假设（H1a + H1b），无传统主效应假设
- 结尾用 "In light of the [tension] we have explicated" 收敛到交互假设

**反模式**：
- 两组逻辑不对称（如 Group A 有 3 层机制，Group B 只有 1 层）→ 审稿人质疑选择性论证
- 缺乏 overarching theory 统摄两组 → 看似两个独立论文拼接
- Group B 的机制只是 Group A 的反面（"相反，Group B 不这么认为"）→ 需独立机制
- 未解释为什么同一 IV 对两组产生相反效应（必须有理论解释，不能只是经验发现）

**与竞争机制链的区别**：
| 维度 | 竞争机制链 | 对称分组双路径 |
|------|-----------|--------------|
| 核心问题 | 哪种理论正确？ | 同一 IV 对不同群体的差异化效应 |
| 两条路径关系 | 互相排斥（A 对则 B 错） | 同时成立（A 对 Group 1, B 对 Group 2） |
| 假设形式 | 竞争假设对 | 单一交互假设（H1a + H1b） |
| 收敛信号 | "Given these competing arguments..." | "In light of the tension we have explicated..." |

---

## 竞争机制链（路径 A vs 路径 B）

**竞争预告**：
```
"However, the literatures on [领域A] and [领域B] offer potentially conflicting 
arguments as to the influence of [X] on [Y]."
```

**路径 A**：
```
"On the one hand, [X_high] may [increase/decrease] [Y] because [mechanism_A]. 
Research suggests that [X_high] are more [特征] and, correspondingly, [行为] 
([文献]). In other words, this research argues that [X_high] tend to [行为2]."
```

**路径 B**：
```
"On the other hand, [X_low] may [increase/decrease] [Y] because [mechanism_B]. 
Indeed, research indicates that [结果] can be particularly [后果], so [X_low] 
who tend to focus on [价值] may be more motivated to [行为3] ([文献])."
```

**语料锚定**：
- Wowak 2025 (MS) — liberal vs conservative CEO recall behavior

---

## 辩证对立型机制推演（Dialectical Contrast Mechanism，kalaignanam2017 型）

**适用**: 研究的核心是比较两种对立选项（A vs B，如 make vs buy, internal vs external, organic vs acquired）的优劣，而非单一 IV→DV 的因果链。理论贡献在于识别每种选项在何种条件下更优。

**与竞争机制链的区别**: 竞争机制链是两种理论对同一关系的竞争预测（哪种理论正确？）；辩证对立型是对立选项各自的优劣对比（两种选项各在什么条件下更优？）。

**骨架（Option A 优势段）**:
```
Previous research has noted two critical advantages of [Option A]: [advantage 1] and [advantage 2] ([citation]). In the case of [context], [Option A] enables firms to [mechanism detail]. [Related theory] contends that [Option A] is a superior mechanism because [theoretical justification] ([citation]). The reason is that [elaboration]. This benefit is crucial in the case of [context] because of [condition].
```

**骨架（Option B 优势+局限段）**:
```
In contrast, [Option B] offers the benefit of [alternative mechanism] ([citations]). However, [limitation of B]. The implication is that [consequence for B].
```

**收敛到 Baseline 假设**:
```
The preceding arguments highlight the trade-offs associated with [decision]. At the time of [process], [Option B] has a distinct advantage over [Option A] because [reason B]. Therefore, [Option B] should offer higher [DV1] compared with [Option A]. In contrast, [Option A] is superior to [Option B] for [DV2] because [reason A]. [Additional justification]. These [advantage category] benefits of [Option A] translate to higher [DV2] and overcome the [disadvantage] the firm experiences at [time point]. Drawing on these arguments, we advance the following baseline hypotheses:

H1: [Option B] has a more positive impact on [DV1] than [Option A].
H2: [Option A] has a more positive impact on [DV2] than [Option B].
```

**语料锚定**:
- kalaignanam2017 (JM) — H1/H2 推导: NPD buy 的"early start"+pay-for-performance → immediate quality 优势；NPD make 的 control+adaptation+learning → future quality 优势

**关键特征**:
- "two critical advantages" — 预告双机制
- "In the case of... enables firms to..." — 情境化机制
- "The reason is that..." — 追加一层解释
- "This benefit is crucial... because of..." — 建立边界条件意识
- "In contrast" — 对称转向另一选项
- "However" — 暴露另一选项的局限
- "The implication is that..." — 推导 consequence
- "trade-offs" — 统一主题词
- "overcome the [disadvantage]" — 建立时间动态（短期劣势 vs 长期优势）

**反模式**:
- 只呈现一方优势 → 审稿人质疑选择性论证
- 优劣对比后无"trade-off"主题收束 → 沦为罗列而非理论整合
- 缺少时间/条件维度 → 无法解释"为什么两种选项共存"

**适用期刊**: JM, JMR, JOM, MSOM（偏好实践 trade-off 类研究）；AMJ/SMJ 需更强的理论承诺

---

## 数字实例化机制句

**适用**：金融/会计概念（option value, stock price sensitivity）、概率/统计概念

**模板**：
```
"To illustrate, consider [主体] holding [具体参数]. A [百分比] decline in 
[变量] to [新参数] would cause [百分比] loss of [指标], as [解释]. Similarly, 
[文献] found that [实证证据]. On average, [统计数字]."
```

**语料锚定**：
- Malik 2025 (JM) — "$99 strike price... A 1% decline in stock price to $99 would cause a 100% loss of the option's intrinsic value"

**QC**：数字例子必须明确标注 "To illustrate"（非 "For example"）

---

## 并行多源机制链 (Parallel Multi-Source Mechanism)

**模板**：
```
"First, [mechanism 1 description with theoretical basis]. Second, [mechanism 2 description with theoretical basis]. Third, [mechanism 3 description with theoretical basis]. Overall, whether it is due to [M1], [M2], or [M3], we posit: [Hypothesis]."
```

**语料锚定**：
- Darby 2023 (MSOM) — CEO stock ownership → recall timing (multiple parallel mechanisms converging on one hypothesis)

---

## 宽度型三理由并行机制 (Width-over-Depth: Three Parallel Reasons)

**适用**: 主效应单一且IV特征丰富——每个IV→DV关系由3个独立的平行理论理由支撑，而非深度多步中介链。用论证密度(多角度独立论证)补偿论证深度(单步因果链)。

**模板**:
```
Applying [theory] to [empirical domain], we [first] argue that [IV dimension] will motivate 
[agents] to [DV action]. Central to [IV dimension] is the "[core driver]" which inspires 
[motivational tendency] ([citations]). [Agents high in IV], therefore, are motivated to 
[behavioral implication] ([citations]). [Bridge: why this motivation naturally maps to DV].

[Reason 1 — first theoretical attribute of IV]:
Specifically, [reason 1 chain: attribute → mechanism → DV mapping] ([citations]). 
Therefore, [partial conclusion 1]. Indeed, [amplification] ([citations]). Further, 
[extended implication] ([citations]). As such, [summary of Reason 1 chain].

[Reason 2 — second theoretical attribute]:
Additionally, [IV dimension] is associated with [second attribute] ([citations]). 
[Mechanism: how attribute 2 maps to DV] ([citations]). Similarly, [parallel evidence] 
([citations]). [Additional amplification].

[Reason 3 — third theoretical attribute]:
Finally, [IV dimension] is associated with [third attribute] ([citations]). 
[Mechanism: how attribute 3 maps to DV]. Further, [extended implication]. 
Therefore, because of [cumulative summary of 3 reasons], we believe that [hypothesis].

[Hypothesis]: [IV] will be [positively/negatively] associated with [DV].
```

**语料锚定**:
- gamache_etal2020 (SMJ) — H1: prevention focus → governance initiatives (3 reasons: duty/obligation→shareholder primacy + worry/safety→board monitoring + rules/accuracy→accountability)
- gamache_etal2020 (SMJ) — H3: promotion focus → social initiatives (3 reasons: ideal self→broad goals + temporal distance + optimism/errors-of-omission)

**关键特征**:
- **"Additionally... Finally..." 为理由间标准节奏标记** — 创造"论证累积"的阅读感受
- **每个理由独立但共同指向同一结论** — 三个理由是理论上的三角互证(triangulation)
- **与 OM "三三制"的区分**: OM三三制的三个原因对应三种不同层面的机制(心理→结构→认知)，宽度型的三个理由来源于IV的不同属性(ought self的三个manifestation)
- **收敛句必须汇总全部三个理由**: "Therefore, because of [理由1], [理由2], and [理由3], we believe that..." — 不能只提最后一个理由
- **与并行多源机制的区分**: 并行多源机制(M1+M2+M3→same Y)是三个不同的中介机制，宽度型是三个平行理由而非三个中介

**与其他架构的区分**:
| | 宽度型三理由 | 并行多源机制 | 两步机制链 |
|---|---|---|---|
| 结构 | 3个平行理由 → 同一假设 | 3个独立中介 → 同一假设 | 1个因果序列 → 2个假设 |
| 理由/机制关系 | 理由来自IV的不同属性 | 机制来自不同的理论或文献 | 机制是因果序列的步骤 |
| 论证类型 | 三角互证 (triangulation) | 多路径汇聚 (multi-path convergence) | 链式递进 (chain) |
| 收敛 | 一个主效应假设 | 一个主效应假设 | 多个假设 (X→M, M→Y) |

**反模式**:
- 三个理由概念重叠(如 "duty" 和 "obligation" 是同一概念的两种说法) → 审稿人质疑 "这真的是三个独立理由？"
- 理由数量不对称(第一个理由有4句论证，第二个只有1句) → 暗示某些理由是事后添加的
- 只用 "This is also consistent with [theory]" 代替独立的理由论证 → 必须为每个理由提供独立的why chain
- 收敛句只提最后或最强的一个理由 → 让读者忘记前两个理由的存在
- 在机制推演型(纯主效应)中使用此架构但所有理由的机制深度都只有单步 → 审稿人可能质疑 "为什么不选最强的一个理由做更深的链？"

---

## 对称三步机制链（CEO 心理特质 → 企业战略 通用骨架）

**适用**: CEO 心理/情感特质（PA/NA、anxiety、hubris 等）对企业战略行为（CSR、recall、innovation 等）的影响机制。两条路径完全对称、方向相反。

**PA 方向（正向/扩展路径）**:
> "Drawing on the [theory], we expect that [IV_positive] will be positively related to [DV]. First, [IV_positive] broadens a [actor]'s scope of [mechanism domain 1: cognition], enabling [actor] to [cognitive consequence] ([citations]). Second, high-[IV_positive] individuals tend to [social mechanism], which [social consequence] ([citations]). Third, the [theory] proposes that [IV_positive] enlarges individuals' [mechanism domain 3: temporal], enabling [actor] to [temporal consequence] ([citations])."

**NA 方向（镜像/收缩路径）**:
> "Conversely, we expect that [IV_negative] will be negatively related to [DV]. First, [IV_negative] narrows a [actor]'s scope of [mechanism domain 1], preventing [actor] from [cognitive consequence] ([citations]). Second, high-[IV_negative] individuals tend to [opposite social mechanism], which [opposite social consequence] ([citations]). Third, the [theory] proposes that [IV_negative] shortens individuals' [mechanism domain 3], leading [actor] to [opposite temporal consequence] ([citations])."

**语料锚定**:
- wang2024 (SMJ) — PA/NA → CSR via broaden-and-build theory。PA: broaden attention → social inclusion → extended time horizon。NA: narrow attention → social exclusion → shortened time horizon。

**关键特征**:
- **三步完全对称**: 认知层（broaden/narrow attention）→ 社会层（inclusion/exclusion）→ 时间层（extended/shortened horizon）
- **每步 1-2 个 citation**: 机制链不是空泛推测，每步都有文献支撑
- **镜像对立**: NA 不是 PA 的"缺失"，而是独立但方向相反的过程——体现 broaden-and-build 理论的对称性
- **理论名称贯穿始终**: 每段开头重述 "Drawing on the [theory]" / "According to the [theory]"，确保读者记住理论锚点

**可迁移性**: **极高** — 适用于所有 CEO 心理特质 → 企业战略类论文。三步可替换为其他理论层：
- 认知层（attention, information processing）
- 社会层（social relationships, stakeholder perception）
- 时间层（time horizon, future orientation, temporal discounting）

**骨架模板（填空式）**:
```
Drawing on the [theory], we expect that [IV] will be [positively/negatively] related to [DV].
First, [IV] [mechanism verb] a [actor]'s scope of [mechanism domain]...
Second, high-[IV] individuals tend to [social mechanism]...
Third, the [theory] proposes that [IV] enlarges individuals' [temporal mechanism]...
```

**反模式**:
- 三步中只有两步有文献支撑 → 审稿人会质疑 "第三步是不是你自己编的？"
- NA 路径被写成 PA 的"反面"而非独立过程 → 必须用 "Conversely" 而非 "Similarly" 开头
- 三步之间缺少连接词 → 每步之间用 "First... Second... Third..." 明确标记节奏

---

## 用文献支撑机制（非罗列）

**模板**：
```
"[Research stream] has shown that [specific mechanism element]. [Author A (year)] 
found that [specific finding], suggesting that [theoretical interpretation]. 
[Author B (year)] extended this logic by demonstrating that [additional mechanism 
element]. Together, these studies suggest that [synthesis], yet they have not 
considered [gap that current hypothesis addresses]."
```

**反模式**：
❌ "(Author A, 2018; Author B, 2019; Author C, 2020)" — 无 argument 总结
✅ "Author A (2018) found that [finding], suggesting that [interpretation]..."

---

## Dual-Theory Architecture Variant (Mayo et al. POMS)

When explaining how [IV] affects [DV] differently across phases/conditions, use two distinct theories:

**Theory A for Phase 1:**
"We leverage [theory A] to help explain the relationship between [IV] and [DV] in [phase 1]. [Theory A] is a framework that explains [core premise] ([foundational citations]). [Theory A] is framed by studies finding evidence that [key behavioral pattern]."

**Theory B for Phase 2:**
"Theoretical support for [behavior in phase 2] is found in [theory B]. [Theory B] proposes that [core premise] and that [implication]. Consequently, when [condition], [actor] may [behavior]."

**Key rule:** The two theories must be conceptually independent (not overlapping mechanisms). If they overlap, use a single overarching theory instead.

---

## 双理论分别解释不同 DV 变体（kalaignanam2017 型）

**适用**: 同一自变量（或两个对立选项）对两个不同结果维度（如 immediate vs future, short-term vs long-term, quantity vs quality）产生差异化影响，每个结果维度由一个独立理论解释。

**与标准 Dual-Theory 的区别**: 标准变体是两个理论解释同一现象的不同阶段/条件；本变体是两个理论分别解释两个不同的 DV。

**Theory A 框架（解释 DV1）**:
```
There are two streams of research pertinent to understanding [outcome domain]. [Theory A], a dominant theoretical lens, focuses on [unit of analysis] and argues that [core premise] ([citation]). Whereas an extensive body of literature has focused on [topic A] ([reviews]), studies [topic B] are less common ([exception]). As noted previously, the key challenge in [topic B] is [specific difficulty]. [Stakes statement: why this is surprising given importance].

Using insights from [Theory A] and [Theory B], we develop a conceptual framework that delineates [scope]. [Figure reference]. The model depicts [overview of relationships for DV1]. The choice of examining these moderating variables is guided by the observation that [core trade-off]. These moderating variables bring into sharp focus the conditions that strengthen or exacerbate the benefits and challenges accompanying [choices].
```

**Theory B 框架（解释 DV2）**:
```
The second relevant stream of research for understanding [outcome domain] is [Theory B]. A key insight from this stream of literature is that [Option A] is inherently a superior mode for [process] ([citations]) compared with [Option B]. [Outcome] improvement often takes the form of a [metaphor]. Our conceptualization of [process] mirrors [theoretical tradition]. Here, [process] is represented as [definition] ([citations]). Typically, [process] in organizations is characterized by [feature] and is punctuated by [disruption]. In this tradition, [process] occurs when there is [indicator]. In the context of [domain], improvement in [outcome] is an indicant of [process] ([citation]).
```

**语料锚定**:
- kalaignanam2017 (JM) — TCE (Williamson 1985) 解释 immediate product quality（交易成本→短期控制/激励）；Organizational Learning (Levin 2000; Cyert & March 1963) 解释 future product quality（学习曲线→长期适应/编码）

**关键特征**:
- **明确宣告双理论架构**: "There are two streams of research..." / "The second relevant stream..."
- **理论分工清晰**: 每个理论对应一个 outcome 维度，无重叠
- **过渡自然**: "Using insights from [Theory A] and [Theory B], we develop..." 在 Theory A 末尾预告 Theory B 的参与
- **对称对比结构**: Theory A 段落解释 Option A vs B 在 DV1 上的优劣；Theory B 段落解释 Option A vs B 在 DV2 上的优劣

**假设推导节奏**:
1. **Baseline 假设（H1/H2）**: 分别从两个理论推导主效应方向
2. **Moderator 假设（H1a/H1b/H2a/H2b）**: 每个 moderator 小节对应一个 baseline 假设，论证逻辑完全平行

**反模式**:
- 两个理论解释同一 outcome → 应合并为一个理论或改为标准 Dual-Theory 架构
- 理论分工不清晰 → 审稿人会问"为什么 TCE 不能解释 future quality？"
- 缺少"trade-off"主题串联 → 两个理论沦为并列的文献综述，失去统一叙事

**适用期刊**: JM, JMR, SMJ（偏好双理论整合）；ASQ 慎用（偏好单一深入理论）

---

## Ability-Motivation 双路径机制框架（Eilert 2017 型）

**适用**：组织决策、企业行为、战略响应类主题中，将机制论证系统性地组织为能力维度和动机维度

**模板**:
```
We expect [IV] to be related to [DV] because of its impact on [theoretical mechanism 1: ability] 
and [theoretical mechanism 2: motivation].

[Ability path]: The ability of the firm to [act] is closely linked to [condition]. 
In this regard, [IV] will trigger "[search type]" or [search description] in firms. 
However, [search type] search behavior is [limitation] in that [explanation] ([citation]). 
Therefore, although [general condition], the firm's ability to provide a quick response 
to [IV condition] is especially limited.

[Motivation path]: When [event], apart from [action 1], the firm also strives to 
[action 2] ([citation]). [Action 2] becomes more consequential for [IV condition], 
especially because [reason]. However, [consequence] might [negative outcome] among 
[actors] ([citation]). The ensuing response would be similar to that predicted by 
the "[auxiliary theory]" hypothesis ([citation]), in which [theoretical prediction].

[拍3-证据]: Research has also shown that [stakeholders] are more likely to [punish] 
[IV condition] than [comparison] ([citations]). Furthermore, [consequence] are more 
likely in cases of [IV condition], and therefore, the stakes are higher. Thus, as 
[IV] increases, firms will also be motivated to [behavior].

[拍4-收敛]: Overall, when [condition], [prediction]. We offer the following baseline hypothesis:

H1: [IV] [direction] [DV].
```

**关键特征**：
- Ability 路径通常涉及知识、资源、专长、流程、搜索能力
- Motivation 路径通常涉及政治成本、声誉保护、问责规避、利益冲突
- 两条路径独立论证，最后 Overall 收敛到同一假设
- 可在 motivation 路径中嵌入辅助理论（如 threat-rigidity, prospect theory, accountability theory）增强说服力
- 假设树型论文中，每个 moderator 小节重复使用该框架：moderator 通过增强/削弱 ability 和 motivation 来改变主效应

**语料锚定**：
- Eilert 2017 (JM) — H1: problem severity -> time to recall (ability via problemistic search myopia; motivation via accountability avoidance + threat-rigidity)
- Eilert 2017 (JM) — H2/H3: each moderator explained via ability + motivation alignment

**可视化工具**：可用 Table 2 式矩阵呈现（Ability / Motivation / Net Effects / Rationale）

**反模式**：
- Ability 和 motivation 路径区分模糊 → 审稿人质疑 "这难道不是同一个机制？"
- 两条路径推导方向矛盾而未解释 net effect → 必须明确总体方向
- 辅助理论引用后未解释其与本理论框架的关系 → 必须建立联系

**连接词模式**：
- Ability -> Motivation 过渡: "When [event], apart from [action 1], the firm also strives to..."
- Motivation -> 辅助理论: "The ensuing response would be similar to that predicted by the '[theory]' hypothesis..."
- 证据 -> 收敛: "Overall, when [condition]... We offer the following baseline hypothesis:"

---

## 替代机制排除骨架（Alternative Mechanisms）

**适用**：提出中介机制后，系统排除其他竞争解释，增强核心机制的排他性论证

**排除预告**:
```
"While we propose that [mediator] is a primary mechanism that explains the relationship 
between [IVs] on [DV], it is important to consider other potential mechanisms."
```

**替代机制 1**:
```
"[Alternative M1]. When [condition], they may be viewed as [attribute]. In addition, 
[IV condition] may also [affect M1], and [M1] has been linked to [DV] ([citations])."
```

**替代机制 2**:
```
"[Alternative M2] is another potential mechanism. Specifically, [mechanism logic]. 
[Behavior] may mitigate this perception because [rationale] ([citation])."
```

**替代机制 3**:
```
"A final alternative mechanism is [Alternative M3]. [Actors] who are [condition] may 
appear overly [attribute] when they engage in [behavior] because [mechanism] ([citation]). 
The [opposite attribute] nature of [intervention] may mitigate [outcome] ([citation])."
```

**核心机制辩护（Overarching Mechanism Defense）**:
```
"While the [N] mechanisms discussed above are plausible, we focus on [mediator] as our 
key mechanism for two reasons. First, we focus on [mediator] because [mediator] has been 
more directly linked with [core concept] in prior work ([citations]). Indeed, [mediator] 
is often perceived as [moral/social attribute] by observers ([citation]) and thus more 
directly relates to [phenomenon] than [M1], [M2], and [M3]. Second, [mediator] is an 
attribute that is considered particularly relevant by observers in [context], which may 
increase its salience over these other attributes ([citations]), meaning that it may be 
particularly relevant when considering how observers respond to [behavior]."
```

**语料锚定**:
- kundro_rothbard (AMJ) — Alternative Mechanisms section (warmth, competence, dominance)

**关键特征**:
- 每个替代机制 2-3 句，独立成段
- 替代机制的选择必须基于文献（不能随意发明）
- 核心机制辩护通常给出 2 个理由（直接相关性 + 情境显著性）
- 反模式：只列替代机制而不解释为何排除；替代机制与核心机制在概念上重叠

---

## 多理论整合骨架（Multi-Theory Integration）

**适用**：用多个理论共同解释同一现象，每个理论承担不同的解释功能

**理论部署声明**:
```
"To understand [phenomenon], we draw on [N] types of [理论类别], those based on [维度A] 
([citations]) and those based on [维度B] ([citations]), and discuss their interplay. 
We argue that [理论A] and [理论B] have implications for [核心问题]."
```

**理论 C（机制理论）引入**:
```
"Moreover, we draw on [理论C] to understand why [前因] elicit [后果]. Indeed, [理论C] 
suggests that when [条件], observers [反应]. Specifically, when [具体条件], [详细后果]."
```

**三理论分工原则**:
- **理论A**（基线理论）：解释基线期望（如 Power role theory -> 高权力者被期望采取 agentic 行为）
- **理论B**（差异理论）：解释群体/情境差异（如 Gender role theory -> 男性和女性面临不同期望）
- **理论C**（机制理论）：解释过程/后果（如 Expectancy violation theory -> 期望违背如何导致负面评价）

**语料锚定**:
- kundro_rothbard (AMJ) — Power role + Gender role + Expectancy violation theory 整合

**关键规则**:
- 每个理论必须承担**独立且不可替代**的解释功能
- 若两个理论解释同一机制，应合并为一个更上位的理论
- 理论引入的顺序通常遵循：基线->差异->机制

**反模式**:
- 三理论沦为 citation list，未说明各自承担什么功能
- 理论之间逻辑重叠（如理论A和理论B都解释同一机制步骤）
- 理论C（机制理论）未与前两个理论建立逻辑联系，孤立存在
- 引入顺序混乱（如先讲机制理论再讲基线理论），读者无法建立认知框架
- 每个理论只有1句话介绍，未展开其核心前提

---

## OM "三三制"机制推演骨架（Shen et al. JOM 型）

**适用**：OM/SCM 领域解释某一治理策略/构念为何影响运营绩效，每个机制对应一个运营改进要素

**主效应骨架**:
```
"We suggest that [IV] may [direction] [DV] for three reasons. First, when firms [condition], 
they may [psychological/behavioral consequence], which decreases [capability 1] ([citations]). 
As [context] control significant resources, [IV] enable firms to obtain [benefit]. As a result, 
[actor] may become complacent and believe that [assumption]. Thus, they may pay less attention 
to [core activity]. [Additional downstream effect].

Second, the [benefit] of [IV] may lead to [structural consequence], preventing firms from 
[action 1]. When firms [condition], they also have an implicit obligation to [obligation]. 
For example, [specific case illustration with concrete details]. Therefore, [IV] may impair 
firms' independence in [domain].

Third, the [benefit] of [IV] may lead to [cognitive/behavioral lock-in] and hinder a firm's 
ability to [capability 2]. The benefits... may cause senior executives to [cognitive bias], 
distracting them from [core activity] ([citations]). Such a focus... will decrease the search 
for [innovation target], leading to [negative outcome]. Therefore, we propose the following 
hypothesis:

H1. [IV] is [direction] related to [DV]."
```

**语料锚定**: shen_zhou_wang_zhang (JOM) — "Political ties and operational efficiency"

**关键特征**:
- "for three reasons" 预告三点并行机制
- 三个原因分别对应：**心理/动机层**（complacency）、**结构/流程层**（structural lock-in）、**认知/学习层**（path dependence）
- 每个原因都嵌入具体企业案例（Dahu Aquaculture, General Motors, Dayang Group）
- 三个机制对应连续运营改进的三个要素（motivation, waste reduction, learning）
- "Therefore, we propose the following hypothesis:" 作为收敛信号

---

## Trade-off → Shock → Dominance 逻辑链（hoffmann2024 型）

**功能**: 适用于政策冲击/法律变化类研究——treatment 的作用机制是移除了对既存激励的约束，而非直接引入新激励。

**核心逻辑**: Agent 面临私人激励 A 和制度约束 B 之间的权衡 → 外生冲击削弱了 B → A 在权衡中占主导 → 行为变化

**句法模板**:
```
[Agents] face a trade-off between (1) [private incentive — e.g., avoiding immediate costs] 
and (2) [disciplinary threat — e.g., being sued by shareholders]. 
We expect that the external shock of [shock name]—which diminishes [disciplinary threat]—
leads [private incentive] to gain prominence in the aforementioned trade-off 
and come to dominate [agents'] decision making.

This expectation is grounded in [primary theory] literature documenting [core mechanism] 
([citation]) and [domain] literature on how [mechanism] can [behavioral outcome] ([citation]).
```

**关键特征**:
- **Trade-off 框架**: 将行为决策框定为两种对立力量的权衡，而非单向因果链
- **外生冲击的角色**: Treatment 不是直接推动行为，而是移除了一个制衡力量——让既存的私人激励不再被约束
- **"gain prominence and come to dominate"**: 动态语言描述权衡重心的转移过程
- **双文献锚定**: 核心理论文献（如 agency theory）解释权衡本身，领域文献（如 myopic management）解释特定情境下的行为表现

**Concession-Rebuttal 先导模式**:
在 Trade-off 链之前，常用 Concession-Rebuttal 建立"为什么私人激励更强"：
```
Under some conditions, [action] could be beneficial ([citations on long-term benefits]).
However, [action] has numerous negative implications ([citations on short-term costs]).
As these negative consequences reflect badly on [agents'] perceived skills,
they prefer not to be associated with them ([citation]).
While one could argue that [potential benefit] could prevent [undesirable action],
based on [decision theory], "losses loom larger than gains" ([citation]).
Hence, we expect that [cost] will not outweigh [benefit] in [agent's] mind.
```

**与标准机制推演的区分**:
| | Trade-off → Dominance | 标准 X→M→Y |
|---|---|---|
| Treatment 性质 | 制度冲击（移除约束） | 直接干预（引入新变量） |
| 机制逻辑 | 权衡失衡 | 因果传导 |
| Theory 定位 | 解释为什么私人激励在约束移除后占主导 | 解释 X 通过 M 影响 Y 的过程 |
| 代理问题 | 核心（管理者 vs 股东利益冲突） | 可有可无 |

**适用**: 政策冲击/法律变化/制度变革研究，其中 treatment 移除或削弱了一个既存的治理/监督机制。特别适合 agency theory 驱动的 Incompleteness × Mechanism 组合。

**语料锚定**: hoffmann_cheong_phan_zurbruegg2024 (JM) — UD laws → reduced litigation risk → managerial opportunism → fewer recalls

**禁忌**: 
- 不能用于 treatment 直接引入新激励的场景（如补贴、税收优惠）——此时用标准 X→M→Y
- Trade-off 的两个力量必须有明确的文献支撑，不能是纯推测

**调节器推导"三三制"骨架**:
```
"We predict that [moderator] [strengthens/weakens] the [direction] impact of [IV] on [DV]. 
First, as [moderator condition], [mechanism 1 modification]. [Reasoning with citation]. 
Firms' loss of [previous advantage], in turn, shifts their attention to [alternative focus], 
motivating them to [action].

Second, [mechanism 2 modification]. In [low moderator] contexts, [condition]. However, 
[moderator change] creates [new condition] ([citations]), reducing [negative outcome]. 
As a result, [actor] can maintain [positive behavior].

Third, [mechanism 3 modification]. In [context with moderator change], [actor] are less 
likely to [previous behavior] ([citations]). Instead, they may develop [new mindset]. Such 
a mindset helps [actor] [positive action] ([citations]). Thus, [IV] become [more/less] 
harmful to [DV].

H[N]. The [direction] relationship between [IV] and [DV] is [stronger/weaker] when [moderator] 
is [high/low] rather than [low/high]."
```

**语料锚定**: shen_zhou_wang_zhang (JOM) — H2-H5 推导段落

**关键特征**:
- 每个调节器段落都重复 "First... Second... Third..." 结构
- 三个子机制与主效应的三个机制**严格对应**（complacency ↔ motivation; lock-in ↔ waste reduction; path dependence ↔ learning）
- "Thus, [IV] become [more/less] harmful to [DV]" 作为段落收敛
- 调节方向必须可由三个子机制共同支持（若某子机制推导方向与其他两个矛盾，需解释 net effect）

**反模式**:
- 三个原因概念重叠（如 "complacency" 和 "lack of motivation" 实为同一机制）
- 调节器的子机制与主效应的子机制不对应（审稿人会质疑"为什么这个调节器不影响机制3？"）
- 三个原因中有一个仅基于常识而无文献支撑 → **反模式"常识谚语作为机制"**：用 folk wisdom（"don't fix something not broken"）替代理论文献。实证证据：shipilov_greve_rowley2019 (SMJ) 中基于 complacency 常识谚语论证的 H1b/H2b 在实证中被反转

---

## "双刃剑"理论框架骨架（Double-Edged Sword）

**适用**：某一策略/构念既有明显好处又有隐性坏处，需要系统呈现理论视角下的两面性

**好处面呈现**:
```
"According to the [theoretical lens], [IV] can benefit firms by [benefit 1] and [benefit 2]. 
First, [IV] provide opportunities for [specific benefit] ([citation]). Second, they offer 
firms [benefit 2 details] ([citations]). They also serve as [benefit 3] ([citations]). Many 
studies have focused on the advantages of [IV] and shown their [positive] impacts on [outcome 1] 
([citations]) and [outcome 2] ([citations])."
```

**坏处面呈现**:
```
"However, the [theoretical lens] also suggests the potential downsides of [IV]. [Citation] 
posits that when [condition], firms are obliged to [negative obligation]. [Citation] suggests 
that [IV] may also [downside 2]. [Citation] indicates that [downside 3]. Consistent with 
these arguments, an emerging body of empirical work has shown that [IV] can have an 
[insignificant/negative] impact on [outcome] ([citations]). Given such findings, recent 
studies have underscored '[cost phrase]' ([citation]) and noted that it is a '[strategic 
choice phrase]' ([citation])."
```

**统一机制提炼**:
```
"Although earlier studies have indicated various reasons for the dark side of [IV], we identify 
that they all have an implicit focus on [mechanism theme]. That is, although [IV] can benefit 
firms' [A], they may also impair their [B]. Accordingly, we explicitly examine how [IV] affect 
[DV], an indicator of [B], to illustrate the mechanism underlying the dark side of [IV]."
```

**语料锚定**: shen_zhou_wang_zhang (JOM) — 2.2 Political embeddedness perspective

**关键特征**:
- 好处面与坏处面篇幅大致对称（避免选择性呈现）
- "However" 作为双面转折信号词
- "Although earlier studies... we identify that they all have an implicit focus on..." → **核心提炼句**：将前人分散的 downside 发现统一为一个理论主题
- "That is, although [IV] can benefit firms' [A], they may also impair their [B]" → 用 A vs B 二元框架统一两面性
- 明确将 DV 定位为 B（坏处面）的指标，而非 A（好处面）的指标

**可迁移性**: 高 — 适用于任何涉及"策略既有收益又有成本"的研究
**适用领域**: 政治关联、多元化、并购、联盟、数字化转型等

**反模式**:
- 好处面篇幅远大于坏处面 → 审稿人质疑作者偏见
- "implicit focus" 提炼不准确 → 审稿人质疑"前人研究真的都关注这个吗？"
- A vs B 区分不清晰 → 审稿人质疑"A 和 B 难道不是一回事？"
- 未明确将 DV 定位为 B（坏处面）的指标 → 读者误以为论文也在研究 A（好处面）
- 坏处面只有 citation 罗列无机制解释 → 沦为"文献说不好"而非"理论说为什么不好"

---

## 双中介并行机制链（Dual Mediator Mechanism）

**适用**：解释 X 通过两个概念独立的平行中介（M1, M2）影响 Y，且 X→Y 仍有未测量残余直接路径

**模板**:
```
"We argue that [IV] affects [DV] through two mediating observable [actions/expenditures]: 
[M1] and [M2]. There is also a direct link from [IV] to [DV] to account for other 
(unmeasured) impacts such as [examples].

We expect [entities] with higher [IV] to have lower [M1] and [M2] for several reasons. 
First, [M1] and [M2] are [discretionary attribute] and therefore tend to be [cut] when 
[cash/resources] are needed immediately ([citations]). Second, [M1] and [M2] are 
investments in intangible assets ([citations]). The returns to these assets are not fully 
known or predictable, leading to uncertainty about [near-term outcome]. Third, the 
intangible assets created by [M1] and [M2] are usually firm specific, making them less 
redeployable... they tend to lose a substantial proportion of their market value when 
the [entity] is in financial distress. Finally, very high levels of [IV] can result in 
an 'underinvestment problem' ([citation]).

[Impact of M1 on DV]. [M1] can influence the antecedents of [DV] in several ways. 
[Mechanism A]. [Mechanism B]. Therefore, we expect [M1] to affect [DV] positively.

[Impact of M2 on DV]. [Parallel structure for M2, with independent theoretical grounding].

Following this discussion, we propose that higher [IV] is likely to reduce [M1] and 
[M2], and this in turn will lower [DV] due to [consequence].

H[N]: The (negative) impact of higher [IV] on [DV] is mediated by (a) [M1] and (b) [M2]."
```

**语料锚定**: malshe_agarwal_2015 (JM) — leverage → advertising/R&D → customer satisfaction

**关键特征**:
- X→M 论证使用四阶递进理由（discretionary nature → uncertain returns → low redeployability → underinvestment），每阶增强因果必然性
- 两个中介各自有独立的 M→Y 论证段落
- H1 为中介假设形式而非主效应假设（"X is mediated by M1 and M2" 而非 "X→Y"）
- 显式声明 "a direct link... to account for other (unmeasured) impacts" → 理论完整性标记

**反模式**:
- 两个中介概念重叠（如 Advertising 和 Marketing spending）→ 应为同一中介的两个指标
- 论证理由数量不对称（M1 有四个理由，M2 只有一个）→ 暗示 M2 可能不需要
- X→M 论证只有 citation 无理论理由（"citation X found that leverage reduces advertising" but not WHY）
- 缺少未测量残差声明 → 审稿人推算出其他未测量 mediator 的存在

---

## 双 DV 并行机制链（Twin DV Parallel Mechanism）

**适用**: 同一 IV 通过不同机制影响两个概念独立的 DV，每个 DV 有独立的假设和理论小节

**模板**:
```
"Our first hypothesis concerns [domain Y1]. [Background literature establishing Y1 as 
important and its key antecedents]. Less well understood, however, are the factors that 
affect [Y1's immediate antecedent] ([citations]).

We extend this logic to argue that [actors] with high levels of [IV] will aim to [DV1 
outcome] by engaging in a [mechanism name] process. Specifically, we propose that [IV 
condition] will [behavioral response leading to Y1]. This prediction builds on the idea 
that [core theoretical mechanism — e.g., anxious individuals prefer supportive others] 
([citations]). The '[theory name]' ([core citation]) specifically argues that [detailed 
mechanism — resources provided by DV1, how they reduce IV's aversive state] ([citations]).

[Optional: qualitative evidence — interview quote, illustrative example].

H1: [IV] will induce [actors] to [DV1 outcome].

---

Our second hypothesis pertains to [domain Y2]. [Background literature establishing Y2 
as important]. [Transition sentence linking the same IV to a different outcome]. [Optional: 
conceptual framework showing how IV manifests in Y2 through two primary sub-mechanisms].

We contend that [IV] will affect [actors'] [Y2 outcome] in the following way. Evidence 
from [discipline] indicates that [core behavioral pattern triggered by IV] ([citations]), 
which in turn leads [actors] to [DV2 outcome] ([citations]). By focusing on [psychological 
mechanism], [IV condition actors] will [specific behavioral consequence], which will, in 
turn, [final effect on DV2]. [Additional reasoning about attractiveness of outcomes].

H2: [IV] will induce [actors] to [DV2 outcome]."
```

**语料锚定**: mannor_wowak_bartkus_gomez-mejia_2016 (SMJ) — job anxiety → social buffering (H1) + strategic risk taking (H2)

**关键特征**:
- 两条路径各自独立（独立小节标题、独立理论工具、独立收敛到假设）
- 第二条路径可以比第一条短（reader 已理解 underlying mechanism）
- 两条路径共享 IV→mechanism 逻辑（如 anxiety → threat fixation），但不共享理论工具
- 路径之间用 "In addition to..." / "Our second hypothesis pertains to..." 过渡
- 可使用访谈材料作为机制证据的补充

**与 Dual Mediator 的区分**:
| | Dual Mediator | Twin DV Parallel |
|---|---|---|
| 结构 | X → M1+M2 → Y（同一 DV） | X → Y1（机制A）/ X → Y2（机制B） |
| 假设 | H1: 中介假设 | H1: Y1 主效应; H2: Y2 主效应 |
| 两个路径的关系 | 两个 M 共同解释 Y | 两个 DV 独立被 X 预测 |

**反模式**:
- 两个 DV 由同一机制链接 → 应合并为同一假设的两个方面
- 第二条路径用 "Similarly" 开头 → 暗示两个 DV 的关系相同，失去理论区分度
- 两条路径篇幅极端不对称（给审稿人暗示其中一条路径是事后添加的）
- IV→Y1 和 IV→Y2 使用同一理论工具而无差异化 → 应合并为单路径

---

## 多层收窄型机制链（Macro→Meso→Micro Layered Mechanism）

**适用**: Quasi-experiment 或 exogenous institutional change 研究——机制链从宏观制度层逐步收窄到微观行为层

**模板**:
```
[Section 2.1: Governance/Institutional Mechanism Layer — 宏观层]
[Core construct] can function as a [governance mechanism], as it makes salient for
[actors] that their actions are monitored and that [negative consequence] will have
[consequences] ([citations]). However, much like other types of [governance mechanisms],
[core construct] can have the unintended consequence of [negative behavioral outcome]
([citations]). Prior research suggests that while [governance mechanism] aims to
[intended effect], it instead often [unintended effect] ([citations]).

[Section 2.2: Legislation/Institutional Change Layer — 中观层]
A [specific legislation/institutional change] is a specific type of [institution] that
can reduce [core construct], or at least the perception of that risk ([citations]).
[Technical details of how the institutional change works — eligibility, mechanism,
hurdle imposed]. Because it imposes a significant hurdle for [actors to engage in
behavior], the adoption of [institutional change] is likely to reduce the perceived
level of [core construct] for [target actors]. In fact, prior research shows that
[empirical evidence confirming the change had its intended effect] ([citations]).

[Section 2.3: Strategy/Behavioral Response Layer — 微观层]
For [target actors], the perception of [core construct] may influence the relative
salience and importance of [group A] compared to [group B]. As [salience theory author]
argued, [salience construct] for [actors] increases when a given [stakeholder] possesses
more [dimension 1], [dimension 2], or [dimension 3] ([citation]). Given their limited
cognitive capacity and resources, [actors] cannot attend to all issues to the same
degree ([citations]). Instead, they prioritize based on perceived salience, which
constantly shifts in response to evolving circumstances.

[Core mechanism claim]: We argue that an exogenous [change in core construct] after
[institutional change event] may lead to [shift in salience/attention]. As the
relative salience of [under-attended group] increases, we expect [actors] will shift
attention from [over-attended group] to [under-attended group] and thus engage more
in [target DV].

[Optional: Alternative motivation acknowledgment — theoretical humility]
We make that prediction recognizing that different motivations might underlie the shift.
In line with [theory A], it could be [motivation A]. However, it could also be [motivation
B]. Our prediction allows for both.

H[N]: [Core prediction]."
```

**语料锚定**: park_lange_jeon (SMJ) — Section 2.1 (litigation risk as governance mechanism) → 2.2 (UD law legislation) → 2.3 (stakeholder strategy effect)

**关键特征**:
- 三层递进：宏观制度机制 → 中观制度变化 → 微观行为响应
- 每层 ~150-250 词，各有独立小节标题和理论依据
- 依赖 quasi-experiment/exogenous shock 作为 empirical context
- 2.2 层提供制度的**技术细节**——不仅是 "X law was passed"，而是解释了 law 如何工作、为什么它降低了风险感知
- 可选：理论谦逊声明——承认因果机制的不确定性

**与其他机制链的区分**:
| | 多层收窄型 | 标准两步链 | 双中介并行 |
|---|---|---|---|
| 结构 | Governance → Legislation → Strategy (3层) | X → M → Y (2步) | X → M1+M2 → Y |
| 层级 | 跨分析层次 (macro→micro) | 单分析层次 | 单分析层次 |
| 经验背景 | Quasi-experiment / exogenous shock | Survey / panel | Survey / panel |

**反模式**:
- 三层之间缺少逻辑递进（如 2.1 和 2.2 都可以独立存在但没有 causal link）→ 应为同一因果链的三个放大层次
- 2.2 层只有 legislation name 无技术细节 → 审稿人不理解为什么该 law 降低了风险
- 三层篇幅极度不均（如 2.1 占 60%）→ 最长的层次应有最多的理论贡献

---

## 2×2 并行矩阵架构 (2×2 Parallel Matrix Architecture)

**适用**: IV 按两个独立维度交叉产生 4 个假设，每个单元格有独立但平行的 T3→T4 推演。与发散树的区别：平行矩阵中假设间无层级依赖（H2a 的成立不依赖 H1a 的成立）。

**模板**:
```
[搭建段：共同理论基础]
The starting point of theory on [phenomenon] is that [core premise] ([citations]).
[Entities] monitor [target], detect threats, and decide how to act in response.
Prior work on [phenomenon-entity] relationship has focused on [narrow scope] ([citations]).

[维度独立性论证 — 确保读者理解两个维度是独立而非同一连续体的两端]
It is important to note that [dimension A] is different from the absence of [dimension B].
An increase in [dimension A] means [entity] is increasingly surrounded by [specific A markers]
that are distinct from [neutral/B markers]. [Dimension A] is associated with specific [markers].
Likewise, [dimension B] is different from the absence of [dimension A].

[2×2 矩阵 — 第一行：Source A + Valence]
[Cell 1: Source A × Positive Valence]
[Valence+] should [directional prediction A+] because [mechanism — e.g., complacency/activation].
[Mechanism elaboration with citation]. Therefore:
H[A+]: [Prediction].

[Cell 2: Source A × Negative Valence]
Conversely, [Valence-] should [directional prediction A-] because [opposite mechanism — e.g.,
problemistic search]. [Mechanism elaboration with citation]. Thus:
H[A-]: [Prediction].

[2×2 矩阵 — 第二行：Source B + Valence (learning/network extension)]
While the previous hypotheses capture [Source A effects], [entities] can also learn from
[Source B] ([learning citation]). [Bridge logic: why Source B matters through same channel].
For changes in [domain], [relevant decision makers/ties] matter for diffusion.

[Cell 3: Source B × Positive Valence]
[Valence+] of [Source B] can [mechanism — parallel to Cell 1 but through network channel].
Therefore:
H[B+]: [Prediction].

[Cell 4: Source B × Negative Valence]
[Valence-] of [Source B] can [mechanism — parallel to Cell 2 but through network channel].
Thus:
H[B-]: [Prediction].
```

**语料锚定**: shipilov_greve_rowley2019 (SMJ) — 媒体报道 (own/interlock) × 语调 (positive/negative) → 治理实践采纳。4 个假设按 source × tone 组织，每个单元格有独立 T3 推演。

**关键特征**:
- 两个维度必须有概念独立性论证（"X is different from the absence of Y"）——正/负不是同一连续体的两端
- 第一行建立基线机制（Source A），第二行通过组织学习/"经验传递"桥接扩展到 Source B
- 每行内用 "Conversely" 标记方向反转，保持平行对称
- **"within and across entities" 双重预测声明**：在假设推导末尾明确预告将使用 between-entity 和 within-entity 两种变异——这是 Theory↔Methods 桥梁
- 假设间无层级依赖：每个假设可以独立检验，但共享共同的理论基础

**与其他架构的区分**:
| | 2×2 并行矩阵 | 发散树 | 线性因果链 |
|---|---|---|---|
| 结构 | IV维度A×B → 4 DV 独立预测 | 主效应→条件1→条件2 分叉 | X→M→Y 单链 |
| 假设关系 | 平行（无层级依赖） | 层级（H2以H1为基础） | 递进（H2以H1为前提） |
| 组织维度 | 2个交叉维度 | 1个主效应+1+个moderator | 1个因果方向 |
| 每单元格论证 | 独立T3→T4 | 基线机制→条件化修正 | 链式分步 |
| 实例 | shipilov_greve_rowley2019 | darby2024 | wu2025 |

**反模式**:
- 两个维度未概念独立（如正/负被读者视为同一连续体的两端而非独立维度）→ 必须在 T1 中论证维度独立性
- 四假设篇幅极度不均（某个单元格只有 3 行，另一个 15 行）→ 暗示该单元格是事后添加的
- 第二行只重复第一行的机制而不提供独立的桥接逻辑（"同理可得" 无理论依据）→ 需要 "learning from others" / "spillover" / "contagion" 类桥接理论
- 正负方向用同一常识谚语论证（"don't fix something not broken"）→ 常识不是理论，需特定理论机制支撑每方向
- 四个假设无整体收束 → T6 在假设数≥3 时强制需要

---

## Iron Triangle 三边机制论证（Regulatory Capture Mechanism）

**适用**: 研究涉及企业政治影响力如何通过监管体系传递——行业→立法者→监管者→行业的三边激励交换

**模板**:
```
[External influence framework] ([citations]) outline several mechanisms (e.g., [mechanism list]) that interested parties can use to exert influence. [IV] is prominent as a means to establish [political outcome] ([citations]), which in turn can evoke preferential treatment, manifested in [decision type 1] by [regulator 1] ([citation]), [decision type 2] in [industry 1] ([citation]), or [decision type 3] cases ([citation]). For [DV context], this preferential treatment might take the form of [specific favorable outcome A] or [specific favorable outcome B].

Research on regulation models supports this argument ([citations]). [Author(s)] present a "regulation capture" view that suggests that firms engage in rent seeking for preferential treatment, which leads regulators to make decisions that benefit the firms they are supposed to regulate ([citation]). [Figure reference] depicts this "iron triangle" interaction ([citations]), which includes a broad set of incentive exchanges among [actor 1: government/legislators], [actor 2: regulators], and [actor 3: industry actors].

[Triangle side 1: Industry ↔ Legislators]. Exchanges between [industry] and [legislators] involve firms that leverage their [economic/political resource] to gain influence, such as [specific action]. In return, [legislators] may take actions to promote the firms' interests ([citation]).

[Triangle side 2: Legislators ↔ Regulator]. [Legislators] determine [regulator]'s [resources/constraints]. Due to their political control over bureaucracies ([citations]), [legislators] can use various means (e.g., [means list]) to reward or punish regulatory agencies. Thus, [regulator] may be motivated to take enforcement actions favored by [legislator] and constituents, or else risk punishment.

[Triangle side 3: Industry ↔ Regulator]. Firms interact with [regulator] by leveraging political connections to influence enforcement decisions. That is, firms exert political influences on [legislators], who can use diverse means to sway the decisions of the [regulator] and encourage them to provide preferable treatment to those particular firms.

This discussion suggests that firms deploy strategies to curry favors from regulators. In [DV context], the quest for [legitimacy/social fitness] may involve [IV behavior] to build relationships with regulators. [Regulation theory] further suggests that firms that [IV behavior] more are less likely to be subject to [adverse regulatory action]. Thus, if [IV] facilitates preferential treatment, we should observe [predicted negative relationship between IV and DV].

H1: [IV] has a [negative] association with [DV dimension 1] and [DV dimension 2].
```

**语料锚定**:
- singh_grewal2023 (JMR) — lobbying → voluntary & mandatory recalls。Iron triangle (Adams 1981; Freeman 1965) + regulation capture (Stigler 1971; Peltzman 1976)。三边论证: 行业↔立法者 (campaign contributions, political support), 立法者↔NHTSA (budgets, oversight), 行业↔NHTSA (political connections → enforcement leniency)。

**关键特征**:
- 三边逐一论证而非笼统说 "political influence matters"——每边有独立的机制和证据
- 框架图 (Figure 3: iron triangle) 作为视觉整合
- 双边政治/制度文献 + 监管捕获文献的交叉引用
- 收敛句 "firms deploy strategies to curry favors from regulators" → 将三边机制统一为 "preferential treatment"
- 预测覆盖两个 DV（voluntary + mandatory recalls）但共享同一个机制基础

**反模式**:
- 三边论证中某一边只有 citation 无机制（如 "Legislators control regulators' budgets (citation)" 但未解释 WHY this matters）
- Iron triangle 被引用但三边未逐一展开 → 框架沦为装饰
- 行业↔监管者边的论证与行业↔立法者边重叠 → 需概念区分

---

## 双视角对比+框架整合（Dual-Perspective Contrast + Framework Integration）

**适用**: 理论贡献的核心是展示现有文献使用视角A（如效率视角）而忽略了视角B（如合法性视角），论文通过整合两个视角提供更全面的解释

**模板**:
```
Our conceptual foundation resonates with [perspective A] and [perspective B] from [parent literature] ([citations]) and its [field] offshoots (e.g., [citations]). [IV] does not change [underlying mechanism], so an [perspective A] implies that it should not influence [DV]. But [parent theory] from a [perspective B] ([citations]) would predict a potential relationship between [IV] and [DV]. In turn, a combination of [perspective A] (economic fitness) and [perspective B] (social fitness) perspectives might explain how [actors] cope with [institutional demands] ([citation]).

In [empirical context], an [perspective A] emphasizes [economic consideration 1] and [economic consideration 2], whereas a [perspective B] focuses on whether [actors] are legitimate in the social context, such as whether they [legitimacy-seeking behavior]. [Define legitimacy] ([citation]). Because [actors] risk illegitimacy penalties if they fail to gain recognition as legitimate ([citation]), they often [legitimacy-enhancing action] ([citation]). Such elements arise, indirectly, from concerns about [social fitness] that prompt influential institutions (e.g., [examples]) or mechanisms (e.g., [examples]) to implement features that require organizations to make trade-offs. This duality of [perspective A] and [perspective B] thus provides a more holistic perspective on [actors]' reactions to [institutional pressures].
```

**语料锚定**:
- singh_grewal2023 (JMR) — Efficiency perspective (Meyer & Rowan 1977; Zucker 1987) vs Legitimacy perspective (DiMaggio & Powell 1983; Suchman 1995)。效率视角预测 lobbying 不应影响召回（不改变产品质量）。合法性视角预测 lobbying 可能影响召回（企业通过政治资本构建社会合法性）。

**关键特征**:
- 两个视角有明确的学术 lineage（organizational sociology → marketing offshoots）
- "does not change [mechanism], so [perspective A] implies no relationship" → 先建立 null baseline
- "a combination of A and B might explain how firms cope with institutional demands" → 整合而非排斥
- 从具体 context 中抽象出 duality (economic fitness vs social fitness)
- 引用 Oliver (1991) 作为 A+B 整合的理论合法性来源

**反模式**:
- 两个视角只命名不展开——每个视角必须有至少一段独立的机制解释
- 视角A和B的篇幅极端不对称 → 暗示其中一个视角是装饰性的
- "duality" 声明后无具体 trade-off 或 tension → 需要展示两个视角在什么条件下产生不同预测

---

## 三层嵌套理论演进 (Nested Extension T2 Architecture)

**适用**: 研究使用了从经典到当代的清晰理论演进脉络——经典理论 → 修正理论 → 扩展理论 → 新维度推导

**模板**:
```
Grounded in [classical theory], [practice/phenomenon] has become a common practice to [original purpose] ([citations]). [Actors] are [risk orientation] because they [reason for risk orientation]. In contrast, [counterpart actors] can [action that mitigates risk], making them [different risk orientation]. This "[labeled risk differential]" ([citation]) suggests that [actors] make less optimal decisions by [risk-avoiding behavior]. To address this [agency problem], [classical theory] suggests [solution], aligning their interests with those of [principals]. [Mechanism of alignment]. — an approach commonly termed "[established term]" ([citation]).

The [revised theory], introduced by [Author(s) (year)], posits that [actors] are *[revised assumption]* (from [source theory]; [citation]), in contrast to the classical theory's assumption of *[original assumption]* ([citation]). The [revised theory] argues that [actors] frame decisions as opportunities to either [action A] or [action B] ([citation]).

Extending the [revised theory] ([citations]), the "[extension name]" perspective highlights that [actor] decision-making relies on [cognitive mechanism] about their [reference object], with [mental process] used to manage [cognitive limitation] ([citation]). More specifically, it suggests that decision-makers are influenced by [N] key factors: (1) [factor 1 definition] and (2) [factor 2 definition]. For [actors], [construct A] represents [what could be lost] (the downside), while [construct B] reflects [what could be gained] (the upside). [Actors] with [high construct A] tend to prioritize [short-term strategy] to [protective action], focusing on the downside. Conversely, those with [high construct B] tend toward [long-term strategy] aimed at [pursuit action], making the upside more appealing ([citations]).
```

**语料锚定**:
- malik_wang_martin_gomezmejia2025 (JM) — Classical Agency Theory (Jensen & Meckling 1976) → Behavioral Agency Model (Wiseman & Gomez-Mejia 1998) → Mixed Gamble perspective (Martin et al. 2013)。三层递进: risk aversion → loss aversion → dual-factor heuristics (current vs prospective wealth)。

**关键特征**:
- 三层不是平行理论罗列，而是**进化链条**: 每层是对前一层的修正或扩展
- Layer 1 (Classical): 建立 baseline assumption (risk aversion) + standard solution (incentive alignment)
- Layer 2 (Revision): 用一个理论反转 baseline assumption (loss aversion ≠ risk aversion)
- Layer 3 (Extension): 从单维度推导到双维度——在 Layer 2 的单一 psychological mechanism 基础上加入认知框架 (heuristics, mental shortcuts)
- 每层有独立的 citation lineage
- 最后收敛到双构念—— Layer 3 的 "two key factors" 直接对应论文的两个核心 IV

**与其他 T2 架构的区分**:
| | 三层嵌套 | 双视角对比+整合 | 单理论引入 |
|---|---|---|---|
| 理论数量 | 3 (进化链) | 2 (互补) | 1 |
| 理论间关系 | 修正/扩展 | 互补/整合 | N/A |
| 适用场景 | 从经典到当代的清晰演化 | 发现两个理论视角共同解释现象 | 已有成熟理论可直接应用 |
| 收敛方式 | 从单维度到双维度 | 从对立到整合 | 从理论到预测 |

**反模式**:
- 三层之间没有清楚的修正/扩展关系 → 退化为 literature review
- Layer 1 和 Layer 2 之间的 contrast 不够锐利 ("risk aversion" vs "loss aversion" 的区别需要明确解释)
- Layer 3 的 "two factors" 在 Layer 1-2 中没有伏笔 → 看起来像新变量拼入而非理论演进的自然收敛

---

## 对称反向双轨机制链 (Symmetric Opposing Dual-Track Mechanism)

**适用**: 同一 IV 的两个概念维度对相同 DV 产生对称但方向相反的效应。每个维度的机制链结构完全平行（signal → inference → positioning choice），但每步的方向相反。

**模板**:
```
##### [IV Dimension 1] and [DV 1]
[IV dimension 1] reflects the extent to which [existing units] fall short of [expectations]. 
Higher [IV dimension 1] signals that current [units] do not adequately address [needs], 
indicating [opportunity type]. In our framework, [DV 1 definition and role]. When [IV 
dimension 1] is high, [actors] infer that [inference about DV 1], either because [reason A] 
or because [reason B]. To address [opportunity] and overcome [challenge] ([citations]), 
[actors] are motivated to [action that increases DV 1]. We therefore expect [actors] to 
[directional prediction for DV 1].

##### [IV Dimension 1] and [DV 2]
[IV dimension 1] also provides information about [different aspect]. When [IV dimension 1] 
is high, [actors] infer that [inference about DV 2], including among [reference group]. 
Given [contextual condition], even [reference group]'s [configurations] may represent 
[limitation]. This inference likely encourages [actors] to [action diverging from reference 
group] ([citation]). Rather than [imitative action], [actors] are motivated to [exploratory 
action].

Taken together, we expect that high [IV dimension 1] will lead [actors] to [prediction for 
DV 1] while simultaneously [prediction for DV 2].

##### [IV Dimension 2] and [DV 1] — [对称反向]
[IV dimension 2] captures the extent to which [evaluators] agree or disagree about [target]. 
High [IV dimension 2] suggests that [existing units] only satisfy a subset of [market] 
([citation]). [IV dimension 2], therefore, signals [alternative demand condition] in which 
[description]. This [landscape] complicates [actors]' assessment of [key consideration]. 
When [condition holds], [actors] cannot rely solely on [single strategy]. Instead, they 
recognize that [alternative strategy may be needed]. As a result, [actors] are motivated to 
[action that decreases DV 1] ([citation]). We therefore expect that higher [IV dimension 2] 
will lead [actors] to [directional prediction for DV 1, opposite of Track A].

##### [IV Dimension 2] and [DV 2] — [对称反向]
[IV dimension 2] also shapes how [actors] assess [different consideration]. Although 
[landscape condition] creates opportunities, it also makes [outcome] harder to [achieve] 
([citation]). Under these conditions, [actors] are more likely to adopt [risk-reducing 
strategy] ([citations]). Among [available options], [specific option] become particularly 
attractive as templates ([citation]), because they signal [proven quality]. By [specific 
action], [actors] can [benefit] ([citation]).

In sum, we expect high [IV dimension 2] to lead [actors] to [prediction for DV 1, opposite 
of Track A] while [prediction for DV 2, opposite of Track A].
```

**语料锚定**:
- zhao-ding_gaba (ORSC) — dissatisfaction → core focus (+), peripheral overlap (-); heterogeneity → core focus (-), peripheral overlap (+)

**关键特征**:
- 两条轨道论证结构完全对称（signal → inference → choice），但每步方向相反
- 每个 IV 维度对应两个 DV，分两段独立推导
- 第二条轨道的读者体验是"预测性"的——读完 Track A 后，读者已能预测 Track B 的结构
- 使用 "also provides information" / "also shapes how" 在 DV 段之间过渡
- 每轨道末尾有 "Taken together" / "In sum" mini-closure
- 假设成对出现 (H1a+H1b, H2a+H2b)，每对共享同一 IV 维度

**与已有双轨并行的区分**:
| | 对称反向双轨 (zhao-ding_gaba) | 损失/增益双轨 (malik2025) |
|---|---|---|
| IV 关系 | 同一 construct 的两个概念维度 | 两个不同的 constructs (current vs prospective wealth) |
| DV 结构 | 每轨道 2 个 DV (共 4 假设) | 每轨道 1 个 DV (共 2 假设) |
| 对称性 | 完全对称反向 | 方向相反但机制不完全对称 |
| 收敛 | 每轨道独立 mini-closure | 无轨道级 closure |

**反模式**:
- 两条轨道篇幅极度不对称 → 暗示其中一条轨道是事后添加的
- 第二条轨道直接复制第一条轨道的句式（"Similarly..."）→ 失去了理论区分度
- 两个 IV 维度未论证概念独立性 → 审稿人质疑 "这难道不是同一连续体的两端？"

---

## 2×2 Cell-by-Cell 调节机制矩阵 (2×2 Moderated Mechanism Matrix)

**适用**: 2 IVs (或 1 IV 的两个构念变体) × 2 Moderators 的完整矩阵设计。每个 moderator 类型有共享的机制 preamble，每个 cell 有独立的 T3→T4 推导。对角线 cell 呈现对称反向。

**模板**:
```
[Common Mechanism Preamble for Moderator A]:
[Theory framework for Moderator A] ([citations]). [Core mechanism logic: how Moderator A affects audience/judge perceptions]. [Low vs High comparison]. Thus, whereas [low Moderator A] may generate little or no response, [high Moderator A is] likely to generate significant responses ([citations]).

Because [high Moderator A stimulates mechanism], we argue that differences in [Construct A] and [Construct B]'s [differentiating feature] will lead [Moderator A] to have different effects on how they are treated as cues about [DV]...

[Cell 1: Construct A × Moderator A — positive moderation]:
[Construct A specific mechanism]. [Low Moderator defense: why effect is weak/non-significant at low levels]. In contrast, [high Moderator logic: why effect strengthens]. Thus, we expect [Moderator A] to amplify the relationship between [Construct A] and [DV]:
H1. [Positive moderation prediction].

[Cell 2: Construct B × Moderator A — negative moderation]:
In contrast to its effect on [Construct A], [low Moderator] is likely to enhance, and [high Moderator] is likely to weaken [Construct B]'s relationship with [DV]. [Construct B mechanism baseline]. [Low Moderator amplification]. However, [high Moderator attenuation logic]. We therefore hypothesize,
H2. [Negative moderation prediction, opposite direction from H1].

[Common Mechanism Preamble for Moderator B]:
[Parallel structure — new mechanism framework]. [Core mechanism logic]...

[Cell 3 + Cell 4 follow same pattern with Moderator B]
```

**语料锚定**:
- han_pollock_paruchuri (SMJ) — reputation/celebrity × objective/perceived severity → scandalization。对角线对称: H1↔H4 (positive moderation), H2↔H3 (negative moderation)

**关键特征**:
- **Common mechanism preamble**: 每个 moderator 类型有共享的理论基础段，避免在每个 cell 中重复相同机制
- **Cell-by-cell derivation**: 每个 cell 有独立的 T3 推导，cell 之间用 "In contrast to its effect on..." 过渡
- **对角线对称**: 2×2 矩阵的对角线呈现对称反向——体现理论设计的 elegance
- **Low→High moderator progression**: 每个假设先论证低 moderator 时的效应，再论证高 moderator 时的转变
- **假设全为调节形式**: 无双主效应假设——调节逻辑是理论核心
- 每个假设推导包含 4 拍: 方向→机制(Low→High)→证据→收敛

**与已有架构的区分**:
| | 2×2 Cell-by-Cell | 对称反向双轨 (zhao-ding_gaba) | 2×2 并行矩阵 (shipilov) |
|---|---|---|---|
| IV 结构 | 2 个不同 constructs | 1 个 construct 的 2 个维度 | 2 个独立交叉维度 |
| Moderator | 2 个 moderators | 无 (纯主效应) | 无 (纯主效应) |
| 假设数 | 4 (全调节) | 4 (全主效应) | 4 (全主效应) |
| 对角线对称 | ✓ (H1↔H4, H2↔H3) | ✓ (H1a↔H2a, H1b↔H2b) | ✗ |

**反模式**:
- 4 个 cell 的篇幅极度不均 (某 cell 3 行，另一个 15 行) → 暗示该 cell 是事后添加的
- Moderator preamble 过于相似 → 两个 moderators 的概念独立性存疑
- 无双主效应但未解释为什么 → 审稿人会问 "为什么不检验主效应?"

---

## Y-shaped 架构 (Y-Shaped: Common Trunk → Dual Path → Contingency Branches)

**适用**: 统一机制基础 → 两个群体产生相反主效应 → 弱势群体的效应进一步被 contingencies 调节。非对称设计（contingencies 只在一条路径上展开）。

**模板**:
```
[Trunk — Shared Mechanism Preamble]:
[Core mechanism: how IV affects the system]. [Established finding: IV → ecosystem-level outcome]. 
But this does not address [firm-level concern].

[Path 1 — Advantaged Group]:
For [Group A], [IV] improves clarity on its position to [succeed]. [Mechanism: why Group A benefits]. 
[Specific advantages 1, 2, 3]. → H1: [IV] REDUCES [DV] for [Group A].

[Path 2 — Disadvantaged Group]:
For [Group B], [IV] makes it LESS clear if it can [succeed]. [Mechanism: why Group B is hurt]. 
[Specific disadvantages 1, 2, 3]. → H2: [IV] HEIGHTENS [DV] for [Group B].
Note that H2 works against the general notion that [IV] should [opposite effect].

[Contingency Branches on Path 2]:
A key part of H2 is that [core difficulty for Group B]. Thus, H2 should be pronounced in 
situations where [difficulty is amplified].
→ H3: [Amplifying factor] → accentuates H2 (+)
→ H4: [Buffering factor A] → attenuates H2 (-)
→ H5: [Buffering factor B] → attenuates H2 (-)
```

**语料锚定**: toh_pyun (SMJ) — standardization → standard-owner (↓uncertainty) / non-standard-owner (↑uncertainty) → strong rival (+), complementary tech (-), production assets (-)

**关键特征**:
- **非对称**: contingencies 只在一条路径 (H2) 上展开——H1 侧无对应调节
- **"Note that H2 works against the general notion..."** → 直接标注反直觉性
- 分支点明确: "A key part of H2 is that...H2 should be pronounced in situations where..."
- 调节方向一致: amplifying factors (+) → accentuate H2; buffering factors (-) → attenuate H2

**与其他架构的区分**:
| | Y-shaped | 对称反向双轨 | 2×2 Cell-by-Cell |
|---|---|---|---|
| 路径数 | 2 (非对称) | 2 (对称) | 4 (矩阵) |
| Contingencies | 仅在一条路径 | 无 | 每个 cell 独立 |
| 假设数 | 5 (2 main + 3 cont.) | 4 (2×2 main) | 4 (全调节) |

---

## Rhetorical-Question 理论 Pivot (What-If Pivot)

**适用**: 从 "文献做了什么" 转向 "但如果情况不同会怎样"——用问句邀请读者进入反直觉推理

**模板**:
```
However, what if [negative action] is the outcome of [failure type] that result from taking [different actions] than those taken by others in the [category]? In other words, what if the [action] is less likely to be shared by others in the same [category] because the [actor] differentiated itself by [adopting nonstandard practices], and it is these [practices] that have led to the [crisis]? We argue that in this situation the [mechanism dynamics] are likely to be different.
```

**语料锚定**:
- paruchuri_pollock_kumar2019 (SMJ) — "However, what if the negative action is the outcome of capability failings that result from taking different actions than those taken by others in the industry? In other words, what if the action is less likely to be shared by others in the same category because the firm differentiated itself by adopting nonstandard practices, and it is these practices that have led to the crisis?"

**关键特征**:
- 两个连续 "what if" 问句——第一个建立 alternative scenario，第二个深化逻辑
- "In other words" 重新表述——确保读者跟上反直觉推理
- 不使用 "We depart from..." / "Unlike prior research..." 等标准 pivot 措辞
- 问句创造 reader-writer 同盟——"让我们一起思考这个可能性"
- 适合理论贡献为 "改变前提条件" 而非 "发现新变量" 的论文

**反模式**:
- 问句后没有 "We argue that..." 的确定性回答——问句必须立即被论证跟进
- "what if" 链过长 (≥3 个) → 读者失去耐心

---

## 联合必要性门控逻辑 (Joint Necessity Gate / AND Gate Logic)

**适用**: 两个条件不是 moderator（连续调节）而是 serial necessary conditions——两者必须同时满足，机制才会运作

**模板**:
```
[Condition A] alone is not sufficient. [Explanation of why A is necessary but must combine with B]. [Condition B] is also required because [explanation]. Thus, for [mechanism] to occur, [Condition A] AND [Condition B] must both hold: only when [A] is [present/high] and [B] is [present/high] does [prediction] manifest.
```

**语料锚定**:
- paruchuri_pollock_kumar2019 (SMJ) — Associability (cuisine type + geographic proximity) AND Salience (media coverage of crisis) must both hold for positive reputation spillover. "associability alone is not sufficient. The associability of other category members has to combine with the salience of the failure to create the cognitive availability required for the spillover to occur."

**与调节效应的区分**:
| | 联合必要性 (AND Gate) | 调节效应 (Moderation) |
|---|---|---|
| 逻辑 | A AND B → 机制启动 | X→Y, moderated by W |
| 条件变量 | 两个必要前提条件 | 一个 IV + 一个 moderator |
| 假设形式 | "Given A and B, X→Y" | "X→Y is stronger when W is high" |
| 实证检验 | 三向交互或分组检验 | 两向交互 |

**反模式**:
- AND gate 的 "必要条件" 退化为 "影响因素" → 如果条件只是 "增强" 而非 "必需"，使用标准调节框架
- 两个必要条件在概念上重叠 → 如果分不清 A 和 B 的独立贡献，应合并为一个条件

---

## 社会比较机制（Social Comparison Mechanism，paruchuri_pollock_kumar2020 型）

**适用**: 某actor的failure/decline使其他actors因比较而显得更好——非自身提升，而是比较基准下降

**模板**:
```
Since social evaluations are made compared to some referent ([citations]), a given level 
of [outcome] can look better or worse depending on how [well/poorly] the comparative 
referents perform, and how similar they are perceived to be to the focal actor ([citations]). 
If a [category member] demonstrates a major [failure type] associated with their 
[differentiating actions], other [actors] will look better not because they enhanced their 
[outcome], but because their comparative referent did something different and worse, making 
them appear better by comparison.
```

**关键特征**:
- **"not because they enhanced... but because their comparative referent did something different and worse"** → 排除自身提升的替代解释，精确定位社会比较机制
- 引用经典社会比较文献(March & Simon 1958; Porac et al. 1999)作为理论基础
- 适用于: reputational spillover, status competition, market positioning研究

**语料锚定**: paruchuri_pollock_kumar2020 (SMJ) — Chipotle E. coli → positive reputation spillover to proximal Mexican restaurants

---

## 认知可用性时效机制（Cognitive Availability Duration，paruchuri_pollock_kumar2020 型）

**适用**: 论证某效应的持续时间由事件的认知可用性(salience/cognitive availability)决定——效应随事件淡出公共注意力而衰减

**模板**:
```
We also argue that [outcome] effects will only persist as long as the [trigger] continues 
to be salient, or cognitively available to the [audience] making the assessments ([citations]). 
Extreme and frequently occurring stimuli tend to be more cognitively available because they 
are figural, or stand out relative to the typical flow of information ([citations]). However, 
since [outcome construct] need to be continually reinforced ([citations]), when the crisis 
abates it will become less salient and its influence will weaken, eventually ceasing to 
factor into [audience's] assessments. Thus, any [outcome] effects are likely to diminish 
and disappear once the [trigger] ceases to be salient.
```

**关键特征**:
- **"figural, or stand out relative to the typical flow of information"** → 在学术术语后立即给出通俗解释
- **"continually reinforced"** → 声誉/社会评价类构念的核心属性——需要持续强化否则消退
- 引用cognitive psychology经典(Fiske & Taylor 1991; Tversky & Kahneman 1973)作为理论基础
- 适用于: event studies, reputational spillover, media effects, crisis management中的时效性论证

**语料锚定**: paruchuri_pollock_kumar2020 (SMJ) — salience decay→positive spillover disappears when media coverage stops

**反模式**:
- Cognitive availability被用作"万能解释"但未与具体研究情境连接 → 必须补充情境特定的机制桥接(如media coverage→salience)
- "continually reinforced" citation不到位 → 必须引用领域内经典(Pollock et al. 2015; Washington & Zajac 2005)

---

## 双重印记对立通道 + 效果持续性差异 + 底物匹配调节（Dual Opposing Channels with Differential Persistence and Substrate-Matched Moderators，qiao2026 型）

**适用**: 同一起源条件（如创始伙伴关系、历史制度/军方关联、创始投资人声誉）**同时**留下两条方向相反的中介通道——一条内嵌于组织结构（capability，促进结果），一条存于外部受众认知（identity，阻碍结果）。核心理论贡献**不是**"哪条通道占优"，而是 (1) 两条通道的**效果持续性（persistence）不同**——内嵌型持续更久、受众认知型更易变；(2) 起源印记者的**后续变迁非对称地**重塑两条通道——每个调节变量只作用于一条通道的**机制底物**。

**与辩证对立双路径 (habel2016) 的关键区分**:

| | 双重印记对立通道 (qiao2026) | 辩证对立双路径 (habel2016) |
|---|---|---|
| 核心理论问题 | 两条通道**衰减速率**谁更慢？印记者后续变迁如何**非对称**重塑？ | 当前条件下**哪条通道占优**？ |
| 中介嵌入位置 | 一条在组织内部（结构/惯例/默会知识），一条在外部（受众认知/集体记忆） | 两条都在同一心理/决策层（benefit vs cost perception） |
| 调节变量 | **通道特异性**——每个调节只作用于一条通道的底物 | 共享一个调节，决定两路径相对强度 |
| 时间/持续性 | 核心理论维度（meta-hypothesis 比较两通道衰减） | 不涉及 |
| 理论增量 | "嵌入位置决定持续性" + "印记者动态重塑" | "对立路径的净效应随条件翻转" |

**模板**:
```
[Origin condition produces dual imprints]
We propose that [origin condition] (e.g., founding [partner] relationships established during 
[sensitive period]) generate enduring effects through two distinct imprints: [internal imprint] 
embedded within [organizational structures / routines / tacit knowledge] and [external imprint] 
manifested in [stakeholder perceptions / collective memory].

[Channel 1 — internal, facilitates]
The [internal imprint] is manifested as [partner-derived procedures / protocols / routines] 
that [enhance performance]. Because [the partner] was [an early adopter / monopoly holder] of 
[scarce expertise], these [procedures] create [structural inertia / tacit knowledge] that 
persists after [direct involvement] ceases ([citations]). Therefore:
H1a: [origin condition] is positively related to [internal imprint].
H1b: [internal imprint] is positively related to [outcome].

[Channel 2 — external, impedes]
We then suggest that [origin condition] can also imprint the [organization] with an [external 
identity] through lasting [associations] that become embedded in [stakeholder categorizations 
/ collective memory / media narratives] ([citations]). [External audiences] may encounter 
[observable markers, e.g., names] as [identification triggers] regardless of current reality. 
Therefore:
H2a: [origin condition] is positively related to [external imprint].
H2b: [external imprint] is negatively related to [outcome].

[Differential-persistence meta-hypothesis — the signature move]
We suggest that [internal imprint] exhibits more persistent effects than [external imprint] 
due to fundamental differences in their embedding mechanisms. [Internal imprint] reside in 
[organizational processes maintained through daily enactment], producing consistent effects 
that decay mainly through [sustained disuse]. In contrast, [external imprint] reside in 
[stakeholder memories requiring continued audience attention]; audience-held interpretations 
shift with [media narratives / political events / expectation violations] even when 
organizational attributes remain constant ([citations]). Therefore:
H3: The [internal imprint] exhibits more enduring effects on [outcome] than the [external imprint].

[Substrate-matched moderators — each moderator targets one channel's substrate]
We further examine how [post-founding transformations of the origin partner] reshape these 
effects. [Moderator 1: a transition that democratizes scarce expertise] diminishes the 
competitive advantage of [internal imprint] by [transforming previously exclusive expertise 
into broadly accessible standards] ([citations]). Therefore:
H4: [Moderator 1] negatively moderates the relationship between [origin condition] and [outcome] 
(via the internal channel).
[Moderator 2: an event that amplifies threat perceptions] exacerbates the negative effects of 
[external imprint] by [heightening stakeholder threat perceptions associated with the 
association] ([citations]). Therefore:
H5: [Moderator 2] negatively moderates the relationship between [origin condition] and [outcome] 
(via the external channel).
```

**实证检验提示（differential persistence 的可检验化）**:
- H3 不能直接读两个系数（一正一负）。技巧：对**负向通道**做 reverse-code 使两条 time×channel interaction 同向，再用 **Wald test** 检验两交互系数是否统计可区分（见 `write-results/SEM-moderated-mediation.md` "Reverse-Code + Wald Test"）。
- 内嵌通道（capability）随时间**增强**（age×capability > 0）；外部通道（identity）随时间**衰减**（主效应负，age×identity > 0 意味负效应被侵蚀）。

**关键特征**:
1. **持续性作为独立理论维度** — H3 是关于"哪条通道衰减更慢"的 meta-hypothesis，区别于 habel2016 "哪条占优"。这是本文的核心理论增量。
2. **嵌入位置决定持续性** — 结构/默会知识（内部，靠日常 enacting 维持，靠 sustained disuse 衰减）vs 受众认知（外部，靠持续注意力维持，靠叙事/事件 shift）。必须给出 **storage location + change mechanism** 双重论证。
3. **底物匹配调节（substrate-matched moderators）** — 每个调节变量精确作用于一条通道的机制底物：能力通道底物是"稀缺专长"（被民用标准化 democratize），身份通道底物是"威胁认知"（被政变 amplify）。调节与通道一一对应，非共享调节。
4. **印记者非对称重塑** — 同一创始印记者的两类后续变迁（能力 democratization / 身份 stigmatization）分别削弱/放大两条通道，体现"印记不是一次性的，印记者持续重塑其表达"。
5. **T6 收束常用历史格言作 foil**（见 `write-introduction/.../theory-lens/05-maxim-contrast.md` 变体 B）。

**可迁移性**: 极高 — 适用于任何"同一起源留下对立双印记"的研究：
- 创始政府/军方关联（capability+ vs security identity−）
- 创始投资人/名人背书（资源+ vs 类别化/锚定−）
- 历史并购/合资（吸收能力+ vs 敌意/类别标签−）
- 创始宗教/意识形态/族裔关联（社群资源+ vs 排他身份−）

**适用期刊**: SMJ（组织异质性、历史与战略）、AMJ、OS、AMR（理论建构）。

**反模式**:
- 把 H3 写成"哪条通道占优"而非"哪条衰减更慢" → 持续性维度才是本文理论增量，占优只是 net effect
- 调节变量同时作用于两条通道而非底物匹配 → 丢失"印记者非对称重塑"的精巧，退化为普通调节
- 持续性论证只用一句话（"内部更稳定"） → 必须给出 storage location + change mechanism 双重论证
- 比较两个一正一负 interaction 系数时不做 reverse-code → Wald test 不可直接解读
- 印记者后续变迁与创始印记脱节 → moderator 必须明确作用于"起源印记者本身"的当下状态（如军方当局 vs 民用化），而非无关事件

**语料锚定**: qiao_hiatt_sine2026 (SMJ) — 创始军方伙伴 → 内部 capability imprint（操作流程/安全协议，+ 国际化）+ 外部 identity imprint（军方名称/联想，− 国际化）；H3 capability 比 identity 更持久；H4 民用化空管 democratize 能力底物；H5 军事政变 amplify 身份威胁。配合 `write-methods/生存分析.md` 变体 6、`write-methods/IV-2SLS.md` 变体 4、`write-results/IV-2SLS.md` 变体 4 使用。

---