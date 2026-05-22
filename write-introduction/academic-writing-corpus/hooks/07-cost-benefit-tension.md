---
type: canonical_hook
canonical_id: "07-cost-benefit-tension"
status: ✓ STANDARD
gap_strength: 低/中
gap_type: Incompleteness / Inadequacy
cross_paper: VERIFIED
generativity: ADAPTABLE
exclusivity: MEDIUM
pollock_type: Anecdote
source_papers:
  - eilert2017 (JM, 2017): "Recall costs vs delay costs — Toyota $17.35m → GM $900m escalation"
created: 2026-05-19
source: Extracted from MVP30 narrative_analysis + eilert2017 distill
---

# 07-cost-benefit-tension — 成本收益张力 Hook

## 功能描述

通过精确呈现一个决策情境中双方对立的成本结构，制造"两边都是深渊"的决策困境，使"时机/选择/策略"成为不可避免的研究问题。以负面事件为核心，但焦点不是事件本身，而是决策者面临的**结构性张力**。

## 适用场景

- 研究涉及组织必须在两个不利选项之间做出权衡（如召回 vs 延迟召回、合规 vs 灵活、透明 vs 保护）
- 存在可量化的、有权威来源的成本数据（SEC 罚款、DOJ 处罚、公司财报）
- 目标期刊接受决策困境开场（JM、JOM、SMJ、OS）
- 需要同时建立**理论相关性**（行为理论/有限理性）和**实践紧迫性**

## 验证状态

### 跨论文复现
- **VERIFIED**: eilert2017 (JM) 经典案例
- 类似结构见于产品召回、合规、危机响应、供应链中断研究

### 生成力
- **ADAPTABLE**: "[Action] is costly... However, delaying [action] may lead to even higher costs" 框架可适配任何双向成本结构

### 排他性
- **MEDIUM**: 主要在涉及组织决策困境的研究中出现

---

## 句法模板

### 变体 A：双面对称 + 案例锚定型（eilert2017 型）

**模板**:
> "[Action A] is costly; [specific direct costs] and [specific indirect costs] make it a [devastating/threatening] prospect for firms. [Second sentence: compelling reason to delay or avoid]. However, delaying [Action A] may lead to even higher costs through [fine mechanism], [liability mechanism], and most importantly, [reputational mechanism] ([citation]). [Specific case with dollar figure]. [Second case with even larger dollar figure]. Therefore, although [Action A] are adverse events in general, a quick response may attenuate the damage ([citation])."

**来源**: eilert2017 (JM), P1

**原文锚定**:
> "Recalls are costly; announcing and implementing one is associated with both direct costs in repair, restitution, or liability and indirect costs such as losses in reputation and market value. Consequently, recalls could have a devastating impact on a firm's performance, sometimes even threatening its survival. Thus, a firm has reasons to avoid a quick recall and instead wait for the investigation to conclude. However, delaying a product recall may lead to higher direct and indirect costs through fines, liability damages, and most importantly, diminished reputation. In 2012, Toyota was fined $17.35 million dollars for delaying a floor mat recall. The U.S. Department of Justice fined General Motors $900 million for willfully delaying the recall for a faulty ignition switch..."

**关键特征**:
- 以 "[Action] is costly" 建立第一面张力
- "Consequently... could have a devastating impact" → 强化严重性
- "Thus, a firm has reasons to avoid" → 给出延迟的合理动机
- "However, delaying... may lead to even higher costs" → 建立第二面张力
- **数字递进公式**: 抽象 → 类别 → 小案例 → 大案例（10x-100x 跳跃）
  - Toyota $17.35m → GM $900m 制造了数量级震撼

**适用**: 产品召回、合规、危机响应、供应链中断等涉及"行动 vs 延迟"两难的研究

---

### 变体 B：精简版（适用于篇幅受限期刊）

**模板**:
> "[Actors] face a dilemma when [external event occurs]. On one hand, [reason to delay]. On the other hand, [reason to act quickly]. [Institutional evidence of variation]. This tension raises important questions for [audience]."

**适用**: 当期刊 Introduction 字数限制较紧时（JM/JMR 偏好更紧凑的 Hook）

---

## 组装规则

### 必须配对
- **与 Progressive Coherence 或 Synthesized Coherence Literature Turn 配对**: 成本张力建立决策困境，文献对话需要展示已有研究如何处理/未处理此困境
- **与 Incompleteness Gap 配对**: 张力 Hook 建立"问题存在且复杂"，Gap 解释"已有理解过于简化（只看一面成本）"

### 互斥
- **不适合与 `03-data-shock` 同用**: 两者都依赖数字，会造成信息过载
- **不适合与 Incommensurability 直接配对**: 张力建立的是"决策困境"，不是"理论对立"

### 反模式提醒
- **只有一面**: 只讲行动成本，不讲延迟成本 → 必须对称呈现
- **数字无来源**: "罚款可能高达数百万" → 给出精确数字和权威来源
- **停留在案例**: 讲完案例就结束了 → 必须转化为普遍问题
- **忽略正面效应**: 简单罗列负面后果会削弱可信度

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| JM | ⭐⭐⭐⭐⭐ | 决策困境是 JM 的标志性 Hook 策略 |
| JOM | ⭐⭐⭐⭐⭐ | 运营/供应链/质量管理研究的标准 Hook |
| SMJ | ⭐⭐⭐⭐☆ | 适合战略决策、治理研究；需更快转入理论 |
| OS | ⭐⭐⭐⭐☆ | 适合实践张力→理论 puzzle 的转译 |
| AMJ | ⭐⭐⭐☆☆ | 可用但需更快显示理论通用性 |

---

## 相关语料

- 配合 `tensions/08-cost-vs-benefit.md` 使用：在文献综述中进一步强化决策困境的理论化
- 配合 `stakes/02-quantified-economic-loss.md` 使用：将案例数字延伸到股东财富损失
- 配合 `transitions/01-hook-to-literature.md` 使用：从"决策困境"过渡到"已有文献如何解释这种困境"
