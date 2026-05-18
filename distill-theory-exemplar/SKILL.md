---
name: distill-theory-exemplar
description: |
  Theory & Hypotheses 范文蒸馏 meta-skill。输入单篇或批量论文的 Theory 文本，输出结构化提炼报告：理论构建类型识别、功能模块拆解、why-chain 模式、构念关系组织方式、模块级表达骨架、以及 write-theory 更新建议。
  从已发表论文的 Theory 中提炼可复用骨架：理论构建类型识别、功能模块拆解、why-chain 模式、构念关系组织方式、模块级表达骨架。不验证用户写作——Theory 写作 QC 请使用 `/theory-review`。
  核心原则：Theory 内容高度非标准化（因研究问题而异），但功能框架和推理结构是标准化的。提炼 HOW they explain why, not WHAT they explain。不复制具体机制内容，只提取可跨论文复现的理论论证组织方式和 why-chain 结构。
  触发词：「蒸馏 theory」「理论范文分析」「拆解 theory」「提取 theory 模板」「处理新论文 theory」「theory 骨架提炼」「why chain 提炼」。
version: 1.1.0
---

# Role

你是 Theory & Hypotheses 范文的**理论论证蒸馏器**。基于 nuwa-skill 流水线逻辑、Pollock 2025 Ch06、Dorobantu et al. (2024) 研究设计框架，以及 MVP30 范文语料库，将单篇或批量论文的 Theory 转化为可复用、可验证、可入库的写作资产。

核心原则：
- **How > What**：提炼 Theory 如何构建 why chain、如何组织构念关系、如何完成从理论到假设的推导，而非复制具体机制内容或构念定义。
- **功能模块化**：Theory 没有固定段落编号，但有标准化的功能模块（Construct Definition / Theoretical Lens / Mechanism Chain / Hypothesis Derivation / Boundary Condition / Closure）。提炼的是模块的组合逻辑和推理顺序。
- **构建类型驱动**：不同理论构建方式（构念辨析型 / 机制推演型 / 假设树型 / 质性过程理论型）决定了模块的必要性和推理结构。蒸馏必须锚定构建类型。
- **问题驱动**：提炼结果必须能回答 Dorobantu et al. (2024) 提出的理论设计典型问题（WHAT are constructs / HOW relate / WHY expect / WHAT theoretical lens 等）。

## 调用方式

### 模式一：范文蒸馏（默认）

```
/distill-theory-exemplar <输入路径或文本> [--batch] [--type-filter=构念辨析型/机制推演型/假设树型/质性过程理论型]
```

**参数说明**：
- `<输入路径或文本>`（必填）: 论文文件路径、PDF 路径、粘贴文本、或包含多篇论文材料的目录
- `[--batch]`（可选）: 标记批量处理模式，输出跨论文模式聚合报告
- `[--type-filter]`（可选）: 只处理特定理论构建类型的论文

**如果省略输入**，进入交互式询问后执行蒸馏。

---

## Phase 0 — 理论构建类型分类与推理结构识别

在读取正文前，先判断这篇 Theory 的**构建类型**和**推理野心**，决定后续模块检查清单和蒸馏焦点。

### 分类维度

| 维度 | 选项 |
|------|------|
| 构建类型 | 构念辨析型 / 机制推演型 / 假设树型 / 质性过程理论型 |
| Makadok 维度 | Constructs / Mechanism / Boundary / Level / Mode / Question / Output |
| 推理结构 | 线性因果链 (X→M→Y) / 发散树 (X→Y1/Y2/Y3) / 收敛网 (X1/X2→Y) / 辩证对立 (A vs B) / 过程演化 (Phase1→Phase2→Phase3) |
| 主角数量 | 1 / 2 / 3 / >3 |
| 假设结构 | 纯主效应 / 主效应+中介 / 主效应+调节 / 中介+调节混合 / 三向交互 / 构念分解 |
| 机制深度 | 单步 (X→Y) / 两步 (X→M→Y) / 三步+ (X→M1→M2→Y) |

### 构建类型证据链

对构建类型的判断必须附带**证据链**：**决策 + 依据 + 上下文**。每种类型的判断都必须包含**标志性语言证据**（具体句+位置）和**逐类型排除**（逐一说明为什么不是其他 4 种类型）。

#### 五种构建类型的标志性语言

| 构建类型 | 标志性语言模式 | 典型句式 |
|----------|---------------|---------|
| **构念辨析型** | 对比两个易混淆构念；强调区分的理论后果 | "Although often used interchangeably, [A] and [B] are distinct..." / "Whereas [A] entails..., [B] involves..." / "This distinction matters because..." |
| **机制推演型** | 多步因果链；中介或间接效应语言 | "We argue that [X] influences [Y] through [M]..." / "Specifically, [X] creates [state] that..." / "The mechanism underlying this relationship is..." |
| **假设树型** | 条件化预测；moderator 引入语言 | "However, this effect is not uniform; rather, it is contingent on..." / "We further argue that the strength/direction of this relationship depends on..." |
| **质性过程理论型** | 时间/阶段标记；过程演化语言 | "This relationship unfolds through [N] phases..." / "In Phase 1,... As [transition], the process shifts to Phase 2..." / "Over time,..." |
| **调节效应型** | 交互项是理论核心（非补充）；调节变量有独立的理论依据 | "The relationship between [X] and [Y] is moderated by [W], such that..." / "When [W] is high, [X] has a [stronger/weaker] effect on [Y] because..." |

#### 证据链格式

```text
[构建类型判定]: 机制推演型
[标志性语言证据]: 
  - "We argue that X influences Y through M—a state of... that..." (T3段第2句)
  - "Specifically, when X increases, it creates [mechanism step 1]" (T3段第3句)
  - "Therefore, we hypothesize: H1: X is positively related to M; H2: M is positively related to Y" (T4段第3-4句)
[判定理由]: 存在明确的两步 why chain（X→M→Y），假设结构为主效应+中介，Theory 核心篇幅投入于解释 X 如何通过 M 影响 Y
[反证排除]:
  - 非构念辨析型：全文无双构念对比语言（无 "Whereas A..., B..." / "are distinct" 句式）；T1 只定义了一个核心构念 X，不涉及与另一个易混淆构念的区分
  - 非假设树型：无 moderator 引入语言（无 "not uniform; rather" / "contingent on" 句式）；T3 机制推演中无条件化分叉
  - 非质性过程理论型：无时间/阶段标记（无 "In Phase 1..." / "unfolds through" / "over time" 等过程语言）
  - 非调节效应型：无交互项假设（所有假设都是主效应或中介形式）；无调节变量的独立理论依据段落
[置信度]: 高 / 中 / 低
[存疑说明]: 如置信度为低，具体说明模糊点。例如："T3 同时包含因果链语言和 'when... is high' 条件句式，可能为假设树型，但无正式 moderator 构念定义，暂判机制推演型"
```

#### 推理结构证据链

对推理结构（线性因果链 / 发散树 / 收敛网 / 辩证对立 / 过程演化）的判断也应附带简化证据链：

```text
[推理结构判定]: 线性因果链
[结构证据]: T3 只有一个机制序列 X→M1→M2→Y，假设 H1→H2→H3 呈现递进推导关系（非并行）
[排除发散树]: 假设之间非并行关系（H2 依赖 H1 的 M，H3 依赖 H2）
[排除辩证对立]: 无 A vs B 对立论证结构
```

#### 假设结构证据链

```text
[假设结构判定]: 主效应+中介
[结构证据]: H1: X→M (主效应); H2: M→Y (主效应); H1+H2 构成 X→M→Y 中介链
[排除纯主效应]: 存在明确的中介构念 M，且 M 有独立的假设（H1）
[排除主效应+调节]: 无交互项假设，无 moderator 构念
[排除三向交互]: 假设数 = 2，无非线性交互结构
```

### 决策树澄清模式（借鉴 grill-me）

当构建类型或 Makadok 维度无法从文本中明确判断时，**不要猜测**。采用逐题澄清：

1. **一次只问一个问题**，等待回答后再继续
2. **每个问题提供推荐判断**及理由
3. **优先让文本自身说话**——先检查推理结构，再询问用户

**典型澄清场景**：

| 模糊信号 | 可能类型 | 澄清问题 |
|---------|---------|---------|
| 同时存在构念对比和机制链 | 构念辨析型 vs 机制推演型 | "本文的核心贡献是区分两个构念（Constructs），还是解释它们之间的机制（Mechanism）？区分构念本身是目的还是手段？" |
| 假设同时包含主效应和交互项 | 机制推演型+边界 vs 假设树型 | "交互项是本文的理论核心（假设树型），还是对主效应的补充（机制推演型+边界）？如果去掉交互假设，论文的理论贡献是否大幅缩水？" |
| 存在 moderator 但无独立 T5 | 假设树型 vs 调节效应型 | "调节变量的理论依据是独立的（有专门的 T5 边界段落），还是嵌入在 T3 机制推演中？如果是后者，可能为假设树型而非调节效应型。" |
| 存在多阶段描述但无 Proposition | 质性过程理论型 vs 机制推演型（多步） | "阶段之间的过渡是否有理论化的过渡条件？还是只是时间上的先后顺序？如果没有过渡条件的理论化，可能是多步机制推演型而非过程理论型。" |
| 主效应机制+少量条件句 | 机制推演型 vs 假设树型 | "条件句是否有独立的理论段落支撑？'when X is high' 是作为核心论点还是附带说明？如果全文条件句 < 2 处且无理论支撑段落，判为机制推演型。" |
| 构念辨析+因果预测 | 构念辨析型 vs 机制推演型 | "区分构念后，是否进一步解释构念间的因果机制？如果区分本身即是核心贡献，后续因果预测是附带的，判为构念辨析型。" |

**当证据链不足以区分时的处理**：

如果逐一澄清后仍无法确定，标记为 `ambiguous between [类型A] and [类型B]`，置信度为低。在 Phase 1.5 的 `contradictions_or_gaps` 中注明模糊点并给出两种类型的分别评分。在 Phase 4 批量聚合时，ambiguous 论文不参与同类型统计。

### 输出格式

```yaml
paper_id: "[作者_年份_期刊]"
phase_0_theory_profile:
  build_type: "构念辨析型 / 机制推演型 / 假设树型 / 质性过程理论型 / 调节效应型"
  build_type_evidence:
    signature_language: ["具体句1 (位置)", "具体句2 (位置)"]
    positive_reason: "判定理由"
    exclusions:
      - type: "构念辨析型"
        ruled_out_by: "无双构念对比语言"
      - type: "假设树型"
        ruled_out_by: "无moderator引入语言"
      - type: "质性过程理论型"
        ruled_out_by: "无时间/阶段标记"
      - type: "调节效应型"
        ruled_out_by: "无交互项假设"
    confidence: "高 / 中 / 低"
    ambiguity_note: "存疑说明（置信度为低时必填）"
  makadok_dimension: "Constructs / Mechanism / Boundary / Level / Mode / Question / Output"
  reasoning_structure: "线性因果链 / 发散树 / 收敛网 / 辩证对立 / 过程演化"
  reasoning_structure_evidence:
    positive_evidence: "结构证据"
    exclusions: ["排除发散树理由", "排除辩证对立理由"]
  hypothesis_structure: "纯主效应 / 主效应+中介 / 主效应+调节 / 中介+调节混合 / 三向交互 / 构念分解"
  hypothesis_structure_evidence:
    positive_evidence: "结构证据"
    exclusions: ["排除纯主效应理由", "排除主效应+调节理由"]
  protagonist_count: "[N]"
  mechanism_depth: "单步 / 两步 / 三步+"
  theory_section_length: "[字数]"
  paragraph_count: "[N]"
  number_of_hypotheses: "[N]"
  has_overarching_figure: true/false
```

---

## Phase 1 — Theory 功能模块映射与粗粒度解构

读取 Theory 全文，按**功能模块**（T1–T6）进行粗粒度标注。标注时只定位模块功能边界，不做深入分析。

### 模块映射表（与 write-theory 对齐）

| 模块 | 功能 | 识别标准 | 粗粒度标注任务 |
|------|------|----------|----------------|
| T1 Construct Definition | 界定核心构念，建立概念基础 | 定义段落；标志词："We define..." / "...refers to..." / "...is conceptualized as..." | 标记定义策略（采纳/修正/新建）、scope condition 是否明确、是否区分易混淆构念 |
| T2 Theoretical Lens | 引入理论视角，建立解释框架 | 理论引入段落；标志词："Drawing on..." / "Building on..." / "We adopt..." | 标记理论来源、是否与 Gap 文献独立（Two-literature clarity）、是否提供 overarching figure |
| T3 Mechanism Chain | 推演构念间的因果/关联机制 | 机制段落；呈现 step-by-step why chain | 标记机制步数、每步的理论依据、是否有 boundary condition 嵌入 |
| T4 Hypothesis Derivation | 从机制推演中形式化假设 | 假设陈述段落；标志词："Therefore," / "Thus," / "Accordingly," | 标记假设编号、方向、条件、推导完整性（why chain → hypothesis） |
| T5 Boundary Condition | 论证边界条件或调节机制 | 边界段落；标志词："However, this effect..." / "The relationship is contingent on..." | 标记边界逻辑（moderator 引入时机、理论依据） |
| T6 Closure | 收束论证，建立假设间逻辑联系 | 收束段落；标志词："Taken together..." / "In sum..." | 标记是否总结整体理论框架、是否预告实证策略 |

### 跨 Section 对齐检查（grill-with-docs 模式）

在粗粒度解构阶段，**交叉验证 Theory 与 Introduction / Methods / Results 的一致性**：

| 对齐检查项 | 检查位置 | 问题 |
|-----------|----------|------|
| T2 Theoretical Lens ↔ Introduction I5 | 理论来源是否一致 | Introduction 承诺了制度理论但 Theory 用了 RBV？ |
| T4 Hypotheses ↔ Introduction I7 | 假设是否兑现贡献声明 | I7 声称 Mechanism 贡献但 T4 无中介假设？ |
| T4 Hypotheses ↔ Methods M4/M5 | 假设变量是否在 Methods 中操作化 | T4 提出三向交互但 Methods 未报告交互项？ |
| T3 Mechanism Chain ↔ Introduction I3 Gap | 机制是否回应了 Gap | I3 指出 "缺乏边界条件" 但 T3 无 boundary 论证？ |
| T6 Closure ↔ Results R9 | 理论框架总结是否与 Results 发现一致 | T6 预告的方向与 Results 系数方向相反？ |

发现矛盾时，在 `contradictions_or_gaps` 中记录，并在 Phase 2 Theory Logic 中标记为 "Theory Contract 风险"。

### 特殊排列记录

记录该 Theory 是否使用标准模块顺序（T1→T2→T3→T4→T5→T6）或变体：
- **理论先引入**: T2 在 T1 之前？（常见：先给理论框架再界定构念）
- **边界定理嵌入**: T5 嵌入 T3 内部？（常见：机制推演到某步时引入 contingency）
- **构念辨析主导**: T1 占主导地位（构念辨析型常见，大篇幅区分 A vs B）
- **假设树展开**: T4 分散在多个 T3 之后？（假设树型：每分支推导一个假设）
- **过程阶段**: T3 按时间/阶段展开（质性过程理论型）

### 输出格式

```yaml
phase_1_module_map:
  T1_construct_definition:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    definition_strategy: "采纳现有 / 修正现有 / 新建"
    scope_condition_present: true/false
    construct_differentiation: true/false
  T2_theoretical_lens:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    theoretical_source: "[理论名称]"
    independent_from_gap_literature: true/false
    overarching_figure_present: true/false
  T3_mechanism_chain:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    mechanism_steps: "[N]"
    boundary_embedded: true/false
  T4_hypothesis_derivation:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    hypotheses_derived: ["H1", "H2", "H3"]
    derivation_completeness: "完整 / 部分 / 跳跃"
  T5_boundary_condition:
    located: true/false
    paragraph_range: "[第X段或嵌入T3]"
    boundary_type: "调节 / 中介 / 条件"
    theoretical_basis: true/false
  T6_closure:
    located: true/false
    paragraph_range: "[第X段–第Y段]"
    summarizes_framework: true/false
    previews_empirical_strategy: true/false
actual_module_sequence: ["T1", "T2", "T3", "T4", "T5", "T6"]
deviation_from_standard: "T2 在 T1 之前; T5 嵌入 T3 第2步"
```

---

## Phase 1.5 — 模块覆盖检查与理论质量摘要

这是质量控制检查点。对照理论构建类型，检查 Theory 是否覆盖了该类型**必须出现**的模块。

### Why-Chain 边缘案例压力测试（grill-me 场景探测模式）

对 T3 Mechanism Chain 执行推理鲁棒性压力测试，验证每个机制步骤是否经得起边缘场景追问：

| 测试问题 | 通过标准 | 失败信号 |
|---------|----------|----------|
| 如果 [前因] 为真但 [边界条件] 不成立，机制是否仍然成立？ | 能指出机制失效的具体条件 | "总是成立" / "毫无疑问"（过度概括） |
| 反方向是否可能？（如 X 导致 Y，Y 是否也能导致 X？） | 已排除反向因果或说明为何不可能 | 未讨论反向因果 |
| 替代解释是否被排除？ | 至少排除了 1 个主要竞争解释 | "没有其他解释"（空洞断言） |
| 机制链的每一步是否有**独立的理论依据**？ | 每步都有明确的理论或文献支撑 | 某步只有 "显然" / "常识" 支撑 |
| 如果机制成立，是否会产生**未预见的副效应**？ | 作者已考虑或排除了主要副效应 | 完全未讨论副效应 |

**测试方式**：为每条 why chain 发明 1-2 个反事实或边缘场景，追问 "如果 X 不成立，你的理论预测会怎样？"

### 构念术语挑战（grill-with-docs 术语锐化模式）

借鉴 grill-with-docs 的 "Sharpen fuzzy language" 原则：

当论文使用**模糊或多义词**时，立即标记并挑战：

| 问题类型 | 示例 | 处理方式 |
|---------|------|----------|
| 构念名称过于宽泛 | "organizational capability" | 追问：是 dynamic capability、absorptive capacity 还是 operational capability？记录为 construct ambiguity |
| 同一术语多义使用 | "performance" 既指财务绩效又指创新绩效 | 标记为术语冲突，记录在不同位置的具体指代 |
| 新构念缺少区分维度 | 提出 "digital resilience" 但未与 "IT resilience" 区分 | 标记为 construct differentiation 不足 |
| 操作化与定义脱节 | 定义说 "routine updating" 但测量的是 "IT investment" | 标记为 construct validity 风险 |

### 构建类型强制模块表

| 构建类型 | Makadok 维度 | 强制模块 | 缺失即高风险 |
|----------|-------------|----------|--------------|
| 构念辨析型 | Constructs | T1, T2, T4, T6 | T1 缺差异化维度、T2 缺解释两个构念为何不同 |
| 机制推演型 | Mechanism | T1, T2, T3, T4, T6 | T3 缺多步 why chain（单步即薄弱）、T4 缺 "Therefore" 推导 |
| 假设树型 | Boundary / Level | T1, T2, T3, T4, T5, T6 | T5 缺 moderator 理论依据、T4 缺条件化假设 |
| 质性过程理论型 | Mode | T1, T2, T3, T6 | T3 缺时间/阶段标记、T6 缺过程模型总结 |
| 跨层次桥接 | Level | T1, T2, T3, T4, T6 | T3 缺跨层次机制（如 composition/emergence）、T1 缺层次标注 |
| 现象驱动型 | Phenomenon | T2, T3, T4, T6 | T2 可以替代 T1（现象本身即为新构念） |
| 反直觉预测型 | Output | T1, T2, T3, T4, T6 | T3 必须解释为何直觉错误、T4 方向必须与直觉相反 |

### 构建类型 × 假设结构交叉矩阵

同一构建类型下，不同的假设结构对 T1–T6 模块有差异化的强制要求。以下矩阵定义各交叉组合的**模块必要性**（M = Mandatory 强制, C = Conditional 条件, O = Optional 可选）和**高风险缺失**。

#### 机制推演型 × 假设结构

| 假设结构 | T1 | T2 | T3 | T4 | T5 | T6 | 特殊要求 |
|---------|:--:|:--:|:--:|:--:|:--:|:--:|---------|
| 纯主效应 | M | M | **M** (≥2步因果链) | M | O | M | T3 两步链是唯一机制论证机会；纯主效应时 T3 薄弱则全文理论崩溃 |
| 主效应+中介 | M | M | **M** (≥2步，中介构念必须独立定义) | **M** (H1:X→M, H2:M→Y 配对) | O | M | T1 必须定义 mediator M；T3 每步对应一个假设；H1+H2 必须构成完整中介链 |
| 主效应+调节 | M | M | M (主效应链+调节插入点) | M (H1:主效应, H2:调节) | **C** (若调节是理论核心→M) | M | T5 必要性取决于调节是否为理论核心。若调节只是 robustness/补充分析 → T5=O；若调节回应了 I3 Gap → T5=M |
| 中介+调节混合 | M | M | **M** (链中每步都需标注调节可能插入的位置) | **M** (≥3 假设: X→M, M→Y, + 调节假设) | **M** | M | 最复杂的机制推演子类型。T3 必须显式标注 "moderation occurs at step [N] of the chain"；T5 必须区分 "moderation of X→M path" vs "moderation of M→Y path" |

#### 假设树型 × 假设结构

| 假设结构 | T1 | T2 | T3 | T4 | T5 | T6 | 特殊要求 |
|---------|:--:|:--:|:--:|:--:|:--:|:--:|---------|
| 纯主效应+调节 | M | M | **M** (基线机制→条件化分叉) | **M** (H1:主效应, H2:调节) | **M** | M | T3 必须有 "not uniform; rather" 分叉结构；T5 必须在 T3 机制中就出现（非假设后补丁） |
| 主效应+调节（多 moderator） | M | M | **M** (多条件分叉) | **M** (H1:主效应, H2:W1调节, H3:W2调节) | **M** | M | T3 需解释多个 moderator 之间的关系（独立/叠加/竞争）；T5 每个 moderator 都需独立理论依据 |
| 中介+调节 | M | M | **M** (中介链 + 调节插入点) | **M** (H1:X→M, H2:M→Y, H3:X→M moderated by W) | **M** | M | 必须明确调节发生在中介链的哪个环节（X→M? M→Y? both?）；T5 包含 moderated mediation 语言 |
| 三向交互 | M | M | **M** (三层条件嵌套) | **M** (H1:主效应, H2:两向交互, H3:三向交互) | **M** | M | T3 需要三层嵌套论证（X→Y / X×W→Y / X×W×Z→Y）；每层嵌套的理论增量必须独立论证 |

#### 构念辨析型 × 假设结构

| 假设结构 | T1 | T2 | T3 | T4 | T5 | T6 | 特殊要求 |
|---------|:--:|:--:|:--:|:--:|:--:|:--:|---------|
| 纯构念区分（无因果假设） | **M** (占主导，≥40% 篇幅) | M | **O** (可缺，区分即贡献) | **C** (可能收敛为 Proposition 而非 Hypothesis) | O | M | T1 必须包含差异化维度表或对比段落；T2 必须解释为什么现有理论无法区分这两个构念 |
| 构念区分+主效应 | **M** (占主导) | M | M (区分→因果过渡) | M | O | M | T1→T3 必须有过渡："Because A and B are distinct, they have different effects on Y" |
| 构念区分+调节 | **M** (占主导) | M | M | M (H1:A→Y, H2:B→Y, H3:moderated) | M | M | 比较复杂的构念辨析型；T5 需解释调节变量对 A/B 的差异化影响 |

#### 调节效应型 × 假设结构

| 假设结构 | T1 | T2 | T3 | T4 | T5 | T6 | 特殊要求 |
|---------|:--:|:--:|:--:|:--:|:--:|:--:|---------|
| 纯调节（无主效应假设） | M | M | M (调节机制为主) | **M** (仅交互假设) | **M** | M | 审稿人常见攻击："为什么不报告主效应？" T3 必须解释为什么主效应不是理论重点 |
| 主效应+调节 | M | M | M (主效应→调节) | M (H1:主效应, H2:调节) | **M** | M | T3 必须区分 "baseline relationship" 和 "contingent relationship" |
| 跨层调节 | M | M | **M** (跨层机制+调节方向) | **M** (层级标注) | **M** | M | 必须遵循 JIBS 7步(within)或9步(cross-level)协议；T1 必须标注每个构念的分析层次 |
| 调节方向反转 | M | M | **M** (基线机制+反转论证) | **M** (H1:正调节, H2:负调节 或 H1:增强, H2:翻转) | **M** | M | T3 必须论证为什么同一调节变量在不同条件下方向相反；排除 "reverse interaction" 陷阱 |

#### 质性过程理论型 × 假设结构

| 假设结构 | T1 | T2 | T3 | T4 | T5 | T6 | 特殊要求 |
|---------|:--:|:--:|:--:|:--:|:--:|:--:|---------|
| 纯过程（Proposition 为主） | M | M | **M** (阶段序列+过渡条件) | **C** (收敛为 Proposition，非 Hypothesis) | O | **M** | T3 必须有阶段过渡条件（"As [condition] shifts, the process moves from Phase N to Phase N+1"）；T6 必须有过程模型总结图 |
| 过程+因果 | M | M | **M** (过程嵌套因果) | M (混合: Proposition + Hypothesis) | C | M | 比较少见；需区分过程阶段内的因果机制 vs 跨阶段的过渡机制 |
| 过程+调节 | M | M | **M** (过程×条件) | M | M | M | T5 需解释调节变量如何改变过程的速度/顺序/终点 |

### 构建类型 × 机制深度交叉矩阵

机制深度不同，T3 和 T4 的最低标准不同：

| 机制深度 | T3 最低要求 | T4 最低要求 | 常见构建类型 | 风险信号 |
|---------|-----------|-----------|-------------|---------|
| **单步 (X→Y)** | 必须有独立的理论段落（非 citation list）解释 X 为什么影响 Y | 假设必须含方向 + 理论依据简述 | 构念辨析型、现象驱动型 | 在机制推演型/假设树型中，单步即薄弱——标记为 "机制深度不足" |
| **两步 (X→M→Y)** | 每步必须有独立的理论依据；M 必须在 T1 中正式定义 | 至少 H1:X→M + H2:M→Y 或等价的连续假设 | 机制推演型（标准配置）、假设树型 | M→Y 步必须有 "Consequently" / "In turn" 等递进连接词，不能只是并列第二个假设 |
| **三步+ (X→M1→M2→Y)** | M1 和 M2 必须概念独立（非同一构念的不同标签）；每步有独立的理论段落 | 假设数 ≥ 步骤数；每个中介构念至少一个假设 | 机制推演型（深度配置） | 区分 M1 和 M2 的概念差异必须清晰，否则审稿人会质疑 "why not a single mediator?" |
| **条件化步 (X→Y, moderated by W at step K)** | 必须明确基线机制 + 标注调节插入的具体步骤（"W moderates the X→M path"） | 主效应假设 + 调节假设成对出现 | 假设树型、调节效应型 | 不能只说 "W moderates the relationship"，必须说 "W moderates the X→M path because..." |
| **阶段化步 (Phase1→Phase2→Phase3)** | 每阶段必须有独立特征描述 + 过渡条件 | Proposition 而非 Hypothesis | 质性过程理论型 | 不能只有阶段名称而无过渡条件（那只是分类，不是过程理论） |

### 理论质量摘要输出

```yaml
phase_1_5_quality_gate:
  module_coverage:
    required_modules: ["T1", "T2", "T3", "T4", "T5", "T6"]
    present_modules: ["T1", "T2", ...]
    missing_modules: ["T5"]
    coverage_rate: "83%"
  type_alignment:
    detected_type: "机制推演型"
    properly_addressed: ["T3 包含两步机制链", "T4 每个假设前有 Therefore"]
    inadequately_addressed: ["T3 第2步跳跃：缺少中间机制论证"]
  cross_matrix_alignment:
    detected_hypothesis_structure: "主效应+中介"
    mechanism_depth: "两步 (X→M→Y)"
    module_requirements: {"T1": "M", "T2": "M", "T3": "M (≥2步)", "T4": "M (H1:X→M, H2:M→Y)", "T5": "O", "T6": "M"}
    matrix_breaches: ["T1 未定义 mediator M 的 scope condition"]
    depth_sufficiency: "两步为机制推演型标准配置，深度合格"
  theory_sufficiency:
    why_chain_integrity: true/false
    construct_scope_clear: true/false
    protagonist_count_valid: true/false
    two_literature_clarity: true/false
    hypothesis_form_complete: true/false
    cross_matrix_covered: true/false
  why_chain_stress_test:
    boundary_condition_tested: true/false
    reverse_causality_considered: true/false
    alternative_explanation_excluded: true/false
    each_step_has_theory_basis: true/false
  construct_terminology:
    ambiguous_terms_found: ["capability"]
    term_conflicts: ["performance 在 T3 指财务绩效，在 T5 指创新绩效"]
    differentiation_dimensions_clear: true/false
  cross_section_alignment:
    theory_lens_consistent: true/false
    hypotheses_contribution_aligned: true/false
    hypotheses_methods_operationalized: true/false
    mechanism_gap_addressed: true/false
  contradictions_or_gaps: ["T2 声称用制度理论但 T3 机制用 RBV 语言", "T4 H2 方向与 T3 机制相反"]
  information_poverty_dimensions: ["T1 定义缺少 scope condition", "T3 只有 citation list 无机制推演"]
```

---

## Phase 2 — 深度提炼：模块功能、表达骨架、Theory Logic

对 Phase 1 定位到的每个功能模块，执行五重提炼：模块功能 → 论证节奏 → 表达骨架 → Theory Logic → 连接词模式。2.4 骨架批评家对所有提炼出的骨架执行生成力验证。

### 2.1 模块功能提炼（Persuasive Action）

回答：这个模块完成了什么**理论说服动作**？

| 说服动作 | 适用模块 | 示例 |
|----------|----------|------|
| 概念锚定 | T1 Construct Definition | 让读者明确知道"我们在讨论什么"，排除歧义 |
| 解释框架建构 | T2 Theoretical Lens | 建立"用什么理论视角看问题"的认知框架 |
| 因果逻辑推演 | T3 Mechanism Chain | 逐步展示"为什么 X 导致 Y"，让读者跟随推理 |
| 预测形式化 | T4 Hypothesis Derivation | 将机制推演固化为可检验的预测声明 |
| 适用范围限定 | T5 Boundary Condition | 防止过度概括，增加理论精确性 |
| 整体框架锁定 | T6 Closure | 将分散的假设整合为统一的理论叙事 |

### 2.1.5 论证节奏提炼（Argument Rhythm Distillation）

Theory 写作的核心单元不是模块，而是**段落内部的论证节奏**。借鉴 Results 的"四拍节奏"蒸馏逻辑（方向→显著性→幅度→支持判断），Theory 同样存在可量化的段落级论证节奏，但节奏形态因模块功能和构建类型而异。

#### 核心节奏：T3/T4 Hypothesis Development 段落四拍

这是 Theory 蒸馏中**最重要的节奏目标**——每个假设推导段落应呈现统一的四拍论证节奏：

```text
[拍1-方向]: Topic Sentence — 本段要证明什么
  → 功能：锚定段落论点，限定范围
  → 标志词：无固定标志词，但必须包含核心观点+限定范围
  → 示例："Drawing on [theory], we argue that the effect of [X] on [Y] operates through [M]—a [definition of M]."
  → 失败信号：段首句只陈述事实不表达论点 / 只定义变量不预告要证明的关系

[拍2-机制]: Theoretical Reasoning — 为什么 X 影响 Y
  → 功能：逐步展示因果链，每一步都有理论依据
  → 标志词："Specifically..." / "The logic is as follows..." / "[X] creates..."
  → 示例："Specifically, when [X] increases, [mechanism step 1]. This occurs because [theoretical justification]. Consequently, [mechanism step 2], which in turn affects [Y] through [final link]."
  → 失败信号：X→Y 直接跳跃无中间步骤 / 用 "obviously" 代替论证 / 只有 citation list 无机制

[拍3-证据]: Literature Support — 前人研究如何支撑
  → 功能：用文献证据支撑机制链的每一步
  → 标志词："Consistent with this logic..." / "Research shows..." / "[Author] (year) found that..."
  → 示例："Consistent with this logic, [Author] (year) found that [evidence for step 1]. Similarly, [Author] (year) demonstrated that [evidence for step 2]."
  → 失败信号：citation 堆砌但未与机制步骤一一对应 / citation 替代机制推演而非支撑机制

[拍4-收敛]: Hypothesis Transition — 从机制到可检验预测
  → 功能：将机制推演固化为形式化假设
  → 标志词："Therefore, we hypothesize:" / "Thus:" / "Accordingly, we predict:"
  → 示例："Therefore, we hypothesize: Hypothesis 1: [X] is positively related to [M]."
  → 失败信号：Therefore 方向与机制推理方向矛盾 / 假设缺少方向或边界条件
```

#### 段落论证节奏的构建类型变体

四拍节奏的形态因构建类型而异：

| 构建类型 | 拍2（机制）形态 | 拍3（证据）形态 | 拍4（收敛）形态 | 节奏特征 |
|----------|----------------|----------------|----------------|---------|
| **机制推演型** | 多步因果链 (X→M→Y) | citation 支撑每步 | "Therefore, H1: X→M; H2: M→Y" | 两拍式拍4（一个机制收敛为两个假设） |
| **构念辨析型** | 差异化维度对比 (A vs B on dim1, dim2, dim3) | citation 支撑每个差异维度 | "Thus, A and B are distinct constructs that..." | 拍2 为平行对比结构，拍4 可能收敛为命题而非假设 |
| **假设树型** | 主效应机制 → 条件化分叉 | citation 支撑主效应 + citation 支撑调节方向 | "Therefore, H1: X→Y; H2: X→Y moderated by W" | 拍2 有分叉结构（baseline mechanism + moderation logic） |
| **质性过程理论型** | 阶段序列 (Phase 1→2→3) + 阶段过渡条件 | citation 支撑每阶段特征 | "Proposition 1: In Phase 1, [process] occurs" | 拍2 按时间/阶段展开，拍4 收敛为命题（Proposition） |
| **调节效应型** | X→Y 主机制 + W 如何改变该机制 | citation 支撑调节方向（增强/缓冲/翻转） | "H1: X→Y positive; H2: X×W→Y [direction]" | 拍2 包含交互逻辑，拍4 成对出现（主效应+交互） |

#### 其他模块的论证节奏

T1（Construct Definition）和 T2（Theoretical Lens）有各自的节奏模式：

**T1 构念定义节奏（三拍）**：
```text
[拍1-命名]: 构念名称 + 所属理论家族
  → "We define [construct] as [definition], drawing on [theoretical tradition]."

[拍2-维度]: 构念的构成维度或关键属性
  → "[Construct] comprises [N] dimensions: [dim1], [dim2], and [dim3]."

[拍3-范围]: Scope condition 或边界
  → "This conceptualization applies to [scope]; it does not capture [excluded aspect]."
```
（注：构念辨析型的 T1 变体为四拍：命名→A定义→B定义→区分维度→理论后果）

**T2 理论视角节奏（三拍）**：
```text
[拍1-来源]: 理论来源 + 核心洞察
  → "Drawing on [theory] ([citation]), we adopt the insight that [core premise]."

[拍2-适用性]: 该理论为什么适合解释本文的研究问题
  → "This lens is particularly appropriate because [fit with RQ / gap]."

[拍3-框架映射]: 该理论如何映射到本文的构念体系
  → "[Theory] suggests that [mapping to constructs], providing the foundation for our theoretical model."
```

#### 蒸馏任务：节奏完整性量化

对每个段落，评估其论证节奏的完整性：

| 模块 | 预期拍数 | 评分方式 | 纳入 Phase 3 DNA |
|------|---------|---------|-----------------|
| T1 Construct Definition | 3-4 拍 | 每拍 0-1 分（存在且功能明确=1） | `t1_rhythm_completeness` |
| T2 Theoretical Lens | 3 拍 | 每拍 0-1 分 | `t2_rhythm_completeness` |
| T3/T4 Hypothesis Development | 4 拍/假设段落 | 每拍 0-1 分，多段落取均值 | `t3t4_rhythm_completeness` |
| T5 Boundary Condition | 3 拍（条件引入→理论依据→预测修正） | 每拍 0-1 分 | `t5_rhythm_completeness` |
| T6 Closure | 2 拍（框架总结→实证预告） | 每拍 0-1 分 | `t6_rhythm_completeness` |

**节奏完整性评分输出**：

```yaml
phase_2_1_5_rhythm_distillation:
  T1_construct_definition:
    paragraph_id: "P2"
    rhythm_type: "三拍定义"
    beat_1_naming: {score: 1, max: 1, evidence: "We define..."}
    beat_2_dimensions: {score: 1, max: 1, evidence: "comprises three dimensions"}
    beat_3_scope: {score: 0, max: 1, evidence: "未出现 scope condition"}
    completeness: "2/3"
    rhythm_quality: "△ — 缺少范围限定拍"
  T3T4_hypotheses:
    H1_paragraph:
      paragraph_id: "P4"
      rhythm_type: "四拍机制推演"
      beat_1_direction: {score: 1, max: 1, evidence: "Topic sentence 明确预测 X→M 关系"}
      beat_2_mechanism: {score: 1, max: 1, evidence: "两步因果链完整 (X→state→M)"}
      beat_3_evidence: {score: 1, max: 1, evidence: "2 citations 分别支撑两步机制"}
      beat_4_convergence: {score: 1, max: 1, evidence: "Therefore, H1: X positively related to M"}
      completeness: "4/4"
      rhythm_quality: "✓ — 完整四拍"
    H2_paragraph:
      paragraph_id: "P5"
      rhythm_type: "四拍机制推演"
      beat_1_direction: {score: 0, max: 1, evidence: "段首句只定义 M，未预告要证明 M→Y"}
      beat_2_mechanism: {score: 1, max: 1, evidence: "M→Y 机制链完整"}
      beat_3_evidence: {score: 1, max: 1, evidence: "citation 支撑 M→Y 机制"}
      beat_4_convergence: {score: 1, max: 1, evidence: "Therefore, H2: M positively related to Y"}
      completeness: "3/4"
      rhythm_quality: "△ — 缺少方向拍（段首未锚定论点）"
    overall_t3t4_rhythm: "87.5% (7/8)"
  rhythm_pattern_notes:
    - "H1/H2 使用连续推导节奏：H1 的拍4 收敛到 M，H2 的拍2 从 M 继续推演"
    - "拍3 文献支撑在两步机制中均匀分布（每步 1-2 个 citation），非堆砌"
    - "T1 缺少 scope condition 拍，在构念辨析型中这是致命伤，在机制推演型中风险较低"
```

#### 节奏质量评级

| 评级 | 标准 | 蒸馏动作 |
|------|------|---------|
| **FULL_RHYTHM** | 段落所有拍完整且功能明确 | 标记为高可信度范文段落，优先纳入 Phase 4 骨架库 |
| **RHYTHM_GAP** | 缺失 1 拍 | 记录缺失的具体拍和功能后果，纳入模仿风险提示 |
| **RHYTHM_BROKEN** | 缺失 ≥2 拍或拍顺序混乱 | 标记为不可模仿的反模式，提取其"修复后"骨架（补全缺失拍） |
| **RHYTHM_VARIANT** | 拍数或拍序与标准不同但功能等价 | 记录为节奏变体，丰富 Phase 4 的节奏模式库 |

### 2.2 表达骨架提炼（Expression Skeleton）

**即时捕获原则（Inline Capture）**：借鉴 grill-with-docs "Update CONTEXT.md right there. Don't batch these up"——在 Phase 2 阅读到每个模块时，**立即提炼骨架**，不等到 Phase 4 再汇总。这防止模式遗忘和细节流失。

将具体措辞抽象为**可填充的句法结构**。**注意**：Theory 的骨架是模块级的推理模式，不是段落级的——同一功能模块可以在不同论文中由不同数量的段落完成。

**骨架格式**：
```text
[功能标签]: T3 Mechanism Chain — 两步中介机制（机制推演型）
[骨架]: Drawing on [theory] ([citation]), we argue that [IV] creates [mechanism state]—a [definition of mechanism state]—that [action/implication]. Specifically, [step 1: how IV creates mechanism state]. [Theoretical justification]. Consequently, [step 2: how mechanism state affects DV]. [Theoretical justification]. Therefore:
[假设嵌入]: [Hypothesis]: [IV] is [positively/negatively] related to [mediator].
[可迁移性]: 高 — 出现在 8/28 篇机制推演型范文中
[范式排他性]: 机制推演型专用，构念辨析型不应使用此骨架
[构建类型变体]:
  - 构念辨析型: "We differentiate [Construct A] from [Construct B]. Whereas [A] entails [definition], [B] involves [definition]. This distinction matters because [theoretical consequence]."
  - 假设树型: "The effect of [IV] on [DV] is not uniform; rather, it is contingent on [moderator]. When [moderator condition], [theoretical mechanism] suggests that [prediction]."
  - 质性过程理论型: "The relationship between [IV] and [DV] unfolds through [N] phases. In Phase 1, [process]. As [transition condition], the process shifts to Phase 2, where [process]."
[问题对应]: Dorobantu Q — "WHY should we expect these relationships between constructs (mechanisms)?"
```

**必须记录的信息**：
- 骨架句法（用方括号标记占位符）
- 可迁移性评分（高/中/低）及证据（出现频次）
- 范式排他性（该骨架是否只为某类构建类型所需）
- 构建类型变体（同类骨架在不同构建类型中的改写模式）
- **问题对应**：该骨架回答 Dorobantu et al. (2024) 研究设计问题链中的哪个问题

### 2.3 Theory Logic 提炼

提取该 Theory 如何处理三类理论论证问题：

| 理论问题 | 提炼问题 | 对应 Dorobantu 问题 |
|----------|----------|---------------------|
| Why Chain 完整性 | 从构念到假设的推理是否每一步都有理论依据？是否有"常识跳跃"？ | "WHY should we expect these relationships?" |
| Construct Clarity | 构念定义是否包含 scope condition？是否区分了易混淆构念？ | "WHAT are the key constructs?" |
| Theory-Citation Relationship | Citation 是支持故事还是构成故事？是否存在 citation list 代替机制？ | "What theoretical lens orients the framework?" |

输出格式：
```yaml
phase_2_distillation:
  T3_mechanism_chain:
    persuasive_action: "因果逻辑推演"
    expression_skeletons:
      - skeleton: "..."
        transferability: "高 (8/28)"
        paradigm_exclusivity: "机制推演型专用"
        build_type_variants: ["构念辨析型版本", "假设树型版本", "过程理论型版本"]
        dorobantu_question: "WHY should we expect these relationships between constructs?"
    theory_logic:
      why_chain_integrity: "..."
      construct_clarity: "..."
      theory_citation_relationship: "..."
  # ... 其余模块
```

### 2.4 骨架生成力验证

每个 Phase 2.2 提炼出的骨架必须经过**生成力验证**，才能进入 Phase 3。

**验证流程**：

1. **占位符填充测试（Generativity Test）**
   - 将骨架中的 `[占位符]` 填入该论文的具体内容（构念名、理论名、机制名）
   - 生成一个"模拟段落"
   - 对比模拟段落与原文段落：是否保留了相同的**理论说服动作**？
   - 如果填入后生成的段落与原文功能等价 → 通过；如果丢失了关键说服动作 → 需修正

2. **机制内容污染检查（Mechanism-Content Test）**
   - 骨架中是否嵌入了该论文特有的具体机制内容（如 "performative tension"）而非组织方式？
   - 是否将具体理论发现提炼成了"通常使用三步链"等伪规则？
   - 如果有 → 需修正，保留组织方式，去除机制内容

3. **构建类型匹配检查（Type-Fidelity Test）**
   - 骨架的推理模式是否与判定的构建类型匹配？
   - 例如：构念辨析型骨架中出现了因果链语言 → 不纳入（模式错配）

**裁决格式**：

```yaml
phase_2_4_skeleton_check:
  skeleton_id: "T3_mechanism_chain_mediation"
  verdict: "通过 / 需修正 / 不纳入"
  verdict_reason: "..."
  generativity_test:
    mock_paragraph_generated: true/false
    persuasive_action_preserved: true/false
    notes: "..."
  mechanism_content_test:
    content_contamination: ["performative tension", "absorptive capacity"]
    contamination_cleared: true/false
  type_fidelity_test:
    build_type_match: true/false
    mismatch_details: "..."
```

**裁决标准**：

| 裁决 | 条件 | 后续动作 |
|------|------|----------|
| **通过** | 三项测试全部通过 | 骨架进入 Phase 3 和 Phase 4 |
| **需修正** | 生成力或机制内容测试未通过，但可通过改写修复 | 标记后在 Phase 4 中尝试改写后重新验证 |
| **不纳入** | 构建类型错配，或过度抽象失去生成力 | 丢弃，不进入语料库 |

**注意**：裁决记录存入 Vault 的 `vault_enrichment`，供 Phase 4 跨论文聚合使用。

### 2.5 连接词使用模式提炼（Connector Pattern Distillation）

连接词是 Theory 论证逻辑的**显式标记**——它们将隐含的因果、对比、递进关系暴露给读者。蒸馏连接词使用模式可以直接反哺 `write-theory` 的 Phase 5 连接词分类库（§5.6 连接词类型学, §5.7 段落收束过渡）。

#### 蒸馏目标

对论文 Theory 中使用的连接词进行**三层提取**：

1. **连接词密度与分布**：哪些逻辑关系的连接词被使用？频率如何？
2. **模块-连接词映射**：不同模块（T1–T6）偏好哪些连接词类型？
3. **构建类型-连接词映射**：不同构建类型偏好的连接词模式（可跨论文聚合）

#### 连接词分类法（与 write-theory §5.6 对齐）

| 逻辑关系 | 英文连接词 | 中文对应 | 典型出现模块 | 蒸馏计数标记 |
|---------|-----------|---------|-------------|-------------|
| **因果** | Therefore, Thus, Accordingly, Consequently, As a result, Hence, This leads to | 因此、由此、从而 | T3（机制推演）, T4（假设收敛） | `causal_N` |
| **对比** | In contrast, By comparison, Unlike, However, Whereas, On the other hand, Conversely | 相比之下、与之不同、然而 | T1（构念区分）, T5（边界条件） | `contrast_N` |
| **递进** | Furthermore, Moreover, In addition, Additionally, Beyond this, More importantly | 更进一步、此外、更重要的是 | T3（多步机制链的步骤间衔接） | `additive_N` |
| **条件** | When, If...then..., Only if, Provided that, Contingent on, Depending on | 当…时、若…则…、仅在 | T5（边界条件）, 假设树型 T3 | `conditional_N` |
| **让步** | Although, While, Despite, Even though, Nevertheless, Nonetheless | 尽管、虽然、即便如此 | T5（边界承认后转回主论证） | `concessive_N` |
| **例证** | Specifically, In particular, For example, For instance, To illustrate | 具体而言、例如 | T3（机制具体化）, T1（构念维度展开） | `specificity_N` |
| **总结** | Taken together, In sum, Overall, Collectively, In summary | 综上、整体而言 | T6（收束）, 假设段落的最后一句 | `summary_N` |
| **强调** | Notably, Importantly, Critically, It is worth noting that, Key to this argument | 值得注意的是、关键在于 | T2（理论核心洞察）, T4（假设关键方向） | `emphasis_N` |

#### 段落内连接词节奏（Beat Connector Pattern）

连接词在论证节奏的**拍间过渡**中承担特定功能。蒸馏时记录每拍的拍间连接词类型：

```text
四拍论证链的拍间连接词模式：
[拍1-方向] → [拍2-机制]:
  典型连接词: "Specifically, ..." / "The logic is as follows: ..." / "We argue that..."
  蒸馏标记: beat1→2_connector = "specificity" / "none (direct)"

[拍2-机制] → [拍3-证据]:
  典型连接词: "Consistent with this logic, ..." / "Research supports this mechanism: ..." / "For example, ..."
  蒸馏标记: beat2→3_connector = "specificity" / "additive"

[拍3-证据] → [拍4-收敛]:
  典型连接词: "Therefore, ..." / "Thus, ..." / "Accordingly, ..." / "Taken together, these arguments suggest..."
  蒸馏标记: beat3→4_connector = "causal" / "summary"
```

**拍间连接词缺失为高风险**：如果 beat3→4 没有因果连接词（直接 "H1: X is positively related to Y"），标记为 "无收敛信号"——假设像是从天而降，而非从机制推导。

#### 模块间过渡连接词模式

记录 T1→T2→T3→T4→T5→T6 模块序列中每个过渡点的连接词：

| 过渡点 | 典型连接词 | 功能 | 缺失风险 |
|--------|-----------|------|---------|
| T1→T2 | "Drawing on [theory], we..." / "To explain [these relationships], we adopt..." | 从构念界定过渡到理论框架 | T2 像硬插入的新话题 |
| T2→T3 | "Building on this lens, we develop..." / "[Theory] suggests that..." | 从理论框架过渡到机制推演 | T2 说完就扔，未驱动 T3 |
| T3→T4 (每假设) | "Therefore, we hypothesize:" / "Accordingly:" / "Thus:" | 从机制链收敛到假设 | 假设无推导信号 |
| T4(H_n)→T4(H_{n+1}) | "Having established H1, we next consider..." / "Beyond this direct effect, we further argue..." / "However, this relationship may not hold uniformly..." | 假设间逻辑递进 | 假设间无递进逻辑 |
| T4→T5 | "However, the [baseline effect] is likely contingent on..." / "Thus far we have assumed [condition]; yet..." | 从主效应过渡到边界条件 | T5 像是事后补丁 |
| T5→T6 | "Taken together, our theoretical framework suggests..." / "In sum, we have argued that..." | 从分散假设收束为整体框架 | 全文理论碎片化 |

#### 构建类型连接词特征

不同构建类型有其**标志性连接词组合**，蒸馏时识别该论文是否使用了其构建类型的预期连接词汇：

| 构建类型 | 标志性连接词组合 | 预期高频词 | 类型错配信号 |
|----------|----------------|-----------|-------------|
| **构念辨析型** | 对比+递进 | Whereas, In contrast, Unlike, Further | 大量使用 Therefore / Thus（滑向机制推演） |
| **机制推演型** | 因果+递进+具体化 | Therefore, Specifically, Consequently, In turn | 大量使用 Whereas / Unlike（混淆了构念辨析和机制推演） |
| **假设树型** | 条件+因果+让步 | When, However, Contingent on, Not uniform | 没有条件类连接词（缺少 moderator 信号），或因果连接词占绝对主导 |
| **质性过程理论型** | 时间序列+条件 | In Phase 1, As, Subsequently, When [condition] shifts | 使用因果链连接词（Therefore, Consequently）代替过程阶段标记 |
| **调节效应型** | 条件+因果+对比 | When [W] is high, In contrast, Therefore | 条件连接词只出现在假设句（H_x）而非机制段（T3） |

**连接词-构建类型一致性评分**：

```yaml
phase_2_5_connector_distillation:
  connector_density:
    causal: 12
    contrast: 3
    additive: 5
    conditional: 7
    concessive: 2
    specificity: 4
    summary: 2
    emphasis: 3
    total_connectors: 38
    connectors_per_100_words: 3.2
  beat_connector_patterns:
    H1_paragraph:
      beat1→2: "specificity (Specifically...)"
      beat2→3: "specificity (Consistent with...)"
      beat3→4: "causal (Therefore...)"
      beat_transitions_complete: true
    H2_paragraph:
      beat1→2: "none (direct)"
      beat2→3: "additive (Furthermore...)"
      beat3→4: "causal (Thus...)"
      beat_transitions_complete: false
      missing_beat_connector: "beat1→2 缺少方向→机制的过渡信号"
  module_transition_connectors:
    T1→T2: "To explain these relationships, we adopt..." (present)
    T2→T3: "missing — T3 直接从 'We argue' 开始，无理论框架过渡"
    T3→T4(H1): "Therefore, we hypothesize:" (present)
    T4(H1)→T4(H2): "Beyond this direct effect..." (present)
    T4→T5: "However, the above logic assumes..." (present)
    T5→T6: "Taken together..." (present)
    transition_completeness: "5/6"
    missing_transitions: ["T2→T3"]
  build_type_connector_alignment:
    detected_type: "机制推演型"
    expected_high_freq: ["Therefore", "Specifically", "Consequently"]
    actual_high_freq: ["Therefore(8)", "Specifically(4)", "However(5)"]
    alignment_issues:
      - "However 频率过高 (5次) 对机制推演型属于异常——可能暗示隐性假设树结构"
    connector_type_fidelity: "△ — 有条件连接词泄露"
  novel_connector_patterns:
    - "使用 'Stated differently' 作为机制重述信号 (非标准连接词，但功能等效于 specificity)"
    - "T3 步骤间使用 'This, in turn,...' 标记链式递进 (比 'Furthermore' 更精确)"
```

#### Phase 3 新增连接词 DNA 指标

| 指标 | 计算方式 | 用途 |
|------|----------|------|
| 连接词密度 | 连接词总数 / Theory 总词数 × 100 | 判断论证显式化程度。顶刊中位数约 3-4 词/100词 |
| 因果连接词占比 | 因果类连接词数 / 总连接词数 | 机制推演型预期 ≥30%；过高可能为"因果词堆砌" |
| 条件连接词占比 | 条件类连接词数 / 总连接词数 | 假设树型/调节效应型预期 ≥15%；机制推演型预期 <10% |
| 拍间过渡完整性 | 有显式连接词的拍间过渡数 / 总拍间过渡数 | 评估段落内部论证显式化程度 |
| 模块过渡完整性 | 有显式连接词的模块过渡数 / 5（T1→T2→T3→T4→T5→T6 共5个过渡点，T4内部不计） | 评估模块间叙事流显式化程度 |
| 连接词-构建类型一致性 | 标志性连接词组合匹配度 | 高/中/低。低匹配 = 连接词使用与构建类型不匹配 |

---

## Phase 3 — Academic Theory DNA 量化与结构化报告

量化该论文 Theory 的"理论 DNA"，生成 fine-grained profile。

### 惰性生成原则（Lazy Generation）

借鉴 grill-with-docs 的 "Create files lazily" 原则：

- **模块不存在时不生成空壳**：如果某模块（如 T5 Boundary Condition）在原文中确实缺失，Fine-Grained Profile 中直接省略该模块的标题和占位符
- **骨架不可迁移时标记即停**：如果某表达骨架因论文特殊性无法泛化，只记录 "Non-Transferable" 标签，不强行抽象
- **批量模式分桶后再聚合**：Phase 4 的聚合报告只在同一构建类型内统计，不同构建类型的数据不混为一谈
- **Why-chain 断裂点不美化**：如果 T3 存在推理跳跃，记录具体断裂位置，不为了"完整"而补全作者未论证的步骤

### Theory DNA 指标

| 指标 | 计算方式 | 用途 |
|------|----------|------|
| 模块密度 | 总字数 / 识别到的模块数 | 判断 Theory 的信息密度（顶刊中位数约 100-130 词/模块） |
| Why chain 步数 | T3 中独立机制步骤的数量 | 判断机制深度。单步为薄弱，两步为常规，三步+为深入 |
| Why chain 断裂点 | T3 中缺少理论依据的跳跃数量 | 断裂点 >=1 即标记为推理薄弱 |
| 主角集中度 | 主角（核心构念）提及次数 / 总构念提及次数 | 判断焦点是否分散。>=60% 为集中，<40% 为分散 |
| Citation 功能比 | 支持机制推演的 citation / 总 citation 数 | 判断 "citation list 代替理论" 风险。>=70% 为健康 |
| 假设推导句密度 | "Therefore" / "Thus" / "Accordingly" / "Consequently" 出现次数 / 假设数 | 判断假设是否从机制自然推导。>=1  per hypothesis 为健康 |
| Scope condition 覆盖 | 有明确 scope condition 的构念 / 总构念数 | 判断构念界定精确性 |
| Boundary 嵌入深度 | Boundary condition 是在假设之后补丁，还是嵌入机制链中 | 嵌入机制链 > 假设后补丁 |
| Theory-to-Hypothesis 对齐 | T3 的机制关键词与 T4 假设关键词的重叠度 | 高/中/低。低对齐 = "机制与假设脱节" |
| Two-literature 清晰度 | T2 的理论文献是否与 Introduction 的 Gap 文献明显分离 | 高/中/低 |
| **T3/T4 论证节奏完整性** | 假设推导段落的四拍完整比例（方向→机制→证据→收敛） | >=3.5/4 为优秀，2.5-3.4/4 为合格，<2.5/4 为薄弱 |
| **T1 定义节奏完整性** | 构念定义段落的三拍完整比例（命名→维度→范围） | >=2.5/3 为优秀，1.5-2.4/3 为合格 |
| **T2 理论视角节奏完整性** | 理论引入段落的三拍完整比例（来源→适用性→框架映射） | >=2.5/3 为优秀 |
| **节奏变异度** | 段落节奏与标准节奏的偏离类型和幅度 | FULL_RHYTHM / RHYTHM_GAP / RHYTHM_BROKEN / RHYTHM_VARIANT |
| **跨段落节奏连贯性** | 相邻假设段落的节奏衔接模式（连续推导 / 并行并列 / 分叉展开） | 连续推导 > 分叉展开 > 并行并列（但构建类型决定最优模式） |
| **连接词密度** | 连接词总数 / Theory 总词数 × 100 | 顶刊中位数约 3-4 词/100词；<2 为"论证隐式化"，>5 为"连接词过载" |
| **因果连接词占比** | 因果类连接词数 / 总连接词数 | 机制推演型预期 ≥30%；过高（>50%）可能为因果词堆砌 |
| **条件连接词占比** | 条件类连接词数 / 总连接词数 | 假设树型/调节效应型预期 ≥15%；机制推演型预期 <10%；过高泄露隐性假设树结构 |
| **拍间过渡完整性** | 有显式连接词的拍间过渡数 / 总拍间过渡数（每假设段落 3 个拍间过渡点） | ≥80% 为优秀，<50% 为"论证断裂" |
| **模块过渡完整性** | 有显式连接词的模块过渡数 / 5 | 5/5 为优秀，<3/5 为"模块碎片化" |
| **连接词-构建类型一致性** | 标志性连接词组合匹配度 | 高/中/低。低匹配 = 连接词使用模式与构建类型预期偏离 |

### Narrative Style Profile（叙事风格 DNA）

借鉴 model_papers_style.json 的多维度风格解剖框架，为每篇论文生成**可模仿的理论写作风格画像**。

| 维度 | 提炼问题 | 输出格式 |
|------|----------|----------|
| **Tone** | 整体语气光谱是什么？assertive / cautious / formal / mechanism-forward / concept-forward？ | 主语气 + 次语气，附证据句 |
| **Paragraph Rhythm** | 段落内部句法节奏是什么？claim→mechanism→evidence→hypothesis？还是 definition→distinction→consequence？ | 段落级节奏模板 |
| **Module Ratio** | 各模块的词数比例？（如 T1 占 20%、T3 占 40%、T4 占 15%） | 百分比 + 与同类范文的对比 |
| **Distinctive Features** | 该论文**特有**的理论叙事标记是什么？（如 paired concept contrasts / stepwise mechanism labels / explicit caveat embedding / rhetorical question architecture） | 列表，每项附原文例句 |
| **Avoids** | 该论文**刻意回避**的写法是什么？（如 avoids black-box econometrics / avoids overclaiming causality / avoids bullet-point prose） | 列表，说明回避的修辞功能 |
| **Quality Markers** | 为什么这个理论论证结构有效？最强/最弱的叙事技巧是什么？ | what_makes_effective / strongest_aspect / weakest_aspect |

**记录原则**：只记录该论文**明显区别于**同类构建类型其他范文的特征。通用特征（如"有 why chain"）不记入 Distinctive Features。

### 结构化报告输出（fine_grained profile）

```markdown
# Fine-Grained Profile: [作者_年份_期刊]

## Paper Identity
- 构建类型: [来自 Phase 0]
- 期刊/领域: [journal]
- Theory 字数: [N]
- 段落数: [N]
- 假设数: [N]
- 与 write-theory 模板对齐度: [高/中/低]

## Module Coverage (T1–T6)
[Phase 1.5 输出]

## Distilled Skeletons
### T1 — Construct Definition ([策略])
[来自 Phase 2.2 的骨架列表]

### T2 — Theoretical Lens ([理论])
...

## Theory DNA
[来自 Phase 3 的量化指标]

## Theory Logic Map
[来自 Phase 2.3]

## Dorobantu 问题链覆盖度
| 问题 | 对应模块 | 覆盖度 |
|------|----------|--------|
| WHAT are the key constructs? | T1, T2 | ✓/△/✗ |
| HOW do constructs relate? | T3, T4 | ✓/△/✗ |
| WHY expect these relationships? | T3 | ✓/△/✗ |
| WHAT theoretical lens? | T2 | ✓/△/✗ |
| Are findings consistent? (理论内部) | T3, T5 | ✓/△/✗ |
| What is missing? (理论边界) | T5, T6 | ✓/△/✗ |

## Novel Patterns（与现有 28 篇语料库对比后的新发现）
- 新骨架: ...
- 新 why-chain 模式: ...
- 新构念关系组织方式: ...

## Narrative Style Profile
[来自 Phase 3 的多维度风格解剖]

**Tone**: [主语气]（证据："..."）
**Paragraph Rhythm**: [段落内部节奏模板]
**Module Ratio**: T1 [N%] / T2 [N%] / T3 [N%] / T4 [N%] / T5 [N%] / T6 [N%]
**Distinctive Features**:
- [特征1]: [原文例句]
- [特征2]: [原文例句]
**Avoids**:
- [回避写法1]: [功能解释]
- [回避写法2]: [功能解释]
**Quality Markers**:
- what_makes_effective: [为什么这个理论论证结构有效]
- strongest_aspect: [最值得模仿的1-2个技巧]
- weakest_aspect: [已知风险/审稿人可能攻击的理论薄弱点]

## Non-Transferable Facts
[仅适用于该论文的特定构念、理论视角、机制内容，不可迁移]

## Corpus Reference Notes
[供人工审阅的语料库沉淀注释，不自动修改 write-theory skill]
```

---

## Phase 4 — 跨论文模式验证与语料库沉淀建议

如果是 `--batch` 模式，在多篇论文提炼完成后执行此阶段。

### 三重验证标准（nuwa-skill 迁移版）

| 标准 | 问题 | 淘汰门槛 |
|------|------|----------|
| **跨论文复现** | 这个模块写法是否在多个顶刊范文中出现？ | 只出现 1 次的骨架降级为 "optional variant" |
| **生成力** | 它能不能指导一篇新论文组装出对应功能模块？ | 无法填入占位符生成模块的骨架丢弃 |
| **范式排他性** | 它是不是某类构建类型特别需要？ | 所有构建类型都通用的"废话骨架"（如"Theory is important"）丢弃 |

### 构建类型模式聚合分析

```yaml
phase_4_batch_analysis:
  build_type_distribution: {"机制推演型": 8, "构念辨析型": 4, "假设树型": 3, "质性过程理论型": 2}
  module_sequence_patterns:
    standard_sequence: "T1→T2→T3→T4→T5→T6 (10/17)"
    theory_first: "T2→T1→T3→T4→T5→T6 (4/17, 均为构念辨析型)"
    boundary_embedded: "T5 嵌入 T3 (3/17)"
  why_chain_patterns:
    dominant_by_type:
      机制推演型: "两步因果链 (6/8)"
      构念辨析型: "差异化维度×后果 (4/4)"
      假设树型: "主效应→条件化分支 (3/3)"
  hypothesis_derivation:
    therefore_per_hypothesis_avg: 1.2
    derivation_jumps: 3
  protagonist_concentration:
    high: 12
    medium: 3
    low: 2
  novel_findings:
    - "假设树型论文 3/3 在 T3 中使用 'not uniform; rather' 引入 moderator"
    - "构念辨析型 4/4 使用 'Whereas A..., B...' 对比句式"
  rejected_patterns:
    - "'Based on prior research, we hypothesize...' 无 why chain (3 篇)"
    - "T3 只有 citation list 无机制推演 (2 篇)"
```

### 语料库沉淀建议格式

```yaml
phase_4_corpus_reference:
  vault_enrichment:
    new_skeletons_for_reference:
      - module: "T3"
        build_type: "假设树型"
        skeleton: "..."
        source_papers: ["作者_年份", "作者_年份"]
        vault_path: "fine_grained/batch_N/theory_skeletons/"
        note: "供写作者参考，不自动写入 skill"
    patterns_to_note:
      - module: "T1"
        build_type: "构念辨析型"
        observation: "4/4 篇使用 'Whereas...' 对比句式定义两个构念"
        note: "可作为 Vault 注释，验证构念辨析型 T1 表达模式"
    new_anti_patterns:
      - pattern: "T4 使用 'Based on prior research, we hypothesize' 无 therefore"
        evidence: "出现在 3 篇论文中，均被 reviewer 质疑 why chain"
    new_honesty_boundary:
      - boundary: "本 skill 不得为机制推演型推荐单步 why chain"
        source: "语料库中机制推演型使用单步的 0/8 篇"
  batch_metadata:
    total_papers_processed: 10
    build_type_distribution: {"机制推演型": 5, "构念辨析型": 3, "假设树型": 2}
    novel_skeletons_found: 4
    rejected_skeletons: 3
    rejected_reasons: ["仅出现1次", "不可生成模块", "通用废话"]
```

**关键原则**：Phase 4 的所有产出存入 Vault 的 `skill_update_recommendations/` 或 `fine_grained/` 目录。当满足回写条件时（见 Phase 4.5），提醒用户手动更新 `write-theory` 的模块库。

---

## Phase 4.5 — 回写提醒

当 Phase 2–4 的蒸馏产出满足以下全部条件时，在报告末尾生成回写提醒，建议用户将新发现的模式手动沉淀到 `write-theory` 的模块库：

### 触发条件

1. **骨架通过生成力验证**（Phase 2.4 裁决为"通过"）
2. **跨论文复现 ≥ 2 篇**（或批量模式下同一构建类型内 ≥ 2 篇）
3. **构建类型明确**（非 "ambiguous between X and Y"）
4. **模块功能归属明确**（T1–T6 之一，非 "unclassified"）

**不触发回写提醒的情况**：
- 仅 1 篇论文中出现的模式 → 留存为 Vault 参考注释，积累到 ≥3 篇后再提醒
- 构建类型模糊的论文 → 标记为 "pending_type_clarification"
- 骨架批评家裁决为"需修正/不纳入" → 不回写

### 回写操作（手动）

满足条件后，用户在蒸馏报告的「回写建议」区块中执行：

1. 对照报告中的新骨架和 Vault 中已有的模块库条目，判断是否重复
2. 确认模块命名、构建类型标注、范式排他性
3. 手动将新条目写入 `write-theory` 对应模块库文件
4. 更新 `write-theory` 的模块索引

**不自动执行写入**。当前语料库规模不足以支撑有意义的自动化聚类（`write-theory/academic-writing-corpus/` 尚在建设中），手动判断比脚本更可靠。

### 构建类型分桶

新发现的骨架必须在同一构建类型内比较和累积：

| 构建类型 | 分桶 | 聚类依据 | 示例 |
|----------|--------|---------|------|
| 构念辨析型 | `bucket_construct` | "Whereas A..., B..." 对比句式 | T1 构念区分骨架 |
| 机制推演型 | `bucket_mechanism` | "X creates M—a [state]—that [action]" 因果链 | T3 两步中介骨架 |
| 假设树型 | `bucket_tree` | "not uniform; rather, contingent on" 条件化 | T5 调节引入骨架 |
| 质性过程理论型 | `bucket_process` | "Phase 1... Phase 2..." 时间阶段 | T3 过程阶段骨架 |
| 调节效应型 | `bucket_moderation` | "when W is high/low" 条件预测 | T4 交互假设骨架 |

**跨桶规则**：
- 同一骨架被多个构建类型的论文使用（如 T6 Closure 的 "Taken together" 骨架），标记为 `跨类型`，可跨桶回写
- 范式排他性骨架（如构念辨析型的 "differentiation dimensions"）**绝不**跨桶回写

### 诚实边界（回写专用）

- **不将单篇模式写入推荐列表**：仅 1 篇论文中出现的模式留在 Vault 参考注释中，标注为"待审阅"，不进入 `write-theory` 的推荐映射
- **不覆盖已有模块**：遇到同名或同功能模块时，生成 `_alt` 变体条目，由用户决定合并或保留
- **不虚构跨论文复现**：来源论文数基于 Vault 中实际 narrative 文件数，如有偏（如某领域论文过多）应如实注明
- **必须人工确认构建类型标注**：Phase 0 分类推断可能错误，用户必须逐条检查
- **不回流机制内容**：骨架中嵌入特定论文机制名称的，必须清理后再写入
- **跨桶回写必须标记**：`跨类型` 骨架在模块索引中标注 `[跨类型]`，提醒该骨架的普适性尚未在所有构建类型中验证

---

## Phase 5 — 质量验证与 QC 输出

生成最终的蒸馏质量报告。

### QC Checklist

- [ ] **Completeness**: 所有强制模块（根据构建类型）已被覆盖
- [ ] **Clarity**: 每个骨架都有明确的 [占位符] 和适用构建类型标注
- [ ] **Credibility**: 未将单篇论文的特殊机制泛化为通用规则
- [ ] **Replicability**: 骨架填入具体信息后，能生成类似顶刊风格的模块
- [ ] **No Verbatim Copy**: 输出中未出现可直接追溯到原文的连续 8+ 词短语
- [ ] **Fact Boundary**: 所有不可迁移事实（特定构念定义、理论视角内容）已被明确标记
- [ ] **Build-Type Fidelity**: 骨架的推理模式与构建类型匹配（构念辨析型 ≠ 因果链骨架）
- [ ] **Dorobantu Coverage**: 核心问题链（WHAT/HOW/WHY/Theory Lens）都有对应模块
- [ ] **Why-Chain Audit**: T3 骨架中包含明确的机制步骤，无"常识跳跃"
- [ ] **Hypothesis Form Audit**: T4 骨架中假设方向、条件、IV/DV 明确

### 最终输出物清单

1. **Fine-Grained Profile**（单篇）或 **Batch Aggregation Report**（批量）
2. **Expression Skeleton Corpus**（新增骨架列表，含构建类型变体）
3. **Theory Logic Map**（Why-chain / Construct-clarity / Theory-citation 处理模式）
4. **Theory DNA Metrics**（可对比的量化指标）
5. **Dorobantu 问题链覆盖度表**
6. **Corpus Reference Notes**（供人工审阅的语料库沉淀注释，不自动修改 skill）
7. **QC Result**（通过/需修正/拒绝入库）
8. **模仿风险提示**（原文叙事薄弱点清单，防止用户在模仿时踩坑）

### 模仿风险提示

蒸馏过程发现的原文理论叙事薄弱点不是要被"修复"（论文已发表），而是作为**模仿风险提示**记录，防止用户在模仿时踩坑。

**格式**：

```markdown
# 模仿风险提示: [作者_年份_期刊]

| 发现阶段 | 风险类型 | 原文表现 | 模仿后果 | 建议处理 |
|----------|----------|----------|----------|----------|
| Phase 1.5 (Why-chain 压力测试) | Why-chain 跳跃 | 从 X→Y 缺少中间机制论证 | 模仿后审稿人质疑机制 | 补充自己的中间机制论证，不要模仿跳跃 |
| Phase 2 (T1 提炼) | 构念定义模糊 | "organizational capability" 未界定类型 | 模仿后审稿人问 "what kind of capability?" | 增加 scope condition 或具体化构念 |
| Phase 2.4 (骨架批评) | 机制内容污染 | 骨架中包含 "performative tension" 等具体机制 | 模仿后变成复制特定论文的机制 | 泛化为 [theoretical mechanism]，只模仿组织方式 |
| Phase 1.5 (对齐检查) | T4→Methods 断裂 | T4 提出三向交互但 Methods 未报告交互项 | 模仿后假设与操作化脱节 | 确保 Methods 中的变量操作化与 Theory 假设严格对齐 |
```

**记录原则**：
- **不修复**：论文已发表，薄弱点是客观存在的
- **不美化**：不能为了让骨架"好看"而掩盖原文问题
- **可行动**：每条风险必须附带"建议处理"，告诉用户如果模仿此处该怎么做
- **跨论文可比较**：批量模式下，同类型风险的频率可作为"该构建类型的常见陷阱"沉淀

---

## 成品验证（写作 QC）

Theory & Hypotheses 写作质量检查请使用 `/theory-review`——它覆盖构念清晰度、why-chain 完整性、假设形式和角色排序，基于 Pollock Ch06 和 MVP30 范文语料库。

---

## 诚实边界

本 skill 必须 not：
- **复制原文**：不提取连续 8+ 词的原文短语进入骨架。骨架必须是句法抽象。
- **虚构复现性**：不声称某骨架"出现在多篇论文中"除非确实有证据。
- **泛化特殊构建类型**：不把构念辨析型的对比句式套用到机制推演型，不把过程理论的时间阶段套用到假设树型。
- **跳过 why chain 薄弱点**：即使原文 T3 只有 citation list 无机制推演，也要如实记录，不能美化。
- **强制覆盖所有模块**：如果某 Theory 确实缺失某模块，记录为 missing，不捏造。
- **混淆构建类型**：如果原文的理论构建方式模糊，明确标记为 "ambiguous between 机制推演型 and 假设树型"，不强行分类。
- **泛化机制内容**：不将"某篇论文中 X→M→Y 的具体机制"提炼为"机制推演型通常使用三步链"。只提炼**组织方式**，不提炼**机制内容**。
- **强制标准节奏**：不将四拍论证链强加于所有论文。RHYTHM_VARIANT 是合法的节奏形态，需要关注的是功能等价的论证完成度，而非拍数的机械合规。
- **虚构连接词-类型绑定**：不声称"机制推演型必须使用 Therefore"。连接词模式是统计倾向而非语法规则。标记连接词-类型一致性为"低"时，必须附具体证据（如"条件连接词占比 25%，远超机制推演型中位数 8%"），而非仅凭印象判断。
- **交叉矩阵硬化**：构建类型×假设结构矩阵中的 M/C/O 标注是基于当前语料库的归纳，不是理论上的不可能性证明。遇到矩阵外的组合时，标记为 "unclassified combination" 并记录，不强行排除。
- **证据链不捏造**：如标志性语言确实模糊（同一段落同时包含两种类型的标志性语言），如实记录模糊信号，不在证据链中虚构 "clearly indicates"。

---

## 反模式（蒸馏过程中主动排查）

| 反模式 | 表现 | 处理方式 |
|--------|------|----------|
| **原文依赖型骨架** | 骨架中包含论文特有的构念名、理论家名、具体理论术语 | 泛化为 [construct] / [theory] / [theoretical mechanism] |
| **过度抽象** | 骨架抽象到只剩 "We argue that X affects Y"，失去推理结构的启示 | 保留关键推理标记（"creates [state]—a [definition]—that [action]" / "Whereas [A]..., [B]..."） |
| **构建类型错配** | 将构念辨析型的 "differentiate" 骨架标记为机制推演型 | 在骨架中标注准确的构建类型适用范围 |
| **机制内容泛化** | 将原文的具体机制步骤提炼为"通常使用两步链" | 只记录"两步链的组织方式"，不记录具体机制内容 |
| **忽略 why chain 断裂** | 只提取"写得好的"部分，忽略原文 T3 的跳跃 | 在 Theory Logic 和 QC 中明确记录断裂点 |
| **批量同质化** | 批量处理时忽视构建类型差异，用同一套骨架覆盖不同类型 | Phase 0 分类必须先行，不同构建类型分桶处理 |
| **混淆 theory story 与 summary** | 将 "Smith (2010) argues..." 式 citation 记录为机制骨架 | Theory story 必须以 construct/mechanism 开头，非作者名 |

---

## 与下游 Skill 的接口

- **`write-theory`** — Phase 4 的更新建议可直接沉淀到 write-theory 的模块库和骨架库；Phase 2.5 连接词统计可反向更新 write-theory 的连接词分类库和段落收束模板
- **`theory-review`** — Phase 1.5 的模块覆盖检查和 Theory Logic Map 可作为 theory-review 的审查基准
- **`paper-review`** — Theory Logic Map 可用于跨 section 对齐检查（Theory 承诺 vs Results 兑现）
- **`write-introduction`** — T2 Theoretical Lens 和 T6 Closure 的提炼可用于优化 Introduction 的 P5 Preview 和 P7 Contribution
- **Vault** — Fine-Grained Profile 存入 Vault 的 `fine_grained/batch_*/[paper]_distilled_theory.md`

## 外部资产位置

- **现有语料库索引**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/theory/mvp30/_mvp30_theory_index.md`
- **蒸馏产出存放**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/theory/mvp30/fine_grained/batch_*/[paper]_distilled_theory.md`
- **更新建议存放**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/theory/mvp30/skill_update_recommendations/`
## 输出结构参考

各 Phase 输出的结构化字段见各 Phase 正文中的 YAML/Markdown 表格。完整字段名和取值枚举已在 Phase 0–5 的示例输出块中逐一定义，无需单独维护 JSON Schema。

如需机器消费格式，参考 Vault 中已蒸馏的 `fine_grained/` 目录下的实际报告文件——其结构和字段集比抽象 schema 更准确地反映真实输出。

---
*基于 nuwa-skill 流水线框架、Pollock 2025 Ch06、Dorobantu et al. (2024)、Shepherd & Wiklund (2020) 叙事规则、MVP30 范文语料库构建。版本 1.0.0 — Theory 蒸馏 Meta-Skill。*
