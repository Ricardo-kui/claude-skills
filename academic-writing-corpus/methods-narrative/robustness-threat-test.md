# Robustness "Threat-Test" Narrative

## 功能定义
将稳健性检验组织为"威胁-测试"对（threat-test pairs）——每个威胁对应一个具体测试，展示研究者对潜在方法论威胁的系统性识别和针对性应对，而非简单罗列替代模型。

## 句法模板

**模板 A（主题分类型）**：
```
We conducted a series of robustness checks to ensure that our results
are not driven by [specific concern].

Endogeneity Concerns
To address potential endogeneity, we [method] and found [consistent
different results].

Alternative Model Specifications
To ensure our results are not sensitive to model choice, we estimated
[alternative model] and found [consistent/different results].

Alternative Measures
To ensure our results are not driven by measurement choices, we used
[alternative measure] and found [consistent/different results].

Sample Sensitivity
To ensure our results are not driven by specific sample characteristics,
we [subsample analysis / exclusion of outliers] and found
[consistent/different results].
```

**模板 B（单威胁详细型）**：
```
A potential concern is that [specific threat]. To address this, we
[method]. Specifically, we [detailed procedure]. The results show
that [finding], suggesting that [our main results are robust to this
concern / this concern explains part of our findings].
```

**模板 C（安慰剂检验型）**：
```
To further validate our identification strategy, we conduct a placebo
test. If our results are driven by [mechanism], then we should not
find a significant effect when we [placebo procedure]. The results
show that [no significant effect / different pattern], confirming
that our main findings are not spurious.
```

## 例句（来自 MVP30）

**来源**：CEO Stock Ownership, Recall Timing, and Stock Market Penalties — Darby et al.

> "5.3.1 Endogeneity (CEM matching, CEO Flip)"
> "5.3.2 Modeling (CPH models, GLM)"
> "5.3.3 Event Date"

**来源**：Now You See Me — Han et al.

> "Scandal measure validation (LIWC)"
> "Alternative cutoffs"
> "Alternative status specifications"
> "Non-high-status interactions"
> "RIR analysis"
> "Post hoc main effects"

**来源**：A Rising Tide Lifts All Boats — DesJardine et al.

> "To ensure our results are not driven by [specific concern], we
> [action taken]."
> "As an alternative specification, we estimated [alternative model]
> and found [consistent/different] results."

**改写模板**：
> "We conducted a series of robustness checks to ensure that our results
> are not driven by alternative explanations.
>
> **Endogeneity.** To address potential endogeneity, we [method].
> The results remain [consistent / directionally similar].
>
> **Alternative Specifications.** We estimated [alternative model]
> and found [consistent results].
>
> **Alternative Measures.** Using [alternative measure], the results
> are [consistent].
>
> **Sample Sensitivity.** Restricting the sample to [subsample],
> the results [hold / are attenuated]."

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | 通用型——所有顶级期刊都要求系统稳健性检验 |
| **理论类型** | 内生性、模型误设、测量误差、样本选择 |
| **前提条件** | 每个检验必须对应一个具体威胁；不能只是"跑更多模型" |
| **风险** | 若稳健性检验结果不一致，必须在讨论部分诚实报告 |

## 关键技巧

稳健性叙事的核心是**威胁与测试的一一对应**：

| 弱表达 | 强表达 |
|--------|--------|
| "We run several robustness checks" | "To address the concern that [specific threat], we [specific test]. The results confirm that [finding]" |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 检验无威胁 | 跑了很多模型但不说明针对什么威胁 | 每个检验前必须先声明威胁 |
| 结果不一致不报告 | 某些稳健性检验结果不同但不提及 | 必须诚实报告不一致结果并解释 |
| 过度稳健性 | 20+ 个稳健性检验 | 5-8 个核心检验足够；过多检验分散焦点 |

## 相关语料

- 配合 `methods-narrative/endogeneity-defense.md` 使用：内生性是稳健性检验的首要类别
- 配合 `methods-narrative/model-selection.md` 使用：替代模型规格是稳健性检验的核心
- 配合 `discussion-moves/limitation-boundary-control.md` 使用：讨论部分回应对稳健性的质疑

## 验证状态
- **跨论文复现**: ✓✓ ROBUST（所有 28 篇 MVP30 论文都有系统稳健性检验）
- **来源论文**: 多篇 × 28
- **生成力**: ✓ GENERATIVE
- **排他性**: 通用
- **期刊限制**: 无限制
- **收录状态**: ⭐ PREMIUM
