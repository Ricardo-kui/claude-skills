# Economic Significance Calculation

## 功能定义
将统计显著性转化为经济显著性——不是"p<0.05"，而是"这个效应值不值得管理者关注"，通过货币化、百分比变化或与基准比较，回答"so what?"问题。

## 句法模板

**模板 A（货币化型）**：
```
The [coefficient/estimate] implies that [specific change in IV] is
associated with a $[X million] [increase/decrease] in [DV].
To put this figure in perspective, [concrete comparison: 'this exceeds
 the annual R&D budget of an average firm in the sample']."
```

**模板 B（百分比变化型）**：
```
A one-standard-deviation increase in [IV] corresponds to a [X%]
[increase/decrease] in [DV], relative to the sample mean.
This translates to [substantive implication for managers].
```

**模板 C（基准比较型）**：
```
The economic magnitude of the effect is [adjective: modest/substantial/
large]. A [specific change] in [IV] is equivalent to [concrete reference:
'eight months of average performance improvement']. Compared with
[benchmark effect: e.g., 'the effect of firm size'], our effect is
[smaller/larger/comparable].
```

**模板 D（成本-收益型）**：
```
While [intervention/treatment] reduces [negative outcome] by [X%],
it also increases [cost] by [Y%]. The net benefit is [positive/negative],
suggesting that [managerial implication].
```

## 例句（来自 MVP30）

**来源**：CEO Stock Ownership, Recall Timing, and Stock Market Penalties — Darby et al.

> "A one-standard-deviation increase—or a 2% increase—in the percentage
> of shares owned by the CEO is associated with a 26-day delay in recall
> initiation... This translates to a [X%] increase in stock market penalties."

**来源**：Does it Pay to Recall your Product Early? — Eilert et al., 2017 (JM)

> "The corresponding losses in shareholder wealth... are $112 million..."
> "The difference in shareholder losses for lower- and higher-reliability
> brands because of recall timing is $84 million."

**来源**：A Rising Tide Lifts All Boats — DesJardine et al.

> "The coefficient implies that a one-standard-deviation increase in
> common ownership is associated with a [X%] increase in CSR performance,
> equivalent to [concrete comparison]."

**改写模板**：> "The [coefficient] implies that [specific change in IV] is associated
> with a [Y-unit] [increase/decrease] in [DV]. To put this figure in
> perspective, [concrete comparison: 'this is equivalent to the annual
> salary of 200 employees']. Compared with [benchmark], our effect is
> [modest/substantial]."

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | SMJ, JM, AMJ — 所有强调管理 relevant 性的期刊 |
| **理论类型** | 管理决策、政策评估、成本-收益分析 |
| **前提条件** | 必须有可信的货币化或百分比转化；不能为了震撼而夸大 |
| **风险** | 经济显著性若过小，会削弱论文贡献；若过大，会被质疑可信度 |

## 关键技巧

经济显著性的核心是**让读者能想象这个数字的现实含义**：

| 弱表达 | 强表达 |
|--------|--------|
| "The effect is economically significant" | "A one-SD increase in X translates to $112 million in shareholder losses—roughly the cost of building a new factory" |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 统计显著=经济显著 | "p < 0.05 so it matters" | 必须独立计算经济显著性；统计显著不一定经济显著 |
| 无基准比较 | 只说"$100 million"但不与什么比较 | 与行业平均、公司规模、或类似研究比较 |
| 货币化牵强 | 把不能货币化的变量强行定价 | 使用百分比变化或排名变化替代 |

## 相关语料

- 配合 `stakes/02-quantified-economic-loss.md` 使用：引言 stakes 中的经济损失数字与结果部分呼应
- 配合 `results-exposition/coefficient-to-substantive.md` 使用：经济显著性是系数转化的进阶
- 配合 `discussion-moves/contribution-statement.md` 使用：贡献声明中的管理意义基于经济显著性

## 验证状态
- **跨论文复现**: ✓ VERIFIED（Eilert et al. 2017; Darby et al.; DesJardine et al.）
- **来源论文**: Eilert et al. (JM) × 1; Darby et al. (SMJ) × 1; DesJardine et al. (SMJ) × 1
- **生成力**: ✓ GENERATIVE
- **排他性**: 通用
- **期刊限制**: 无限制
- **收录状态**: ✓ STANDARD
