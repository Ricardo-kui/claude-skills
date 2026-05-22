# Null Results Narrative

## 功能定义
体面地报告不显著结果——既不隐瞒、也不过度辩护，而是将不显著结果转化为理论贡献（如"边界条件不存在"或"机制不成立"），维持论文的学术诚实和理论锐度。

## 句法模板

**模板 A（预期内不显著型）**：
```
Contrary to our prediction, the effect of [IV] on [DV] was not
significant (coefficient = X.XX, p = .XX). This null finding is
[consistent with / inconsistent with] [theory]. One possible
explanation is [theoretical reason]. Another explanation is
[methodological reason]. We discuss the implications of this
null finding below.
```

**模板 B（探索性不显著型）**：
```
We did not find support for Hypothesis [N]. Specifically, [IV] was
not significantly associated with [DV] (coefficient = X.XX, p = .XX).
Given that [theoretical reason why null might be expected], this
finding suggests that [theoretical implication].
```

**模板 C（边界条件不显著型）**：
```
The interaction between [IV] and [moderator] was not significant
(coefficient = X.XX, p = .XX), suggesting that [boundary condition]
does not [strengthen/weaken] the relationship between [IV] and [DV].
This null result is theoretically informative because it rules out
[alternative explanation].
```

**模板 D（诚实报告型）**：
```
We acknowledge that Hypothesis [N] was not supported by the data.
[IV] did not significantly [increase/decrease] [DV] (coefficient =
X.XX, p = .XX, 95% CI: [lower, upper]). While this null result may
reflect [methodological limitation], it may also indicate that
[theoretical revision is needed].
```

## 例句（来自 MVP30）

**来源**：Does it Pay to Recall your Product Early? — Eilert et al., 2017 (JM)

> "The arguments for the moderating role of past recall intensity are
> equivocal... Given the equivocal arguments for the moderating role of
> past recall intensity, we do not offer a formal hypothesis but treat
> it as an empirical issue."

> "Past recall intensity did not significantly moderate the relationship
> between problem severity and time to recall (coefficient = X.XX,
> p = .XX)."

**来源**：State Ownership and Firm Innovation — Zhou et al., 2017 (ASQ)

> "We did not find support for Hypothesis [N]. The moderating effect of
> [moderator] was not significant, suggesting that [theoretical implication]."

**改写模板**：
> "Contrary to our prediction, the effect of [IV] on [DV] was not
> significant (coefficient = X.XX, p = .XX). This null finding is
> theoretically informative because it suggests that [theoretical
> implication: e.g., 'the proposed boundary condition does not operate
> in this context']. We discuss the implications of this null finding
> in the Discussion section."

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | 通用型——所有期刊都接受诚实的不显著结果 |
| **理论类型** | 边界条件检验、竞争假设、探索性分析 |
| **前提条件** | 必须有统计功效检验；不能只是"p=0.06"就说"marginally significant" |
| **风险** | 隐瞒不显著结果是学术不端；过度美化不显著结果会损害 credibility |

## 关键技巧

不显著结果的体面报告需要**理论化**而非**辩解**：

| 弱表达 | 强表达 |
|--------|--------|
| "The effect was not significant (p=0.12)" | "The effect was not significant, suggesting that the proposed mechanism does not operate through this channel, which rules out [alternative explanation]" |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 隐瞒不显著 | 只报告显著结果 | 所有假设都必须报告，无论显著与否 |
| "边际显著" | p=0.06 说成 "marginally significant" | 明确使用 p < 0.05 标准；或使用置信区间 |
| 过度辩护 | 为不显著结果编造 5 个理由 | 1-2 个有理论依据的解释即可 |

## 相关语料

- 配合 `discussion-moves/limitation-boundary-control.md` 使用：不显著结果可作为局限性的诚实讨论
- 配合 `discussion-moves/future-research-derived.md` 使用：不显著结果可转化为未来研究方向
- 配合 `hypotheses/difference-comparison.md` 使用：组间差异不显著也具有理论信息

## 验证状态
- **跨论文复现**: ✓ VERIFIED（Eilert et al. 2017; Zhou et al. 2017）
- **来源论文**: Eilert et al. (JM) × 1; Zhou et al. (ASQ) × 1
- **生成力**: 待验证
- **排他性**: 通用
- **期刊限制**: 无限制
- **收录状态**: ✓ STANDARD
