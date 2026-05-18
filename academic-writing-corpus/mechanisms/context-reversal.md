# Context Reversal Mechanism

## 功能定义
展示一个变量在某种情境下产生正向效应，但在另一种情境下产生负向效应（或效应反转），从而论证"情境反转"是理解复杂组织现象的关键——同一因素不是好或坏，而是取决于它发生在什么情境中。

## 句法模板

**模板 A（两阶段反转型）**：
```
When [X] increases from zero to [low level], the [positive mechanism]
becomes more salient yet the [negative mechanism] is relatively minor.
As [X] moves from [low] to [high] levels, however, the additional
[positive effect] increases rather incrementally, but the [negative
mechanism] becomes evident. In such situations, an increase in [X]
triggers more [negative outcomes]. Thus we predict that a [moderate]
level of [X] is most beneficial to [Y].
```

**模板 B（逻辑对立型）**：
```
The [Theory A] view emphasizes the [positive aspect] brought by [X].
The [Theory B] view highlights the [negative aspect] caused by [X].
Because both views offer valid arguments, we need to consider both
when examining the overall effect of [X] on [Y].
```

**模板 C（边界条件反转型）**：
```
Under [Condition A], [X] enhances [Y] because [positive mechanism].
Under [Condition B], [X] diminishes [Y] because [negative mechanism].
The reversal occurs because [theoretical explanation for why the
mechanism switches].
```

## 例句（来自 MVP30）

**来源**：State Ownership and Firm Innovation — Zhou et al., 2017 (ASQ)

> "When state ownership increases from zero to minority levels, the
> institutional effect becomes more salient yet the efficiency problem
> is relatively minor... As state ownership moves from minority to
> majority levels, however, the additional resource allocation advantages
> increase rather incrementally, but the decision-making power shifts to
> the managers designated by government officials. Accordingly, the dual
> agency problem of SOEs becomes evident... Thus we predict that a
> minority level of state ownership is most beneficial to innovation."

**来源**：Two Sides of the Same Coin — Pontikes, 2012 (ASQ)

> "We theorize that market categories are two-sided: while they confer
> legitimacy that enables organizations to access resources, they also
> impose constraints that can stifle innovation."

**改写模板**：
> "When [X] increases from zero to [low level], the [positive mechanism]
> becomes more salient yet the [negative mechanism] is relatively minor.
> As [X] moves from [low] to [high] levels, however, the additional
> [positive effect] increases rather incrementally, but the [negative
> mechanism] becomes evident. Thus we predict that a [moderate] level
> of [X] is most beneficial to [Y]."

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | ASQ, AMJ — 适合制度理论与效率理论冲突的论文 |
| **理论类型** | 制度逻辑整合、代理理论、组织经济学、类别理论 |
| **前提条件** | 必须有两种对立理论各自成立的条件区间；不能只描述反转而无机制解释 |
| **风险** | 若反转点不可识别，会被质疑为事后合理化；必须有理论预测的拐点 |

## 关键技巧

反转机制的核心是展示**力量的此消彼长**：

| 弱表达 | 强表达 |
|--------|--------|
| "X has both positive and negative effects" | "The positive effect increases incrementally, but the negative effect becomes dominant beyond a threshold" |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 反转无拐点 | "有时正有时负"但不说清何时转换 | 明确给出理论预测的拐点或边界条件 |
| 单理论解释 | 用一个理论解释正负两种效应 | 反转必须由两个不同理论解释，否则不是真正的反转 |
| U型偷懒 | 任何非线性都预测倒U | 必须有理论论证为什么两端都差而中间最好 |

## 相关语料

- 配合 `mechanisms/inverted-u-mechanism.md` 使用：情境反转常表现为倒U型关系
- 配合 `hypotheses/inverted-u-hypothesis.md` 使用：正式假设陈述倒U型预测
- 配合 `tensions/10-constraint-vs-freedom.md` 使用：类别约束与资源获取的张力同源

## 验证状态
- **跨论文复现**: ✓ VERIFIED（Zhou et al. 2017; Pontikes 2012）
- **来源论文**: Zhou et al. (ASQ) × 1; Pontikes (ASQ) × 1
- **生成力**: 待验证
- **排他性**: 中——适合制度复杂性和组织变革论文
- **期刊限制**: ASQ 极度适合；AMJ 适合；SMJ 可用但需强调绩效含义
- **收录状态**: 🔬 EXPERIMENTAL
