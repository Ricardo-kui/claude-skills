---
category: identification-exogeneity
description: Heckman 选择模型中，用同行/同伴 prevalence 作为排他性限制变量，并说明跨行业 segments 的加权计算。
function: 可信性——为 Heckman 选择模型提供理论驱动的外生识别变量
slots: M7, M8
source_exemplar: "chung_low_rust_2022_jams (Journal of the Academy of Marketing Science): Peer CMO presence as Heckman exclusion restriction, weighted across firm industry segments"
created: 2026-07-08
updated: 2026-07-08
---

# Heckman 选择模型：同行 Prevalence 排他性限制

## 核心原则

当样本仅包含某个职位/角色存在的观测值时（例如仅分析有 CMO 的公司），可能存在非随机选择偏差。Heckman 选择模型需要第一阶段有一个**排他性限制变量**：它影响是否被选中（selection equation），但直接影响第二阶段结果。同行 prevalence 是一种经典且可迁移的排除限制——同行行为通过规范压力/模仿机制影响焦点组织是否采用某角色/结构，但不太可能直接影响焦点组织的具体决策结果。

## 第一阶段选择方程

### 选项 1：标准 Probit/Logit 选择方程

> In the first stage, we model the probability that [focal unit] has [role/structure] as a function of the exclusion restriction and the same set of control variables used in the second stage:
>
> ```
> Prob([Role Presence] = 1) = F(γ₀ + γ₁[Peer Prevalence] + Controls + μ)
> ```
>
> where [Peer Prevalence] is the proportion of peer [units] in the same [industry/peer group] that have [role/structure].

### 选项 2：强调模仿/制度同形机制

> Firms operating in similar industries face comparable market conditions and thus have similar needs for [role] in the top management team ([citation]). Therefore, the prevalence of [role] among peer firms should influence whether a focal firm also adopts [role], but it should not directly affect the focal firm’s [outcome] once [role] presence is accounted for.

## 排他性限制论证

### 选项 1：三段式排除限制论证

> A valid exclusion restriction must influence selection into the sample but have no direct effect on the outcome ([citation]). [Peer Prevalence] satisfies this condition for three reasons. First, peer [units] operate in similar institutional environments, so their adoption of [role] predicts the focal firm’s adoption through mimetic or normative pressures ([citation]). Second, we define peers across the multiple industry segments that the focal firm operates in, rather than only its primary segment. This expands peers to include peripheral rivals whose actions are less likely to directly impact the focal firm’s [outcome]. Third, the large number of peer firms (on average, [N] per focal firm) attenuates concerns that any single peer could simultaneously influence both [role adoption] and [outcome].

### 选项 2：简洁版

> Following [citation], we use the proportion of peer firms with [role] as the exclusion restriction. The prevalence of [role] among industry peers should affect whether the focal firm has [role], because firms in similar industries tend to imitate each other ([citation]). However, this peer prevalence is unlikely to directly influence the focal firm’s [outcome], especially because peers are defined across multiple industry segments and thus include many peripheral rather than direct rivals.

## 跨 Segments 加权

### 选项 1：详细说明

> We obtain the primary and secondary [industry segments] in which each focal firm operates from [data source: e.g., Compustat segment files]. We focus on industries defined at the [two-digit SIC / NAICS] level. For each segment, we calculate the proportion of peer firms (excluding the focal firm) that have [role]. When a firm operates in multiple segments, we compute a weighted average prevalence across segments, using the number of peer firms in each segment as weights. Because firms operate in multiple segments and these segments tend to change over time within a firm, [Peer Prevalence] varies both across firms and over time.

### 选项 2：简化版

> Peer prevalence is calculated as the segment-weighted proportion of peer firms with [role], where weights reflect the number of peers in each of the focal firm’s reported industry segments.

## 第二阶段结果方程

> In the second stage, we estimate the structural equation for [outcome] using observations with [role] present, while including the inverse Mills ratio (λ) derived from the first stage to correct for selection bias.

## 占位符清单

| 占位符 | 含义 | 示例 |
|--------|------|------|
| `[role/structure]` | 选择样本中的关键角色/结构 | CMO presence |
| `[Peer Prevalence]` | 排他性限制变量名 | Peer CMO presence |
| `[industry/peer group]` | 同伴定义 | two-digit SIC industries |
| `[data source]` | 行业 segments 来源 | Compustat segment files |
| `[N]` | 平均同伴数 | 67 |
| `[outcome]` | 第二阶段 DV | myopic marketing management |

## 可迁移场景

| 研究情境 | 选择变量 | 排他性限制 |
|---------|---------|-----------|
| 仅分析有 CMO 的公司 | CMO presence | Peer CMO prevalence |
| 仅分析有董事会的子公司 | Board presence | Peer board prevalence |
| 仅分析进行并购的公司 | Acquisition dummy | Peer acquisition rate in same industry |
| 仅分析创新的公司 | Innovation adoption | Peer adoption rate in technology class |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| `We use peer prevalence as an instrument.` | 混淆 Heckman 排除限制与 IV 工具变量 | 明确说明这是 Heckman 选择模型的 exclusion restriction |
| 仅报告第一阶段显著，不解释为何满足排除限制 | 审稿人质疑外生性 | 提供三段式理论论证 |
| 同伴只按主行业定义 | 同伴可能是直接竞争对手，直接影响结果 | 按多 segments 定义并加权，扩大同伴池 |
| 第二阶段不报告 inverse Mills ratio / rho | 无法判断选择偏误大小 | 报告 rho 及其显著性 |
