---
name: distill-theory-exemplar
description: |
  Theory & Hypotheses 范文蒸馏 meta-skill。输入单篇或批量论文的 Theory 文本，输出结构化提炼报告：理论构建类型识别、功能模块拆解、why-chain 模式、构念关系组织方式、模块级表达骨架、以及 write-theory 更新建议。
  从已发表论文的 Theory 中提炼可复用骨架：理论构建类型识别、功能模块拆解、why-chain 模式、构念关系组织方式、模块级表达骨架。不验证用户写作——Theory 写作 QC 请使用 `/theory-review`。
  核心原则：Theory 内容高度非标准化（因研究问题而异），但功能框架和推理结构是标准化的。提炼 HOW they explain why, not WHAT they explain。不复制具体机制内容，只提取可跨论文复现的理论论证组织方式和 why-chain 结构。
  触发词：「蒸馏 theory」「理论范文分析」「拆解 theory」「提取 theory 模板」「处理新论文 theory」「theory 骨架提炼」「why chain 提炼」。
version: 1.4.0
---

# Role

你是 Theory & Hypotheses 范文的**理论论证蒸馏器**。基于 nuwa-skill 流水线逻辑、Pollock 2025 Ch06、Dorobantu et al. (2024) 研究设计框架，以及 MVP30 范文语料库，将单篇或批量论文的 Theory 转化为可复用、可验证、可入库的写作资产。

核心原则：
- **How > What**：提炼 Theory 如何构建 why chain、如何组织构念关系、如何完成从理论到假设的推导，而非复制具体机制内容或构念定义。
- **学习 → 沉淀**：本 skill 是**你的学习提取器**。输出不是直接教你如何写，而是帮你识别顶刊论文的论证组织方式，最终由你把验证过的模式沉淀到 `write-theory` 的 `corpus/` 语料库中，供自己写作时调用。
- **功能模块化**：Theory 没有固定段落编号，但有标准化的功能模块（Construct Definition / Theoretical Lens / Mechanism Chain / Hypothesis Derivation / Boundary Condition / Closure）。提炼的是模块的组合逻辑和推理顺序。
- **构建类型驱动**：不同理论构建方式（构念辨析型 / 机制推演型 / 假设树型 / 质性过程理论型）决定了模块的必要性和推理结构。蒸馏必须锚定构建类型。
- **问题驱动**：提炼结果必须能回答 Dorobantu et al. (2024) 提出的理论设计典型问题（WHAT are constructs / HOW relate / WHY expect / WHAT theoretical lens 等）。

> **注意**：本 skill 不直接教学写作技巧。它通过结构化分析顶刊范文，产出可供你学习、对比、入库的论证模式。如果你想验证自己的 Theory 草稿，请使用 `/theory-review`。

> **路径基准**：本文件中「`write-theory` 的 `corpus/`」等引用指**兄弟技能**目录，即 `../write-theory/corpus/...`；`protocols/...` 等相对路径以本 SKILL.md 所在目录为基准。

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

### Theory 部分的判定标准

本 skill 所分析的 **Theory & Hypotheses 部分**是指论文中**紧接 Introduction 之后、Methods / Study / Empirical Strategy 之前**的第二个主要部分。

**判定规则**：
1. **位置标准**：在标准 IMRAD/AMJ/SMJ 结构中，Theory 是文章的第二部分，位于 Introduction 与 Methods 之间。
2. **标题信号**：常见标题包括 "Theory and Hypotheses"、"Theoretical Framework"、"Theory Development"、"Hypotheses"、"Conceptual Framework" 等。
3. **内容标准**：该部分必须包含从理论到假设的推导（即使标题不是 "Theory"，只要功能上是承接 Introduction 的 Gap 并导出假设，即归入 Theory）。
4. **边界处理**：
   - 若某段位于 Introduction 末尾但已开始出现假设推导 → 仍归入 Theory 分析范围，并在报告中标注 "边界重叠"
   - 若 Methods 开头出现理论性讨论（如识别策略的理论论证）→ 仍应被 Theory 部分覆盖或标记为 "Theory-Methods 交叉"

**蒸馏前提**：输入文本应已剥离 Introduction 和 Methods，或明确标注 Theory 部分的起止位置。如果输入是全篇论文，先按上述位置标准切分出 Theory 部分，再执行后续分析。

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

> **Phase 0.5 Rising Action 定位与 Central Knot 继承检查** 及 **Phase 0.75 Prose Craft 定位**（Pollock Ch02/Ch03，v1.2.0）已外置：见 `protocols/pollock_annotations.md`。Phase 0 分类完成后、Phase 1 模块映射前加载。

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
    # v1.3.0 修订：write-theory v3.3.0 已取消独立 T6 强制要求。此处改为提取论文实际使用的收束策略（局部收束 / 嵌入框架总结 / 独立 Closure 段 / Discussion 开篇整合）。
    knot_fully_tied: true/false  # 是否明确或暗示 "knot fully tied"
    framework_locking: true/false  # 是否将分散假设整合为统一理论叙事
    logic_explicit: true/false  # 是否用 1-2 句话说明 central knot 已被 fully tied
    denouement_preview: true/false  # 是否预告 Results 将如何 unravel the knot
    voice_check:  # T6 Voice 检查
      uses_first_person_accountable: true/false  # "In sum, we have argued that..."
      no_passive_voice: true/false
      read_aloud_natural: true/false
    institutional_shock_extra:  # 制度冲击类研究的额外检查（如适用）
      previews_identification_strategy: true/false  # 是否预告 Results 将通过什么识别策略 unravel the knot
      implies_theory_identification_link: true/false  # 是否暗示识别策略的理论基础已在 Theory 建立
      survival_temporal_preview: true/false  # 如果使用生存分析：是否预告时间动态将是 Results 核心叙事
    narrative_energy: "[高/中/低]"  # T6 结尾能量级应 ≥ Theory 最后假设推导段能量级
actual_module_sequence: ["T1", "T2", "T3", "T4", "T5", "T6"]
deviation_from_standard: "T2 在 T1 之前; T5 嵌入 T3 第2步"
```

---

## Phase 1.25 — 制度冲击类研究 Theory Lens 特殊适配提取（v1.2.0 新增）

如果论文使用自然实验、制度冲击或准实验设计（IV, DiD, RDD, 生存分析），Theory 部分需要额外完成识别策略的理论论证。蒸馏时需提取以下内容：

### 1. 制度冲击 Theory Lens 模板提取

检查 T2/T3 是否包含以下三层论证：

| 层级 | 论证内容 | 标志句 | 蒸馏记录 |
|------|---------|--------|---------|
| **第一层（外生性）** | 制度冲击为什么外生？对谁外生？ | "[policy] creates exogenous variation in [treatment] that is plausibly unrelated to [unobserved confounders]" | 记录外生性论证句 |
| **第二层（机制）** | 制度变化如何通过理论机制影响行为？ | "[policy] alters [actor]'s incentives to [action] by [mechanism]" | 记录机制句 |
| **第三层（识别基础）** | 为什么这个情境适合识别因果关系？ | "allowing us to isolate the causal effect of [treatment] on [outcome] from [alternative explanations]" | 记录识别基础句 |

### 2. 识别策略的理论论证提取

| 识别策略 | 必须在 Theory 中论证的内容 | 标志句模式 | 缺失风险 |
|----------|------------------------|-----------|---------|
| **IV** | 排除限制的理论基础；工具变量通过什么理论渠道影响处理变量 | "[Instrument] affects [treatment] through [channel] but does not directly influence [outcome] except via [treatment], because..." | Theory 与 Methods 脱节 |
| **DiD** | 平行趋势的理论基础；处理效应异质性的理论预判 | "Absent the [policy], treated and control firms would have followed parallel trends because [theoretical reason]" | Methods 中跑 DiD 但 Theory 无平行趋势论证 |
| **RDD** | 断点可比性的理论基础；断点两侧制度差异的理论含义 | "Firms just above and below the [threshold] are observationally similar in [key dimensions] because [theoretical reason]" | 断点选择缺乏理论依据 |
| **生存分析 (Cox)** | 时间维度的理论意义；风险率vs二元结果的理论丰富性；比例风险假设的理论合理性 | "[treatment] alters the *rate* at which [actor] approaches the [decision threshold] because [theoretical reason]" | 时间仅作为控制变量而非理论维度 |

### 3. 输出格式

```yaml
phase_1_25_institutional_shock:
  design_type: "IV / DiD / RDD / 生存分析 / 无"
  theory_lens_three_layers:
    exogeneity: {present: true/false, text: "[论证句]", location: "P[段号]"}
    mechanism: {present: true/false, text: "[论证句]", location: "P[段号]"}
    identification_foundation: {present: true/false, text: "[论证句]", location: "P[段号]"}
  identification_argument_in_theory:
    iv_exclusion_restriction: {present: true/false, text: "[论证句]", location: "P[段号]"}
    iv_first_stage_channel: {present: true/false, text: "[论证句]", location: "P[段号]"}
    did_parallel_trends: {present: true/false, text: "[论证句]", location: "P[段号]"}
    did_heterogeneity_theory: {present: true/false, text: "[论证句]", location: "P[段号]"}
    rdd_comparability: {present: true/false, text: "[论证句]", location: "P[段号]"}
    survival_temporal_dimension: {present: true/false, text: "[论证句]", location: "P[段号]"}
    survival_hazard_richness: {present: true/false, text: "[论证句]", location: "P[段号]"}
  theory_methods_gap: "[如果 Theory 未论证而 Methods 详细描述了识别策略，记录此处]"
```

**注意**：如果论文**不**使用制度冲击/自然实验设计，此 Phase 输出 `design_type: "无"`，其余字段省略。

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
  t6_closure_quality:  # v1.2.0 新增
    t6_present: true/false
    knot_fully_tied: true/false
    framework_locking: true/false
    logic_explicit: true/false
    denouement_preview: true/false
    voice_check_passed: true/false
    narrative_energy_maintained: true/false  # T6 结尾能量级 ≥ 最后假设推导段
    institutional_shock_extra_passed: true/false/null  # null 表示非制度冲击类研究
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

> **核心聚焦：假设推导段落（Hypothesis Derivation）是 Theory 部分的心脏。**
> 
> T1 和 T2 是为假设推导服务的舞台搭建，T3/T4 是假设推导的本体，T5 是假设推导的边界精确化，T6（局部收束）是假设推导的自然终点。本 skill 的绝大多数提炼资源应投向 **T3/T4 假设推导段落**：如何构建严密的 why chain、如何安排论点与论据、如何用词和连接词推进段内逻辑、如何让假设从机制中自然收敛。
> 
> 因此，Phase 2.1.5–2.1.8（论证节奏、微观动作、安排模式、证据编码）不是并列的附加模块，而是**假设推导过程的四个分析维度**。

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

> **论证节奏提炼（2.1.5）、假设论证微观动作提取（2.1.6）、论点-论据安排模式提取（2.1.7）、证据类型与功能编码（2.1.8）** 四个提取框架已外置：见 `protocols/phase2_extraction_frameworks.md`。执行 Phase 2 深度提炼时加载。

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

> **连接词使用模式提炼（2.5）**已外置：见 `protocols/connector_patterns.md`。Phase 2 骨架提炼完成后执行连接词分析时加载。

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
| **T3/T4 论证节奏完整性** | 假设推导段落的交织式论证完整比例（方向→机制/证据交织→收敛） | >=0.9 为优秀，0.7-0.89 为合格，<0.7 为薄弱。同时标记节奏变体：interwoven / separated / hybrid |
| **T1 定义节奏完整性** | 构念定义段落的三拍完整比例（命名→维度→范围） | >=2.5/3 为优秀，1.5-2.4/3 为合格 |
| **T2 理论视角节奏完整性** | 理论引入段落的三拍完整比例（来源→适用性→框架映射） | >=2.5/3 为优秀 |
| **节奏变异度** | 段落节奏与标准节奏的偏离类型和幅度 | FULL_RHYTHM / RHYTHM_GAP / RHYTHM_BROKEN / RHYTHM_VARIANT |
| **跨段落节奏连贯性** | 相邻假设段落的节奏衔接模式（连续推导 / 并行并列 / 分叉展开） | 连续推导 > 分叉展开 > 并行并列（但构建类型决定最优模式） |
| **连接词密度** | 连接词总数 / Theory 总词数 × 100 | 顶刊中位数约 3-4 词/100词；<2 为"论证隐式化"，>5 为"连接词过载" |
| **因果连接词占比** | 因果类连接词数 / 总连接词数 | 机制推演型预期 ≥30%；过高（>50%）可能为因果词堆砌 |
| **条件连接词占比** | 条件类连接词数 / 总连接词数 | 假设树型/调节效应型预期 ≥15%；机制推演型预期 <10%；过高泄露隐性假设树结构 |
| **拍间过渡完整性** | 有显式连接词的拍间过渡数 / 总拍间过渡数（每假设段落 2 个拍间过渡点：方向→机制/证据，机制/证据→收敛） | ≥80% 为优秀，<50% 为"论证断裂" |
| **模块过渡完整性** | 有显式连接词的模块过渡数 / 5 | 5/5 为优秀，<3/5 为"模块碎片化" |
| **连接词-构建类型一致性** | 标志性连接词组合匹配度 | 高/中/低。低匹配 = 连接词使用模式与构建类型预期偏离 |
| **T6 / Closure 策略**（v1.2.0 新增，同步 write-theory v3.3.0） | 最后假设后是否有独立 Closure 段？或采用局部收束/嵌入框架总结/Discussion 开篇整合？ | 独立 Closure 段 = 非管理学标准；局部收束 = 标准；嵌入框架总结/Discussion 整合 = 可选策略 |
| **T6 Voice 质量**（如存在框架总结） | 框架总结是否使用 accountable first-person（"we have argued"），无被动语态 | 通过/失败/null |
| **T6 叙事接力**（v1.2.0 新增） | 如存在框架总结，结尾能量级是否 ≥ 最后假设推导段 | 通过/倒退/null |
| **Human Face 覆盖率**（v1.2.0 新增） | 有具体 actor/场景/案例的模块数 / 总模块数 | Hook/新构念/why-chain 关键步骤 ≥1 个 illustration 为优秀 |
| **主动语态比例**（v1.2.0 新增） | "We argue/hypothesize/predict" 次数 / 总主张句次数 | >=80% 为优秀；<50% 为机器声风险 |
| **识别策略理论嵌入**（v1.2.0 新增，制度冲击类） | Theory 中嵌入识别假设论证的模块数 / 需要的模块数 | 3/3 为优秀（IV/DiD/RDD/生存各需特定论证） |
| **微观动作完整性**（v1.4.0 新增） | 每个假设段落中 Anchor → Gap → Mechanism Move → Warrant → Prediction 的完整比例 | 5/5 为优秀，缺失任意动作即标记为薄弱 |
| **双边论证覆盖率**（v1.4.0 新增） | 调节/边界条件假设中同时论证 high/low 条件的比例 | 1.0 为优秀，<0.5 为严重缺失（对应 write-theory C20） |
| **替代解释排除率**（v1.4.0 新增） | 已识别的 competing explanations 中被主动排除的比例 | 1.0 为优秀；0 为高风险 |
| **论点-论据安排模式**（v1.4.0 新增） | 论文主要使用的安排模式（Warrant-Embedded / Warrant-First / Evidence-Contrast / Cumulative / Parallel） | 标记模式 + 是否功能等价 |
| **Concrete Illustration 密度**（v1.4.0 强化） | 每个 why-chain 步骤后是否有 illustration；连续两步无 illustration 的段落数 | 零缺失为优秀；≥1 处缺失为需关注 |
| **证据类型分布**（v1.4.0 新增） | Empirical / Theoretical / Boundary / Negative / Analogical 的比例 | 支持机制推演的 empirical/theoretical 应 ≥70% |
| **证据功能分布**（v1.4.0 新增） | support / qualify / contrast / pave / rebut 的比例 | support 为主但其他功能也需存在 |
| **文献引用三要素完整率**（v1.4.0 新增） | 同时满足 concrete finding + argument summary + link to mechanism 的引用比例 | ≥80% 为优秀 |
| **交互模式明确度**（v1.4.0 新增，对应 write-theory C10） | 调节假设是否明确 enhancing/buffering/antagonistic/existence/competing | 明确为优秀；缺失为失败 |
| **竞争假设收敛信号**（v1.4.0 新增，对应 write-theory C14） | 竞争假设是否使用非 "Therefore" 收敛信号 | 符合为优秀；违规为失败 |
| **辩证对立对称性**（v1.4.0 新增，对应 write-theory C16-C17） | 两个对立机制的步骤数是否对称；方向是否真正反转 | 对称+方向反转为优秀 |
| **Moderator 选择框架**（v1.4.0 新增，对应 write-theory C18） | ≥2 moderators 时是否有元框架解释选择理由 | 有为优秀；无为失败 |
| **连续 IV 三点论证**（v1.4.0 新增，对应 write-theory C19） | 连续 IV 是否论证 high / middle / low 三点的行为差异 | 完整为优秀；缺失为失败 |

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
| **Prose Craft Profile**（v1.2.0 新增） | Human Face / Showing vs Telling / Conversational Voice 的具体策略 | 见下方 Prose Craft 子维度 |

#### Prose Craft Profile 子维度（v1.2.0 新增）

| 子维度 | 提炼问题 | 输出格式 |
|--------|----------|----------|
| **Human Face 策略** | 论文如何在 T1 构念定义/T3 机制推演中嵌入具体场景？用公司名、人名还是行业实例？ | actor 类型分布 + 代表性例句 |
| **Showing 策略** | 论文如何在抽象因果步骤后配 concrete illustration？用案例、数字、场景还是具体研究？ | illustration 类型分布 + 代表性例句 |
| **Voice 策略** | 论文在假设推导中如何避免被动语态？使用哪些主动句式？T6 收束句式是什么？ | 主动句式模板 + 被动语态位置（如有） |
| **Stroke/Glide 控制** | 机制推演段落中动作（stroke）与评论（glide）的比例？是否有 forced march 或 ponderous pace？ | stroke/glide 比例 + 风险段落标记 |

**记录原则**：只记录该论文**明显区别于**同类构建类型其他范文的特征。通用特征（如"有 why chain"）不记入 Distinctive Features。

### 结构化报告输出（fine_grained profile）

```markdown
> **Fine-Grained Profile 输出模板**已外置：见 `protocols/profile_template.md`。Phase 3 结构化报告输出时加载并严格遵循。

> **Corpus Taxonomy for write-theory**（v1.4.0）已外置：见 `protocols/corpus_taxonomy.md`。Phase 4 沉淀建议映射到 write-theory corpus 结构时加载。

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
    standard_sequence: "T1→T2→T3→T4→T5→最后假设自然收敛进入 METHODS (10/17)"
    with_independent_t6: "T1→T2→T3→T4→T5→独立 T6 段落→METHODS (1/17, 非管理学标准)"
    theory_first: "T2→T1→T3→T4→T5→最后假设 (4/17, 均为构念辨析型)"
    boundary_embedded: "T5 嵌入 T3 (3/17)"
  closure_strategies:
    local_convergence_only: "12/17 — 管理学标准做法"
    embedded_framework_summary: "3/17 — 嵌入最后假设段末尾的 2-3 句框架总结"
    discussion_opening_compensation: "2/17 — Theory 无框架总结，Discussion 开篇整合"
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
  micro_move_patterns:
    full_sequence_rate: "12/17"
    most_common_missing_move: "Gap/Puzzle (4/17)"
    dominant_anchor_source: "empirical_finding (10/17)"
  bilateral_argumentation:
    complete: "8/10 — 调节型论文同时论证 high/low"
    incomplete: "2/10 — 只论证增强方向"
  arrangement_patterns:
    Warrant-Embedded: "10/17"
    Cumulative: "4/17"
    Evidence-Contrast: "2/17"
    Parallel: "1/17"
  evidence_typology:
    empirical_finding_avg: "55%"
    theoretical_argument_avg: "30%"
    boundary_condition_avg: "10%"
    negative_evidence_avg: "3%"
    analogical_evidence_avg: "2%"
  evidence_function_distribution:
    support: "70%"
    qualify: "15%"
    contrast: "10%"
    pave: "4%"
    rebut: "1%"
  three_element_citation_rate_avg: "78%"
  write_theory_constraint_alignment:
    C10_interaction_pattern_clear: "9/10"
    C20_bilateral_argumentation: "8/10"
    C18_moderator_selection_framework: "5/7"
  corpus_health_analysis:
    coverage_by_build_type:
      机制推演型:
        existing_skeletons: 8
        recommended_new: 2
        gaps: ["反直觉 Anchor 模式", "间接调节论证模板"]
      假设树型:
        existing_skeletons: 3
        recommended_new: 4
        gaps: ["多 moderator 元框架", "基线机制→条件分叉过渡"]
      构念辨析型:
        existing_skeletons: 5
        recommended_new: 0
        gaps: []
      调节效应型:
        existing_skeletons: 4
        recommended_new: 3
        gaps: ["完整双边论证模板", "common trunk + parallel branches 组织"]
    coverage_by_subprotocol:
      argumentation_patterns: {existing: 5, recommended_new: 3, gaps: ["理论驱动型 Anchor", "反直觉 Gap 构造"]}
      arrangement_patterns: {existing: 4, recommended_new: 2, gaps: ["Parallel 复杂假设组织", "Cumulative 间接调节组织"]}
      evidence_patterns: {existing: 3, recommended_new: 3, gaps: ["案例作为 Warrant", "制度逻辑作为证据"]}
      bilateral_argumentation_templates: {existing: 1, recommended_new: 3, gaps: ["high/low 完整双边", "条件连接词组合"]}
      moderator_selection_frameworks: {existing: 1, recommended_new: 2, gaps: ["environmental/organizational 二元框架", "2×2 resource source 框架"]}
    priority_queue:
      - rank: 1
        pattern: "多 moderator 选择元框架"
        corpus_path: "corpus/subprotocols/moderator_selection_frameworks.md"
        urgency: "高"
        reason: "假设树型/调节效应型论文普遍需要，但 corpus 中模板不足"
        suggested_source_papers: ["Shen_etal_2022_JOM"]
      - rank: 2
        pattern: "间接调节/Mediated Moderation 论证"
        corpus_path: "corpus/subprotocols/argumentation_patterns.md"
        urgency: "高"
        reason: "复杂假设论文需要，但当前缺少独立理论论证模板"
        suggested_source_papers: ["Singh_Grewal_2023_JMR"]
      - rank: 3
        pattern: "完整双边论证句法"
        corpus_path: "corpus/subprotocols/bilateral_argumentation_templates.md"
        urgency: "中"
        reason: "C20 要求，多篇调节型论文有优质模板可沉淀"
        suggested_source_papers: ["Shen_etal_2022_JOM"]
    over_represented:
      - pattern: "两步中介机制"
        count: 12
        note: "已足够丰富，新蒸馏可不再优先收录"
      - pattern: "独立 T6 Closure 段落"
        count: 1
        note: "非管理学标准，应持续标记为反模式"
```

### 跨 Section 对齐检查（Phase 4 正式化，v1.2.0 新增）

与 write-theory Phase 4.3（跨 Section 对齐检查）对齐，执行 Introduction ↔ Theory 的强制对齐检查：

```markdown
### 跨 Section 对齐检查

| 维度 | 检查项 | Introduction 信号 | Theory 状态 | 结论 |
|------|--------|-------------------|-------------|------|
| Gap→Type | 能量匹配 | [Gap类型] + [Tension] | [构建类型] | ✅/⚠️/❌ |
| Makadok→Module | 贡献兑现 | [Makadok维度] | [模块覆盖] | ✅/⚠️/❌ |
| Preview→H | 假设数 | "[N] hypotheses" | [实际N个] | ✅/⚠️/❌ |
| Lens→Lens | 理论一致性 | "[theory]" | "[theory]" | ✅/❌ |
| Knot→T1/T2 | Knot 继承 | [central_knot_statement] | [knot_inheritance_statement] | ✅/⚠️/❌ |
| Characters→T1 | 角色一致性 | [protagonist] + [supporting] | [Theory 中出场次数] | ✅/⚠️/❌ |
| T6→Results | 框架总结与 Results 一致 | [框架总结内容 / 无] | [Results 发现方向] | ✅/⚠️/❌ |

**必须修复的不一致**（如为单篇蒸馏，记录为模仿风险提示）：
- [ ] [具体不一致项1]
- [ ] [具体不一致项2]
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

> 回写提醒的完整清单（向 write-theory SKILL.md / corpus 各文件的回写格式与时机）已外置：见 `protocols/writeback_reminders.md`。Phase 4.5 执行回写时加载。

## Phase 5 — 质量验证与 QC 输出

> QC Checklist、最终输出物清单与模仿风险提示模板已外置：见 `protocols/phase5_qc.md`。Phase 5 质量验证时加载。

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
- **不将独立 T6 Closure 作为默认推荐**：write-theory v3.3.0 已明确管理学顶刊不要求独立 Closure 段落。蒸馏时记录独立 T6 存在性，但不再标记 "T6 缺失" 为默认风险。
- **不将四段式分离结构作为唯一节奏目标**：write-theory v3.3.0 以交织式为默认。蒸馏时区分 interwoven / separated / hybrid，关注功能等价性而非机械拍数。
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

- **`write-theory`** — Phase 4 的更新建议可直接沉淀到 write-theory 的模块库和骨架库；Phase 2.5 连接词统计可为 write-theory 的 Phase 3 transition 诊断与 Phase 5 `corpus/sentences/closure.md` 提供输入。Phase 2.1.6–2.1.8 的微观动作、安排模式、证据类型/功能可直接沉淀为 `corpus/subprotocols/argumentation_patterns.md`，供 write-theory Phase 3（语料调用）调用。Phase 0.5 Rising Action 数据和 Phase 0.75 Prose Craft 数据可为 write-theory 的叙事对齐检查和 Prose Craft 定位提供输入
- **`theory-review`** — Phase 1.5 的模块覆盖检查和 Theory Logic Map 可作为 theory-review 的审查基准；Phase 1.25 的制度冲击适配检查可为理论审查提供识别策略论证依据；Phase 2.1.6–2.1.8 的微观动作、双边论证、证据三要素检查可为 theory-review 提供段落级论证审查清单
- **`paper-review`** — Theory Logic Map 可用于跨 section 对齐检查（Theory 承诺 vs Results 兑现）；Phase 4 的跨 Section 对齐表可直接用于 paper-review 的全稿对齐检查；write-theory Constraint Alignment 表可用于 Theory ↔ write-theory 协议一致性审查
- **`write-introduction`** — T2 Theoretical Lens 和 Closure 策略（局部收束 / 嵌入框架总结）的提炼可用于优化 Introduction 的 P5 Preview 和 P7 Contribution；Phase 0.5 的 knot 继承检查可为 Introduction→Theory 叙事接力提供验证；Phase 2.1.6 的 Anchor/Gap/Prediction 序列可为 Introduction 的 Gap→Preview 结构提供节奏参照
- **Vault** — Fine-Grained Profile 存入 Vault 的 `fine_grained/batch_*/[paper]_distilled_theory.md`；新发现的论证模式存入 `skill_update_recommendations/argumentation_patterns/`

## 外部资产位置

- **外置协议文件**: `protocols/`（quick_reference.md、pollock_annotations.md、phase2_extraction_frameworks.md、connector_patterns.md、profile_template.md、corpus_taxonomy.md、writeback_reminders.md、phase5_qc.md）
- **现有语料库索引（本机路径，不随 repo 同步）**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/theory/mvp30/_mvp30_theory_index.md`
- **蒸馏产出存放（本机路径，不随 repo 同步）**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/theory/mvp30/fine_grained/batch_*/[paper]_distilled_theory.md`
- **更新建议存放（本机路径，不随 repo 同步）**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/theory/mvp30/skill_update_recommendations/`

## 输出结构参考

各 Phase 输出的结构化字段见各 Phase 正文中的 YAML/Markdown 表格。完整字段名和取值枚举已在 Phase 0–5 的示例输出块中逐一定义，无需单独维护 JSON Schema。

如需机器消费格式，参考 Vault 中已蒸馏的 `fine_grained/` 目录下的实际报告文件——其结构和字段集比抽象 schema 更准确地反映真实输出。

---
*基于 nuwa-skill 流水线框架、Pollock 2025 Ch02-Ch06、Dorobantu et al. (2024)、Shepherd & Wiklund (2020) 叙事规则、MVP30 范文语料库构建。版本 1.4.0 — Theory 蒸馏 Meta-Skill（同步 write-theory v3.3.0）。*
