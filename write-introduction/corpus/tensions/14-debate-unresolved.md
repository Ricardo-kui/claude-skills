---
type: canonical_tension
canonical_id: "14-debate-unresolved"
status: ✓ STANDARD
gap_type: Inadequacy
cross_paper: VERIFIED
generativity: GENERATIVE
exclusivity: MEDIUM
source_papers:
  - 'kundro_rothbard (AMJ, 2020+): debate on whether power protects women—one hand power frees, other hand gender role violations persist'
  - 'eilert2017 (JM, 2017): How does the relationship vary... (rhetorical question tension)'
  - 'wowak2025 (MS, 2025): liberal vs conservative CEO recall behavior—conflicting predictions'
  - 'lee_wu_bednar_orsc_18968 (Organization Science): one local institution loses oversight and visibility simultaneously, creating opposing CSR incentives resolved by substitute intermediaries'
created: 2026-05-24
updated: 2026-08-02
source: Distilled from Kundro & Rothbard (AMJ), Eilert et al. (JM), Wowak et al. (MS), and Lee, Wu & Bednar (Organization Science)
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
<!-- retrieval-move:
{
  "functions": [
    "intro.gap_conflicting_accounts"
  ],
  "definitions": [
    {
      "id": "intro.gap_conflicting_accounts",
      "label": "揭示既有解释相互矛盾",
      "section": "introduction",
      "refines": "intro.literature_to_gap",
      "definition": "把针对同一焦点关系的两套既有解释及其不同预测并置，说明分歧为何尚不能由现有对话解决。",
      "use_when": [
        "双方都存在可追溯的论据，且讨论对象、结果和比较条件足以构成同一个问题。",
        "指出分歧落在何处；不同指标或不相容样本产生不同结果时，先核对是否真有解释冲突。"
      ],
      "neighbors": [
        {
          "id": "intro.gap_unexplained",
          "distinction": "缺少解释不等于解释冲突；本动作需要双方实质内容。"
        },
        {
          "id": "theory.competing_predictions",
          "distinction": "Theory 中将对立机制收敛为正式竞争预测；此处先建立文献对话的问题。"
        }
      ],
      "positive_example": {
        "kind": "verbatim",
        "cue": "On the one hand, emerging research has corroborated",
        "why": "同一块先呈现权力解除角色约束的解释，再呈现性别角色理论的反向解释；来源年份仍沿用卡片的待补状态。"
      },
      "mismatch_example": {
        "kind": "illustrative",
        "text": "既有理论预测惩罚会抑制行为，但现实中该行为仍然持续。",
        "why": "只有理论与现象不一致，尚未呈现两套既有解释；应先定位为现象张力。",
        "actual_function": "intro.tension"
      },
      "aliases": [
        "揭示既有解释相互矛盾",
        "既有解释冲突",
        "conflicting prior accounts"
      ],
      "review_cases": []
    }
  ],
  "position": "文献对话的问题化位置，先对称呈现双方解释",
  "prerequisite": "按本块 definitions 的 use_when 核对当前需求与研究事实。",
  "next": "把未解决的分歧接到本文拟回答的问题。",
  "applicability": {
    "required_facts": {
      "comparable_accounts": true
    }
  }
}
-->

**模板**:
> "Yet, it remains to be seen whether [IV] protects [group A] in the same way as it protects [group B] in the context of [behavior]. Indeed, within the [field] literature, there is a debate on whether or not [IV] will mitigate [negative outcome] against [group A]. On the one hand, emerging research has corroborated the suggestion that [IV] will protect [group A] from [outcome] in certain contexts ([citations]) because [mechanism A]. On the other hand, extant research on [theory B] has questioned whether [group A] benefit from [IV] in the same way [group B] do and suggests they may be viewed as [negative attribute] ([citations]) and still face [negative outcome] ([citations]). This debate has large societal implications too, particularly as [trend]. Indeed, [group A] may find themselves in a double bind ([citation]) where they are simultaneously expected to engage in [behavior] and also penalized for doing so."

**来源**: kundro_rothbard (AMJ), P2（待补年份——frontmatter 标 2020+，未定）

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

### 变体 D：竞争假设悖论型（du_tsolmon2024 型）

**模板**:
> "A fundamental tension exists in the literature: although [behavior X] is typically viewed as [negative consequence], so we may expect [rational actor response], studies still find [widespread X persists] ([citations]). This contradiction reflects competing assumptions about [construct]. Some scholars argue that [view A: X is efficient/redundant] ([citations]). Conversely, [theory camp B] emphasize[s] [view B: X is valuable], suggesting [B's implication] ([citations]). [Theoretical escalation: the resource/property at stake]."

**来源**: du_tsolmon2024 (ORSC), P2

**原文锚定**:
> "A fundamental tension exists in the literature: although high postacquisition managerial turnover from target firms is typically viewed as detrimental to M&A performance, so we may expect firms to retain target managers, studies still find large-scale top management departures from target firms after M&A. This contradiction reflects competing assumptions about the value of target managers. Some scholars argue that in related acquisitions, overlapping knowledge makes target managers replaceable, allowing efficiency gains through reducing redundancy. Conversely, the resource-based view (RBV) and strategic human capital (SHC) literatures emphasize the critical knowledge and capabilities these managers possess, suggesting retention advantages for PAI."

**关键特征**:
- 以"理性预期被现实证伪"开场：'so we may expect..., [yet] studies still find'——预期与现实的落差制造认知失调（区别于变体A的"同一 IV 对不同群体差异化效应未检验"、变体B的"两个理论对同一关系相反预测"）
- 悖论归因于"competing assumptions about [construct]"——不是数据矛盾，而是理论假设对立
- 两阵营对称呈现（Some scholars argue... Conversely, [theory camp] emphasize）但各自只给一句机制——克制，不展开
- 末尾用资源属性（non–scale-free resource incurs opportunity costs）升级 stakes——把悖论上升到"错了会怎样"的资源理论层面

**适用**: Inadequacy × Mechanism 组合；当经验现象与"理性预期"系统背离，且文献中存在两个各执一词的理论阵营时。适合 ORSC/SMJ/AMJ 的行为战略与人力资本交叉研究

**禁忌**:
- 两个阵营必须真实存在且可引用——不能把一个观点的推论 strawman 成对立阵营
- 'so we may expect' 的预期必须是读者会自然认同的常识逻辑，否则悖论感失效

<!-- retrieval-move:
{
  "functions": [
    "intro.gap_conflicting_accounts"
  ],
  "function_evidence": {
    "intro.gap_conflicting_accounts": {
      "kind": "verbatim",
      "cue": "This contradiction reflects competing assumptions about the value of target managers",
      "why": "同一人员保留问题上并置知识冗余与关键能力两种解释，说明其预测分歧。"
    }
  },
  "function_support": {
    "intro.gap_conflicting_accounts": "complete"
  },
  "position": "反常现象呈现之后、竞争解释定位处",
  "prerequisite": "两套解释针对可比较的收购情境、行动者及结果。",
  "next": "明确在哪些条件下两种解释可被区分。",
  "advances": "把经验矛盾定位为理论解释的分歧。",
  "next_evidence": [
    "双方解释的原始文献",
    "可比较的情境与结果"
  ],
  "applicability": {
    "required_facts": {
      "competing_accounts_documented": true,
      "comparison_scope_aligned": true
    }
  }
}
-->

---

### 变体 E：单一制度双重功能同时衰退 → 对立激励 → 替代者条件化（Lee–Wu–Bednar 型）

**验证状态**: EMERGING（单篇来源；仅作 `section_variant`）

**模板**:
> "[Institution] historically performs two intertwined functions: [function A] and [function B]. Its decline weakens both simultaneously, but the two losses create opposing incentives for [actor]'s [response]. The erosion of [function A] reduces [pressure/incentive A], whereas the loss of [function B] increases [need/incentive B]. The net response is therefore theoretically ambiguous. We resolve this ambiguity by asking whether [substitute intermediaries] can replace either function: when substitutes remain active, [path A/B] should dominate; when they are absent, [opposing path] should dominate."

**来源**: Lee, Wu, and Bednar, *Organization Science*, DOI 10.1287/orsc.2024.18968, Introduction.

**关键特征**:
- 张力来自**同一制度冲击同时拆除两个耦合功能**，而不是两篇文献各自给出一个互斥预测。
- 每个功能损失必须导向一个可区分、方向相反的行为激励；不能只把“双重功能”写成并列背景。
- 替代性中介不是普通控制变量，而是决定哪条路径占优的条件化装置。
- 贡献落点是 contingent framework：把“平均效应是什么”改写为“在何种信息生态中哪条路径占优”。

**适用**: 地方媒体、监管机构、行业协会、平台或社区组织衰退；同一制度同时承担监督与传播、约束与赋能、认证与可见性等双重功能。

**禁忌**:
- 两个功能若方向相同，不应强行套用本变体。
- 替代者必须能承接至少一个被削弱的功能；仅与冲击相关不构成边界条件。
- Introduction 只能承诺条件化解释，不能在未识别机制时声称替代者“证明”了具体路径。

---


### 变体 F：悖论假设并置型（what_changes_after_women_enter_top_manage_2020 型）

**模板**: Further, a theoretical tension surrounds the mechanisms that scholars invoke to explain [关系]. Some researchers conjecture [机制A] could explain [关联1] ([cites]). Other scholars speculate [机制B] might explain [关联2] ([cites]). These arguments seem to rest on paradoxical assumptions: how can [X] simultaneously [A] and also [B]? As long as this theoretical tension remains unaddressed, researchers will selectively draw from either [A] or [B], obscuring [完整图景] ([cite]).

**原文锚定**: "These arguments seem to rest on paradoxical assumptions: how can women simultaneously be more open to change and also risk averse? As long as this theoretical tension remains unaddressed, researchers will selectively draw from either theoretical arguments, obscuring the full picture"

**关键特征**:
- 并置的两条机制主张各自成立、各有引用、各自解释不同关联——矛盾不在发现层面，而在"假设能否共存"层面（比对立发现更深一层）
- 用一句修辞性问句把矛盾钉死（"how can X simultaneously A and also B?"），问句本身就是 Gap 陈述
- 张力的代价不是"知识缺口"而是"选择性引用"（selective theorizing）——只取其一忽略其二的建模偏误，为双机制整合模型直接铺路

**适用**: Incommensurability R3（对立机制）×Mechanism 组合的标志型 Tension；两条机制均有文献支撑且论文将同时建模两者时；适合紧随 Incompleteness 型 gap 段作为第二重张力。

**禁忌**: 两条机制必须真的同指一个自变量且方向相反，不可为制造张力硬凑；问句钉死后正文必须真的同时处理两者，否则沦为空头悖论。
<!-- retrieval-move:
{
  "functions": [
    "intro.gap_conflicting_accounts"
  ],
  "function_evidence": {
    "intro.gap_conflicting_accounts": {
      "kind": "verbatim",
      "cue": "how can women simultaneously be more open to change and also risk averse?",
      "why": "直接并置开放变革与风险厌恶前提，并说明选择性援引会遮蔽整体解释。"
    }
  },
  "function_support": {
    "intro.gap_conflicting_accounts": "complete"
  },
  "position": "已有解释列举之后、研究问题转折处",
  "prerequisite": "两个前提的对象与条件可比较；本卡标题与来源键的既有差异仍需核验。",
  "next": "说明研究怎样处理这一张力。",
  "advances": "将表面兼容的论据转成尚未解决的解释冲突。",
  "next_evidence": [
    "两个前提的文献与适用条件",
    "来源身份核验"
  ],
  "applicability": {
    "required_facts": {
      "competing_accounts_documented": true,
      "comparison_scope_aligned": true
    }
  }
}
-->


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
