# Coefficient to Substantive Meaning

## 功能定义
将统计系数转化为读者能理解的实质意义——不是"系数=0.35, p<0.05"，而是"CEO持股每增加2个百分点，召回延迟26天"，让数字具备管理 relevant 性和现实可感性。

## 句法模板

**模板 A（标准转化型）**：
```
A one-standard-deviation increase in [IV] is associated with a
[Y-unit] [increase/decrease] in [DV] (coefficient = X.XX, p < .05).
This indicates that [substantive interpretation of coefficient magnitude].
```

**模板 B（概率变化型）**：
```
A change in [IV] from one standard deviation below the mean to one
standard deviation above the mean [increases/decreases] the likelihood
of [DV] from [X%] to [Y%].
```

**模板 C（时间/事件转化型）**：
```
A one-standard-deviation increase—or a [X%] increase—in [IV] is
associated with a [Y-unit] [delay/acceleration] in [DV].
This translates to [concrete comparison: e.g., 'a doubling of the penalty']."
```

**模板 D（对比参照型）**：
```
The coefficient implies that [specific change in IV] leads to
[specific change in DV], which is equivalent to [concrete reference
that readers can imagine: e.g., 'the cost of building a new factory']."
```

## 例句（来自 MVP30）

**来源**：CEO Stock Ownership, Recall Timing, and Stock Market Penalties — Darby et al.

> "A one-standard-deviation increase—or a 2% increase—in the percentage
> of shares owned by the CEO is associated with a 26-day delay in recall
> initiation."

**来源**：CEO Regulatory Focus and Myopic Marketing Management

> "A change in the CEO's promotion focus predominance from one standard
> deviation below the mean to one standard deviation above the mean
> increases the likelihood of myopic marketing management from 16% to 19.4%."

**来源**：Does it Pay to Recall your Product Early? — Eilert et al., 2017 (JM)

> "The shape parameter is greater than 1 ([value], p < .01), suggesting
> that the hazard of [event] increases over the time of the [process]."

**改写模板**：
> "A one-standard-deviation increase in [IV] is associated with a
> [Y-unit] [increase/decrease] in [DV] (coefficient = X.XX, p < .05).
> This indicates that [substantive interpretation: e.g., 'the firm delays
> its response by nearly a month']."

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | JM, SMJ, AMJ — 所有强调管理 relevant 性的期刊 |
| **理论类型** | 通用型——任何实证论文都需要 |
| **前提条件** | 必须报告标准化的效应量；不能只是原始系数 |
| **风险** | 若转化牵强，会损害 credibility；必须使用读者能想象的参照物 |

## 关键技巧

系数转化的核心是**具象化翻译**：

| 弱表达 | 强表达 |
|--------|--------|
| "The coefficient is 0.35" | "A one-standard-deviation increase in X is associated with a 26-day delay in Y" |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 只报告统计显著性 | "p < 0.05" 但不报告效应量 | 必须同时报告系数大小和实质意义 |
| 转化无参照 | "increases by 0.35 units" | 使用读者能理解的单位（天、美元、百分比） |
| 过度转化 | 把微小效应夸大为重大管理意义 | 诚实报告效应量；若效应小，可以说 "modest but meaningful" |

## 相关语料

- 配合 `results-exposition/economic-significance.md` 使用：经济显著性是系数转化的进阶
- 配合 `stakes/02-quantified-economic-loss.md` 使用： stakes 部分的经济损失数字与结果部分呼应
- 配合 `discussion-moves/contribution-statement.md` 使用：贡献声明中的管理启示需要基于系数转化

## 验证状态
- **跨论文复现**: ✓✓ ROBUST（所有 28 篇 MVP30 论文都有系数转化段落）
- **来源论文**: 多篇 × 28
- **生成力**: ✓ GENERATIVE
- **排他性**: 通用
- **期刊限制**: 无限制
- **收录状态**: ⭐ PREMIUM
