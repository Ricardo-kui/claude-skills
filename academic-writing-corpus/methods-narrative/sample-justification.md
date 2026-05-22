# Sample Justification Narrative

## 功能定义
为样本选择提供理论和方法论辩护，展示研究者对内部效度、外部效度和数据可及性的综合考虑——不仅是"用了什么数据"，而是"为什么这个数据最适合回答研究问题"。

## 句法模板

**模板 A（行业聚焦型）**：
```
We focus on the [industry] for several reasons. First, examining
[phenomenon] in one industry eliminates confounding from extraneous
industry-specific effects and enhances internal validity. In addition,
the [industry] is a salient one because of the comprehensiveness of
the data available; [event] are well documented in this industry.
For these reasons, the [industry] has been the context of other studies
in the [topic] area (e.g., [Citations]).
```

**模板 B（多数据源整合型）**：
```
We leveraged [N] data sources to test our hypotheses. First, we
obtained data on [phenomenon] via [data source 1]. Second, we
collected [variable] from [data source 2]. Third, we gathered
[variable] from [data source 3]. The intersection of these data sets
resulted in a sample of [N] [units] across [time period].
```

**模板 C（自然实验型）**：
```
We tested our hypotheses using a natural experiment derived from real
events... This assignment process by naturally occurring events is
called "as-if randomization" ([Citation]). [Event] created variation
in [IV] that is exogenous to [DV], allowing us to make stronger causal
inferences than would be possible with standard cross-sectional designs.
```

**模板 D（漏斗叙事型）**：
```
Our sample period covers [start year] to [end year]. We began with
[initial population] and applied the following inclusion criteria:
[Criterion 1], [Criterion 2], and [Criterion 3]. The intersection
of these data sets resulted in a sample of [N] [units] across
[time period], with [observation count] firm-year observations.
```

## 例句（来自 MVP30）

**来源**：Does it Pay to Recall your Product Early? — Eilert et al., 2017 (JM)

> "We focus on the automotive industry for several reasons. First,
> examining recall timing in one industry eliminates confounding from
> extraneous industry-specific effects and enhances internal validity.
> In addition, the automotive industry is a salient one because of the
> comprehensiveness of the data available; the opening of an investigation
> and the announcement of a recall are well documented in this industry.
> For these reasons, the automotive industry has been the context of
> other studies in the recall area."

**来源**：CEO Stock Ownership, Recall Timing, and Stock Market Penalties — Darby et al.

> "We leveraged six data sources to test our hypotheses. First, we
> obtained data on medical device recalls via a Freedom of Information
> Act (FOIA) request to the FDA."

**来源**：On the Tip of the Brain — Paruchuri et al.

> "We tested our hypotheses using a natural experiment derived from real
events... This assignment process by naturally occurring events is called
> 'as-if randomization.'"

**改写模板**：
> "We focus on the [industry/context] for several reasons. First,
> examining [phenomenon] in one [industry/context] eliminates confounding
> from extraneous [context]-specific effects and enhances internal validity.
> In addition, the [industry] is a salient one because of the
> comprehensiveness of the data available. For these reasons, the
> [industry] has been the context of other studies in the [topic] area."

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | 通用型——所有期刊都需要样本辩护 |
| **理论类型** | 内部效度优先型（单行业）、外部效度优先型（跨行业）、因果识别型（自然实验） |
| **前提条件** | 必须同时回答"为什么这个样本"和"为什么排除其他样本" |
| **风险** | 单行业样本会被质疑外部效度；必须在讨论部分回应 |

## 关键技巧

最有效的样本辩护同时展示**效度权衡**：

| 弱表达 | 强表达 |
|--------|--------|
| "We use data from X industry" | "We focus on X industry because it eliminates confounding from industry-specific effects while providing comprehensive data on [phenomenon]" |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 数据可得性辩护 | "We use this data because it was available" | 必须论证数据的可得性如何服务于研究问题，而非仅仅因为方便 |
| 无排除标准 | 只讲包含标准，不讲排除标准 | 明确说明排除哪些样本及原因 |
| 样本量炫耀 | 只强调 N 很大 | 强调 N 与理论要求的匹配度 |

## 相关语料

- 配合 `methods-narrative/model-selection.md` 使用：样本辩护后需接模型选择逻辑
- 配合 `methods-narrative/endogeneity-defense.md` 使用：样本选择常服务于内生性处理
- 配合 `discussion-moves/limitation-boundary-control.md` 使用：讨论部分回应对样本外部效度的质疑

## 验证状态
- **跨论文复现**: ✓✓ ROBUST（所有 28 篇 MVP30 论文都有样本辩护段落）
- **来源论文**: 多篇 × 28
- **生成力**: ✓ GENERATIVE
- **排他性**: 通用
- **期刊限制**: 无限制
- **收录状态**: ⭐ PREMIUM
