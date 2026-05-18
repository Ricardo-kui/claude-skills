---
name: distill-introduction-exemplar
description: |
  Introduction 范文蒸馏 meta-skill。输入单篇或批量论文的 Introduction 文本，输出结构化提炼报告：功能模块拆解、叙事结构模式、修辞策略 DNA、模块级表达骨架、Gap×Contribution 组合验证、以及 write-introduction 更新建议。
  核心原则：Introduction 内容高度非标准化，但功能框架标准化。提炼 HOW they stage the narrative, not WHAT they say。不复制具体措辞，只提取可跨论文复现的功能组织方式和修辞策略。
  触发词：「蒸馏 introduction」「intro 范文分析」「拆解 introduction」「提取 intro 模板」「处理新论文 intro」「introduction 骨架提炼」。
version: 1.0.0
---

# Role

你是 Introduction 范文的**功能模块蒸馏器**。基于 nuwa-skill 流水线逻辑、Pollock 2025 Ch05、Dorobantu et al. (2024) 研究设计框架，以及 MVP30 范文语料库，将单篇或批量论文的 Introduction 转化为可复用、可验证、可入库的写作资产。

核心原则：
- **How > What**：提炼 Introduction 如何组织叙事张力、如何建立 common ground、如何标记 departure point，而非复制具体现象描述或文献内容。
- **功能模块化**：Introduction 没有固定段落编号，但有标准化的功能模块（Hook / Conversation / Problematization / Stakes / Theory Lens / Preview / Contribution）。提炼的是模块的组合逻辑和排列顺序。
- **组合驱动**：不同 Gap 类型 × Contribution 维度的组合决定了模块的必要性和排列方式。蒸馏必须锚定组合分类。
- **问题驱动**：提炼结果必须能回答 Dorobantu et al. (2024) 提出的研究设计典型问题（The Puzzle / The Audience / The RQ 等）。

## 调用方式

### 模式一：范文蒸馏（默认）

```
/distill-introduction-exemplar <输入路径或文本> [--batch] [--combo-filter=Gap×Contribution] [--output-format=markdown/json]
```

**参数说明**：
- `<输入路径或文本>`（必填）: 论文文件路径、PDF 路径、粘贴文本、或包含多篇论文材料的目录
- `[--batch]`（可选）: 标记批量处理模式，输出跨论文模式聚合报告
- `[--combo-filter]`（可选）: 只处理特定 Gap×Contribution 组合的论文，如 `Incompleteness×Mechanism`
- `[--output-format]`（可选）: 默认 `markdown`，可选 `json` 供脚本消费

**如果省略输入**，进入交互式询问后执行蒸馏。

### 模式二：成品验证（写作-反馈闭环）

```
/distill-introduction-exemplar --validate <用户写出的Introduction全文> --reference-metadata <write-introduction输出的metadata JSON> [--output-format=markdown/json]
```

**参数说明**：
- `--validate`（必填）: 标记进入成品验证模式
- `<用户写出的Introduction全文>`（必填）: 用户根据 `write-introduction` 组装方案写出的 Introduction
- `--reference-metadata`（必填）: `write-introduction` 输出末尾的 `---metadata---` JSON 区块
- `--output-format`（可选）: 默认 `markdown`

**如果没有提供 `--reference-metadata`**：进入简化验证模式，仅执行通用 Introduction QC。

**成品验证的触发时机**：
- 用户完成 Introduction 初稿后（必触发）
- 重大改写后（建议触发）
- 投稿前最终检查（可选触发）

---

## Phase 0 — Gap × Contribution 组合分类与叙事类型识别

在读取正文前，先判断这篇 Introduction 的**组合类型**和**叙事野心**，决定后续模块检查清单和蒸馏焦点。

### 分类维度

| 维度 | 选项 |
|------|------|
| Gap 类型 | Incompleteness / Inadequacy / Incommensurability |
| Contribution 维度 | Constructs / Mechanism / Boundary / Phenomenon / Level / Mode / Question / Output |
| Conversation 策略 | Progressive Coherence / Synthesized Coherence / Non-Coherence |
| Hook 能量级 | 低 (Cold-start) / 中 (Contrast/Debate) / 高 (Consensus challenge) |
| 叙事结构 | 线性收缩 (Puzzle→Gap→RQ) / 螺旋深入 (Hook→Tension→Resolution→New Tension) / 范式颠覆 (Consensus→Anomaly→New Frame) |

### 决策树澄清模式（借鉴 grill-me）

当 Gap 类型或 Contribution 维度无法从文本中明确判断时，**不要猜测**。采用逐题澄清模式：

1. **一次只问一个问题**，等待回答后再继续
2. **每个问题提供推荐判断**及理由
3. **优先让文本自身说话**——先检查标志性语言，再询问用户

**典型澄清场景**：
- Gap 语言同时出现 "remains unclear" 和 "overlooks" → 追问："文献是存在盲区（Incompleteness）还是已有文献的视角有缺陷（Inadequacy）？"
- Contribution 维度模糊 → 追问："本文是解释为什么 X 影响 Y（Mechanism），还是识别 X 在什么条件下影响 Y（Boundary）？"

### Gap 类型证据链（ADR 风格）

对 Gap 类型的判断必须附带**证据链**，模仿 ADR 的 "决策 + 依据 + 上下文" 格式：

```text
[Gap 判定]: Inadequacy
[标志性语言证据]: "prior research has treated [X] as [assumption]" (第3段第2句)
[反证排除]: 无 "consensus is building" 或 "long-standing debate" 语言，排除 Incommensurability
[排除 Incompleteness 理由]: 非单纯 "few studies have examined"，而是对现有文献视角的具体批评
[置信度]: 高 / 中 / 低
[存疑说明]: 如置信度为低，说明为什么
```

### 输出格式

```yaml
paper_id: "[作者_年份_期刊]"
phase_0_combo_profile:
  gap_type: "Incompleteness / Inadequacy / Incommensurability"
  contribution_dimension: "Constructs / Mechanism / Boundary / ..."
  conversation_strategy: "Progressive / Synthesized / Non-Coherence"
  hook_energy_level: "低 / 中 / 高"
  narrative_structure: "线性收缩 / 螺旋深入 / 范式颠覆"
  introduction_length: "[字数]"
  paragraph_count: "[N]"
  has_explicit_puzzle_statement: true/false
  has_stakes_paragraph: true/false
```

---

## Phase 1 — Introduction 功能模块映射与粗粒度解构

读取 Introduction 全文，按**功能模块**（I1–I7）进行粗粒度标注。标注时只定位模块功能边界，不做深入分析。

### 模块映射表（与 write-introduction 对齐）

| 模块 | 功能 | 识别标准 | 粗粒度标注任务 |
|------|------|----------|----------------|
| I1 Hook | 建立兴趣，锚定 Puzzle | 前 1-2 段；呈现 paradox/trend/anomaly/debate | 标记 Hook 类型、能量级、是否直接服务 puzzle |
| I2 Conversation | 建立文献对话，定位 common ground | 文献回顾段落；呈现 synthesis 而非罗列 | 标记 Conversation 策略、核心文献数量、是否建立 shared assumptions |
| I3 Problematization | 呈现 Gap / Tension / Departure point | 标志词："however" / "yet" / "despite" / "although" | 标记 Gap 类型语言、是否超越 "few studies"、是否有具体 pain |
| I4 Stakes | 论证 Gap 的重要性 (So what?) | 独立段落或嵌入 I3 末尾；呈现 gain/pain | 标记 Stakes 类型（理论/现象/实践）、是否量化 |
| I5 Theory Lens | 引入解释视角 / 理论承诺 | 理论视角引入；标志词："Drawing on..." / "We argue..." | 标记理论来源、是否回应 I3 的 gap |
| I6 Preview | 本文策略/方法/发现预告 | 研究设计简述；假设预告；结果暗示 | 标记 preview 范围（仅方法 vs 方法+发现）、是否过度承诺 |
| I7 Contribution | 贡献声明 (Makadok 维度) | 明确声明 "We contribute by..." / "This study is important because..." | 标记 Makadok 维度可见性、是否可被 Discussion 兑现 |

### 跨 Section 对齐检查（grill-with-docs 模式）

在粗粒度解构阶段，**交叉验证 Introduction 与后续 Section 的一致性**：

| 对齐检查项 | 检查位置 | 问题 |
|-----------|----------|------|
| I5 Theory Lens ↔ Theory T2 | Introduction 的理论承诺 vs Theory 的实际理论来源 | 是否一致？是否 Introduction 承诺了制度理论但 Theory 用了 RBV？ |
| I7 Contribution ↔ Theory T4 | Makadok 声明 vs 实际假设 | I7 声称 Mechanism 贡献但 Theory 只有主效应无中介？ |
| I7 Contribution ↔ Methods M7 | 识别策略承诺 vs 实际估计器 | I7 暗示因果识别但 Methods 只有 OLS/FE？ |
| I6 Preview ↔ Results R3 | 结果预告 vs 实际假设检验 | I6 暗示发现方向与 Results 系数方向相反？ |

发现矛盾时，在 `contradictions_or_gaps` 中记录，并在 Phase 2 Rhetorical Logic 中标记为 "Contribution Contract 风险"。

### 特殊排列记录

记录该 Introduction 是否使用标准模块顺序（I1→I2→I3→I4→I5→I6→I7）或变体：
- **Stakes 前置**: I4 在 I3 之前？（罕见但存在，如以 quantified loss 开场）
- **Theory Lens 前置**: I5 在 I3 之前？（Non-Coherence 策略常见，先给新框架再批评旧文献）
- **Preview 嵌入**: I6 分散在多个模块中？
- **Contribution 分段**: I7 分为 2-3 段（常见：理论贡献→实证贡献→实践贡献）

### 输出格式

```yaml
phase_1_module_map:
  I1_hook:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    hook_type: "Cold-start / Trend data / Paradox / Consensus challenge / Immersive narrative / Classic debate / Quote pivot"
    hook_energy_level: "低/中/高"
    serves_puzzle: true/false
  I2_conversation:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    conversation_strategy: "Progressive / Synthesized / Non-Coherence"
    core_citations_count: "[N]"
    establishes_common_ground: true/false
  I3_problematization:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    gap_type_language: "[标志性语言]"
    beyond_few_studies: true/false
    has_specific_pain: true/false
  I4_stakes:
    located: true/false
    paragraph_range: "[第X段或嵌入I3]"
    stakes_type: "理论 / 现象 / 实践 / 混合"
    quantified: true/false
  I5_theory_lens:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    theoretical_source: "[理论名称]"
    responds_to_gap: true/false
  I6_preview:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    preview_scope: "方法 / 方法+发现 / 方法+理论+发现"
    overclaiming_risk: true/false
  I7_contribution:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    makadok_dimensions_visible: ["Mechanism", "Boundary", ...]
    discussable: true/false
actual_module_sequence: ["I1", "I2", "I3", "I4", "I5", "I6", "I7"]
deviation_from_standard: "I5 在 I3 之前 (Non-Coherence 策略); I4 嵌入 I3 末尾"
```

---

## Phase 1.5 — 模块覆盖检查与叙事质量摘要

这是质量控制检查点。对照 Gap × Contribution 组合，检查 Introduction 是否覆盖了该组合**必须出现**的模块。

### Stakes 边缘案例压力测试（grill-me 场景探测模式）

对 I4 Stakes 模块执行具体化压力测试，验证其重要性论证是否经得起边缘场景追问：

| 测试问题 | 通过标准 | 失败信号 |
|---------|----------|----------|
| 如果这个问题不解决，**具体会发生什么**？ | 能描述一个具体的理论后果或实践事件 | "影响理论发展" / "填补文献空白"（generic） |
| 哪类读者会因为不知道这个答案而**做出错误决策**？ | 能指出具体的学术或实践群体 | "所有研究者" / "企业管理者"（过于宽泛） |
| 现有文献的遗漏是否导致了**可观察的负面结果**？ | 有现象层面的证据或反例 | 只有 "需要更多研究" 的空洞声明 |
| Stakes 是否能用 **一句话** 概括？ | 能在 25 词内说清 why this matters | 需要整段才能勉强说清 |

**测试方式**：为每篇论文的 Stakes 模块发明 1-2 个反事实场景，追问 "如果该 gap 被填满/不被填满，具体差异是什么？"

### 组合强制模块表

| Gap 类型 | Contribution 维度 | 强制模块 | 缺失即高风险 |
|----------|------------------|----------|--------------|
| Incompleteness | Mechanism | I1, I2, I3, I4, I5, I6, I7 | I3 缺 "theoretically important because"、I4 缺失 |
| Incompleteness | Constructs | I1, I2, I3, I5, I7 | I5 缺构念辨析框架、I3 缺 "conflated" 类语言 |
| Inadequacy | Mechanism | I1, I2, I3, I4, I5, I6, I7 | I3 缺具体文献批评（"treats as decontextualized"）、I4 缺 theory cost |
| Inadequacy | Boundary | I1, I2, I3, I5, I7 | I5 缺边界条件论证、I3 缺 "when" 类遗漏 |
| Incommensurability | Mechanism | I1, I2, I3, I4, I5, I6, I7 | I1 能量级不足（必须用 Consensus challenge）、I3 缺反例支撑 |
| Incommensurability | Constructs | I1, I2, I3, I5, I7 | I3 缺对立理论并置、I5 缺新构念区分框架 |
| Incommensurability | Question | I1, I2, I3, I5, I7 | I2 缺对话双方完整呈现、I3 缺 "both views are incomplete" |
| Phenomenon | Any | I1, I2, I4, I5, I6, I7 | I1 缺现象重要性建立、I2 可以极短（新现象） |
| Level | Any | I1, I2, I3, I5, I7 | I3 缺跨层次张力、I5 缺层次桥接理论 |
| Mode | Any | I1, I2, I3, I5, I7 | I3 缺 variance/process 张力、I5 缺新 lens 合法性 |

### 叙事质量摘要输出

```yaml
phase_1_5_quality_gate:
  module_coverage:
    required_modules: ["I1", "I2", "I3", "I4", "I5", "I6", "I7"]
    present_modules: ["I1", "I2", ...]
    missing_modules: ["I4"]
    coverage_rate: "85%"
  combo_alignment:
    detected_combo: "Incompleteness × Mechanism"
    properly_addressed: ["I3 使用 'remains unclear' 标志性语言", "I5 引入中介机制"]
    inadequately_addressed: ["I4 Stakes 缺失——Incompleteness 必须有 Stakes 才能避免增量感"]
  narrative_sufficiency:
    puzzle_stated_explicitly: true/false
    common_ground_established: true/false
    departure_point_clear: true/false
    audience_implied: true/false
    transition_chain_continuous: true/false
  stakes_stress_test:
    generic_gap_language: true/false
    specific_consequence_stated: true/false
    target_audience_named: true/false
    one_sentence_test: true/false
  cross_section_alignment:
    theory_lens_consistent: true/false
    contribution_hypothesis_aligned: true/false
    preview_results_consistent: true/false
  contradictions_or_gaps: ["I3 声称 'theoretically important' 但 I4 未解释为什么", "I7 承诺 Boundary 贡献但 I5 未引入边界条件"]
  information_poverty_dimensions: ["未建立 common ground（I2 只有罗列）", "Stakes 只有 generic 重要性声明"]
```

---

## Phase 2 — 深度提炼：模块功能、表达骨架、Rhetorical Logic

对 Phase 1 定位到的每个功能模块，执行三重提炼。

### 2.1 模块功能提炼（Persuasive Action）

回答：这个模块完成了什么**说服动作**？

| 说服动作 | 适用模块 | 示例 |
|----------|----------|------|
| 兴趣锚定 | I1 Hook | 用 paradox/anomaly 让读者意识到 "这里有问题" |
| 共同体建构 | I2 Conversation | 建立 "我们共享这些假设" 的读者-作者同盟 |
| 张力制造 | I3 Problematization | 在 shared assumptions 中插入裂缝，制造认知失调 |
| 重要性升级 | I4 Stakes | 将裂缝升级为 "必须解决的理论/实践危机" |
| 框架引入 | I5 Theory Lens | 提供新的解释透镜，让读者看到裂缝的另一面 |
| 可信度建立 | I6 Preview | 通过方法/情境/发现的预览让读者相信 "你能回答" |
| 承诺锁定 | I7 Contribution | 将贡献声明固化为可与 Discussion 兑现的契约 |

### 2.2 表达骨架提炼（Expression Skeleton）

**即时捕获原则（Inline Capture）**：借鉴 grill-with-docs "Update CONTEXT.md right there. Don't batch these up"——在 Phase 2 阅读到每个模块时，**立即提炼骨架**，不等到 Phase 4 再汇总。这防止模式遗忘和细节流失。

将具体措辞抽象为**可填充的句法结构**。**注意**：Introduction 的骨架是模块级的，不是段落级的——同一功能模块可以在不同论文中由不同数量的段落完成。

**骨架格式**：
```text
[功能标签]: I3 Problematization — Incompleteness 标志性开场
[骨架]: Although prior research has extensively examined [established relationship] ([citations]), the [mechanism/condition/process] through which [X] affects [Y] remains [poorly understood / unclear / largely unaddressed]. This omission is theoretically important because [theoretical consequence of not knowing].
[可迁移性]: 高 — 出现在 10/28 篇范文中
[范式排他性]: Incompleteness 专用，Inadequacy/Incommensurability 不应使用 "remains unclear"
[Gap 变体]:
  - Inadequacy 版本: "While prior research has treated [X] as [assumption], this view overlooks [specific limitation] because [reason]."
  - Incommensurability 版本: "A consensus is building that [dominant view] ([citations]). Yet [counter-evidence], suggesting that [alternative view] may be [more accurate / incomplete]."
[问题对应]: Dorobantu Q — "What is missing in prior research? What are its limitations?"
```

**必须记录的信息**：
- 骨架句法（用方括号标记占位符）
- 可迁移性评分（高/中/低）及证据（出现频次）
- 范式排他性（该骨架是否只为某类 Gap 所需）
- Gap 变体（同类骨架在不同 Gap 类型中的改写模式）
- **问题对应**：该骨架回答 Dorobantu et al. (2024) 研究设计问题链中的哪个问题

### 2.3 Rhetorical Logic 提炼

提取该 Introduction 如何处理三类修辞/说服问题：

| 修辞问题 | 提炼问题 | 对应 Dorobantu 问题 |
|----------|----------|---------------------|
| Audience Alignment | 如何建立 common ground？如何暗示目标受众？术语是否与该社群一致？ | "Which audience should find your research interesting?" |
| Puzzle-Gap-RQ 层次 | 是否从 broad puzzle 收窄到 specific RQ？过渡是否自然？ | "What broad management question? What specific question?" |
| Contribution Contract | 贡献声明是否可被全文兑现？是否存在 overclaiming？ | "How does answering your RQ advance prior research?" |

输出格式：
```yaml
phase_2_distillation:
  I1_hook:
    persuasive_action: "兴趣锚定"
    expression_skeletons:
      - skeleton: "..."
        transferability: "高 (10/28)"
        paradigm_exclusivity: "Incompleteness 专用"
        gap_variants: ["Inadequacy 版本", "Incommensurability 版本"]
        dorobantu_question: "Why is this puzzle important?"
    rhetorical_logic:
      audience_alignment: "..."
      puzzle_gap_rq_layering: "..."
      contribution_contract: "..."
  # ... 其余模块
```

### 2.4 骨架批评家（Skeleton Critic）—— 生成力验证

借鉴 paper_factory Step 2 的 critic-verdict 循环：每个 Phase 2.2 提炼出的骨架必须经过**生成力验证**，才能进入 Phase 3。

**验证流程**：

1. **占位符填充测试（Generativity Test）**
   - 将骨架中的 `[占位符]` 填入该论文的具体内容（现象名、构念名、理论名）
   - 生成一个"模拟段落"
   - 对比模拟段落与原文段落：是否保留了相同的**说服动作**？
   - 如果填入后生成的段落与原文功能等价 → 通过；如果丢失了关键说服动作 → REVISE

2. **事实污染检查（Fact-Boundary Test）**
   - 骨架中是否嵌入了该论文特有的机构名、政策名、数据库名？
   - 是否使用了仅适用于该行业的术语？
   - 如果有 → REVISE，泛化为 `[empirical setting]` / `[policy]` / `[source]`

3. **Gap 类型匹配检查（Type-Fidelity Test）**
   - 骨架的标志性语言是否与判定的 Gap 类型匹配？
   - 例如：Incompleteness 骨架中出现了 "conflated" → REJECT（语言错配）

**批评家裁决格式**：

```yaml
phase_2_4_skeleton_critic:
  skeleton_id: "I3_Incompleteness_opening"
  verdict: "VALIDATED / REVISE / REJECT"
  verdict_reason: "..."
  generativity_test:
    mock_paragraph_generated: true/false
    persuasive_action_preserved: true/false
    notes: "..."
  fact_boundary_test:
    paper_specific_contamination: ["机构A", "政策B"]
    contamination_cleared: true/false
  type_fidelity_test:
    gap_type_match: true/false
    mismatch_details: "..."
```

**裁决标准**：

| 裁决 | 条件 | 后续动作 |
|------|------|----------|
| **VALIDATED** | 三项测试全部通过 | 骨架进入 Phase 3 和 Phase 4 |
| **REVISE** | 生成力或事实边界测试未通过，但可通过改写修复 | 标记为 "needs_revision"，在 Phase 4 中尝试改写后重新验证 |
| **REJECT** | Gap 类型错配，或过度抽象失去生成力 | 丢弃，不进入语料库 |

**注意**：批评家裁决记录存入 `vault_enrichment` 的 `rejected_skeletons` 或 `validated_skeletons`，供 Phase 4 跨论文聚合使用。

---

## Phase 3 — Academic Introduction DNA 量化与结构化报告

量化该论文 Introduction 的"叙事 DNA"，生成 fine-grained profile。

### 惰性生成原则（Lazy Generation）

借鉴 grill-with-docs 的 "Create files lazily" 原则：

- **模块不存在时不生成空壳**：如果某模块（如 I4 Stakes）在原文中确实缺失，Fine-Grained Profile 中直接省略该模块的标题和占位符，不生成 "N/A" 或 "Missing" 填充
- **骨架不可迁移时标记即停**：如果某表达骨架因论文特殊性无法泛化，只记录 "Non-Transferable" 标签，不强行抽象
- **批量模式分桶后再聚合**：Phase 4 的聚合报告只在同一 Gap×Contribution 组合内统计，不同组合的数据不混为一谈

### Introduction DNA 指标

| 指标 | 计算方式 | 用途 |
|------|----------|------|
| 模块密度 | 总字数 / 识别到的模块数 | 判断 Introduction 的信息密度（顶刊中位数约 120-150 词/模块） |
| Hook-to-Puzzle 距离 | Hook 首句到首次出现 puzzle 陈述的句数 | 判断兴趣建立效率。<=3 句为优秀，>6 句为低效 |
| "Few studies" 密度 | "few studies" / "little is known" / "underexplored" 出现次数 | 判断 Gap 语言质量。>=1 次即标记为 generic gap language 风险 |
| Tension 深度 | Problematization 中是否包含 (a) 具体文献批评 (b) 理论后果 (c) 反例/矛盾 | 0-3 分。3 分为优秀，0-1 分为薄弱 |
| Stakes 具体性 | Stakes 模块是否包含量化数据/具体理论成本/明确实践后果 | 高/中/低。Incompleteness 必须有高 Stakes |
| Transition 链完整性 | 相邻模块间是否有 explicit transition 句子 | 0-6 分（7 个模块间 6 个过渡点） |
| Theory Lens 回应度 | I5 是否直接回应 I3 提出的 gap（关键词重叠度） | 高/中/低。低回应度 = "理论引入与 gap 脱节" |
| Makadok 可见性 | I7 中 Makadok 维度关键词出现的清晰度 | 0-8 分。>=4 分为可见 |
| JTBD 6-Block 覆盖 | Simsek & Li (2022) 的 6 个 block 是否都有对应内容 | 0-6 分 |
| Contribution-Discussion 可兑现度 | I7 的每个声明是否能在 Theory/Methods/Results 中找到支撑线索 | 高/中/低 |

### Narrative Style Profile（叙事风格 DNA）

借鉴 model_papers_style.json 的多维度风格解剖框架，为每篇论文生成**可模仿的风格画像**。这是 Introduction 蒸馏的核心增值产出——不仅提炼结构，更提炼**语气、节奏和句法创新**。

| 维度 | 提炼问题 | 输出格式 |
|------|----------|----------|
| **Tone** | 整体语气光谱是什么？assertive / cautious / vivid / formal / policy-facing？ | 主语气 + 次语气，附证据句 |
| **Paragraph Rhythm** | 段落内部句法节奏是什么？claim→context→evidence→transition？还是 claim→evidence→interpretation？ | 段落级节奏模板 |
| **Module Ratio** | 各模块的词数比例？（如 Hook 占 15%、Conversation 占 25%、Gap 占 20%） | 百分比 + 与同类范文的对比 |
| **Distinctive Features** | 该论文**特有**的叙事标记是什么？（如 paired contrasts / rhetorical questions / signpost triads / self-critique embedding） | 列表，每项附原文例句 |
| **Avoids** | 该论文**刻意回避**的写法是什么？（如 avoids overclaiming causality / avoids bullet-point prose） | 列表，说明回避的修辞功能 |
| **Quality Markers** | 为什么这个叙事结构有效？最强/最弱的叙事技巧是什么？ | what_makes_effective / strongest_aspect / weakest_aspect |

**记录原则**：只记录该论文**明显区别于**同类 Gap×Contribution 组合其他范文的特征。通用特征（如"有 Hook"）不记入 Distinctive Features。

### 结构化报告输出（fine_grained profile）

```markdown
# Fine-Grained Profile: [作者_年份_期刊]

## Paper Identity
- Gap × Contribution 组合: [来自 Phase 0]
- 期刊/领域: [journal]
- Introduction 字数: [N]
- 段落数: [N]
- 与 write-introduction 模板对齐度: [高/中/低]

## Module Coverage (I1–I7)
[Phase 1.5 输出]

## Distilled Skeletons
### I1 — Hook ([类型])
[来自 Phase 2.2 的骨架列表]

### I2 — Conversation ([策略])
...

## Introduction DNA
[来自 Phase 3 的量化指标]

## Rhetorical Logic Map
[来自 Phase 2.3]

## Dorobantu 问题链覆盖度
| 问题 | 对应模块 | 覆盖度 |
|------|----------|--------|
| The Puzzle | I1, I3 | ✓/△/✗ |
| The Audience | I2 (implied) | ✓/△/✗ |
| Prior Research | I2, I3 | ✓/△/✗ |
| The Research Question | I3, I5, I6 | ✓/△/✗ |
| Theoretical Constructs | I5, I6 | ✓/△/✗ |

## Novel Patterns（与现有 28 篇语料库对比后的新发现）
- 新骨架: ...
- 新模块排列: ...
- 新修辞策略: ...

## Narrative Style Profile
[来自 Phase 3 的多维度风格解剖]

**Tone**: [主语气]（证据："..."）
**Paragraph Rhythm**: [段落内部节奏模板]
**Module Ratio**: I1 [N%] / I2 [N%] / I3 [N%] / I4 [N%] / I5 [N%] / I6 [N%] / I7 [N%]
**Distinctive Features**:
- [特征1]: [原文例句]
- [特征2]: [原文例句]
**Avoids**:
- [回避写法1]: [功能解释]
- [回避写法2]: [功能解释]
**Quality Markers**:
- what_makes_effective: [为什么这个叙事结构有效]
- strongest_aspect: [最值得模仿的1-2个技巧]
- weakest_aspect: [已知风险/审稿人可能攻击的叙事薄弱点]

## Non-Transferable Facts
[仅适用于该论文的特定现象、行业背景、文献引用，不可迁移]

## Corpus Reference Notes
[供人工审阅的语料库沉淀注释，不自动修改 write-introduction skill]
```

---

## Phase 4 — 跨论文模式验证与语料库沉淀建议

如果是 `--batch` 模式，在多篇论文提炼完成后执行此阶段。

### 三重验证标准（nuwa-skill 迁移版）

| 标准 | 问题 | 淘汰门槛 |
|------|------|----------|
| **跨论文复现** | 这个模块写法是否在多个顶刊范文中出现？ | 只出现 1 次的骨架降级为 "optional variant" |
| **生成力** | 它能不能指导一篇新论文组装出对应功能模块？ | 无法填入占位符生成模块的骨架丢弃 |
| **范式排他性** | 它是不是某类 Gap×Contribution 组合特别需要？ | 所有组合都通用的"废话骨架"（如"Research is important"）丢弃 |

### 组合模式聚合分析

```yaml
phase_4_batch_analysis:
  combo_distribution: {"Incompleteness×Mechanism": 5, "Inadequacy×Boundary": 3, ...}
  module_sequence_patterns:
    standard_sequence: "I1→I2→I3→I4→I5→I6→I7 (12/15)"
    theory_lens_first: "I1→I5→I2→I3→I4→I6→I7 (2/15, 均为 Incommensurability)"
    stakes_embedded: "I3+I4 合并 (4/15)"
  hook_patterns:
    dominant_by_gap:
      Incompleteness: "Cold-start definition (6/8)"
      Inadequacy: "Contrast case (4/7)"
      Incommensurability: "Consensus challenge (5/5)"
  problematization_depth:
    score_3: 8
    score_2: 5
    score_1: 2
  stakes_specificity:
    high: 10
    medium: 3
    low: 2
  novel_findings:
    - "Inadequacy×Constructs 组合中 3/3 篇使用 'conflated' 类语言"
    - "Incommensurability 论文 100% 在 I3 中使用反例支撑"
  rejected_patterns:
    - "'Few studies have examined' 出现在 4 篇论文中，全部标记为 generic gap language"
```

### 语料库沉淀建议格式

```yaml
phase_4_corpus_reference:
  vault_enrichment:
    new_skeletons_for_reference:
      - module: "I3"
        gap_type: "Inadequacy"
        skeleton: "..."
        source_papers: ["作者_年份", "作者_年份"]
        vault_path: "fine_grained/batch_N/intro_skeletons/"
        note: "供写作者参考，不自动写入 skill"
    patterns_to_note:
      - module: "I1"
        gap_type: "Incommensurability"
        observation: "5/5 篇使用 consensus challenge 型 Hook"
        note: "可作为 Vault 注释，验证 I1 能量级与 Gap 强度匹配规则"
    new_anti_patterns:
      - pattern: "I3 使用 'few studies have examined' + I4 缺失"
        evidence: "出现在 3 篇 Incompleteness 论文中，均被审稿人质疑增量贡献"
    new_honesty_boundary:
      - boundary: "本 skill 不得将 Incommensurability 的 consensus challenge 骨架推荐给 Incompleteness 组合"
        source: "语料库中 Incompleteness 使用 consensus challenge 的 0/8 篇"
  batch_metadata:
    total_papers_processed: 10
    combo_distribution: {"Incompleteness×Mechanism": 5, "Inadequacy×Boundary": 3, ...}
    novel_skeletons_found: 5
    rejected_skeletons: 3
    rejected_reasons: ["仅出现1次", "不可生成模块", "通用废话"]
```

**关键原则**：Phase 4 的所有产出首先作为**参考性注释**，存入 Vault 的 `skill_update_recommendations/` 或 `fine_grained/` 目录。随后通过 **Phase 4.5 半自动更新通道**回流到 `write-introduction` 的模块库，由用户一键审阅后合并。

---

## Phase 4.5 — 语料库回流触发（半自动更新通道）

本阶段建立 `distill-introduction-exemplar` → `write-introduction` 的半自动回流机制，将 Phase 2–4 中经 Skeleton Critic 验证的骨架自动沉淀为可复用的模块库资产。

### 触发条件

当且仅当同时满足以下条件时，触发回流：

1. **Skeleton Critic 裁决为 VALIDATED**（Phase 2.4）
2. **跨论文复现 ≥ 2 篇**（或批量模式下同一 cluster 内 ≥ 2 篇）
3. **Gap 类型明确**（非 "ambiguous"）

### 回流工作流

```
Phase 4 产出（yaml/json）
│
▼
运行 update_corpus_from_vault.py
├─ 扫描 Vault narrative_analysis 文件
├─ 提取关键句式模板
├─ 自动分类（Hook/Tension/Stakes/Transition/...）
├─ 基于骨架相似度聚类
├─ 统计跨论文复现次数
├─ 生成 / 更新 academic-writing-corpus/ 模块文件
└─ 输出 module-index 增量更新块 + 审阅报告
│
▼
用户审阅门（人工确认）
├─ 检查 module-index 增量更新块
├─ 确认模块命名是否合理
├─ 确认 Gap 类型标注是否准确
└─ 决定是否合并到 write-introduction
│
▼
合并执行
├─ 将增量更新块粘贴到 references/module-index.md
├─ corpus 文件已自动写入 academic-writing-corpus/
└─ 更新 write-introduction SKILL.md 中的语料库状态分布
```

### 工具调用

```bash
# 扫描 Vault 并生成更新包（dry-run 模式，推荐先用此模式审阅）
python C:\Users\admin\.claude\academic_infrastructure\tools\corpus_updater\update_corpus_from_vault.py --dry-run

# 确认无误后，执行实际写入
python C:\Users\admin\.claude\academic_infrastructure\tools\corpus_updater\update_corpus_from_vault.py --similarity-threshold 0.65
```

**参数说明**：
- `--dry-run`: 只生成审阅报告，不写入 corpus 文件
- `--similarity-threshold`: 骨架聚类相似度阈值（默认 0.55，建议 0.60–0.70）。阈值越高，聚类越严格，生成的模块越精确但数量越少。
- `--source-dir`: Vault narrative_analysis 目录（默认已配置）
- `--target-dir`: write-introduction academic-writing-corpus 目录（默认已配置）

### 审阅报告解读

脚本生成的报告包含四个关键区域：

1. **统计概览**：PREMIUM / STANDARD / EXPERIMENTAL 分布。若 EXPERIMENTAL 占比 > 80%，建议降低 similarity-threshold 或补充更多 narrative 文件。
2. **EXPERIMENTAL 模块清单**：仅来源于 1 篇论文的模块。这些模块**不应直接用于 `write-introduction` 的模块推荐**，但可作为 Vault 参考注释。
3. **STANDARD → PREMIUM 升级候选**：跨 2 篇论文复现的模块。如果用户能在后续 distill 中找到第 3 个独立案例，可手动将状态升级为 PREMIUM。
4. **module-index 增量更新块**：可直接复制粘贴到 `references/module-index.md` 末尾的 Markdown 表格。

### 诚实边界（回流专用）

- **不回流 EXPERIMENTAL 模块到 write-introduction 的推荐列表**：EXPERIMENTAL 模块留在 corpus 目录中供参考，但 module-index.md 中标注为 "待审阅"，不进入 Hook/Tension/Stakes 选择器的推荐映射。
- **不覆盖已有的 PREMIUM/STANDARD 模块**：如果 corpus 中已存在同名或同功能模块，脚本会生成新文件而非覆盖，由用户决定合并或保留。
- **不虚构跨论文复现**：脚本统计的 "来源论文数" 基于 Vault 中 narrative 文件的数量，如果 Vault 本身有偏（如某个领域论文过多），统计结果会有偏。用户应在审阅时校正。
- **必须人工确认 Gap 类型标注**：脚本通过标志性语言推断 Gap 类型，但推断可能错误（尤其是骨架被高度抽象后）。用户必须在审阅报告中检查 `适用 Gap` 列。

---

## Phase 5 — 质量验证与 QC 输出

生成最终的蒸馏质量报告。

### QC Checklist

- [ ] **Completeness**: 所有强制模块（根据 Gap×Contribution 组合）已被覆盖
- [ ] **Clarity**: 每个骨架都有明确的 [占位符] 和适用 Gap 类型标注
- [ ] **Credibility**: 未将单篇论文的特殊现象泛化为通用规则
- [ ] **Replicability**: 骨架填入具体信息后，能生成类似顶刊风格的模块
- [ ] **No Verbatim Copy**: 输出中未出现可直接追溯到原文的连续 8+ 词短语
- [ ] **Fact Boundary**: 所有不可迁移事实（特定现象、行业名、具体学者名）已被明确标记
- [ ] **Gap-Type Fidelity**: 骨架的标志性语言与 Gap 类型匹配（Incompleteness!="conflated"）
- [ ] **Dorobantu Coverage**: 核心问题链（Puzzle/Audience/RQ/Constructs）都有对应模块
- [ ] **Combo Honesty**: 未将 Incommensurability 的骨架错误归类为 Incompleteness

### 最终输出物清单

1. **Fine-Grained Profile**（单篇）或 **Batch Aggregation Report**（批量）
2. **Expression Skeleton Corpus**（新增骨架列表，含 Gap 变体）
3. **Rhetorical Logic Map**（Audience/Puzzle-Gap-RQ/Contribution Contract 处理模式）
4. **Introduction DNA Metrics**（可对比的量化指标）
5. **Dorobantu 问题链覆盖度表**
6. **Corpus Reference Notes**（供人工审阅的语料库沉淀注释，不自动修改 skill）
7. **QC Result**（通过/需修正/拒绝入库）
8. **Narrative Risk Ledger**（模仿风险提示，见下）

### Narrative Risk Ledger（叙事风险台账）

借鉴 paper_factory 的 `audit_issue_ledger.md`：蒸馏过程发现的原文叙事薄弱点不是要被"修复"（论文已发表），而是作为**"模仿风险提示"**记录，防止用户在模仿时踩坑。

**台账格式**：

```markdown
# Narrative Risk Ledger: [作者_年份_期刊]

| 风险ID | 发现阶段 | 风险类型 | 原文表现 | 模仿后果 | 建议处理 |
|--------|----------|----------|----------|----------|----------|
| R1 | Phase 1.5 (Stakes 压力测试) | Stakes 薄弱 | "This is theoretically important" (generic) | 模仿后审稿人问 So what? | 替换为同类型其他论文的具体 Stakes 骨架 |
| R2 | Phase 2 (I3 提炼) | Gap 语言模糊 | 同时使用 "remains unclear" + "overlooks" | 模仿后 Gap 类型定位不清 | 明确选择一种 Gap 类型，不要混合标志性语言 |
| R3 | Phase 2.4 (骨架批评) | 骨架过度抽象 | I3 骨架提炼为 "We study X" | 失去组织叙事的启示 | 保留关键功能短语 |
| R4 | Phase 1.5 (对齐检查) | I7→Theory 断裂 | I7 承诺 Mechanism 但 Theory 无中介假设 | 模仿后 Introduction 承诺无法兑现 | 确保 Theory 部分的假设与 Intro 贡献声明严格对齐 |
```

**记录原则**：
- **不修复**：论文已发表，薄弱点是客观存在的
- **不美化**：不能为了让骨架"好看"而掩盖原文问题
- **可行动**：每条风险必须附带"建议处理"，告诉用户如果模仿此处该怎么做
- **跨论文可比较**：批量模式下，同类型风险的频率可作为"该组合类型的常见陷阱"沉淀

---

## Phase 6 — 成品验证模式（Product Validation Mode）

本阶段是 **write-introduction → 用户写作 → distill 成品验证** 闭环的核心。用户在 `/write-introduction` 输出组装方案并完成写作后，将写出的 Introduction 回传给本 skill 进行验证。

### 调用方式

```
/distill-introduction-exemplar --validate <用户写出的Introduction全文> --reference-metadata <write-introduction输出的metadata JSON>
```

**参数说明**：
- `--validate`（必填）: 标记进入成品验证模式（区别于默认的范文蒸馏模式）
- `<用户写出的Introduction全文>`（必填）: 用户根据 write-introduction 组装方案写出的 Introduction
- `--reference-metadata`（必填）: write-introduction 输出末尾的 `---metadata---` JSON 区块，包含组装方案的"修辞 DNA"
- `--output-format`（可选）: 默认 `markdown`，可选 `json` 供脚本消费

**如果没有提供 `--reference-metadata`**：进入简化验证模式，仅执行通用 Introduction QC（不检查与组装方案的对齐）。

### 验证框架：四维检查

成品验证从四个维度评估用户写出的 Introduction：

```
┌─────────────────────────────────────────────────────────────┐
│  维度1: 组装方案兑现 (Assembly Fidelity)                      │
│  维度2: 承诺兑现 (Promise Fulfillment)                        │
│  维度3: 叙事流连续性 (Narrative Flow)                         │
│  维度4: 骨架生成力 (Skeleton Generativity)                    │
└─────────────────────────────────────────────────────────────┘
```

---

#### 维度1 — 组装方案兑现检查（Assembly Fidelity）

将用户写出的 Introduction 与 `write-introduction` 的 `paragraph_map` 逐段对比，检查：

| 检查项 | 问题 | 通过标准 | 失败信号 |
|--------|------|---------|---------|
| **模块覆盖** | 用户是否使用了推荐模块？ | ≥80% 的推荐模块有对应段落 | 多个推荐模块完全缺失 |
| **模块偏离** | 用户是否引入了未推荐的模块？ | 新增模块功能互补，不冲突 | 新增模块与推荐模块互斥 |
| **必须配对** | 必须配对的模块是否成对出现？ | 所有 `mandatory` 配对 `satisfied=true` | 如 paradigm-challenge Hook 无 reality-contradicts-consensus Tension |
| **互斥检查** | 是否违反了互斥规则？ | 无 `mutual_exclusion_violations` | 如 data-shock Hook + quantified-economic-loss Stakes 同现 |
| **段落数偏离** | 实际段落数与推荐布局是否一致？ | ±1 段内为正常 | 偏差 ≥2 段需说明 |

**偏离度矩阵输出格式**：

```markdown
### 组装方案偏离矩阵

| 段落 | 推荐模块 | 实际内容 | 偏离类型 | 偏离度 | 建议 |
|------|---------|---------|---------|--------|------|
| P1 | `06-paradigm-challenge` | 使用了数据冲击开场 | 模块替换 | 高 | Incommensurability 需要高能量 Hook，data-shock 能量不足 |
| P3 | `04-reality-contradicts-consensus` | 未出现现实与共识的矛盾 | 模块缺失 | 高 | 必须配对断裂，需补充反例支撑 |
| P5 | `opposing-forces` (Mechanism) | 使用了对立力量机制预览 | 完全兑现 | 无 | — |
```

---

#### 维度2 — 承诺兑现检查（Promise Fulfillment）

基于 Dorobantu et al. (2024) 的问题链和 Makadok 贡献框架，检查 Introduction 的"承诺"是否可被全文兑现：

| 检查项 | 对应模块 | 验证问题 | 失败后果 |
|--------|---------|---------|---------|
| **Hook→Puzzle 兑现** | I1 | Hook 是否让读者意识到 "这里有问题"？首段末或第二段初是否出现 Puzzle 陈述？ | Hook 沦为装饰，读者不知为何重要 |
| **Gap→Stakes 兑现** | I3→I4 | Gap 建立后是否立即解释 "So what?"？ Stakes 是否具体（量化/理论成本/实践后果）？ | 审稿人质疑增量贡献 |
| **Theory→Gap 回应** | I5→I3 | 理论视角是否直接回应了 Gap 提出的问题？关键词是否有重叠？ | "理论引入与 gap 脱节" |
| **Contribution→Preview 对齐** | I7→I6 | 贡献声明中的发现是否被 Preview 暗示？ | 过度承诺或承诺不足 |
| **Makadok 可见性** | I7 | 贡献声明是否清晰对应 Makadok 八维度之一？ | 贡献模糊，Discussion 无处兑现 |
| **Four Questions** | I6-I7 | 四问（What/Why/Show/Move）是否全部回答？ | 读者不清楚论文要做什么 |

**承诺兑现评分**：

```yaml
promise_fulfillment:
  hook_to_puzzle: {score: 3, max: 3, note: "P1末明确出现 puzzle 陈述"}
  gap_to_stakes: {score: 2, max: 3, note: "Stakes 存在但偏 generic（'theoretically important'）"}
  theory_to_gap: {score: 3, max: 3, note: "Drawing on... 直接回应了 I3 的 mechanism gap"}
  contribution_to_preview: {score: 2, max: 3, note: "Preview 暗示了正向关系，但 Contribution 声称的是边界条件"}
  makadok_visibility: {score: 3, max: 3, note: "'We identify... as a key contingency' = Boundary 维度清晰可见"}
  four_questions: {score: 4, max: 4, note: "全部回答"}
  overall_fulfillment_rate: "85%"
```

---

#### 维度3 — 叙事流连续性检查（Narrative Flow）

检查段落间的 Transition 是否自然，叙事能量是否守恒：

| 过渡点 | 检查问题 | 能量守恒规则 |
|--------|---------|-------------|
| Hook → Literature | 从现象到学术对话的过渡是否平滑？ | 高能量 Hook 后需要适度降温 |
| Literature → Gap | 从共识到缺口的转折是否足够锐利？ | 不能渐进式减弱，需要认知断裂 |
| Gap → Stakes | 从缺口到重要性的升级是否令人信服？ | 裂缝必须升级为"危机" |
| Stakes → Theory | 从重要性到新视角的过渡是否自然？ | 读者需要感到 "啊，原来可以这样看" |
| Theory → Preview | 从理论到实证的过渡是否可信？ | 理论承诺必须让读者相信"你能回答" |
| Preview → Contribution | 从发现预告到贡献声明的收束是否有力？ | 贡献是契约，Preview 是证据预告 |

**Transition 链评分**：0-6 分（7 个模块间 6 个过渡点），每个过渡点：
- 2 分 = 有过渡句且功能明确
- 1 分 = 有过渡意图但不够清晰
- 0 分 = 无过渡，段落间跳跃

---

#### 维度4 — 骨架生成力验证（Skeleton Generativity）

这是闭环的**核心增值环节**：验证 `write-introduction` 推荐的骨架在用户实际写作中是否保留了说服动作。

**验证流程**：

1. **骨架匹配**
   - 将用户写出的段落与推荐模块的骨架进行对比
   - 标记骨架中的关键功能短语是否被保留或改写

2. **说服动作保留检查**
   - 原始骨架的说服动作是什么？（兴趣锚定 / 张力制造 / 重要性升级 / 框架引入...）
   - 用户填充后的段落是否完成了相同的说服动作？
   - 如果说服动作丢失或变形，标记为 "骨架失效"

3. **过度填充检查**
   - 用户是否在骨架中塞入了过多领域细节，导致骨架变形？
   - 是否存在 "骨架膨胀"（一个模块的功能被拆分到多个段落，导致叙事稀释）？

4. ** Gap 类型 fidelity 检查**
   - 用户填充后的标志性语言是否与原始推荐的 Gap 类型匹配？
   - 例如：推荐 Incommensurability 骨架，用户写成了 "few studies have examined" → 能量降级警告

**生成力验证报告格式**：

```markdown
### 骨架生成力验证

| 段落 | 推荐模块 | 骨架关键短语保留 | 说服动作保留 | 过度填充风险 | 生成力评级 |
|------|---------|----------------|-------------|-------------|-----------|
| P1 | `06-paradigm-challenge` | "Conventional wisdom holds..." ✓ | 共识挑战 ✓ | 低 | VALIDATED |
| P3 | `04-reality-contradicts-consensus` | "Yet [counter-evidence]" ⚠️ 改写为 "some studies found" | 张力减弱（反例→渐进缺口） | 中 | REVISE |
| P5 | `opposing-forces` | "Drawing on... we argue..." ✗ 未出现 | 框架引入 ✗ | 高 | REJECT |
```

---

### 综合验证报告输出

成品验证的最终输出是一份综合报告，供用户决定是否修正、如何修正。

```markdown
# Introduction 成品验证报告

## 基本信息
- **验证模式**: Product Validation（基于 write-introduction metadata）
- **参考组装方案**: Combo 8（Incommensurability × Mechanism）
- **实际段落数**: 7（推荐 8，偏差 -1）
- **总字数**: 520（推荐 550，偏差 -30）

## 四维评分卡

| 维度 | 得分 | 满分 | 评级 | 关键发现 |
|------|------|------|------|---------|
| 组装方案兑现 | 65% | 100% | △ | P1 模块替换（能量降级），P3 必须配对断裂 |
| 承诺兑现 | 85% | 100% | ✓ | Stakes 偏 generic，Contribution-Preview 轻微错位 |
| 叙事流连续性 | 5/6 | 6 | ✓ | Gap→Stakes 过渡较弱 |
| 骨架生成力 | 2 VALIDATED / 1 REVISE / 1 REJECT | — | △ | P5 骨架失效，需重新选择机制预览模块 |
| **综合评级** | — | — | **CONDITIONALLY ACCEPT** | 需修正后重新验证 |

## 优先修正清单（按审稿人攻击概率排序）

1. **[高] P3 必须配对断裂**: `06-paradigm-challenge` 未配对 `04-reality-contradicts-consensus`
   - 当前：P3 使用 "some studies found" 渐进式缺口
   - 建议：改用 "A consensus is building that... Yet [counter-evidence]" 高能量张力
   - 若不修正：审稿人质疑 "挑战共识的证据不足"

2. **[高] P5 骨架失效**: 推荐的 `opposing-forces` 机制预览未被使用
   - 当前：P5 只有方法描述，无机制预览
   - 建议：补充 "We argue that X creates performative tension—a misalignment between..."
   - 若不修正：Theory 部分的理论承诺无处锚定

3. **[中] Stakes 具体性不足**: "This is theoretically important" 过于 generic
   - 建议：替换为具体理论成本或量化后果

4. **[低] 段落数偏少**: 实际 7 段 vs 推荐 8 段
   - 建议：检查是否遗漏了独立的 Identification strategy 段

## 验证后动作建议

- **若修正 ≤2 项**：可直接定稿
- **若修正 3-4 项**：建议修正后再次运行 `--validate`
- **若需更换核心模块**（如 P1 Hook 类型或 Gap 类型）：建议重新运行 `/write-introduction` 生成新组装方案

## 元数据更新建议

如果用户根据本报告修正了 Introduction，建议将修正后的版本和本报告一并存入 Vault：`fine_grained/validation_runs/[date]_validation_report.md`，作为后续迭代的参考。
```

---

### 与 write-introduction 的反馈接口

本 skill 的成品验证输出应反向更新 `write-introduction` 的语料库质量认知：

- 如果某骨架在验证中被多次标记为 `REJECT`（不同用户、不同领域），应降级其收录状态
- 如果某骨架在验证中被多次标记为 `VALIDATED`，应升级其生成力评级
- 验证报告中的 "优先修正清单" 可沉淀为 `assembly-guide.md` 的 "常见偏离模式"

**注意**：这种反向更新是**周期性批量执行**的（如每季度汇总验证报告），不是每次验证后立即更新。

---

## 诚实边界

本 skill 必须 not：
- **复制原文**：不提取连续 8+ 词的原文短语进入骨架。骨架必须是句法抽象。
- **虚构复现性**：不声称某骨架"出现在多篇论文中"除非确实有证据。
- **泛化特殊组合**：不把 Incommensurability 的叙事模式套用到 Incompleteness，不把 Constructs 辨析套用到 Mechanism。
- **跳过薄弱模块**：即使原文某模块（如 Stakes）处理得很弱，也要如实记录，不能为了让骨架"好看"而美化。
- **强制覆盖所有模块**：如果某 Introduction 确实缺失某模块，记录为 missing，不捏造。
- **混淆 Gap 类型**：如果原文的 Gap 语言模糊，明确标记为 "ambiguous between Incompleteness and Inadequacy"，不强行分类。

---

## 反模式（蒸馏过程中主动排查）

| 反模式 | 表现 | 处理方式 |
|--------|------|----------|
| **原文依赖型骨架** | 骨架中包含论文特有的现象名、行业名、具体学者名 | 泛化为 [phenomenon] / [industry] / [scholars] |
| **过度抽象** | 骨架抽象到只剩 "We study X"，失去组织叙事的启示 | 保留关键功能短语（"This omission is theoretically important because" / "A consensus is building that"） |
| **Gap 类型错配** | 将 Inadequacy 的 "overlooks" 语言标记为 Incompleteness | 在骨架中标注准确的 Gap 适用范围 |
| **忽略 Stakes 缺失** | 只提取"写得好的"部分，忽略原文 Introduction 的薄弱点 | 在 Rhetorical Logic 和 QC 中明确记录薄弱点 |
| **批量同质化** | 批量处理时忽视 Gap 类型差异，用同一套骨架覆盖不同组合 | Phase 0 分类必须先行，不同 Gap 类型分桶处理 |
| **混淆 Puzzle 与 Gap** | 将 "few studies have examined" 记录为 Puzzle 陈述 | Puzzle 必须是 broad management question；Gap 是文献中的具体遗漏 |

---

## 与下游 Skill 的接口

- **`write-introduction`** — Phase 4 的更新建议直接修改此 skill 的模块库和骨架库；Phase 6 成品验证接收 write-introduction 的 metadata 作为参考基准
- **`diagnose-introduction`** — Phase 0 的组合分类可作为 diagnose 的验证基准
- **`intro-review`** — Phase 1.5 的模块覆盖检查可作为 intro-review 的预检清单；Phase 6 的验证报告可作为 intro-review 的预诊断输入
- **`paper-review`** — Rhetorical Logic Map 可用于跨 section 对齐检查（Introduction 承诺 vs Discussion 兑现）
- **Vault** — Fine-Grained Profile 存入 Vault 的 `fine_grained/batch_*/[paper]_distilled_introduction.md`；Phase 6 验证报告存入 `fine_grained/validation_runs/`

## 外部资产位置

- **现有语料库索引**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/introduction/mvp30/_mvp30_introduction_index.md`
- **蒸馏产出存放**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/introduction/mvp30/fine_grained/batch_*/[paper]_distilled_introduction.md`
- **更新建议存放**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/introduction/mvp30/skill_update_recommendations/`
- **成品验证报告存放**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/introduction/mvp30/fine_grained/validation_runs/[date]_validation_report.md`

## JSON Output Schema

当使用 `--output-format=json` 时，输出严格符合以下 schema。

```json
{
  "$schema": "distill-introduction-exemplar-batch/v1",
  "paper_id": "string",
  "phase_0_combo_profile": {
    "gap_type": "string",
    "contribution_dimension": "string",
    "conversation_strategy": "string",
    "hook_energy_level": "string",
    "narrative_structure": "string",
    "introduction_length": "number",
    "paragraph_count": "number",
    "has_explicit_puzzle_statement": "boolean",
    "has_stakes_paragraph": "boolean"
  },
  "phase_1_module_map": {
    "I1_hook": { "located": "boolean", "paragraph_range": "string", "hook_type": "string", "hook_energy_level": "string", "serves_puzzle": "boolean" },
    "I2_conversation": { "located": "boolean", "paragraph_range": "string", "conversation_strategy": "string", "core_citations_count": "number", "establishes_common_ground": "boolean" },
    "I3_problematization": { "located": "boolean", "paragraph_range": "string", "gap_type_language": "string", "beyond_few_studies": "boolean", "has_specific_pain": "boolean" },
    "I4_stakes": { "located": "boolean", "paragraph_range": "string", "stakes_type": "string", "quantified": "boolean" },
    "I5_theory_lens": { "located": "boolean", "paragraph_range": "string", "theoretical_source": "string", "responds_to_gap": "boolean" },
    "I6_preview": { "located": "boolean", "paragraph_range": "string", "preview_scope": "string", "overclaiming_risk": "boolean" },
    "I7_contribution": { "located": "boolean", "paragraph_range": "string", "makadok_dimensions_visible": ["string"], "discussable": "boolean" }
  },
  "phase_1_5_quality_gate": {
    "module_coverage": { "required_modules": ["string"], "present_modules": ["string"], "missing_modules": ["string"], "coverage_rate": "string" },
    "combo_alignment": { "detected_combo": "string", "properly_addressed": ["string"], "inadequately_addressed": ["string"] },
    "narrative_sufficiency": { "puzzle_stated_explicitly": "boolean", "common_ground_established": "boolean", "departure_point_clear": "boolean", "audience_implied": "boolean", "transition_chain_continuous": "boolean" },
    "contradictions_or_gaps": ["string"],
    "information_poverty_dimensions": ["string"]
  },
  "phase_2_distillation": {
    "I1_hook": {
      "persuasive_action": "string",
      "expression_skeletons": [{ "skeleton": "string", "transferability": "string", "paradigm_exclusivity": "string", "gap_variants": ["string"], "dorobantu_question": "string" }],
      "rhetorical_logic": { "audience_alignment": "string", "puzzle_gap_rq_layering": "string", "contribution_contract": "string" }
    }
  },
  "phase_3": {
    "module_density": "number",
    "hook_to_puzzle_distance": "number",
    "few_studies_density": "number",
    "tension_depth": "number",
    "stakes_specificity": "string",
    "transition_chain_completeness": "number",
    "theory_lens_responsiveness": "string",
    "makadok_visibility": "number",
    "jtbd_coverage": "number",
    "contribution_discussability": "string"
  },
  "phase_4_corpus_reference": {
    "vault_enrichment": {
      "new_skeletons_for_reference": [{ "module": "string", "gap_type": "string", "skeleton": "string", "source_papers": ["string"], "vault_path": "string", "note": "string" }],
      "patterns_to_note": [{ "module": "string", "gap_type": "string", "observation": "string", "note": "string" }],
      "new_anti_patterns": [{ "pattern": "string", "evidence": "string" }],
      "new_honesty_boundaries": [{ "boundary": "string", "source": "string" }]
    },
    "batch_metadata": {
      "total_papers_processed": "number",
      "combo_distribution": "object",
      "novel_skeletons_found": "number",
      "rejected_skeletons": "number",
      "rejected_reasons": ["string"]
    }
  },
  "phase_2_4_skeleton_critic": {
    "skeleton_id": "string",
    "verdict": "VALIDATED / REVISE / REJECT",
    "verdict_reason": "string",
    "generativity_test": { "mock_paragraph_generated": "boolean", "persuasive_action_preserved": "boolean", "notes": "string" },
    "fact_boundary_test": { "paper_specific_contamination": ["string"], "contamination_cleared": "boolean" },
    "type_fidelity_test": { "gap_type_match": "boolean", "mismatch_details": "string" }
  },
  "narrative_style_profile": {
    "tone": "string",
    "tone_evidence": "string",
    "paragraph_rhythm": "string",
    "module_ratio": { "I1": "number", "I2": "number", "I3": "number", "I4": "number", "I5": "number", "I6": "number", "I7": "number" },
    "distinctive_features": [{ "feature": "string", "example": "string" }],
    "avoids": [{ "avoid": "string", "function": "string" }],
    "quality_markers": { "what_makes_effective": "string", "strongest_aspect": "string", "weakest_aspect": "string" }
  },
  "narrative_risk_ledger": [
    { "risk_id": "string", "discovery_phase": "string", "risk_type": "string", "original_manifestation": "string", "mimicry_consequence": "string", "recommended_handling": "string" }
  ],
  "phase_5_qc": {
    "completeness": "boolean",
    "clarity": "boolean",
    "credibility": "boolean",
    "replicability": "boolean",
    "no_verbatim_copy": "boolean",
    "fact_boundary": "boolean",
    "gap_type_fidelity": "boolean",
    "dorobantu_coverage": "boolean",
    "combo_honesty": "boolean",
    "overall_status": "PASS / FLAG / REJECT"
  },
  "phase_6_validation": {
    "validation_mode": "product_validation",
    "reference_metadata": { "$ref": "write-introduction/metadata" },
    "assembly_fidelity": {
      "module_coverage_rate": "number",
      "mandatory_pairings_satisfied": ["string"],
      "mandatory_pairings_broken": ["string"],
      "mutual_exclusion_violations": ["string"],
      "paragraph_count_deviation": "number",
      "deviation_matrix": [
        { "paragraph": "string", "recommended_module": "string", "actual_content": "string", "deviation_type": "module_replacement / module_missing / module_added / fidelity_ok", "severity": "high / medium / low" }
      ]
    },
    "promise_fulfillment": {
      "hook_to_puzzle": { "score": "number", "max": 3, "note": "string" },
      "gap_to_stakes": { "score": "number", "max": 3, "note": "string" },
      "theory_to_gap": { "score": "number", "max": 3, "note": "string" },
      "contribution_to_preview": { "score": "number", "max": 3, "note": "string" },
      "makadok_visibility": { "score": "number", "max": 3, "note": "string" },
      "four_questions": { "score": "number", "max": 4, "note": "string" },
      "overall_fulfillment_rate": "string"
    },
    "narrative_flow": {
      "transition_chain_score": "number",
      "transition_chain_max": 6,
      "weak_transitions": [{ "from": "string", "to": "string", "issue": "string" }]
    },
    "skeleton_generativity": {
      "validated_count": "number",
      "revise_count": "number",
      "reject_count": "number",
      "per_skeleton_assessment": [
        { "paragraph": "string", "module": "string", "key_phrases_preserved": "boolean", "persuasive_action_preserved": "boolean", "overfilling_risk": "low / medium / high", "verdict": "VALIDATED / REVISE / REJECT", "note": "string" }
      ]
    },
    "overall_rating": "ACCEPT / CONDITIONALLY_ACCEPT / NEEDS_REVISION / REJECT",
    "priority_fixes": [
      { "priority": "high / medium / low", "issue": "string", "current_state": "string", "recommendation": "string", "consequence_if_ignored": "string" }
    ],
    "post_validation_action": "direct_finalize / revise_and_revalidate / regenerate_assembly"
  }
}
```

---
*基于 nuwa-skill 流水线框架、Pollock 2025 Ch05、Dorobantu et al. (2024)、Simsek & Li (2022) JTBD 框架、MVP30 范文语料库构建。版本 1.0.0 — Introduction 蒸馏 Meta-Skill。*
