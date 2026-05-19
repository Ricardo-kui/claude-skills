---
type: canonical_reference
canonical_id: "01-progressive-coherence"
status: ✓ STANDARD
gap_type: Incompleteness
cross_paper: VERIFIED
generativity: GENERATIVE
exclusivity: MEDIUM
source_papers:
  - eilert2017 (JM, 2017): "predominantly focused on X and Y. However, little attention to Z"
  - wu2025 (SMJ, 2025): "Authority quote pivot → remains poorly understood"
  - gamache2020 (SMJ, 2020): "Natural progression from general to specific"
  - mayo2021 (POM, 2021): "Cross-disciplinary literature review with Table"
created: 2026-05-19
source: Extracted from literature-turn-templates.md + MVP30 validation
---

# 01-progressive-coherence — Progressive Coherence 递进式文献对话

## 功能描述

P2-P3 的功能：承认文献已有实质进展，但精确指出被遗漏的维度/机制/时点/对象。核心逻辑是"已有文献做了 A 和 B，但遗漏了 C——不是因为他们错了，而是因为该领域自然发展到此时才出现 C 的问题。"

这是 **Incompleteness** Gap 最常用的 Conversation 策略。

## 适用场景

- Gap 类型 = **Incompleteness**（文献留下关系、机制、时点、对象或结果维度的空白）
- 需要解释为什么这个遗漏是重要的（不只是"没人做过"）
- 目标期刊接受递进式对话（JM, SMJ, AMJ, OS 均适用；ASQ 可能需要更强的理论缺口）

## 验证状态

### 跨论文复现
- **VERIFIED** (≥4 papers): eilert2017 (JM), wu2025 (SMJ), gamache2020 (SMJ), mayo2021 (POM)

### 生成力
- **GENERATIVE**: "Although research has... little attention has been paid to..." 模板高度可迁移

### 排他性
- **MEDIUM**: 几乎只在 Incompleteness 中出现

---

## 句法模板

### 变体 A：自然推进型（gamache2020 型）

**模板**:
> "Research in [field] has long recognized the importance of [phenomenon] and has often attempted to understand [outcome]. As part of this effort, recent research has drawn on [theory] to focus on [specific aspect] ([citations]). For example, research in this tradition has considered [specific examples of what IS known]."

**来源**: gamache2020 (SMJ), adapted

**关键特征**:
- "has long recognized" → 承认长期积累
- "As part of this effort" → 展示自然推进
- "For example" → 用具体研究支撑共识

---

### 变体 B：快速文献回顾型（eilert2017 型）

**模板**:
> "A substantial body of research has examined [reactive/post-hoc response to phenomenon]. [Author A] found that [finding]. [Author B] showed that [finding]. Most recently, [Author C] demonstrated [finding]. These studies collectively establish that [core consensus]. However, what remains unclear is [our focus]."

**来源**: eilert2017 (JM), adapted

**关键特征**:
- 用 3-4 句话快速建立文献共识
- "collectively establish that" → 确认已有进展
- "However, what remains unclear is" → 精确指出遗漏

---

### 变体 C：权威引语过渡型（wu2025 型）

**模板**:
> "Accordingly, a substantial body of research has examined [dominant focus]. [Authority], however, note that '[insightful observation that reframes focus]' (emphasis original). Yet, despite some noteworthy exceptions (e.g., [Exception A]; [Exception B]), [our focus] remains poorly understood."

**来源**: wu2025 (SMJ), P1-P2

**关键特征**:
- 用权威引语作为从"已有进展"到"仍有缺口"的转折支点
- "emphasis original" 显示对原文的精确引用
- "remains poorly understood" → 中等强度措辞

---

### 变体 D：跨学科引入型（mayo2021 型）

**模板**:
> "In fact, research outside of [target field] indicates that [actors] may manage risks related to [negative events] via at least two mechanisms: [mechanism 1] ([citations]) or [mechanism 2] ([citations]), and that the chosen risk management mechanism may depend on [key variable]. The contexts of these empirical studies are predominantly in [field A] ([citations]) and [field B] ([citations]); see Table [number]. These studies indicate that [condition 1], [actors] may [behavior 1] ([citations]), leading to [consequence A] ([citations]). [Condition 2], [actors] may [behavior 2] ([citations]), to avoid [consequence B]."

**来源**: mayo2021 (POM), P2

**关键特征**:
- "research outside of [target field] indicates" → 明确跨学科引入
- "via at least two mechanisms" → 预告二元机制
- "see Table [number]" → 用表格呈现文献回顾（POM/MSOM 风格）
- 条件分句清晰区分不同情境下的行为差异

**适用**: 将 finance/accounting/psychology 发现引入 OM 或战略管理的研究

---

### 变体 E：Table 1 文献矩阵型（darby2025 型）

**模板**:
> "A growing body of [domain] research offers insights into [phenomenon]. For example, [level_1_findings]. Recently, scholars have moved beyond [level_1] to examine [level_2], finding that [level_2_findings] ([citations]). This shift in focus is due, in part, to [external_change] ([citation]). Indeed, [reinforcement]."

同时嵌入 Table 1: 按 [DV 行] × [IV 类别列] 组织的文献矩阵，每格包含作者+年份+发现方向。

**来源**: darby2025 (JSCM), P2 + Table 1

**关键特征**:
- 叙事段落仅 3-4 句建立递进式文献线索
- Table 1 替代了原本需要 3-4 段的冗长文献叙述
- 矩阵按 IV 类别分列（召回特征 / 供应链因素 / 公司治理因素），按 DV 分行（召回次数 / 召回时滞）
- 每格仅 1-2 行：作者+年份+发现方向（+/-/ns）

**适用**: 文献 >=15 篇、需要在 Introduction 中展示文献广度的研究。文献 <10 篇时段落叙事足矣，无需矩阵。
**禁忌**: Table 1 不是完整文献综述的替代品——它是对文献模式的视觉摘要。正文仍需 2-3 句叙事建立逻辑线索。

---


## 组装规则

### 必须配对
- **与 `03-data-shock` (Hook) 配对**: 数据冲击建立 stakes，递进缺口将数据转化为学术问题
- **与 `10-practical-puzzle` (Hook) 配对**: 实践困境建立相关性，递进缺口精确到学术文献
- **与 `01-despite-progress-unaddressed` (Tension) 配对**: Progressive Coherence 是此 Tension 的标准 Conversation 策略

### 反模式提醒
- **不要把 Literature Turn 写成完整文献综述**: P2 是过渡，不是文献回顾。2-3 句即可
- **不要让 Hook 和 Literature Turn 脱节**: 必须在语义上连接
- **不要只引用自己导师的论文**: 展示文献广度

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| JM/JMR | ⭐⭐⭐⭐⭐ | 自然推进型最适配 |
| SMJ | ⭐⭐⭐⭐⭐ | 权威引语型适配 SMJ "冷静专业"风格 |
| AMJ | ⭐⭐⭐⭐⭐ | 需要解释为什么这个遗漏有理论重要性 |
| OS | ⭐⭐⭐⭐☆ | 偏好系统/结构性缺口论证 |
| ASQ | ⭐⭐☆☆☆ | ASQ 偏好更强的理论缺口（Inadequacy/Incommensurability） |

---

## 相关语料

- 配合 `hooks/03-data-shock.md` 使用：数据建立 stakes，递进缺口转化为学术问题
- 配合 `tensions/01-despite-progress-unaddressed.md` 使用：最常用的 Tension-Literature Turn 配对
- 配合 `transitions/01-hook-to-literature.md` 使用：Hook→Literature Turn→Gap 的标准链条