# Interaction Marginal Effects Narrative

## 功能定义
将交互效应系数转化为边际效应叙事——不是"交互项系数=0.45, p<0.05"，而是"当品牌可靠性高时，问题严重性对召回时间的正向效应减弱了40%"，展示调节变量的实际影响幅度。

## 句法模板

**模板 A（交互项报告型）**：
```
The interaction term between [IV] and [moderator] is [positive/negative]
and [significant] (coefficient = X.XX, p < .05), suggesting that
[interpretation]. To facilitate interpretation, we plot the marginal
effects of [IV] on [DV] at [low/medium/high] levels of [moderator]
(see Figure X).
```

**模板 B（条件效应型）**：
```
At [low level] of [moderator], a one-standard-deviation increase in
[IV] is associated with a [Y-unit] [increase/decrease] in [DV].
At [high level] of [moderator], the same increase in [IV] is associated
with a [Y-unit] [increase/decrease] in [DV].
Thus, [moderator] [strengthens/weakens] the effect of [IV] on [DV]
by [percentage or absolute difference].
```

**模板 C（斜率比较型）**：
```
The slope of [IV] on [DV] is [steep/flat] when [moderator] is [low],
but becomes [flatter/steeper] when [moderator] is [high].
Specifically, the marginal effect decreases from [value] to [value]
as [moderator] increases from the 10th to the 90th percentile.
```

## 例句（来自 MVP30）

**来源**：Public Enemies — Han et al.

> "The interaction term between [IV] and [moderator] is [positive] and
> [significant] (coefficient = X.XX, p < .05), suggesting that [interpretation].
> We plot the marginal effects... at the 10th, 50th, and 90th percentiles
> of [moderator]."

**来源**：Now You See Me — Han et al.

> "Because our models involve nonlinear specifications with multiple
> ordinal outcomes, only interpreting the coefficients and their
> significance can be misleading; therefore, we also report marginal
> effects at the means and modes of the covariates."

**来源**：Does it Pay to Recall your Product Early? — Eilert et al., 2017 (JM)

> "We report marginal effects at the 10th and 90th percentiles of
> [moderator] to show the conditional effect of [IV] on [DV]."

**改写模板**：
> "The interaction term between [IV] and [moderator] is [positive/negative]
> and [significant] (coefficient = X.XX, p < .05), suggesting that
> [interpretation]. To facilitate interpretation, we plot the marginal
> effects of [IV] on [DV] at [low/medium/high] levels of [moderator].
> At [low level] of [moderator], a one-standard-deviation increase in
> [IV] is associated with a [Y-unit] [change] in [DV]. At [high level],
> the same increase is associated with a [Y-unit] [change]. Thus,
> [moderator] [strengthens/weakens] the effect by [difference]."

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | 通用型——所有包含交互项的论文 |
| **理论类型** | 调节效应、条件效应、边界条件 |
| **前提条件** | 非线性模型（logit, probit, Tobit, AFT）必须报告边际效应；线性模型也需条件效应图 |
| **风险** | 仅报告交互项系数会导致误读；必须结合条件效应图或边际效应表 |

## 关键技巧

交互效应叙事的核心是**让读者看到两条不同的斜率**：

| 弱表达 | 强表达 |
|--------|--------|
| "The interaction is significant" | "When brand reliability is high, the effect of severity on recall time is reduced by 40% compared to when reliability is low" |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 只报告交互系数 | 系数方向与条件效应方向可能相反 | 必须绘制条件效应图或报告边际效应 |
| 无参照点 | "边际效应=0.3"但不说明在什么水平 | 在均值、±1SD、或十分位数报告 |
| 图表无标注 | 图中有两条线但不标注哪条对应哪组 | 明确标注高低调节水平 |

## 相关语料

- 配合 `hypotheses/moderation-weakening.md` 和 `moderation-strengthening.md` 使用：假设的理论预测必须在边际效应中展示
- 配合 `results-exposition/coefficient-to-substantive.md` 使用：交互效应的系数转化需分别报告各条件下的效应
- 配合 `results-exposition/economic-significance.md` 使用：条件效应的经济显著性需分条件计算

## 验证状态
- **跨论文复现**: ✓✓ ROBUST（所有含交互项的 MVP30 论文都报告边际效应）
- **来源论文**: 多篇 × 28
- **生成力**: ✓ GENERATIVE
- **排他性**: 通用
- **期刊限制**: 无限制
- **收录状态**: ⭐ PREMIUM
