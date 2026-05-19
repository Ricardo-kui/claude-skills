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
created: 2026-05-19
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
> "Understanding how state ownership affects firm innovation is critical because institutional theory and efficiency logic offer competing predictions. Institutional theory predicts that state ownership constrains innovation by imposing political goals, whereas efficiency logic suggests state ownership facilitates innovation by providing resources and reducing uncertainty."

**关键特征**:
- "A long-standing debate" → 承认分歧的历史深度
- "offer incompatible predictions" → 明确不兼容性
- 每个理论都有具体的预测内容（不能只说"观点不同"）
- "Resolving this tension requires" → 自然引出研究方案

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

## 组装规则

### 必须配对
- **与 `06-paradigm-challenge` (Hook) 配对**: 高能量 Hook 匹配高能量 Conversation
- **与 `04-reality-contradicts-consensus` (Tension) 配对**: Non-Coherence 是此 Tension 的标准 Conversation 策略

### 互斥
- **不能与 `01-despite-progress-unaddressed` (Tension) 同用**: 能量不匹配（高 vs 低）
- **不能在 Incompleteness 中使用**: Non-Coherence 的"理论冲突"逻辑与 Incompleteness 的"遗漏"逻辑矛盾

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
- 配合 `tensions/04-reality-contradicts-consensus.md` 使用：必须配对
- 配合 `contributions/_index.md` 中的 Makadok 维度使用：Incommensurability 通常涉及 Constructs 或 Mechanism 贡献