# Inverted-U Hypothesis

## 功能定义
陈述自变量与因变量之间的倒U型关系假设——效应随自变量增加先增强后减弱，预测最优水平存在于中间区间，适用于两种对立机制此消彼长的情境。

## 句法模板

**模板 A（双逻辑反转型）**：
```
Because both [Theory A] and [Theory B] offer valid arguments, we need
to consider both when examining the overall effect of [X] on [Y].
When [X] increases from zero to [low level], the [positive mechanism]
becomes more salient yet the [negative mechanism] is relatively minor.
As [X] moves from [low] to [high] levels, however, the [negative
mechanism] becomes evident. Thus we predict that a [moderate] level
of [X] is most beneficial to [Y]:
Hypothesis [N]: [X] has an inverted U-shaped impact (first increasing
and then decreasing) on [Y], such that a [moderate level] of [X]
generates the most [Y].
```

**模板 B（简洁型）**：
```
We propose that the relationship between [X] and [Y] follows an
inverted U-shaped pattern. At low levels of [X], [positive mechanism]
dominates. However, as [X] continues to increase, [negative mechanism]
begins to offset and eventually overwhelm the positive effect.
Hypothesis [N]: [X] has an inverted U-shaped effect on [Y].
```

**模板 C（三假设分解型）**：
```
We decompose the overall effect of [X] on [Y] into three stages:
Hypothesis [N]a: At low levels of [X], [X] is positively related to [Y].
Hypothesis [N]b: At high levels of [X], [X] is negatively related to [Y].
Hypothesis [N]c: The overall relationship between [X] and [Y] follows
an inverted U-shaped pattern.
```

## 例句（来自 MVP30）

**来源**：State Ownership and Firm Innovation — Zhou et al., 2017 (ASQ)

> "Whereas the institutional view emphasizes the resource advantage brought by state ownership, the efficiency view highlights the dual agency problem caused by state ownership. Because both views offer valid arguments, we need to consider both when examining the overall effect of state ownership on innovation."

> "When state ownership increases from zero to minority levels, the institutional effect becomes more salient yet the efficiency problem is relatively minor... As state ownership moves from minority to majority levels, however, the additional resource allocation advantages increase rather incrementally, but the decision-making power shifts to the managers designated by government officials. Accordingly, the dual agency problem of SOEs becomes evident... Thus we predict that a minority level of state ownership is most beneficial to innovation:"

> **Hypothesis 1c (H1c):** State ownership of a firm has an inverted U-shaped impact (first increasing and then decreasing) on its innovation, such that a minority state ownership generates the most innovation output.

**改写模板**：
> "Because both [Theory A] and [Theory B] offer valid arguments, we need
> to consider both when examining the overall effect of [X] on [Y].
> When [X] increases from zero to [low level], the [positive mechanism]
> becomes more salient yet the [negative mechanism] is relatively minor.
> As [X] moves from [low] to [high] levels, however, the [negative
> mechanism] becomes evident. Thus we predict that a [moderate] level
> of [X] is most beneficial to [Y]:
> **Hypothesis [N]:** [X] has an inverted U-shaped impact (first increasing
> and then decreasing) on [Y], such that a [moderate level] generates
> the most [Y]."

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | ASQ, AMJ — 适合制度逻辑冲突论文；SMJ 适合战略决策 |
| **理论类型** | 制度经济学、代理理论、组织经济学、最优结构理论 |
| **前提条件** | 必须有两种对立理论；必须能理论预测拐点位置；必须使用 U-test |
| **风险** | 倒U型极易被质疑为数据挖掘；必须在理论部分预先提出，且报告拐点置信区间 |

## 关键技巧

倒U型假设的关键是**力量的此消彼长必须有理论节奏**：

| 弱表达 | 强表达 |
|--------|--------|
| "X has an inverted-U effect on Y" | "The positive effect increases incrementally at low levels, but the negative effect becomes dominant beyond a threshold because [theoretical mechanism]" |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 事后发现倒U | 先跑回归发现 X² 显著，再编两个理论 | 两种对立理论必须在理论部分同时提出 |
| 拐点无理论 | "中间最好"但说不清为什么 | 用理论论证拐点的位置 |
| 只报告二次项 | 只跑 X + X²，不做 U-test | 必须报告 Lind & Mehlum (2010) 或类似检验 |

## 相关语料

- 配合 `mechanisms/inverted-u-mechanism.md` 使用：倒U型机制的理论论证模板
- 配合 `mechanisms/context-reversal.md` 使用：倒U型是情境反转的一种数学表现
- 配合 `results-exposition/interaction-marginal-effects.md` 使用：结果部分用边际效应展示倒U型曲线

## 验证状态
- **跨论文复现**: ⚠️ SINGLE-INSTANCE（仅 Zhou et al. 2017 完整使用）
- **来源论文**: Zhou et al. (ASQ) × 1
- **生成力**: 待验证
- **排他性**: 高——仅适用于两种对立理论同时成立的构念
- **期刊限制**: ASQ 极度适合；AMJ/SMJ 可用但需强调绩效含义
- **收录状态**: 🔬 EXPERIMENTAL
