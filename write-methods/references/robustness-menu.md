# Robustness Check Menu — 稳健性归属判断（从 SKILL.md 下沉，v0.1）

> 由 write-methods 在涉及稳健性归属 / M10 预告 / M8 边界时**读取**。顶刊论文通常要求系统报告稳健性，但**位置取决于该检验是否属于基准识别策略的一部分**。

## 归属判断

| 检验类型 | 归属 | 原因 |
|---|---|---|
| IV 排他性约束 / 弱工具变量诊断 | **M8**（基准识别一部分） | 没有这些诊断，2SLS 估计量本身不可信 |
| DiD 平行趋势 / 事件研究 | **R7**（通常）或 **M8 预览 + R7 报告** | 平行趋势是识别假设，但其结果通常在 Results 中展示；M8 可预告 "we assess in Results" |
| 匹配共同支撑域 / 平衡性 | **M2/M8**（基准样本构造） | 匹配是获得可比对照组的前提 |
| 替代模型 / 替代测量 / 子样本 / 安慰剂 / 时点敏感性 | **R7** | 属于对主结果稳健性的补充验证 |
| 机制 / 替代解释排除 / 探索性扩展 | **R8** | 非假设检验，属于补充或事后分析 |

## Results 稳健性清单（供 M10 预告时引用）

当用户在 Methods 中问及 robustness 时，提示："稳健性检验通常在 Results 中展开；Methods 只在基准识别需要时简要说明。"

- [ ] **Model selection**: Alternative functional forms, distributions, or estimators (e.g., Weibull/Gompertz for hazard models; GEE for panel logit; LPM+2SLS for binary IV)
- [ ] **Measure sensitivity**: Alternative operationalizations, cutoffs, percentile thresholds, or transformations (e.g., top/bottom 20%, 30%, 40% vs. quartile; raw count vs. relative percentage)
- [ ] **Sample selection**: Matching (CEM, PSM), weighting, subsample analysis, or attrition comparison
- [ ] **Reverse causality**: Lag structures (t-1, t-2), Granger causality, lead-lag tests, or control-function approach
- [ ] **Alternative explanations**: Mechanism vs. confound via interactions, auxiliary models, or placebo tests
- [ ] **Outliers and influential observations**: With and without top/bottom 1% or Cook's distance thresholds
- [ ] **Clustering and SE sensitivity**: Alternative clustering levels, wild bootstrap, or spatial HAC

## M10 Results 预告段（仅用于预告 R7 内容，不展开结果）

```text
To assess the robustness of our findings, we report a series of sensitivity analyses in the Results section. These address [measurement concerns] through [alternative operationalizations], [model choice] through [alternative estimators], [sample composition] through [subsample analyses], and [endogeneity concerns] through [lag structures / placebo tests].
```

**注意**：该预告段不得包含具体结果、系数或 "results remain consistent" 等结论性表述——那些属于 R7。

## M8 中不应出现的稳健性内容

以下检查应严格留在 Results（R7/R8），不得在 M8 中详细展开：
- 替代模型（如 OLS 换 Tobit / Poisson 换负二项）的估计结果；
- 替代测量/截断点选择后的系数变化；
- 安慰剂检验、随机化处理、置换检验的具体结果；
- 子样本敏感性分析的结果。
