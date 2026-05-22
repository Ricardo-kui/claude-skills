# Inverted-U Mechanism

## 功能定义
论证自变量与因变量之间存在倒U型关系——初期正向效应随自变量增加而增强，但超过拐点后负向机制开始主导，从而预测最优水平存在于中间区间而非极端值。

## 句法模板

**模板 A（双逻辑整合型）**：
```
The [Theory A] view emphasizes the [positive aspect] brought by [X],
whereas the [Theory B] view highlights the [negative aspect] caused by [X].
Because both views offer valid arguments, we need to consider both when
examining the overall effect of [X] on [Y]. A firm may be [low X],
[moderate X], or [high X], and the varying degree of [X] can make the
[Theory A] or [Theory B] logic more or less salient.

When [X] increases from zero to [low level], the [positive mechanism]
becomes more salient yet the [negative mechanism] is relatively minor.
As [X] moves from [low] to [high] levels, however, the additional
[positive effect] increases rather incrementally, but the [negative
mechanism] becomes evident. Thus we predict that a [moderate] level
of [X] is most beneficial to [Y]: [Hypothesis statement].
```

**模板 B（边际递减转换型）**：
```
At low levels of [X], [positive mechanism] dominates because [reason].
However, as [X] continues to increase, [negative mechanism] begins to
offset and eventually overwhelm the positive effect because [reason].
Therefore, the relationship between [X] and [Y] follows an inverted
U-shaped pattern, with the optimal level of [X] occurring at [theoretical
prediction or empirical range].
```

**模板 C（三区间划分型）**：
```
We identify three regions in the [X]-[Y] relationship.
In Region 1 ([low X]), [positive mechanism] operates virtually unopposed.
In Region 2 ([moderate X]), [positive mechanism] and [negative mechanism]
are in tension, with the positive effect still dominant but diminishing.
In Region 3 ([high X]), [negative mechanism] dominates, producing a net
negative effect on [Y].
```

## 例句（来自 MVP30）

**来源**：State Ownership and Firm Innovation — Zhou et al., 2017 (ASQ)

> "Whereas the institutional view emphasizes the resource advantage brought
> by state ownership, the efficiency view highlights the dual agency problem
> caused by state ownership. Because both views offer valid arguments, we
> need to consider both when examining the overall effect of state ownership
> on innovation. A firm may be majority state-owned (an SOE), minority
> state-owned (a mixed firm), or privately owned without state capital, and
> the varying degree of state ownership can make the institutional or
> efficiency logic more or less salient."

> "When state ownership increases from zero to minority levels, the
> institutional effect becomes more salient yet the efficiency problem is
> relatively minor... As state ownership moves from minority to majority
> levels, however, the additional resource allocation advantages increase
> rather incrementally, but the decision-making power shifts to the managers
> designated by government officials. Accordingly, the dual agency problem
> of SOEs becomes evident... Thus we predict that a minority level of
> state ownership is most beneficial to innovation:"

> **Hypothesis 1c (H1c):** State ownership of a firm has an inverted U-shaped
> impact (first increasing and then decreasing) on its innovation, such that
> a minority state ownership generates the most innovation output.

**改写模板**：
> "Because both [Theory A] and [Theory B] offer valid arguments, we need to
> consider both when examining the overall effect of [X] on [Y]. When [X]
> increases from zero to [low level], the [positive mechanism] becomes more
> salient yet the [negative mechanism] is relatively minor. As [X] moves
> from [low] to [high] levels, however, the [negative mechanism] becomes
> evident. Thus we predict that a [moderate] level of [X] is most
> beneficial to [Y]: [Hypothesis statement]."

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | ASQ, AMJ, SMJ — 适合复杂机制论文；ASQ 偏好制度逻辑整合 |
| **理论类型** | 制度经济学、代理理论、组织经济学、资源基础观冲突 |
| **前提条件** | 必须有两种对立理论各自成立的条件区间；必须能理论预测拐点位置 |
| **风险** | 倒U型关系极易被质疑为数据挖掘；必须在理论部分预先提出，且结果部分报告拐点置信区间 |

## 关键技巧

倒U型论证的关键是**力量的此消彼长必须有理论节奏**：

| 弱表达 | 强表达 |
|--------|--------|
| "X has an inverted-U effect on Y" | "The positive effect increases incrementally at low levels, but the negative effect becomes dominant beyond a threshold because [theoretical mechanism]" |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 事后发现倒U | 先跑回归发现倒U，再编两个理论 | 两种对立理论必须在理论部分同时提出 |
| 拐点无理论 | "中间最好"但说不清为什么是这个拐点 | 用理论论证拐点的位置（如 minority ownership） |
| 只报告二次项 | 只跑 X + X²，不做 U-test | 必须报告 Lind & Mehlum (2010) 或类似检验 |

## 相关语料

- 配合 `hypotheses/inverted-u-hypothesis.md` 使用：正式假设的倒U型句式
- 配合 `results-exposition/interaction-marginal-effects.md` 使用：结果部分用边际效应展示倒U型曲线
- 配合 `mechanisms/context-reversal.md` 使用：倒U型是情境反转的一种数学表现

## 验证状态
- **跨论文复现**: ⚠️ SINGLE-INSTANCE（仅 Zhou et al. 2017 完整使用）
- **来源论文**: Zhou et al. (ASQ) × 1
- **生成力**: 待验证
- **排他性**: 高——仅适用于两种对立理论同时成立的构念
- **期刊限制**: ASQ 极度适合；AMJ/SMJ 可用但需强调绩效含义
- **收录状态**: 🔬 EXPERIMENTAL
