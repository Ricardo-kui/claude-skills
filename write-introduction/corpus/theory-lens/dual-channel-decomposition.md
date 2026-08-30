---
type: canonical_theory_lens
canonical_id: "dual-channel-decomposition"
status: EMERGING
gap_type: Incompleteness
cross_paper: EMERGING
generativity: GENERATIVE
exclusivity: MEDIUM
source_papers:
  - fini_jourdan_perkmann_2017 (AMJ, 2017): "Dual-channel index decomposition — one index family split into ability + identity-conformance dimensions whose alignment depends on index source (endogenous aligned / exogenous divergent)"
created: 2026-08-12
updated: 2026-08-12
source: Distilled by distill-introduction-exemplar Phase 4.6 (fini_jourdan_perkmann_2017 Introduction)
---

# Theory Lens — 双通道指数分解（Dual-Channel Index Decomposition）

## 功能描述

Theory Lens（P4-P5）的功能：在 Gap/Tension 建立之后，向读者提供**新的解释框架**——告诉他们"我们可以用什么透镜来看这个问题"。这不是理论综述，而是**理论承诺**："Drawing on X, we argue that..."。

本模板沉淀的是**单信号家族双通道分解**透镜：把**同一个可观察评价信号（indices）**分解为**两个信息维度**（能力 ability + 身份一致 identity conformance），并给出**维度对齐条件取决于信号来源**（endogenous 对齐 / exogenous 分歧）的理论结构。分解 → 对齐条件 → 分歧 → 由此推导条件化/曲线预测，是它的完整逻辑链。

与 `theory-lens-templates.md`（跨框架句法模板集，变体 A = trait-activation 动态透镜）互补：后者建模"稳定倾向 + 情境 cue → 个体内开关"；本模板建模"一个信号携带两种信息，二者随信号来源对齐或分歧"。二者都是不绑定单一理论名的可迁移透镜模式。

## 适用场景

- Gap 类型 = **Incompleteness**（已知机制在 context 层面的延伸；可含 theory-level Inadequacy 次层）
- 研究有**单一可观察信号**（endorsement、rating、certification、analyst coverage、prior evaluation），该信号同时携带质量/能力信息与身份/规范信息，且两种信息的一致性取决于**信号来自谁**
- 主效应为曲线（inverted-U）或条件化预测，其形状由双通道分歧机制推导，而非堆叠调节变量

## 验证状态

### 跨论文复现
- **EMERGING** (1 paper): fini_jourdan_perkmann_2017 (AMJ)

### 生成力
- **GENERATIVE**: 单信号分解为两信息维度 + 对齐条件取决于来源，可迁移到任何信号解读设计（背书、评分、认证、分析师覆盖），其中信号携带质量 + 身份/一致信息，且二者一致性依赖信号来源

### 排他性
- **MEDIUM**: 主要服务 Incompleteness × Mechanism（信号解读/多受众评价）；不适用于无多源信号、无身份/规范维度的纯质量信号研究

---

## 句法模板

### 变体 A：双通道指数分解型（fini2017 型）

**模板**:
> "We address this question by developing a theory that distinguishes between [indices from aligned evaluators] and [indices from external evaluators]. We argue that such indices generally provide two types of information to evaluators: indices of [ability: higher past evaluations → higher imputed capability], and indices of [conformance: higher past evaluations → greater conformity with the identity expected by the evaluating audience]. In the case of [aligned indices], both dimensions are closely aligned and therefore indistinguishable. However, in the case of [external indices], both dimensions diverge; this has implications for how [focal evaluators] are influenced by evaluations provided by [external audiences]."

**来源**: fini_jourdan_perkmann_2017 (AMJ), P4

**原文锚定**:
> "We address this question by developing a theory that distinguishes between endogenous indices (previous evaluations by peers) and exogenous indices (previous evaluations provided by an external, non-peer audience). We argue that such indices generally provide two types of information to evaluators: indices of ability (the higher somebody's past evaluations, the higher their imputed ability), and indices of identity conformance (the higher somebody's past evaluations, the more they conform to the identity expected by the evaluating audience). In the case of endogenous indices, both dimensions are closely aligned and therefore indistinguishable. However, in the case of exogenous indices, both dimensions diverge; this has implications for how peer evaluators are influenced by the evaluations provided by external audiences."

**关键特征**:
- **单信号家族双通道分解**: 不是对比两个构念，而是把**一个**指数家族拆成两个信息维度（ability + identity conformance）——这是与 `09-construct-contrast-introduction`（新构念借同家族旧构念对照）最根本的区别
- **对齐条件取决于信号来源**: endogenous（同源）时两维对齐、不可区分；exogenous（异源）时两维分歧——来源本身进入理论结构，而非只当调节变量
- **曲线预测从分歧机制推导**: inverted-U 是"正的能力通道 + 负的身份一致通道"的反向叠加的机械结果——预测是**推导**出来的，不是断言出来的
- **直接回应 RQ**: 透镜首句 "We address this question by developing a theory..." 显式回收 Tension 段的 RQ，满足"Theory Lens 必须与 Tension 关键词重叠"的配对要求

**适用**: endorsement/rating/certification/analyst-coverage/prior-evaluation 类信号解读研究；多受众评价（peer vs external）研究；Incompleteness × Mechanism；贡献类型为 Mechanism（主）+ Constructs（次，endogenous/exogenous 区分）

**禁忌**: 双通道必须都携带可识别的信息且都有理论根据——若外部认可不同时携带能力与身份/规范信息，不要为追求反直觉套用双通道；若两类受众无任何能力标准重叠，须先论证该信号为何仍具信息价值；曲线预测必须由双通道机制推导，不得用堆叠调节变量代替机制

---

## 组装规则

### 必须配对
- Theory Lens 必须直接回应 Tension 提出的 gap（关键词重叠）——本变体常与 `tensions/02-implicit-assumption-wrong` 变体 G（同质同侪推断→跨受众双信息分离）或 `tensions/01-despite-progress-unaddressed`（同质受众机制→多受众情境延伸）配对
- 双通道分歧的预测必须在 Preview 中兑现为 inverted-U / 条件化预测（`previews/mechanism-preview` 变体 F 常承接通道匹配调节）
- Theory Lens 必须与 Theory Development 章节的实际理论来源一致

### 反模式提醒
- **不要把 Theory Lens 写成理论综述**: 2-3 句核心逻辑即可，不是文献回顾
- **不要引入与 Gap 无关的理论**: 如果 Tension 说的是信号解读/多受众机制缺口，Theory Lens 必须引入解释该机制的理论
- **不要过度承诺**: "We address this question by developing a theory..." ≠ "We fully develop X"——承诺要与 Theory 章节的实际深度匹配
- **不要把单信号双通道写成两个并列信号**: 双通道是同一指数的两个信息维度，不是两个不同的自变量

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| AMJ | ⭐⭐⭐ 高 | 偏好心理/行为/社会评价理论；fini2017 即 AMJ 范本 |
| ASQ | ⭐⭐⭐ 高 | 需要更强的理论深度——双通道需有社会评价/身份理论支撑 |
| OS | ⭐⭐ 中 | 接受机制化透镜，但需快速过渡到组织层面后果 |
| SMJ | ⭐⭐⭐ 高 | 简洁的理论承诺；信号解读/多受众战略问题适配 |

---

## 槽位填充正误对比

### `[indices from aligned evaluators] vs [indices from external evaluators]` — 双通道分解

❌ "External indices influence evaluators positively because they signal ability." → 只用了能力通道，压平了双通道——身份/一致通道被删掉，inverted-U 无从推导

✅ "In the case of endogenous indices, both dimensions are closely aligned and therefore indistinguishable. However, in the case of exogenous indices, both dimensions diverge; this has implications for how peer evaluators are influenced by the evaluations provided by external audiences." → 显式命名两个维度（ability + identity conformance）+ 对齐条件（endogenous aligned / exogenous divergent）——曲线预测由此机械推导

**填充检查**: 你的双通道是否都携带可识别信息？对齐条件是否显式绑定到信号来源？曲线/条件化预测是否从分歧推导而非断言？

### `[focal evaluators]` — 焦点评价者

❌ "this has implications for how evaluators are influenced" → 泛化了评价者——没说明是对外源信号的解读，还是对同源信号的解读

✅ "this has implications for how peer evaluators are influenced by the evaluations provided by external audiences" → 焦点评价者（peer）+ 被解读的信号（external）双指定——把对齐/分歧机制锚定在具体的受众关系上
