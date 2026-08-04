---
type: canonical_reference
canonical_id: "01-progressive-coherence"
status: ✓ STANDARD
gap_type: Incompleteness
cross_paper: VERIFIED
generativity: GENERATIVE
exclusivity: MEDIUM
source_papers:
  - eilert2017 (JM, 2017): "predominantly focused on X and Y. However, little attention to Z"
  - wu2025 (SMJ, 2025): "Authority quote pivot → remains poorly understood"
  - gamache2020 (SMJ, 2020): "Natural progression from general to specific"
  - mayo2021 (POM, 2021): "Cross-disciplinary literature review with Table"
  - grewal2025 (JM, 2025): "Consensus building + practice complexity in digital advertising ecosystems"
  - cui_yang_vertinsky_smj (SMJ): "Consensus + stakes + three unaddressed issues preview"
  - malshe2015 (JM, 2015): "Nascent marketing–finance stream + complementary-half pivot (equity examined, debt not)"
  - schumacher_keck_tang2020 (SMJ, 2020): "Two mature streams joined through a necessary interpretive bottleneck"
created: 2026-05-19
updated: 2026-08-03
source: Extracted from literature-turn-templates.md + MVP30 validation
---

# 01-progressive-coherence — Progressive Coherence 递进式文献对话

## 功能描述

P2-P3 的功能：承认文献已有实质进展，但精确指出被遗漏的维度/机制/时点/对象。核心逻辑是"已有文献做了 A 和 B，但遗漏了 C——不是因为他们错了，而是因为该领域自然发展到此时才出现 C 的问题。"

这是 **Incompleteness** Gap 最常用的 Conversation 策略。

## 适用场景

- Gap 类型 = **Incompleteness**（文献留下关系、机制、时点、对象或结果维度的空白）
- 需要解释为什么这个遗漏是重要的（不只是"没人做过"）
- 目标期刊接受递进式对话（JM, SMJ, AMJ, OS 均适用；ASQ 可能需要更强的理论缺口）

## 验证状态

### 跨论文复现
- **VERIFIED** (≥4 papers): eilert2017 (JM), wu2025 (SMJ), gamache2020 (SMJ), mayo2021 (POM)

### 生成力
- **GENERATIVE**: "Although research has... little attention has been paid to..." 模板高度可迁移

### 排他性
- **MEDIUM**: 几乎只在 Incompleteness 中出现

---

## 句法模板

### 变体 A：自然推进型（gamache2020 型）

**模板**:
> "Research in [field] has long recognized the importance of [phenomenon] and has often attempted to understand [outcome]. As part of this effort, recent research has drawn on [theory] to focus on [specific aspect] ([citations]). For example, research in this tradition has considered [specific examples of what IS known]."

**来源**: gamache2020 (SMJ), adapted

**关键特征**:
- "has long recognized" → 承认长期积累
- "As part of this effort" → 展示自然推进
- "For example" → 用具体研究支撑共识

---

### 变体 B：快速文献回顾型（eilert2017 型）

**模板**:
> "A substantial body of research has examined [reactive/post-hoc response to phenomenon]. [Author A] found that [finding]. [Author B] showed that [finding]. Most recently, [Author C] demonstrated [finding]. These studies collectively establish that [core consensus]. However, what remains unclear is [our focus]."

**来源**: eilert2017 (JM), adapted

**关键特征**:
- 用 3-4 句话快速建立文献共识
- "collectively establish that" → 确认已有进展
- "However, what remains unclear is" → 精确指出遗漏

---

### 变体 C：权威引语过渡型（wu2025 型）

**模板**:
> "Accordingly, a substantial body of research has examined [dominant focus]. [Authority], however, note that '[insightful observation that reframes focus]' (emphasis original). Yet, despite some noteworthy exceptions (e.g., [Exception A]; [Exception B]), [our focus] remains poorly understood."

**来源**: wu2025 (SMJ), P1-P2

**关键特征**:
- 用权威引语作为从"已有进展"到"仍有缺口"的转折支点
- "emphasis original" 显示对原文的精确引用
- "remains poorly understood" → 中等强度措辞

---

### 变体 D：跨学科引入型（mayo2021 型）

**模板**:
> "In fact, research outside of [target field] indicates that [actors] may manage risks related to [negative events] via at least two mechanisms: [mechanism 1] ([citations]) or [mechanism 2] ([citations]), and that the chosen risk management mechanism may depend on [key variable]. The contexts of these empirical studies are predominantly in [field A] ([citations]) and [field B] ([citations]); see Table [number]. These studies indicate that [condition 1], [actors] may [behavior 1] ([citations]), leading to [consequence A] ([citations]). [Condition 2], [actors] may [behavior 2] ([citations]), to avoid [consequence B]."

**来源**: mayo2021 (POM), P2

**关键特征**:
- "research outside of [target field] indicates" → 明确跨学科引入
- "via at least two mechanisms" → 预告二元机制
- "see Table [number]" → 用表格呈现文献回顾（POM/MSOM 风格）
- 条件分句清晰区分不同情境下的行为差异

**适用**: 将 finance/accounting/psychology 发现引入 OM 或战略管理的研究

---

### 变体 E：Table 1 文献矩阵型（darby2025 型）

**模板**:
> "A growing body of [domain] research offers insights into [phenomenon]. For example, [level_1_findings]. Recently, scholars have moved beyond [level_1] to examine [level_2], finding that [level_2_findings] ([citations]). This shift in focus is due, in part, to [external_change] ([citation]). Indeed, [reinforcement]."

同时嵌入 Table 1: 按 [DV 行] × [IV 类别列] 组织的文献矩阵，每格包含作者+年份+发现方向。

**来源**: darby2025 (JSCM), P2 + Table 1

**关键特征**:
- 叙事段落仅 3-4 句建立递进式文献线索
- Table 1 替代了原本需要 3-4 段的冗长文献叙述
- 矩阵按 IV 类别分列（召回特征 / 供应链因素 / 公司治理因素），按 DV 分行（召回次数 / 召回时滞）
- 每格仅 1-2 行：作者+年份+发现方向（+/-/ns）

**适用**: 文献 >=15 篇、需要在 Introduction 中展示文献广度的研究。文献 <10 篇时段落叙事足矣，无需矩阵。
**禁忌**: Table 1 不是完整文献综述的替代品——它是对文献模式的视觉摘要。正文仍需 2-3 句叙事建立逻辑线索。

---

### 变体 F：共识建立 + 实践复杂性型（grewal2025 型）

**模板**:
> Increased [construct] risks in turn require increased efforts to [desired outcome] in [domain] ([authority citations]). In such contexts, managing [construct] often entails [key consideration] that stem from [perception basis]. Across [environments], [concrete examples]. But [key uncontrollable factor], because [reason]. [Actors] devote substantial [resources] to [action], but such efforts have not proven widely successful. Not only is [construct] difficult in practice, with strategically important consequences, but it also involves substantial complexity, because [nuance].

**来源**: Grewal, Vana, and Stephen (2025), *Journal of Marketing*, P2

**原文锚定**:
> "Increased brand safety risks in turn require increased efforts to keep the overall brand reputation safe in digital advertising ecosystems (IAB 2018; Johnson, Voorhees, and Khodakarami 2023). In such contexts, managing brand safety often entails adjacency considerations that stem from the perceived safety or suitability of content that a brand appears near, next, or adjacent to in a given media channel. Across digital environments, user-generated posts appear above or below brands' advertisements in Facebook and Instagram feeds; pre- and mid-roll advertisements run during videos on YouTube... But the content that the brand appears adjacent to largely is beyond the brand's control, because it gets determined by opaque algorithms. In the struggle to ensure brands do not appear alongside inappropriate—that is, unsafe—content, companies devote substantial time, effort, and advertising dollars to try to secure safe ad space... Not only is managing brand safety difficult in practice, with strategically important consequences, but it also involves substantial complexity, because the definition of 'safe' adjacent content varies across brands, products, and audiences."

**关键特征**:
- 用 "Increased X risks require increased efforts" 将现象升级为研究问题
- 列举具体环境/平台让抽象概念落地
- "unfortunately" / "but such efforts have not proven widely successful" 建立实践困境
- "not only... but also..." 连接实践重要性和理论复杂性

**适用**: 数字平台、算法、UGC 等新兴环境对传统管理实践的挑战
**禁忌**: 复杂性铺垫必须与后续 gap 直接相关

---


### 变体 G：共识 + Stakes 嵌入 + 三重缺口预告（cui_yang_vertinsky_smj 型）

**模板**:
> A thorough study of [puzzle] is of great theoretical importance, contributing to [broad theoretical goal] ([citation]). Prior studies on [stream] have provided important insights into [tension] ([citations]). For example, researchers maintain that [mechanism 1] and have identified important factors that influence [outcome], such as [factor A], [factor B], and [factor C] ([citations]). However, [N] important issues in this sphere of research remain unaddressed.

**来源**: Cui, Yang & Vertinsky (SMJ), P2

**原文锚定**:
> "A thorough study of this 'collaboration–competition' relationship between partners is of great theoretical importance, contributing to the development of a more comprehensive model of inter-firm behavior rendered by strategic alliances (Kogut, 1989). Prior studies on alliance learning have provided some important insights into the tension between collaboration and competition... researchers maintain that competition within alliances stems from the misalignment of interests between allies... and have identified important factors that influence allies' competitive learning within alliances, such as asymmetric learning capabilities, the ratio between private and common interests, and knowledge similarities between allies... However, three important issues in this sphere of research remain unaddressed."

**关键特征**:
- 用 "A thorough study of... is of great theoretical importance" 同时完成 Stakes 声明和 Literature Turn 过渡。
- 先列举已有研究的具体贡献（factors A/B/C），再转向缺口，形成 progressive coherence。
- 结尾用数字预告（three important issues）降低读者认知负荷，并与后文 Tension 段落一一对应。
- 整个 P2 将 Literature Turn、Stakes、Tension 预告三种功能压缩在一段内，适合 Introduction 紧凑的 SMJ 风格。

**适用**: Incompleteness × (Mechanism + Boundary)；已有文献较丰富、缺口可明确列举为 2-4 点的研究；SMJ/AMJ。

**禁忌**: 不要只列文献不总结 argument；每个 factor 必须具体；Stakes 不能只有 "theoretically important" 而无 broad theoretical goal 支撑。

---

### 变体 H：新兴交叉流 + 互补半区缺口型（malshe2015 型）

**模板**:
> "The issues of [source-field question] have been central to [source discipline] research for more than [time period] (for a review, see [classic review]). [Brief definition of the source-field construct]. Recently, [target-field] scholars have begun to examine the interaction between [target-field topic] and [source-field construct] by investigating [angle 1 already examined] ([citation 1]) and [angle 2 already examined] ([citation 2]). Yet little research investigates [the complementary half — the unexamined polarity of the same phenomenon]."

**来源**: Malshe & Agarwal (2015, *Journal of Marketing*), P1–P2

**原文锚定**:
> "The issues of what influences a firm's choice of debt and equity and how this choice affects its nonfinancial strategic decisions have been central to corporate finance research for more than half a century (for a review, see Graham and Leary 2011). The relative proportions of debt and equity constitute a firm's capital structure, typified by its financial leverage... Recently, marketers have begun to examine the interaction between marketing strategy and leverage by investigating both the role of marketing while raising equity (Luo 2008) and how these equity funds influence marketing strategy (Kurt and Hulland 2013). Yet little research investigates the effects of debt on marketing."

**关键特征**:
- **三步文献对话**:
  1. **源学科纵深建立** — "[source discipline] research for more than [half a century]" + 经典综述引用，先确立所借构念在源学科的深厚积累（兼作 Move 1 significance via disciplinary context）
  2. **新兴交叉流承认** — "Recently, [target field] have begun to examine..." 用 "recently/begun" 标志交叉流为**新兴**（非成熟），并枚举已检视的具体角度（angle 1 / angle 2），展示对最邻近前人工作的精确掌握
  3. **互补半区 pivot** — gap 不是新维度，而是**同一现象的未检视镜像半区**（equity side done, debt side not）。"Yet little research investigates [the complementary half]" 把缺口定位为前人刚起步时漏掉的另一半
- **"recently/begun" 是关键信号词**: 区别于变体 A（gamache2020 "has long recognized" 成熟流）与变体 B（eilert2017 "substantial body" 成熟流）——本变体处理的是**交叉流尚未成熟**的情境，gap 的合法性来自"连刚起步的工作都只做了一半"
- **互补半区 vs 新维度的判别**: 现象有两个天然极性（equity/debt、success/failure、upside/downside、entry/exit），前人只检视了一极，另一极是 gap。这与变体 G（cui 三重维度缺口，跨 outcome/IV/context 三个**独立维度**）不同——本变体的 gap 是**单一维度内的镜像极性**，不是新维度
- **gap 的"why surprising"用源学科证据支撑**: 随后的 multi-reason gap（见 `tensions/01-despite-progress-unaddressed` 变体 D malshe2015）三条理由都引用**源学科**（finance）的成熟发现（debt 占 80% 融资；高杠杆企业削减无形资产/质量；债务限制增长期权）——用源学科证据为交叉缺口的重要性背书，是跨学科文献对话的可信度来源

**适用条件**:
- 跨学科嫁接研究：从源学科（finance/economics/psychology）引入构念到目标学科（marketing/strategy/OB）
- 目标学科已有**新兴**（非成熟）的交叉流，且该流只检视了现象的一极
- 现象有天然双极性（equity/debt、gain/loss、entry/exit、approach/avoid）
- 目标期刊接受跨学科对话且重视源学科证据（JM/JMR 跨职能接口、JCR、SMJ 跨学科）

**禁忌**:
- 不要把源学科写成"已解决"该问题——源学科的积累是构念合法性的来源，但目标学科的交叉才是 gap 所在
- "recently/begun" 必须名副其实——若交叉流已成熟（≥10 年、数十篇），用变体 A/B 而非本变体
- 互补半区必须真的"未检视"——若已有零星研究触及另一极，须精确引用并说明本文与它们的不同
- 源学科证据支撑 gap 时，每条理由的引文必须来自源学科的经典/综述，不可用目标学科的边缘文献充数

**与贡献段的回响**: 本变体的 equity/debt 互补半区应在贡献段兑现为"among the first to study [debt half]" + "combine literature from both [source] and [target]"——gap 与贡献共享同一互补半区逻辑，形成 hook→turn→gap→contribution 的紧致回响（malshe2015 P5 即如此）。

---

### 变体 I：双成熟文献流 + 必要解释瓶颈（Schumacher–Keck–Tang 2020 型）

**验证状态**: EMERGING（单篇来源；仅作 `section_variant`）

**模板**:
> "[Stream A] has established that [objective signal relative to a reference point] shapes [organizational response]. Yet the signal can influence action only after [focal decision maker] interprets it. Separately, [Stream B] shows that [decision-maker disposition] systematically biases the processing of [relevant information]. Although each stream is well developed, their intersection remains underexamined: we do not yet know how [disposition] changes the interpretation of [signal] and thereby alters [response]."

**来源**: Schumacher, Keck, and Tang (2020), *Strategic Management Journal*, Introduction P1.

**关键特征**:
1. 两套文献各自先获得完整承认，避免把任一方写成稻草人。
2. 用“信号必须先被行动者解释”建立必要中间环节，再证明第二套文献恰好会改变这个环节。
3. Gap 位于两个成熟知识块的交叉处，而不是任何一套文献内部的错误或互补极性遗漏。
4. 交叉点直接生成可检验链条：`disposition → interpretation of signal → organizational response`。

**适用**: 宏观刺激—组织行为关系依赖关键行动者的认知处理，且另有成熟的个体偏差、身份或倾向文献可解释该处理过程。典型为 `Incompleteness × (Mechanism + Boundary)`。

**禁忌**:
- 必须证明该解释环节对 X→Y 是必要的；不能仅因两套文献共享一个行动者就声称需要整合。
- 两流的既有结论须分别准确呈现；若已有研究已直接检验交叉关系，应改写为边界或机制精细化，而不是“尚未交叉”。
- 不要用方向反转把 Gap 误标为前人结论矛盾；反转若来自本文新边界，主 Gap 仍可是不完整性。

---


## 组装规则

### 默认配对（对角线，能量匹配）
- **与 `03-data-shock` (Hook) 配对**: 数据冲击建立 stakes，递进缺口将数据转化为学术问题
- **与 `10-practical-puzzle` (Hook) 配对**: 实践困境建立相关性，递进缺口精确到学术文献
- **与 `01-despite-progress-unaddressed` (Tension) 配对**: Progressive Coherence 是此 Tension 的标准 Conversation 策略

### 非默认组合（非对角合法，不由 Gap 类型反推）
> Coherence × Problematization 是 3×3 设计空间，对角线只是默认；完整矩阵见 `literature-turns/_index.md` 顶部 3×3 速查表与 `diagnose-introduction/references/intertextual-construction-playbook.md` §2。

- **Progressive × Inadequacy（合法非对角·主流盲区型）**: 累积成熟的传统内部存在系统性视角遗漏（去情境化/单一情境/构念混淆）——须用该传统自身的标准证明遗漏（Elsbach & Kramer 2003）。
- **Progressive × Incommensurability（合法非对角·共识颠覆型）**: 成熟共识在核心假设上错了——稻草人风险最高，需决定性反例与充分理论跑道（gamache2023；Hahl 2017）。

### 反模式提醒
- **不要把 Literature Turn 写成完整文献综述**: P2 是过渡，不是文献回顾。2-3 句即可
- **不要让 Hook 和 Literature Turn 脱节**: 必须在语义上连接
- **不要只引用自己导师的论文**: 展示文献广度

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| JM/JMR | ⭐⭐⭐⭐⭐ | 自然推进型最适配 |
| SMJ | ⭐⭐⭐⭐⭐ | 权威引语型适配 SMJ "冷静专业"风格 |
| AMJ | ⭐⭐⭐⭐⭐ | 需要解释为什么这个遗漏有理论重要性 |
| OS | ⭐⭐⭐⭐☆ | 偏好系统/结构性缺口论证 |
| ASQ | ⭐⭐☆☆☆ | ASQ 偏好更强的理论缺口（Inadequacy/Incommensurability） |

---

## 相关语料

- 配合 `hooks/03-data-shock.md` 使用：数据建立 stakes，递进缺口转化为学术问题
- 配合 `tensions/01-despite-progress-unaddressed.md` 使用：最常用的 Tension-Literature Turn 配对
- 配合 `transitions/01-hook-to-literature.md` 使用：Hook→Literature Turn→Gap 的标准链条
