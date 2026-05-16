# Moderation-Weakening Hypothesis

## 功能定义
陈述一个调节变量如何削弱（weaken/attentuate/reduce）主效应关系，从而展示边界条件——核心效应在何种情境下会减弱甚至消失。

## 句法模板

**模板 A（标准削弱型）**：
```
[Theoretical argument for moderation direction].
Thus, we propose:
Hypothesis [N]: The [positive/negative] relationship between [X] and
[Y] will be [weaker/less positive/less negative] when [Moderator] is
[higher/lower].
```

**模板 B（边界缓冲型）**：
```
[Condition] should [reduce/mitigate/alleviate] the [negative/positive]
effect of [X] on [Y]. This is because [theoretical mechanism].
Formally:
Hypothesis [N]: The moderating effect of [Moderator] on the relationship
between [X] and [Y] is [positive/negative], such that the relationship
is [weaker/stronger] when [Moderator] is [high/low].
```

**模板 C（间接表达型）**：
```
We posit that [Moderator] will [weaken/dampen] the effect of [X] on
[Y]. First, [mechanism 1]. Second, [mechanism 2]. Therefore:
Hypothesis [N]: The effect of [X] on [Y] is less [positive/negative]
when [Moderator] is higher.
```

## 例句（来自 MVP30）

**来源**：Does it Pay to Recall your Product Early? (JM)

> "Overall, as brand reliability increases, the motivation and ability to hasten recalls for severe problems will increase. Thus, we expect:"
> **H₂:** The higher a brand's reliability, the weaker the relationship between problem severity and time to recall.

**来源**：State Ownership and Firm Innovation (ASQ)

> "We posit that institutional development will weaken the effect of state ownership on R&D input. First, the resource advantage of state ownership decreases with institutional development... Second, regulatory pressure is alleviated with institutional development... Therefore:"
> **Hypothesis 2 (H2):** The effect of state ownership on R&D input is less positive when institutional development is higher.

**来源**：How Shareholder Litigation Risk Influences Firm Orientation toward Stakeholders

> "We argue that stakeholder orientation is less positive when managers are protected from shareholder litigation risk because of state universal demand (UD) laws..."
> **Hypothesis 2:** The positive relationship between shareholder litigation risk and stakeholder orientation is weaker for firms incorporated in states with universal demand laws.

**改写模板**：
> "[Theoretical argument for why moderator weakens the relationship].
> Thus, we propose:
> **Hypothesis [N]:** The [positive/negative] relationship between [X]
> and [Y] will be [weaker] when [Moderator] is [higher/lower]."

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | 通用型——AMJ/SMJ/ASQ 都接受 |
| **理论类型** | 边界条件、情境理论、权变理论 |
| **前提条件** | 必须有明确理论论证为什么调节变量削弱主效应 |
| **风险** | "Weaker" 不等于 "disappear"；若预测逆转方向，应使用竞争假设而非削弱假设 |

## 关键技巧

削弱假设的论证关键是展示**力量的此消彼长**：

| 弱表达 | 强表达 |
|--------|--------|
| "M weakens the effect of X on Y" | "M reduces the resource advantage of X, thereby weakening its effect on Y" |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 削弱无机制 | "M weakens the effect"但不解释如何削弱 | 至少给出两个理论机制 |
| 与主效应矛盾 | 调节论证与主效应逻辑冲突 | 调节机制必须是主效应机制的延伸 |
| 事后合理化 | 先发现交互项不显著，再编造削弱故事 | 调节假设必须在理论部分预先提出 |

## 相关语料

- 配合 `mechanisms/opposing-forces.md` 使用：削弱假设常由对立力量理论推导
- 配合 `results-exposition/interaction-marginal-effects.md` 使用：结果部分用边际效应展示削弱程度
- 配合 `tensions/07-same-policy-opposite-effects.md` 使用：削弱假设是同一政策不同效应的形式化表达

## 验证状态
- **跨论文复现**: ✓ VERIFIED（Eilert et al. 2017; Zhou et al. 2017; Han et al.）
- **来源论文**: Eilert et al. (JM) × 1; Zhou et al. (ASQ) × 1; Han et al. × 1
- **生成力**: ✓ GENERATIVE
- **排他性**: 低——通用型调节假设
- **期刊限制**: 无限制
- **收录状态**: ✓ STANDARD
