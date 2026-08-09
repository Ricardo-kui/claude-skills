# Phase 1.5 — 槽位覆盖检查与调研质量摘要

这是质量控制检查点。对照设计类型，检查 Methods 是否覆盖了该类设计**必须出现**的槽位。

## 设计类型强制槽位表

| 设计类型 | 强制槽位 | 缺失即高风险 |
|----------|----------|--------------|
| 面板数据/OLS | M1, M2, M3, M4, M6, M7, M10 | M7 缺诊断、M6 缺 because |
| 自然实验/DiD | M1, M2, M7, M8 | M8 缺平行趋势、M2 缺处理/对照描述 |
| IV/2SLS | M4, M7, M8 | M8 缺排他性约束、M7 缺第一阶段说明 |
| 实验 | M1, M2, M6, M7, M8 | M8 缺操纵检验、M2 缺随机化说明 |
| 匹配DiD | M2, M7, M8 | M2 缺匹配后平衡、M8 缺重叠支撑 |
| 文本构念 | M3/M4, M7, M8 | M3/M4 缺效度链、M8 缺与人工程度相关性 |
| 同伴效应/网络效应 | M4, M7, M8 | M4 缺反射性问题处理、M8 缺 falsification |
| 动态面板/GMM | M7, M8 | M7 缺 Nickell bias 说明、M8 缺过度识别 |
| 同时方程 | M1, M4, M7, M8 | M7 缺 order/rank 条件、M8 缺方程特定诊断 |
| 稀有结果 | M2, M3, M7 | M2 缺抽样策略说明、M7 未解释稀有结果对幅度的影响 |
| 实证对象构建 | M2, M3/M4, M7 | M2 缺从原始痕迹到分析变量的构建步骤、M3/M4 缺 face validity 论证 |
| 事件历史+事件研究 | M2, M3, M7 | M2 缺过程时钟定义、M3 未分过程/市场双时钟 DV、M7 缺分布选择依据 |
| PSM匹配面板 | M2, M7, M8 | M2 缺匹配步骤与共同支撑域、M8 缺匹配后平衡检验 |
| 多行为者设计 | M2, M3, M7 | M2 缺多数据源匹配逻辑、M3 未区分主/辅行为者结果 |
| 推断二元结果 | M3, M4, M7, M8 | M3 缺从信号到状态的推断逻辑、M8 缺分类准确性验证 |
| IV + 非线性 (Tobit/Poisson/生存) | M4, M7, M8 | M8 缺排他性约束与第一阶段说明、M7 未解释非线性估计器选择依据 |

## 调研质量摘要输出

```yaml
phase_1_5_quality_gate:
  slot_coverage:
    required_slots: ["M1", "M2", ...]
    present_slots: ["M1", "M2", ...]
    missing_slots: ["M8"]
    coverage_verdict: "完整 / 轻微缺口 / 严重缺失"  # 替代数字百分比——覆盖率 80% 但论证平庸不如 60% 但每个槽位都是典范
  special_design_markers:
    detected: ["IV", "匹配"]
    properly_addressed: ["M7 第一阶段"]
    inadequately_addressed: ["M8 排他性约束仅一句话"]
  source_sufficiency:
    sample_funnel_auditable: true/false
    diagnostic_tests_named: true/false
    robustness_location_specified: true/false
  contradictions_or_gaps: ["M7 声称用 FE 但未报告 Hausman", "M8 说检验在 Results 但 Results 未出现"]
  information_poverty_dimensions: ["未报告 VIF 值", "未说明标准误聚类层级"]
  skill_implication:
    - slot: "M2"
      implication: "无漏斗计数 → 建议在面板数据-OLS 变体 X 的警告中标注'多数据库合并可省略漏斗，但需报告交集后 N'"
    - slot: "M7"
      implication: "分布选择仅一句话 → 建议在生存分析 M7 主骨架中增加参数分布选择的最小论证要求"
```
