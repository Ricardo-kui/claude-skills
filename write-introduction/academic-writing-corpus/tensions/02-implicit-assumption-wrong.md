---
type: canonical_tension
canonical_id: "02-implicit-assumption-wrong"
status: ✓ STANDARD
gap_type: Inadequacy
cross_paper: ROBUST
generativity: GENERATIVE
exclusivity: HIGH
source_papers:
  - 'paruchuri2020 (SMJ, 2020): "A major, but generally untested assumption... is that..."'
  - 'gamache2020 (SMJ, 2020): "While important... considers... broadly" (conflation assumption)'
  - 'han2020 (AMJ, 2020): "Most research on [topic] has treated [construct] as decontextualized"'
  - 'zhao_ding2022 (OS, 2023): "challenges an implicit premise that lower entry barriers mechanically translate into greater product variety" (mechanical-causal-chain assumption; variant D)'
  - "weng_yang (JMS): self-labeled 'theoretical inadequacy' with embedded theory lens — 'While insightful, prior studies have fallen short... This is an important theoretical inadequacy since...'"
  - 'reinwald_kanitz_bamberger_backmann_hoegl_2026 (Organization Science, 2026): "mixed findings expose the implicit assumption that political-dissimilarity effects remain stable rather than being activated by macro events" (temporal-stability assumption; variant F)'
created: 2026-05-18
updated: 2026-08-02
source: Extracted from MVP30 narrative_analysis files + weng_yang distill + reinwald et al. 2026 distill
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

### 变体 D：挑战机械因果链前提型（zhao_ding2022 型）

**模板**:
> "[Contribution / framing 句]. [We / Our study] challenges an implicit premise that [driver X] mechanically translate(s) into [outcome Y]. Although prior [work / research] often assumes that [actors] achieve [outcome Y] by [assumed mechanism], we show that [outcome Y] varies systematically with [our explanatory variable]. [Contrast finding 1], whereas [contrast finding 2]."

**来源**: zhao_ding2022 (OS, 2023), P35（标志性语言）；Tension 的逻辑铺垫在 P25-P27（demand uncertainty → firm-specific knowledge insufficient）

**原文锚定**:
> "First, we contribute to the emerging research on positioning strategies in digital markets by theorizing and testing antecedents of heterogeneous positions. In doing so, our study challenges an implicit premise that lower entry barriers mechanically translate into greater product variety. Although prior work often assumes that entrants in digital markets expand product variety by targeting heterogeneous customer preferences, we show that novelty in positioning varies systematically with external market feedback."

**关键特征**:
- 标志性句式 **"challenges an implicit premise that [X] mechanically translate into [Y]"**——挑战的是一条"机械因果链"假设（低壁垒 → 机械地 → 多样性），而非构念混淆、去情境化或未检验假设
- **Gap 声明放在 Contribution 段（P35）而非独立 Tension 段**；Tension 的逻辑铺垫（demand uncertainty、firm-specific knowledge 不足以 mapping demand landscape）提前在 P27 完成。这是紧凑型 Introduction 的常见编排
- **"Although prior work often assumes... we show that... varies systematically with..."** 的让步-反证结构：先陈述被挑战的假设，再用"varies systematically with [我们的变量]"给出替代机制
- 紧跟对比发现（High dissatisfaction → differentiated positions；high heterogeneity → imitative positioning）兑现"varies systematically"的承诺

**与变体 A/B/C 的区分**:
- 变体 A（paruchuri）：连续解构两个"未检验假设"（untested assumption）
- 变体 B（gamache）：指出构念被"笼统对待"，需细分（considers broadly → distinguish A/B）
- 变体 C（han）：指出构念被"去情境化"对待（decontextualized）
- **变体 D（zhao/gaba）：挑战一条"机械因果链"**（X mechanically → Y）——被挑战的不是构念的测量或边界，而是一条被默认的因果映射

**适用情境**:
- 研究挑战的是"X 机械地导致 Y"的隐含因果假设（而非构念混淆或测量问题）
- 适合紧凑型 Introduction（Gap 声明嵌入 Contribution 段）
- 目标期刊接受挑战性贡献：OS, SMJ, AMJ

**使用禁忌**:
- 若 Gap 是构念混淆（A 和 B 被混为一谈），改用变体 B（gamache 型）
- 若 Gap 是理论不平衡或两个理论推出矛盾预测，改用 `06-theoretical-imbalance` 或 `04-reality-contradicts-consensus`
- 不能只喊"challenges an implicit premise"而不给替代机制——必须紧跟"varies systematically with [变量]"或对比发现，否则沦为空泛声明

---

### 变体 E：自标Inadequacy+理论嵌入型（weng_yang 型）

**模板**:
> "While insightful, prior studies have fallen short of thoroughly examining [specific overlooked factor]. This is an important theoretical inadequacy since [reason: why overlooking this factor matters — tie to theory]. [Theory name] asserts that [core theoretical claim with quote] ([citation]). As [key concept] affect how [actors] absorb and interpret information, outline alternatives, and implement eventual decisions, [outcomes] are likely to be altered. Prior research suggests that [related but non-central factors] have strong bearings on [outcomes] ([citations]). In this study, we suggest that [our central claim: the overlooked factor is likely to play a crucial role]."

**来源**: weng_yang (JMS), P2

**原文锚定**:
> "While insightful, prior studies have fallen short of thoroughly examining the role of CEOs in establishing within-firm pay disparity. This is an important theoretical inadequacy since executives' personal views profoundly affect their decisions and behaviours (Liu et al., 2018; Wowak et al., 2017)."

**关键特征**:
- 自标 "theoretical inadequacy"——罕见地直接使用 inadequacy 标签，而非依赖隐含语言（如 "overlooks" / "untested assumption"）
- Tension 段落内嵌微型 Theory Lens（upper echelons），形成 "gap→why matters→alternative lens" 的微型三段论——不需要等到下一段才引入理论
- 使用理论原文引用（Hambrick & Mason, p. 193）作为权威支撑，而非仅依赖实证引用
- 结尾句以 positive claim 收束（"In this study, we suggest that..."），而非传统的以 gap 陈述收束——从批评直接过渡到提案

**与变体 A/B/C/D 的区分**:
- 变体 A（paruchuri）：连续解构两个"未检验假设"（untested assumption）
- 变体 B（gamache）：指出构念被"笼统对待"（considers broadly → distinguish A/B）
- 变体 C（han）：指出构念被"去情境化"（decontextualized）
- 变体 D（zhao/gaba）：挑战"机械因果链"（X mechanically → Y）
- **变体 E（weng/yang）：自标 inadequacy + 同段理论嵌入 + positive claim 收束**——被挑战的不是一个具体假设，而是文献整体的"忽略内部因素"倾向；理论在同一段内被引入作为替代视角

**适用**: 适用于 Inadequacy × Phenomenon 组合；当被忽略的因素是一个"人/行动者"特征（而非结构/制度因素），且可以用一个成熟理论来论证为什么这个因素重要；期刊接受 "theoretical inadequacy" 标签（JMS, JM, SMJ, AMJ）

**禁忌**: "避免将 'theoretical inadequacy' 用于仅仅是遗漏了变量（那是 Incompleteness）；必须有真正的理论视角缺失；Theory Lens 嵌入 Tension 时不应过度展开（保留详细推演给 Theory section）；positive claim 收束时不要过度承诺（用 'we suggest' 而非 'we prove'）"

---

### 变体 F：混合发现 → 暴露稳定效应假设 → 宏观事件激活型（Reinwald et al. 2026 型）

**验证状态**: EMERGING（单篇来源；仅作 `section_variant`）

**模板**:
> "Prior research offers inconsistent evidence about whether [difference/relationship X] affects [workplace outcome Y]. These findings are difficult to reconcile if the effect is assumed to remain stable over time. We suggest that this stability assumption is incomplete: [macro event Z] can bring an otherwise suppressible identity or distinction to the foreground, activating [threat/attention mechanism] and thereby changing when [X] shapes [Y]."

**来源**: Reinwald, Kanitz, Bamberger, Backmann, and Hoegl (2026), *Organization Science*, Introduction.

**关键特征**:
1. 先把显著与不显著结果组织成真实的经验张力，而不是笼统声称“文献很少”。
2. 被挑战的是“效应跨时间稳定”的共同建模假设；替代解释是事件驱动的构念激活，而非简单增加一个控制变量。
3. 宏观事件必须与微观机制相连：事件提高身份显著性/威胁加工，近端机制再影响互动结果。

**适用**: 同一关系在事件期与常态期出现混合证据；核心构念平时可被压抑、事件中被激活；贡献属于 Inadequacy × Boundary/Mechanism。

**禁忌**:
- 不得把任何结果异质性都归因于“时间变化”；必须指出理论上可识别的激活事件与机制。
- 只有一个事件后截面不能支持“随时间变化”的完整叙事；至少需要事件前后比较或重复测量。
- “事件后斜率不显著”只能写为观察窗内未检测到衰减，不能写成永久效应。

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

---

## 槽位填充正误对比

### `[gap statement]` — Inadequacy（挑战隐性假设）

❌ "Few studies have examined the relationship between political ties and innovation." → 没说为什么少，审稿人反问 "so what?"

✅ "The implicit assumption underlying the political connections literature — that resource acquisition automatically translates into performance gains — may be incorrect. Politically connected firms face a structural dilemma: the relationships that facilitate resource inflows simultaneously reduce the pressure to deploy those resources efficiently." → 指出了具体的隐性假设（"resource acquisition → performance"）+ 解释了为什么它可能是错的（"reduce the pressure to deploy efficiently"）

### `[theoretical consequence]` — 理论后果

❌ "This omission limits our understanding of political ties." → 笼统——"limits understanding" 可以套在任何研究上

✅ "Without specifying the allocation mechanism, resource dependence theory cannot explain why politically connected firms with comparable resource endowments exhibit widely divergent innovation outcomes." → 具体到某个理论的特定预测能力受影响（"resource dependence theory" + "cannot explain divergent outcomes"）
