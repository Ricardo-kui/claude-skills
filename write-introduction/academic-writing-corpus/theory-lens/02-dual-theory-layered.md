---
type: canonical_theory_lens
canonical_id: "02-dual-theory-layered"
status: EMERGING
gap_type: Incompleteness
cross_paper: EMERGING
generativity: ADAPTABLE
exclusivity: HIGH
source_papers:
  - hoffmann_cheong_phan_zurbruegg2024 (JM, 2024): "Agency theory for main effect mechanism + business ethics framework for boundary conditions"
created: 2026-06-05
source: Distilled by distill-introduction-exemplar from Hoffmann et al. 2024 JM
---

# 02-dual-theory-layered — 双理论分层锚定 Theory Lens

## 功能描述

当研究同时涉及**主效应机制解释**和**边界条件推导**时，用两个互补理论分别承担不同论证功能。主理论（primary theory）解释"为什么 X 影响 Y"，次要框架（secondary organizing framework）为"X 的影响在什么条件下变化"提供分类系统。

核心逻辑：`[Primary theory] explains why [treatment] → [outcome]; [secondary framework] identifies conditions under which this effect varies.`

## 适用场景

- Gap 类型 = **Incompleteness** × **(Mechanism + Boundary)**
- 主效应的理论无法自然推导出边界条件（或推导出的边界条件不够系统化）
- 有两个或以上的调节变量，需要一个统一的分类框架来组织
- 次要框架不是竞争理论，而是 taxonomy/classification——它为"为什么选这些调节变量"提供理论理由

## 验证状态

### 跨论文复现
- **EMERGING** (1 paper): hoffmann_cheong_phan_zurbruegg2024 (JM)

### 生成力
- **ADAPTABLE**: 双理论结构可迁移到任何 Mechanism + Boundary 组合

### 排他性
- **HIGH**: 仅适用于 Incompleteness × (Mechanism + Boundary) 组合；单独的主效应或单独的边界条件研究不需要

---

## 句法模板

### 变体 A：代理理论 + 企业伦理框架型（hoffmann2024 型）

**模板**:
> In developing our conceptual framework and corresponding hypotheses on how [treatment] affects [outcome] and the boundary conditions of this effect, we rely on arguments from [primary theory] ([citation]) and [secondary framework/literature] ([citation]). Our point of departure is the observation that [baseline structural condition — e.g., separation of ownership and control]. This situation introduces the potential for [core mechanism], in which [agents] [behavior inconsistent with principals' interests], thus [violation of normative standard].

> Given the argument that [core mechanism] underlies [agents'] response to [treatment], our investigation of the boundary conditions of this main effect will be guided by insights from prior literature on [mitigating mechanisms]. The [secondary] literature distinguishes two main [mechanism types] to constrain [self-interest-seeking behavior] — [type 1: internal/intrinsic] and [type 2: external/extrinsic] ([citation]). This literature considers [type 1] as a means for [alignment logic] that operates by [mechanism]. [Type 2], in contrast, works by [monitoring/enforcement logic], which [mechanism]. A key distinction between these two solutions to [core problem] is thus that the former relies on [agents] intrinsically *wanting* to [do the right thing], while the latter is based on extrinsically *forcing* them to do so by means of [formal accountability mechanism]. Next, we discuss our expectations on how [type 1], in terms of [specific measure 1], and [type 2], in terms of [specific measure 2], will shift the main effect of [treatment] on [outcome].

**来源**: hoffmann_cheong_phan_zurbruegg2024 (JM), P4

**原文锚定**:
> "In developing our conceptual framework and corresponding hypotheses on how changes in managerial liability affect a firm's product recall decisions and the boundary conditions of this effect, we rely on arguments from agency theory (Jensen and Meckling 1976) and the business ethics literature (Husted 2007)." / "The business ethics literature distinguishes two main governance mechanisms to constrain the self-interest-seeking behavior of agents and reduce the occurrence of moral problems in organizations—corporate culture and normative control (Husted 2007)."

**关键特征**:
- **双理论的功能分工明确**: 主理论（agency theory）解释主效应机制 → 次要框架（business ethics）提供调节变量的分类系统
- **理论间通过 "Given the argument that..." 过渡句连接**: 明确标识两个理论之间的逻辑关系——次要理论不是在挑战主理论，而是在主理论的机制基础上识别约束条件
- **intrinsic vs extrinsic 区分框架**: 将两个调节变量分别归属为内部约束（culture → wanting to do right）和外部约束（monitoring → being forced to do right），创造概念上的对称配对
- **"A key distinction... is thus that the former relies on... while the latter is based on..."**: 明确区分两个约束机制的本质差异，增强理论优雅性
- **从框架到操作的映射**: 在引入分类框架后，立即将每个分类映射到具体可测量的构念

**适用**: Incompleteness × (Mechanism + Boundary) 组合。当主效应机制依赖代理冲突/激励问题（agency theory, tournament theory, incentive alignment frameworks），且边界条件需要一个组织治理/伦理/制度框架来系统化时。

**禁忌**: 
- 次要框架必须是真正的 organizing framework，不能只是一个方便的分类标签
- 两个理论之间必须是互补关系，不能是竞争关系
- intrisic vs extrinsic 的区分必须有理论依据，不能是事后合理化

---

## 组装规则

### 必须配对
- 主理论必须直接回应 Tension 中识别的主效应缺口
- 次要框架必须由主效应的机制类型自然导出（如 agent conflict → ethics/gov framework for constraint mechanisms）
- Theory Lens 中的理论承诺必须与后续 Theory Development 章节的实际理论使用一致

### 互斥
- **不能与单一理论的 Theory Lens 模板同用**: 本模板需要≥2个理论源
- 如果主效应和边界条件可以用同一理论解释 → 不需要双理论结构，用标准 Theory Lens 即可

### 反模式提醒
- **理论堆砌**: 如果两个理论的关系没有被清楚阐述（"why these two?"），审稿人会将之视为理论堆砌而非分层锚定
- **次要框架过于薄弱**: 如果次要框架只是一个 citation 而没有真正的概念内容，不要使用此模板
- **缺少过渡句**: 必须用 "Given the argument that..." 型过渡句说明两个理论的分工关系

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| JM | ⭐⭐⭐ 极高 | JM 接受 multi-theory framework 且偏好组织治理/伦理视角 |
| SMJ | ⭐⭐⭐ 高 | 双理论结构适合战略领域的 multi-level 研究 |
| AMJ | ⭐⭐ 中 | 需要确保两个理论各自都有充分的理论深度 |
| OS | ⭐⭐ 中 | 偏好"less is more"——确认两个理论确实都需要 |
| ASQ | ⭐ 低 | ASQ 偏好单一理论的深入发展，双理论可能被视为不够聚焦 |

---

## 槽位填充正误对比

### `[primary theory]` + `[secondary framework]` — 理论分工

❌ "We draw on agency theory and institutional theory." → 两个理论并列但未说明各自负责解释什么——读者不知道哪个解释 main effect，哪个解释 boundary conditions。

✅ "We rely on arguments from agency theory, which explains why managers face a trade-off between private incentives and shareholder interests, and the business ethics literature, which provides a taxonomy of organizational mechanisms—corporate culture and normative control—that can constrain self-interest-seeking behavior." → 主理论解释 trade-off（主效应机制），次要框架提供约束条件分类（边界条件）。

### `[transition between theories]` — 理论间过渡

❌ "Additionally, we draw on business ethics literature to examine moderators." → "Additionally" 暗示两个理论是并列的附加选择，而非有逻辑分工的整合框架。

✅ "Given the argument that agency conflicts between shareholders and managers underlie managers' opportunistic response to UD law adoption, our investigation of the boundary conditions of this main effect will be guided by insights from prior literature on organizational mechanisms that can mitigate such agency conflicts." → "Given that [main effect mechanism] underlies [behavior], our investigation of boundary conditions will be guided by [secondary framework]" —— 过渡句使两个理论的分工关系 explicit。
