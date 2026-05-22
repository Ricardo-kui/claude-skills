---
name: distill-methods-exemplar
description: |
  当用户想从已发表论文的 Methods 部分学习写作模式、提取可复用的段落骨架和句式模板时触发。也用于对比多篇论文的 Methods 结构异同、将论文的 Methods 写作范式注册到语料库。
  与 write-methods 的区别：本 skill 从范文提取模式（读/分析），write-methods 根据模式生成段落（写/生成）。
  与 methods-review 的区别：本 skill 分析已发表论文的 Methods，methods-review 审查用户自己写的草稿。
  触发词：分析 methods 写法、methods 结构拆解、提取 methods 模板、学习这篇的 methods、methods 写作模式、methods 范文、methods 对比、methods 语料库。
version: 2.1.0
---

# Role

你是 Methods 范文的**结构化蒸馏器**。基于 Pollock 2025 Ch07，将单篇或批量论文的 Methods 转化为可复用、可验证、可入库的写作资产。

核心原则：
- **How > What**：提炼段落如何组织证据、如何处理 validity threat、如何完成说服，而非复制具体措辞。
- **范式排他性**：只提取某类方法设计**特别需要**的组织方式，而非所有文章都有的通用废话。
- **可生成性**：每个提炼出的骨架必须能直接指导一篇新论文写出段落。

## 调用方式

```
/distill-methods-exemplar <输入路径或文本> [--batch] [--design-filter=面板数据/DiD/实验/...] [--output-format=markdown/json]
```

**参数说明**：
- `<输入路径或文本>`（必填）: 论文文件路径、PDF 路径、粘贴文本、或包含多篇论文材料的目录
- `[--batch]`（可选）: 标记批量处理模式，输出跨论文模式聚合报告
- `[--design-filter]`（可选）: 只处理特定设计类型的论文
- `[--output-format]`（可选）: 默认 `markdown`，可选 `json` 供脚本消费

**如果省略输入**，进入交互式询问后执行蒸馏。

---

## Phase 0 — 论文类型与设计分类

在读取正文前，先判断这篇论文 Methods 的**设计范式**，决定后续槽位检查清单和蒸馏焦点。

### 分类维度

| 维度 | 选项 |
|------|------|
| 数据形态 | 面板数据 / 截面数据 / 实验 / 多研究 / 质性→量化 |
| 识别策略 | OLS/FE / 自然实验/DiD / IV/2SLS / RDD / 匹配 / 实验随机化 |
| 估计器 | 线性 / Logit/Probit / 生存分析 / 计数模型 / SEM / GMM / Tobit |
| 特殊结构 | 多行为者 / 网络效应 / 文本构念 / 堆叠扩散 / 同时方程 |
| 因果强度 | 描述性 / 预测性 / 因果识别（quasi-experimental）/ 实验因果 |

### 输出格式

```yaml
paper_id: "[作者_年份_期刊]"
phase_0_design_profile:
  data_architecture: "面板数据 / 截面 / 实验 / ..."
  identification_strategy: "OLS+FE / DiD / IV / ..."
  estimator_family: "线性 / 非线性 / 生存 / ..."
  special_structure: "无 / 匹配DiD / 文本构念 / ..."
  causal_ambition: "描述 / 预测 / 准实验因果 / 实验因果"
  methods_section_length: "[字数]"
  number_of_tables_referenced: "[N]"
```

---

## Phase 1 — Methods 文本读取与粗粒度解构

读取 Methods 全文，按叙事槽位目录（M1–M10）进行**粗粒度标注**。标注时只定位段落功能，不做深入分析。

### 槽位映射表（与 write-methods 对齐）

| 槽位 | 功能 | 粗粒度标注任务 |
|------|------|----------------|
| M1 | 研究情境 / 实证背景 | 定位 setting 段落，提取 3 个理由的论证结构 |
| M2 | 数据来源与样本漏斗 | 定位样本描述，标记起始 N → 每步排除 → 最终 N |
| M3 | 因变量操作化 | 定位 DV 定义段落，标记构念→操作化→来源→方向 |
| M4 | 自变量 / 核心预测变量 | 定位每预测变量段落，标记与假设的对应关系 |
| M5 | 调节/中介/机制变量 | 定位边界/机制变量，标记交互项说明 |
| M6 | 控制变量与竞争性解释 | 定位 controls 段落，标记每个变量的 because 逻辑 |
| M7 | 模型规格与估计方法 | 定位 estimator 段落，标记公式+文字+诊断 |
| M8 | 识别策略 / 效度 / 诊断检验 | 定位 identification 段落，标记假设+检验+位置 |
| M9 | 多研究 / 实验程序 | 如适用，标记研究间衔接结构 |
| M10 | Methods→Results 过渡（可选） | 定位 transition 段落，标记 Results 预告结构。顶刊实证论文中约 70% 缺失，若缺失不严重惩罚覆盖率 |

#### 跨槽位段落识别

实际范文中，部分段落同时覆盖多个槽位功能。标注时增加以下标签：

| 标签 | 示例 | 处理方式 |
|------|------|----------|
| `M1+M2 merged` | POMS Mayo2023 的 3.1 "Research Design and Data Sources" 同时论证 setting 合法性 + 报告数据来源 | 同时计入 M1 和 M2 的 present_slots，但标注 merged |
| `M3+M4 merged` | 某一段同时定义 DV 和核心预测变量 | 同时计入 M3 和 M4，记录 paragraph_range 为同一区间 |
| `M6+Table merged` | POMS 用表格呈现 controls，正文仅一句话总起 | M6 located=true，但标注 "table_bears_function" |
| `M7+M8 merged` | DiD/IV 设计中识别策略与模型规格在同一节 | 同时计入 M7 和 M8，标注 merged |

#### 非段落元素识别

Methods 中部分核心说服功能由**非段落文本**完成，不可遗漏：

| 元素类型 | 功能 | 典型位置 | 处理方式 |
|----------|------|----------|----------|
| `Table: variables` | 变量定义表（如 JM 2015 Malshe Table 1） | M3–M6 之间 | 记录表头列名逻辑，标记对应槽位 |
| `Table: model comparison` | 模型选择比较表（如 JM 2017 Eilert BIC 表） | M7 内部或之后 | 记录比较维度（distribution × BIC/AIC） |
| `Equation sequence` | 方程组（如 JMR 2023 Singh 2SLS 方程组） | M7 | 记录方程数量和呈现顺序 |
| `Figure: model-free` | 无模型证据图（如 JMR 2023 Singh 分组均值图） | M1/M7/M8 之前 | 标记为 Model-Free Evidence 前置 |
| `Subsection heading` | 子标题化 IV 论证（如 JMR 的 #### Instrument Relevance） | M4/M7 | 将子标题视为独立功能区块，分别标注槽位 |

### 输出格式

```yaml
phase_1_slot_map:
  M1:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    setting_claims: ["理由1", "理由2", "理由3"]
    cross_slot_note: "M1+M2 merged"  # 可选
  M2:
    located: true/false
    funnel_steps: ["起始", "排除1", "排除2", "最终"]
    has_numbers: true/false
    cross_slot_note: "M1+M2 merged"  # 可选
  # ... 其余槽位

phase_1_non_paragraph_elements:
  tables:
    - table_id: "Table 1"
      location: "between M3 and M4"
      function_slots: ["M3", "M4", "M6"]
      header_columns: ["Variable", "Purpose", "Equation", "Data Set", "Literature"]
    - table_id: "Table 4"
      location: "within M7"
      function_slots: ["M7"]
      header_columns: ["Distribution", "Log-Likelihood", "BIC"]
  equations:
    - equation_count: 5
      location: "M7"
      function_slots: ["M7"]
      sequence_note: "main outcome → mediator A → mediator B → downstream outcome → endogenous choice"
  figures:
    - figure_id: "Figure 6"
      location: "before M7"
      function_slots: ["M8"]
      type: "model-free evidence"
      content_note: "group mean comparison by lobbying intensity"
  subsections:
    - heading: "Instrument Relevance"
      location: "within M4"
      function_slots: ["M4"]
      parent_section: "Instrumental Variable Model"
```

---

## Phase 1.5 — 槽位覆盖检查与调研质量摘要

这是质量控制检查点。对照设计类型，检查 Methods 是否覆盖了该类设计**必须出现**的槽位。

### 设计类型强制槽位表

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

### 调研质量摘要输出

```yaml
phase_1_5_quality_gate:
  slot_coverage:
    required_slots: ["M1", "M2", ...]
    present_slots: ["M1", "M2", ...]
    missing_slots: ["M8"]
    coverage_rate: "80%"
    cross_slot_mergers_detected: ["M1+M2", "M6+Table"]
    non_paragraph_elements_count: 3
  special_design_markers:
    detected: ["IV", "匹配"]
    properly_addressed: ["M7 第一阶段"]
    inadequately_addressed: ["M8 排他性约束仅一句话"]
  source_sufficiency:
    sample_funnel_auditable: true/false
    # 注：若 M2 为 M1+M2 merged 或多源匹配型，sample_funnel_auditable 应为 true，但审计链可能简化
    diagnostic_tests_named: true/false
    robustness_location_specified: true/false
  contradictions_or_gaps: ["M7 声称用 FE 但未报告 Hausman", "M8 说检验在 Results 但 Results 未出现"]
  information_poverty_dimensions: ["未报告 VIF 值", "未说明标准误聚类层级"]
```

---

## Phase 2 — 深度提炼：段落功能、表达骨架、Validity Logic

对 Phase 1 定位到的每个槽位段落，执行三重提炼。

### 2.1 段落功能提炼

回答：这个段落完成了什么**说服动作**？

| 说服动作 | 示例 |
|----------|------|
| 合法性论证 | Setting 段落论证"为什么这个情境适合检验理论" |
| 可审计性 | 样本漏斗让审稿人可以复现样本选择 |
| 对齐性 | 变量操作化段落建立构念→假设→测量的映射 |
| 抗辩性 | Controls 段落预判竞争性解释并提前排除 |
| 可信性 | 识别策略段落让审稿人相信因果推断成立 |
| 导航性 | M10 段落预告 Results 的阅读顺序 |

### 2.2 表达骨架提炼（Expression Skeleton）

将具体措辞抽象为**可填充的句法结构**。这是最关键的输出。

**骨架格式**：
```text
[功能标签]: 论证 setting 合法性
[骨架]: [Empirical setting] provides an appropriate context for examining [theoretical relationship] for [N] reasons. First, [setting property] makes [mechanism] observable. Second, [scope condition] reduces [confound]. Third, [data feature] allows us to observe [unit/process] over [period].
[可迁移性]: 高 — 出现在 12/28 篇范文中
[范式排他性]: 通用 setting 论证，不绑定特定设计
[设计变体]: DiD 版本替换首句为政策冲击描述；实验版本替换为"We test X using a Y experiment"
```

**必须记录的信息**：
- 骨架句法（用方括号标记占位符）
- 可迁移性评分（高/中/低）及证据（出现频次）
- 范式排他性（该骨架是否只为某类设计所需）
- 设计变体（同类骨架在不同设计中的改写模式）

### 2.3 Validity Logic 提炼

提取该 Methods 如何处理三类 validity threat：

| Threat 类型 | 提炼问题 |
|-------------|----------|
| 内部效度 | 如何排除 omitted variable / reverse causality / simultaneity？识别策略是什么？ |
| 构造效度 | 如何论证 measure 捕捉了 construct？是否有效度检验链？ |
| 外部效度 | Setting 的 boundary 在哪里？是否讨论 generalizability 限制？ |

输出格式：
```yaml
phase_2_distillation:
  M1_setting:
    persuasive_action: "合法性论证"
    expression_skeletons:
      - skeleton: "..."
        transferability: "高 (12/28)"
        paradigm_exclusivity: "通用"
        design_variants: ["DiD variant", "Experiment variant"]
    validity_logic:
      internal: "..."
      construct: "..."
      external: "..."
  # ... 其余槽位
```

---

### 2.6 句法微模板提取（Sentence-Level Micro-Templates）

在段落级骨架（Phase 2.2）之下，进一步提取**句子级/句法微模板**。这是解决"段落结构正确但表达同质化"问题的关键层。

**提取原则**：
- **How within How**：不是"这个段落做什么"，而是"这个段落内的关键句如何完成说服"。
- **可替换性**：同一骨架的同一槽位，应能填入多套微模板，生成风格迥异的段落。
- **功能绑定**：微模板必须与骨架的说服动作绑定，不能脱离骨架功能独立使用。

**提取流程**：

1. **定位关键句法位置**：在 Phase 2.2 的骨架中，标记以下关键句法位置：
   - 段首锚定（Opening Anchor）
   - because 从句（Because Clause）
   - 因果动词（Causal Verb）
   - 过渡衔接（Transition）
   - 数字叙事节奏（Numerical Rhythm）

2. **提取微模板**：将原文中这些位置的句法抽象为可填充单元。

3. **分类归档**：按功能分类存入 `academic-writing-corpus/micro-templates/` 的对应文件。

**六大微模板类别**：

| 类别 | 功能 | 存储位置 | 对应槽位 |
|------|------|---------|---------|
| **段首锚定短语** | 告诉读者"本段做什么" | `micro-templates/opening-anchors.md` | M1–M10 |
| **because 从句架构** | 论证控制变量/样本排除/构念效度的理由 | `micro-templates/because-clauses.md` | M2, M3, M4, M6 |
| **因果动词梯度** | 根据设计强度选择因果声称力度 | `micro-templates/causal-hedging.md` | M3, M4, M7, M8 |
| **过渡衔接短语** | 段落内部的逻辑推进标记 | `micro-templates/transitions.md` | M1–M10 |
| **样本漏斗节奏** | 数字叙事的句法序列 | `micro-templates/funnel-rhythm.md` | M2 |
| **识别策略预告** | 在 Methods 中预告 Results 的诊断检验 | `micro-templates/identification-foreshadowing.md` | M8 |
| **变量操作化句式** | 构念→测量→来源→方向 | `micro-templates/variable-operationalization.md` | M3, M4, M5 |
| **稳健性检验预告** | 预告 Results 的稳健性检验 | `micro-templates/robustness-foreshadowing.md` | M8, M10 |

**微模板格式**：

```yaml
phase_2_6_micro_templates:
  M6_controls:
    opening_anchor:
      template: "We included a broad set of control variables that influence [DV] directly and those that help address alternative explanations ([methodology_citation])."
      frequency: "中 (4/28)"
      transferability: "通用"
      risk_level: "安全"
    because_clauses:
      - template: "...because [larger and older firms] may have more resources for both [IV] and [DV]."
        subtype: "竞争性解释型"
        frequency: "高"
      - template: "...because [omitted variable] may confound the [IV-DV] relationship by [mechanism]."
        subtype: "遗漏变量型"
        frequency: "中"
    transitions:
      - template: "We first included [level_1]_level factors..."
        function: "层级递进"
      - template: "We also controlled for [level_2]_level characteristics..."
        function: "层级递进"
      - template: "Lastly, we included firm and year fixed effects..."
        function: "层级收尾"
```

**与 write-methods 的接口**：

`write-methods` 输出段落骨架时，在 `[placeholder]` 层级之下，为关键句法位置提供 2–3 个微模板选项供用户选择。例如：

```text
M6. 控制变量与竞争性解释

[段首锚定选项]：
  A. "We include controls for [threat family] because [alternative explanation]."（通用）
  B. "We included a broad set of control variables that influence [DV] directly and those that help address alternative explanations ([citation])."（because 密度高）

[because 从句选项]：
  A. 竞争性解释型: "...because [rival theory] predicts..."
  B. 遗漏变量型: "...because [omitted variable] may confound..."

骨架主体: [We began with... → After excluding... → The final sample...]
```

**诚实边界**：
- 不提取不可迁移的论文特定短语（机构名、政策名、数据库名）。
- 不虚构微模板的来源频次。
- 高风险微模板（强因果动词）必须标注设计类型限制。

---

### 2.4 骨架批评家（Skeleton Critic）—— 生成力验证

每个 Phase 2.2 提炼出的骨架必须经过**生成力验证**，才能进入 Phase 3 和后续语料库沉淀。

**验证流程**：

1. **占位符填充测试（Generativity Test）**
   - 将骨架中的 `[占位符]` 填入该论文的具体内容（变量名、样本量、估计器名）
   - 生成一个"模拟段落"
   - 对比模拟段落与原文段落：是否保留了相同的**说服动作**？
   - 如果填入后生成的段落与原文功能等价 → 通过；如果丢失了关键说服动作 → REVISE

2. **事实污染检查（Fact-Boundary Test）**
   - 骨架中是否嵌入了该论文特有的机构名、政策名、数据库名？
   - 是否使用了仅适用于该行业的术语？
   - 如果有 → REVISE，泛化为 `[empirical setting]` / `[policy]` / `[source]`

3. **设计类型匹配检查（Type-Fidelity Test）**
   - 骨架的标志性语言是否与判定的设计类型匹配？
   - 例如：OLS/FE 骨架中出现 "parallel trends" → REJECT（语言错配）
   - 例如：非 IV 骨架中出现 "exclusion restriction" → REJECT
   - 因果语言强度是否与设计家族的允许词汇表一致？

**批评家裁决格式**：

```yaml
phase_2_4_skeleton_critic:
  skeleton_id: "M7_survival_aft_distribution_selection"
  verdict: "VALIDATED / REVISE / REJECT"
  verdict_reason: "..."
  generativity_test:
    mock_paragraph_generated: true/false
    persuasive_action_preserved: true/false
    notes: "..."
  fact_boundary_test:
    paper_specific_contamination: ["数据库A", "机构B"]
    contamination_cleared: true/false
  type_fidelity_test:
    design_type_match: true/false
    causal_language_compliant: true/false
    mismatch_details: "..."
```

**裁决标准**：

| 裁决 | 条件 | 后续动作 |
|------|------|----------|
| **VALIDATED** | 三项测试全部通过 | 骨架进入 Phase 3 和 Phase 4 |
| **REVISE** | 生成力或事实边界测试未通过，但可通过改写修复 | 标记为 "needs_revision"，在 Phase 4 中尝试改写后重新验证 |
| **REJECT** | 设计类型错配，或过度抽象失去生成力 | 丢弃，不进入语料库。记录拒绝原因供 Phase 4 汇总 |

**注意**：批评家裁决记录存入 Phase 4 的 `validated_skeletons` 或 `rejected_skeletons`，供跨论文聚合使用。


## Phase 3 — Academic Methods DNA 量化与结构化报告

量化该论文 Methods 的"表达 DNA"，生成 fine-grained profile。

### Methods DNA 指标

| 指标 | 计算方式 | 用途 |
|------|----------|------|
| 段落平均句数 | 每段句子数 / 段数 | 判断该期刊/设计的 Methods 密度 |
| 每段是否先定位功能 | 段首句是否说明"本段做什么" | 判断导航性 |
| 假设对齐密度 | 变量段落中提及 Hypothesis 编号的比例 | 判断 Theory-Methods 耦合度 |
| because 密度 | 控制变量/样本排除中 "because" 或等效词的比例 | 判断抗辩性。MVP30 顶刊中位数约 35%，>=60% 为优秀，<30% 需关注 |
| 因果语言强度 | "effect of" / "impact on" / "associated with" / "leads to" 的分布 | 判断 causal ambition 与 design strength 是否匹配 |
| 诊断检验前置比例 | 诊断检验是在 M7 说明还是在 Results 才出现 | 判断 ritual 规范性 |
| 样本数字审计链 | 起始→中间→最终 N 是否完整 | 判断可审计性 |
| 滞后/时点标记密度 | t-1 / contemporaneous / event window 的明确度 | 判断时间逻辑清晰度 |

### 结构化报告输出（fine_grained profile）

```markdown
# Fine-Grained Profile: [作者_年份_期刊]

## Paper Identity
- 设计分类: [来自 Phase 0]
- 期刊/领域: [journal]
- Methods 字数: [N]
- 与 write-methods 模板对齐度: [高/中/低]

## Slot Coverage (M1–M10)
[Phase 1.5 输出]

## Distilled Skeletons
### M1 — 研究情境
[来自 Phase 2.2 的骨架列表]

### M2 — 样本漏斗
...

## Methods DNA
[来自 Phase 3 的量化指标]

## Validity Logic Map
[来自 Phase 2.3]

## Novel Patterns（与现有 28 篇语料库对比后的新发现）
- 新骨架: ...
- 新设计变体: ...
- 新 validity threat 处理: ...

## Non-Transferable Facts
[仅适用于该论文的特定事实，不可迁移]

## Corpus Reference Notes
[供人工审阅的语料库沉淀注释，不自动修改 write-methods skill]
```

---

## Phase 4 — 跨论文模式验证与语料库沉淀建议

如果是 `--batch` 模式，在多篇论文提炼完成后执行此阶段。

### 三重验证标准

| 标准 | 问题 | 淘汰门槛 |
|------|------|----------|
| **跨论文复现** | 这个写法是否在多个顶刊范文中出现？ | 只出现 1 次的骨架降级为 "optional variant" |
| **生成力** | 它能不能指导一篇新论文写出段落？ | 无法填入占位符生成段落的骨架丢弃 |
| **范式排他性** | 它是不是某类方法场景特别需要？ | 所有设计都通用的"废话骨架"（如"Data is important"）丢弃 |

### 语料库沉淀建议格式

```yaml
phase_4_corpus_reference:
  vault_enrichment:
    new_skeletons_for_reference:
      - slot: "M7"
        design_type: "堆叠扩散Logit"
        skeleton: "..."
        source_papers: ["作者_年份", "作者_年份"]
        vault_path: "fine_grained/batch_N/skeletons/"
        note: "供写作者参考，不自动写入 skill"
    patterns_to_note:
      - slot: "M8"
        design_type: "匹配DiD"
        observation: "3/5 篇匹配DiD 都报告了 common support 百分比"
        note: "可作为 Vault 注释，供人工判断是否纳入 skill 参考"
    new_anti_patterns:
      - pattern: "Bad control in DiD: controlling for post-treatment outcome determinants"
        evidence: "出现在 2 篇被审稿人质疑的论文中"
    new_honesty_boundary:
      - boundary: "本 skill 不能为动态面板推荐固定效应而不提示 Nickell bias"
        source: "语料库中 3 篇 GMM 论文都在 M7 明确提及此问题"
  batch_metadata:
    total_papers_processed: 10
    design_type_distribution: {"DiD": 4, "OLS/FE": 3, "实验": 2, "IV": 1}
    novel_skeletons_found: 5
    rejected_skeletons: 3
    rejected_reasons: ["仅出现1次", "不可生成段落", "通用废话"]
```

**关键原则**：Phase 4 的产出分为两层：
- **机器消费层**（硬化接口）：包含骨架文本的 `corpus_enrichment` YAML 块由 `_update_registry.py` **自动**处理，同时更新注册表和追加变体到语料库分片文件。
- **人工消费层**：仅含参考注释的 `vault_enrichment` 存入 Vault 的 `skill_update_recommendations/` 或 `fine_grained/` 目录，供人工审阅后决定是否纳入 skill。

Distill skill **自动修改** `write-methods` 的语料库分片文件（通过 `_update_registry.py`），但**不自动修改** SKILL.md 本身的协议层文本。

### 自动沉淀路径：→ academic-writing-corpus（由 _update_registry.py 执行）

验证通过的变体骨架通过 `corpus_enrichment` YAML 的 `append_skeleton` action **自动**追加到 `write-methods/academic-writing-corpus/[设计类型].md` 的「累积变体」区块。

**无需手动编辑**。`_update_registry.py` 会自动完成：
- [x] 读取目标分片文件
- [x] 在「累积变体」区块追加新变体（含骨架、来源论文、验证状态）
- [x] 更新文件头 `variants_count` 和 `updated` 字段
- [x] 同时更新 `_evidence_registry.yaml` 的定量证据

**`evidence_updates` 中触发骨架追加的条件**：
- `action: "append_skeleton"`（推荐，显式标记骨架更新）
- `action: "create_new"` 且包含 `skeleton` 字段（新建设计类型时自动创建骨架）

**手动审阅仍需要的场景**（不通过脚本自动处理）：
- 将累积变体**提升为主骨架**或标记为 `✓ STANDARD`
- 修改主骨架的定性内容（句法模板、设计变体、反模式提醒等）
- 删除或修改已写入的累积变体

---

### Phase 4.5 — 证据注册表更新逻辑与 corpus_enrichment 硬化输出

Phase 4 的产出分为两层：
- **人工消费层**： 和 （Vault 参考注释，供人工审阅后决定是否纳入 skill）
- **机器消费层**： 结构化 YAML 块（自动更新  的定量证据）

#### corpus_enrichment 硬化输出块

在 Phase 4 输出末尾，**必须附加**以下结构化 YAML 块。这是 distill 与 write-methods 之间的**硬化接口**——write-methods 可通过注册表直接感知每个设计类型的证据积累状态。

```yaml
corpus_enrichment:
  batch_id: "batch_YYYY-MM-DD"
  papers_processed: N
  last_updated: "YYYY-MM-DD"

  evidence_updates:
    - target: "academic-writing-corpus/生存分析.md"
      design_type: "生存分析"
      slot: "M7"
      action: "append_papers"
      new_papers: ["author_year (journal)"]
      updated_paper_count: N
      new_status: "ROBUST / VERIFIED / EMERGING"

    - target: "academic-writing-corpus/面板数据-OLS.md"
      design_type: "面板数据-OLS"
      slot: "M6"
      action: "update_status"
      previous_status: "VERIFIED"
      new_status: "ROBUST"
      reason: "paper_count 从 4 升至 6，跨 >=2 sources"

    - target: "academic-writing-corpus/XX-new-design.md"
      design_type: "新设计类型"
      slot: "M7"
      action: "create_new"
      skeleton: "Because [DV] is [type], we estimate..."
      source_papers: ["author_year"]
      transferability: "high"
      note: "供写作者参考，可作为新增设计类型 corpus 文件的候选"

  anti_pattern_updates:
    - target_design_type: "面板数据-OLS"
      target_slot: "M6"
      pattern: "控制变量无 because 逻辑——3/8 OLS/FE 论文控制变量仅列举名称"
      evidence: ["paper_a", "paper_b", "paper_c"]
      recommended_action: "在 write-methods M6 模板中强化 '每个控制变量必须有 because' 的提醒"

  validation_feedback:
    - design_type: "生存分析"
      phase_6_validations: 0
      note: "尚无 Phase 6 验证数据"

  batch_metadata:
    design_types_covered: ["面板数据-OLS", "生存分析", "IV-2SLS"]
    novel_skeletons_found: N
    rejected_skeletons: N
    rejected_reasons: ["仅出现1次", "设计类型错配", "因果语言越级", "过度抽象"]
```

**字段说明**：

| 字段 | 用途 | 消费方 |
|------|------|--------|
|  | 对现有 corpus 文件的证据更新（新增论文、状态升级、新建设计类型文件） | write-methods 加载时合并到  |
|  | 批量蒸馏发现的常见失败模式 | write-methods 反模式清单 |
|  | Phase 6 验证结果积累 |  validation_history |
|  | 批量处理元数据 | 注册表 meta 字段 |

#### 状态自动判定规则

| 条件 | 新状态 |
|------|--------|
|  且跨  独立数据源/期刊 | **ROBUST** |
|  | **VERIFIED** |
|  | **EMERGING** |

#### 注册表更新方式

1. 将 Phase 4 输出的  YAML 块保存为临时文件
2. 运行本 skill 目录下的自动化工具：
   ```bash
   python _update_registry.py /tmp/corpus_enrichment.yaml
   ```
3. 工具自动完成：
   - 读取 
   - 对每个  条目：追加 papers、重算 paper_count、按阈值判定 status
   - 应用 
   - 更新  和 
   - 写回注册表

**工具位置**: 

**注意**：Phase 4.5 的 `_update_registry.py` 执行两项自动更新：
1. **注册表更新**：`_evidence_registry.yaml` 中的定量证据（paper_count、status、common_failures）。
2. **语料库骨架追加**：包含 `skeleton` 字段的 `evidence_updates` 条目会自动追加到目标分片文件的「累积变体」区块。

主骨架的定性内容（句法模板、设计变体、反模式提醒等）仍需人工审阅后手动更新；累积变体的追加已自动化。

**与 Vault 注释的关系**： 块是**机器消费**的结构化输出；Phase 4 原有的  和  等 YAML 是**人工消费**的参考注释。两者并行产出，不互相替代。

---

## Phase 5 — 质量验证与 QC 输出

生成最终的蒸馏质量报告，确保产出物可以安全进入 Vault 和 Skill 更新流程。

### QC Checklist

- [ ] **Completeness**: 所有强制槽位（根据设计类型）已被覆盖
- [ ] **Clarity**: 每个骨架都有明确的 [占位符] 和插入位置
- [ ] **Credibility**: 未将单篇论文的特殊做法泛化为通用规则
- [ ] **Replicability**: 骨架填入具体信息后，能生成类似顶刊风格的段落
- [ ] **No Verbatim Copy**: 输出中未出现可直接追溯到原文的连续 8+ 词短语
- [ ] **Fact Boundary**: 所有不可迁移事实已被明确标记
- [ ] **Causal Language Audit**: 提取的骨架中因果语言强度与设计类型匹配

### 最终输出物清单

1. **Fine-Grained Profile**（单篇）或 **Batch Aggregation Report**（批量）
2. **Expression Skeleton Corpus**（新增骨架列表）
3. **Validity Logic Map**（该设计类型的 threat 处理模式）
4. **Methods DNA Metrics**（可对比的量化指标）
5. **Corpus Reference Notes**（供人工审阅的语料库沉淀注释，不自动修改 skill）
6. **QC Result**（通过/需修正/拒绝入库）

---

## Phase 6 — 成品验证模式（Product Validation Mode）

本阶段是 **write-methods → 用户写作 → distill 成品验证** 闭环的核心。用户在 write-methods 输出段落骨架并完成写作后，将写出的 Methods 回传给本 skill 进行验证。

### 调用方式

```
/distill-methods-exemplar --validate <用户写出的Methods全文> --reference-metadata <write-methods输出的metadata JSON> [--output-format=markdown/json]
```

**参数说明**：
- `--validate`（必填）: 标记进入成品验证模式（区别于默认的范文蒸馏模式）
- `<用户写出的Methods全文>`（必填）: 用户根据 write-methods 段落骨架写出的 Methods
- `--reference-metadata`（必填）: write-methods 输出末尾的 `---metadata---` JSON 区块
- `--output-format`（可选）: 默认 `markdown`，可选 `json` 供脚本消费

**如果没有提供 `--reference-metadata`**：进入简化验证模式，仅执行通用 Methods QC（不检查与组装方案的对齐）。

### 验证框架：四维检查

```
┌─────────────────────────────────────────────────────────────┐
│  维度1: 组装方案兑现 (Assembly Fidelity)                      │
│  维度2: 槽位完整性 (Slot Completeness)                        │
│  维度3: 因果语言合规 (Causal Language Compliance)              │
│  维度4: 骨架生成力 (Skeleton Generativity)                    │
└─────────────────────────────────────────────────────────────┘
```

---

#### 维度1 — 组装方案兑现检查（Assembly Fidelity）

将用户写出的 Methods 与 write-methods 的 metadata slot_map 逐槽位对比，检查：

| 检查项 | 问题 | 通过标准 | 失败信号 |
|--------|------|---------|---------|
| **槽位覆盖** | 用户是否覆盖了推荐槽位？ | >=80% 的推荐槽位有对应段落 | 多个强制槽位完全缺失 |
| **设计变体偏离** | 用户是否使用了推荐以外的设计变体？ | 新增变体与设计类型兼容 | 如 OLS 中混入 DiD 平行趋势语言 |
| **控制变量 because 覆盖** | M6 中每个控制变量是否有 because 逻辑？ | >=60% 控制变量有 because（顶刊优秀线） | <30% 控制变量仅有名称列举 |
| **样本漏斗完整性** | M2 的起始 N→排除→最终 N 是否完整？ | 每步有数字和理由 | 跳步或缺失数字 |

**偏离度矩阵输出格式**：

```markdown
### 组装方案偏离矩阵

| 槽位 | 推荐状态 | 实际内容 | 偏离类型 | 严重度 | 建议 |
|------|---------|---------|---------|--------|------|
| M1 | 推荐保留 | 缺失 | 槽位缺失 | 低（AMJ 30%可省略） | 如 Introduction 已覆盖 setting，可省略 |
| M7 | DiD 变体 | 使用了 OLS 语言 | 设计变体替换 | 高 | 加入平行趋势检验段落和事件研究设定 |
| M6 | 至少5个带because的control | 仅列举变量名 | because 缺失 | 高 | 每个控制变量补充 because [竞争性解释] |
```

---

#### 维度2 — 槽位完整性检查（Slot Completeness）

基于 Phase 1.5 的强制槽位表，逐槽位检查 completeness、clarity、credibility：

| 检查项 | 对应槽位 | 验证问题 | 失败后果 |
|--------|---------|---------|---------|
| **Setting 合法性** | M1 | Setting 是否论证了"为什么这个情境适合检验理论"？ | 审稿人质疑 external validity |
| **样本可审计性** | M2 | 起始 N → 每步排除（理由+数字）→ 最终 N？ | 审稿人无法复现样本选择 |
| **构念-操作化对齐** | M3/M4 | 变量操作化是否与 Theory 构念一致？ | 构念效度被质疑 |
| **控制逻辑完整性** | M6 | 每个控制变量对应一个竞争性解释？ | omitted variable concern |
| **估计器选择理由** | M7 | 为什么选此 estimator 而不是替代方案？ | 审稿人要求更换估计器 |
| **识别策略充分性** | M8 | 关键识别假设是否有检验方法预告？ | 因果推断不被信任 |
| **结果预告准确性** | M10 | Results 预告是否与假设一一对应？ | Introduction→Results 断裂 |

**槽位评分卡**：

```yaml
slot_completeness:
  M1: {score: N, max: 3, note: "..."}
  M2: {score: N, max: 3, note: "..."}
  M3: {score: N, max: 3, note: "..."}
  M4: {score: N, max: 3, note: "..."}
  M5: {score: N, max: 3, note: "..."}
  M6: {score: N, max: 3, note: "..."}
  M7: {score: N, max: 3, note: "..."}
  M8: {score: N, max: 3, note: "..."}
  M10: {score: N, max: 3, note: "..."}
  overall_completeness_rate: "X%"
```

---

#### 维度3 — 因果语言合规检查（Causal Language Compliance）

基于 write-methods 的因果语言强制词汇表，逐句检查 Methods 中的因果动词是否与设计强度匹配：

| 设计家族 | 允许动词 | 禁止动词 | 违规后果 |
|---------|---------|---------|---------|
| 面板数据/OLS/FE | associated with, related to, linked to | increases, decreases, leads to, causes, drives | 审稿人质疑 causal overclaim |
| DiD/自然实验 | effect of...on...（仅平行趋势支持后）, associated with | causes, leads to（无条件禁止） | 平行趋势检验未通过时用"effect"被审稿人攻击 |
| IV/2SLS | effect of...on..., increases, decreases | causes, leads to, produces | second-stage 可"effect"但避免"causes" |
| 非线性模型 | associated with, increases the likelihood of, changes the probability of | increases, decreases, causes | 系数不可直接解释 |
| 生存分析 | associated with, lengthens/shortens time to, changes the hazard of | causes, leads to | hazard ratio 需转述 |
| 实验 | caused, led to, produced, increased, decreased | — | 随机化支持后可直接使用 |

**违规记录格式**：

```markdown
### 因果语言违规清单

| 位置 | 违规表述 | 设计类型 | 违规类型 | 严重度 | 建议替换 |
|------|---------|---------|---------|--------|---------|
| M7 第3句 | "DT increases innovation" | OLS/FE | 强因果词 | 高 | "DT is associated with higher innovation" |
| M8 第2句 | "This effect of..." | DiD（平行趋势未在Methods预告） | 越级 | 中 | 将"effect"改为"relationship"或将平行趋势预告前置 |
```

---

#### 维度4 — 骨架生成力验证（Skeleton Generativity）

验证 write-methods 推荐的骨架在用户实际写作中是否保留了说服动作：

1. **骨架匹配**：将用户写出的段落与推荐槽位的骨架对比，标记关键功能短语是否保留

2. **说服动作保留检查**：原始骨架的说服动作是什么？（合法性论证 / 可审计性 / 抗辩性 / ...）用户填充后的段落是否完成了相同的说服动作？

3. **过度填充检查**：用户是否在骨架中塞入了过多领域细节导致骨架变形？是否存在"骨架膨胀"（一个槽位的功能被稀释到多个段落）？

4. **设计类型 fidelity 检查**：用户填充后的标志性语言是否与原始推荐的设计类型匹配？

**生成力验证报告格式**：

```markdown
### 骨架生成力验证

| 槽位 | 推荐变体 | 骨架关键短语保留 | 说服动作保留 | 过度填充风险 | 生成力评级 |
|------|---------|----------------|-------------|-------------|-----------|
| M2 | DiD变体 | "Our primary sample consists of..." ✓ | 可审计性 ✓ | 低 | VALIDATED |
| M6 | 通用 | "because [rival explanation]" ⚠️ 仅2/5变量保留 | 抗辩性减弱 | 中 | REVISE |
| M7 | 生存分析 | "We use an accelerated failure time metric..." ✗ 未出现 | 可信性 ✗ | 高 | REJECT |
```

---

### 综合验证报告输出

```markdown
# Methods 成品验证报告

## 基本信息
- **验证模式**: Product Validation（基于 write-methods metadata）
- **参考设计类型**: DiD/自然实验
- **实际段落数**: 8（推荐 8-10，偏差 0）
- **总字数**: 650

## 四维评分卡

| 维度 | 得分 | 满分 | 评级 | 关键发现 |
|------|------|------|------|---------|
| 组装方案兑现 | 75% | 100% | △ | M7 使用了 OLS 语言而非 DiD 变体 |
| 槽位完整性 | 85% | 100% | ✓ | M6 控制变量 because 密度仅 40%（目标 60%） |
| 因果语言合规 | 90% | 100% | ✓ | 1 处 OLS 语言越级 |
| 骨架生成力 | 6 VALIDATED / 1 REVISE / 1 REJECT | — | △ | M7 骨架失效 |
| **综合评级** | — | — | **CONDITIONALLY ACCEPT** | 需修正后重新验证 |

## 优先修正清单（按审稿人攻击概率排序）

1. **[高] M7 设计变体错配**: 推荐 DiD 变体但使用了通用 OLS 语言
   - 当前：未包含平行趋势检验预告、未指定处理/对照分组
   - 建议：替换为 DiD 变体骨架，加入 "Identification comes from comparing changes in [treated units]..."
   - 若不修正：审稿人质疑因果识别策略

2. **[高] M6 because 密度不足**: 仅 2/5 控制变量有 because 逻辑
   - 建议：为每个控制变量补充 because [竞争性解释]
   - 若不修正：审稿人质疑 "why these controls?"

3. **[中] M7 因果语言**: 1 处 "leads to" 违规
   - 建议：替换为 "is associated with"
```

---

### Phase 6 的两层定位

| 层级 | 触发 | 产出 | 数据流向 | 目的 |
|------|------|------|---------|------|
| **即时 QC** | 每次 `--validate` | 四维评分 + 优先修正清单 | 直接给用户 | 写作辅助——发现槽位缺失、因果语言违规、because 不足 |
| **周期性汇总** | 每 10+ 次验证后人工检查 | `common_revise_reasons` 模式识别 | 手动更新注册表 common_failures | 语料库维护——发现哪些槽位模板在真实使用中反复出问题 |

**即时 QC 是现在就能用的东西。** 周期性汇总需要跨论文、跨用户的累积数据。

---

## 诚实边界

本 skill 必须 not：
- **复制原文**：不提取连续 8+ 词的原文短语进入骨架。骨架必须是句法抽象。
- **虚构复现性**：不声称某骨架"出现在多篇论文中"除非确实有证据。
- **泛化特殊设计**：不把 IV 的语言习惯套用到 OLS，不把实验的操纵检验套用到档案数据。
- **虚构统计量**：不编造样本量、VIF 值、F 统计量来填充骨架。
- **跳过 validity threat**：即使原文处理得很弱，也要如实记录，不能为了让骨架"好看"而美化。
- **强制覆盖所有槽位**：如果某论文 Methods 确实缺失某槽位，记录为 missing，不捏造。

---

## 反模式（蒸馏过程中主动排查）

| 反模式 | 表现 | 处理方式 |
|--------|------|----------|
| **原文依赖型骨架** | 骨架中包含论文特有的机构名、政策名、数据库名 | 泛化为 [empirical setting] / [policy] / [source] |
| **过度抽象** | 骨架抽象到只剩 "We measure X"，失去组织证据的启示 | 保留关键功能短语（"for three reasons" / "because"） |
| **因果语言越级** | 将原文中 design strength 不支持的 causal 表述原样保留 | 在骨架中降级为 "associated with" 或按设计类型标注允许的 causal 强度 |
| **忽略非显著/缺失** | 只提取"写得好的"部分，忽略原文 Methods 的薄弱点 | 在 Validity Logic 和 QC 中明确记录薄弱点 |
| **批量同质化** | 批量处理时忽视设计差异，用同一套骨架覆盖不同设计 | Phase 0 分类必须先行，不同设计类型分桶处理 |

---

## 与下游 Skill 的接口

- **`write-methods`** — 两层接口：(1) Phase 4 `corpus_enrichment` YAML 块 → Phase 4.5 → `_evidence_registry.yaml`（自动更新定量证据）；(2) Phase 4 `vault_enrichment` → Vault（人工审阅后更新 corpus 定性内容）。Phase 6 即时 QC 接收 write-methods 的 metadata JSON 作为参考基准，输出四维评分和修正建议
- **`methods-review`** — Phase 1.5 的槽位覆盖检查可作为 methods-review 的预检清单
- **`paper-review`** — Validity Logic Map 可用于跨 section 对齐检查
- **Vault** — Fine-Grained Profile 存入 Vault 的 `fine_grained/batch_*/[paper]_distilled_methods.md`；Phase 6 验证报告存入 `fine_grained/validation_runs/`

## 外部资产位置

- **现有语料库索引**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/_mvp30_methods_results_index.md`
- **现有 28 篇覆盖矩阵**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/deep_distillation/_methods_results_28_paper_coverage_matrix.md`
- **蒸馏产出存放**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/fine_grained/batch_*/[paper]_distilled_methods.md`
- **更新建议存放**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/skill_update_recommendations/`

## JSON Output Schema

当使用 `--output-format=json` 时，输出严格符合以下 schema，确保脚本可消费。

```json
{
  "$schema": "distill-methods-exemplar-batch/v2",
  "paper_id": "string",
  "phase_0_design_profile": {
    "data_architecture": "string",
    "identification_strategy": "string",
    "estimator_family": "string",
    "special_structure": "string",
    "causal_ambition": "string",
    "methods_section_length": "number",
    "number_of_tables_referenced": "number"
  },
  "phase_1_slot_map": {
    "M1": { "located": "boolean", "paragraph_range": "string", "setting_claims": ["string"] },
    "M2": { "located": "boolean", "funnel_steps": ["string"], "has_numbers": "boolean" },
    "M3": { "located": "boolean", "dv_construct": "string", "operationalization": "string" },
    "M4": { "located": "boolean", "predictors": [{ "name": "string", "hypothesis_link": "string" }] },
    "M5": { "located": "boolean", "moderators": ["string"], "mediators": ["string"] },
    "M6": { "located": "boolean", "controls_with_because": "boolean" },
    "M7": { "located": "boolean", "estimator_named": "boolean", "diagnostics_named": "boolean" },
    "M8": { "located": "boolean", "identification_assumption": "string", "test_location": "string" },
    "M9": { "located": "boolean", "study_count": "number" },
    "M10": { "located": "boolean", "results_preview": "string" }
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
      "sample_funnel_auditable": "boolean",
      "diagnostic_tests_named": "boolean",
      "robustness_location_specified": "boolean"
    },
    "contradictions_or_gaps": ["string"],
    "information_poverty_dimensions": ["string"]
  },
  "phase_2_distillation": {
    "M1": {
      "persuasive_action": "string",
      "expression_skeletons": [
        {
          "skeleton": "string",
          "transferability": "string",
          "paradigm_exclusivity": "string",
          "design_variants": ["string"]
        }
      ],
      "validity_logic": { "internal": "string", "construct": "string", "external": "string" }
    }
  },
  "phase_2_4_skeleton_critic": {
    "skeleton_id": "string",
    "verdict": "VALIDATED / REVISE / REJECT",
    "verdict_reason": "string",
    "generativity_test": { "mock_paragraph_generated": "boolean", "persuasive_action_preserved": "boolean", "notes": "string" },
    "fact_boundary_test": { "paper_specific_contamination": ["string"], "contamination_cleared": "boolean" },
    "type_fidelity_test": { "design_type_match": "boolean", "causal_language_compliant": "boolean", "mismatch_details": "string" }
  },
  "phase_3": {
    "avg_sentences_per_paragraph": "number",
    "function_positioning_rate": "number",
    "hypothesis_alignment_density": "number",
    "because_density": "number",
    "causal_language_strength": "string",
    "diagnostic_foreshadowing_rate": "number",
    "sample_funnel_completeness": "boolean",
    "temporal_clarity_density": "number"
  },
  "phase_4_corpus_reference": {
    "vault_enrichment": {
      "new_skeletons_for_reference": [
        { "slot": "string", "design_type": "string", "skeleton": "string", "source_papers": ["string"], "vault_path": "string", "note": "string" }
      ],
      "patterns_to_note": [
        { "slot": "string", "design_type": "string", "observation": "string", "note": "string" }
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
      "design_type_distribution": "object",
      "novel_skeletons_found": "number",
      "rejected_skeletons": "number",
      "rejected_reasons": ["string"]
    }
  },
  "phase_4_5_corpus_enrichment": {
    "batch_id": "string",
    "papers_processed": "number",
    "last_updated": "string",
    "evidence_updates": [
      {
        "target": "string",
        "design_type": "string",
        "slot": "string",
        "action": "append_papers / update_status / create_new",
        "new_papers": ["string"],
        "updated_paper_count": "number",
        "new_status": "ROBUST / VERIFIED / EMERGING"
      }
    ],
    "anti_pattern_updates": [
      {
        "target_design_type": "string",
        "target_slot": "string",
        "pattern": "string",
        "evidence": ["string"],
        "recommended_action": "string"
      }
    ],
    "batch_metadata": {
      "design_types_covered": ["string"],
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
    "overall_status": "PASS / FLAG / REJECT"
  },
  "phase_6_validation": {
    "validation_mode": "product_validation",
    "reference_metadata": { "description": "write-methods 输出的 ---metadata--- JSON 区块" },
    "assembly_fidelity": {
      "slot_coverage_rate": "number",
      "deviations": [
        { "slot": "string", "recommended": "string", "actual": "string", "deviation_type": "string", "severity": "string" }
      ]
    },
    "slot_completeness": {
      "overall_completeness_rate": "string",
      "per_slot_scores": { "M1": "number", "M2": "number", "M3": "number", "M4": "number", "M5": "number", "M6": "number", "M7": "number", "M8": "number", "M10": "number" }
    },
    "causal_language_compliance": {
      "violations": [
        { "location": "string", "violation_text": "string", "design_type": "string", "severity": "string", "suggested_fix": "string" }
      ],
      "overall_compliance_rate": "string"
    },
    "skeleton_generativity": {
      "validated_count": "number",
      "revise_count": "number",
      "reject_count": "number",
      "per_skeleton_assessment": [
        { "slot": "string", "variant": "string", "key_phrases_preserved": "boolean", "persuasive_action_preserved": "boolean", "verdict": "VALIDATED / REVISE / REJECT", "note": "string" }
      ]
    },
    "overall_rating": "ACCEPT / CONDITIONALLY_ACCEPT / NEEDS_REVISION / REJECT",
    "priority_fixes": [
      { "priority": "high / medium / low", "issue": "string", "current_state": "string", "recommendation": "string", "consequence_if_ignored": "string" }
    ]
  }
}
```

---
*基于 Pollock 2025 Ch07、MVP30 范文语料库构建。版本 2.0.0 — Methods 蒸馏 Meta-Skill。*
