# Story Blueprint — Han, Pollock & Graffin (2020) AMJ

## 文件头

```yaml
id: han2020
paper: "Han, Pollock & Graffin (2020, AMJ) — Now You See Me: How Status and Categorical Proximity Shape Misconduct Scandalization"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（vault 报告 + 全文回读）→ ROBUST
source_records: [vault narrative/methods_results 报告, parsed full text]
vault_reports:
  intro: "narrative_analysis/mvp30/han2020_now_you_see_me_amj_narrative.md"
  methods_results: "narrative_analysis/methods_results/mvp30/methods/han2020_now_you_see_me_methods_narrative.md + results/... + deep_distillation/papers/...（报告齐全）"
  story_arc: null
corpus_links:
  write-introduction: "共识建立+去情境化批判（'treated... as decontextualized'——'This is problematic because'）——路径待验证"
  write-methods: "ordered probit + 多媒体覆盖测量——路径待验证"
  write-results: "复现+双向条件化（insider 放大/outsider 消解）+ 边际效应全程分析——路径待验证"
```

## Story

### one_liner

> 共识——高地位者的违规必然被丑闻化（status imparts salience）——确实成立，但被去情境化地理解；本文揭示媒体惯例的情境剧本：同行业的高地位违规者**放大**丑闻化（记者有剧本——salience 增强），行业外的高地位违规者**消解**之（注意力分流——效应归零）——"Now You See Me"：地位让你被看见，但看/不看取决于情境剧本。

### knot

```yaml
knot:
  primary_type: consensus-puzzle        # 第五原型：完整性/无条件性/条件性消解/条件性失效/本文情境双向调制
  compound_types: []                    # 对称边界条件（insider 放大 + outsider 消解）是调制结构，非子类型
  statement: "共识——高地位者的违规被丑闻化（'Research has consistently found that individuals are drawn to
              high-status actors' wrongdoing because status imparts salience'）；但地位被去情境化地理解——过去违规者的
              地位×行业内外双向调制：insider 放大（0.196***）、outsider 消解（−0.074***——效应归零）"
  tied_at:
    - "Intro P1：共识建立（高地位→丑闻化——'Research has consistently found'）→ 前因缺口（除违规者地位外 antecents 被忽视）"
    - "Intro P2：去情境化批判（'treated the misbehaving actor's status as decontextualized'——'context... can differentially shape assessments and responses, sometimes even inverting the relationships'）"
  untied_at:
    - "Theory H1-H3：复现 + insider 放大 + outsider 消解"
    - "Results Table 2：H1 支持（0.073***）+ H2/H3 支持（0.196***/−0.074***）"
  antagonist: "'高地位必丑闻化'共识的去情境化版本（status imparts salience 被当作无条件定律）"
  antagonist_built_by:
    - "共识建立（'Research has consistently found'）→ 去情境化批判（'This is problematic because'——情境可反转关系）"
    - "对称边界条件排布（insider 放大 vs outsider 削弱——'amplifies... when... but weakens it when...'）"
    - "引语加持（'both the type and characteristics of a specific context may substantially influence the formation of news media coverage'）"
```

### characters

```yaml
characters:
  protagonist: [firm status（X）, misconduct scandalization（DV——ordinal：无覆盖/中等/丑闻化）]
  supporting:
    - "high-status insider breaches（放大——媒体剧本：边际效应 −9.2%→−16.8%）"
    - "high-status outsider breaches（消解——注意力分流：+1SD 效应归零——'more important boundary condition than we expected'）"
    - "media routines（机制——记者剧本/惯例）"
    - "journalists（gatekeepers——注意力分配者）"
  ensemble: [数据泄露 2015-2018、ordered probit、多媒体覆盖测量（LIWC 语气验证）]
```

### resolution_logic

`revelation` 揭幕（揭幕情境如何调制地位效应——媒体惯例的 insider/outsider 剧本——"Now You See Me"：看见与否是情境的魔术）。

### five_acts

```yaml
five_acts:
  exposition: "Intro P1-P2：共识建立（高地位→丑闻化——'Research has consistently found'）→ 前因缺口 → 去情境化批判（情境可反转关系）"
  rising_action: "Intro P3-P5（过去违规者地位×行业内外边界条件 + 数据泄露 2015-2018 + 三贡献）+ Theory（media routines——insider 放大/outsider 削弱）+ Methods（ordered probit、多媒体测量）"
  climax: "Results Table 2——H1 复现共识（firm status → 丑闻化 0.073***）+ H2/H3 揭晓：insider 放大（0.196***——边际效应从 −9.2% 到 −16.8%）/ outsider 消解（−0.074***——高 outsider 时效应归零）"
  falling_action:
    - "边际效应全程分析（Plot d-f：insider 全程显著；Plot g-l：outsider +1SD 归零——'more important boundary condition than we expected'）"
    - "丑闻测量验证（LIWC 语气 t-test p=.002、scandal-word 词典 p=.010——'scandalized' 类别的媒体语言确实更负面）"
    - "负二项连续规格稳健性（三种变换——结果一致——但 categorical 处理更恰当）"
    - "内生性检验（endogeneity concerns 区段）+ 非高地位违规者控制"
  denouement: "Discussion——媒体惯例解释（记者对同行业高地位违规者有'剧本'——salience 增强；外部高地位违规多→注意力疲劳/分流——
               忽略当前违规）——'Now You See Me'（地位让你被看见，但看/不看取决于情境剧本）"
```

### stakes

```yaml
stakes:
  theoretical: "scandalization 前因被忽视——地位被去情境化——情境可反转关系（媒体惯例视角缺失）"
  practical: "高地位企业违规后的媒体命运取决于情境（行业内外过去违规者的地位）——'丑闻'不是事件属性而是情境产物"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 地位→丑闻版——'高地位必然丑闻化'（现有研究共识——status imparts salience）"
  - "讲法B: 事件特征版——只做违规事件的属性（severity/类型——忽略情境）"
  - "讲法C: 后果版——丑闻化的后果（声誉/市场——主流——'event is a scandal... then looked at how differences in status influence the way the scandal affects different actors'）"
  - "本文: 情境双向调制版——insider 放大/outsider 消解（'Now You See Me'——媒体惯例剧本——看见与否是情境的魔术）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "无具名企业（数据泄露样本——媒体覆盖计数）；'Now You See Me' 标题魔术意象作隐喻性人面"
  rhetorical_question: "未见 pivot【已核实】——去情境化批判用陈述句式（'This is problematic because...'）"
  pacing_notes: "共识→去情境化批判→对称边界条件→发现预览；climax=三结果并置（复现+双向调制）；falling action 边际全程+测量验证+稳健性"
  showing_telling: "标题意象（'Now You See Me'——看见与看不见的魔术——showing 手段）；'amplifies... but weakens it when...'（对称句式）；引语加持（context 重要性）"
  voice: "理论挑战口吻；'This is problematic because'（批判句式——两次）；'more important boundary condition than we expected'（意外性诚实）"
```

### cross_paper_notes

- **consensus-puzzle 五原型（"共识条件化"家族）**：pontikes（完整性）/ cutolo（无条件性）/ gamache（条件性消解）/ kundro（条件性失效）/ **han2020（情境双向调制——insider 放大 + outsider 消解对称——比单向条件更完整）**。
- **media routines 家族 2 例**：han2020（丑闻化情境）↔ lovelace2021（造星过程）——同一透镜两个故事。
- **与 han2024 对照（同姓 Han + Pollock——scandalization 两端）**：han2020（status→scandalization 前因——情境）↔ han2024（reputation/celebrity→scandalization 后果 2×2）——scandalization 前因与后果两端。
- **status 家族**：pollock2015（status↔reputation 共演）/ hahl2017（status 真实性）/ keeves2017（status 关系双面）/ han2020（status 丑闻化）——status 概念空间四故事。
- **判别器记录**：consensus-puzzle 判定基于共识（地位→丑闻化）成立（H1 复现）但被情境双向调制。
