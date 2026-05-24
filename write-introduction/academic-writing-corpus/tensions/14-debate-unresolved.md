---
type: canonical_tension
canonical_id: "14-debate-unresolved"
status: ✓ STANDARD
gap_type: Inadequacy
cross_paper: VERIFIED
generativity: GENERATIVE
exclusivity: MEDIUM
source_papers:
  - kundro_rothbard (AMJ, 2020+): "debate on whether power protects women: one hand power frees, other hand gender role violations persist"
  - eilert2017 (JM, 2017): "How does the relationship vary..." (rhetorical question tension)
  - wowak2025 (MS, 2025): "liberal vs conservative CEO recall behavior — conflicting predictions"
created: 2026-05-24
source: Distilled from Kundro & Rothbard (AMJ), Eilert et al. (JM), Wowak et al. (MS)
---

# 14-debate-unresolved — 文献辩论未决 Tension

## 功能描述

在 Gap 段揭示同一领域内文献发现的系统性矛盾或理论辩论，指出现有研究尚未调和这些对立发现。这是 **Inadequacy** 问题化的核心 Tension 变体：不是"文献有缺口"，而是"文献存在对立结论但缺乏整合框架"。

## 适用场景

- Gap 类型 = **Inadequacy**（现有文献视角不完整，无法解释矛盾发现）
- 同一主题下存在两个对立的经验发现或理论预测
- 目标是用新理论框架调和/解释这些矛盾
- 常见于性别研究、领导力、组织行为等领域

## 验证状态

### 跨论文复现
- **VERIFIED** (≥3 papers): AMJ (kundro_rothbard), JM (eilert2017), MS (wowak2025)
- 跨越 OB、营销、战略领域

### 生成力
- **GENERATIVE**: "On the one hand... On the other hand..." 模板高度可迁移

### 排他性
- **MEDIUM**: 可在 Inadequacy 和 Incommensurability 中出现，但前者更常见

---

## 句法模板

### 变体 A：对立发现对称呈现型（kundro_rothbard 型）

**模板**:
> "Yet, it remains to be seen whether [IV] protects [group A] in the same way as it protects [group B] in the context of [behavior]. Indeed, within the [field] literature, there is a debate on whether or not [IV] will mitigate [negative outcome] against [group A]. On the one hand, emerging research has corroborated the suggestion that [IV] will protect [group A] from [outcome] in certain contexts ([citations]) because [mechanism A]. On the other hand, extant research on [theory B] has questioned whether [group A] benefit from [IV] in the same way [group B] do and suggests they may be viewed as [negative attribute] ([citations]) and still face [negative outcome] ([citations]). This debate has large societal implications too, particularly as [trend]. Indeed, [group A] may find themselves in a double bind ([citation]) where they are simultaneously expected to engage in [behavior] and also penalized for doing so."

**来源**: kundro_rothbard (AMJ), P2

**原文锚定**:
> "Yet, it remains to be seen whether power protects women in the same way as it protects men in the context of moral objection. Indeed, within the gender and power literature, there is a debate on whether or not power will mitigate backlash against women. On the one hand, emerging research has corroborated the suggestion that power will protect women from retaliation in certain contexts... because it frees women from constraining role expectations. On the other hand, extant research on gender role theory has questioned whether women benefit from power in the same way men do and suggests they may be viewed as lower in self-control... and still face retaliation... This debate has large societal implications too, particularly as women continue to move into higher-power positions in organizations. Indeed, women may find themselves in a double bind where they are simultaneously expected to engage in moral objection and also penalized for doing so."

**关键特征**:
- "it remains to be seen whether..." → Inadequacy 标志性开场（暗示现有知识不足）
- "there is a debate on whether or not..." → 明确标注文献分歧
- "On the one hand... On the other hand..." → 对称结构呈现对立发现
- 两方都引用具体文献（避免选择性呈现）
- "double bind" → 用理论概念升级 Stakes

---

### 变体 B：竞争机制预言型（wowak2025 型）

**模板**:
> "However, the literatures on [领域A] and [领域B] offer potentially conflicting arguments as to the influence of [X] on [Y]. On the one hand, [X_high] may [increase/decrease] [Y] because [mechanism_A]. Research suggests that [X_high] are more [特征] and, correspondingly, [行为] ([文献]). In other words, this research argues that [X_high] tend to [行为2]. On the other hand, [X_low] may [increase/decrease] [Y] because [mechanism_B]. Indeed, research indicates that [结果] can be particularly [后果], so [X_low] who tend to focus on [价值] may be more motivated to [行为3] ([文献])."

**来源**: wowak2025 (MS), Theory section

**关键特征**:
- 用两个不同理论/文献流推导相反预测
- 每方都有独立的机制逻辑和文献支撑
- 最后通过实证或额外理论决定哪方成立（或条件化）

---

### 变体 C：修辞问句探索型（eilert2017 型）

**模板**:
> "How does the relationship between [IV] and [DV] vary as a function of [moderator]? [Moderator] is [definition]. [Theoretical justification]. There are [N] reasons why [moderator] should moderate this relationship. [Reason 1]: [Mechanism logic] ([citation]). Consequently, [prediction]. [Reason 2]: [Mechanism logic] ([citation]). Thus, [prediction]."

**来源**: eilert2017 (JM), H2/H3 opening

**关键特征**:
- 用修辞问句直接承接主效应，开启 moderator 论证
- "There are N reasons" 预告多路径
- 适用于假设树型论文中 moderator 的引入

---

## 组装规则

### 必须配对
- **与 `11-overlooked-alternative` (Tension) 配对**: 若辩论的一方是被忽视的替代解释
- **与多理论 Theory Lens 配对**: 辩论型 Tension 通常需要引入新理论框架来调和矛盾
- **与 `E 调节效应型` (Theory Variant) 配对**: 辩论未决型 Tension 在 Theory 部分通常以调节效应型（E 型）来解释条件化差异——"文献发现矛盾是因为忽略了 [moderator]"，而非简单地选边站。参见 `write-theory/corpus/variants/E_moderation.md`。若调节器复杂（三向交互、多层分类），分别使用 E3/E5 子协议。

### 互斥
- **不能与 `01-despite-progress-unaddressed` (Tension) 同用**: 后者是"已有进展但遗漏"，前者是"已有研究但矛盾"
- **与 `04-reality-contradicts-consensus` 的区别**: 后者是理论预测 vs 现实矛盾（Incommensurability），前者是文献内部发现矛盾（Inadequacy）

### 反模式提醒
- **不要只呈现一方证据**: 对称呈现是此 Tension 的核心修辞力量
- **不要以"mixed results"草草了事**: 必须解释为什么结果会矛盾（你的理论框架正是用来解释这个的）
- **避免 generic gap language**: 不要以 "few studies have examined" 结束，要以理论框架需求结束

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| AMJ | ⭐⭐⭐ 极高 | "On the one hand... On the other hand..." 是 AMJ OB 论文标志结构 |
| ASQ | ⭐⭐⭐ 高 | 偏好理论层面的辩论（竞争机制预言型） |
| JM | ⭐⭐⭐ 高 | 修辞问句型最适配 |
| SMJ | ⭐⭐⭐ 中 | 需要更具体的案例/数据支撑辩论双方 |
| OS | ⭐⭐ 中 | 偏好机制解释而非经验发现罗列 |
