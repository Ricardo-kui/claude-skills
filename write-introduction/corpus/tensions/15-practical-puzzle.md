---
type: canonical_tension
canonical_id: "15-practical-puzzle"
status: ✓ STANDARD
gap_type: Inadequacy
cross_paper: VERIFIED
generativity: GENERATIVE
exclusivity: MEDIUM
source_papers:
  - shen_zhou_wang_zhang (JOM, 202X): "conventional wisdom that political ties help vs recent research on downsides → practical puzzle"
  - eilert2017 (JM, 2017): "practitioners believe severity → quick recall, but delays happen → puzzle"
created: 2026-05-24
source: Distilled from Shen et al. (JOM)
---

# 15-practical-puzzle — 实践谜题 Tension

## 功能描述

在 Gap 段呈现实践领域中的传统智慧/常识信念与新兴研究发现之间的矛盾，将这种矛盾升级为"实践谜题"（practical puzzle），并以具体的实践问题列表导出 Stakes。这是 **Inadequacy** 问题化的一种变体：现有文献未能解释为什么实践者的信念与研究发现不一致。

## 适用场景

- Gap 类型 = **Inadequacy**（现有研究未能调和实践信念与研究发现）
- 目标期刊为 **OM/SCM/管理实践导向**的期刊（JOM, POMS, IJOPM, SMJ）
- 研究领域存在强烈的"传统智慧"或行业惯例
- 新近研究发现了与常识相反的效果/代价

## 验证状态

### 跨论文复现
- **VERIFIED** (≥2 papers): JOM (shen_zhou_wang_zhang), JM (eilert2017)
- 常见于运营管理、营销、战略领域

### 生成力
- **GENERATIVE**: "widely believed among practitioners... However... Such contradiction leads to a practical puzzle" 模板可高度适配

### 排他性
- **MEDIUM**: 可在 Inadequacy 和部分 Phenomenon-driven 研究中出现

---

## 句法模板

### 变体 A：传统智慧 vs 新发现 downside 型（shen_zhou_wang_zhang 型）

**模板**:
> "The question merits managerial attention because in [context], it is widely believed among practitioners that [conventional wisdom] ([citations]). However, recent research has explored their downsides, suggesting that [downside 1], [downside 2], and [downside 3] ([citations]). Such contradiction leads to a practical puzzle: should practitioners follow conventional wisdom by [action]? This puzzle suggests [N] real-world problems for [field]: (1) Do [IV] facilitate [DV]? (2) Under what conditions should firms be especially cautious about [action]? and (3) What strategies can firms take as remedies for the downsides of [IV]? These important practical questions motivate us to examine the role of [IV] in [field]."

**来源**: shen_zhou_wang_zhang (JOM), P2

**原文锚定**:
> "The question merits managerial attention because in emerging economies, it is widely believed among practitioners that political ties are necessary for achieving superior performance. However, recent research has explored their downsides, suggesting that political ties may oblige firms to carry political water, subject them to politicians' rent seeking, and make them vulnerable when a politician falls out of favor. Such contradiction leads to a practical puzzle: should practitioners follow conventional wisdom by pursuing political ties when operating in emerging economies? This puzzle suggests three real-world problems for operations management: (1) Do political ties facilitate operational efficiency? (2) Under what conditions should firms be especially cautious about establishing political ties? and (3) What strategies can firms take as remedies for the downsides of political ties? These important practical questions motivate us to examine the role of political ties in operations management."

**关键特征**:
- "widely believed among practitioners" → 建立传统智慧的实践基础
- "However, recent research has explored their downsides" → 引入学术反证
- 三个 downside 并列（结构：动词短语, 动词短语, and 动词短语）
- "Such contradiction leads to a practical puzzle" → **核心过渡句**，将矛盾升级为谜题
- 反问句 "should practitioners follow conventional wisdom by...?" → 强化谜题的实践紧迫性
- [N] 个具体问题，每个问题对应论文的一个核心目标
- "These important practical questions motivate us to examine..." → 以实践动机收束

---

### 变体 B：政策悖论型（eilert2017 型）

**模板**:
> "[Phenomenon] affects [stakeholder outcome] and expose [actors] to [risk list]. Consequently, [intervention] are often [action] to limit damage. In [context], [agency] reported [trend data]. In [specific industry], [scope magnitude]. The decision of whether and when to [act] is not a simple one. [Actions] are costly; [cost list]. Thus, [actor] has reasons to avoid quick response. However, delaying [action] may lead to [higher costs] through [cost mechanisms]. Therefore, although [events] are adverse, quick response may attenuate damage."

**来源**: eilert2017 (JM), P1-P3

**关键特征**:
- 从现象成本出发，建立"行动昂贵但不行动更昂贵"的悖论
- 以"The decision... is not a simple one"开启谜题
- 适用于政策/决策导向型论文

---

## 组装规则

### 必须配对
- **与 `hook-cold-start` 配对**: 实践谜题需要先有现象/构念建立
- **与 Preview 中的干预/策略配对**: 实践问题 (3) 必须在 Preview/Contribution 中有对应的策略答案
- **与 `E 调节效应型` (Theory Variant) 配对**: 实践谜题型 Tension 在 Theory 部分通常以调节效应型（E 型）来解释"在什么条件下传统智慧成立/失效"。若谜题涉及多个边界条件（如环境层+组织层），使用 E5 多层调节器分类协议。参见 `write-theory/corpus/variants/E_moderation.md`。

### 互斥
- **不能与 `01-despite-progress-unaddressed` (Tension) 同用**: 后者是"文献有进展但遗漏"，前者是"实践信念与研究发现矛盾"
- **与 `14-debate-unresolved` 的区别**: 后者是文献内部的对立发现（On the one hand... On the other hand...），前者是实践信念 vs 学术发现的矛盾

### 反模式提醒
- ** downside 必须是研究发现，而非作者臆测**: 每个 downside 都需要引用文献
- **问题列表必须对应论文结构**: (1) 对应主效应假设, (2) 对应边界条件假设, (3) 对应缓解策略/干预假设
- **不要过度使用 "practical puzzle"**: JOM 偏好实践导向，但 AMJ/ASQ 可能认为过于实务化而缺乏理论深度

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| JOM | ⭐⭐⭐ 极高 | JOM 明确偏好实践谜题型开场 |
| POMS | ⭐⭐⭐ 高 | 适用于运营管理实践导向研究 |
| SMJ | ⭐⭐⭐ 中 | 需将实践谜题与理论缺口更紧密结合 |
| AMJ | ⭐⭐ 中 | AMJ 接受但需补充理论 Stakes（"so what for theory?"） |
| ASQ | ⭐⭐ 低 | ASQ 偏好理论谜题而非实践谜题 |

---

## 变体扩展

### 变体 C：成本-收益悖论型

当论文的核心张力是"某种策略既有明显收益又有隐性成本"时：

> "While [strategy] provides [benefit] that help firms [outcome], it also imposes [cost] that may [negative consequence]. This creates a paradox for [actors]: should they [action A] at the risk of [cost], or [action B] at the risk of [alternative cost]? We suggest that the answer depends on [contingency]."

**适用**: 任何涉及权衡（trade-off）的策略研究
