---
design_type: "自然实验-DiD"
status: 🧪 EMERGING
source_papers:
  - lee_wu_bednar_orsc_18968 (Organization Science; DOI 10.1287/orsc.2024.18968)
variants_count: 3
created: 2026-05-18
updated: 2026-08-02
---

# 自然实验-DiD — Methods 骨架

## 主骨架

参见 `write-methods/SKILL.md` → 槽位骨架加载 → 本类型适用的 `references/slot-M*.md`（各 slot 文件内含 `自然实验-DiD` 专用变体）。

## 设计特征摘要

- 地理层级冲击必须明确映射到分析单位，并报告从原始事件到可识别处理组的样本漏斗。
- 估计器选择应服从因变量支持域；“由计数项目构造”不等于必须使用计数模型。
- 错位实施 DiD 的可信度检查应围绕识别威胁组织；传统 TWFE/Bacon 只能诊断，不能修复异质处理效应偏误。

## 累积变体

<!-- distill-methods-exemplar Phase 4 验证通过的变体写入此处 -->
<!-- 格式：
### 变体 N: [来源论文] (YYYY-MM-DD)
**验证状态**: 通过 / 需修正
**槽位**: M?
**骨架**:
> "..."
**与原骨架差异**: ...
-->

### 变体 1：跨层级冲击映射 + 处理事件样本漏斗（2026-08-02）

**来源论文**: Lee, Wu & Bednar, *Organization Science*, DOI 10.1287/orsc.2024.18968

**验证状态**: EMERGING（单篇；`section_variant`）

**槽位**: M2（Data and Sample）

**骨架**:
> "We observe [shock] at the [geographic/institutional] level and assign exposure to [analysis units] using [headquarters/operating-location rule]. This mapping explains why the number of treated [locations] in the analytical sample is smaller than the number in the original event database: only [locations meeting the unit-presence rule] contribute treated observations. Starting from [N0] affected locations, the final sample contains [N1] treated locations, [N2] units, and [N3] unit-period observations; we also report the distribution across [event subtypes]."

**与原骨架差异**: 不只报告最终 N；把“冲击发生在哪一层—谁被视为暴露—为何处理事件减少”写成可审计映射链。

**边界**:
- headquarters 映射必须有理论理由；若经营活动跨地区，需讨论 exposure misclassification。
- 同一单位可能受多个事件影响时，必须预先规定 first-event、stacked cohort 或风险集规则。

### 变体 2：有符号的计数衍生因变量 → 线性 FE 估计器选择（2026-08-02）

**来源论文**: Lee, Wu & Bednar, *Organization Science*, DOI 10.1287/orsc.2024.18968

**验证状态**: EMERGING（单篇；`section_variant`）

**槽位**: M7（Model Specification）

**骨架**:
> "Although [outcome] is constructed from counts, it is defined as [positive component minus negative component] and can therefore take negative values. Poisson and negative-binomial models, which require a nonnegative outcome, are not appropriate for this signed measure. We estimate a linear [unit]-fixed-effects model with [time] fixed effects, lag [moderators/controls] by [k] period(s), and cluster standard errors at the level where treatment varies."

**与原骨架差异**: 先检查支持域，再选择模型；避免根据变量来源标签机械使用 count model。

**边界**:
- 负值支持域只是排除 Poisson/NB 的理由，不自动证明线性模型最优；仍需检查极端值、分布形态与替代构造。
- 聚类层级原则上不应低于处理赋值层级；处理簇很少时需小样本修正或随机化推断。

### 变体 3：错位 DiD 三层诊断栈 + 现代估计诚实边界（2026-08-02）

**来源论文**: Lee, Wu & Bednar, *Organization Science*, DOI 10.1287/orsc.2024.18968

**验证状态**: EMERGING / LEGACY-DIAGNOSTIC（可借用组织方式，不得把原估计方案当现代默认）

**槽位**: M8（Validity and Robustness）

**骨架**:
> "We organize design checks by threat. First, an event-study plot assesses pre-treatment dynamics. Second, a permutation exercise randomly reassigns treated units and treatment timing to evaluate whether similarly large estimates arise under placebo exposure. Third, a decomposition describes which treatment-group comparisons receive weight in the conventional TWFE estimate. Because decomposition diagnoses rather than removes contamination from heterogeneous cohort/time effects, the main analysis should additionally use a heterogeneity-robust staggered-DiD estimator (e.g., cohort-time ATT or interaction-weighted event study) and report sensitivity to deviations from parallel trends."

**与原骨架差异**: 把图、置换与权重分解分别绑定到 pretrend、偶然相关和污染比较三类威胁，并明确诊断与修复的差异。

**不可降级的现代要求**:
- Goodman–Bacon 分解不能替代 Callaway–Sant'Anna / Sun–Abraham 等异质性稳健估计。
- “处理前系数不显著”不是平行趋势成立的充分证据；应给联合检验、置信区间和图形，并在可行时做 HonestDiD/Rambachan–Roth 型敏感性分析。
- 随机置换必须保持真实处理设计的簇结构与实施时序约束；任意打乱会产生无意义的安慰剂分布。
