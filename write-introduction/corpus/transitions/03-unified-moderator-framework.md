---
type: canonical_transition
canonical_id: "03-unified-moderator-framework"
status: ✓ STANDARD
function: "Main Effect → Boundary Conditions（主效应到统一调节框架的过渡）"
cross_paper: VERIFIED
generativity: GENERATIVE
exclusivity: HIGH
source_papers:
  - darby2026 (JOM, 2026): "information asymmetry unifies R&D intensity (firm-level) and device class (product-level)"
  - gamache2023 (SMJ, 2023): "scrutiny unifies gender and acquisition activity"
  - ceo_regulatory_focus_ijrm (IJRM, 2021): "regulatory focus unifies myopic marketing behaviors"
created: 2026-05-19
source: Extracted from darby2026 distill
---

# 03-unified-moderator-framework — 统一调节框架过渡

## 功能描述

当研究包含**多个调节变量**时，用**单一理论核心维度**将它们统一起来，避免调节变量显得松散无关。核心结构是：承认边界条件的必要性 → 引入统一理论维度 → 分别标注各变量的分析层级 → 预测统一效应方向（均削弱或均增强主效应）。

与分别展开每个调节变量再各找理论依据的区别：统一框架让读者感知到调节变量不是"事后追加"，而是**理论驱动的系统性边界检验**。

## 适用场景

- 研究包含 **2-4 个调节变量**，且它们可以共享同一理论机制
- 调节变量分布在**不同分析层级**（如 firm-level + product-level；individual-level + team-level）
- 需要展示理论的一致性（"不是随便挑了几个变量，而是检验同一理论维度在不同层级的表现"）
- 常见于 agency theory（information asymmetry）、upper echelons（executive discretion）、制度理论（institutional pressure）等理论框架

## 验证状态

### 跨论文复现
- **VERIFIED** (≥3 papers): darby2026 (JOM), gamache2023 (SMJ), ceo_regulatory_focus_ijrm (IJRM)
- 共同特征：多个 moderator → 一个 theoretical core dimension → 不同 levels

### 生成力
- **GENERATIVE**: "Both moderating hypotheses are grounded in the concept of [theoretical core dimension]" 可适配任何有统一理论机制的多调节变量研究

### 排他性
- **HIGH**: 仅适用于多调节变量共享同一理论机制的研究。若调节变量各自基于不同理论（如一个基于 agency theory，一个基于 resource dependence），不应使用此结构，而应分别论证

---

## 句法模板

### 变体 A：理论核心维度 + 多层调节（darby2026 型）

**模板**:
> We then consider possible boundary conditions by examining [number] moderating factors. Both moderating hypotheses are grounded in the concept of [theoretical core dimension]—a core dimension within [theory] defined as "[definition]" ([citation]). [Theoretical core dimension] between [party A] and [party B] inhibits [party A]'s ability to [function] and [function] ([citation]). As [theoretical core dimension] increases, so too does [consequence], wherein [mechanism] ([citation]). We examine [number] factors—one at the [level 1] and one at the [level 2]—that may increase [theoretical core dimension] between [party A] and [party B]. Such increases make it more difficult for [party A] to [function], thereby weakening [main relationship].

**来源**: darby2026 (JOM), P5

**原文锚定**:
> We then consider possible boundary conditions by examining two moderating factors. Both moderating hypotheses are grounded in the concept of information asymmetry—a core dimension within agency theory defined as "a condition wherein one party in a relationship has more or better information than another" (Bergh et al. 2019, 122). Information asymmetry between a principal and an agent inhibits the principal's ability to monitor the agent and assess the agent's behavior (Eisenhardt 1989). As information asymmetry increases, so too does the potential for moral hazard, wherein agents pursue their own objectives rather than those of principals (Bendoly et al. 2025). We examine two factors—one at the firm-level and one at the product-level—that may increase information asymmetry between executives and large institutional investors. Such increases make it more difficult for large institutional investors to monitor executives, thereby weakening the association with time-to-recall.

**关键特征**:
- "We then consider possible boundary conditions" → 平滑过渡，不突兀
- "Both moderating hypotheses are grounded in the concept of..." → 立即建立统一框架
- 引用**理论定义**（带页码）而非笼统提及，增强学术严谨性
- 明确标注**分析层级**（firm-level / product-level），让读者预知变量的层次分布
- 统一预测方向：both increase X → both weaken monitoring → both weaken main effect
- 适用于：agency theory 的信息不对称、upper echelons 的自由裁量权、制度理论的压力等统一维度

---

### 变体 B：情境化统一型（gamache2023 型）

**模板**:
> We also consider [number] boundary conditions that may alter [relationship]. Both boundary conditions reflect [theoretical core dimension], but they operate through different pathways. [Moderator 1] captures [dimension 1] and reflects [mechanism 1]. [Moderator 2] captures [dimension 2] and reflects [mechanism 2]. We expect that both will [strengthen/weaken] [relationship], but for different reasons.

**来源**: gamache2023 (SMJ), adapted

**关键特征**:
- 明确说明"for different reasons" → 承认机制差异，同时保持预测方向一致
- 适合两个调节变量虽然共享理论维度但路径不同的情况

---

### 变体 C：精简统一型（ceo_regulatory_focus_ijrm 型）

**模板**:
> We further argue that [theoretical core dimension] matters. Specifically, [moderator 1] and [moderator 2] reflect different facets of [theoretical core dimension]. [Brief explanation of each]. Taken together, we expect that [main relationship] will be [strengthened/weakened] under [condition].

**来源**: ceo_regulatory_focus_ijrm (IJRM), adapted

**关键特征**:
- 更简洁，适合调节变量理论逻辑较为直接的研究
- "reflect different facets of" → 强调构念的多面性而非层次差异

---

## 组装规则

### 必须配对
- **与多调节变量研究设计配对**: 若只有一个调节变量，不需要"统一框架"，直接展开即可
- **与 Theory Lens 配对**: 统一框架中引用的理论必须在 Theory 部分有更充分的展开
- **与 Makadok Boundary 贡献配对**: 使用此结构的论文通常在 Contribution 中声明 Boundary 维度贡献

### 互斥
- **不能与各自独立理论的调节变量同用**: 如果调节变量 A 基于 theory X，调节变量 B 基于 theory Y，强行统一会扭曲理论逻辑
- **不能与 "exploratory" 调节变量同用**: 统一框架暗示理论驱动的假设，不适用于事后探索性分析

### 反模式提醒
- **不要只说"we examine two moderators"而不解释为什么**: 必须立即给出统一理论维度的理由
- **不要用不同的理论解释不同的调节变量，却声称它们"统一"**: 诚实边界——如果机制真的不同，不要用此结构
- **不要遗漏预测方向**: 统一框架必须说明所有调节变量对主效应的预测方向（均增强、均削弱、或条件化反转）
- **层级标注必须清晰**: 如果调节变量跨越 firm/product/individual 等层级，必须在首次出现时明确标注，否则读者会混淆分析单位

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| JOM | ⭐⭐⭐ 极高 | 运营/质量/安全研究常用 firm-level + product-level 双层调节；信息不对称是经典统一维度 |
| SMJ | ⭐⭐⭐ 高 | 战略研究常用 executive discretion / environmental uncertainty 作为统一维度 |
| AMJ | ⭐⭐⭐ 高 | 组织行为研究常用 individual-level + team-level / context-level 组合 |
| OS | ⭐⭐⭐ 高 | 制度研究常用 institutional pressure / legitimacy 统一多个场域层面的调节变量 |
| ASQ | ⭐⭐ 中 | 可用，但 ASQ 偏好更深层面的理论统一（如 paradox / contradiction），而非简单的"核心维度" |
