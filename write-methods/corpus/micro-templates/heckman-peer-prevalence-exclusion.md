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


### 选项 3：逐条四步辩护 + 双向相关实证校验（raithel2024 型）

[功能标签]: M8 — 逐条排除限制的效度论证，理论机制 + 两个方向的相关性证据并列呈现

[骨架]: "We identified [k] potential exclusion restrictions that have a bearing on [the selection process] but are unlikely to have a direct impact on [the outcome]. We use (1) [restriction_1]. [Institutional mechanism] should increase [the actor's] motivation and ability to [comply/report]... [Decision-makers on the outcome side], on the other hand, are less likely to be aware of [the restriction information]. The correlation of this exclusion restriction with the [selection indicator] is [r_high] (p=[p1]). However, [restatement of why no direct link] should not directly correlate with [the outcome]. The correlation of the exclusion restriction with [the outcome] is only [r_low] (p=[p2])."

[结构要点]: 每条限制四步——(a) 命名限制；(b) 机制论证它推动选择；(c) 机制论证它不触及结果（信息不可得/与当前决策无关）；(d) 报告与选择指标的高相关 + 与结果的零相关，两个数字都出现在正文

[原文锚点]: "The correlation of this exclusion restriction with the sample indicator is 0.478 (p=0.000). However, this ability and motivation to restore and share more recent data should not directly correlate with recall effectiveness. The correlation of the exclusion restriction with recall effectiveness is only 0.052 (p=0.451)."

[可迁移性]: 高 — 所有 Heckman/CEM/选择模型的排除限制辩护通用

[范式排他性]: 高 — 只服务于含排除限制的识别设计

[设计变体]: 相关性证据可换成辅助回归复验（Liu, Liu & Luo 2016 变体15 路径）；制度性限制（批次号/处理顺序）用"决策者不可见"论证替代相关数字

[区别于既有 heckman-peer-prevalence 模板]: 既有模板论证"同行 prevalence 为何有效"这一单条限制的理论依据；本模板是逐条限制的通用四步辩护结构，且把双向相关性数字写入正文作为实证校验

<!-- wb:raithel_2024_product_recall_effectiveness_and_consumers_part:m8_exclusion_restriction_empirical_validity_pair -->
<!-- wb-meta: gap=Incompleteness status=EMERGING -->


### 选项 4：双层同伴工具 + 部门多样性排除强化（mallapragada2025 型）

[功能标签]: 同一"同伴流行度"工具逻辑在两个分类粒度各取一个工具（窄行业 + 宽部门、剔除窄行业），排除性论证随粒度分层强化

[骨架]: "As instruments, we used [the behavior] in peer firms in the [n-digit industry] and [m-digit sector], excluding firms from the [n-digit industry]. These are relevant instruments because [firms look to each other when making the decision] (e.g., [citation]); these effects are also statistically significant in the first-stage model. However, such behavior is very unlikely to be directly correlated with [the focal outcome] but is most likely channeled only through the focal firm's [channel], thereby satisfying the exclusion restriction. This argument is stronger for peer firms in the [m-digit sector]; while they are related, they also operate in more diverse businesses, and their impact on [the outcome], if any, happens only through the focal firm's [channel]. As [the behavior] outside the focal industry but within the sector is less relevant to a focal firm's [behavior], our use of sector peers provides us with strong exogenous variation."

[可迁移性]: 高 — 任何同伴流行度 IV 设计；"部门多样性 → 直接渠道更不可达"是可移植的排除性强化论证
[范式排他性]: 低 — 排除性论证模板，与选择模型/控制函数/2SRI 均兼容
[与选项 1/3 区分]: 选项 1 三段式纯理论论证、选项 3 四步辩护加实证校验对；本选项的独特维度是工具对的双粒度结构加随粒度递进的排除性强化论证，可叠加在选项 1 或 3 之上

<!-- wb:mallapragada_2025_to_acquire_or_to_ally_the_impact_of_strate:m8_dualgranularity_peer_exclusion_strengthening -->
<!-- wb-meta: gap=Incompleteness status=EMERGING -->
