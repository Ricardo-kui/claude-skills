# Problemistic Search and Threat Rigidity

## 功能定义
用"问题导向搜索"（problemistic search）和"威胁刚性"（threat rigidity）两个经典行为理论概念来解释为什么组织在面临严重问题时反而反应迟缓——搜索行为消耗认知资源，威胁感知引发防御性固化。

## 句法模板

**模板 A（问题触发搜索型）**：
```
[X] will trigger "problemistic" or problem-oriented investigations in
[actors]. However, problemistic search behavior is myopic in that the
investigation will rely on traditional routines and, thus, may not
quickly arrive at a solution ([Cyert & March 1992]; [Argote & Greve 2007]).
Therefore, although [event] might trigger the search for a solution,
[actor]'s ability to provide a quick response to [X] is especially limited.
```

**模板 B（威胁刚性与责任规避型）**：
```
When [event occurs], [actor] also strives to determine who is to be held
accountable for the failure ([Sitkin 1992]). Assessing accountability
becomes more consequential for [X], especially because of the desire to
prevent such problems in the future. However, the desire to avoid
responsibility might lower motivation to share information and pursue a
solution among those likely to be held accountable ([Madsen & Desai 2010]).
The ensuing response would be similar to that predicted by the
"threat-rigidity" hypothesis ([Staw, Sandelands, & Dutton 1981]),
in which the key concern may not be solving the problem but rather
protecting the interest of the dominant coalition by controlling decisions.
```

**模板 C（利益相关者惩罚型）**：
```
Research has also shown that stakeholders are more likely to punish severe
[events] than less severe [events] ([Citations]). Furthermore, [negative
consequences] are more likely in cases of [X], and therefore, the stakes
are higher. Thus, as [X] increases, [actors] will also be motivated to
avoid external accountability and delay [response]. The benefit of delaying
is that [actor] could avoid [negative outcome] altogether if [condition].
```

## 例句（来自 MVP30）

**来源**：Does it Pay to Recall your Product Early? — Eilert et al., 2017 (JM)

> "Severe problems will trigger 'problemistic' or problem-oriented
> investigations in firms. However, problemistic search behavior is myopic
> in that the investigation will rely on traditional routines and, thus,
> may not quickly arrive at a solution."

> "When a product defect is suspected, apart from searching for a solution,
> the firm also strives to determine who is to be held accountable for
> the failure. Assessing accountability becomes more consequential for
> severe problems... the desire to avoid responsibility might lower
> motivation to share information... The ensuing response would be similar
> to that predicted by the 'threat-rigidity' hypothesis."

> "Research has also shown that stakeholders are more likely to punish
> severe recalls than less severe recalls... lawsuits are more likely
> in cases of severe defects, and therefore, the stakes are higher.
> Thus, as problem severity increases, firms will also be motivated to
> avoid external accountability and delay the recall."

**改写模板**：
> "[X] will trigger 'problemistic' or problem-oriented investigations in
> [actors]. However, problemistic search behavior is myopic in that the
> investigation will rely on traditional routines and, thus, may not
> quickly arrive at a solution. Therefore, although [event] might trigger
> the search for a solution, [actor]'s ability to provide a quick response
> to [X] is especially limited."

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | JM, JAP, ASQ — 适合行为理论驱动的论文 |
| **理论类型** | 行为理论（Cyert & March）、威胁刚性理论、组织决策、危机管理 |
| **前提条件** | 现象必须涉及组织在压力/威胁下的非最优反应；需要引用经典文献 |
| **风险** | 若问题并不严重，problemistic search 不适用；过度使用威胁刚性会显得理论懒惰 |

## 关键技巧

让机制"可想象"的关键是展示**认知过程**：

| 弱表达 | 强表达 |
|--------|--------|
| "Firms search for solutions when facing problems" | "Firms engage in problemistic search, but this search is myopic—it relies on traditional routines and may not quickly arrive at a solution" |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 搜索无代价 | 只说" firms search for solutions"不讨论搜索的副作用 | 必须强调问题导向搜索的近视性和时间消耗 |
| 刚性泛化 | 任何迟缓反应都归因于威胁刚性 | 威胁刚性只适用于威胁情境；机会情境应使用其他理论 |
| 缺乏微观基础 | 只讲组织层面，不讲个体决策者的心理 | 用 Madsen & Desai (2010) 的个体责任规避机制连接微观与宏观 |

## 相关语料

- 配合 `mechanisms/dual-path-ability-motivation.md` 使用：problemistic search 解释 ability 下降，threat rigidity 解释 motivation 下降
- 配合 `hooks/10-practical-puzzle.md` 使用：实践难题常由 problemistic search 和 threat rigidity 导致
- 配合 `discussion-moves/reversal-silver-lining.md` 使用：讨论部分可反转——延迟虽有害，但体现了组织的审慎搜索

## 验证状态
- **跨论文复现**: ⚠️ SINGLE-INSTANCE（仅 Eilert et al. 2017 完整使用双机制）
- **来源论文**: Eilert et al. (JM) × 1
- **生成力**: 待验证
- **排他性**: 高——仅适用于威胁/危机情境下的组织反应迟缓
- **期刊限制**: JM 偏好消费者行为；ASQ 偏好组织决策理论
- **收录状态**: 🔬 EXPERIMENTAL
