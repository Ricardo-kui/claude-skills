---
type: canonical_tension
canonical_id: "17-puzzle-contrast"
status: ⚠ EMERGING
gap_type: Incompleteness (主) + Inadequacy (辅)
cross_paper: EMERGING
generativity: GENERATIVE
exclusivity: MEDIUM
source_papers:
  - singh_grewal2023 (JMR, 2023): "Objective product quality should be the only determinant... Yet anecdotal evidence suggests otherwise."
created: 2026-05-24
updated: 2026-05-24
source: Extracted from Singh_Grewal_2023_JMR distill-introduction-exemplar
---

# 17-puzzle-contrast — Puzzle 对比型张力

## 功能定义

不依赖标准文献缺口语言（"few studies" / "remains unclear" / "overlooks"），而是通过**理论预测 vs 现象证据的认知冲突**建立 puzzle：标准理论预测 X 不应该影响 Y（因为 X 不改变 Y 的底层机制），但轶事/现象证据显示 X 可能确实影响 Y。

这种张力依赖的是读者对"事情不应该这样"的直觉反应，而非对"文献有缺口"的学术认知。

## 适用场景

- 核心 IV 在理论上不应影响 DV（如 lobbying 不改变产品质量 → 不应影响召回）
- 但有轶事/政策/制度证据暗示相反
- 目标期刊接受 puzzle-driven 叙事（JMR、JM、SMJ）
- Introduction 内无完整 Literature Turn（文献推迟到后续 Section）

---

## 句法模板

### 变体 A：理论零假设 vs 现象矛盾型（singh_grewal2023 型）

**模板**:
> "The answers to these questions are not obvious. [Standard theory/perspective] suggests that [IV] should have [null/zero] impact on [DV], because [IV] does not alter [underlying mechanism]. Yet anecdotal evidence suggests otherwise. Uncovering a relationship between [IV] and [DV] thus can offer critical [domain 1] and [domain 2] insights."

**来源**: singh_grewal2023 (JMR), P2

**原文锚定**:
> "The answers to these questions are not obvious. Objective product quality should be the only determinant of product recalls, and lobbying should have no impact, because it does not alter product quality. Yet anecdotal evidence suggests otherwise. Uncovering a relationship between lobbying and product recalls thus can offer critical strategic marketing and public policy insights."

**关键特征**:
- **"not obvious"** — 非标准 Gap 开场词，建立 puzzle 而非 gap
- **"should be... should have no impact"** — 从标准理论推导零假设
- **"because it does not alter [mechanism]"** — 简洁的逻辑链条，不依赖文献回顾
- **"Yet anecdotal evidence suggests otherwise"** — 单一转折句建立张力，不需要系统文献综述
- 张力建立后直接收敛到 stakes（"critical... insights"）— 无独立的 Stakes 段落
- 能量等级：中 — 不攻击文献，只挑战直觉

**与标准 Incompleteness 的区别**:
- 经典 Incompleteness: "Although prior research has extensively examined [X], the role of [Z] remains unclear." → 依赖文献对话
- Puzzle 对比型: "X should not affect Y... Yet it seems to." → 依赖认知冲突
- Puzzle 对比型不需要提前展示文献——轶事证据足以建立 tension

**与标准 Inadequacy 的区别**:
- 经典 Inadequacy: "Prior research has treated X as [assumption], overlooking [alternative]." → 直接批评文献
- Puzzle 对比型: 不批评文献（甚至可以承认标准理论在正常情况下是对的），只指出现象层面存在矛盾

---

## 组装规则

### 必须配对
- **与 `10-immersive-narrative` (Hook) 配对**: Policy anecdote 或制度报告建立轶事证据的可信度
- **与量化 Stakes 配对**: Puzzle 建立后必须立即量化 "so what"（如行业规模、召回成本）
- **必须有后续理论支撑**: Introduction 中的 puzzle 暗示必须在 Theory 部分兑现（如 legitimacy perspective 解释为什么 lobbying 实际影响 recalls）

### 互斥规则
- **不与标准 Incompleteness 共存**: 不要同时使用 "remains unclear" 和 "should be... Yet..."——两种语言暗示不同的 Gap 建立策略
- **不与完整 Literature Turn 配对**: 如果在 Introduction 中已建立了完整文献对话，使用标准 Incompleteness/Inadequacy 模板更合适

### 反模式提醒
- **"anecdotal evidence" 不能空洞**: 必须有具体、可引用、制度性来源的轶事证据（Congressional report, internal documents, news reports）——不能只是 "some say..."
- **标准理论预测必须有理论名称**: "Objective product quality should be the only determinant" 背后是 efficiency perspective——应具名但可在 Introduction 中省略理论名称（推迟到 Theory）
- **不能只有 puzzle 没有 stake**: "Yet anecdotal evidence suggests otherwise" 后必须立即解释 why this matters
- **不是所有 "surprising finding" 都适合**: 该模板适用于理论预测 vs 现象的 puzzle，不适用于假设检验中发现的反直觉结果（后者应在 Discussion 处理）

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| JMR | ⭐⭐⭐⭐⭐ | 接受 puzzle-driven + 制度证据的叙事风格 |
| JM | ⭐⭐⭐⭐☆ | 适合政策/消费者保护主题 |
| SMJ | ⭐⭐⭐☆☆ | 可用，但通常需要更明确的文献定位 |
| ASQ | ⭐⭐⭐☆☆ | 偏好更完整的文献对话；puzzle 需要更深的理论根源 |
| OS | ⭐⭐⭐☆☆ | 适合但通常与理论 gap 混合使用 |

---

## 相关语料

- 配合 `hooks/10-immersive-narrative.md` 变体 C（Policy Anecdote + Table）使用
- 不要与 `tensions/01-despite-progress-unaddressed.md` 混合使用（Incompleteness 策略冲突）
- 与 `tensions/15-practical-puzzle.md` 的区分：15 是实践传统智慧 vs 新 downside；16 是理论零预测 vs 现象矛盾
