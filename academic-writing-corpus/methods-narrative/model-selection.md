# Model Selection Narrative

## 功能定义
为统计模型的选择提供方法论辩护，展示研究者对因变量分布特征、数据结构和估计偏误的系统考量——不是"用了什么模型"，而是"为什么这个模型最适合数据的生成过程"。

## 句法模板

**模板 A（分布匹配型）**：
```
We analyze [DV] using a [Model Name] with a [Distribution] for the
underlying [failure rate/error structure]. This model is appropriate
because [DV] is [non-negative/censored/count/ordinal], and a standard
[OLS] approach would [produce biased estimates/violate assumptions].
```

**模板 B（非线性解释型）**：
```
Because our models involve nonlinear specifications with [multiple
ordinal outcomes/multiple interaction terms], only interpreting the
coefficients and their significance can be misleading; therefore, we
also report [marginal effects/average marginal effects/predicted
probabilities] to facilitate substantive interpretation.
```

**模板 C（固定效应型）**：
```
Our main analyses use [OLS/regressions] with [firm fixed effects]
that control for observed and unobserved time-invariant [firm]
characteristics and [year fixed effects] that control for common
[macroeconomic] shocks that affect all [units].
```

**模板 D（工具变量/2SLS型）**：
```
To account for potential endogeneity of [IV], we employ a [two-stage
least squares (2SLS)/control function] approach. In the first stage,
we regress [endogenous variable] on [instrument(s)] and [controls].
In the second stage, we use the predicted values from the first stage
to estimate the effect on [DV].
```

## 例句（来自 MVP30）

**来源**：Does it Pay to Recall your Product Early? — Eilert et al., 2017 (JM)

> "We analyze time to recall using a Weibull accelerated failure time
> (AFT) hazard model."

**来源**：CEO Stock Ownership, Recall Timing, and Stock Market Penalties — Darby et al.

> "We tested Hypotheses 1 and 2 using accelerated failure time (AFT)
> models with a Weibull distribution for the underlying failure rate."

**来源**：State Ownership and Firm Innovation — Zhou et al., 2017 (ASQ)

> "We employed a Tobit analysis to deal with the non-negative nature
> of our dependent variables."

**来源**：Now You See Me — Han et al.

> "Because our models involve nonlinear specifications with multiple
> ordinal outcomes, only interpreting the coefficients and their
> significance can be misleading; therefore, we also report marginal
> effects."

**来源**：A Rising Tide Lifts All Boats — DesJardine et al.

> "Our main analyses use ordinary least squares (OLS) regressions with
> firm fixed effects that control for observed and unobserved
> time-invariant firm characteristics and year fixed effects that control
> for common macroeconomic shocks that affect all firms."

**改写模板**：
> "We analyze [DV] using a [Model] with a [Distribution]. This model
> is appropriate because [DV] is [non-negative/censored/count], and
> a standard OLS approach would [violate assumptions]. Because our
> models involve [nonlinear specifications], we also report
> [marginal effects] to facilitate substantive interpretation."

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | 通用型——所有实证论文都需要模型辩护 |
| **理论类型** | 持续时间模型、计数模型、选择模型、面板模型、工具变量 |
| **前提条件** | 必须论证模型假设与数据特征的匹配；不能只引用 precedent |
| **风险** | 复杂模型若无充分辩护，会被质疑为炫技；简单模型若无辩护，会被质疑为粗糙 |

## 关键技巧

模型选择的核心是展示**数据生成过程的理解**：

| 弱表达 | 强表达 |
|--------|--------|
| "We use OLS regression" | "We use OLS with firm and year fixed effects to control for unobserved time-invariant heterogeneity and common macroeconomic shocks" |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 先例驱动 | "Following Smith (2010), we use Model X" | 必须独立论证为什么 Model X 适合你的数据 |
| 模型堆砌 | 同时报告 5-6 种模型结果 | 主分析模型只有一个；其他模型放入稳健性检验 |
| 忽视假设 | 不说清模型假设 | 明确说明关键假设及检验方法 |

## 相关语料

- 配合 `methods-narrative/endogeneity-defense.md` 使用：模型选择常服务于内生性处理
- 配合 `results-exposition/coefficient-to-substantive.md` 使用：非线性模型需要特别解释系数
- 配合 `results-exposition/interaction-marginal-effects.md` 使用：交互项模型需报告边际效应

## 验证状态
- **跨论文复现**: ✓✓ ROBUST（所有 28 篇 MVP30 论文都有模型选择段落）
- **来源论文**: 多篇 × 28
- **生成力**: ✓ GENERATIVE
- **排他性**: 通用
- **期刊限制**: 无限制
- **收录状态**: ⭐ PREMIUM
