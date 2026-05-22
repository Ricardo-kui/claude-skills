# Dual-Path (Ability-Motivation) Mechanism

## 功能定义
将主效应分解为两条并行或互补的中介路径——"能力路径"与"动机路径"——从而展示现象作用的完整心理或行为机制，避免单一路径的理论简化。

## 句法模板

**模板 A（理论奠基型）**：
```
Prior research has shown that these response dimensions are a function
of the motivation and ability of the firm to respond to the external
event ([Citation]). We argue that [X] affects [Y] through its impact
on the ability and motivation of [actors] to respond.
```

**模板 B（机制分解型）**：
```
The ability of [actor] to [respond/act] is closely linked to whether
[actor] can [identify a solution/access resources]. In this regard,
[X] will trigger [cognitive search behavior]. However, [this search
behavior] is myopic in that [it relies on traditional routines and
may not quickly arrive at a solution]. Therefore, although [event]
might trigger the search for a solution, [actor]'s ability to provide
a quick response to [X] is especially limited.

When [event occurs], apart from searching for a solution, [actor] also
strives to [determine accountability]. Assessing accountability becomes
more consequential for [X], especially because of the desire to prevent
such problems in the future. However, [accountability process] might
lower motivation to share information and pursue a solution among those
likely to be held accountable. The ensuing response would be similar to
that predicted by the "threat-rigidity" hypothesis ([Staw et al., 1981]),
in which the key concern may not be solving the problem but rather
protecting the interest of the dominant coalition by controlling decisions.
```

**模板 C（表格化总结型）**：
```
[Table: Overview of Rationale for Hypotheses]
| Condition | Ability to [Act] | Motivation to [Act] | Net Effect on [Outcome] | Rationale |
|-----------|------------------|---------------------|------------------------|-----------|
| [X] (H1)  | Negative         | Negative            | Increase               | Triggers problemistic search; need to determine internal accountability |
| [X × Moderator] (H2) | Positive | Positive      | Decrease               | More likely to have systems in place to determine root cause |
```

## 例句（来自 MVP30）

**来源**：Does it Pay to Recall your Product Early? — Eilert et al., 2017 (JM)

> "We approach recall timing decisions from the vantage point of the
> behavioral theory of the firm. From this perspective, the ability and
> motivation of firms to respond to a defect investigation in light of
> these multiple and often conflicting goals are key determinants of
> their actions."

> "We argue that the more severe the defect, the greater the attention
> to the investigation because a recall involving a severe defect is
> costlier than a recall involving less severe problems. However,
> although problem severity triggers the search for a solution, it does
> not necessarily lead to a quick response, because it reduces the
> ability and motivation of firms to respond."

> "The ability of the firm to provide a quick response is closely linked
> to whether the firm can identify a potential solution to fix the defect.
> In this regard, severe problems will trigger 'problemistic' or
> problem-oriented investigations in firms. However, problemistic search
> behavior is myopic in that the investigation will rely on traditional
> routines and, thus, may not quickly arrive at a solution."

**改写模板**：
> "We approach [phenomenon] from the vantage point of [theory]. From
> this perspective, the ability and motivation of [actors] to respond
> to [event] in light of these multiple and often conflicting goals
> are key determinants of their actions. We argue that [X] affects
> [Y] through its impact on the ability and motivation of [actors]
> to respond."

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | JM, JAP, AMJ — 适合机制分解型论文；SMJ 偏好组织层面能力-动机 |
| **理论类型** | 中介效应论文、行为理论、威胁刚性理论、问题导向搜索 |
| **前提条件** | 两条路径必须有明确的理论区分；引用 Chen & Hambrick (1995) 或 Staw et al. (1981) 等经典文献支撑 |
| **风险** | 若两条路径概念上过于接近，会被质疑为事后拆分；表格化总结能增强说服力 |

## 关键技巧

最有效的双路径论证让读者能在脑中画出两条并行的因果链：

| 弱表达 | 强表达 |
|--------|--------|
| "X affects Y through ability and motivation" | "X affects Y through two distinct routes: by enhancing ability (which enables Y) and by reducing motivation (which energizes/deters Y)" |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 路径概念重叠 | ability 和 motivation 在测量上高度相关 | 确保两条路径的理论来源不同 |
| 单一路径足够 | 实际上一条路径就能解释全部方差 | 先论证为什么单一路径是理论简化 |
| 事后合理化 | 先跑回归发现两个中介都显著，再编故事 | 双路径必须在理论部分预先提出，并用表格总结 |

## 相关语料

- 配合 `hypotheses/mediation-chain.md` 使用：正式假设中需分别陈述两条中介路径
- 配合 `results-exposition/coefficient-to-substantive.md` 使用：结果部分需分别量化两条路径的间接效应
- 配合 `tensions/09-resource-acquisition-vs-utilization.md` 使用：能力-动机与资源获取-利用张力同源

## 验证状态
- **跨论文复现**: ✓ VERIFIED（Eilert et al. 2017; Shi et al. 2021 使用 motivation/opportunity/ability 三条件）
- **来源论文**: Eilert et al. (JM) × 1; Shi et al. (AMJ) × 1
- **生成力**: 待验证
- **排他性**: 中——适合中介分解，但不适用于简单主效应
- **期刊限制**: JM/JAP 偏好微观基础；SMJ 偏好组织层面
- **收录状态**: 🔬 EXPERIMENTAL
