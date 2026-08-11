# Phase 3 — Academic Results DNA 量化与结构化报告

量化该论文 Results 的"表达 DNA"，生成 fine-grained profile。

## 论证手法诊断

不量化机械指标（句数、定位率），而是诊断这篇 Results 在证据展演上的强弱之处。

| 维度 | 诊断问题 | 输出 |
|------|---------|------|
| **四拍节奏** | 主效应段落是否有方向→显著性→幅度→支持判断的完整节奏？非显著结果如何处理？ | 完整/缺拍 + 非显著处理方式 |
| **因果语言自律** | "associated with" vs "effect of" 的分布是否匹配估计器设计？ | 越级/一致/过于保守 |
| **稳健性组织** | 按威胁组织还是按表格机械罗列？ | threat-based / table-based / mixed |
| **非显著叙事** | 不显著结果是被诚实报告、跳过、还是转化为边界发现？ | 陈述处理方式 |
| **新颖度** | 这篇 Results 的证据展演节奏与 write-results 当前模板有多少不同？ | 高度新颖 / 部分新颖 / 与模板一致 |

每个诊断维度输出时附带 skill 对比：
```
[定性判断] → 与 write-results 当前模板的关系 → [skill 改进方向]
```

## 结构化报告输出（fine_grained profile）

```markdown
# Fine-Grained Profile: [作者_年份_期刊]

## Paper Identity
- 估计器分类: [来自 Phase 0]
- 期刊: [journal]
- 新颖度: 这篇 Results 的证据展演节奏与现有模板的差异程度

## Slot Coverage (R1–R9) — 含 quality + learn_worth
[Phase 1 输出]

## 值得学的骨架（skill_gap != SKIP）
[来自 Phase 2.2 — 仅列出真正新增的]

## 论证手法诊断
[Phase 3 诊断维度]

## Validity Logic Map
[来自 Phase 2.3]
```

## 反模式（蒸馏过程中主动排查）

| 反模式 | 表现 | 处理方式 |
|--------|------|----------|
| **原文依赖型骨架** | 骨架中包含论文特有的变量名、表格编号、具体系数 | 泛化为 [predictor] / [Table X] / [coefficient] |
| **系数即解释** | 原文只报 "β=0.15, p<0.05" 不翻译实质含义 | 记录为反模式，不将其作为"标准骨架"提取 |
| **因果越级语言** | 将 OLS 结果中的 "caused" "led to" 原样保留 | 在骨架中降级或标注 design-specific 允许范围 |
| **交互后主效应独立解释** | 交互显著后仍独立解释主效应 | 记录为反模式，在 skill 中增加警告骨架 |
| **稳健性机械罗列** | 按 Table 3/4/5 罗列而非按 threat 组织 | 记录为反模式，提取 threat-based 替代骨架 |
| **忽略非显著** | 原文跳过不显著假设 | 在 R6 部分标记为"缺失"，并记录为非支持处理反例 |
| **事后分析未标记** | post hoc 检验包装成 confirmatory | 记录为反模式，在 R8 中增加探索性标记骨架 |
