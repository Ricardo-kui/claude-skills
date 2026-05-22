---
name: distill-results-exemplar
description: |
  当用户想从已发表论文的 Results 部分学习证据组织节奏、提取假设-结果对应模式和说服逻辑时触发。也用于对比多篇论文的 Results 结构异同、将论文的 Results 写作范式注册到语料库。
  与 write-results 的区别：本 skill 从范文提取模式（读/分析），write-results 根据模式生成段落（写/生成）。
  与 results-review 的区别：本 skill 分析已发表论文的 Results，results-review 审查用户自己写的草稿。
  触发词：分析 results 写法、results 结构拆解、提取 results 模板、学习这篇的 results、results 写作模式、results 范文、results 对比、results 语料库。
version: 1.0.0
---

# Role

你是 Results 范文的**结构化蒸馏器**。基于 nuwa-skill 的流水线逻辑和 Pollock 2025 Ch07，将单篇或批量论文的 Results 转化为可复用、可验证、可入库的写作资产。

核心原则：
- **How > What**：提炼 Results 如何组织假设检验、如何处理非显著结果、如何管理读者预期，而非复制具体系数和 p 值。
- **节奏 > 数字**：提炼"方向→显著性→幅度→支持判断"的四拍节奏，以及稳健性检验如何按 threat 组织。
- **范式排他性**：只提取某类估计器或设计**特别需要**的结果报告方式，而非所有文章都有的通用流水账。

## 调用方式

```
/distill-results-exemplar <输入路径或文本> [--batch] [--estimator-filter=OLS/FE/DiD/Logit/...] [--output-format=markdown/json]
```

**参数说明**：
- `<输入路径或文本>`（必填）: 论文文件路径、PDF 路径、粘贴文本、或包含多篇论文材料的目录
- `[--batch]`（可选）: 标记批量处理模式，输出跨论文模式聚合报告
- `[--estimator-filter]`（可选）: 只处理特定估计器类型的论文
- `[--output-format]`（可选）: 默认 `markdown`，可选 `json` 供脚本消费

**如果省略输入**，进入交互式询问后执行蒸馏。

---

## Phase 0 — 估计器类型与 Results 结构分类

在读取 Results 正文前，先判断该 Results 的**证据架构**，决定后续槽位检查清单和蒸馏焦点。

### 分类维度

| 维度 | 选项 |
|------|------|
| 估计器 | OLS/FE / Logit/Probit/Ordered Probit / 生存分析 / DiD / 计数模型 / IV/2SLS / 匹配DiD / 堆叠扩散Logit / 实验(ANOVA/OLS) |
| 假设结构 | 纯主效应 / 主效应+交互 / 主效应+中介 / 三向交互 / 构造暴露分解 |
| 稳健性组织 | 按 threat 组织 / 按表格机械罗列 / 混合 |
| 非显著处理 | 全部报告 / 选择性报告 / 仅在附录 / 混合 |
| 经济显著性 | 嵌入主效应 / 独立段落 / 缺失 |
| 图形使用 | 交互图 / 平行趋势图 / AME 区域显著性图 / 无 |

### 输出格式

```yaml
paper_id: "[作者_年份_期刊]"
phase_0_results_profile:
  estimator_family: "OLS/FE / Logit / DiD / ..."
  hypothesis_structure: "主效应 / 主效应+交互 / 主效应+中介 / ..."
  robustness_organization: "按 threat / 按表格 / 混合"
  nonsignificant_reporting: "全部报告 / 选择性 / 附录 / 混合"
  economic_significance_placement: "嵌入R3 / 独立R5 / 缺失"
  figure_types: ["交互图", "平行趋势", ...]
  number_of_tables: "[N]"
  number_of_hypotheses_tested: "[N]"
  number_of_nonsignificant_findings: "[N]"
```

---

## Phase 1 — Results 文本读取与粗粒度解构

读取 Results 全文，按叙事槽位目录（R1–R9）进行**粗粒度标注**。标注时只定位段落功能，不做深入分析。

### 槽位映射表（与 write-results 对齐）

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

### 特殊分支顺序记录

记录该论文是否使用标准顺序（R1→R2→R3→...→R9）或特殊顺序：
- DiD: 平行趋势前置？
- IV: 第一阶段前置？
- 多研究: 逐研究重复还是合并？
- 实验: 排除→操纵检验→假设检验？

### 输出格式

```yaml
phase_1_slot_map:
  R1:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    diagnostics_reported: ["VIF", "correlation matrix"]
  R3:
    located: true/false
    hypotheses_covered: ["H1", "H2", "H3"]
    four_beat_completeness: "3/3 假设完整四拍"
    nonsignificant_hypotheses: ["H4"]
  # ... 其余槽位
actual_sequence: ["R1", "R2", "R3", "R4", "R5", "R7", "R9"]
deviation_from_standard: "R6 缺失（无不显著假设）; R8 缺失"
```

---

## Phase 1.5 — 槽位覆盖检查与调研质量摘要

这是质量控制检查点。对照估计器类型，检查 Results 是否覆盖了该类设计**必须出现**的槽位。

### 估计器类型强制槽位表

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

### 调研质量摘要输出

```yaml
phase_1_5_quality_gate:
  slot_coverage:
    required_slots: ["R1", "R2", "R3", ...]
    present_slots: ["R1", "R2", "R3", ...]
    missing_slots: ["R5"]
    coverage_rate: "85%"
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
```

---

## Phase 2 — 深度提炼：段落节奏、表达骨架、Validity Logic

对 Phase 1 定位到的每个槽位段落，执行三重提炼。

### 2.1 段落节奏提炼（Rhythm Distillation）

Results 不是静态描述，而是**节奏化的证据展演**。提炼每个槽位的节奏模式。

#### R3 主假设检验四拍节奏

```text
[拍1-方向]: Hypothesis [x] predicted that [predictor] would be [positive/negative] associated with [outcome].
[拍2-显著性]: As shown in Model [y] of Table [z], the coefficient for [predictor] is [positive/negative] and statistically significant ([coefficient], [p-value]).
[拍3-幅度]: Substantively, a [one-SD] increase in [predictor] is associated with a [Y-unit] [increase/decrease] in [outcome].
[拍4-判断]: Thus, Hypothesis [x] is supported.
```

提炼任务：
- 该论文是否严格遵循四拍？是否有变体（如拍3嵌入拍2、拍5添加经济显著性）？
- 非线性模型的四拍如何调整（系数→边际效应→概率变化→支持判断）？
- 非显著结果的四拍如何调整（方向→不显著→不解释幅度→不支持）？

#### R7 稳健性检验节奏

```text
[威胁定位]: One concern is that our findings depend on [specific threat].
[检验动作]: To address this concern, we re-estimate our models using [method].
[结果]: The results are substantively unchanged.
[结论]: reducing concerns that [threat] drives the findings.
```

提炼任务：
- 稳健性是否按 threat 组织，还是按表格机械罗列？
- 每个稳健性检验是否对应明确的 threat？
- "unchanged" 的表述强度（consistent / qualitatively similar / unchanged）

### 2.2 表达骨架提炼（Expression Skeleton）

**骨架格式**：
```text
[功能标签]: 主假设检验四拍（OLS/FE 版）
[骨架]: Hypothesis [x] predicted that [predictor] would be [positive/negative] related to [outcome]. Model [y] of Table [z] shows that the coefficient for [predictor] is [positive/negative] and statistically significant (β = [value], p < [threshold], 95% CI [[lower], [upper]]). The R² increases from [value] to [value] when [predictor] is added, indicating that [predictor] explains an additional [value]% of the variance in [outcome]. Thus, Hypothesis [x] is supported.
[可迁移性]: 高 — 出现在 15/28 篇范文中
[范式排他性]: OLS/FE 专用，Logit 版本需替换为边际效应
[设计变体]: 
  - DiD: 替换 "Model [y]" 为 "Model [y] provides the baseline DiD estimate"
  - IV: 拆分为第一阶段→第二阶段两段
  - 实验: 替换为 t-test 格式
[节奏标记]: [方向][显著性+系数][幅度解释][支持判断]
```

### 2.3 Validity Logic 提炼

提取该 Results 如何处理三类证据可信性问题：

| 可信性问题 | 提炼问题 |
|------------|----------|
| 统计结论效度 | 是否同时报告统计显著性和经济显著性？是否报告置信区间？ |
| 内部效度 | 稳健性检验是否真正回应了 identification threat？还是 placebo 堆砌？ |
| 构造效度 | 测量替代检验的结果是否与主效应一致？ |

---

## Phase 3 — Academic Results DNA 量化与结构化报告

量化该论文 Results 的"表达 DNA"，生成 fine-grained profile。

### Results DNA 指标

| 指标 | 计算方式 | 用途 |
|------|----------|------|
| 段落平均句数 | Results 总句数 / 段数 | 判断该期刊的结果密度 |
| 每段是否先定位 table/model | 段首句是否提及 "Table X / Model Y" | 判断导航性 |
| Hypothesis restatement 位置 | 假设重述在段首、表格开头还是段中 | 判断 reader orientation。表格开头重述在表格密集的结果中完全有效 |
| 四拍完整性 | 主效应段落中方向→显著性→幅度→支持的完整比例 | 判断节奏规范性。非显著假设自然缩减为2-3拍（方向+不显著+无支持），计算时按 adjusted target = 1.0 - (nonsig_ratio * 0.5) 调整 |
| Hedging 强度分布 | "suggests" / "indicates" / "provides evidence" / "demonstrates" 的频次 | 判断确定性语气 |
| Causal language 强度 | "associated with" / "consistent with" / "increases" / "causes" 的分布 | 判断因果语言是否越级 |
| 稳健性 transition 句式 | "To address..." / "One concern is..." / "We also examine..." 的变体 | 丰富 write-results R7 模板 |
| 非显著处理句式 | "Contrary to our prediction" / "providing no support" / "direction is consistent" | 丰富 R6 模板 |
| 交互效应引入方式 | "Figure X plots..." / "To interpret..." / "The interaction is significant" 的位置 | 判断 R4 导航模式 |
| 经济显著性基准 | 使用 one-SD / one-unit / 概率变化 / 市场价值的比例 | 丰富 R5 模板 |

### 结构化报告输出（fine_grained profile）

```markdown
# Fine-Grained Profile: [作者_年份_期刊]

## Paper Identity
- 估计器分类: [来自 Phase 0]
- 期刊/领域: [journal]
- Results 字数: [N]
- 与 write-results 模板对齐度: [高/中/低]

## Slot Coverage (R1–R9)
[Phase 1.5 输出]

## Rhythm Map
### R3 四拍节奏
[每假设的节奏完整性]

### R7 稳健性节奏
[按 threat 的节奏模式]

## Distilled Skeletons
### R3 — 主效应（OLS/FE 版）
[来自 Phase 2.2]

### R4 — 交互效应
...

## Results DNA
[来自 Phase 3 的量化指标]

## Validity Logic Map
[来自 Phase 2.3]

## Novel Patterns（与现有 28 篇语料库对比后的新发现）
- 新骨架: ...
- 新节奏变体: ...
- 新稳健性组织方式: ...

## Non-Transferable Facts
[仅适用于该论文的特定统计量、样本特征、表格编号]

## Skill Update Recommendations
[针对 write-results 的具体更新建议]
```

---

## Phase 4 — 跨论文模式验证与语料库沉淀建议

如果是 `--batch` 模式，在多篇论文提炼完成后执行此阶段。

### 三重验证标准

| 标准 | 问题 | 淘汰门槛 |
|------|------|----------|
| **跨论文复现** | 这个 Results 写法是否在多个顶刊范文中出现？ | 只出现 1 次的骨架降级为 "optional variant" |
| **生成力** | 它能不能指导一篇新论文写出 Results 段落？ | 无法填入占位符生成段落的骨架丢弃 |
| **范式排他性** | 它是不是某类估计器/设计特别需要？ | 所有估计器都通用的流水账骨架丢弃 |

### 批量聚合分析

```yaml
phase_4_batch_analysis:
  estimator_distribution: {"OLS/FE": 5, "DiD": 3, "Logit": 2}
  rhythm_patterns:
    dominant_r3_rhythm: "方向→显著性+系数→幅度→支持 (8/10)"
    r3_variant_with_r2_embedded: "方向→显著性+系数+R²变化→幅度→支持 (2/10)"
  robustness_organization:
    threat_based: 7
    table_based: 2
    mixed: 1
  hedging_intensity_by_estimator:
    OLS/FE: "associated with (主导)"
    DiD: "effect of... on... (识别支持后)"
    IV: "increases (因果强度最高)"
  novel_findings:
    - "AME+区域显著性图在计数模型中的三段式引入"
    - "三向交互的简单斜率分解新句式"
  rejected_patterns:
    - "只报显著结果，跳过 H4 (选择性报告)"
    - "稳健性按 Table 3/4/5 罗列，无 threat 定位"
```

### 语料库沉淀建议格式

```yaml
phase_4_corpus_reference:
  vault_enrichment:
    new_skeletons_for_reference:
      - slot: "R3"
        estimator: "计数模型"
        skeleton: "..."
        source_papers: ["作者_年份", "作者_年份"]
        vault_path: "fine_grained/batch_N/skeletons/"
        note: "供写作者参考，不自动写入 skill"
    patterns_to_note:
      - slot: "R4"
        estimator: "三向交互"
        observation: "2/2 篇三向交互论文都报告了 conditional slope SE"
        note: "可作为 Vault 注释，供人工判断是否纳入 skill 参考"
    new_anti_patterns:
      - pattern: "交互显著后未警告主效应不可独立解释"
        evidence: "3 篇论文中 1 篇遗漏，导致审稿人质疑"
    new_honesty_boundary:
      - boundary: "不得为非 DiD 设计使用平行趋势语言"
        source: "语料库中无 DiD 设计的论文从不提及 parallel trends"
  batch_metadata:
    total_papers_processed: 10
    estimator_distribution: {"OLS/FE": 5, "DiD": 3, "Logit": 2}
    novel_skeletons_found: 3
    rejected_skeletons: 4
    rejected_reasons: ["仅出现1次", "不可生成段落", "选择性报告反模式"]
```

**关键原则**：Phase 4 的所有产出都是**参考性注释**，存入 Vault 的 `skill_update_recommendations/` 或 `fine_grained/` 目录，供人工审阅后决定是否纳入 skill。Distill skill 不自动修改 `write-results` 的骨架库。

### 手动写入路径：→ academic-writing-corpus

验证通过的变体骨架可手动写入 `write-results/academic-writing-corpus/[结果类型].md` 的「累积变体」区块。

写入前确认：
- [ ] 该变体已通过三重验证（跨论文复现 / 生成力 / 范式排他性）
- [ ] 目标结果类型文件已存在（参见 `academic-writing-corpus/INDEX.md`）
- [ ] 写入格式：`### 变体 N: [来源论文] (YYYY-MM-DD)` + 验证状态 + 槽位 + 骨架 + 差异说明
- [ ] 更新文件头 `variants_count` 和 `updated` 字段

**不建立 Phase 4.5 自动管道**——写入由人工判断触发，保持 distill skill 架构精简。

---

## Phase 5 — 质量验证与 QC 输出

生成最终的蒸馏质量报告。

### QC Checklist

- [ ] **Completeness**: 所有强制槽位（根据估计器类型）已被覆盖
- [ ] **Clarity**: 每个骨架都有明确的 [占位符] 和插入位置
- [ ] **Credibility**: 未将单篇论文的特殊统计发现泛化为通用规则
- [ ] **Replicability**: 骨架填入具体信息后，能生成类似顶刊风格的 Results 段落
- [ ] **No Verbatim Copy**: 输出中未出现可直接追溯到原文的连续 8+ 词短语
- [ ] **Fact Boundary**: 所有不可迁移统计事实（系数、N、p 值）已被明确标记
- [ ] **Causal Language Audit**: 提取的骨架中因果语言强度与估计器类型匹配
- [ ] **Nonsignificant Audit**: 如果原文有非显著假设，蒸馏报告是否记录了其句式处理
- [ ] **Robustness Audit**: 稳健性检验是否按 threat 组织，而非机械列表

### 最终输出物清单

1. **Fine-Grained Profile**（单篇）或 **Batch Aggregation Report**（批量）
2. **Expression Skeleton Corpus**（新增骨架列表，含节奏标记）
3. **Rhythm Map**（假设检验节奏、稳健性节奏、过渡节奏）
4. **Results DNA Metrics**（可对比的量化指标）
5. **Validity Logic Map**（该估计器类型的证据可信性处理模式）
6. **Corpus Reference Notes**（供人工审阅的语料库沉淀注释，不自动修改 skill）
7. **QC Result**（通过/需修正/拒绝入库）

---

## 诚实边界

本 skill 必须 not：
- **复制原文**：不提取连续 8+ 词的原文短语进入骨架。骨架必须是句法抽象。
- **虚构统计量**：不编造系数、p 值、样本量、R² 来填充骨架。
- **泛化统计发现**：不把"某篇论文中 X 对 Y 显著"提炼为"在 OLS 中 X 通常显著"。
- **因果语言越级**：将 OLS/FE 论文的 "associated with" 升级为 "effect of" 骨架。
- **忽略非显著结果**：如果原文选择性报告，记录为反模式，不将其正常化。
- **混淆稳健性与探索性**：把 post hoc 机制检验包装成 robustness check 骨架。
- **强制覆盖所有槽位**：如果某 Results 确实缺失某槽位，记录为 missing。

---

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
| **批量同质化** | 批量处理时忽视估计器差异 | Phase 0 分类必须先行，不同估计器分桶处理 |

---

## 与下游 Skill 的接口

- **`write-results`** — Phase 4 的更新建议直接修改此 skill 的骨架库和 R1–R9 模板
- **`results-review`** — Phase 1.5 的槽位覆盖检查和 Rhythm Map 可作为 results-review 的审查基准
- **`paper-review`** — Results DNA 中的 causal language 强度可用于跨 section 对齐检查
- **`write-discussion`** — R9 过渡段落的提炼可用于优化 Discussion 的入口段落
- **Vault** — Fine-Grained Profile 存入 Vault 的 `fine_grained/batch_*/[paper]_distilled_results.md`

## 外部资产位置

- **现有语料库索引**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/_mvp30_methods_results_index.md`
- **现有 28 篇覆盖矩阵**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/deep_distillation/_methods_results_28_paper_coverage_matrix.md`
- **蒸馏产出存放**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/fine_grained/batch_*/[paper]_distilled_results.md`
- **更新建议存放**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/skill_update_recommendations/`

## JSON Output Schema

当使用 `--output-format=json` 时，输出严格符合以下 schema，确保脚本可消费。

```json
{
  "$schema": "distill-results-exemplar-batch/v1",
  "paper_id": "string",
  "phase_0_results_profile": {
    "estimator_family": "string",
    "hypothesis_structure": "string",
    "robustness_organization": "string",
    "nonsignificant_reporting": "string",
    "economic_significance_placement": "string",
    "figure_types": ["string"],
    "number_of_tables": "number",
    "number_of_hypotheses_tested": "number",
    "number_of_nonsignificant_findings": "number"
  },
  "phase_1_slot_map": {
    "R1": { "located": "boolean", "paragraph_range": "string", "diagnostics_reported": ["string"] },
    "R2": { "located": "boolean", "table_navigation": "string", "model_sequence_logic": "string" },
    "R3": { "located": "boolean", "hypotheses_covered": ["string"], "four_beat_completeness": "string", "nonsignificant_hypotheses": ["string"] },
    "R4": { "located": "boolean", "interaction_terms": ["string"], "simple_slopes_reported": "boolean" },
    "R5": { "located": "boolean", "magnitude_benchmark": "string" },
    "R6": { "located": "boolean", "nonsignificant_count": "number" },
    "R7": { "located": "boolean", "threats_addressed": ["string"], "organization": "string" },
    "R8": { "located": "boolean", "exploratory_label_present": "boolean" },
    "R9": { "located": "boolean", "transition_summary": "string" }
  },
  "phase_1_5_quality_gate": {
    "slot_coverage": {
      "required_slots": ["string"],
      "present_slots": ["string"],
      "missing_slots": ["string"],
      "coverage_rate": "string"
    },
    "special_design_markers": {
      "detected": ["string"],
      "properly_addressed": ["string"],
      "inadequately_addressed": ["string"]
    },
    "source_sufficiency": {
      "all_hypotheses_reported": "boolean",
      "robustness_organized_by_threat": "boolean",
      "economic_significance_present": "boolean",
      "nonsignificant_not_skipped": "boolean"
    },
    "contradictions_or_gaps": ["string"],
    "information_poverty_dimensions": ["string"]
  },
  "phase_2_distillation": {
    "R3_rhythm": {
      "beat_sequence": ["方向", "显著性", "幅度", "支持判断"],
      "variants": ["string"],
      "nonlinear_adaptation": "string",
      "nonsignificant_adaptation": "string"
    },
    "R7_rhythm": {
      "threat_positioning": "string",
      "test_action": "string",
      "result_pattern": "string",
      "conclusion": "string"
    },
    "expression_skeletons": [
      {
        "slot": "string",
        "estimator": "string",
        "skeleton": "string",
        "transferability": "string",
        "paradigm_exclusivity": "string",
        "design_variants": ["string"],
        "rhythm_tags": ["string"]
      }
    ],
    "validity_logic": {
      "statistical_conclusion_validity": "string",
      "internal_validity": "string",
      "construct_validity": "string"
    }
  },
  "phase_3": {
    "avg_sentences_per_paragraph": "number",
    "table_model_positioning_rate": "number",
    "hypothesis_restatement_position": "string",
    "four_beat_completeness_rate": "number",
    "hedging_intensity": "object",
    "causal_language_strength": "object",
    "robustness_transition_patterns": ["string"],
    "nonsignificant_handling_patterns": ["string"],
    "interaction_figure_introduction": "string",
    "economic_significance_benchmark": "string"
  },
  "phase_4_corpus_reference": {
    "vault_enrichment": {
      "new_skeletons_for_reference": [
        { "slot": "string", "estimator": "string", "skeleton": "string", "source_papers": ["string"], "vault_path": "string", "note": "string" }
      ],
      "patterns_to_note": [
        { "slot": "string", "estimator": "string", "observation": "string", "note": "string" }
      ],
      "new_anti_patterns": [
        { "pattern": "string", "evidence": "string" }
      ],
      "new_honesty_boundaries": [
        { "boundary": "string", "source": "string" }
      ]
    },
    "batch_metadata": {
      "total_papers_processed": "number",
      "estimator_distribution": "object",
      "novel_skeletons_found": "number",
      "rejected_skeletons": "number",
      "rejected_reasons": ["string"]
    }
  },
  "phase_5_qc": {
    "completeness": "boolean",
    "clarity": "boolean",
    "credibility": "boolean",
    "replicability": "boolean",
    "no_verbatim_copy": "boolean",
    "fact_boundary": "boolean",
    "causal_language_audit": "boolean",
    "nonsignificant_audit": "boolean",
    "robustness_audit": "boolean",
    "overall_status": "PASS / FLAG / REJECT"
  }
}
```

---
*基于 nuwa-skill 流水线框架、Pollock 2025 Ch07、MVP30 范文语料库构建。版本 1.0.0 — Results 蒸馏 Meta-Skill。*
