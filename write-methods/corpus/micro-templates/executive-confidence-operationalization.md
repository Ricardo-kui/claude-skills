---
category: variable-operationalization
description: 高管信心/过度自信的档案操作化——期权 moneyness、媒体描述、双代理收敛，以及构念形成窗与结果观察窗分离。
function: 对齐性——将心理学构念“信心/过度自信”转译为可重复计算的档案数据指标
slots: M2, M4, M8
source_exemplar: "chung_low_rust_2022_jams (JAMS): option moneyness; schumacher_keck_tang_2020_smj (SMJ): disjoint tenure windows + media/option dual proxies; kashmiri_nicol_arora_2017_jams (JAMS): four-indicator narcissism composite + succession exclusion + same-CEO/successor validation"
created: 2026-07-08
updated: 2026-08-03
---

# 高管信心操作化（Executive Confidence Operationalization）

## 核心原则

高管信心在档案研究中通常无法直接观测。顶刊营销/金融/管理文献最通行的代理指标是**基于期权 moneyness 的行为度量**：高管延迟行使已 vested 且深度实值期权，反映其对未来股价的乐观信念。该指标的优势在于：(1) 基于标准薪酬数据库（Execucomp）即可计算；(2) 已被大量研究交叉验证；(3) 可随时间变化，适用于面板数据。

## 标准操作化句式

### 选项 1：平均 moneyness（通用版）

> [Actor] confidence is measured as the average moneyness of the exercisable options held by the [actor] in [year t]. The average moneyness is defined as the ratio of the average value per option to the average strike price ([citations]).

### 选项 2：强调理论直觉

> Following [citation], we infer [actor] confidence from the tendency to hold exercisable options that are deep in the money. Confident [actors] expect the firm’s stock price to continue appreciating and therefore delay exercising vested options, even when doing so would reduce their exposure to idiosyncratic risk ([citation]). We operationalize this tendency as the average ratio of per-option value to strike price across all exercisable options held by the [actor] in [year t].

### 选项 3：简洁操作化 + 滞后声明

> [Actor] confidence is the average moneyness (average value per option divided by average strike price) of the [actor]’s exercisable options, measured with a one-year lag relative to the dependent variable to preserve temporal ordering and minimize reverse causality.

### 选项 4：构念形成窗与结果观察窗完全分离

> To reduce contamination between [stable actor trait] and the outcomes used to test its consequences, we use nonoverlapping windows. We construct the trait from observable behavior during the first [k] periods of each actor's tenure and estimate its relationship with outcomes only in subsequent periods.

### 选项 5：方法异质的双代理收敛

> We operationalize [confidence/overconfidence] with two proxies grounded in different data-generating processes: [public-description/text proxy] and [revealed-choice/portfolio proxy]. Convergent directional results reduce dependence on any one proxy, while we examine each proxy's distinct contamination channel separately.

**来源**: Schumacher, Keck, and Tang (2020), *Strategic Management Journal*（任期前三年形成媒体与期权代理，后续年份检验风险反应）。

**关键区别**: 这不是普通的一期滞后。普通滞后仍可能让 trait 测量与结果周期重叠；本变体把整个构念形成期与结果观察期切开，并使用两种不同痕迹系统做收敛验证。

### 选项 6：显著性—薪酬复合代理 + 继任者对照验证（narcissism 型）

> We construct [executive trait] from standardized indicators drawn from distinct observable traces: [visual self-prominence], [name prominence in organizational communications], [relative cash compensation], and [relative noncash compensation]. We average the indicators over [trait window] after excluding the succession year, when communication and compensation arrangements may be transitional. To examine whether the composite reflects the executive rather than a persistent firm attribute, we compare its within-executive stability over time with the correspondence between successive executives at the same firm. Higher within-executive stability and weak successor correspondence strengthen the trait interpretation, while not uniquely identifying the latent construct.

**来源**: Kashmiri, Nicol, and Arora (2017), *Journal of the Academy of Marketing Science*。

**使用条件**:
- 四个指标必须先标准化再合成；保留各指标的方向、缺失规则与权重。
- 视觉/传播 prominence 与相对薪酬来自不同痕迹，但都可能受企业传播政策、治理结构或绩效影响；“多指标”不等于“无污染”。
- 继任者对照是 construct-validity pattern，不是随机化。若 CEO 任期筛选要求其留任 5–7 年，需同时报告由此产生的 survivorship/tenure selection。
- succession year exclusion 应基于制度与测量理由，不能只因为该年结果不显著。

## 构造细节占位符

| 占位符 | 含义 | 示例 |
|--------|------|------|
| `[actor]` | 行为者 | CEO / CMO / CFO / TMT |
| `[year t]` | 测量时点 | fiscal year t |
| `[average value per option]` | 每份期权平均价值 | Execucomp item OPT_UNEX_EXER_EST_VALUE / OPT_UNEX_EXER_NUM |
| `[average strike price]` | 平均行权价 | 通常由 Compustat 股价与期权价值反推 |
| `[exercisable options]` | 已可行权期权 | 区分 exercisable vs. unexercisable；文献多用 exercisable |
| `[lag structure]` | 滞后处理 | lagged one year relative to DV |
| `[formation window]` | 构念形成期 | first 3 years of actor tenure |
| `[outcome window]` | 结果观察期 | years after the formation window |
| `[text proxy]` | 公开描述代理 | confidence-related media terms near actor name |
| `[choice proxy]` | 行为选择代理 | delayed exercise of deep-in-the-money vested options |
| `[visual self-prominence]` | 视觉显著性代理 | annual-report photograph size/composition |
| `[communication prominence]` | 传播显著性代理 | executive-name mentions normalized by document length |
| `[relative compensation]` | 相对地位/报酬代理 | executive pay divided by next-highest-paid executive pay |

## 何时使用 moneyness 而非其他代理

| 替代测量 | 适用情境 | 局限 |
|---------|---------|------|
| 期权 moneyness | 有大量高管薪酬面板数据；研究对象为 CEO/CMO/CFO | 假设高管风险厌恶且理性分散化；对非期权密集型样本不适用 |
| 文本情绪/语调 | 有 earnings call / 访谈 / 公开信文本 | 可能同时捕捉情绪、认知复杂度、印象管理 |
| 并购/投资过度自信指标 | 研究特定公司决策 | 决策结果可能是内生的，且样本选择性高 |
| 调查/心理测量 | 实验或小样本高管调查 | 外部效度和时间跨度受限 |

## 诚实边界

1. **不是直接测量过度自信**：期权 moneyness 反映的是“基于财富的信念”，与心理学意义上的过度自信有区别。应说明“we are not studying executive short-termism per se; rather, we examine how [DV] may be a by-product of executive confidence.”
2. **滞后理由必须写**：同期薪酬/期权价值可能受 DV 影响，因此所有 pay-related 变量应滞后。
3. **样本边界**：仅适用于授予大量期权的高管；若样本中某些高管无 exercisable options，需说明缺失值处理（排除 / 设零 / 替代指标）。
4. **双代理不是自动构念证明**：媒体代理可能含印象管理，期权代理可能含激励、税务或风险偏好。跨代理同向只能降低单一操作化依赖，不能证明二者只捕捉能力高估。
5. **分离窗口不是外生性**：早期任期的企业环境仍可能同时影响 trait proxy 与后续行为；需要固定效应、匹配或其他设计补强。
6. **稳定性对照不是构念纯度证明**：同一 CEO 跨期相关高于同一企业相邻 CEO，只能降低“纯企业属性”解释，不能排除传播团队、薪酬制度与 CEO—firm matching。

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| `CEO confidence is measured by stock option holdings.` | 混淆持仓数量与 moneyness | 明确使用 average value/strike price ratio |
| `Higher stock price means higher confidence.` | 混淆市场价格与高管信念 | moneyness 是“实值程度”而非绝对股价 |
| 未说明 exercisable vs. unexercisable | 不同行权状态反映不同信念结构 | 明确使用 exercisable options |
| 未报告滞后结构 | 反向因果风险 | 在 M4 中说明 `measured with a lag relative to [DV]` |
