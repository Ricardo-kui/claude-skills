<!-- write-results 输出元数据模板：原 SKILL.md 内嵌的 ---metadata--- JSON 区块，由 SKILL.md「输出元数据模板」段按需加载。内容未做语义修改。 -->

### ---metadata---（已废弃——不再生成 JSON 元数据），封装假设-结果对齐状态和 Results 的"证据 DNA"，供 `/paper-review`、`/distill-results-exemplar` 直接消费。

```json
---metadata---
{
  "skill_version": "3.1.0",
  "model_type": "OLS/FE",
  "has_interactions": true,
  "has_mediator": false,
  "journal_target": "AMJ",
  "slot_map": {
    "R1": { "present": true, "table_referenced": "Table 1", "focus": "descriptive stats + VIF" },
    "R2": { "present": true, "table_referenced": "Table 2", "model_sequence": "M1(baseline)→M2(IV)→M3(mediator)→M4(full)" },
    "R3": { "present": true, "hypotheses_tested": ["H1", "H2", "H3"], "four_beat_compliance": "pending" },
    "R4": { "present": true, "interaction_type": "two-way", "interpretation_strategy": "marginal effects plot" },
    "R5": { "present": true, "embedded_in_R3": true },
    "R6": { "present": false, "reason": "all hypotheses significant in main tests" },
    "R7": { "present": true, "threats_addressed": ["reverse causality", "model choice"] },
    "R8": { "present": false },
    "R9": { "present": true }
  },
  "hypothesis_fulfillment_map": [
    { "hypothesis": "H1", "prediction": "positive", "model": "Model 2, Table 2", "result_status": "pending", "causal_language_required": "associated with" },
    { "hypothesis": "H2", "prediction": "positive", "model": "Model 3, Table 2", "result_status": "pending", "causal_language_required": "associated with" },
    { "hypothesis": "H3", "prediction": "positive interaction", "model": "Model 4, Table 2", "result_status": "pending", "causal_language_required": "associated with", "interpretation_required": "marginal effects + figure" }
  ],
  "design_strength": "面板数据/OLS",
  "causal_language_permitted": ["associated with", "related to", "linked to"],
  "causal_language_prohibited": ["causes", "leads to", "drives", "produces"],
  "economic_significance_required": true,
  "non_significant_handling_required": false,
  "downstream_interfaces": ["/paper-review", "/distill-results-exemplar"],
  "cross_section_alignment": {
    "methods_model_match": { "status": "pending", "notes": "需确认 Results 表格与 Methods M7 的模型规格一致" },
    "theory_hypothesis_match": { "status": "pending", "notes": "需填入实际系数后更新 fulfillment_map" }
  },
  "feedback_interface": {
    "validation_skill": "/distill-results-exemplar",
    "validation_mode": "--validate",
    "required_inputs": ["用户写出的 Results 全文", "本 metadata JSON"],
    "validation_focus": ["四拍完整性", "假设-结果对齐", "因果语言合规", "非显著假设报告", "经济显著性"],
    "trigger_timing": "用户完成 Results 初稿后"
  }
}
```

**字段说明**：
- `slot_map`: R1-R9 每个槽位的生成状态和关键属性
- `hypothesis_fulfillment_map`: 假设-结果兑现映射，是 Theory ↔ Results 对齐的核心资产。`result_status` 在生成时为 pending，用户填入实际系数后更新为 supported/not_supported/partially_supported
- `design_strength` / `causal_language_permitted` / `causal_language_prohibited`: 从 Methods metadata 继承，确保 Results 因果语言与 design strength 匹配
- `economic_significance_required`: 是否要求每个显著假设报告经济显著性（通常为 true）
- `cross_section_alignment`: 与上游 skill 的对齐状态
- `feedback_interface`: 写作-反馈闭环接口
