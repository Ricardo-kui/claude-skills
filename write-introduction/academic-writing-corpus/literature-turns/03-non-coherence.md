---
type: canonical_reference
canonical_id: "03-non-coherence"
status: ✓ STANDARD
gap_type: Incommensurability
cross_paper: VERIFIED
generativity: GENERATIVE
exclusivity: HIGH
source_papers:
  - zhou2017 (ASQ, 2017): "Institutional vs efficiency logics: competing predictions"
  - keeves2017 (ASQ, 2017): "Asymmetry: ingratiation benefits but backfires"
  - pontikes2012 (ASQ, 2012): "Category spanning: positive or negative?"
  - kundro2023 (AMJ, 2023): "Power protects vs gender role theory"
  - vidal_mitchell2015 (OS, 2015): "nested evidence synthesis: majority pattern plus exceptions for levels, followed by opposing findings for changes"
  - bendig_hensellek_schulte2024 (ETP, 2024): "benefit-oriented outcome consensus is reopened through product-safety harm, then resolved by a cost-learning dominance schedule"
  - lee_park2024 (SMJ, 2024): "positive and negative failure-learning accounts are steelmanned symmetrically, treated as coexisting, and reconciled through an accumulation-dependent dominance schedule"
created: 2026-05-19
updated: 2026-08-04
source: Extracted from literature-turn-templates.md + MVP30 validation
---

# 03-non-coherence — Non-Coherence 冲突式文献对话

## 功能描述

P2-P3 的功能：呈现两个或多个理论/文献流的不兼容性，它们各自都有支持证据，但推出相反预测。核心逻辑是"这两个理论不能同时正确——除非我们重新理解这个现象。"

这是 **Incommensurability** Gap 的 Conversation 策略。

## 适用场景

- Gap 类型 = **Incommensurability**（不同理论推出不兼容解释）
- 需要展示真实的理论分歧（不是稻草人）
- 目标期刊接受理论辩论（ASQ, ASR, SMJ, AMJ）
- 研究旨在整合、调和或替代现有理论

## 验证状态

### 跨论文复现
- **VERIFIED** (≥4 papers): zhou2017 (ASQ), keeves2017 (ASQ), pontikes2012 (ASQ), kundro2023 (AMJ)

### 生成力
- **GENERATIVE**: 理论对立结构在整合型论文中高度可迁移

### 排他性
- **HIGH**: 几乎只在 Incommensurability 中出现；在 Incompleteness 中使用会造成能量不匹配

---

## 句法模板

### 变体 A：理论对立型（zhou2017 型）

**模板**:
> "A long-standing debate in [field] centers on two perspectives: [view A], which emphasizes [focus A], and [view B], which focuses on [focus B]. These perspectives offer incompatible predictions about [outcome]. [View A] predicts [prediction A], while [view B] suggests [prediction B]. Resolving this tension requires [our approach]."

**来源**: zhou2017 (ASQ), adapted

**原文锚定**:
> "According to the conventional, efficiency-based economic view, mostly rooted in agency theory, state ownership plays a minor role in spurring firms' innovation and performance. ... According to this view, SOEs should gradually lose their innovativeness and competitiveness over time. In reality, however, many SOEs in emerging economies have evolved into dynamic dynamos, rather than the predicted dying dinosaurs (Ralston et al., 2006; Musacchio and Lazzarini, 2014; Stan, Peng, and Bruton, 2014). An institutional perspective helps to explain this growth. ... Because SOEs have access to policy information, government support, and valuable resources (Chen et al., 2014; Musacchio and Lazzarini, 2014), these advantages presumably could foster innovation."

（修正说明：原锚定 "Understanding how state ownership affects firm innovation is critical because..." 为合成句且两逻辑立场与原文相反；已替换为原文 P2–P3 逐字句。）

**关键特征**:
- "A long-standing debate" → 承认分歧的历史深度
- "offer incompatible predictions" → 明确不兼容性
- 每个理论都有具体的预测内容（不能只说"观点不同"）
- "Resolving this tension requires" → 自然引出研究方案

**完整架构（zhou2017 双层 non-coherence + facet-decomposition 解析）**:
zhou2017 的 non-coherence 实为**双层叠加**，是其文献对话的高质量所在：
1. **理论层对立**——效率逻辑（agency theory：state ownership → 创新 decline）vs 制度逻辑（政府控制稀缺资源 → SOE 获资源 → foster innovation），两理论对同一 outcome 推出相反预测。
2. **实证层不和**——"empirical evidence is **mixed**"：三类研究分别报告 negative（Jefferson/Xu/Guan；Ayyagari 47 国）/ positive（Li & Xia；Choi Lee Williams）/ null（Choi Park Hong 韩国）。用三方向（正/负/无）的具体研究枚举，把"理论对立"落到"实证也不和"的双重 discord。
3. **现实反证（prediction-vs-reality）**——效率逻辑预测 SOEs 是"dying dinosaurs"，现实却是"dynamic dynamos"（中国 106 家 Fortune Global 500，2/3 为 SOE）。一句 vivid 对偶把理论预测与现实事实对立。
4. **Facet-decomposition 解析（resolution）**——"To resolve the theoretical and empirical inconsistencies, we theorize that the [两逻辑] pertain to **different facets** of [现象]: [逻辑 A = resource allocation/input], [逻辑 B = resource utilization/efficiency]." 即两理论都"对"，但各管一个 sub-facet；整合两 facet 推出**倒 U**（minority state ownership 最优）。

**可迁移核心**：当两理论给出不兼容预测且实证 mixed，不要选边站或宣布一方错——而是**分解到不同 facet**（allocation vs utilization；selection vs influence；motivation vs ability），让两理论各管一 facet，再整合（常产生非单调整体关系）。这是 Non-Coherence × Incommensurability 的"整合式 resolution"，区别于"替换式 resolution"（宣布一方错、用新理论替代）。配套 write-theory：dual-logic integration（H1a 输入 + H1b 效率 → H1c 倒 U）见 `hypothesis_derivation_patterns.md`。

---

### 变体 B：非对称关系型（keeves2017 型）

**模板**:
> "Although extant theory and research has yielded considerable insight and convincing evidence on [topic], it has focused almost entirely on [one direction/one level/one actor]. The [related literature] has provided compelling evidence, however, that [asymmetry insight]. Scholars have devoted little theoretical or empirical attention to understanding how [phenomenon] may operate in [the opposite direction/at a different level/through a different mechanism]."

**来源**: keeves2017 (ASQ), P2

**关键特征**:
- 先承认已有文献的洞察力和证据
- "focused almost entirely on" → 指出方向性偏见
- "provided compelling evidence, however, that" → 用转折引入对立证据
- 暗示需要双向/多层次/多机制的视角

---

### 变体 C：元分析冲突型（gamache2023 型）

**模板**:
> "According to the conventional view, [general prediction]. This assumption has been supported by [meta-analysis/large-scale study] showing that [summary finding] ([citation]). However, a closer look reveals [counter-evidence]. [Specific case 1] ([citation]). [Specific case 2] ([citation]). These observations raise a puzzle: why do [actors] [counter-intuitive behavior]?"

**来源**: gamache2023 (SMJ), adapted

**关键特征**:
- "According to the conventional view" → 先建立共识
- 用元分析/大规模研究支撑共识
- "However, a closer look reveals" → 用具体反例打破共识
- "raise a puzzle" → 将矛盾转化为研究问题

**适用**: 挑战元分析共识的研究

---

### 变体 D：多数结论—例外—相反结果的嵌套综合型（Vidal & Mitchell 型）

**模板**:
> "Prior research has addressed [phenomenon] from two related vantage points. Work on [dimension A] most commonly finds [dominant relationship], while also documenting [named exceptions]. A smaller stream examines [dimension B], where the evidence is more varied: [finding one] contrasts with [finding two]. Taken together, the literature establishes that [shared baseline], but it does not support a single directional account of [focal relationship]."

**来源**: Vidal & Mitchell (Organization Science, 2015), Introduction P1

**原文锚定（释义）**:
> 文献对话先给主流结论，再主动承认例外，之后切换到规模较小但结果更分散的第二条研究线，最后把两条线压缩成一个方向性冲突。

**关键特征**:
- 每条引文都承担分类功能：支持多数模式、标记例外或代表相反方向，而非按作者逐篇摘要。
- “较小研究流”不是 Gap 本身；它的作用是提供足以破坏单一方向解释的证据。
- 先建立前人研究已经知道什么，再精确指出这些知识为何无法共同组成一个连贯解释。

**适用**: 前人研究结论矛盾型 Gap；尤其适合存在“主流关系 + 例外”以及另一条“方向混合”研究线的情形。

**禁忌**: 不要把样本、指标或情境完全不同的系数机械放在一起；必须先证明这些研究确实在回答可比较的问题。

---

### 变体 E：高阶后果冲突 → 固定关系机制裁决型（Bendig–Hensellek–Schulte 型）

**验证状态**: EMERGING（单篇来源；仅作 `section_variant`；Incommensurability R3-primary / R2-secondary）

**功能节拍**: 正向结果空间建共识 → 执行成本/暗面证据 → 上卷为高阶后果族（R2）→ 固定 X–adverse Y → 成本—学习主导权预告（R3）

**模板**:
> "Research commonly evaluates [strategic activity] through [financial/innovation outcomes], emphasizing gains from [resources and learning]. Yet the same activity requires [search, coordination, and integration], which can disrupt [core operations] and produce [high-stakes adverse outcome]. These findings do not merely add another dependent variable; they reveal that the broader consequences of [activity] include both benefits and harms. We therefore introduce [adverse Y] into the outcome family and theorize, for the fixed relationship between [activity intensity] and [adverse Y], how [cost mechanism] dominates initially while [learning mechanism] becomes stronger after experience accumulates."

**来源**: Bendig, Hensellek, and Schulte (2024), *Entrepreneurship Theory and Practice*

**原文锚定**（仅溯源，勿作生成句）:
> CVC/alliance 文献偏财务价值与专利 → 执行成本与整合负担 → 产品召回作为有意义不利后果 → RBV+learning 下成本先占优、学习后占优的倒 U 预告。

**两级结构**:
1. **R2 让冲突可见**：先把财务价值、创新产出与产品安全上卷为“对母公司及利益相关者的后果”这一可辩护高阶结果族。
2. **R3 让冲突可检验**：进入理论裁决后，锁定同一 X、同一 Y 和同一时间单位，规定成本与学习收益如何沿 X 改变相对主导权。

**为什么不同于变体 D**:
- 变体 D 在同一经验关系内整理多数模式、例外与相反方向，再按 X 方向或行动形式分解。
- 本变体先揭示既有结果空间偏向正向绩效，再以高风险 Y 暴露净评价冲突，最后在新的固定 X→Y 关系中完成机制裁决。

**适用**: 研究领域习惯以财务、创新或增长结果评价某战略“有益”，但已有可靠证据显示该战略还可能产生运营、产品安全、员工或社会伤害；作者能够证明这些结果属于同一高阶有效性/利益相关者后果判断。

**禁忌**:
- 新旧 Y 之间必须有明确高阶家族，不得把概念无关的结果拼成“矛盾”。
- 高阶 R2 只负责建立问题；具体预测仍须固定 X/Y，不能直接比较不同模型中的不可比系数。
- 两个相反机制只有在相对强度随 X、时间或状态系统变化时，才足以预告 U/倒 U。
- 模板保持功能节拍+placeholder；勿贴源论文长段或专有交易类型名作生成句。

---

### 变体 F：侵占威胁 → 平均优势 → 制衡追问型（Anderson–Reeb 型，EMERGING）

**模板**:
> "Evidence on [concentrated control arrangement] documents the risk of [appropriation/entrenchment harm]. Yet the same arrangement is widespread and, on average, associated with [performance advantage], partly because it enables [monitoring/commitment benefit]. This coexistence raises a sharper question: what governance arrangement preserves [benefit] while constraining [harm]? We therefore shift attention from [conventional conflict dyad] to [controlling-owner–outside-claimant conflict] and examine how the relative representation of [actor A] and [actor B] determines which mechanism dominates."

**来源**: Anderson and Reeb (2004), *Administrative Science Quarterly*

**关键动作**:
1. **先让伤害可信**：以理论和可核查事实建立控制权转化为私人收益的风险。
2. **完整承认平均优势**：不把既有正向结果写成错误，而是说明其监督、承诺和专用知识基础。
3. **以制衡问题联结两边**：问题不是“到底正还是负”，而是什么结构能保留收益并抑制伤害。
4. **重画冲突对象**：从管理者—股东冲突转向控制股东—外部股东冲突。
5. **进入 R3 才固定关系**：将 X 锁定为两类董事的相对配置，将 Y 锁定为企业价值，再推导机制优势切换。

**为什么不同于变体 E**:
- 变体 E 从被忽视的负向 Y 扩展高阶结果族，再在新的 X→Y 关系内裁决成本与学习机制。
- 本变体不靠增加 Y 制造张力，而是把同一组织形式的平均优势分解为不同治理配置，并将“谁来制衡”设为理论问题。

**适用**: 既有研究一方面记录集中控制、创始人权力或强势行动者的监督/承诺收益，另一方面有可比较的侵占、固化或利益相关者伤害证据；研究能提出维持收益所需的制衡配置。

**禁忌**: 不要仅凭正面平均系数与几个负面案例宣称矛盾；必须证明双方回答同一个价值后果问题，并在正式推理中固定具体 X、Y、层级、时间范围和 estimand。

---

### 变体 G：对称双流 → 共存声明 → 累积轴裁决型（Lee–Park 型，EMERGING）

**模板**:
> "One stream shows that [repeated experience] improves [outcome] because it expands [enabling process]. A second stream shows that the same experience can impair [outcome] because it erodes [constraining prerequisite]. Both accounts are theoretically credible and address the same focal relation. Rather than asking which account is universally correct, we ask how the two processes coexist and change in relative strength as [experience] accumulates."

**来源**: Lee and Park (2024), *Strategic Management Journal*, Introduction P1–P4.

**关键特征**:
- 两个文献流按“发现 → 机制”完全对称展开，先让双方都达到最强版本，再谈整合。
- Departure point 不是笼统的 `findings are mixed`，而是指出单一方向理论无法表示两个过程会同时发生。
- 用累计暴露轴替代简单选边：理论任务变成说明哪个过程在哪个区间成为约束性短板。
- Stakes 被嵌入共存声明：在失败反复出现且后果严重的情境中，误判主导过程会直接误判学习轨迹。

**适用**: 同一个 X–Y 关系存在方向相反、证据充分的过程解释；X 可累积、分阶段或沿连续区间变化；研究能够给出机制相对强度如何变化的理论依据。

**禁忌**: 不要仅凭正负研究并存就推导曲线；必须固定同一 X、Y、层级与时间范围，并说明两个过程为何会共存、为何其相对强度会随 X 系统变化。

---

## 组装规则

### 默认配对（对角线，能量匹配）
- **与 `06-paradigm-challenge` (Hook) 配对**: 高能量 Hook 匹配高能量 Conversation
- **与 `04-reality-contradicts-consensus` (Tension) 配对**: Non-Coherence 是此 Tension 的标准 Conversation 策略

### 非默认组合（非对角合法/可疑，不由 Gap 类型反推）
> Coherence × Problematization 是 3×3 设计空间，对角线只是默认；完整矩阵见 `literature-turns/_index.md` 顶部 3×3 速查表与 `diagnose-introduction/references/intertextual-construction-playbook.md` §2。

- **Non-Coherence × Inadequacy（合法非对角·调停型）**: 两个阵营各自部分正确，本研究通过澄清边界条件裁决分歧（Hirsch & Lounsbury 1997；常配 write-theory 竞争假设型）。需有真正的裁决依据，不可和稀泥。
- **Non-Coherence × Incompleteness（可疑组合·先重新诊断）**: 文献既在冲突，"还有更多可知道"会 undersell 张力——通常应重诊为 Non-Coherence × Inadequacy。唯一例外：冲突被承认，但某一具体机制确实未被检视。

### 反模式提醒
- **不要制造稻草人**: 两个理论都必须有真实文献支撑
- **不要只说"观点不同"**: 必须具体到"预测相反"——一个说 X→Y 正相关，另一个说 X→Y 负相关
- **不要用情绪代替证据**: "Scholars have ignored..." → 改为 "Scholars have devoted little attention to..."

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| ASQ | ⭐⭐⭐⭐⭐ | 理论整合和 facet 分解是 ASQ 的核心偏好 |
| ASR | ⭐⭐⭐⭐⭐ | 经典理论对话是必备 |
| SMJ | ⭐⭐⭐⭐⭐ | 需要具体数字和案例支撑反例 |
| AMJ | ⭐⭐⭐⭐☆ | 机制链必须清晰 |
| OS | ⭐⭐⭐☆☆ | 可用，但需要更强的制度逻辑支撑 |
| JM/JMR | ⭐⭐☆☆☆ | 不典型；营销期刊偏好数据开场 |

---

## 相关语料

- 配合 `hooks/06-paradigm-challenge.md` 使用：高能量 Hook 匹配高能量 Conversation
- 配合 `tensions/04-reality-contradicts-consensus.md` 使用：默认配对（对角线；非对角合法组合见本文件"非默认组合"小节与 `_index.md` 3×3 速查表）
- 配合 `contributions/_index.md` 中的 Makadok 维度使用：Incommensurability 通常涉及 Constructs 或 Mechanism 贡献
