---
category: identification-exogeneity
description: 用行为者决策领域之外的替代因变量进行 falsification 检验，并讨论主效应与替代结果之间的替代/转换关系。
function: 可信性——通过“该影响只在理论预期领域内出现”来强化因果识别
slots: M8, M10
source_exemplar: "chung_low_rust_2022_jams (Journal of the Academy of Marketing Science): accrual earnings management as falsification DV outside CMO's domain; substitution discussed"
created: 2026-07-08
updated: 2026-07-08
---

# 替代 DV Falsification（Alternative-DV Falsification）

## 核心原则

Falsification 检验通过替换因变量来验证理论的边界。当理论预测某个影响只在特定行为者/决策领域内发生时，可以找一个**该行为者无法直接影响、但机制上相关的替代结果**。如果核心交互项在替代 DV 上不显著（或方向/模式不同），则支持主效应不是由泛泛的遗漏变量或共同趋势驱动。

## 标准句式

### 选项 1：总起段

> An alternative way to establish causality is to provide a falsification test in which we examine how [alternative DV]—an outcome that is outside the decision-making domain of [actor]—is affected by [focal predictor / interaction]. If our theory is correct, [focal predictor / interaction] should [not significantly predict / have a different effect on] [alternative DV].

### 选项 2：明确替代 DV 与主 DV 的关系

> We use the same specification as in Table [reference], except that we replace [main DV] with [alternative DV], a measure of [construct] ([citation]). Although [alternative DV] is conceptually related to [main DV] as both reflect [broad phenomenon], it is not under the direct control of [actor] and therefore should not respond to [actor]-related interactions in the same way.

### 选项 3：讨论替代/转换

> The insignificant effect on [alternative DV] for the [actor]-related interactions is consistent with our interpretation that [actor]’s influence is specific to [main DV]. At the same time, the significant effect of [other predictor] on [alternative DV] suggests that when [actor] curbs [main DV], decision makers may substitute toward [alternative DV] to achieve the same objective ([citation]).

## 占位符清单

| 占位符 | 含义 | 示例 |
|--------|------|------|
| `[main DV]` | 主因变量 | myopic marketing management (MMM) |
| `[alternative DV]` | 替代因变量 | discretionary accruals / accrual earnings management |
| `[actor]` | 理论边界内的行为者 | CMO |
| `[focal predictor / interaction]` | 待检验的预测变量或交互项 | CEO confidence × CMO confidence |
| `[broad phenomenon]` | 两个 DV 共同反映的广义现象 | earnings management |
| `[construct]` | 替代 DV 测量的构念 | accrual-based earnings management |

## 设计变体

### 变体 A：行为者领域外（actor-domain falsification）

> 核心逻辑：若 X→Y 通过行为者 A 的作用渠道，则当 Y' 不在 A 的控制范围内时，X→Y' 不应显著。

示例：CMO 影响营销预算，但不影响应计盈余管理；因此 CMO-related 交互项对 AEM 应不显著。

### 变体 B：时间维度 falsification（lead-lag）

> 核心逻辑：若 X 确实导致 Y，则 X 不应显著预测 Y 的过去值。

示例：用未来或过去的 Y 替换当前 Y，检验反向因果。

### 变体 C：地理/制度边界 falsification

> 核心逻辑：若机制只在特定制度边界内成立，则替换为边界外的样本时效应应消失。

示例：某政策只在 A 国实施，B 国为安慰剂。

## 与安慰剂检验的区别

| 类型 | 替换对象 | 目的 |
|------|---------|------|
| 替代 DV falsification | 因变量 | 验证效应是否局限于理论预测的决策领域 |
| 安慰剂处理 falsification | 处理变量/样本 | 验证效应不是由随机因素或共同趋势驱动 |
| 时间 falsification | 因变量的时间 lead/lag | 验证时序因果方向 |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 替代 DV 与主 DV 完全无关 | 无法说明为什么应该看到 null | 选择理论上相关但行为者控制范围不同的 DV |
| 替代 DV 显著就说主效应不稳健 | 可能恰好反映替代机制 | 将替代结果解释为机制补充（substitution）而非证伪 |
| 不解释为什么替代 DV 在行为者领域外 | 外生性论证不足 | 明确说明 [actor] 无法直接决定 [alternative DV] |
| 仅在 Results 中报告，Methods 不预告 | 显得事后补充 | 在 M8 或 M10 中预告 falsification 设计 |
