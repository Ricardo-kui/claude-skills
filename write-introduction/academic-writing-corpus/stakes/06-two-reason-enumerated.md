---
type: canonical_stakes
canonical_id: "06-two-reason-enumerated"
status: ⚠ EMERGING
gap_type: Incompleteness
cross_paper: VERIFIED
generativity: GENERATIVE
exclusivity: LOW
source_papers:
  - malik_wang_martin_gomezmejia2025 (JM, 2025): "This oversight is important for two primary reasons. First... Second..."
  - pollock2015 (ASQ, 2015): "Understanding X is important because [theoretical]. [process]. For [young firms], [practical]. A deeper understanding can also [downstream]."
  - ridge_hill_ingram_kolomeitsev_worrell2024 (AMJ, 2024): "Two-construct-property theoretical reasons — construct affects both views and actions AND is subject to activation (variant C)"
created: 2026-05-24
updated: 2026-08-12
source: Extracted from Malik_etal_2025_JM distill-introduction-exemplar + ridge2024
---

# 06-two-reason-enumerated — 双原因枚举型 Stakes

## 功能定义

在 Tension 建立 gap 之后，用 "This oversight is important for [N] primary reasons" 的结构化枚举来论证 gap 的重要性。每个 reason 来自独立的论证维度，共同建立"这个 gap 必须被填补"的紧迫感。

## 适用场景

- Incompleteness gap 建立后需要升级重要性
- Research question 涉及多 stakeholder（shareholders + customers + employees 等）
- Gap 的后果可以从多个独立维度论证（如 stakeholder harm + theoretical mechanism breakdown）

---

## 句法模板

### 变体 A：后果+机制双原因型（malik2025 型）

**模板**:
> "This oversight is important for two primary reasons. First, while [agents] are responsible for [primary duty], their actions during [crisis context]—such as [specific examples]—can have long-lasting consequences for [stakeholder list]. Second, although [mechanism/design feature] is typically designed to [intended alignment] under [normal conditions], that alignment may weaken during [crisis conditions]. In these situations, [mechanism becomes volatile], exposing [agents] to [risk type]—even as their [long-term interest] remains tied to [stakeholder value]. Under such pressure, [agents] may seek to [self-protective action] ([citation]), potentially at the expense of [stakeholder value]."

**来源**: malik_wang_martin_gomezmejia2025 (JM), P3

**原文锚定**:
> "This oversight is important for two primary reasons. First, while CEOs are responsible for steering business strategy, their actions during crises—such as product failures or organizational breakdowns—can have long-lasting consequences for shareholders, customers, employees, or other related stakeholders. Second, although stock options are typically designed to align CEO interests with those of shareholders under normal conditions, that alignment may weaken during crises. In these situations, the value of options becomes highly volatile, exposing CEOs to significant short-term financial risk—even as their long-term wealth remains tied to shareholder value. Under such pressure, CEOs may seek to protect their current wealth (Kahneman & Tversky, 1979), potentially at the expense of long-term shareholder value."

**关键特征**:
- **"This oversight is important for [N] primary reasons"**: 显式预告论证结构，读者知道接下来有 N 个独立理由
- **Reason 1 — 后果维度**: Stakeholder harm（"long-lasting consequences for shareholders, customers, employees"）
- **Reason 2 — 机制维度**: Mechanism breakdown（alignment weakens under crisis → volatile options → self-protective behavior）
- **两个原因来自不同论证域**: One is about WHO is harmed, the other about WHY the existing mechanism fails — 避免重复
- **从 broad 到 specific 的递进**: Reason 1 描述广泛后果，Reason 2 提供具体的理论机制
- **"potentially at the expense of"**: 收束句同时点出 stakes 的代价方向

**Reason 维度选择指南**:
| 维度 | 适用场景 | 示例措辞 |
|------|---------|---------|
| **后果维度** | Gap 导致可观察的负面结果 | "can have long-lasting consequences for..." |
| **机制维度** | 现有解释机制在特定条件下失效 | "alignment may weaken during..." / "the mechanism breaks when..." |
| **规模维度** | Gap 影响的经济/社会规模 | "this affects [N] firms / [$$$] in market value" |
| **趋势维度** | Gap 在当下特别紧迫 | "this trend is accelerating..." / "regulatory pressure is mounting..." |
| **理论维度** | Gap 阻碍理论发展 | "without understanding this, theory cannot explain..." |

---

## 组装规则

### 必须配对
- **紧随 Tension**: "This oversight is important..." 直接接续 "little is known" / "remains unclear" 等 Incompleteness 语言
- **Reason 数量 ≥ 2**: 单原因是 assertion 而非论证——两个理由建立论证厚度
- **每个 Reason 有独立论证域**: 不能两个原因都是 stakeholder harm 的不同说法

### 互斥规则
- **不与量化 Stakes 冲突但需配合**: 如果使用 `02-quantified-economic-loss`，双原因 Stakes 提供的是论证结构，量化数据可以作为某个 Reason 的支撑
- **Reason 不替代 Theory**: Reason 2 提供的是"为什么 gap 重要"的机制论据，不是全文的理论框架

### 反模式提醒
- **Reason 1 和 Reason 2 来自同一论证域**: "First, this harms shareholders. Second, this harms customers." → 应合并为一个 "harms multiple stakeholders" reason
- **Reason 2 是机制论证而非 stakes 论证**: 如果 Reason 2 读起来像是 Theory 部分的预览而非 "why this matters" → 需要重写为 stakes 语言
- **"Two reasons" 预告后各 reason 极度不均**: 一个 reason 有 5 句另一个只有 1 句 → 暗示其中一个 reason 是凑数的
- **N > 3 时读者失去耐心**: 两到三个原因是 sweet spot

---

### 变体 B：多层 ascending-cascade 型（pollock2015 型）

**模板**（不编号的递进式多层 Stakes，4 层）:
> "Understanding [the nature and nuances of the gap] is important because [theoretical layer: the constructs/mechanisms differ in a way that matters]. [Developmental/process layer: building/achieving X requires understanding how Y changes over time and how Z can influence its trajectory]. For [specific audience, e.g., young/resource-constrained actors], understanding this [relationship] can provide crucial guidance for [practical resource-allocation decision] ([citations]). A deeper understanding of [the gap] can also shed light on [downstream outcome domain: how it influences broader organizational/societal outcomes and success] (e.g., [citations])."

**来源**: pollock2015 (ASQ), P4

**原文锚定**:
> "Understanding the nature and nuances of the relationship between reputation and status and how it evolves over time is important because reputation and status are built in different ways and create different kinds of value (Washington and Zajac, 2005; Barron and Rolfe, 2012). Building each intangible asset requires understanding how reputation and status change over time and how significant events can influence the trajectory of their development. For young firms, understanding this relationship can provide crucial guidance for investing their scarce resources and attention to effectively build their status and reputation (Rindova, Petkova, and Kotha, 2007; Fund et al., 2008). A deeper understanding of how status and reputation coevolve can also shed light on how these two intangible assets influence organizational outcomes and success (e.g., Dimov, Shepherd, and Sutcliffe, 2007; Ertug and Castellucci, 2013)."

**关键特征**:
- **不编号的递进 cascade**（vs 变体 A 的 "First... Second..." 显式编号）: 用 "because → [elaboration] → For [audience] → A deeper understanding can also" 的语篇连接词实现 4 层递进，节奏更流畅、适合 ASQ narrative 风格
- **四层从抽象到具体、从理论到实践到下游**:
  1. **理论层** — "built in different ways and create different kinds of value"（构念本质差异）
  2. **过程/发展层** — "requires understanding how... change over time and how significant events can influence the trajectory"（动态过程）
  3. **受众特定实践层** — "For young firms... crucial guidance for investing their scarce resources"（具体受众的资源配置决策）
  4. **下游结果层** — "A deeper understanding... can also shed light on how... influence organizational outcomes and success"（对更广结果域的启示）
- **"can also" 收束**: 末层用 "A deeper understanding... can also shed light on..." 拓展到下游结果域，把 gap 的重要性从"对本研究对象重要"升级到"对更广文献重要"——这是 stakes 的最高能量收束
- **与变体 A 的关系**: 变体 A 是显式编号的双原因（适合 JM 结构化风格）；变体 B 是不编号的递进多层（适合 ASQ/AMJ narrative 风格），层数可 3–4，每层来自不同论证域

**适用条件**:
- Gap 的后果可从理论 + 过程 + 受众特定实践 + 下游结果多个层面论证
- 目标期刊偏好 narrative 而非 enumerate 的 Stakes（ASQ/AMJ）
- 研究对象本身有明确的"弱势/资源约束"受众（如 young firms, small ventures, emerging-market firms）——使第 3 层"受众特定实践"自然落地

**禁忌**:
- 四层不得来自同一论证域——理论层与下游层不能都讲"影响 outcomes"
- 第 3 层受众特定实践必须具体到"资源配置/决策"层面，不能泛泛说"对 X 重要"
- "can also shed light on" 的下游域必须与本研究 DV 有理论距离——若下游就是 DV 本身，则不是升级而是重复

---

### 变体 C：双构念属性理论型（ridge2024 型）

**模板**:
> "Thus, understanding how [focal construct] impacts [outcome] is particularly important for at least two reasons. First, [construct] affects both [cognition] and [action] toward [targets]. Second, [construct] is subject to activation, a process in which [cognitions and ensuing choice tendencies] stemming from the trait change after prompting by [trait-relevant cues] (i.e., [operationalized cues]; [citations])."

**来源**: ridge_hill_ingram_kolomeitsev_worrell2024 (AMJ), P3 end

**原文锚定**:
> "understanding how CEO paranoia impacts stakeholder engagement is particularly important for at least two reasons. First, paranoia affects both views and actions toward others. Second, paranoia is subject to activation, a process in which cognitions and ensuing choice tendencies stemming from the trait change after prompting by trait-relevant cues."

**关键特征**:
- **两个 reason 都是理论性构念属性**: 不同于变体 A 的"后果维度 + 机制维度"、也不同于变体 B 的"理论→过程→受众→下游"递进——本变体的两个理由都关于构念本身的内在属性，是纯理论 stakes
- **Reason 2（"subject to activation"）是承重结构**: 把 Stakes 论证直接转化为"时间动态贡献"的许可证——构念可被 trait-relevant cues 激活，所以"同一个构念为何会产生不同行为/为何行为随时间变化"才值得研究
- **"First...Second..." 显式编号**与变体 A 结构一致，但论证域完全不同（construct-property 域）——检索时按论证域区分，勿与 A 的 harm/mechanism 域混淆
- **承接构念引入型 Tension**: "Thus, understanding how..." 常直接衔接 trait-valence 不对称缺口（`01-despite-progress-unaddressed` 变体 AG）或任何构念引入型 Incompleteness 缺口

**适用**: theory-first AMJ/ASQ/OS 论文，贡献为机制 + 个体内动态；构念的理论重要性来自其内在属性（同时影响认知与行动 + 可被激活）

**禁忌**: 当领域期待量化/实践性 stakes（危机、伤害、市值类论文）时不要使用；Reason 2 必须真正构念专属（不能是泛泛的 "traits interact with situations"）

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| JM | ⭐⭐⭐⭐⭐ | 结构化论证风格适配 |
| AMJ | ⭐⭐⭐⭐☆ | 可用但通常与理论 Stakes 混合 |
| SMJ | ⭐⭐⭐⭐☆ | 适合 multi-stakeholder 主题 |
| ASQ | ⭐⭐⭐☆☆ | 偏好更 narrative 而非 enumerate 的 Stakes 风格 |
