# Difference Comparison Hypothesis

## 功能定义
陈述两个或多个群体/条件/层次之间效应差异的假设——不是预测主效应方向，而是预测效应的相对大小或方向差异，适用于比较逻辑（A vs. B）驱动的研究。

## 句法模板

**模板 A（组间差异型）**：
```
[Theoretical argument for why Group A differs from Group B].
Specifically, [mechanism for Group A] vs. [mechanism for Group B].
Thus, we predict:
Hypothesis [N]: The effect of [X] on [Y] is [stronger/weaker/more
positive/more negative] for [Group A] than for [Group B].
```

**模板 B（层次差异型）**：
```
Building on [theory], we argue that [X] has [qualitatively different]
effects at different [levels/units] of analysis.
At the [micro] level, [X] [increases/decreases] [Y] because [mechanism].
At the [macro] level, [X] [increases/decreases] [Y] because [different
mechanism].
Hypothesis [N]: The relationship between [X] and [Y] differs across
[levels/units], such that [specific prediction].
```

**模板 C（差异反转型）**：
```
Whereas prior research has found that [X positively affects Y] in
[Context A], we argue that [X negatively affects Y] in [Context B]
because [theoretical mechanism].
Hypothesis [N]: The effect of [X] on [Y] is [positive/negative] in
[Context A] but [negative/positive] in [Context B].
```

## 例句（来自 MVP30）

**来源**：State Ownership and Firm Innovation — Zhou et al., 2017 (ASQ)

> "Compared with established SOEs, state start-ups are also less influenced by the legacy of a socialist imprint and bear fewer historical burdens... As a result, state start-ups suffer less from the dual agency problem and can use their resource input more efficiently to generate innovation:"
> **Hypothesis 4 (H4):** The moderating effect of state ownership on the relationship between R&D intensity and innovation output is less negative for start-up firms than for established SOEs.

**来源**：Those Closest Wield the Sharpest Knife — Keeves et al., 2017 (ASQ)

> "We theorize that ingratiation leads to resentment and social undermining when the target is a powerful CEO, but this process is contingent on the closeness of the relationship between the ingratiator and the CEO."
> **Hypothesis 3:** The positive relationship between ingratiation and social undermining is stronger when the ingratiator and the CEO have a close relationship.

**来源**：Do Political Ties Facilitate Operational Efficiency

> "We argue that the effect of political ties on operational efficiency is contingent on the type of political tie..."
> **Hypothesis 2:** The positive effect of political ties on operational efficiency is stronger for cultivated ties than for obligatory ties.

**改写模板**：
> "[Theoretical argument for why Group A differs from Group B].
> Specifically, [mechanism for Group A] vs. [mechanism for Group B].
> Thus, we predict:
> **Hypothesis [N]:** The effect of [X] on [Y] is [stronger/weaker]
> for [Group A] than for [Group B]."

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | ASQ, AMJ, SMJ — 适合比较逻辑驱动的论文 |
| **理论类型** | 组间比较、层次理论、制度逻辑、关系理论 |
| **前提条件** | 必须有理论论证为什么两组/两层效应不同；不能只是探索性比较 |
| **风险** | 差异比较容易被质疑为事后分组；分组标准必须在理论部分预先定义 |

## 关键技巧

差异比较假设的关键是展示**机制差异**而非仅统计差异：

| 弱表达 | 强表达 |
|--------|--------|
| "The effect is stronger for A than B" | "A suffers less from [negative mechanism] than B, thereby experiencing a stronger positive effect of X on Y" |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 无理论分组 | 先跑数据发现两组有差异，再编理由 | 分组标准和理论机制必须在假设前提出 |
| 差异方向不清 | "The effect differs between A and B" | 必须明确预测哪组更强 |
| 过度分组 | 同时比较 4-5 组 | 最多比较 2-3 组；过多组削弱理论焦点 |

## 相关语料

- 配合 `mechanisms/context-reversal.md` 使用：差异比较是情境反转的形式化表达
- 配合 `tensions/06-forward-vs-backward-looking.md` 使用：前瞻性 vs. 后瞻性比较
- 配合 `results-exposition/interaction-marginal-effects.md` 使用：结果部分展示组间斜率差异

## 验证状态
- **跨论文复现**: ✓ VERIFIED（Zhou et al. 2017; Keeves et al. 2017; Political ties paper）
- **来源论文**: Zhou et al. (ASQ) × 1; Keeves et al. (ASQ) × 1
- **生成力**: 待验证
- **排他性**: 中——适合比较型论文，不适用于纯主效应论文
- **期刊限制**: 无限制
- **收录状态**: 🔬 EXPERIMENTAL
