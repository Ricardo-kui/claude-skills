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