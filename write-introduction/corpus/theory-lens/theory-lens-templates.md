---
type: canonical_theory_lens
canonical_id: "theory-lens-templates"
status: EMERGING
gap_type: all
cross_paper: EMERGING
generativity: GENERATIVE
exclusivity: MEDIUM
source_papers:
  - ridge_hill_ingram_kolomeitsev_worrell2024 (AMJ, 2024): "Trait-activation dynamic lens — stable disposition + situation-activated within-person switch (avoidance→aggression)"
created: 2026-08-12
updated: 2026-08-12
source: Distilled by distill-introduction-exemplar Phase 4.6
---

# Theory Lens — 跨框架句法模板

## 功能描述

Theory Lens（P4-P5）的功能：在 Gap/Tension 建立之后，向读者提供**新的解释框架**——告诉他们"我们可以用什么透镜来看这个问题"。这不是理论综述，而是**理论承诺**："Drawing on X, we argue that..."。

本文件是 theory-lens 模块的**跨框架句法模板集**：各具体理论框架的专题文件（agency theory、maxim contrast、context bridging、socio-cognitive frame、dual-theory layered 等）见 `theory-lens/_index.md` 文件清单；本文件沉淀的是**不绑定单一理论名、可迁移到多个框架**的句法模式。ridge2024 提供的 trait-activation 动态透镜是第一个被沉淀的跨框架模板。

## 适用场景

- Theory Lens 必须直接回应 Tension 提出的 gap（关键词重叠）
- Theory Lens 必须与 Preview 中的研究设计一致
- Theory Lens 必须与 Theory Development 章节的实际理论来源一致

## 验证状态

### 跨论文复现
- **EMERGING** (1 paper): ridge_hill_ingram_kolomeitsev_worrell2024 (AMJ)

### 生成力
- **GENERATIVE**: 稳定倾向 + 情境偶发 cue → 个体内行为偏移的两段式透镜，可迁移到任何 disposition × situation-activation 设计（trait activation、personality systems）

### 排他性
- **MEDIUM**: 主要服务 Incompleteness × Mechanism（动态/时间机制）；不适用于无时间动态、无 cue 操作化的静态主效应设计

---

## 句法模板

### 变体 A：特质激活动态透镜型（ridge2024 型）

**模板**:
> "We address the foregoing issues by developing a more nuanced theory of (a) how [focal construct] affects specific approaches to [outcome] and (b) what might prompt a change in approach by [actors]. To do so, we build from [framework theory] to derive a foundational logic of why a focal [actor] characteristic such as [construct] affects how that [actor] engages [targets]. We then integrate [N] salient aspects of [construct]. First, [baseline mechanism: construct property → safety behavior → target behavior]. Second, drawing on theorizing about [activation of construct], which builds on trait activation and related personality theories, we argue that [trait-relevant cues] affect how those with elevated levels of [construct] engage [targets]. Specifically, when cues indicate that [baseline behavior] has not offered protection from external entities, individuals higher in the trait tend to shift away from [baseline] to directly engage [targets]."

**来源**: ridge_hill_ingram_kolomeitsev_worrell2024 (AMJ), P4-P6

**原文锚定**:
> "we argue that paranoia-relevant cues affect how those with elevated levels of paranoia engage stakeholders. Specifically, when cues indicate that avoidance has not offered protection from external entities, individuals higher in the trait tend to shift away from avoidance to directly engage the external entities."

**关键特征**:
- **两段式透镜架构**: 先由宿主框架理论（upper echelons）建立基线逻辑（disposition → safety behavior → 对目标的行为），再引入 trait activation 的"情境开关"——开关才是新颖性所在
- **解决时间动态缺口**: 一个稳定倾向 + 情境偶发 cue → 个体内行为偏移（avoidance→aggression）——把"为什么策略/行为随时间变化"理论化，直接兑现 temporal-dynamics 贡献
- **命名安全行为连续谱的两极**: avoidance 与 aggression 是同一安全行为谱系的对立极，给理论一个干净的内部对照
- **与既有 theory-lens 变体的区别**: `05-maxim-contrast` 只是用格言具象化 trade-off，未提供个体内激活开关；本变体是 theory-lens 模块中第一个建模 within-person activation switch 的模板

**适用**: strategic-leadership / upper-echelons 论文，理论化"特质效应如何随外部事件（监管裁决、对手攻击、危机）随时间变化"；Incompleteness × Mechanism（动态）

**禁忌**: 激活开关必须有具体 cue 操作化（否则读作 situationism 空谈）；不要承诺 Methods 观察不到的动态——若实证设计无法观测 cue 触发前后的个体内变化，改用静态主效应透镜

---

## 组装规则

### 必须配对
- Theory Lens 必须直接回应 Tension 提出的 gap（关键词重叠）——本变体常与 `01-despite-progress-unaddressed` 变体 AG（trait-valence 不对称）配对
- 激活开关的 cue 操作化必须在 Methods/研究设计中兑现
- Theory Lens 必须与 Preview 中的研究设计一致（`previews/findings-preview` 变体 R 常承接激活逻辑的发现预览）

### 反模式提醒
- **不要把 Theory Lens 写成理论综述**: 2-3 句核心逻辑即可，不是文献回顾
- **不要引入与 Gap 无关的理论**: 如果 Tension 说的是时间动态缺口，Theory Lens 必须引入解释动态机制的理论
- **不要过度承诺**: "Drawing on X" ≠ "We fully develop X"——承诺要与 Theory 章节的实际深度匹配

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| AMJ | ⭐⭐⭐ 高 | 偏好心理/行为理论；trait-activation 动态透镜适配 CEO 心理类研究 |
| ASQ | ⭐⭐⭐ 高 | 需要更强的理论深度——激活机制需有心理学文献支撑（trait activation、personality systems） |
| OS | ⭐⭐ 中 | 接受机制化透镜，但需快速过渡到组织层面后果 |
| SMJ | ⭐⭐⭐ 高 | 简洁的理论承诺；动态透镜直接兑现"approach shifts over time"的战略问题 |

---

## 槽位填充正误对比

### `[baseline behavior] vs [shifted behavior]` — 安全行为连续谱两极

❌ "when cues indicate danger, individuals higher in the trait engage targets more." → 只给了"更强/更弱"的幅度变化，没有命名行为如何改变类型（avoidance → aggression）——审稿人看不到一个可辨识的个体内切换

✅ "when cues indicate that avoidance has not offered protection from external entities, individuals higher in the trait tend to shift away from avoidance to directly engage the external entities." → 明确命名连续谱的两极（avoidance vs aggression）和切换条件（保护失败 cue）——机制可辨识、可检验

**填充检查**: 你的两极是否构成同一连续谱的对立端？切换条件（cue）是否可操作化？
