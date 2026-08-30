---
type: canonical_reference
canonical_id: "08-cost-vs-benefit"
status: ✓ STANDARD
gap_type: Incompleteness / Inadequacy
generativity: ADAPTABLE
exclusivity: MEDIUM
source_papers:
  - eilert2017 (JM, 2017): "Recall costs vs delay costs — Toyota $17.35m → GM $900m escalation"
  - kim2022 (MS, 2022): "On the one hand / On the other hand dilemma articulation — testing vs rushing to market"
  - castellaneta_conti_kacperczyk2017 (SMJ, 2017): "Double-edged information-asymmetry paradox — rival vs buyer channels of same legal protection"
cross_paper: VERIFIED
updated: 2026-08-05
created: 2026-05-19
source: Extracted from MVP30 narrative_analysis + eilert2017 distill + castellaneta_conti_kacperczyk2017
---

# 08-cost-vs-benefit — 成本收益权衡张力

## 功能定义

呈现组织决策中两种相互竞争的压力，使决策困境成为核心研究问题。这种张力不仅是描述性的，更是理论性的——它解释了为什么"理性"行为者会做出看似非理性的选择。

与 `07-cost-benefit-tension` (Hook) 配套使用：Hook 段建立成本困境的现实紧迫性，Tension 段在文献层面解释为什么这个困境在理论上未被充分理解。

## 适用场景

- 研究涉及组织必须在两个不利选项之间做出权衡（如召回 vs 延迟召回、合规 vs 灵活）
- 存在可量化的、有权威来源的成本数据
- 目标期刊接受决策困境论证（JM、JOM、SMJ、OS）
- 需要解释为什么"理性"决策者会做出"次优"选择

---

## 句法模板

### 变体 A：对称成本结构（eilert2017 型）

**模板**:
> "[Decision A] is costly; [direct costs] and [indirect costs] make it a [devastating/threatening] prospect. [Reason to delay or avoid]. However, delaying [Decision A] may lead to even higher costs through [penalty 1], [penalty 2], and most importantly, [most salient penalty] ([citation]). [Specific case evidence]. [Second case evidence with escalated magnitude]. Therefore, although [Decision A] are adverse events in general, a quick response may attenuate the damage."

**来源**: eilert2017 (JM), P1

**原文锚定**:
> "Recalls are costly; announcing and implementing one is associated with both direct costs in repair, restitution, or liability and indirect costs such as losses in reputation and market value. Consequently, recalls could have a devastating impact on a firm's performance, sometimes even threatening its survival. Thus, a firm has reasons to avoid a quick recall and instead wait for the investigation to conclude. However, delaying a product recall may lead to higher direct and indirect costs through fines, liability damages, and most importantly, diminished reputation."

**关键特征**:
- 先建立第一面成本（行动成本）
- "However, delaying..." 建立第二面成本（延迟成本）
- 数字递进：抽象 → 类别 → 小案例 → 大案例

---

### 变体 B：竞争目标型

**模板**:
> "Firms must balance [Goal A] against [Goal B]. [Why Goal A pushes toward action]. [Why Goal B pushes toward inaction or delay]. [Evidence that this tension produces systematic variation in outcomes]."

---

## 组装规则

### 必须配对
- **与 `07-cost-benefit-tension` (Hook) 配对**: Hook 建立现实困境，Tension 在文献层面理论化该困境
- **与 `01-despite-progress-unaddressed` (Tension) 的升级使用**: 如果文献已研究过成本但只看了其中一面，用 08 替代 01

### 反模式提醒
- **成本不对称**: 一方成本巨大，另一方微不足道 → 必须让读者感到"两边都疼"
- **无决策主体**: 必须明确决策主体（firms, managers, regulators）
- **停留在描述**: 必须以问题结束："This tension raises important questions about [theoretical mechanism]"

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| JM | ⭐⭐⭐⭐⭐ | 决策困境是 JM 的核心张力类型 |
| JOM | ⭐⭐⭐⭐⭐ | 运营/供应链研究的经典张力 |
| SMJ | ⭐⭐⭐⭐☆ | 适合战略决策、治理研究 |
| OS | ⭐⭐⭐⭐☆ | 适合实践张力→理论 puzzle 的转译 |

---

### 变体 C：双边困境展开型（kim2022 型）

**模板**:
> "On the one hand, a firm can choose to [Prudent Action]. Such [action] allows the firm to [positive consequence 1], thereby [positive consequence 2]. These [actions], however, typically require [cost/delay], resulting in [negative tradeoff]. On the other hand, a firm may be tempted to [Risky Action], [doing only minimal alternative]. By [taking risky action], the firm can [benefit 1] and [benefit 2]. These advantages, however, come at the risk of [negative outcome]. A [negative outcome], when it occurs, could be detrimental both to [Stakeholder A] and to [Stakeholder B]. [Specific damage chains: at a minimum... in worst-case]. The firm not only incurs [direct cost type], but may also incur [other losses]: [list of 3-4 specific costs]."

**来源**: kim2022 (MS), P4

**原文锚定**:
> "On the one hand, a firm can choose to conduct thorough quality assurance testing of various circumstances and conditions encountered in everyday product use. Such testing allows the firm to detect and correct potential sources of product failure, thereby avoiding the possibility of having to issue a recall. These tests, however, typically require a dedicated period of time to complete, resulting in a delay of the product launch. On the other hand, a firm may be tempted to forgo extensive quality assurance testing and rush to market, running only minimal, short-term laboratory tests that are insufficient to detect all possible shortcomings."

**关键特征**:
- 与变体 A 不同——本变体不依赖量化成本数字，而是通过组织行动的后果链条建立张力
- 每边遵循相同结构：Action → Positive consequence → BUT cost/risk → 具体 damage chain
- damage chain 从 mild 到 severe 递进（"at a minimum... in worst-case scenarios..."），建立 escalation 感
- 不以 "few studies have examined" 结尾——以极端后果（"go out of business"）收束，为 Stakes 和 RQ 做情感铺垫

**适用**: 适用于分析模型论文的 Introduction——需要先建立决策情境的丰富纹理再引入形式模型；适用于运营管理、营销战略、管理科学等接受 "决策困境" 作为 Introduction 核心组织逻辑的领域

**禁忌**: "两边必须大致均衡——如果一边的成本/收益明显压倒另一边，决策困境变得虚假；'on the one hand / on the other hand' 是强标记语言——如果期刊要求更 subtle 的写作风格（如 ASQ），应改用 'Firms face a tradeoff between...' 等效表述"

---

### 变体 D：双刃剑信息不对称悖论型（Castellaneta–Conti–Kacperczyk 型）

**验证状态**: EMERGING（单篇来源；仅作 `section_variant`）

**功能节拍**: 对立效应声明 → 通道 A（升值）→ 通道 B（贬值）→ 双刃命名 → 权变消解预告

**模板**:
> "We argue that [X] can move [Y] in opposite directions. Via [channel A: rival-side information / appropriability], stronger [X] [raises Y] by [reducing imitation or misappropriation]. Via [channel B: buyer-side information / adverse selection], stronger [X] [lowers Y] by [worsening valuation uncertainty and bid discounts]. The same instrument thus creates [advantageous asymmetries toward rivals] and [disadvantageous asymmetries toward buyers]. Because the net effect is ambiguous ex ante, we examine when [W_enhance] amplifies channel A and when [W_hinder…] amplify channel B."

**来源**: Castellaneta, Conti & Kacperczyk (2017, SMJ), P3–P4

**原文锚定**:
> 同一保护工具 → 对手侧 vs 买方侧信息不对称 → double-edged → 行业权变消解。

**关键特征**:
- **同一工具、相反通道**：不是决策者在 A/B 行动间选择（变体 C），而是同一制度变量同时制造升值与贬值机制。
- **对称命名双刃**：两边都落在信息对象差异上，便于后续异号调节分别放大各通道。
- **悖论后必须接权变预告**：避免 Intro 停在不可裁决的对立。
- **可兼作 Theory Lens**：在独立 Theory 之前用机制对仗完成解释承诺。

**适用**: Incompleteness × (Mechanism + Boundary)；制度/IP 保护对交易定价或市值可能符号反转；控制权市场、重复交易、信息不对称定价；SMJ。

**禁忌**: 两边机制篇幅须大致对称；不得无消解路径结束；勿与受众价值观对立（`07-same-policy-opposite-effects`）混用；勿整段复述源论文成语。

---

## 相关语料

- 配合 `hooks/07-cost-benefit-tension.md` 使用：Hook 与 Tension 的一体两面
- 配合 `stakes/02-quantified-economic-loss.md` 使用：将抽象成本转化为精确经济损失
