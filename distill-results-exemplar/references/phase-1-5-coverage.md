# Phase 1.5 — 槽位覆盖检查与调研质量摘要

这是质量控制检查点。对照估计器类型，检查 Results 是否覆盖了该类设计**必须出现**的槽位。

## 估计器类型强制槽位表

| 估计器类型 | 强制槽位 | 缺失即高风险 |
|------------|----------|--------------|
| OLS/FE | R1, R2, R3, R7 | R1 缺诊断、R3 缺经济显著性 |
| Logit/Probit | R1, R2, R3, R5(嵌入), R7 | R3 直接解释系数大小、R5 缺边际效应 |
| Ordered Probit | R1, R2, R3, R5, R7 | R3 未区分 category-specific effects |
| 生存分析 | R1, R2, R3, R7 | R3 缺 shape parameter 解释 |
| DiD | R2, R3, R7(平行趋势+安慰剂) | R7 缺 event-study / permutation |
| 计数模型 | R1, R2, R3, R5(AME), R7 | R3 只报 IRR 不解释方向 |
| IV/2SLS | R2(第一阶段), R3, R7 | R2 缺 F-statistic / R7 缺排他性检验 |
| 匹配DiD | R2, R3, R7 | R7 缺匹配敏感性 / 重叠支撑 |
| 实验 | R2(排除/操纵检验), R3, R7 | R2 缺 manipulation check |
| 堆叠扩散Logit | R2, R3, R7 | R3 未解释风险集 |
| 同伴效应/网络效应 | R3, R4, R7 | R7 缺 falsification / 安慰剂网络 |
| 推断二元结果 | R3, R7 | R7 缺阈值敏感性 |
| 多研究 | R1–R8(逐研究), R9(跨研究综合) | 缺少跨研究一致性对比、未标记研究间设计升级逻辑 |
| 构造暴露分解 | R3, R4, R7 | R3 未分解为 component A/B、R4 未报告暴露强度异质性 |
| 跨受众构念对比 | R3, R5, R7 | R3 未在多 outcome 间做上层梯队对比、R5 缺 audience-specific 幅度解释 |
| 三向交互 | R3, R4, R7 | R4 缺简单斜率分解、未报告 conditional slope 标准误 |

## 调研质量摘要输出

```yaml
phase_1_5_quality_gate:
  slot_coverage:
    required_slots: ["R1", "R2", "R3", ...]
    present_slots: ["R1", "R2", "R3", ...]
    missing_slots: ["R5"]
    coverage_verdict: "完整 / 轻微缺口 / 严重缺失"
  special_design_markers:
    detected: ["三向交互", "AME+区域显著性"]
    properly_addressed: ["R4 分解了简单斜率"]
    inadequately_addressed: ["R5 未报告区域显著性的转折值"]
  source_sufficiency:
    all_hypotheses_reported: true/false
    robustness_organized_by_threat: true/false
    economic_significance_present: true/false
    nonsignificant_not_skipped: true/false
  contradictions_or_gaps: ["R3 声称支持 H2 但系数方向相反", "R7 报告了安慰剂检验但在 Methods 中未预告"]
  information_poverty_dimensions: ["未报告置信区间", "未说明 simple slope 的标准误"]
  skill_implication:
    - slot: "R3"
      implication: "四拍完整但缺少 CI → write-results 生存分析 R3 主骨架应增加 CI 报告要求"
    - slot: "R7"
      implication: "稳健性按表格罗列而非按威胁 → 建议在 R7 主骨架中强制 threat-based 组织"
```
