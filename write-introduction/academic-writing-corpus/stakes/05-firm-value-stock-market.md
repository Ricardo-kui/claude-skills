---
type: canonical_stakes
canonical_id: "05-firm-value-stock-market"
status: ✓ STANDARD
gap_type: Incompleteness / Inadequacy
cross_paper: VERIFIED
generativity: ADAPTABLE
exclusivity: MEDIUM
source_papers:
  - eilert2017 (JM, 2017): "CAR −.6% → $168M loss; delayed recall → $112M additional loss"
  - vadakkepatt2022 (JM, 2022): "positive lobbying→firm value but negative via customer satisfaction"
  - malshe2015 (JM, 2015): "1-SD leverage increase → $26M operating cash flow loss"
  - darby2024 (MSOM, 2024): "stock market penalties magnified by recall delay"
created: 2026-05-19
source: Extracted from MVP30 narrative_analysis files + global corpus migration
---

# 05-firm-value-stock-market — 企业价值/资本市场 Stakes

## 功能描述

将研究问题连接到企业价值或股东财富的波动，使研究立即获得财务相关性。这种 Stakes 特别适合战略、治理、营销和运营论文，因为它提供了一个通用的"货币化"评估框架。与 `02-quantified-economic-loss` 的区别：本模块聚焦于**资本市场定价机制**（股价反应、估值折扣、股东财富），而非广义的运营成本或经济损失。

## 适用场景

- 研究涉及股价反应、事件研究、托宾Q、市场估值
- 研究含公司治理、战略决策、政治行为、创新投资的财务后果
- 目标期刊接受 event study 或财务绩效作为结果变量（SMJ, JOM, JM, MSOM, AMJ）
- 需要说服读者"市场会惩罚/奖励这种行为"

## 验证状态

### 跨论文复现
- **VERIFIED** (≥4 papers): eilert2017 (JM), malshe2015 (JM), darby2024 (MSOM), vadakkepatt2022 (JM)
- 跨越产品召回、财务杠杆、游说、召回时机等多元领域

### 生成力
- **ADAPTABLE**: "market prices this information" 逻辑高度可迁移，但需要清晰的中介链

### 排他性
- **MEDIUM**: 必须与股价/估值有合理理论连接；不能强行 financialize

---

## 句法模板

### 变体 A：事件研究+金额转化型（eilert2017 型）

**模板**:
> "[Event / Decision / Phenomenon] has significant implications for shareholder value. The mean [abnormal return / valuation impact] is [X%], which translates into an average [loss / gain] of $[Y million] (average market capitalization = $[Z billion]). This [loss / gain] reflects the market's assessment of [theoretical mechanism]."

**来源**: eilert2017 (JM), P1 + results

**原文锚定**:
> "The mean CARs to recall announcements is −.6%, which translates into a mean shareholder loss of $168 million (average market capitalization = $28 billion)."
> "...the corresponding losses in shareholder wealth (at average levels of brand characteristics) because of delayed time to recall are $112 million..."

**关键特征**:
- 统计系数 → 百分比 → 绝对金额，三层递进
- 必须给出 average market capitalization 作为分母，让读者判断金额大小
- 第二句用 "because of [mechanism]" 建立因果链（不是相关是市场评估）

**适用**: 事件研究论文（召回、并购、CEO变更、丑闻等）

---

### 变体 B：经济显著性锚定型（malshe2015 型）

**模板**:
> "The impact is economically significant: [quantification of effect size in dollar terms or percentage]. This is especially meaningful when [baseline comparison]. Without understanding [mechanism], [actors] are likely to [overestimate/underestimate] [outcome], especially in firms with [condition]."

**来源**: malshe2015 (JM), P3

**原文锚定**:
> "The impact of leverage on satisfaction is economically significant: a one-standard-deviation increase in leverage from the average level results in a .47 point decrease in customer satisfaction, which is equivalent to an estimated loss of $26 million in net operating cash flows."

**关键特征**:
- "one-standard-deviation increase" 建立效应量的管理直观性
- 将统计效应转化为具体金额（$26 million）
- 金额必须有计算依据，不能凭空编造

**适用**: 面板数据/回归研究，需要将系数转化为经济意义

---

### 变体 C：市场惩罚放大型（darby2024 型）

**模板**:
> "We find that [behavior] significantly magnifies the [market penalty], with [quantified consequence]. The consequences extend beyond [immediate outcome] to [broader outcome], affecting [stakeholders]. Moreover, no studies of which we are aware have examined [specific financial consequence]."

**来源**: darby2024 (MSOM), P6

**关键特征**:
- "significantly magnifies" → 不只说"有影响"，说"放大惩罚"
- 区分直接后果（召回成本）和市场后果（stock penalty）
- 暗示如果管理者不理解这个机制，会同时承担运营和财务双重损失

**适用**: 研究行为/决策的财务后果，尤其是惩罚性后果

---

### 变体 D：估值矛盾揭示型（vadakkepatt2022 型）

**模板**:
> "Previous findings reveal a [direction] effect of [IV] on [financial outcome] ([citations]). However, when we account for [mediator], this [direction] effect is [counteracted/diminished] because [mediator] also [direction] affects [financial outcome]. This insight challenges [literature] that suggests largely [direction] effects of [IV] on [financial outcome]."

**来源**: vadakkepatt2022 (JM), P5

**原文锚定**:
> "We also replicate previous findings of a positive effect of lobbying on firm value but identify a negative counteracting effect when we account for customer satisfaction. This insight challenges economic and finance literature that suggests largely positive effects of lobbying on firm value."

**关键特征**:
- 先承认已有发现的正确性（"replicate previous findings"）
- 再用新视角揭示隐藏成本（"identify a negative counteracting effect"）
- "challenges [literature]" → 将修正框定为对文献的贡献而非否定

**适用**: 研究某行为的财务后果但发现存在被忽视的抵消机制

---

## 关键技巧：小系数、大经济意义

这是管理学期刊中**最常见也最容易被 reviewer 挑战**的表达问题。

### 叙事升级链
1. 报告统计系数（−4.11 × 10⁻⁵）
2. 报告统计显著性（p < .05）
3. 转化为百分比影响（−.6%）
4. 转化为绝对金额（$168 million）
5. 与 benchmark 比较（"equivalent to [X]% of quarterly profit" / "equivalent to [Y]% of industry average R&D spend"）

### 防御性写作
- "Although the coefficient appears modest in magnitude..."
- "Given the large market capitalization of firms in our sample..."
- "These losses are not trivial when multiplied across the industry..."
- "When aggregated across all [actor] in [market], the total impact exceeds $[X billion]."

---

## 插入位置指南

| 布局类型 | 推荐插入位置 | 形式 |
|---------|------------|------|
| 紧凑型 | Gap 段末尾或 Findings Preview 中（1-2句） | Inline |
| 标准型 | 独立 P4（2-3句） | 独立段 |
| 扩展型 | 独立 P4 + 经济显著性计算细节 | 独立段 |

**注意**: JM/JMR 偏好将经济显著性直接嵌入 Findings Preview（如 vadakkepatt2022 的紧凑结构），而非独立的 Stakes 段落。SMJ/AMJ 偏好独立的 Stakes 或贡献段中的财务论证。

---

## 组装规则

### 必须配对
- **必须在 Gap 之后出现**: Stakes 是缺口重要性的论证
- **与具体数字的真实性绑定**: 不能编造数字；金额必须来自可引用的来源或可复现的计算
- **必须建立中介链**: 不能从行为直接跳到股价，必须说明 "market prices [information/mechanism]"

### 互斥
- **不能与 `02-quantified-economic-loss` (Stakes) 同用**: 两者都是财务 Stakes，重复使用会造成 stakes 冗余。选择原则：若研究直接涉及股价/CAR/估值，用本模块；若涉及广义运营成本/效率损失，用量化经济损失
- **不能与 `03-data-shock` (Hook) 同用**: 若 Hook 已用市场数据开场，Stakes 应转向理论或实践层面，避免数字疲劳

### 反模式提醒
- **强行 financialize**: 研究的是员工满意度，但硬要说"这影响股价"——必须建立清晰的中介链：satisfaction → productivity → earnings → stock price
- **数字无比较**: "$168 million loss" 但不告诉读者这是大是小——必须与 benchmark 比较
- **因果语言过强**: "Our findings show that X causes Y% stock return" → Event study 只证明"市场对新信息的反应"，不是"X 导致长期价值创造"
- **只给百分比不给金额**: 对管理者来说，−.6% 不如 $168 million 直观

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| JM/JMR | ⭐⭐⭐ 极高 | 经济显著性在 Intro 中报告是标准预期；偏好"系数→金额→benchmark"三段式 |
| SMJ | ⭐⭐⭐ 高 | 偏好战略后果与股东价值的连接；可接受 event study 语言 |
| JOM/MSOM/POM | ⭐⭐⭐ 高 | 偏好运营成本+市场惩罚双重论证 |
| AMJ | ⭐⭐ 中 | 需与理论重要性并行，不能只有财务数字 |
| ASQ | ⭐ 低 | 纯经济 stakes 与 ASQ 理论导向不匹配；如用，必须连接到制度/场域理论 |

---

## 相关语料

- 配合 `results-exposition/economic-significance.md` 使用：将统计结果转化为经济意义的标准流程
- 配合 `hooks/03-data-shock.md` 使用：若 Hook 未用市场数据，Stakes 可用市场数据建立第二重震撼
- 配合 `discussion-moves/reversal-silver-lining.md` 使用：即使事件负面，也可讨论其对长期估值的正面信号价值