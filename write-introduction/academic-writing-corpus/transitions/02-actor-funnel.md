---
type: canonical_transition
canonical_id: "02-actor-funnel"
status: ⭐ PREMIUM
function: "General Actor → Specific Actor → Most Specific Actor（文献焦点漏斗式细化）"
cross_paper: VERIFIED
generativity: GENERATIVE
exclusivity: MEDIUM
source_papers:
  - darby2026 (JOM, 2026): "shareholders → institutional investors → Big Four"
  - gamache2020 (SMJ, 2020): "stakeholder strategy → CEO role → CEO regulatory focus"
  - shen2022 (JOM, 2022): "political ties → political embeddedness → contingent resource utilization"
  - wu2025 (SMJ, 2025): "stakeholder pressure → direct vs indirect → institutional corporate social performance"
created: 2026-05-19
source: Extracted from darby2026 distill + MVP30 narrative_analysis
---

# 02-actor-funnel — Actor 漏斗式细化过渡

## 功能描述

在 Introduction 中从**一般性行动者类别**（如 shareholders, stakeholders, executives）逐步聚焦到**最具体的行动者子集**（如 Big Four institutional investors, CEO regulatory focus）。这不是简单的定义 narrowing，而是一个**层层递进的论证过程**：每一层都回答"为什么重要？""为什么这个子集更关键？""理论依据是什么？"

与直接说 "we focus on X" 的区别：Actor funnel 通过展示更广泛类别中的异质性，让读者**自己得出结论**——最具体的子集才是理论上最值得研究的。

## 适用场景

- 研究需要将焦点从 broad category 收窄到 specific subset（如 governance → board → female directors）
- 理论上有理由认为**子集之间的差异**是研究的关键（如不是所有 institutional investors 都一样）
- 需要建立"为什么是这个子集而不是其他"的合法性
- 常见于治理、upper echelons、利益相关者、制度理论研究

## 验证状态

### 跨论文复现
- **VERIFIED** (≥4 papers): darby2026 (JOM), gamache2020 (SMJ), shen2022 (JOM), wu2025 (SMJ)
- 跨越治理、战略、运营、制度理论多个领域

### 生成力
- **GENERATIVE**: "While... there are... The latter tend to be more consequential... Accordingly, we focus on..." 结构可适配任何有异质性行动者的研究情境

### 排他性
- **MEDIUM**: 专用于需要从 broad actor category 聚焦到 specific subset 的研究。若研究中所有行动者同质（如"all firms"），不需要此过渡

---

## 句法模板

### 变体 A：三层漏斗 + 异质性论证（darby2026 型）

**模板**:
> [Theory] suggests that [general actor] might be one possibility to [solve problem] ([citation]). As [role], [general actor] play an important [function] wherein they [mechanism], which, in turn, [outcome] ([citation]). [Contextual evidence of actor relevance]. For example, [citation] found that [specific finding].
>
> [Specific actor category]—that is, [definition] ([citations])—are an especially intriguing group of [general actor] because of [reason for prominence]. [Specific actor] are typically [characteristic 1] and [characteristic 2] ([citation]). Ultimately, [specific actor] are accountable to [stakeholder], so it is perhaps unsurprising that they [behavioral tendency]. Indeed, empirical evidence in neighboring fields suggests that [specific actor] "[quote about broad influence]" ([citation]), including [example 1], [example 2], and [example 3].
>
> While the collective influence of [specific actor] should not be understated, there are [number/heterogeneity] who may vary in terms of [dimension of variation] ([citation]). For example, [contrast 1], whereas [contrast 2]. The latter tend to be more consequential due, in part, to [reason 1] and [reason 2] ([citation]). Indeed, [theory] suggests that [specific sub-group] are the ones who have [capability] ([citation]), and evidence from practice suggests that [supporting evidence]. Accordingly, we focus on [specific sub-group]—specifically, [names]—who [distinguishing characteristic] ([citation]). As [bounded rationality assumption], executives should attend to the demands of such influential [actors] ([citation]). Building on this, we theorize that [specific sub-group] may also influence [dependent variable] because [theoretical rationale]. As such, our first research question asks: *[RQ1]*

**来源**: darby2026 (JOM), P2-P4

**原文锚定**:
> Agency theory suggests that a firm's shareholders might be one possibility to encourage more timely recalls (Eisenhardt 1989). As principals, shareholders play an important monitoring role wherein they try to ensure that their agents (executives) make good decisions, which, in turn, helps protect the value of their investments (Kim et al. 2019b). Shareholders have long cared about supply chain successes and failures (e.g., Hendricks and Singhal 2003), and the ramifications for a firm's long-term performance and reputation are "driving more investors to become interested in the supply chains of their portfolio companies" (Straight 2024, para. 7). For example, Cheung et al. (2020) found that ownership by investors who simultaneously own shares in a buyer and a supplier was associated with improvements in suppliers' operating and marketing performance.
>
> Institutional investors—that is, organizations such as mutual funds, hedge funds, banks, and insurance companies that manage more than $100 million in assets (Connelly et al. 2010; Cheung et al. 2020)—are an especially intriguing group of shareholders because of their prominence in equity markets. Institutional investors are typically a firm's largest shareholders and collectively own the vast majority of shares in publicly traded firms (Helmuth et al. 2023). Ultimately, institutional investors are accountable to the individuals who entrust their money to them, so it is perhaps unsurprising that they use their clout to influence portfolio firms. Indeed, empirical evidence in neighboring fields suggests that institutional investors "appear to have a voice in virtually every major decision that executives face" (Helmuth et al. 2023, 722), including innovation (Kim et al. 2019a), competitive moves (Connelly et al. 2019), and sustainability policies (Kim et al. 2019b).
>
> While the collective influence of institutional investors should not be understated, there are thousands of institutional investors who may vary in terms of their engagement with portfolio firms (McCahery et al. 2016). For example, there are many institutional investors who manage a few hundred million dollars in assets, whereas a few institutional investors manage trillions of dollars in assets. The latter tend to be more consequential to firm decision-making due, in part, to the size of their ownership stakes and the resources they can dedicate to researching, monitoring, and engaging with portfolio firms (Lewellen and Lewellen 2022). Indeed, agency theory suggests that large shareholders are the ones who have the motivation and capability required to effectively monitor firms (Dharwadkar et al. 2008), and evidence from practice suggests that such shareholders make use of the power that their size confers (e.g., Helmuth et al. 2023). Accordingly, we focus on ownership by *large* institutional investors—specifically, BlackRock, Vanguard, Fidelity, and State Street—who collectively managed nearly $32 trillion in assets by the end of 2024 (WTW 2025) and are colloquially known as the "Big Four" (Strine 2020). As boundedly rational actors, executives should attend to the demands of such influential shareholders (Eisenhardt 1989). Building on this, we theorize that ownership by large institutional investors may also influence how quickly products are recalled after a defect is discovered because recall delays create an array of adverse consequences that matter to their long-term investment objectives and reputations (e.g., McNabb 2015). As such, our first research question asks: *is ownership by large institutional investors associated with a firm's time-to-recall?*

**关键特征**:
- **三层递进**：General category → Specific category → Most specific subset
- **每层三要素**：定义 + 重要性证据 + 理论依据
- **承认异质性**：用 "While... there are..." 展示 broader category 内部的差异，为聚焦最 specific subset 铺垫
- **理论收束**：每一层的最后都回到理论依据（agency theory, bounded rationality），避免让人觉得聚焦是随意的
- **RQ 嵌入**：漏斗的最终产物是 RQ1，形成"论证→问题"的闭环

---

### 变体 B：两层漏斗 + 构念细化（gamache2020 型）

**模板**:
> Research in [field] has long recognized the importance of [broad phenomenon]. As part of this effort, recent research has drawn on [theory] to focus on the role of [general actor]. While important, much of the work on [topic] is general and considers [outcome] in a very broad sense. Research has yet to seriously consider [specific aspect of actor]. This omission is critical, as [explanation].

**来源**: gamache2020 (SMJ), P1-P2

**关键特征**:
- 从 broad phenomenon 到 general actor 到 specific aspect
- "While important... is general and considers... in a very broad sense" → 经典"尊重但批评"句式
- 适合构念细化型研究（从笼统到具体类型）

---

### 变体 C：条件化漏斗（shen2022 型）

**模板**:
> Existing research on [topic] has largely focused on [dominant direction]. Scholars have shown that [typical finding]. However, this focus on [direction A] has left [direction B] relatively underexplored. Understanding [direction B] is important because [reason]. We therefore examine [specific focus].

**来源**: shen2022 (JOM), adapted

**关键特征**:
- 用"方向"而非"层级"来组织漏斗
- 适合同一行动者在不同条件下的差异化研究

---

## 组装规则

### 必须配对
- **与 Incompleteness / Inadequacy Gap 配对**: Actor funnel 的收窄逻辑通常服务于"文献遗漏了某个特定子集"的缺口论证
- **与 Theory Lens 配对**: 漏斗的最终聚焦点必须能被理论解释（如 agency theory 解释为什么 large shareholders 更有监督动机）

### 互斥
- **不要在没有理论理由的情况下使用**: 如果 "we focus on X" 只是出于数据可得性，不要用漏斗结构——读者会觉得你在强行 justify
- **不要在漏斗中间引入无关的文献综述**: 每一层只回答"为什么这一层重要"，不要展开该层的全部文献

### 反模式提醒
- **不要只有两层**: 两层收窄（如 "firms → CEOs"）通常不需要完整的 funnel 结构，直接说 "we focus on CEOs" 即可。Funnel 结构的价值在三层及以上时才显现
- **不要在每一层都用 "However"**: 第一层到第二层是"细化"而非"转折"，用 "In particular" / "More specifically" 而非 "However"
- **不要遗漏 "As such, our research question asks"**: 漏斗的终点必须是 RQ，否则读者不知道收窄是为了什么

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| JOM | ⭐⭐⭐ 极高 | 运营/供应链研究常用 actor 细化（如 governance → board → female directors） |
| SMJ | ⭐⭐⭐ 极高 | Upper echelons / 战略研究的标志性结构 |
| AMJ | ⭐⭐⭐ 高 | 组织行为/HR 领域常用；需搭配清晰的机制链 |
| OS | ⭐⭐⭐ 高 | 制度理论研究中从 broad institutional pressure 到 specific mechanism 的标准写法 |
| ASQ | ⭐⭐ 中 | 可用，但通常更直接地进入理论对话，actor 细化可能被视为过度铺垫 |
