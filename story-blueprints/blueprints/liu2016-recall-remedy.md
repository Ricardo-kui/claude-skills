# Story Blueprint — Liu, Liu & Luo (2016) JM

## 文件头

```yaml
id: liu2016
paper: "Liu, Liu & Luo (2016, JM) — What Drives a Firm's Choice of Product Recall Remedy? The Impact of Remedy Cost, Product Hazard, and the CEO"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（OCR 全文回读）→ ROBUST
source_records: [OCR parsed full text]
vault_reports:
  intro: null（OCR 全文回读）
  methods_results: null（OCR 全文回读：CPSC 召回、logit remedy 选择）
  story_arc: null
corpus_links:
  write-introduction: "决策半区缺口（'companies make two critical decisions: timing and remedy'——timing 已研究/remedy 空白）——路径待验证"
  write-methods: "remedy 选择 logit（full vs partial）+ CEO 激励调节——路径待验证"
  write-results: "成本-危害权衡 + CEO 激励干扰（cash comp/equity/tenure）——路径待验证"
```

## Story

### one_liner

> 召回中有两个关键决策——时机（已充分研究）与**补救方式**（"almost no research has examined recall remedy"）——实证发现：成本高时企业回避全额补救、危害严重时倾向全额补救；但 CEO 个人激励干扰决策（高现金薪酬/低股权激励/长任期→更少全额补救）——Big Lots 全额退款 vs World Dryer 维修包——补救选择被 CEO 的自利污染。

### knot

```yaml
knot:
  primary_type: half-domain-gap         # 第六原型：recall 决策半区（timing done/remedy not——'almost no research has examined recall remedy'）
  compound_types: []                    # 成本-危害权衡 + CEO 干扰是结构，非子类型
  statement: "recall 决策的两个关键维度——timing（已充分研究——eilert/darby 系）与 remedy（'almost no research has examined
              recall remedy'——空白）——补救选择=成本-危害权衡（成本高回避全额/危害严重倾向全额）——
              CEO 个人激励干扰（高现金薪酬/低股权激励/长任期→更少全额补救——自利污染）"
  tied_at:
    - "Intro：决策半区缺口（'companies make two critical decisions: timing and remedy. Several recent studies have provided insights on the timing issue... Our study focuses on remedy'）→ Big Lots vs World Dryer（同类吹风机不同补救）"
    - "Theory：成本-危害权衡框架 + CEO 激励（cash/equity/tenure）"
  untied_at:
    - "Theory H1-H8：成本/危害/CEO 三组假设"
    - "Results：H2 支持（hazard→full remedy β=.477, p<.05）+ CEO tenure 负（−.507, p<.01）+ H7/H8 不支持"
  antagonist: "recall 决策研究的 timing 导向（时机已做、补救空白——'almost no research has examined recall remedy'）"
  antagonist_built_by:
    - "决策双极排布（'two critical decisions: timing and remedy'——天然双极一极空白）"
    - "Big Lots vs World Dryer 对照（同类吹风机——全额退款 vs 维修包——补救差异具象化）"
    - "CEO 激励干扰论证（'CEOs' personal interests interfere with remedy decisions'——自利污染）"
```

### characters

```yaml
characters:
  protagonist: [recall characteristics（X——remedy cost + product hazard）, remedy choice（DV——full vs partial）]
  supporting:
    - "CEO cash compensation（负向——短期收益导向）"
    - "CEO equity incentive（正向——长期对齐）"
    - "CEO tenure（负向——−.507, p<.01——保守/自利）"
    - "consumers（受益方——补救质量直接影响消费者）"
  ensemble: [CPSC 召回、logit remedy 选择模型、Big Lots/World Dryer/Enesco 具名案例]
```

### resolution_logic

`exploration` 拓荒（补 remedy 决策半区——成本-危害权衡地图 + CEO 激励条件化——补救选择的完整决定因素）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：决策半区缺口（timing 已做/remedy 空白——'almost no research has examined recall remedy'）→ Big Lots vs World Dryer（同类吹风机——全额退款 vs 维修包）"
  rising_action: "成本-危害权衡框架（成本高回避全额/危害严重倾向全额）+ CEO 激励（cash/equity/tenure——自利污染）+ Methods（CPSC 召回、logit）"
  climax: "Results——H2 揭晓：危害严重→更可能全额补救（β=.477, p<.05——'remedies provided are overall responsive to consumer safety'——'certainly good news for consumers'）"
  falling_action:
    - "CEO 干扰揭晓（cash comp 负向/equity 正向/tenure −.507, p<.01——'CEOs' personal interests interfere with remedy decisions'）"
    - "交互（CEO 财务利益调节成本/危害效应——'moderate the effects of remedy cost and consumer harm'）"
    - "H7/H8 不支持（tenure×cost/hazard 交互 n.s.——诚实报告——'adverse impact does not spill over'）"
  denouement: "Discussion——remedy 选择的完整决定因素（成本/危害/CEO）；消费者福利与领导伦理（'leadership ethics'）；
              公共政策（补救质量的监管含义）"
```

### stakes

```yaml
stakes:
  theoretical: "remedy 决策空白——'almost no research has examined recall remedy'——recall 决策研究只做 timing"
  practical: "补救质量直接影响消费者（全额退款 vs 维修包）；CEO 自利对补救的干扰（领导伦理）；公共政策"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 召回后果版——recall→市场反应/声誉/成本（recall 文献主流——不涉及补救）"
  - "讲法B: 召回时机版——timing 前因（eilert/darby 系——另一决策维度）"
  - "讲法C: 危机沟通版——危机管理策略（Dawar & Pillutla——支持/阻挠——非补救成本）"
  - "本文: 补救半区拓荒版——成本-危害权衡 + CEO 激励干扰（'remedies provided are overall responsive to consumer safety'——但 CEO 自利污染）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "Big Lots vs World Dryer（同类吹风机——全额退款 vs 维修包——补救差异具象化）；Enesco 陶瓷（电源适配器过热——全额退款或新适配器）；Shelly's Diner 案例"
  rhetorical_question: "未见【已核实】"
  pacing_notes: "决策半区缺口→Big Lots 对照→成本-危害框架→CEO 激励→logit；climax=H2 揭晓（'good news for consumers'）；falling action CEO 干扰+交互+H7/H8 不支持"
  showing_telling: "Big Lots vs World Dryer（补救对照——同一产品的两种命运）；'leadership ethics'（伦理收口）"
  voice: "JM 实证口吻；'almost no research has examined'（精确缺口）；'certainly good news for consumers'（正向发现的温暖措辞）"
```

### cross_paper_notes

- **half-domain-gap 六原型（recall 决策半区）**：malshe/wu/malik/mayo/lun/**liu2016**——与 eilert2017 组成"recall 决策双半区"对照对（timing 前因 vs remedy 选择）。
- **recall 现象域十四讲法**（决策维度 +1——remedy）。
- **与 wowak2015/darby2024 的 CEO 激励家族呼应**：wowak（期权→发生率）/darby（持股→延迟）/liu（薪酬结构→补救选择）——CEO 激励×召回三场景。
- **判别器记录**：half-domain-gap 判定基于 recall 决策的天然双极（timing/remedy——'two critical decisions' 明示）——一极已做一极空白。
