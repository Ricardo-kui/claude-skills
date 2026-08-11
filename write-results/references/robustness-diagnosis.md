# Robustness Diagnosis — 稳健性检验决策诊断（从 SKILL.md 下沉，v0.1）

> 由 write-results 在 `methods.robustness_plan` 缺失时**执行**（Yuan et al. 2026, *Journal of Management* 六维稳健性分析框架 + Figure 2 决策流程图）。在生成 R7 段落之前按三步评估需要哪些稳健性检验——避免"机械罗列所有稳健性检验"的反模式，只生成对该研究特定脆弱性有意义的检验。

## Step 1: 六维扫描

检查每个维度是否存在可检验的替代方案：

| 维度（Yuan et al. 2026） | 检查问题 | 信号来源 |
|--------------------------|---------|---------|
| **测量变异** (Measurement) | 关键构念是否有替代操作化/代理变量/替代数据源？ | `paper-state.yaml` variables 字段含多个备选测量 / 用户标记 |
| **协变量变异** (Covariate) | 控制变量选择是否存在理论不确定性？替代控制集是否合理？ | 控制变量数量 > 5 / 缺少 DAG / 用户标记 |
| **预处理变异** (Preprocessing) | 是否做了缺失数据处理、离群值处理、变量转换？有替代策略吗？ | 样本量 > 1000 / 存在缺失值 / 含偏态变量 |
| **子样本变异** (Subsampling) | 样本是否可被理论上有意义地拆分为子组（行业/时期/规模/人口）？ | 面板数据 / 多行业 / 多时期 / 用户标记 |
| **统计规格变异** (Statistical specification) | 是否有多个理论上可辩护的估计器/参数设定/聚类层级？ | `estimator_family` 含备选 / 复杂数据结构 |
| **方法变异** (Methodological) | 是否有多子研究/多方法（实验+调查+二手数据）？ | `paper-state.yaml` sub-studies 数量 ≥ 2 |

## Step 2: 可辩护性 / 可行性 / 必要性筛选

对 Step 1 识别到的每个维度，按论文 REC A2–A4 评估：

| 筛选标准 | 问题 | 不通过时的处理 |
|---------|------|---------------|
| **可辩护性** (Justifiability) | 替代方案是否有理论依据且统计上有效？非任意变化或劣质选择？ | 排除该维度，在 R7 开头或 Methods 中解释排除理由 |
| **可行性** (Feasibility) | 替代方案是否可用现有数据实现？无需额外数据收集？ | 排除该维度，在 limitations 中说明"would be valuable but not feasible because [reason]" |
| **必要性** (Necessity) | 该维度是否对应本研究的特定脆弱性（研究问题新颖性 / 方法和统计局限 / 结果特征）？ | 标记为 optional——可生成但不强制 |

**脆弱性来源**（论文 REC A3）：
- **研究问题特征**：新颖/反直觉发现、挑战已有结论、先前文献结论不一致、可能指导高成本实践干预
- **方法和统计脆弱性**：小样本、测量工具心理计量属性未知或不佳、使用新统计方法
- **结果特征**：效应量小、跨样本/时期/子组不一致、与 meta 分析或强理论预测矛盾

## Step 3: 输出稳健性计划

基于筛选结果，输出结构化稳健性计划：

```yaml
robustness_plan:
  mandatory:       # 必须生成 R7 段落的维度——有明确威胁 + 有可行替代
    - measurement_variation
  recommended:     # 建议生成但可跳过
    - covariate_variation
    - statistical_specification_variation
  optional:        # 标记为可选/探索性（低必要性但有可行替代）
    - preprocessing_variation
  excluded:        # 排除并附理由
    - methodological_variation: "单一研究设计，无多方法"
    - subsampling_variation: "样本量不足以支持理论上有意义的子组分析"
```

该计划（1）指导后续 R7 段落生成——只生成 `mandatory` 和 `recommended` 维度的段落；（2）写入 `paper-state.yaml` 供下游消费。

## 诊断触发方式

- **自动触发**：当 `paper-state.yaml` 中 `methods.robustness_plan` 字段不存在时
- **手动跳过**：`/write-results OLS/FE --skip-robustness-diagnostic`（直接使用默认 R7 threat-based 段落）
- **仅诊断**：`/write-results --robustness-diagnostic-only`（仅输出诊断结果，不生成段落骨架）
