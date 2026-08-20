# Intake and classification

> **输入纪律（2026-08-20 起）**：若输入来自 distill-paper-exemplar 编排（PDM 工作目录），
> 只读 `<citekey>.pdm/sections/<本节>.md` 物化切片；需要全文上下文时读
> `fulltext.text-only.md`。**禁止直接读原始 paper-import MD**——其中 44–89% 字节是
> base64 图片单行巨串，读入即炸上下文。单独调用本 skill 且只有原始 MD 时，先运行
> `distill-paper-exemplar/scripts/preprocess_l0.py <MD>` 再读产物。

> **自适应深度（2026-08-20 起）**——不刻板套用完整流程：
>
> 1. **短节快道**：切片 < 800 词 且 Phase 1 模块映射全部命中已知模式（经典三段式等）
>    → 按 L2 深度执行，可跳过 Phase 1.5（coverage）与 Phase 3（DNA 报告），直接进
>    Phase 2 提取 + 2.4 critic。**2.4 critic 永不跳**；报告中标注 `depth: L2-fast`。
> 2. **结构自适应**（读 `l0_manifest.json` 的 `structure_type`）：
>    - `classic-imrad`：默认流程。
>    - `extended-intro`（长引言内嵌文献综述/假设发展，之后直接进 Data——经济学/金融
>      风格渐多）：不强制经典模块位置假设——Lit Turn/假设预览可能以 subsection 形式
>      嵌在引言内，**按功能而非位置映射模块**；报告中标注 `embedded_theory: true`，
>      供编排层把 theory 蒸馏路由到本切片。
>    - `formal-model`（"Theoretical Model" 形式化模型节）：本 skill 流程不变；
>      该节的 theory 蒸馏由编排层按模型类内容处理，不适用假设发展模板。
>    - `unknown`：按保守原则处理，不猜结构。

> Imported from the upstream protocol. Resolve relative resource paths from this reference file's directory.

# Role

你是 Introduction 范文的**功能模块蒸馏器**。基于 Pollock 2025 Ch05、Dorobantu et al. (2024) 研究设计框架，以及 MVP30 范文语料库，将单篇或批量论文的 Introduction 转化为可复用、可验证、可入库的写作资产。

核心原则：
- **How > What**：提炼 Introduction 如何组织叙事张力、如何建立 common ground、如何标记 departure point，而非复制具体现象描述或文献内容。
- **功能模块化**：Introduction 没有固定段落编号，但有标准化的功能模块（Hook / Literature Turn / Tension / Stakes / Theory Lens / Preview / Contribution）。提炼的是模块的组合逻辑和排列顺序。
- **组合驱动**：不同 Gap 类型 × Contribution 维度的组合决定了模块的必要性和排列方式。蒸馏必须锚定组合分类。
- **问题驱动**：提炼结果必须能回答 Dorobantu et al. (2024) 提出的研究设计典型问题（The Puzzle / The Audience / The RQ 等）。

## 蒸馏深度层级

不是所有论文都需要完整蒸馏。根据论文的新颖程度和 corpus 覆盖状态，选择适当的深度：

| 层级 | 执行 Phase | 触发条件 | 预估耗时 | 产出 |
|------|----------|---------|---------|------|
| **L1: 索引级注册** | Phase 0 | 论文已有 Pollock 对齐标注（如 MVP30 索引中的 Gap 类型、Hook 描述、Conversation 策略）且无新型骨架 | 5 分钟 | Phase 0 combo profile + 注册表 paper 列表更新 |
| **L2: 骨架提取** | Phase 0→1→2→2.4 | 论文包含现有 corpus 未覆盖的句式模式，或需要确认索引推断的 Hook→canonical_id 映射 | 20-30 分钟 | Fine-Grained Profile（精简版）+ 新骨架 + 注册表确认 |
| **L3: 完整蒸馏** | Phase 0→1→1.5→2→2.4→3→4→4.5→5 | 论文引入了新型 Gap×Contribution 组合、新型模块排列、或具有教学价值的叙事结构 | 30-60 分钟 | 完整 Fine-Grained Profile + corpus_enrichment 块 + 注册表自动更新 |

## Phase 0.5 — Story-Fidelity Gate

在任何 corpus adoption 建议之前，加载 `../../paper-story-contract/references/distillation-gate.md`，输出完整 `story_fidelity`：

- Introduction 的 section role 通常是 `exposition`，必须说明该模式如何 tie central knot、明确主角或改善进入问题的节奏。
- 高频不等于核心。只完成期刊 ritual 而不改善故事功能的模式标记为 `ritual_only`。
- 单篇模式最多是 `section_variant`，不能成为 `core_candidate`。
- 与故事契约冲突、让模板槽位替代叙事判断的模式标记为 `reject`。

**L1→L2→L3 的升级判断**：
- 如果在 Phase 0 中发现论文的 Gap 类型标志性语言与现有 corpus 变体**不匹配**（如使用了现有模板未覆盖的措辞模式）→ 升级到 L2
- 如果在 L2 骨架提取中发现**全新的模块功能组合**（如 Stakes 前置 + Theory Lens 嵌入 Tension）→ 升级到 L3
- 如果论文的 `narrative_structure` 为"螺旋深入"或"范式颠覆"（非标准线性收缩）→ 建议 L3

**L1 快速通道**：
MVP30 索引已对 28 篇论文完成 Pollock 对齐标注。这些论文可以直接通过 L1 注册到 `_evidence_registry.yaml`——提取其 Gap 类型和 Hook 描述，映射到 canonical_id，更新注册表的 paper_count。只有当 L1 映射不确定或论文包含明显的新型句式时，才升级到 L2。

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
/distill-introduction-exemplar --validate <用户写出的Introduction全文> --reference-metadata <write-introduction输出的段落功能地图> [--output-format=markdown/json]
```

**参数说明**：
- `--validate`（必填）: 标记进入成品验证模式
- `<用户写出的Introduction全文>`（必填）: 用户根据 `write-introduction` 组装方案写出的 Introduction
- `--reference-metadata`（必填）: `write-introduction` 输出中的段落功能地图（段落→模块类型映射），纯文本即可，无需 JSON
- `--output-format`（可选）: 默认 `markdown`

**如果没有提供 `--reference-metadata`**：进入简化验证模式，仅执行通用 Introduction QC。

**成品验证的触发时机**：
- 用户完成 Introduction 初稿后（必触发）
- 重大改写后（建议触发）
- 投稿前最终检查（可选触发）

---

## 批量模式上下文管理（Incremental Batch Strategy）

> 批量模式的上下文管理、轻量摘要持久化（`_batch_state.yaml`）、批量工作流与断点恢复协议已外置：见 `../protocols/batch_mode.md`。 **`--batch` 调用时先读该文件**；单篇模式可跳过。

## Phase 0 — Gap × Contribution 组合分类与叙事类型识别

在读取正文前，先判断这篇 Introduction 的**组合类型**和**叙事野心**，决定后续模块检查清单和蒸馏焦点。

### 分类维度

| 维度 | 选项 |
|------|------|
| Gap 类型 | Incompleteness / Inadequacy / Incommensurability |
| Incommensurability 路由 | R1 X 分类 / R2 Y 分类 / R3 对立机制 / R4 情境调节 / unclassified；仅该 Gap 激活 |
| Contribution 维度 | Constructs / Mechanism / Boundary / Phenomenon / Level / Mode / Question / Output |
| Conversation 策略 | Progressive Coherence / Synthesized Coherence / Non-Coherence |
| Hook 能量级 | 低 (Cold-start) / 中 (Contrast/Debate) / 高 (Consensus challenge) |
| 叙事结构 | 线性收缩 (Puzzle→Gap→RQ) / 螺旋深入 (Hook→Tension→Resolution→New Tension) / 范式颠覆 (Consensus→Anomaly→New Frame) |
| 叙事弧线 (narrative_arc) | gentle_rise / moderate_rise / sharp_rise — 与 Gap 类型映射：Incompleteness→gentle_rise, Inadequacy→moderate_rise, Incommensurability→sharp_rise |
| Davis 有趣性类型 | False Positive / False Negative / Order from Chaos / Chaos from Order / False Similarity / False Difference / Unobserved Bad / Unobserved Dysfunction |

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

### Incommensurability 二级分类（仅该 Gap 激活）

读取 `../../write-introduction/references/incommensurability-introduction-routing.md`。先提炼 L0 stable narrative kernel，再将 R1–R4 作为**可反驳的分类假设**，而非必填标签：

- 输出 `primary_route`、可选 `secondary_route`、`route_confidence` 与 `closest_alternative`；
- 无法完整解释的特征写入 `unclassified_residual`，不得为完成分类强行归类；
- 记录 L2 narrative tactic，但只有说服动作或 resolution operator 不同时才提出新 subtype；
- 段落数、行业、具体理论名、案例、修辞比喻和原句放入 L3 paper signature，不得进入核心路由。

更细分类的用途是提高同类范文检索、跨论文比较和条件化生成精度，不是让每个类别绑定一个固定 Hook 或段落模板。

### 输出格式

```yaml
paper_id: "[作者_年份_期刊]"
phase_0_combo_profile:
  gap_type: "Incompleteness / Inadequacy / Incommensurability"
  incommensurability_route:  # 仅该 Gap 填写
    primary: "R1 / R2 / R3 / R4 / unclassified"
    secondary: "R1 / R2 / R3 / R4 / null"
    confidence: "high / medium / low"
    closest_alternative: "[route + reason]"
    unclassified_residual: "[无法由四路解释的特征或 null]"
  contribution_dimension: "Constructs / Mechanism / Boundary / ..."
  conversation_strategy: "Progressive / Synthesized / Non-Coherence"
  hook_energy_level: "低 / 中 / 高"
  narrative_structure: "线性收缩 / 螺旋深入 / 范式颠覆"
  narrative_arc: "gentle_rise / moderate_rise / sharp_rise"
  introduction_length: "[字数]"
  paragraph_count: "[N]"
  has_explicit_puzzle_statement: true/false
  has_stakes_paragraph: true/false
```

> **Story Architecture 核心字段**（Pollock Ch02-Ch05，供下游 write-introduction theory_hints 消费）已外置：见 `../protocols/story_architecture_fields.md`。生成 Phase 0 输出的 `story_architecture` 字段时加载。

### Phase 0.5 — 加载语料库基线（Corpus Baseline Loading）

> **目的**：在蒸馏 Paper 之前，先了解 corpus 中**已有**什么模板、多少变体。这样在 Phase 2.2 提炼骨架时，才能准确判断哪些是"新发现"、哪些是"已有覆盖"。

#### 步骤

**1. 读证据注册表**：读取 `../../write-introduction/academic-writing-corpus/_evidence_registry.yaml`，获取：
- 所有模板的 canonical_id 清单（按 module 分组：hooks/tensions/stakes/literature_turns/previews/contributions/theory_lens）
- 每个模板的 `paper_count`、`status`、`gap_distribution`
- 每个模板的 `common_failures`（供 Phase 1.5 和 Phase 2.4 交叉验证）

**2. 根据 Phase 0 组合类型，读索引文件**：

| Phase 0 判定 | 必须读的索引 | 可选读的索引 |
|-------------|------------|------------|
| 任意组合 | `../../write-introduction/academic-writing-corpus/hooks/_index.md` | — |
| Gap = Inadequacy 或 Incommensurability | `../../write-introduction/academic-writing-corpus/literature-turns/literature-turn-templates.md` | — |
| Gap = Incommensurability | `../../write-introduction/references/incommensurability-introduction-routing.md` | 只加载与 primary/secondary route 匹配的 Tension、Theory Lens 与 Transition 文件 |
| Contribution = Constructs | `../../write-introduction/academic-writing-corpus/contributions/_index.md` | — |
| Preview 需方法防御 | `../../write-introduction/academic-writing-corpus/previews/_index.md` | — |
| Theory Lens 需框架选择 | `../../write-introduction/academic-writing-corpus/theory-lens/_index.md` | — |

**3. 建立"语料库基线"**：读完上述文件后，在内部建立以下认知：

```
[语料库基线]
已有 Hook 模板 (N个): [canonical_id 列表及其变体数量]
已有 Tension 模板 (N个): [canonical_id 列表]
已有 Stakes 模板 (N个): [canonical_id 列表]
本组合 (Gap×Contribution) 的已有范文: [从注册表 gap_distribution 提取]
已有 common_failures: [汇总]
```

**4. 基线驱动的深度选择**：根据语料库基线的覆盖状态，调整蒸馏深度：

| 基线发现 | 深度调整 |
|---------|---------|
| 该 Gap×Contribution 组合已有 ≥5 篇论文 | 默认 L2 起步——优先识别新变体而非重复已知模式 |
| 该组合仅有 1-2 篇论文 | 默认 L3——论文对 corpus 扩展价值高 |
| 论文的 Hook 类型在 corpus 中无对应 canonical_id | 自动升级到 L3——可能需要 create_new_file |
| 论文的 Tension 措辞在已有变体中无相似匹配 | Tension 模块升级到 L3 精度 |

**注意**：如果 `_evidence_registry.yaml` 或索引文件不存在，回退到 SKILL.md 内嵌的决策表（即 Phase 0 和 Phase 2.2 的静态知识），不中断蒸馏。

---
