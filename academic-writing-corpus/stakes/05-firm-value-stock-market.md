# Firm Value / Stock Market Stakes

## 功能定义
将研究问题连接到企业价值或股东财富的波动，使研究立即获得财务 relevant 性。这种 stakes 特别适合战略、治理、营销和运营论文，因为它提供了一个通用的"货币化"评估框架。

## 句法模板

**模板 A（事件研究型）**：
```
[Event] triggers significant stock market reactions.
[Specific figure: cumulative abnormal returns of X%].
[Translate to dollar terms: this translates to an average loss of $Y million].
[Third sentence: why market reacts — what information is being revealed].
```

**模板 B（机制型）**：
```
[Theoretical mechanism] has direct implications for firm value.
[Explain the causal chain: mechanism → intermediate outcome → stock price].
[Evidence that markets price this mechanism, even if imperfectly].
```

**模板 C（比较估值型）**：
```
Firms that [Condition A] trade at a [premium / discount] of [X%] relative to firms that [Condition B].
[Second sentence: this valuation gap reflects [theoretical mechanism]].
[Third sentence: understanding this gap is important because [practical or theoretical reason]].
```

## 例句（来自 MVP30）

**来源**：Does it Pay to Recall your Product Early?

> "The mean CARs to recall announcements is −.6%, which translates into a mean shareholder loss of $168 million (average market capitalization = $28 billion)."

> "...the corresponding losses in shareholder wealth (at average levels of brand characteristics) because of delayed time to recall are $112 million..."

**改写模板**：> "[Event / Decision / Phenomenon] has significant implications for shareholder value. The mean [abnormal return / valuation impact] is [X%], which translates into an average [loss / gain] of $[Y million] (average market capitalization = $[Z billion]). This [loss / gain] reflects the market's assessment of [theoretical mechanism]."

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | SMJ, JOM, JM, Marketing Science, 任何接受 event study 的期刊 |
| **理论类型** | **信息经济学 / 公司治理 / 市场微观结构** — 任何可以被资本市场定价的现象 |
| **前提条件** | 研究必须有合理的理论连接到 firm value；不能强行 financialize |
| **风险** | 如果理论机制与 stock market 之间没有清晰的逻辑链，会被质疑"为什么要用 CAR" |

## 关键技巧：小系数、大经济意义

这是管理学期刊中**最常见也最容易被 reviewer 挑战**的表达问题。

**叙事升级链**：
1. 报告统计系数（−4.11 × 10⁻⁵）
2. 报告统计显著性（p < .05）
3. 转化为百分比影响（−.6%）
4. 转化为绝对金额（$168 million）
5. 与 benchmark 比较（"equivalent to [X]% of quarterly profit"）

**防御性写作**：
- "Although the coefficient appears modest in magnitude..."
- "Given the large market capitalization of firms in our sample..."
- "These losses are not trivial when multiplied across the industry..."

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 强行 financialize | 研究的是员工满意度，但硬要说"这影响股价" | 必须建立清晰的中介链：satisfaction → productivity → earnings → stock price |
| 数字无比较 | "$168 million loss" — 但不知道这是大是小 | 必须与 benchmark 比较：industry average, firm size, quarterly revenue |
| 因果语言过强 | "Our findings show that X causes Y% stock return" | Event study 只证明"市场对新信息的反应"，不是"X 导致长期价值创造" |

## 相关语料

- 配合 `hooks/03-data-shock.md` 使用：用市场数据作为 opening stakes
- 配合 `results-exposition/economic-significance.md` 使用：将统计结果转化为经济意义的标准流程
- 配合 `discussion-moves/reversal-silver-lining.md` 使用：即使事件负面，也可讨论其对长期估值的正面信号价值
