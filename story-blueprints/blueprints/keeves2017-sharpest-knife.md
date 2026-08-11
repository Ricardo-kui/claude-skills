# Story Blueprint — Keeves, Westphal & McDonald (2017) ASQ

## 文件头

```yaml
id: keeves2017
paper: "Keeves, Westphal & McDonald (2017, ASQ) — Those Closest Wield the Sharpest Knife: How Ingratiation Leads to Resentment and Social Undermining of the CEO"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（vault 报告 + 全文回读）→ ROBUST
source_records: [vault narrative/methods_results/theory 报告, parsed full text, 早期故事弧资产]
vault_reports:
  intro: "narrative_analysis/mvp30/keeves2017_ingratiation_resentment_asq_narrative.md"
  theory: "narrative_analysis/theory/mvp30/fine_grained/batch_2026-07-09/keeves2017_ingratiation_resentment_distilled_theory.md"
  methods_results: "narrative_analysis/methods_results/mvp30/methods/keeves2017_ingratiation_resentment_methods_narrative.md + results/... + deep_distillation/papers/...（报告齐全）"
  story_arc: "narrative_analysis/_story_arcs/keeves2017_ingratiation_resentment_asq_story_arc.md（早期资产——链接不复制，以 blueprint 为准）"
corpus_links:
  write-introduction: "单向效应缺口（'focused almost entirely on the beneficial outcomes'）——路径待验证"
  write-theory: "自尊威胁→外化归因→怨恨机制链——路径待验证"
  write-methods: "调查+档案混合（3,895 dyads）+ SEM——路径待验证（park2013 同设计家族）"
```

## Story

### one_liner

> 逢迎被当作获取社会资本的工具（文献只讲收益），但同一行为对双方意义相反：逢迎者表面亲近、内心怨恨——逢迎违反真实性/自主/功绩理想→威胁自尊→外化归因→怨恨 CEO→向记者散布负面评论暗中破坏 CEO 的社会资本——"最亲近的人挥最利的刀"，且对少数族裔/女性 CEO 格外锋利。

### knot

```yaml
knot:
  primary_type: irony-reversal          # 第四原型：受众分裂（pontikes）/ 反果（desjardine2023）/ 类别分裂（toh2023）/ 关系双面（本文）
  compound_types: [assumption-flip]     # 单向收益前提被挑战（'focused almost entirely on the beneficial outcomes'）
  statement: "逢迎研究只讲逢迎对逢迎者的收益；但同一行为对双方意义相反——逢迎违反 authenticity/autonomy/meritocracy 理想
              →威胁逢迎者自尊→外化归因→怨恨 CEO→社会破坏（向记者负面评论）——最亲近的人挥最利的刀"
  tied_at:
    - "Intro P2：单向效应缺口（'focused almost entirely on the beneficial outcomes... social relations are not necessarily symmetrical'）"
    - "Intro P3：理论核心（'different and even opposing social and psychological consequences'——narrative 标注悖论型）"
  untied_at:
    - "Theory H1/H2：怨恨揭晓 + 人口学边界"
    - "Results：怨恨显著（1 SD 恭维→1.5-2 点怨恨）+ H3 SEM 闭环（怨恨→三种负面评论中介）"
  antagonist: "逢迎研究的单向收益假设（社会影响文献——只讲 influence agent 的益处）"
  antagonist_built_by:
    - "'focused almost entirely on the beneficial outcomes'（缺口句式——单边化指控）"
    - "网络不对称性引用（'social relations are not necessarily symmetrical'——理论依据）"
    - "标题意象（'Those Closest Wield the Sharpest Knife'——亲近与伤害的并置）"
```

### characters

```yaml
characters:
  protagonist: [ingratiation（X——focal/other 双源）, resentment（DV→中介）→ negative commentary/social undermining（最终 DV）]
  supporting:
    - "positive self-regard（中介——自尊威胁：真实性/自主/功绩理想被违反）"
    - "demographic differences（H2——白人男性经理×少数族裔/女性 CEO：怨恨 +18-44%）"
    - "CEO（target——受害方）"
    - "journalists（第三方——社会破坏的通道）"
  ensemble: [3,895 manager-CEO dyads、调查+档案混合（park2013 同设计）、SEM、CEO 调查数据]
```

### resolution_logic

`revelation` 揭幕（展示被忽略的阴暗面——逢迎的代价面 + 不对称关系）+ 机制链揭幕（自尊威胁→外化归因→怨恨→社会破坏）。研究者是拆镜人：把逢迎的单面镜子翻过来，露出另一面的怨恨。

### five_acts

```yaml
five_acts:
  exposition: "Intro P1-P2：背景（社会资本+逢迎功能）→ 单向效应缺口（'focused almost entirely on the beneficial outcomes'——网络不对称性）"
  rising_action: "Intro P3-P5（理论核心：自尊威胁→外化归因→怨恨；边界：少数族裔/女性 CEO 怨恨更强；后果：社会破坏）+ Methods（3,895 dyads 调查+档案、SEM）"
  climax: "Results——H1a/H1b 揭晓：逢迎显著增加怨恨（1 SD 恭维→1.5-2 点怨恨/5 分制）——'讨好者怨恨被讨好者'首次揭晓"
  falling_action:
    - "H2a/b 人口学边界（白人男性经理+少数族裔/女性 CEO：怨恨 +18-44%——向上歧视的实证）"
    - "机制验证（自尊中介：p<.001, z=2.70-2.94——真实性/自主/功绩理想受损；补偿扩展：奖励低时怨恨更强）"
    - "H3 SEM 闭环（怨恨→三种负面评论中介 z=2.03-4.12——社会破坏闭环：faint praise/间接/直接负面陈述）"
    - "稳健性（CEO FE、change variables、绩效调节——低绩效放大）"
  denouement: "Discussion——回到开头：'managers' attempts to build their own social capital can trigger behavior
               that has the potential to harm the social capital of their target'——不对称关系（target 正面情感/
               逢迎者怨恨——情感与行为相反方向）；'insidious form of social discrimination'（向上歧视——
               minority/女性 CEO 受害）；社会资本丧失机制（非自身行为而是同事人际行为）"
```

### stakes

```yaml
stakes:
  theoretical: "逢迎研究单向化——只讲收益不讲代价；社会资本丧失的微观机制缺失；向上歧视（upward discrimination）未研究"
  practical: "CEO 的社会资本被最亲近的人暗中破坏——少数族裔/女性 CEO 尤甚；'最亲近的人'不等于支持"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 逢迎收益版——逢迎者获得推荐/好感（逢迎文献主流——'focused almost entirely on the beneficial outcomes'）"
  - "讲法B: target 正面反应版——只做 target 喜欢逢迎者（不对称关系的另一半——target 视角单面）"
  - "讲法C: 逢迎技能版——逢迎作为政治技能/印象管理工具（组织行为主流——工具性视角）"
  - "本文: 阴暗面揭幕版——逢迎→自尊威胁→怨恨→社会破坏（同一行为的代价面 + 不对称关系 + 向上歧视）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "标题意象（'Those Closest Wield the Sharpest Knife'——隐喻性人面：亲近者/刀）；少数族裔与女性 CEO 的具象受害情境"
  rhetorical_question: "未见【已核实】"
  pacing_notes: "单向缺口→悖论核心→边界→后果链；climax=怨恨揭晓（1.5-2 点/5 分制）；falling action 机制验证+边界+SEM 闭环"
  showing_telling: "标题隐喻（sharpest knife——亲近与伤害并置）；'insidious'（阴险的——形容词色彩）；'opposing emotions'（相反情感并置）"
  voice: "理论驱动实证口吻；克制（'may have the potential to harm'——谨慎表述）"
```

### cross_paper_notes

- **irony-reversal 四原型（"同一 X 劈开两类 Y"四种形态）**：受众分裂（pontikes）↔ 行动反果（desjardine2023）↔ 类别分裂（toh2023）↔ **关系双面（keeves2017——同一关系内双方情绪相反）**。
- **同作者不同故事第 4 组**：park2013（neglected-arena——进入门槛/逆马太）↔ keeves2017（irony-reversal——逢迎反向伤害）——同为 Westphal 参与、同为 ASQ、同为 CEO 调查+档案混合——"同作者同方法不同故事"。
- **与 hahl2017 的 authenticity 家族对照**：hahl（借取真实性——地位者消费低眉修补软肋）↔ keeves（违反真实性——逢迎损害自尊）——"authenticity 理想的两面：借取 vs 违反"。
- **vault 早期故事弧资产**：`_story_arcs/keeves2017_ingratiation_resentment_asq_story_arc.md`（链接不复制——以 blueprint 为准）。
- **判别器记录**：irony-reversal 判定基于"同一行为对双方意义相反"（现象内冲突）——本文形态=关系双面。
