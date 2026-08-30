---
type: canonical_tension
canonical_id: "03-structural-blindspot"
status: ✓ STANDARD
gap_type: Inadequacy
cross_paper: VERIFIED
generativity: GENERATIVE
exclusivity: HIGH
source_papers:
  - gamache2020 (SMJ, 2020): "most prior research considers [phenomenon] broadly... This structural tendency has limited our understanding"
  - shipilov2020 (SMJ, 2020): "existing research focuses on [dominant lens]... We propose to supplement with the network view"
  - shen2022 (JOM, 2022): "conventional wisdom" vs "dark side evidence" structural blindspot
created: 2026-05-18
source: Extracted from MVP30 narrative_analysis files
---

# 03-structural-blindspot — 结构性盲点 Tension

## 功能描述

Inadequacy 问题化的一个特定变体：不只是在某个具体假设上有问题，而是整个文献因为方法论惯例、理论传统或学科边界而系统性地忽略了一个视角。这种盲点是"结构性的"——它不是个别研究者的疏忽，而是整个研究范式的特征。与 `02-implicit-assumption-wrong` 的区别：本品强调盲点的系统性/结构性原因，而非特定假设的错误。

## 适用场景

- Gap 类型 = **Inadequacy**（文献系统性地忽略了某物）
- 盲点源于：学科边界（如财务学者不关注营销后果）、方法论惯例（如只用横截面数据）、理论传统（如只关注一个层次的效应）
- 需要连接多个文献流来展示盲点的结构性原因

## 验证状态

### 跨论文复现
- **VERIFIED** (≥3 papers): gamache2020 (SMJ), shipilov2020 (SMJ), shen2022 (JOM)

### 生成力
- **GENERATIVE**: 结构性盲点逻辑高度可迁移

### 排他性
- **HIGH**: 几乎只在 Inadequacy 中出现

---

## 句法模板

### 变体 A：笼统对待型（gamache2020 型）

**模板**:
> "While important, research on [topic] generally considers [phenomenon] broadly. This structural tendency to [lump/aggregate/treat uniformly] has limited our understanding of [specific variation]. Most prior research considers [broad category] collectively, overlooking how [specific types] may have [different antecedents/consequences/mechanisms]."

**来源**: gamache2020 (SMJ), P2-P3

**原文锚定**:
> "Most prior research investigating the role of CEOs considers all stakeholder strategies collectively, typically lumping governance-oriented strategies along with broader socially-oriented strategies (e.g., Tang et al., 2018), or, in some cases, excluding governance-oriented strategies altogether (e.g., Chin et al., 2013). This work neglects the fact that different stakeholder strategies may appeal to different CEOs."

**关键特征**:
- "structural tendency" → 明确指出这不是个别疏忽，而是系统模式
- "collectively" vs "specific types" → 笼统 vs 精细的对比
- 暗示修正这个盲点需要新的理论分类体系

---

### 变体 B：视角补充型（shipilov2020 型）

**模板**:
> "Existing research focuses on [dominant lens/perspective]. While this focus has yielded important insights, it has overlooked [complementary perspective]. We propose to supplement the focus on [dominant lens] with [new perspective]. Indeed, prior research has already shown that [new perspective mechanism] (e.g., [citation]). We propose that [new insight from combining perspectives]."

**来源**: shipilov2020 (SMJ), P3

**原文锚定**:
> "Second, we propose to supplement the focus on the firm's own media coverage with the network view. Indeed, prior research has already shown that network ties such as board interlocks are conduits through which practices and behaviors diffuse... We propose that the influences of positive or negative media coverage... might come not only from the firm's own (direct) coverage, but also be spillovers from its network partners' (indirect) media coverage."

**关键特征**:
- "supplement... with..." → 不是推翻已有视角，而是增加维度
- 承认已有网络研究的价值（不是稻草人）
- 区分 direct 和 indirect 效应

---

### 变体 C：常规智慧片面型（shen2022 型）

**模板**:
> "[Conventional wisdom/prevailing view] holds that [dominant claim]. However, [contrary evidence/dark side]. The conventional wisdom focuses on [one mechanism/one outcome], systematically overlooking [alternative mechanism/outcome]. This blindspot persists because [structural reason—e.g., data limitation, disciplinary boundary, theoretical tradition]."

**来源**: shen2022 (JOM), adapted

**关键特征**:
- "prevailing view" → 共识不是假的，是片面的
- "systematically overlooking" → 盲点是结构性的
- 解释为什么盲点持续存在（不只是"没人想到"）

---

## 组装规则

### 必须配对
- **与 `05-literature-consensus-blindspot` (Hook) 配对**: 文献共识暗示盲点存在，结构盲点 Tension 揭示盲点的系统性原因
- **必须引用具体文献证明盲点的结构性**: 不能只说"文献忽视了 X"，必须引具体论文展示模式

### 互斥
- **不能与 `01-despite-progress-unaddressed` (Tension) 同用**: 前者是 Incompleteness（"漏了"），本品是 Inadequacy（"系统性地漏了"）
- **不能与 Incompleteness Gap 同用**: 结构性盲点属于 Inadequacy 范畴

### 反模式提醒
- **不能让结构性原因听起来像借口**: "没人研究因为数据不可得"是弱论证；"没人研究因为理论传统指向了另一方向"是强论证
- **不要省略已有的例外研究**: 如果有少数研究突破了盲点，必须引用并说明为什么它们不足以改变范式
- **不要在 Gap 段提出完整的解决方案**: 结构性盲点的解决方案（新理论框架）应在后续 Theory 段展开

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| SMJ | ⭐⭐⭐ 极高 | 变体 A 和 B 是 SMJ 标志句式 |
| AMJ | ⭐⭐⭐ 高 | 偏好展示结构性盲点的多文献来源 |
| OS | ⭐⭐ 中 | 偏好系统/结构性论证 |
| ASQ | ⭐⭐ 中 | 偏好理论传统本身作为盲点来源 |
| JM/JMR | ⭐ 低 | 营销期刊偏好更直接的缺口论证 |
