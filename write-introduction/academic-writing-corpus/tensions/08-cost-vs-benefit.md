---
type: canonical_reference
canonical_id: "08-cost-vs-benefit"
status: ✓ STANDARD
gap_type: Incompleteness / Inadequacy
cross_paper: VERIFIED
generativity: ADAPTABLE
exclusivity: MEDIUM
source_papers:
  - eilert2017 (JM, 2017): "Recall costs vs delay costs — Toyota $17.35m → GM $900m escalation"
created: 2026-05-19
source: Extracted from MVP30 narrative_analysis + eilert2017 distill
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

## 相关语料

- 配合 `hooks/07-cost-benefit-tension.md` 使用：Hook 与 Tension 的一体两面
- 配合 `mechanisms/dual-path-ability-motivation.md` 使用：成本对应动机约束，收益对应能力约束
- 配合 `stakes/02-quantified-economic-loss.md` 使用：将抽象成本转化为精确经济损失
