# Story Blueprint — Kundro & Rothbard (2023) AMJ

## 文件头

```yaml
id: kundro2023
paper: "Kundro & Rothbard (2023, AMJ) — Does Power Protect Female Moral Objectors? How and When Moral Objectors' Gender, Power, and Use of Organizational Frames Influence Perceived Self-Control and Experienced Retaliation"
paper_type: quantitative   # 四研究（档案 + 3 实验）
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（vault 报告 + 全文回读）→ ROBUST
source_records: [vault narrative/methods_results 报告, parsed full text]
vault_reports:
  intro: "narrative_analysis/mvp30/kundro2023_power_female_moral_objectors_amj_narrative.md"
  methods_results: "narrative_analysis/methods_results/mvp30/methods/kundro2023_power_female_moral_objectors_methods_narrative.md + results/... + deep_distillation/papers/... + fine_grained/batch_02_wu2025_kundro2023/...（四报告齐全）"
  story_arc: null
corpus_links:
  write-introduction: "标题问句 Hook（Does Power Protect Female Moral Objectors?）——路径待验证"
  write-theory: "role expectations + expectancy violation 整合——路径待验证"
  write-methods: "四研究（档案 + CIT 实验 + 2 预注册实验）+ 调节中介——路径待验证（falchetti2022 实验家族）"
```

## Story

### one_liner

> 组织伦理文献建议高权力者承担 moral objection（权力=保护伞），但四研究一致显示：**权力只保护男性**——高权力女性 objector 与平均权力女性一样受报复（double bind：被期待 objection 又因此受罚）；机制=观察者感知的 self-control（角色期望违背）；解药不是更多权力，而是 **organizational frame**（把 objection 框架为服务组织）——框架消除性别差异。

### knot

```yaml
knot:
  primary_type: consensus-puzzle        # 第四原型：完整性（pontikes）/ 无条件性（cutolo）/ 条件性消解（gamache2023）/ 条件性失效（本文——性别）
  compound_types: [assumption-flip]     # "权力=保护伞"（power as panacea）前提被性别条件化挑战
  statement: "组织伦理共识——高权力者应承担 moral objection 且受权力保护（'power as panacea'）；但 power 只保护男性——
              高权力女性 objector 面临 double bind（被期待 objection 又因此受罚）——性别条件使保护失效；
              organizational frame 是解药（框架消除性别差异）"
  tied_at:
    - "Intro P1-P2：moral objection 价值+报复风险（Hook+stakes）→ 默认解法（高权力者应 objection）→ 核心张力
      （'whether power protects women'——gender and power 两文献预测冲突）→ double bind"
    - "Theory：role expectations + expectancy violation"
  untied_at:
    - "Theory H1-H4：权力主效应 + 性别调节 + framing 三向 + self-control 调节中介"
    - "Results：H2 四研究全支持（男性受益/女性不受益）；H3/H4 解药生效（organizational frame 消除差异）"
  antagonist: "组织伦理文献的'权力=保护伞'共识（power as panacea——advocacy 建议未考虑性别）"
  antagonist_built_by:
    - "标题问句（'Does Power Protect Female Moral Objectors?'——修辞问即 knot 载体）"
    - "默认解法引入（'scholars suggest... those at the top'——既有建议建立）"
    - "两文献预测冲突排布（power frees vs gender constrains——争论化）"
```

### characters

```yaml
characters:
  protagonist: [structural power（X）, retaliation（DV——报复）]
  supporting:
    - "gender（核心调节——double bind 的来源：男性受益/女性不受益）"
    - "moral objection framing（H3/H4——standard vs organizational——解药）"
    - "perceived self-control（中介——道德美德感知）"
    - "moral objector（主体——高权力女性：被期待又受罚）"
  ensemble: [U.S. Merit Board 档案、CIT 实验、MTurk 预注册实验×2]
```

### resolution_logic

`remedy` 解药（organizational frame——给已知惩罚加缓解条件——与 cutolo2024 同族；不是要更多权力，而是换框架）+ 机制揭幕（self-control 感知）。

### five_acts

```yaml
five_acts:
  exposition: "Intro P1-P2：moral objection 关键行为+报复风险（Hook+stakes）→ 默认解法（高权力者应 objection——权力=保护伞）
               → 核心张力（'whether power protects women'）→ double bind（被期待又受罚）"
  rising_action: "Intro P3-P4（power×gender + 三理论 + self-control 机制 + organizational frame 预览 + 贡献）+ Theory
                  （role expectations + expectancy violation）+ 四研究设计（档案 + CIT + 2 预注册实验）"
  climax: "Study 1——H1/H2 揭晓：power 减少报复（b=−.12, p<.001）但 gender 交互显著（b=−.08, p=.007）——
           **权力保护男性（b=−0.15）远强于女性（b=−.07）**——'权力不是保护伞，是男性专属的伞'"
  falling_action:
    - "Study 2（观察者视角复现 H2——F=5.18, p=.02——高权力女性 vs 平均权力女性无差；H1 不显著诚实报告）"
    - "Study 3/4 解药揭晓（三向交互：standard frame 下 power×gender 显著 [F=7.60/17.40]、organizational frame 下消失
      [F=1.09/.71]——男性才受 power 保护 [F=12.20/14.70]、女性不受 [F=0.18/4.36 n.s.]）"
    - "H4 调节中介（self-control：standard frame 男性间接效应显著 [IMM=−.49/−.30 CI 排除 0]、女性不显著、
      organizational frame 无差——机制在位）"
    - "替代机制排除（warmth/competence/dominance 不中介——self-control 特异性）"
  denouement: "Discussion——回到开头：'power alone is not enough to mitigate retaliation against women'——
               'Instead of viewing power as a panacea, our research suggests that considering who the power holder is
               (i.e., their gender) and how the power holder behaves (i.e., moral objection framing) has critical implications'；
               组织框架作为可行解药（communal content——消除角色违规感）"
```

### stakes

```yaml
stakes:
  theoretical: "'权力保护异议者'建议未考虑性别——expectancy violation 下女性反而受罚——organizational ethics 文献盲区"
  practical: "女性不断进入高权力岗位——double bind 的现实代价；组织框架作为可操作的解药（培训/沟通指导）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 权力保护版——高权力者应 objection 且受保护（组织伦理文献建议——'power as panacea'）"
  - "讲法B: 女性赋权版——'让更多女性掌权'（advocacy 文献——本文证据显示不够：权力不保护女性）"
  - "讲法C: 报复抑制版——只做 retaliation 的抑制因素（组织伦理主流——不问谁受害）"
  - "本文: 性别条件化+解药版——power 只保护男性；organizational frame 消除差异——'不是要更多权力，而是换框架'"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "中低——四研究实验（Merit Board 档案现实场景 + MTurk 受试者——无具名个人）"
  rhetorical_question: "标题即修辞问（'Does Power Protect Female Moral Objectors?'——knot 载体——与 shipilov2020 标题问句同型）"
  pacing_notes: "四研究递进（档案→实验→机制实验→复现——每研究一轮 climax 起伏）；falling action 含解药揭晓
                 （organizational frame 消除差异——remedy 的实证高潮）；H1 部分不支持（Study 2/4）诚实报告"
  showing_telling: "标题问句（knot 载体）；'double bind'（概念隐喻）；'power as a panacea'（批评隐喻）"
  voice: "理论驱动实证口吻；克制（'power does not automatically protect'——谨慎否定）"
```

### cross_paper_notes

- **consensus-puzzle 四原型（"共识条件化"家族）**：pontikes（完整性）/ cutolo（无条件性）/ gamache2023（条件性消解——审视下共识归零）/ **kundro2023（条件性失效——性别下保护失效）**——gamache↔kundro 对照对：同为"共识在条件 X 下不成立"，gamache 消解差异、kundro 失效保护。
- **标题问句家族（rhetorical_question 新形态）**：shipilov2020（"Is All Publicity Good Publicity?"）+ kundro2023（"Does Power Protect Female Moral Objectors?"）——标题问句作 knot 载体 2 例。
- **remedy 解法家族 +1**：cutolo2024（叙事解药——文本层）↔ kundro2023（框架解药——沟通层）——"解药家族 2 例"。
- **与 gamache2023 的性别研究对照**：gamache（女性 CEO 行为差异被审视消解——情境镜头）+ kundro（女性 objector 受罚未被权力保护——性别镜头）——性别研究两种讲法。
- **paradox 候选评估记录**：double bind 悖论感→判定 consensus-puzzle 张力（非"同一预测自相矛盾"）——paradox 仍待建（Mishina 2010 候选）。
- **判别器记录**：consensus-puzzle 判定基于共识（power protects）被条件（gender）失效——与 gamache2023 同族。
