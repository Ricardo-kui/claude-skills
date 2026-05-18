---
type: canonical_hook
canonical_id: "03-data-shock"
status: ✓ STANDARD
gap_strength: 低
gap_type: Incompleteness
cross_paper: VERIFIED
generativity: ADAPTABLE
exclusivity: MEDIUM
source_papers:
  - eilert2017 (JM, 2017): "390 recalls in 2014, NHTSA data"
  - darby2024 (MSOM, 2024): "CEO stock ownership and recall timing"
  - shi2021 (JMR, 2021): "organizational herding in advertising disclosures"
created: 2026-05-18
source: Manually curated from MVP30 narrative_analysis files
---

# 03-data-shock — 数据冲击 Hook

## 功能描述

用具体数字、统计趋势或市场规模建立现象的 scale 和重要性。不争论理论，不挑战范式——纯粹用数据让读者意识到"这个问题足够大，值得关注"。是 Incompleteness 问题化最常用的低能量 Hook。

## 适用场景

- Gap 类型 = **Incompleteness**（文献留下关系、机制、时点或结果维度的空白）
- 研究涉及具有可量化规模的市场现象（产品召回、广告支出、安全事件等）
- 目标读者是实证导向的（营销、运营、金融期刊）
- 论文需要快速建立"为什么这个问题重要"而不需要理论辩论

## 验证状态

### 跨论文复现
- **VERIFIED** (≥3 papers): 在 JMR (shi2021), MSOM (darby2024), JM (eilert2017) 中独立出现
- 跨越不同研究领域：产品召回、广告支出、运营管理

### 生成力
- **ADAPTABLE**: 可在营销、运营、金融等量化领域有效使用，但在理论型期刊（ASQ/ASR）中适配度低

### 排他性
- **MEDIUM**: 跨 Gap 类型可用（Incompleteness 最常见，但也可用于 Inadequacy 的补充），但在 Incommensurability 中不应使用

---

## 句法模板

### 变体 A：趋势+规模型（eilert2017 型）

**模板**:
> "[Phenomenon] affect [stakeholder 1] and expose [stakeholder 2] to [risks]. Consequently, [outcome]. In [country], [regulatory body] reported [statistic]. In [specific industry], [regulatory body] has overseen [scale of phenomenon]."

**来源**: eilert2017 (JM), P1

**原文锚定**:
> "Defective products affect the physical safety of consumers and expose manufacturers to liability claims, fines, and loss of reputation. Consequently, defective products are often recalled... In the United States, the Consumer Products Safety Commission reported a total of 390 recalls in 2014... In the U.S. automobile industry, the National Highway Transportation and Safety Agency (NHTSA) has overseen recalls involving hundreds of millions of vehicles."

**关键特征**:
- 从通用现象（产品安全）缩放到具体数字（390 recalls）
- 同时涉及消费者和制造商两个利益相关方
- "Consequently" 自然过渡到研究主题
- 两个递增的规模数字（390 → hundreds of millions）

---

### 变体 B：行业新闻型（shi2021 型）

**模板**:
> "In [year], [specific event with number]. This [event] highlights [broader phenomenon]. In fact, [industry data showing scale]. Yet, despite [scale/importance], [what we don't know]."

**来源**: shi2021 (JMR), adapted

**关键特征**:
- 用具体行业事件开场（而非纯数字）
- 事件→现象→数据→缺口，逐步收窄
- 数字不是目的，是建立 relevance 的手段

---

### 变体 C：成本量化型（eilert2017 P2-P3 型）

**模板**:
> "[Action A] could have [negative consequence]. Thus, [actor] has reasons to [avoid action]. However, [avoiding action] may lead to [worse consequence]. [Example + dollar figure]. Therefore, although [phenomenon] are adverse events, [quick action] may [positive outcome]."

**来源**: eilert2017 (JM), P2-P3

**原文锚定**:
> "Recalls are costly... Consequently, recalls could have a devastating impact... Thus, a firm has reasons to avoid a quick recall... However, delaying a product recall may lead to higher direct and indirect costs... In 2012, Toyota was fined $17.35 million... Therefore, although recalls are adverse events in general, a quick response may attenuate the damage."

**关键特征**:
- "Thus... However... Therefore..." 建立双向成本逻辑链
- 用具体案例+美元金额（Toyota, $17.35 million）支撑论证
- 成本-收益张力建立后自然引出研究问题

---

## 组装规则

### 必须配对
- **与 `01-despite-progress-unaddressed` (Tension) 配对**: 数据冲击建立了 stakes，但还需要解释"已有进展中遗漏了什么"，否则读者会问"so what academically?"

### 互斥
- **不能与 `02-quantified-economic-loss` (Stakes) 同用**: 数据冲击 Hook 已含 stakes 论证，再用量化损失 Stakes 会造成数字疲劳和功能冗余
- **不能与 `06-paradigm-challenge` (Hook) 同用**: 能量等级冲突（低 vs 高）

### 反模式提醒
- **不要堆砌数字而无叙事**: 数据冲击 Hook 的核心是数据+叙事链，不是数据dump
- **不要使用过时的数据**: 数据的冲击力依赖于时效性
- **不要在没有真实数据时编造**: 如果领域没有可信的规模统计，改用其他 Hook 类型

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| JM/JMR | ⭐⭐⭐ 极高 | 营销期刊首选；可搭配 Table 1 文献缺口可视化 |
| MSOM | ⭐⭐⭐ 极高 | 运营期刊偏好量化开场 |
| SMJ | ⭐⭐ 中 | 需搭配明确的战略重要性论证 |
| JOM | ⭐⭐ 中 | 适合运营/供应链研究 |
| ASQ/ASR | ⭐ 低 | 理论型期刊不建议纯数据开场 |
