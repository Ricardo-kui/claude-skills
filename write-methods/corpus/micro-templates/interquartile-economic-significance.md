---
category: economic-significance
description: 用自变量的四分位距（IQR）移动解释回归系数的经济显著性——将统计系数转化为“从第25百分位到第75百分位”的实质变化。
function: 经济显著性——把 β 系数翻译为读者可感知的业务/组织影响
slots: M7, M8, M10
source_exemplar: "chung_low_rust_2022_jams (Journal of the Academy of Marketing Science): interquartile move in CEO confidence associated with 0.29 percentage point increase in MMM"
created: 2026-07-08
updated: 2026-07-08
---

# 四分位距经济显著性（Interquartile Economic Significance）

## 核心原则

统计显著性不等于经济显著性。对于连续或近似连续的预测变量，顶刊常用**从第25百分位到第75百分位（IQR）的移动**来报告系数的经济含义。这种做法有三个优点：
1. 直接对应样本中真实存在的变异幅度；
2. 便于跨研究比较（不受原始单位量纲影响）；
3. 比“一个标准差变化”更不容易受极端值驱动。

## 标准句式

### 选项 1：基础版

> An interquartile move in [IV] from the 25th percentile to the 75th percentile is associated with a [value] [unit] increase in [DV].

### 选项 2：与系数直接挂钩

> The coefficient on [IV] is [coefficient] (SE = [se], p [relation] [threshold]), indicating that an interquartile increase in [IV] is associated with a [value] [unit] change in [DV].

### 选项 3：强调相对幅度

> Given that the mean (median) of [DV] is [mean_DV] ([median_DV]), a [value] [unit] change following an interquartile increase in [IV] represents an economically meaningful [percentage]% shift relative to the typical [DV] level.

### 选项 4：与业务后果衔接

> A back-of-the-envelope calculation suggests that an interquartile increase in [IV] leads to an expected [outcome] of [magnitude] over [time horizon] through its effect on [DV].

## 占位符清单

| 占位符 | 含义 | 示例 |
|--------|------|------|
| `[IV]` | 核心自变量 | CEO confidence |
| `[DV]` | 因变量 | myopic marketing management (MMM) |
| `[coefficient]` | 回归系数 | 0.287 |
| `[se]` | 标准误 | 0.11 |
| `[value]` | IQR 移动对应的 DV 变化 | 0.29 |
| `[unit]` | DV 单位 | percentage points |
| `[mean_DV]` / `[median_DV]` | DV 描述统计 | 0.42% |
| `[percentage]` | 相对变化百分比 | 69% |
| `[time horizon]` | 时间跨度 | the next few years |

## 适用槽位

| 槽位 | 使用情境 |
|------|---------|
| M7 | 在模型规格段落中预告将如何解释经济显著性 |
| M8 | 在识别/诊断段落中补充效应大小的直观说明 |
| M10 | 在 Methods→Results 过渡段中预告 Results 将报告 IQR 经济显著性 |
| Results | 主效应段落中直接报告 |

## 与标准差解释的对比

| 指标 | 优点 | 缺点 | 适用情境 |
|------|------|------|---------|
| IQR（25th–75th） | 抗极端值；反映样本真实离散 | 若分布偏斜，IQR 与 SD 差异大 | 连续预测变量；分布有偏 |
| 1 SD | 与标准化系数兼容；统计惯例 | 受极端值影响；对肥尾分布不稳定 | 预测变量近似正态 |
| Min–Max | 显示全谱效应 | 依赖样本极值，外部效度弱 | 作为补充而非主报告 |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 仅报告 `β = 0.287, p < .01` | 读者无法判断影响大小 | 补充 IQR 或 SD 经济显著性 |
| `A one-unit increase in X...` | 原始单位可能缺乏业务含义 | 改用 IQR 或标准化解释 |
| 经济显著性数字与 Results 表格不一致 | 跨 section 断裂 | 确保 Methods 预告与 Results 报告使用同一分位数 |
| 忽略 DV 的基础率 | 0.29 在基础率为 0.42 时很显著，在基础率为 100 时微不足道 | 报告相对百分比或基础率 |
