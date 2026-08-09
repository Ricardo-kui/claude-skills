# Phase 1 — Results 文本读取与粗粒度解构

读取 Results 全文，按叙事槽位目录（R1–R9）进行**粗粒度标注**。标注时只定位段落功能，不做深入分析。

## 槽位映射表（与 write-results 对齐）

| 槽位 | 功能 | 粗粒度标注任务 |
|------|------|----------------|
| R1 | 描述性统计 / 诊断导向 | 定位 descriptives 段落，标记诊断检验（VIF/multicollinearity） |
| R2 | 模型序列 / 表格导航 | 定位 table navigation，标记 Model 1→2→3 的增量逻辑 |
| R3 | 主假设检验 | 逐假设定位，标记方向→显著性→幅度→支持判断的四拍完整性 |
| R4 | 交互效应 / 条件效应 | 定位交互项报告，标记 simple slopes / AME / 图示 |
| R5 | 经济 / 实质显著性 | 定位 magnitude 解释，标记基准对比方式 |
| R6 | 非显著 / 混合 / 意外发现（可选，若无非显著假设） | 定位 null/mixed findings，标记处理方式。若 number_of_nonsignificant_findings = 0 或 1，缺失不严重惩罚 |
| R7 | 稳健性 / 效度 / 敏感性 | 逐 threat 定位，标记组织方式（threat-based vs table-based） |
| R8 | 补充 / 事后 / 机制 | 定位 supplemental，标记探索性/验证性标签 |
| R9 | Results→Discussion 过渡（可选） | 定位 transition，标记核心模式总结。顶刊实证论文中约 70% 缺失，若缺失不严重惩罚覆盖率 |

## 特殊分支顺序记录

记录该论文是否使用标准顺序（R1→R2→R3→...→R9）或特殊顺序：
- DiD: 平行趋势前置？
- IV: 第一阶段前置？
- 多研究: 逐研究重复还是合并？
- 实验: 排除→操纵检验→假设检验？

## 输出格式

```yaml
phase_1_slot_map:
  R1:
    quality: "✅ 强 / ⚠️ 可改进 / ❌ 缺失"
    paragraph_range: "[第X段–第Y段]"
    diagnostics_reported: ["VIF", "correlation matrix"]
    learn_worth: "值得学/不值得学/反模式 — 1句话原因"
  R3:
    quality: "✅ 强 / ⚠️ 可改进 / ❌ 缺失"
    hypotheses_covered: ["H1", "H2", "H3"]
    four_beat_completeness: "3/3 假设完整四拍"
    nonsignificant_hypotheses: ["H4"]
    learn_worth: "值得学/不值得学/反模式 — 1句话原因"
  # ... 其余槽位
actual_sequence: ["R1", "R2", "R3", "R4", "R5", "R7", "R9"]
deviation_from_standard: "R6 缺失（无不显著假设）; R8 缺失"
```
