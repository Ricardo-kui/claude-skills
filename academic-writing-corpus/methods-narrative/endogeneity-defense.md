# Endogeneity Defense Narrative

## 功能定义
系统论证研究如何处理潜在的内生性问题（遗漏变量、反向因果、测量误差），展示研究者对因果推断威胁的清醒认识和应对能力——这是顶级期刊 Methods 部分的必备段落。

## 句法模板

**模板 A（一般性声明型）**：
```
We recognize that [IV] may be endogenous to [DV] because of
[specific endogeneity concern: omitted variables / reverse causality /
measurement error]. To address this concern, we [method].
```

**模板 B（控制函数法）**：
```
We account for this endogeneity using the control function approach.
Specifically, we first regress [endogenous variable] on [instrument(s)]
and [controls] to obtain the residual, which captures the unobserved
factors affecting [endogenous variable]. We then include this residual
in the main equation to control for endogeneity.
```

**模板 C（自然实验/外生冲击型）**：
```
We ruled out many potential sources of endogeneity by tracking the most
accurate [event/disclosure] dates for the [incidents]. [Specific method:
as-if randomization / exogenous shock / regulatory change] creates
variation in [IV] that is plausibly exogenous to [DV].
```

**模板 D（匹配/CEM型）**：
```
To address potential selection bias, we use [coarsened exact matching
(CEM) / propensity score matching (PSM)] to create a matched sample
in which [treatment and control groups] are balanced on [observed
covariates]. This ensures that our estimates are not driven by
[pre-existing differences between groups].
```

## 例句（来自 MVP30）

**来源**：Does it Pay to Recall your Product Early? — Eilert et al., 2017 (JM)

> "We account for this endogeneity using the control function approach."

**来源**：Public Enemies — Han et al.

> "We ruled out many potential sources of endogeneity by tracking the
> most accurate disclosure dates for the breach incidents."

**来源**：CEO Regulatory Focus and Myopic Marketing Management

> "To address potential reverse causality, we [method] and found that
> [finding]."

**来源**：CEO Stock Ownership, Recall Timing, and Stock Market Penalties — Darby et al.

> "To address potential endogeneity of CEO ownership, we use coarsened
> exact matching (CEM) to create a matched sample..."

**改写模板**：
> "We recognize that [IV] may be endogenous to [DV] because of
> [specific concern]. To address this concern, we [method].
> Specifically, we [detailed procedure]. This approach ensures that
> our estimates capture the [causal] effect of [IV] on [DV] rather
> than [alternative explanation]."

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | ASQ, SMJ, AMJ — 所有顶级期刊都重视内生性处理 |
| **理论类型** | 因果推断、自然实验、工具变量、匹配方法 |
| **前提条件** | 必须明确识别内生性的具体来源；不能泛泛而谈 |
| **风险** | 内生性处理不当是 desk rejection 的首要原因；必须在主分析和稳健性检验中都处理 |

## 关键技巧

内生性辩护的核心是展示**对因果推断威胁的系统性识别**：

| 弱表达 | 强表达 |
|--------|--------|
| "We address endogeneity using instrumental variables" | "We address potential reverse causality by using lagged IVs and an instrumental variable approach with [specific instrument], which satisfies the exclusion restriction because [justification]" |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 泛泛而谈 | "We address endogeneity concerns"但不具体说明 | 必须明确指出内生性来源和具体处理方法 |
| 工具变量弱 | F-statistic < 10 但不报告或忽视 | 必须报告第一阶段 F 统计量；弱工具变量需使用有限信息方法 |
| 只做一种检验 | 只用 PSM 或只用 IV | 至少使用两种互补方法交叉验证 |

## 相关语料

- 配合 `methods-narrative/instrumental-variable.md` 使用：IV 是内生性处理的核心方法
- 配合 `methods-narrative/robustness-threat-test.md` 使用：内生性检验是稳健性检验的核心类别
- 配合 `results-exposition/null-results.md` 使用：内生性处理后的不显著结果需要特别解释

## 验证状态
- **跨论文复现**: ✓✓ ROBUST（所有 28 篇 MVP30 论文都有内生性处理段落）
- **来源论文**: 多篇 × 28
- **生成力**: ✓ GENERATIVE
- **排他性**: 通用
- **期刊限制**: 无限制
- **收录状态**: ⭐ PREMIUM
