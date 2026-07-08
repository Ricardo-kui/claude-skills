---
category: variable-operationalization
description: 高管信心（executive confidence）的期权 moneyness 操作化——基于 exercisable options 的 average value/strike price 比例，并说明滞后处理。
function: 对齐性——将心理学构念“信心/过度自信”转译为可重复计算的档案数据指标
slots: M4
source_exemplar: "chung_low_rust_2022_jams (Journal of the Academy of Marketing Science): CEO and CMO confidence measured as average moneyness of exercisable stock options"
created: 2026-07-08
updated: 2026-07-08
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

## 构造细节占位符

| 占位符 | 含义 | 示例 |
|--------|------|------|
| `[actor]` | 行为者 | CEO / CMO / CFO / TMT |
| `[year t]` | 测量时点 | fiscal year t |
| `[average value per option]` | 每份期权平均价值 | Execucomp item OPT_UNEX_EXER_EST_VALUE / OPT_UNEX_EXER_NUM |
| `[average strike price]` | 平均行权价 | 通常由 Compustat 股价与期权价值反推 |
| `[exercisable options]` | 已可行权期权 | 区分 exercisable vs. unexercisable；文献多用 exercisable |
| `[lag structure]` | 滞后处理 | lagged one year relative to DV |

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

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| `CEO confidence is measured by stock option holdings.` | 混淆持仓数量与 moneyness | 明确使用 average value/strike price ratio |
| `Higher stock price means higher confidence.` | 混淆市场价格与高管信念 | moneyness 是“实值程度”而非绝对股价 |
| 未说明 exercisable vs. unexercisable | 不同行权状态反映不同信念结构 | 明确使用 exercisable options |
| 未报告滞后结构 | 反向因果风险 | 在 M4 中说明 `measured with a lag relative to [DV]` |
