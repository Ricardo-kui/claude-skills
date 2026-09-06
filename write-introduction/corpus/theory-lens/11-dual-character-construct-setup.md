---
type: canonical_theory_lens
canonical_id: "11-dual-character-construct-setup"
status: ✓ STANDARD
gap_type: Incompleteness
cross_paper: EMERGING (1 paper)
generativity: GENERATIVE
exclusivity: HIGH
source_papers:
  - desjardine_li_shi_2025_amj (AMJ, 2025): "rating agencies 权威面（trusted authorities 塑造利益相关者态度）+ 利益面（own economic agendas 可被杠杆化）双面合取 → 影响可能性"
created: 2026-09-05
source: Distilled from DesJardine, Li & Shi (AMJ) Introduction P3（2026-09-05 整篇重蒸馏 gate ① create_new_file 改判，自 theory-lens/09 变体 B 升格独立模块）
---

# 11-dual-character-construct-setup — 构念双面性装置引入型 Theory Lens

## 功能描述

在 Theory Lens 段落引入一个**核心构念**，方法是把该构念的**双面性**（dual character）各自供弹药：权威面（为什么它重要——能塑造利益相关者态度/结果）+ 利益面（为什么它可被利用——自身有 interests/incentives，可被外部玩家杠杆化）。两面**合取**才能推出理论杠杆（影响的可能性），从而把构念介绍直接焊到下一段的理论声明上。与 09-construct-contrast-introduction（靠同家族旧构念对照获得合法性）判别：本模块靠构念自身双面性获得"既重要又可被杠杆化"的合法性，适用于以构念为**工具**（instrument）而非仅为解释视角的理论。

## 适用场景

- 贡献维度 = **Constructs**，且核心理论动作是"某类行动者可杠杆化该构念"
- 构念对读者**半熟**（无需轶事教学，但不能默认其可影响性）
- 典型对象：信息中介 / 评估机构 / 看门人（rating agencies、news outlets、review aggregators 等引语定义+范例三元组可一段完成的构念）
- Incompleteness × Constructs 组合

## 验证状态

### 跨论文复现

- EMERGING（1 源）：desjardine_li_shi_2025_amj（AMJ 2025）。待第二篇 multi-audience / intermediary 杠杆化论文交叉后升 VERIFIED。

### 生成力

- 双面性框架可拆出句级模板（引语定义+范例三元组+两面合取+"raising the possibility"桥接句），可迁移到任何"被杠杆化的中介构念"。

### 排他性

- HIGH：与构念对照（09）、跨学科导入（10）动作类型不同——本模块的合法性来源是构念的**利益面**，不依赖旧构念对照或源学科教学。

## 句法模板

### 变体 A：构念双面性装置引入型（desjardine_li_shi_2025_amj 型）

**模板**:
> "[Construct] are '[quoted definition]' ([citation]), including [exemplar 1], [exemplar 2], and [exemplar 3]. Because they are seen as [authority property], [construct] are known to [consequence-power: shape stakeholder responses] ([citation]). At the same time, because these [construct] have their own [interests/incentives] ([citation]), they can be subject to outside influence, raising the possibility that [players] may try to leverage them to advance their own [agendas]."

**来源**: desjardine_li_shi_2025_amj (AMJ), P3

**原文锚定**:
> "At the same time, because these intermediaries have their own economic agendas and incentives, they can be subject to outside influence, raising the possibility that some players may try to leverage these intermediaries to advance their own competitive agendas."

**关键特征**:
- 双面性装置：一个构念的两面各自供弹药——权威面（trusted authorities → 能塑造利益相关者态度，给"重要"）+ 利益面（own economic agendas → 可被外部影响，给"可利用"）；两面合取才能推出理论杠杆（影响的可能性）
- 可能性证明桥接句（"raising the possibility that..."）把构念介绍直接焊到下一段理论声明（"Against this backdrop, we develop a theory of..."），使 P3 不是背景板而是理论的前件
- 引语定义+范例三元组（rating agencies / news outlets / review aggregators）在一段内完成构念操作化，成本低于轶事教学路线
- 与 09-construct-contrast（变体 A）的区别：那边靠同家族旧构念对照获得合法性、价值锚定在旧构念失效的 scope condition；本变体靠构念自身双面性获得"既重要又可被杠杆化"的合法性，适用于以构念为工具（instrument）而非仅为解释视角的理论

**适用**: Constructs 贡献且核心理论动作是"某类行动者可杠杆化该构念"的研究；构念对读者半熟（无需轶事教学，但不能默认其可影响性）；Incompleteness × Constructs

**禁忌**: 两面必须缺一不可且各带引文支撑——只写权威面会退化成普通背景介绍，只写利益面则构念重要性悬空；"raising the possibility" 后必须紧跟理论声明，若下一段转去综述文献则桥接失效

<!-- wb:desjardine_2025_information_based_competition_the_case_of_ri:theory_lens_dual_character_construct_setup_desjardine2025 -->

## 与其他 Theory Lens 的区别

- vs **09-construct-contrast-introduction**：09 靠新旧构念对照（同家族、真实差异）获得合法性；本模块靠构念自身双面性（权威面+利益面合取）获得合法性——无需旧构念参照系
- vs **10-cross-discipline-construct-import**：10 教学式导入读者不认识的源学科构念；本模块默认构念半熟，只补"可影响性"这一面

## 组装规则

### 必须配对

- 后接理论声明段（"Against this backdrop, we develop a theory of..."）——桥接句不能悬空
- Theory 段须操作化利益面（谁有权衡/激励去杠杆化该构念），否则 P3 的可能性只是修辞

### 反模式提醒

- 只写权威面 = 普通 background（构念重要性已有文献背书时不构成 lens）
- 两面各写一段但无合取推理 → "important but irrelevant"
- 范例三元组超过一段 → 退化为构念综述
