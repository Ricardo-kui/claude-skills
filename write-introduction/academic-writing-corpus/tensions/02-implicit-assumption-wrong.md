---
type: canonical_tension
canonical_id: "02-implicit-assumption-wrong"
status: ✓ STANDARD
gap_type: Inadequacy
cross_paper: VERIFIED
generativity: GENERATIVE
exclusivity: HIGH
source_papers:
  - paruchuri2020 (SMJ, 2020): "A major, but generally untested assumption... is that..."
  - gamache2020 (SMJ, 2020): "While important... considers... broadly" (conflation assumption)
  - han2020 (AMJ, 2020): "Most research on [topic] has treated [construct] as decontextualized"
created: 2026-05-18
source: Extracted from MVP30 narrative_analysis files
---

# 02-implicit-assumption-wrong — 隐性假设错误 Tension

## 功能描述

Inadequacy 问题化的核心 Tension：不是"文献遗漏了东西"，而是"文献依赖一个未经验证或有问题的假设"。这个假设可能是关于构念的性质、关系的方向、情境的无关性，或者是多个构念的可互换性。揭示这个假设的错误，就为修正视角的研究建立了必要性。

## 适用场景

- Gap 类型 = **Inadequacy**（文献看到了现象但理解偏了）
- 需要展示已有研究共享一个未被意识到的假设
- 这个假设的修正对理论有实质性影响
- 目标期刊接受"修正性"贡献（SMJ, AMJ, OS, ASQ）

## 验证状态

### 跨论文复现
- **VERIFIED** (≥3 papers): paruchuri2020 (SMJ), gamache2020 (SMJ), han2020 (AMJ)

### 生成力
- **GENERATIVE**: "The implicit assumption that... may be incorrect because..." 模板高度可迁移

### 排他性
- **HIGH**: 是区分 Inadequacy 与 Incompleteness 的标志性 Tension

---

## 句法模板

### 变体 A：双重解构型（paruchuri2020 型）

**模板**:
> "A major, but generally untested assumption underlying [research stream] is that [assumption 1]. However, [complexity that undermines assumption]. [Elaboration]. A second frequent, but generally untested assumption... is that [assumption 2]. This assumption is important because [significance]. However, [limitation of current research]."

**来源**: paruchuri2020 (SMJ), P2-P3

**原文锚定**:
> "A major, but generally untested assumption underlying these questions and concerns about reputation spillovers is that other firms are seen as being similar enough to the focal firm to experience a reputation spillover if they are members of the same broad category... A second frequent, but generally untested assumption... is that the spillover effects will be enduring, at least to some degree."

**关键特征**:
- "major, but generally untested assumption" → 精准定位理论软肋
- 连续解构两个核心假设，展示问题的系统性
- 每个假设都解释"为什么重要"和"为什么不成立"

---

### 变体 B：构念混淆型（gamache2020 型）

**模板**:
> "While important, research on [topic] generally considers [phenomenon] broadly. As a result, scholars have yet to systematically distinguish between [specific type A] and [specific type B]. This distinction is theoretically meaningful because [reason why A and B have different antecedents/consequences]."

**来源**: gamache2020 (SMJ), P2-P3

**原文锚定**:
> "While important, research on corporate social responsibility generally considers stakeholder strategies broadly. As a result, scholars have yet to systematically distinguish between the specific types of stakeholder strategies that firms pursue. This distinction is theoretically meaningful because different types of stakeholder strategies may have different antecedents..."

**关键特征**:
- "While important" → 先承认文献价值（不树稻草人）
- "considers... broadly" → 指出笼统对待的问题
- "This distinction is theoretically meaningful because" → 解释为什么细分重要

---

### 变体 C：去情境化批判型（han2020 型）

**模板**:
> "Most research on [topic] has treated [construct] as decontextualized. This is problematic because the context in which an event or action occurs can differentially shape assessments and responses, sometimes even inverting the relationships ([citations]). We have little insight, however, about how context shapes [effect]."

**来源**: han2020 (AMJ), P2

**原文锚定**:
> "Further, most research on the relationship between status and scandalization has treated the misbehaving actor's status as decontextualized. This is also problematic because the context in which an event or action occurs can differentially shape assessments and responses, sometimes even inverting the relationships."

**关键特征**:
- "treated [construct] as decontextualized" → 识别出一个理论假设：情境不重要
- "sometimes even inverting the relationships" → 暗示忽略情境会导致方向性误判
- 直接挑战一个方法论层面的隐性假设

---

## 组装规则

### 必须配对
- **与 `05-literature-consensus-blindspot` (Hook) 配对**: 文献共识盲点引入学术情境，隐性假设揭示盲点的具体内容
- 或与 `04-puzzle-paradox` (Hook) 配对：谜题暗示某个假设错误，隐性假设 Tension 明确指出哪个假设有问题
- **与 `02-implicit-assumption-wrong` 配套的 Stakes**: 解释如果假设持续错误，利益相关者会做出什么误判

### 互斥
- **不能与 `01-despite-progress-unaddressed` (Tension) 同用**: 前者是"好但不完整"，本品是"依赖错误假设"
- **不能与 Incompleteness Gap 同用**: 逻辑矛盾

### 反模式提醒
- **不要制造稻草人假设**: 不能声称一个文献没有的假设。必须引用具体的、被广泛引用的文献来证明假设确实存在
- **不要只指出假设错误而不提供替代**: Gap 段结尾必须暗示一个修正的框架
- **不要把"尚未研究"包装成"假设错误"**: 区分 "not yet studied" 和 "studied under a wrong assumption"

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| SMJ | ⭐⭐⭐ 极高 | 变体 A（双重解构型）是 SMJ 标志句式 |
| AMJ | ⭐⭐⭐ 极高 | 变体 C（去情境化批判型）最适配 AMJ |
| ASQ | ⭐⭐⭐ 高 | 偏好构念层面的假设挑战（变体 B） |
| OS | ⭐⭐ 中 | 偏好实践/制度层面的假设挑战 |
| JM/JMR | ⭐⭐ 中 | 需要与管理后果挂钩 |
