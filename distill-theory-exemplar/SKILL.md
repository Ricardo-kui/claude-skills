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

## Phase 0.5 — Rising Action 定位与 Central Knot 继承检查（Pollock Ch02，v1.2.0 新增）

Theory & Hypotheses 在整篇论文的 Five-Act 结构中属于 **Rising Action** 的后半段。蒸馏时必须检查 Theory 是否继承了 Introduction 建立的 Central Knot，并验证叙事连续性。

### 输入接口

如果输入包含 Introduction 文本或上游 `write-introduction` 输出的 `theory_hints` YAML 块，解析以下字段：
- `central_knot_statement`：如果存在且非 `null` → 作为 Theory 的叙事锚点
- `narrative_arc`：决定 Theory 的 rising action 强度
- `protagonist_construct` / `supporting_constructs`：作为角色定位初始值

### Central Knot 推断规则（当上游未提供时）

从 Theory 文本自身推断核心冲突：
- Incommensurability → "对立理论或证据之间的矛盾冲突"
- Inadequacy → "现有解释存在盲区或基于错误假设"
- Incompleteness → "遗漏了关键维度、机制或时点"
- 具体推断：从 T3 Mechanism Chain 的转折信号词或 T2 Theoretical Lens 的框架对立中提取

### Phase 0.5 诊断流程

按顺序检查以下叙事对齐项：

1. **Knot 继承检查**
   - Theory P1（T1/T2）是否明确或暗示地承接了 Introduction 的 central knot？
   - 标志："To resolve the paradox that [knot]..." / "To explain why [knot]..."
   - 如无 explicit 承接，检查是否 implicit 通过 Gap 文献的延续来承接

2. **Rising Action 强度检查**
   - 对比 Introduction 的 `narrative_arc` 与 Theory 的 rising action 强度
   - Theory 的 rising action 应 ≥ Introduction 的 closing energy，为 Results climax 蓄力
   - 检测：T1-T2 能量级是否低于 Introduction P7-P8 → 标记"叙事阶段倒退"

3. **Characters 一致性检查**
   - Theory 中的主角/配角是否与 Introduction 承诺的一致？
   - Introduction 承诺了 mediator M，但 Theory T1 未定义 M → 标记"角色缺失"
   - Introduction 的 protagonist 在 Theory 中出场次数 < 3 → 标记"主角淡出"

4. **Plot Emergence 检查**
   - 情节是否从构念互动中自然浮现，而非强加？
   - 检测：T3 的 why chain 是否从 T2 的理论框架自然推导而来？
   - T3 引入了新理论视角但未在 T2 铺垫 → 标记"extraneous storyline"

### 输出格式

```yaml
phase_0_5_rising_action:
  central_knot_inherited: true/false
  knot_inheritance_statement: "[Theory 中承接 knot 的具体句子]"
  knot_inheritance_location: "T1/T2/P[段号]"
  narrative_arc_continuity: "一致 / 增强 / 倒退"
  protagonist_consistent: true/false
  protagonist_presence_in_theory: "[N] 次提及"
  supporting_construct_consistent: true/false
  missing_promised_construct: "[如有，列出 Introduction 承诺但 Theory 未定义的构念]"
  plot_emergence_natural: true/false
  extraneous_storyline_risk: "[描述，如无则 null]"
```

---

## Phase 0.75 — Prose Craft 定位（Pollock Ch03，v1.2.0 新增）

Theory section 的 Rising Action 不仅需要功能推进，还需要 prose 层面的可读性。以下三个工具与 Phase 1-5 并行执行。

### 1. Human Face in Theory

| 检查点 | 通过标准 | 蒸馏记录 |
|--------|---------|---------|
| P1 Knot Inheritance | 用 1 句具体场景说明"这个问题在现实世界中长什么样" | 记录具体场景句 |
| P2-P4 新构念首次出现 | 每个新构念首次出现时配 1 个具体例子 | 记录构念名+例子内容 |
| P5-PN Why-chain 关键步骤 | 每个 why-chain 关键步骤可配 1 个微型场景（1-2句） | 记录微型场景句 |

### 2. Showing vs Telling in Theory

| 检查点 | 通过标准 | 蒸馏记录 |
|--------|---------|---------|
| Stroke 段落（70%） | 每个抽象因果步骤后，跟 1 句 concrete illustration | 记录 illustration 类型和频率 |
| Glide 段落（30%） | 用比喻/类比解释抽象概念 | 记录比喻/类比句 |
| 连续无 showing | 不允许连续 2 个 stroke 句子无 showing | 标记断裂位置 |

### 3. Conversational Voice in Theory

| 检查点 | 通过标准 | 蒸馏记录 |
|--------|---------|---------|
| P1 承接 | "To resolve the paradox that [knot], we argue that..." | 记录承接句式 |
| 假设推导 | "We argue that..." / "We hypothesize that..." | 记录主动语态频率 |
| T6 收束 | "In sum, we have argued that..." | 记录收束句式 |
| 禁止被动 | 无 "It is argued that..." / "It is hypothesized that..." | 标记被动语态位置 |

### Prose Craft 输出格式

```yaml
phase_0_75_prose_craft:
  human_face:
    p1_scene_present: true/false
    p1_scene_text: "[具体场景句]"
    construct_illustrations:
      - construct: "[构念名]"
        illustration: "[例子内容]"
        location: "T[模块] P[段号]"
    why_chain_scenes:
      - step: "[机制步骤]"
        scene: "[微型场景]"
        location: "P[段号]"
  showing_vs_telling:
    stroke_paragraphs: N
    glide_paragraphs: N
    stroke_glide_ratio: "N:N"
    illustration_types: ["案例", "数字", "场景", "具体研究"]
    showing_gaps: ["[断裂位置描述]"]
  conversational_voice:
    active_voice_count: N
    passive_voice_count: N
    passive_voice_locations: ["P[段号]: [原句]"]
    hypothesis_transition_phrases: ["Therefore, we hypothesize:", "Thus:"]
    closure_phrase: "[T6 收束句]"
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

### 2.1.5 论证节奏提炼（Argument Rhythm Distillation）

Theory 写作的核心单元不是模块，而是**段落内部的论证节奏**。借鉴 Results 的"四拍节奏"蒸馏逻辑（方向→显著性→幅度→支持判断），Theory 同样存在可量化的段落级论证节奏，但节奏形态因模块功能和构建类型而异。

#### 核心节奏：T3/T4 Hypothesis Development 段落交织式论证链（与 write-theory v3.3.0 对齐）

write-theory v3.3.0 将每个假设推导段落定义为**交织式论证链（Interwoven Logic Chain）**：
**Topic Sentence → Theoretical Reasoning + Literature Support（交织） → Hypothesis Transition**

文献引用与理论推理**交织**而非先后排列——这是管理学顶刊的默认写法。蒸馏中**最重要的节奏目标**是每个假设推导段落完成功能等价的论证：方向锚定、机制推演（文献锚定）、假设收敛。

```text
[拍1-方向]: Topic Sentence — 本段要证明什么
  → 功能：锚定段落论点，限定范围
  → 示例："Drawing on [theory], we argue that the effect of [X] on [Y] operates through [M]."
  → 失败信号：段首句只陈述事实不表达论点 / 只定义变量不预告要证明的关系

[拍2-机制+证据交织]: Reasoning & Literature Interwoven — 为什么 X 影响 Y
  → 功能：逐步展示因果链，每步由文献或理论依据锚定
  → 节奏模式：
     "Prior research has established that [X→state1] ([citation]). However, it remains 
     unclear how [state1] leads to [Y]. We argue that [state1] creates [state2] 
     because [theoretical justification]. Consequently, [state2] affects [Y] 
     through [final link]."
  → 失败信号：X→Y 直接跳跃无中间步骤 / 用 "obviously" 代替论证 / 只有 citation list 无机制 / 文献支撑与机制步骤脱节

[拍3-收敛]: Hypothesis Transition — 从机制到可检验预测
  → 功能：将机制推演固化为形式化假设
  → 标志词："Therefore, we hypothesize:" / "Thus:" / "Accordingly, we predict:"
  → 示例："Therefore, we hypothesize: Hypothesis 1: [X] is positively related to [M]."
  → 失败信号：Therefore 方向与机制推理方向矛盾 / 假设缺少方向或边界条件
```

**备选节奏：分离式（少数情况）**——当某一步的文献支持特别密集、需要单独展开时，可暂时将 [机制] 和 [文献] 分离。但整个段落的默认节奏是交织的。蒸馏时标记论文使用的是交织式还是分离式。

#### 交织式论证链各要素 QC 提取（与 write-theory v3.3.0 对齐）

对每个假设推导段落，提取以下 QC 指标：

| 要素 | 提取问题 | 失败信号 | 记录格式 |
|------|---------|---------|---------|
| **Topic Sentence 精准度** | 是否同时包含话题+核心观点+限定范围？是否使用 active verb + concrete subject？段首句是否在 15 词内说出核心判断？ | 段首句只陈述事实/只定义变量/无主语被动语态（"It is argued that"） | `{topic_sentence_quality: "高/中/低", word_count_to_core_claim: N, has_active_verb: true/false, has_concrete_subject: true/false}` |
| **Reasoning-Literature 交织度** | 文献引用是否嵌入在机制链步骤中？每个引用是否总结了 argument 并链接到 concrete finding？ | 独立的文献罗列段落；citation 与 mechanism 步骤脱节；citation 替代机制推演 | `{interwoven: true/false, citations_count: N, argument_summarized_count: N, concrete_finding_linked_count: N, citation_vs_mechanism_alignment: "高/中/低"}` |
| **Theoretical Reasoning 完整性** | 从 X 到 Y 的每一步因果推理是否明确写出？每步间是否有 explicit transition？ | 逻辑跳跃（省略关键步骤）；缺少 transition（从 A 直接跳到 C）；用 "obviously" 代替论证 | `{mechanism_steps_count: N, logical_jumps: ["从 X 到 M 缺少中间步骤"], transitions: ["Consequently", "Thus", "In turn"]}` |
| **Hypothesis Transition 收敛质量** | 收束句是否总结了推理链而非简单重复 "we hypothesize"？ | 无理论收束直接 "we hypothesize"；Therefore 方向与机制矛盾 | `{has_theoretical_closure: true/false, transition_phrase: "Therefore/Thus/Accordingly", hypothesis_direction_matches_mechanism: true/false}` |
| **Concrete Illustration（可选）** | 每个因果步骤后是否有 1 句 concrete illustration？ | 连续 2 个推理步骤无 illustration | `{illustration_count: N, illustration_types: ["案例", "场景", "比喻"], showing_gaps: ["步骤2无 illustration"]}` |
| **识别策略嵌入**（制度冲击类） | Theory 中是否嵌入了对识别假设的理论论证？ | Methods 描述了识别策略但 Theory 完全未提及 | `{identification_strategy_in_theory: true/false, iv_exclusion_restriction: "...", did_parallel_trends: "...", location: "P[段号]"}` |
| **节奏变体标记** | 论文使用的是交织式还是分离式？是否功能等价？ | 分离式但文献与机制无明确链接 | `{rhythm_variant: "interwoven / separated / hybrid", functional_equivalent: true/false}` |

**逻辑跳跃诊断**：逐句标记因果连接词（Consequently/Thus/Thereby/As a result/This leads to...）。缺少中间步骤 → 记录具体跳跃位置。

**Topic Sentence 反模式示例提取**：
- ❌ 被动语态例句："It is argued that CEO overconfidence affects firm risk." → 记录并标记为违反 Conversational Voice
- ✅ 主动语态例句："We argue that CEO overconfidence increases firm risk-taking because overconfident leaders systematically underestimate downside uncertainty." → 记录为优质模板

#### 段落论证节奏的构建类型变体

交织式节奏的形态因构建类型而异：

| 构建类型 | 机制+证据交织形态 | 收敛形态 | 节奏特征 |
|----------|-------------------|----------|---------|
| **机制推演型** | 多步因果链，每步嵌入 citation | "Therefore, H1: X→M; H2: M→Y" | 一个机制链收敛为一个或多个假设 |
| **构念辨析型** | 差异化维度对比，每个差异维度嵌入 citation | "Thus, A and B are distinct constructs that..." | 交织形态为对比+证据，收敛可能为命题而非假设 |
| **假设树型** | 主效应机制 → 条件化分叉，分叉处嵌入 citation | "Therefore, H1: X→Y; H2: X→Y moderated by W" | 基线机制与调节逻辑交织 |
| **质性过程理论型** | 阶段序列 (Phase 1→2→3) + 过渡条件，每阶段嵌入 citation | "Proposition 1: In Phase 1, [process] occurs" | 按时间/阶段展开 |
| **调节效应型** | X→Y 主机制 + W 如何改变该机制，嵌入调节方向 citation | "H1: X→Y positive; H2: X×W→Y [direction]" | 主效应与交互逻辑交织 |

#### 节奏变体记录

蒸馏时必须区分：
- **INTERWOVEN（默认）**：文献引用嵌入 why-chain 的每一步
- **SEPARATED（少数）**：机制段落先完整推演，再用单独段落密集支撑文献
- **HYBRID（混合）**：局部交织+局部分离

记录格式：
```yaml
rhythm_pattern:
  primary: "interwoven / separated / hybrid"
  evidence: "[具体段落位置与句式]"
  functional_equivalent: true/false  # 是否完成功能等价的论证
```

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

| 模块 | 预期节奏单元 | 评分方式 | 纳入 Phase 3 DNA |
|------|-------------|---------|-----------------|
| T1 Construct Definition | 3-4 拍 | 每拍 0-1 分（存在且功能明确=1） | `t1_rhythm_completeness` |
| T2 Theoretical Lens | 3 拍 | 每拍 0-1 分 | `t2_rhythm_completeness` |
| T3/T4 Hypothesis Development | 交织式 3 单元（方向→机制/证据交织→收敛）/假设段落 | 每单元 0-1 分，多段落取均值；同时标记 rhythm variant | `t3t4_rhythm_completeness` |
| T5 Boundary Condition | 3 拍（条件引入→理论依据→预测修正） | 每拍 0-1 分 | `t5_rhythm_completeness` |
| T6 / Closure 策略 | 局部收束（必须）+ 可选框架总结 | 局部收束：有/无；框架总结：嵌入/Discussion/缺失 | `closure_strategy_completeness` |

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
      rhythm_type: "交织式机制推演"
      beat_1_direction: {score: 1, max: 1, evidence: "Topic sentence 明确预测 X→M 关系"}
      beat_2_mechanism_literature_interwoven: {score: 1, max: 1, evidence: "两步因果链完整，citation 嵌入每一步 (X→state→M)"}
      beat_3_convergence: {score: 1, max: 1, evidence: "Therefore, H1: X positively related to M"}
      completeness: "3/3"
      rhythm_quality: "✓ — 完整交织节奏"
    H2_paragraph:
      paragraph_id: "P5"
      rhythm_type: "交织式机制推演"
      beat_1_direction: {score: 0, max: 1, evidence: "段首句只定义 M，未预告要证明 M→Y"}
      beat_2_mechanism_literature_interwoven: {score: 1, max: 1, evidence: "M→Y 机制链完整，citation 嵌入机制"}
      beat_3_convergence: {score: 1, max: 1, evidence: "Therefore, H2: M positively related to Y"}
      completeness: "2/3"
      rhythm_quality: "△ — 缺少方向拍（段首未锚定论点）"
    overall_t3t4_rhythm: "83.3% (5/6)"
  rhythm_pattern_notes:
    - "H1/H2 使用连续推导节奏：H1 的收敛句引出 M，H2 的机制+证据交织从 M 继续推演"
    - "citation 在两步机制中均匀分布（每步 1-2 个 citation），非堆砌"
    - "T1 缺少 scope condition 拍，在构念辨析型中这是致命伤，在机制推演型中风险较低"
```

#### 节奏质量评级

| 评级 | 标准 | 蒸馏动作 |
|------|------|---------|
| **FULL_RHYTHM** | 段落所有拍完整且功能明确 | 标记为高可信度范文段落，优先纳入 Phase 4 骨架库 |
| **RHYTHM_GAP** | 缺失 1 拍 | 记录缺失的具体拍和功能后果，纳入模仿风险提示 |
| **RHYTHM_BROKEN** | 缺失 ≥2 拍或拍顺序混乱 | 标记为不可模仿的反模式，提取其"修复后"骨架（补全缺失拍） |
| **RHYTHM_VARIANT** | 拍数或拍序与标准不同但功能等价 | 记录为节奏变体，丰富 Phase 4 的节奏模式库 |

### 2.1.6 假设论证微观动作提取框架（Micro-Moves for Hypothesis Argumentation）

交织式节奏回答了段落的**形态**，但没有回答作者在段落中具体执行了哪些**说服动作**。本节提供一个**分析透镜**，帮你在阅读顶刊范文时识别：作者是用哪几个动作完成从起点到假设的推导的。这些标注结果最终可用于对比多篇论文、归纳该构建类型的典型论证路径，并沉淀为 `write-theory` 的写作模式。

#### 标准微观动作序列（用于分析范文）

```text
[Anchor]        → 论文固定的论证起点： prior finding / theoretical premise / accepted scope condition
     ↓
[Gap/Puzzle]    → 论文指出的现有解释缺口、边界或反直觉之处
     ↓
[Mechanism Move]→ 论文提出的新因果步骤或条件化逻辑
     ↓
[Warrant]       → 论文用理论或文献说明该机制步骤为何成立
     ↓
[Prediction]    → 论文收敛到可检验假设的方式
```

**每个动作的识别信号**（蒸馏时从原文提取）：

| 动作 | 典型句法 | 在范文中的功能 | 标注为缺失的风险 |
|------|---------|--------------|----------------|
| **Anchor** | "Prior research has established that..." / "A long-standing assumption in the literature is..." | 让读者接受论证起点 | 起点是作者自己的断言而非学界共识 |
| **Gap/Puzzle** | "However, it remains unclear whether..." / "What remains less understood is..." | 制造认知张力 | 无 gap，直接 "we argue" |
| **Mechanism Move** | "We argue that [X] leads to [state] because..." | 提出新的因果机制 | X→Y 直接跳跃，无中间状态 |
| **Warrant** | "This is consistent with [theory], which posits that..." / "[Author] (year) found that..." | 为机制步骤提供合法性 | Warrant 只是 citation list，未与机制步骤链接 |
| **Prediction** | "Therefore, we hypothesize:..." | 把机制固化为假设 | 假设方向与机制推理矛盾 |

#### 蒸馏任务：微观动作标注

对每个假设推导段落，标注：

```yaml
phase_2_1_6_micro_moves:
  H1_paragraph:
    paragraph_id: "P4"
    moves_detected:
      - move: "Anchor"
        evidence: "Prior research has established that X increases state A (Smith, 2010)."
        source: "empirical_finding"
      - move: "Gap"
        evidence: "Yet how state A translates into Y remains unclear."
      - move: "Mechanism Move + Warrant"
        evidence: "We argue that state A creates state B because [theory] posits... (Jones, 2012)."
      - move: "Prediction"
        evidence: "Therefore, we hypothesize: H1: X is positively related to Y."
    missing_moves: []
    move_quality: "完整序列"
```

#### 双边论证提取（Bilateral Argumentation）

`write-theory` Constraint 20 规定：调节/边界条件段落应同时论证 "when M=high → effect" 和 "when M=low → effect"。蒸馏时记录范文是否遵守该规则，以及它是如何用具体句法完成双边论证的——这些句法可沉淀为 `write-theory` 的调节论证模板。

蒸馏时必须提取：

```yaml
bilateral_argumentation:
  moderator: "W"
  high_condition:
    present: true/false
    mechanism: "When W is high, X→Y is strengthened because..."
    evidence: "[citation supporting high-condition mechanism]"
  low_condition:
    present: true/false
    mechanism: "When W is low, X→Y is weakened because..."
    evidence: "[citation supporting low-condition mechanism]"
  symmetry: "完整 / 仅单边 / 缺失"
  note_for_corpus: "如完整，提取其 high/low 论证句法作为 write-theory 模板候选"
```

#### 替代解释排除（Ruling Out Alternatives）

提取范文如何处理 competing explanations——这是判断一篇 Theory 是否"self-aware"、是否提前回应审稿人质疑的关键。记录其排除策略和典型句法，可作为 `write-theory` 中竞争假设/反直觉预测型论文的写作参照。

| 排除策略 | 典型表达 | 蒸馏标记 |
|---------|---------|---------|
| **理论不一致** | "This alternative account would predict the opposite effect..." | `theoretical_inconsistency` |
| **范围条件** | "Such an explanation applies to [context], but our setting involves..." | `scope_condition` |
| **经验证据反例** | "Recent evidence, however, shows that..." | `empirical_counter` |
| **机制不可通约** | "While plausible, this mechanism does not explain why..." | `mechanism_incommensurable` |

记录格式：
```yaml
alternative_explanations:
  competing_accounts: ["account1", "account2"]
  ruling_out_strategy: ["theoretical_inconsistency", "scope_condition"]
  location: "P[段号]"
  completeness: "完整 / 部分 / 缺失"
```

### 2.1.7 论点-论据安排模式提取（Argument-Evidence Arrangement Patterns）

节奏和微观动作回答"段落内部发生什么"，安排模式回答"范文的论点和论据被组织成什么样的完整论证"。本节提供一套**分类框架**，帮你在对比多篇论文时识别：同一构建类型是否偏好某种安排方式？不同期刊/主题是否存在安排差异？这些模式可沉淀为 `write-theory` 的段落组织建议。

#### 五种标准安排模式（分类用）

| 模式 | 结构 | 适用场景 | 构建类型倾向 |
|------|------|---------|-------------|
| **Warrant-Embedded** | Claim → Reasoning + Evidence 交织 → Hypothesis | 默认；大多数机制推演型 | 机制推演型、假设树型 |
| **Warrant-First** | Claim → 密集理论依据 → 机制推演 → Hypothesis | 理论依据特别密集，需要单独展开 | 构念辨析型、理论密集型 |
| **Evidence-Contrast** | 反方证据 → 转折 → 自己的机制 → Hypothesis | 论文要挑战既有观点 | 反直觉预测型、辩证对立型 |
| **Cumulative** | H1 收敛 → H2 从 H1 的收敛点继续推演 | 假设间有逻辑依赖 | 中介链、两步机制 |
| **Parallel** | 共享同一理论框架的多个假设分别推导 | 假设间相互独立但同属一个理论 | 构念辨析型、多主效应 |

#### 蒸馏任务：安排模式识别

```yaml
phase_2_1_7_arrangement_pattern:
  primary_pattern: "Warrant-Embedded"
  secondary_pattern: "Cumulative"
  evidence: "H1 段末收敛到 M；H2 段首直接 'Building on this mechanism, we next argue M→Y'"
  paragraph_flow:
    - paragraph_id: "P4"
      function: "Anchor + Mechanism Move"
      arrangement: "Warrant-Embedded"
    - paragraph_id: "P5"
      function: "Cumulative extension from P4"
      arrangement: "Cumulative"
```

#### Concrete Illustration 提取

`write-theory` Phase 3（段落级 QC 检查表）把"不允许连续 2 个推理步骤无 illustration"作为写作规则。本节用于**提取范文如何执行这一规则**：它在哪些步骤放 illustration？用的是什么类型？哪些步骤省略了？这些提取结果可作为 `write-theory` Prose Craft 子协议的素材。

```yaml
concrete_illustration_pattern:
  illustration_density: "每个推理步骤后 1 句 / 每 2 步 1 句 / 稀疏"
  illustration_types:
    - type: "公司案例"
      example: "When Apple faced [situation], [mechanism] produced [outcome]."
    - type: "数字场景"
      example: "A 1-standard-deviation increase in X corresponds to..."
    - type: "比喻"
      example: "This is akin to..."
  missing_illustration_steps: ["步骤2", "步骤3"]
  note_for_corpus: "如某类 illustration 在同类论文中高频出现，可沉淀为 write-theory 推荐"
```

#### 复杂假设的段落安排

对假设树型、中介+调节混合、多调节型论文，提取其**段落级组织逻辑**。重点不是判断对错，而是记录：范文如何把多个假设编织进一个连贯叙事？假设之间靠什么连接词/逻辑关系衔接？这些信息可直接用于优化 `write-theory` 的复杂假设路由。

```yaml
complex_hypothesis_organization:
  pattern: "common_trunk → dual_branch"  # 或 baseline_first → moderation_second / mediation_chain
  common_trunk_paragraphs: ["P4"]
  branch_paragraphs:
    - branch_id: "H1"
      paragraph: "P5"
      relationship_to_trunk: "direct effect from common mechanism"
    - branch_id: "H2"
      paragraph: "P6"
      relationship_to_trunk: "moderation of trunk mechanism"
  relationship_between_hypotheses: "sequential / parallel / nested"
  clarity_risk: "如分支间关系不自明，需框架总结"
```

### 2.1.8 证据类型与功能编码（Evidence Typology & Function Coding）

`distill-theory-exemplar` 已经检查 citation 是否总结 argument 并链接 concrete finding，但还没有系统分析**范文把什么当证据、证据执行什么功能、如何与论点交织**。本节提供一个编码框架，帮你在阅读时识别：顶刊作者是用 empirical finding 支撑机制？用 theoretical argument 做 warrant？还是用 negative evidence 排除替代解释？编码结果可沉淀为 `write-theory` 的证据使用指南。

#### 证据类型学（用于编码范文中的证据）

| 证据类型 | 定义 | 典型来源 | 在 Theory 中的摆放位置 |
|---------|------|---------|---------------------|
| **Empirical Finding Evidence** | 前人研究的 concrete result | 实证论文 | 支撑机制步骤的 why chain |
| **Theoretical Argument Evidence** | 理论家的核心主张或理论逻辑 | 理论论文 | 为 mechanism move 提供合法性 |
| **Boundary Condition Evidence** | 说明某机制只在某范围内成立 | 边界条件研究 | 引出或支撑 T5 |
| **Negative Evidence** | 前人未发现或机制不成立的证据 | 零结果、反例研究 | 排除替代解释、强化 gap |
| **Analogical Evidence** | 比喻、类比、案例 | 案例研究、行业报告 | 在抽象机制后提供 concrete illustration |

#### 证据功能标注

每个 citation 必须标注其功能：

| 功能 | 作用 | 典型连接词 |
|------|------|----------|
| `support` | 直接支持当前机制步骤 | "Consistent with this logic..." |
| `qualify` | 限定机制的适用范围 | "However, this effect is limited to..." |
| `contrast` | 与当前机制形成对比，引出转折 | "In contrast, ..." / "Whereas ..." |
| `pave` | 为后续推理铺路 | "This raises the question of whether..." |
| `rebut` | 排除替代解释 | "This alternative account cannot explain..." |

#### 文献引用三要素模板

`write-theory` 要求每个引用总结 argument 并链接 concrete finding。提炼可复用的三要素句式：

```text
[Author] (year) found that [concrete finding] — [argument summary].
This suggests that [mechanism step], because [theoretical reason].
```

蒸馏时提取每个 citation 是否满足三要素：

```yaml
evidence_three_element_check:
  citation: "Smith (2010)"
  concrete_finding: "firms delaying recalls experienced 23% greater stock-price declines"
  argument_summary: "market punishes uncertainty more than bad news"
  link_to_current_mechanism: "consistent with our argument that X increases perceived uncertainty"
  three_elements_complete: true/false
```

#### 蒸馏任务：证据地图

为每个假设推导段落生成证据地图：

```yaml
phase_2_1_8_evidence_map:
  H1_paragraph:
    paragraph_id: "P4"
    evidence_items:
      - citation: "Smith (2010)"
        type: "empirical_finding"
        function: "support"
        mechanism_step: "X → state A"
        three_elements_complete: true
      - citation: "Jones (2012)"
        type: "theoretical_argument"
        function: "pave"
        mechanism_step: "state A → state B"
        three_elements_complete: true
    evidence_type_distribution: {"empirical_finding": 2, "theoretical_argument": 1}
    evidence_function_distribution: {"support": 2, "pave": 1}
    evidence_placement: "embedded_in_mechanism"  # 或 "separate_literature_block" / "front_loaded"
```

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

连接词是 Theory 论证逻辑的**显式标记**——它们将隐含的因果、对比、递进关系暴露给读者。蒸馏连接词使用模式可以直接反哺 `write-theory` 的连接词与收束语料（Phase 3 段落级 transition 诊断 + Phase 5 `corpus/sentences/closure.md` 收束/过渡句式）。

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
| **总结** | Taken together, In sum, Overall, Collectively, In summary | 综上、整体而言 | 嵌入最后假设段末尾的框架总结 / 假设段落的最后一句 | `summary_N` |
| **强调** | Notably, Importantly, Critically, It is worth noting that, Key to this argument | 值得注意的是、关键在于 | T2（理论核心洞察）, T4（假设关键方向） | `emphasis_N` |

#### 段落内连接词节奏（Beat Connector Pattern）

连接词在论证节奏的**拍间过渡**中承担特定功能。蒸馏时记录每拍的拍间连接词类型：

```text
交织式论证链的拍间连接词模式：
[拍1-方向] → [拍2-机制+证据交织]:
  典型连接词: "Specifically, ..." / "We argue that..." / "Prior research shows..."
  蒸馏标记: beat1→2_connector = "specificity" / "evidence_pivot" / "none (direct)"

[拍2-机制+证据交织] → [拍3-收敛]:
  典型连接词: "Therefore, ..." / "Thus, ..." / "Accordingly, ..." / "Taken together, these arguments suggest..."
  蒸馏标记: beat2→3_connector = "causal" / "summary"
```

**拍间连接词缺失为高风险**：如果机制到假设的过渡没有因果连接词（直接 "H1: X is positively related to Y"），标记为 "无收敛信号"——假设像是从天而降，而非从机制推导。

**交织式典型信号**：当段落中出现 "Prior research shows X. However, what if Y? We argue that Z because..." 时，记录为文献与推理交织的标准模式。

#### 模块间过渡连接词模式

记录 T1→T2→T3→T4→T5→T6 模块序列中每个过渡点的连接词：

| 过渡点 | 典型连接词 | 功能 | 缺失风险 |
|--------|-----------|------|---------|
| T1→T2 | "Drawing on [theory], we..." / "To explain [these relationships], we adopt..." | 从构念界定过渡到理论框架 | T2 像硬插入的新话题 |
| T2→T3 | "Building on this lens, we develop..." / "[Theory] suggests that..." | 从理论框架过渡到机制推演 | T2 说完就扔，未驱动 T3 |
| T3→T4 (每假设) | "Therefore, we hypothesize:" / "Accordingly:" / "Thus:" | 从机制链收敛到假设 | 假设无推导信号 |
| T4(H_n)→T4(H_{n+1}) | "Having established H1, we next consider..." / "Beyond this direct effect, we further argue..." / "However, this relationship may not hold uniformly..." | 假设间逻辑递进 | 假设间无递进逻辑 |
| T4→T5 | "However, the [baseline effect] is likely contingent on..." / "Thus far we have assumed [condition]; yet..." | 从主效应过渡到边界条件 | T5 像是事后补丁 |
| T5→T6 / Closure | "Taken together, our theoretical framework suggests..." / "In sum, we have argued that..."（仅当存在独立或嵌入的框架总结时出现） | 从分散假设收束为整体框架 | 如假设间逻辑关系不自明且无框架总结，可能导致追问 |
| T5→METHODS | （无连接词，最后假设直接结束） | 管理学标准做法 | 无——这是正常结尾 |

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
# Fine-Grained Profile: [作者_年份_期刊]

## Paper Identity
- 构建类型: [来自 Phase 0]
- 期刊/领域: [journal]
- Theory 字数: [N]
- 段落数: [N]
- 假设数: [N]
- 与 write-theory 模板对齐度: [高/中/低]

## Rising Action 定位（Pollock Ch02，v1.2.0 新增）

**Central Knot 继承**: [true/false] — "[knot_inheritance_statement]"
**叙事弧线连续性**: [一致/增强/倒退] — 与 Introduction narrative_arc 的对比
**角色一致性**:
- 主角: [protagonist_construct]（Theory 中出现 [N] 次）
- 配角: [supporting_construct1], [supporting_construct2]
- 缺失角色: [如有，列出 Introduction 承诺但 Theory 未定义的构念]
**Plot Emergence**: [自然/有风险] — [extraneous_storyline_risk 或 null]

## Prose Craft Profile（Pollock Ch03，v1.2.0 新增）

**Human Face 策略**:
- P1 场景: "[具体场景句]"
- 构念 illustration: [构念名] → "[例子内容]"
- Why-chain 微型场景: [步骤] → "[场景句]"

**Showing vs Telling 策略**:
- Stroke/Glide 比例: [N:N]
- Illustration 类型分布: [案例/数字/场景/具体研究]
- Showing 断裂点: [如有]

**Conversational Voice 策略**:
- 主动语态频率: [N] 次
- 被动语态位置: [P[段号]: "[原句]"]
- T6 收束句式: "[closure_phrase]"

## 制度冲击特殊适配（v1.2.0 新增，如适用）

**设计类型**: [IV / DiD / RDD / 生存分析 / 无]
**三层论证覆盖**:
- 外生性: [✓/✗] — "[论证句]"
- 机制: [✓/✗] — "[论证句]"
- 识别基础: [✓/✗] — "[论证句]"
**识别策略理论嵌入**: [IV排除限制/DiD平行趋势/RDD可比性/生存时间维度] — [✓/✗]
**Theory-Methods 识别链接**: [无缝/脱节]

## Module Coverage (T1–T6)
[Phase 1.5 输出]

## Distilled Skeletons
### T1 — Construct Definition ([策略])
[来自 Phase 2.2 的骨架列表]

### T2 — Theoretical Lens ([理论])
...

## Argumentation Micro-Moves Map（v1.4.0 新增）

[来自 Phase 2.1.6]

### H1 / P4
- **Anchor**: [起点句]
- **Gap/Puzzle**: [缺口句]
- **Mechanism Move**: [机制步骤]
- **Warrant**: [文献/理论支撑]
- **Prediction**: [假设收敛]
- **缺失动作**: [如有]

### H2 / P5
...

### 双边论证
- **Moderator**: [W]
- **High condition**: [论证句]
- **Low condition**: [论证句]
- **对称性**: [完整/仅单边/缺失]

### 替代解释排除
- **已识别竞争解释**: [list]
- **排除策略**: [theoretical_inconsistency / scope_condition / empirical_counter / mechanism_incommensurable]
- **位置**: [P段号]

## Argument-Evidence Arrangement Pattern（v1.4.0 新增）

[来自 Phase 2.1.7]

- **主要模式**: [Warrant-Embedded / Warrant-First / Evidence-Contrast / Cumulative / Parallel]
- **辅助模式**: [如有]
- **证据**: [具体段落位置与句式]
- **功能等价性**: [true/false]

### Concrete Illustration 分布
- **密度**: [每个步骤后 1 句 / 每 2 步 1 句 / 稀疏]
- **类型分布**: [案例 / 数字 / 场景 / 比喻]
- **缺失位置**: [步骤2, 步骤3]

### 复杂假设段落组织
- **Pattern**: [common_trunk → dual_branch / baseline_first → moderation_second / mediation_chain]
- **H1 位置**: [P4]
- **H2 位置**: [P5]
- **假设间关系**: [sequential / parallel / nested]

## Evidence Map（v1.4.0 新增）

[来自 Phase 2.1.8]

### 证据类型分布
- Empirical finding: [N] ([%])
- Theoretical argument: [N] ([%])
- Boundary condition: [N] ([%])
- Negative evidence: [N] ([%])
- Analogical evidence: [N] ([%])

### 证据功能分布
- support: [N]
- qualify: [N]
- contrast: [N]
- pave: [N]
- rebut: [N]

### 文献引用三要素完整率
- 完整: [N/%]
- 缺失 concrete finding: [N/%]
- 缺失 argument summary: [N/%]
- 缺失 link to mechanism: [N/%]

### 代表性三要素例句
- "[Author] (year) found that [concrete finding] — [argument summary]. This suggests that [mechanism step], because [theoretical reason]."

## Theory DNA
[来自 Phase 3 的量化指标，已包含微观动作、双边论证、证据类型/功能、约束对齐等新指标]

## Theory Logic Map
[来自 Phase 2.3]

## write-theory Constraint Alignment（v1.4.0 新增）

| 约束 | 检查项 | 状态 | 说明 |
|------|--------|------|------|
| C10 交互模式 | 调节假设是否明确 enhancing/buffering/antagonistic/existence/competing | ✓/✗/N/A | |
| C14 竞争假设收敛 | 竞争假设是否使用非 "Therefore" 信号 | ✓/✗/N/A | |
| C16 辩证对立对称 | 对立机制步骤数是否对称 | ✓/✗/N/A | |
| C17 真正方向反转 | 是否方向反转而非仅强度变化 | ✓/✗/N/A | |
| C18 Moderator 选择框架 | ≥2 moderators 是否有元框架 | ✓/✗/N/A | |
| C19 连续 IV 三点 | high/middle/low 行为差异是否论证 | ✓/✗/N/A | |
| C20 双边论证 | 调节/边界条件是否同时论证 high/low | ✓/✗/N/A | |

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

**Prose Craft 子维度**（v1.2.0 新增）:
- **Human Face 策略**: [actor 类型分布 + 代表性例句]
- **Showing 策略**: [illustration 类型分布 + 代表性例句]
- **Voice 策略**: [主动句式模板 + 被动语态位置]
- **Stroke/Glide 控制**: [比例 + 风险段落标记]

## Non-Transferable Facts
[仅适用于该论文的特定构念、理论视角、机制内容，不可迁移]

## Corpus Recommendations（v1.4.0 新增）

基于本篇论文的提取结果，按 Corpus Taxonomy 分类给出沉淀建议。

```yaml
corpus_recommendations:
  ready_for_corpus:
    - pattern_id: "[唯一标识，如 parallel_three_mechanisms]"
      pattern_name: "[人类可读名称]"
      source_paper: "[作者_年份_期刊]"
      corpus_path: "corpus/subprotocols/arrangement_patterns.md"
      section: "[建议写入的章节]"
      build_type: "[适用构建类型]"
      confidence: "high / medium / low"
      cross_paper_evidence: "[已验证的范文数 / 需要再积累的范文数]"
      rationale: "[为什么这个模式值得沉淀]"
      entry_preview: |
        ### [Pattern Name]
        [可直接写入 corpus 的 markdown 条目预览]
  needs_validation:
    - pattern_id: "[唯一标识]"
      pattern_name: "[名称]"
      source_paper: "[作者_年份_期刊]"
      corpus_path: "[目标路径]"
      note: "[为什么还需要验证 / 需要找什么类型的论文验证]"
  anti_patterns:
    - pattern_id: "[唯一标识]"
      pattern_name: "[名称]"
      source_paper: "[作者_年份_期刊]"
      reason: "[为什么不建议沉淀到 write-theory]"
      alternative: "[如果要实现类似功能，建议用什么替代]"
```

**记录原则**：
- 单篇论文出现的新颖模式 → 优先放入 `needs_validation`
- 与 write-theory 当前 Constraints 冲突的做法 → 放入 `anti_patterns`
- 过于论文特异的机制内容 → 不进入任何 corpus，只在 Non-Transferable Facts 记录

## Corpus Reference Notes
[供人工审阅的语料库沉淀注释，不自动修改 write-theory skill]
```

---

## Corpus Taxonomy for write-theory（v1.4.0 新增）

本 skill 的终极目的不是产出报告，而是把验证过的模式沉淀到 `write-theory` 的语料库中。为避免沉淀时混乱，所有提取产物必须按以下 taxonomy 分类存放。

### 分类原则

1. **按功能粒度分层**：
   - `variants/`：整篇 Theory 的宏观结构（按构建类型）
   - `subprotocols/`：中观论证策略/模式（跨构建类型可复用）
   - `sentences/`：微观句式模板（填充式表达单元）

2. **按构建类型分桶**：
   - 同一模式若只在某构建类型中出现 → 写入该构建类型的 variant
   - 同一模式跨多个构建类型出现 → 写入 `subprotocols/` 并标注 `[跨类型]`

3. **按证据强度准入**：
   - 单篇论文出现 → 只入 Vault 参考注释
   - 2 篇同类型论文出现 → `subprotocols/` 作为可选变体
   - ≥3 篇跨期刊论文出现 → 可进入 `variants/` 或 `SKILL.md` 默认规则

### Taxonomy 映射表

| 提取产物 | 沉淀位置 | 文件名/路径 | 准入门槛 |
|---------|---------|------------|---------|
| 构建类型整体结构（T1–T6 模块序列、比例、节奏） | `corpus/variants/` | `A_construct_differentiation.md`<br>`B_mechanism_elaboration.md`<br>`C_hypothesis_tree.md`<br>`D_process_theory.md`<br>`E_moderation.md`<br>`F_competing_hypotheses.md`<br>`G_dialectical_opposition.md` | ≥2 篇该构建类型论文一致 |
| 假设论证微观动作（Anchor/Gap/Mechanism/Warrant/Prediction） | `corpus/subprotocols/` | `argumentation_patterns.md` | ≥2 篇论文出现同类动作序列 |
| **假设推导段落级模板（完整 Anchor→Mechanism→Warrant→Prediction）** | `corpus/subprotocols/` | `hypothesis_derivation_patterns.md` | ≥2 篇论文出现同类段落结构 |
| 论点-论据安排模式（Warrant-Embedded / Evidence-Contrast / Cumulative / Parallel） | `corpus/subprotocols/` | `arrangement_patterns.md` | ≥2 篇论文使用同模式 |
| 复杂假设段落组织（common trunk / dual branch / baseline→moderation） | `corpus/subprotocols/` | `hypothesis_organization_patterns.md` | ≥2 篇复杂假设论文一致 |
| 证据类型、证据功能、文献三要素句式 | `corpus/subprotocols/` | `evidence_patterns.md` | ≥2 篇论文出现同类证据策略 |
| 双边论证 high/low 句法 | `corpus/subprotocols/` | `bilateral_argumentation_templates.md` | ≥2 篇调节效应型论文一致 |
| Moderator 选择元框架 | `corpus/subprotocols/` | `moderator_selection_frameworks.md` | ≥2 篇多 moderator 论文一致 |
| Closure 策略（局部收束 / 嵌入框架总结 / Discussion 回补） | `corpus/subprotocols/` | `closure_strategies.md` | ≥3 篇管理学顶刊论文一致 |
| 识别策略理论嵌入（IV/DiD/RDD/生存分析） | `corpus/subprotocols/` | `identification_strategy_in_theory.md` | ≥2 篇制度冲击类论文一致 |
| 构念定义句式 | `corpus/sentences/` | `construct_definition.md` | ≥3 篇论文使用同类句式 |
| 理论视角引入句式 | `corpus/sentences/` | `theoretical_lens.md` | ≥3 篇论文使用同类句式 |
| 机制推演句式 | `corpus/sentences/` | `mechanism_chain.md` | ≥3 篇论文使用同类句式 |
| 调节假设句式 | `corpus/sentences/` | `moderation.md` | ≥3 篇论文使用同类句式 |
| 假设形式句式 | `corpus/sentences/` | `hypothesis_forms.md` | ≥3 篇论文使用同类句式 |
| 收束/过渡连接词句式 | `corpus/sentences/` | `closure.md`<br>`connectors.md` | ≥3 篇论文使用同类连接词 |

### 单篇蒸馏时的快速分类决策

对每个提取出的骨架/模式，按以下问题链决定去向：

```text
Q1: 该模式是否只适用于特定构建类型？
    ├── 是 → 进入 corpus/variants/[build_type].md
    └── 否 → Q2

Q2: 该模式是否涉及具体措辞/句法结构？
    ├── 是 → 进入 corpus/sentences/[function].md
    └── 否 → Q3

Q3: 该模式是否跨构建类型可复用？
    ├── 是 → 进入 corpus/subprotocols/[pattern_type].md
    └── 否/不确定 → 只入 Vault 参考注释
```

### Corpus Entry 标准格式

每个写入 corpus 的条目必须包含以下字段：

```markdown
<!-- 
pattern_id: [唯一标识]
build_type: [适用构建类型 / 跨类型]
source_papers: ["作者_年份_期刊", "作者_年份_期刊"]
confidence: [high / medium / low]
-->

### [Pattern Name]

**适用场景**: [一句话说明在什么情况下使用]
**排列模式**: [Warrant-Embedded / Parallel / 等]
**范文来源**: [论文引用]

**骨架**:
```
[可填充的句法结构]
```

**为什么有效**: [该模式的说服逻辑]
**注意事项**: [使用该模式时的风险和边界]
**反模式**: [什么情况下不该用]
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

当 Phase 2–4 的蒸馏产出满足以下全部条件时，在报告末尾生成回写提醒，建议用户将新发现的模式手动沉淀到 `write-theory` 的模块库：

### 触发条件

1. **骨架通过生成力验证**（Phase 2.4 裁决为"通过"）
2. **跨论文复现 ≥ 2 篇**（或批量模式下同一构建类型内 ≥ 2 篇）
3. **构建类型明确**（非 "ambiguous between X and Y"）
4. **模块功能归属明确**（T1–T6 或 T6-Variant 之一，非 "unclassified"）
5. **与当前 write-theory v3.3.0 不冲突**——回写前必须对照 write-theory 当前版本的约束（如 T6 Closure 非强制、文献引用以交织式为默认等）

**不触发回写提醒的情况**：
- 仅 1 篇论文中出现的模式 → 留存为 Vault 参考注释，积累到 ≥3 篇后再提醒
- 构建类型模糊的论文 → 标记为 "pending_type_clarification"
- 骨架批评家裁决为"需修正/不纳入" → 不回写
- **与 write-theory 当前版本核心约束冲突** → 标记为 "pending_protocol_revision"，先更新 write-theory 或降级为"可选变体"，不回写为默认规则

### 回写分类：默认规则 vs 可选变体

| 类型 | 判断标准 | 回写位置 |
|------|---------|---------|
| **默认规则** | ≥3 篇跨期刊论文一致，且与 write-theory 当前约束兼容 | 更新 `SKILL.md` Constraints / Phase 默认结构 |
| **可选变体** | 2-3 篇论文一致但存在期刊/类型特异性，或与当前约束不完全兼容 | 写入 `corpus/variants/` 或 `corpus/subprotocols/` 作为变体 |
| **待审阅** | 仅 1 篇出现，或样本有偏 | 只入 Vault 注释，不入 skill |
| **不采纳** | 与已验证的顶刊惯例明显冲突（如独立 T6 段落） | 不写入，仅记录为反模式 |

**回写前冲突检查清单**：
- [ ] T6 相关骨架：是否与 write-theory "不要求独立 Closure 段" 兼容？
- [ ] 文献引用节奏：是否支持"交织式"而非"分离式四段式"？
- [ ] 模块标签：是否允许无 "Theory and Hypotheses" 标题的主题标题进入？
- [ ] Institutional Background：是否作为可选前置模块而非 Theory 的一部分？
- [ ] Closure 信号：是否区分"假设段局部收束"与"全文独立 Closure 段"？

### 回写操作（手动 + 结构化预览）

满足条件后，蒸馏报告会在 `corpus_recommendations` 区块中为每个可沉淀模式生成一个**可直接 append 到 write-theory corpus 的 markdown 条目预览**。用户执行：

1. 对照报告中的 `pattern_id` 和 Vault 中已有条目，判断是否重复
2. 确认 `corpus_path`、`build_type`、`confidence` 标注正确
3. 复制 `entry_preview` 到对应 corpus 文件末尾
4. 更新 `write-theory` 的模块索引（如适用）

**生成的条目必须包含**：
- `pattern_id`（唯一标识）
- `build_type`（适用构建类型）
- `source_papers`（来源论文）
- `适用场景`（一句话说明）
- `骨架`（可填充的句法结构）
- `为什么有效`（说服逻辑）
- `注意事项`（边界和风险）
- `反模式`（不该用的情况）

**不自动执行写入**。模型只生成预览，最终写入由用户审核后完成。

**示例条目预览格式**（以 Shen_etal_2022_JOM 的 Parallel Moderation 为例）：

```markdown
<!-- 
pattern_id: parallel_moderation_from_three_mechanism_trunk
build_type: 机制推演型 + 调节效应型
source_papers: ["Shen_Zhou_Wang_Zhang_2022_JOM"]
confidence: medium
-->

### Parallel Moderation from a Three-Mechanism Trunk

**适用场景**: 主效应有多个并行的机制路径，需要用多个 moderators 分别检验每条路径的边界条件。
**排列模式**: Common Trunk → Parallel Branches
**范文来源**: Shen, Zhou, Wang, and Zhang (2022), *Journal of Operations Management*

**骨架**:
```
[Mechanism Trunk]
We argue that [IV] [direction] [DV] through three mechanisms: 
(1) [mechanism 1], (2) [mechanism 2], and (3) [mechanism 3].

[Branch for Moderator W1]
These effects, however, are contingent on [W1]. When [W1] is high, 
[mechanism 1]: ...; [mechanism 2]: ...; [mechanism 3]: ...
Therefore, H[X]: ...

[Branch for Moderator W2]
Similarly, [W2] alters the relationship because ...
[mechanism 1]: ...; [mechanism 2]: ...; [mechanism 3]: ...
Therefore, H[X+1]: ...
```

**为什么有效**: 读者先在 H1 理解完整的机制 trunk，之后每个 moderator 只需说明它如何改变 trunk 的每个分支，避免重复建立新机制。
**注意事项**: 
- 每个 branch 必须回到 trunk 的机制分别论证，不能只笼统说 "W moderates the relationship"
- 建议用元框架（如 environmental/organizational 或 supply/demand）组织多个 moderators
**反模式**: 如果 moderators 之间没有 conceptual 联系，不要强行 parallel，应改为假设树型逐个引入。
```

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
- 同一骨架被多个构建类型的论文使用（如局部收束信号 "Therefore, we hypothesize:"），标记为 `跨类型`，可跨桶回写
- 范式排他性骨架（如构念辨析型的 "differentiation dimensions"）**绝不**跨桶回写
- **注意**：write-theory v3.3.0 已取消"T6 Closure 作为独立模块"的强制要求。回写时，"Taken together, our theory posits..." 类骨架只能作为"嵌入最后假设段末尾的可选 2-3 句框架总结"标记，不能作为独立 T6 段落推荐。

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

#### 功能层 QC（原有）
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

#### T6 Closure QC（v1.2.0 新增，同步 write-theory v3.3.0）

> **注意**：write-theory v3.3.0 明确——管理学顶刊（JMS, AMJ, SMJ, ASQ, OS 等）**不要求独立的 T6 Closure 段落**。最后假设推导段的局部收束信号（"Therefore, we hypothesize:" / "Thus," / "Accordingly,"）已承担收敛功能。因此本 skill 的 T6 QC 从"是否存在独立 T6"改为"是否存在合适的收束策略"。

- [ ] **局部收束信号**：每个假设前是否有 Therefore/Thus/Accordingly 等收敛信号？
- [ ] **独立 T6 段落**：是否存在独立的 "Taken together..." 段落？→ 如存在，标记为"非管理学标准但可选"；如不存在，标记为"管理学标准做法"
- [ ] **框架整合位置**：如假设间逻辑关系不够自明，框架总结出现在哪里？（A）最后假设段末尾嵌入 2-3 句 /（B）Discussion 开篇 /（C）缺失，可能导致追问
- [ ] **T6 Voice**：如存在独立或嵌入的框架总结，是否使用 accountable first-person（"we have argued"），无被动语态？
- [ ] **T6 叙事接力**：如存在独立或嵌入的框架总结，结尾能量级是否 ≥ 最后假设推导段？
- [ ] **Discussion 回补**：如 Theory 无框架总结，Results/Discussion 是否有 "one expected—one unexpected" 等整合信号？

**记录格式**：
```yaml
t6_closure_qc:
  independent_t6_present: true/false
  standard_in_management: false  # 管理学默认：false 为正常
  local_convergence_signals: ["Therefore", "Thus", "Accordingly"]
  framework_integration_strategy: "embedded / discussion_opening / missing"
  voice_check_passed: true/false/null
  narrative_energy_maintained: true/false/null
  discussion_compensation: true/false/null
```

#### Prose Craft QC（v1.2.0 新增）
- [ ] **Human Face in Theory**: P1 有具体场景说明 knot 在现实世界的样子？
- [ ] **Construct Illustration**: 每个新构念首次出现配 1 个 concrete illustration？
- [ ] **Why-chain Scenes**: 关键步骤可配微型场景（1-2句）？
- [ ] **Stroke/Glide 比例**: 机制推演段落 70% stroke / 30% glide？
- [ ] **Conversational Voice**: P1 用 "To resolve the paradox..."; 假设推导用 "We argue that..."; T6 用 "In sum, we have argued that..."
- [ ] **无被动语态**: 无 "It is argued that..." / "It is hypothesized that..." / "The literature suggests that..."
- [ ] **无 Inflated Symbolism**: 无 "paradigm shift" / "fundamentally transforms"

#### 识别策略 QC（v1.2.0 新增，制度冲击类研究）
- [ ] **IV 研究**: Theory 是否论证了排除限制的理论基础？是否说明了工具变量通过什么理论渠道影响处理变量？
- [ ] **DiD 研究**: Theory 是否论证了平行趋势的理论基础？是否预判了处理效应异质性来源？
- [ ] **RDD 研究**: Theory 是否论证了断点可比性？是否说明了断点两侧制度差异的理论含义？
- [ ] **生存分析**: Theory 是否解释了时间维度的理论意义？是否论证了比例风险假设的理论合理性？
- [ ] **Theory-Methods 识别链接**: 如果 Methods 描述了识别策略但 Theory 完全未提及 → ⚠️ 标记

#### 论证、安排与证据 QC（v1.4.0 新增，对应 write-theory v3.3.0 核心诉求）

以下检查项用于**评估范文在假设论证、论点论据安排、证据摆放三个维度上是否符合 write-theory 的协议**，并提取其偏离方式。目的是帮你在沉淀语料库时判断：哪些范做法可直接复用，哪些需要标注为"例外"或"反模式"。

- [ ] **微观动作完整性**: 每个假设推导段落是否包含 Anchor → Gap/Puzzle → Mechanism Move → Warrant → Prediction 的完整序列？缺失哪个动作？
- [ ] **双边论证完整性**: 调节/边界条件段落是否同时论证 high-condition 和 low-condition 的机制？（write-theory C20）
- [ ] **替代解释排除**: 论文是否识别并主动排除主要 competing explanations？使用什么策略？
- [ ] **安排模式识别**: 论文主要使用 Warrant-Embedded / Warrant-First / Evidence-Contrast / Cumulative / Parallel 中的哪一种？是否功能等价？
- [ ] **Concrete Illustration 规则**: 是否存在连续 2 个推理步骤无 illustration 的情况？
- [ ] **证据类型健康度**: Empirical finding + theoretical argument 是否占证据总数的 ≥70%？是否存在 evidence type 与论点功能错配？
- [ ] **证据功能多样性**: 是否只有 support 型引用？qualify / contrast / pave / rebut 功能是否缺失？
- [ ] **文献引用三要素**: 每个引用是否同时满足 concrete finding + argument summary + link to current mechanism？
- [ ] **交互模式明确度**: 调节假设是否明确 enhancing / buffering / antagonistic / existence / competing？（write-theory C10）
- [ ] **竞争假设收敛信号**: 竞争假设是否避免使用 "Therefore" 等传统因果收敛信号？（write-theory C14）
- [ ] **辩证对立对称性**: 两个对立机制的步骤数是否对称？方向是否真正反转（而非仅强度变化）？（write-theory C16-C17）
- [ ] **Moderator 选择框架**: 当存在 ≥2 moderators 时，是否有元框架解释为什么选择这些 moderator？（write-theory C18）
- [ ] **连续 IV 三点论证**: 连续 IV 是否论证 high / middle / low 三点的行为差异？（write-theory C19）

**记录格式**：
```yaml
argumentation_qc:
  micro_move_completeness: "5/5"  # 或缺失动作列表
  bilateral_argumentation: {high: true, low: true, symmetry: "完整"}
  alternative_explanations: {identified: ["account1"], ruled_out: ["account1"], strategy: "scope_condition"}
  arrangement_pattern: "Warrant-Embedded + Cumulative"
  illustration_gap_count: 0
  evidence_type_health: {empirical: 0.5, theoretical: 0.3, boundary: 0.1, negative: 0.1, analogical: 0.0}
  evidence_function_diversity: {support: 5, qualify: 1, contrast: 1, pave: 1, rebut: 0}
  three_element_citation_rate: "85%"
  write_theory_constraint_alignment:
    C10_interaction_pattern: "明确 enhancing"
    C14_competing_hypothesis_signal: "通过"
    C16_dialectical_symmetry: "N/A"
    C17_true_direction_reversal: "N/A"
    C18_moderator_selection_framework: "通过"
    C19_continuous_IV_three_point: "N/A"
    C20_bilateral_argumentation: "通过"
```

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

蒸馏过程发现的原文理论叙事薄弱点不是要被"修复"（论文已发表），而是作为**模式采纳风险评估**记录。目的是帮你在把范文做法沉淀到 `write-theory` 语料库时判断：哪些做法是安全的默认规则？哪些应降级为"例外"或"反模式"？当你自己写作时，这些提示也能帮你避开已被验证的陷阱。

**格式**：

```markdown
# 模仿风险提示: [作者_年份_期刊]

| 发现阶段 | 风险类型 | 原文表现 | 模仿后果 | 建议处理 |
|----------|----------|----------|----------|----------|
| Phase 1.5 (Why-chain 压力测试) | Why-chain 跳跃 | 从 X→Y 缺少中间机制论证 | 模仿后审稿人质疑机制 | 补充自己的中间机制论证，不要模仿跳跃 |
| Phase 2 (T1 提炼) | 构念定义模糊 | "organizational capability" 未界定类型 | 模仿后审稿人问 "what kind of capability?" | 增加 scope condition 或具体化构念 |
| Phase 2.4 (骨架批评) | 机制内容污染 | 骨架中包含 "performative tension" 等具体机制 | 模仿后变成复制特定论文的机制 | 泛化为 [theoretical mechanism]，只模仿组织方式 |
| Phase 1.5 (对齐检查) | T4→Methods 断裂 | T4 提出三向交互但 Methods 未报告交互项 | 模仿后假设与操作化脱节 | 确保 Methods 中的变量操作化与 Theory 假设严格对齐 |
| Phase 1.5 (T6 检查) | 独立 T6 Closure 段落 | 论文有独立的 "Taken together..." 段落 | 非管理学标准，可能被审稿人视为冗余 | 如需框架总结，嵌入最后假设段末尾 2-3 句，或放到 Discussion 开篇 |
| Phase 1.5 (T6 检查) | 无局部收敛信号 | 假设前无 Therefore/Thus/Accordingly | 假设像从天而降，非从机制推导 | 每个假设前必须有因果连接词收敛 |
| Phase 1.5 (T6 检查) | 框架总结能量骤降 | 框架总结用 "In conclusion, we tested..." 纯方法总结 | 破坏 Rising Action 连续性，读者失去兴趣 | 如需框架总结，用 "In sum, we have argued that..." 保持理论能量 |
| Phase 0.75 (Prose QC) | 无人脸 Theory | T1 定义只有抽象描述，无 "A promotion-focused CEO, for example..." | 模仿后读者难以将抽象构念与经验世界连接 | 每个新构念首次出现配 1 个具体例子 |
| Phase 0.75 (Prose QC) | 机器声 Theory | 假设推导用 "It is hypothesized that..." | 模仿后像模板生成而非研究者判断 | 改用 "We hypothesize that..." |
| Phase 1.25 (制度冲击) | 识别策略与理论脱节 | Methods 详细描述 IV/DiD/RDD 但 Theory 完全未论证 | 模仿后审稿人质疑"为什么这个识别策略在理论上是合理的？" | Theory 中必须嵌入识别假设的理论论证 |
| Phase 2.5 (段落 QC) | Topic Sentence 埋藏核心判断 | 段首句用 "Drawing on institutional theory..." 无方向性预测 | 读者读完整段才知道论点 | 段首句必须在 15 词内说出核心判断：主语+主动动词+方向 |
| Phase 2.5 (段落 QC) | 无收敛信号 | 假设前无 Therefore/Thus/Accordingly | 假设像从天而降，非从机制推导 | 每个假设前必须有因果连接词收敛 |
| Phase 2.5 (段落 QC) | Citation 替代机制 | T3 只有 "Smith (2010) argues... Jones (2012) found..." | 模仿后变成文献综述而非理论推演 | 每个引用必须总结 argument 并链接到机制步骤 |
| Phase 2.6 (微观动作) | 论证动作缺失 | 假设段落直接从 "We argue" 开始，无 Anchor 或 Gap | 读者不知道为什么需要这个新假设 | 补充 Anchor（学界共识）和 Gap（现有解释不足） |
| Phase 2.6 (微观动作) | Warrant 薄弱 | Mechanism Move 后只有一句 "consistent with [theory]"，无具体文献 | 机制步骤像作者臆断 | 每个 mechanism move 后嵌入 1-2 个总结 argument 的 citation |
| Phase 2.6 (双边论证) | 只论证调节增强方向 | 段落只说 "when W is high, X→Y is stronger"，未解释 low-W 条件 | 审稿人质疑机制完整性 | 同时论证 high-W 和 low-W 条件下的理论逻辑 |
| Phase 2.6 (替代解释) | 未排除竞争解释 | 论文提出新机制但 ignore 明显 alternative account | 审稿人会提出 "what about..." | 主动识别 1-2 个主要 competing explanations 并用理论/范围条件排除 |
| Phase 2.7 (安排模式) | 连续两步无 illustration | 机制链连续两个步骤都只有抽象推理，无案例/数字/场景 | 读者难以把抽象机制与经验世界连接 | 每两个推理步骤间至少插入 1 句 concrete illustration |
| Phase 2.7 (复杂假设) | 假设间关系不明 | H1 和 H2 段落无逻辑连接词，像两个独立 mini-papers | 论文理论框架显得碎片化 | 用 "Building on H1..." / "Beyond this direct effect..." 等明确假设间关系 |
| Phase 2.8 (证据类型) | 证据类型单一 | 全部 citation 都是 empirical finding，无 theoretical argument | 论证缺乏理论根基 | 每个机制步骤同时嵌入 empirical finding 和 theoretical warrant |
| Phase 2.8 (证据功能) | 只有 support 型引用 | 所有 citation 都用来"支持"，无 qualify / contrast / rebut | 论证显得 one-sided，缺乏 nuance | 在关键步骤加入限定、对比或排除替代解释的引用 |
| Phase 2.8 (文献引用三要素) | Citation 无 concrete finding | "Smith (2010) argues that..." 只有抽象主张，无具体发现 | 引用无法支撑具体机制步骤 | 改写为 "Smith (2010) found that [具体发现] — [argument summary]" |
| Phase 2.8 / C10 | 交互模式不明确 | 调节假设只说 "W moderates X→Y"，未说明 enhancing/buffering/antagonistic | 读者无法判断理论预期 | 在机制和假设中明确交互模式类型 |
| Phase 2.8 / C18 | Moderator 选择无框架 | "We also examine the moderating role of Z" 无理由逐个引入 | 审稿人质疑为什么选这些 moderator | 用元框架（如 awareness vs capacity）解释 moderator 选择 |
| Phase 2.8 / C19 | 连续 IV 只论证一端 | "High X increases Y" 但未讨论 low/middle X 的行为 | 理论预测不完整 | 对称论证 high / middle / low 三点的行为差异 |
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

- **`write-theory`** — Phase 4 的更新建议可直接沉淀到 write-theory 的模块库和骨架库；Phase 2.5 连接词统计可反向更新 write-theory 的连接词分类库和段落收束模板。Phase 2.6–2.8 的微观动作、安排模式、证据类型/功能可直接沉淀为 `corpus/subprotocols/argumentation_patterns.md`，供 write-theory Phase 3（语料调用）调用。Phase 0.5 Rising Action 数据和 Phase 0.75 Prose Craft 数据可为 write-theory 的叙事对齐检查和 Prose Craft 定位提供输入
- **`theory-review`** — Phase 1.5 的模块覆盖检查和 Theory Logic Map 可作为 theory-review 的审查基准；Phase 1.25 的制度冲击适配检查可为理论审查提供识别策略论证依据；Phase 2.6–2.8 的微观动作、双边论证、证据三要素检查可为 theory-review 提供段落级论证审查清单
- **`paper-review`** — Theory Logic Map 可用于跨 section 对齐检查（Theory 承诺 vs Results 兑现）；Phase 4 的跨 Section 对齐表可直接用于 paper-review 的全稿对齐检查；write-theory Constraint Alignment 表可用于 Theory ↔ write-theory 协议一致性审查
- **`write-introduction`** — T2 Theoretical Lens 和 Closure 策略（局部收束 / 嵌入框架总结）的提炼可用于优化 Introduction 的 P5 Preview 和 P7 Contribution；Phase 0.5 的 knot 继承检查可为 Introduction→Theory 叙事接力提供验证；Phase 2.6 的 Anchor/Gap/Prediction 序列可为 Introduction 的 Gap→Preview 结构提供节奏参照
- **Vault** — Fine-Grained Profile 存入 Vault 的 `fine_grained/batch_*/[paper]_distilled_theory.md`；新发现的论证模式存入 `skill_update_recommendations/argumentation_patterns/`

## 外部资产位置

- **现有语料库索引**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/theory/mvp30/_mvp30_theory_index.md`
- **蒸馏产出存放**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/theory/mvp30/fine_grained/batch_*/[paper]_distilled_theory.md`
- **更新建议存放**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/theory/mvp30/skill_update_recommendations/`
## 输出结构参考

各 Phase 输出的结构化字段见各 Phase 正文中的 YAML/Markdown 表格。完整字段名和取值枚举已在 Phase 0–5 的示例输出块中逐一定义，无需单独维护 JSON Schema。

如需机器消费格式，参考 Vault 中已蒸馏的 `fine_grained/` 目录下的实际报告文件——其结构和字段集比抽象 schema 更准确地反映真实输出。

---
*基于 nuwa-skill 流水线框架、Pollock 2025 Ch02-Ch06、Dorobantu et al. (2024)、Shepherd & Wiklund (2020) 叙事规则、MVP30 范文语料库构建。版本 1.4.0 — Theory 蒸馏 Meta-Skill（同步 write-theory v3.3.0）。*
