# Story Blueprint — Li, Bapuji, Talluri, Singh & Narayanan (2026) JSCM

## 文件头

```yaml
id: li2026
paper: "Li, Bapuji, Talluri, Singh & Narayanan (2026, JSCM) — Vertical Spillover of Product Recalls: Theorization and Empirical Examination in the US Automobile Industry"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（OCR 全文回读）→ ROBUST
source_records: [OCR parsed full text]
vault_reports:
  intro: null（OCR 全文回读）
  methods_results: null（OCR 全文回读：154 媒体报告大召回/752 dyads/2010-2019）
  story_arc: null
corpus_links:
  write-introduction: "垂直 vs 水平溢出区分（'vertical spillovers are not only distinct from horizontal ones but also more complex'）——路径待验证"
  write-theory: "社会网络管道/棱镜（cash flow + impression 双通道）——路径待验证"
  write-results: "垂直溢出确认 + 三网络条件——路径待验证"
```

## Story

### one_liner

> 召回的水平溢出（竞争对手）已被充分研究——垂直溢出（供应商）"largely under-researched"——且主流研究"mainly focused on the cash flow effect"；本文揭示双通道：买方-供应商关系作为"管道"（现金流效应）与"棱镜"（印象效应——guilt by association）同时传导召回损失；共同商业关系加剧、共同机构持股/分析师覆盖缓解。

### knot

```yaml
knot:
  primary_type: assumption-flip         # 第六原型："垂直溢出=纯现金流损失"隐含前提（'mainly focused on the cash flow effect'——原文锚）vs 管道/棱镜双通道
  compound_types: [neglected-arena]     # 垂直溢出子域空白（'largely under-researched'——与 pupovac 共享）
  statement: "召回溢出研究只做水平（竞争对手——共享行业分类）——垂直溢出（供应商）'largely under-researched'；
              且垂直溢出研究'mainly focused on the cash flow effect'——本文扩展：网络关系作为'管道'（现金流效应）
              与'棱镜'（印象效应——'guilt by association'）同时传导——共同商业关系加剧、共同机构持股/分析师覆盖缓解"
  tied_at:
    - "Intro：危机管理背景（VW 排放丑闻 Tier-1 供应商 −2.69%/ZTE 禁令 3.33%）→ 水平溢出已做/垂直空白 → 'vertical spillovers... more complex'"
    - "Theory：社会网络理论（Podolny——pipes and prisms——现金流/印象双通道）"
  untied_at:
    - "Theory H1-H4：垂直溢出 + 三网络条件"
    - "Results：垂直溢出确认 + 共同商业关系加剧 + 共同持股/分析师缓解"
  antagonist: "'垂直溢出=纯现金流损失'的主流理解（原文锚：'this stream of research has mainly focused on the cash flow effect'——印象效应被忽略）"
  antagonist_built_by:
    - "VW/ZTE 案例开场（−2.69%/3.33%——垂直溢出的规模具象）"
    - "管道/棱镜双通道理论（'as pipes... as prisms'——对称排布——现金流/印象双机制）"
    - "主流前提锚（'mainly focused on the cash flow effect. Extending this stream of research, evidence of increased negative media coverage of suppliers indicates that network ties also function as prisms'——原文直接支撑）"
```

### characters

```yaml
characters:
  protagonist: [buyer recall（X）, supplier firm value（DV——垂直溢出损失）]
  supporting:
    - "管道机制（现金流效应——运营中断传导——分析师下调供应商销售/利润预期）"
    - "棱镜机制（印象效应——'guilt by association'——负面媒体覆盖增加——分类化传导）"
    - "common business ties（加剧——网络管道更密——'create a larger prism'）"
    - "common institutional ownership + common analyst coverage（缓解——信息管道/过滤器——降低信息不对称）"
  ensemble: [154 媒体报告大召回/752 dyads/2010-2019/美国汽车业、七源数据、VW/ZTE 案例]
```

### resolution_logic

`revelation` 揭幕（揭幕垂直溢出的双通道——管道/棱镜 + 三网络条件化——"垂直溢出比想象的复杂"）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：VW 排放丑闻（Tier-1 供应商 −2.69%）/ZTE 禁令（3.33%）→ 水平溢出已做（Borah & Tellis/Zavyalova——竞争对手）→ 垂直溢出'largely under-researched' → 'not only distinct from horizontal ones but also more complex'"
  rising_action: "社会网络理论（Podolny——pipes and prisms——现金流/印象双通道）+ 扩展网络条件（共同商业关系/共同机构持股/共同分析师覆盖）+ Methods（154 大召回/752 dyads/七源数据）"
  climax: "Results——垂直溢出确认：买方召回→供应商显著价值损失（'Confirming the vertical spillover effect'——首揭）"
  falling_action:
    - "共同商业关系加剧（'stronger when the supplier shares more common business ties'——网络管道更密/棱镜更大）"
    - "共同机构持股/分析师覆盖缓解（'weaker when there is a high level of common institutional ownership and common analyst coverage'——信息管道/过滤器——降低不确定性与负面印象）"
    - "稳健性"
  denouement: "Discussion——垂直溢出的双通道机制（现金流 + 印象——'guilt by association'——分析师预期下调 + 负面媒体覆盖双证据）；
              供应链协作质量风险（'pave the way for supply chain partners to work collectively to avoid quality risks'）；
              网络条件的治理含义"
```

### stakes

```yaml
stakes:
  theoretical: "垂直溢出 under-researched——机制（管道/棱镜）与条件（扩展网络）缺失——'more complex' 的垂直效应"
  practical: "供应商在买方召回中的价值损失（VW −2.69%/ZTE 3.33%）；供应链质量协作"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 水平溢出版——recall→竞争对手（Borah & Tellis/Zavyalova——共享行业分类）"
  - "讲法B: 制造商后果版——recall→制造商自身（recall 文献主流——单主体）"
  - "讲法C: 现金流损失版——只做垂直溢出的运营/现金流后果（主流理解——'mainly focused on the cash flow effect'——本文挑战）"
  - "本文: 双通道揭幕版——管道/棱镜（现金流+印象——'guilt by association'）+ 三网络条件"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "VW 排放丑闻（Tier-1 供应商 −2.69%——具名事件）；ZTE 禁令（3.33%）；通用汽车/Toyota 情境（汽车业）"
  rhetorical_question: "未见【已核实】"
  pacing_notes: "VW/ZTE 案例开场→水平已做/垂直空白→管道/棱镜理论→三网络条件；climax=垂直溢出确认；falling action 三条件"
  showing_telling: "'pipes and prisms'（管道/棱镜隐喻——Podolny 社会网络）；'guilt by association'（分类化意象）；'more complex'（复杂化强调）"
  voice: "JSCM 供应链实证口吻；'largely under-researched'（空白强调）；'warrant dedicated theoretical attention'（理论呼吁）"
```

### cross_paper_notes

- **assumption-flip 六原型（机制前提复杂化）**：paruchuri/shipilov/hahl/lovelace/darby2025/**li2026**——"垂直溢出=纯现金流"前提（原文锚：'mainly focused on the cash flow effect'）被管道/棱镜双通道复杂化。
- **垂直传染家族对照对（同现象双篇不同透镜）**：pupovac（股东筛选——信息不对称）↔ li2026（管道/棱镜——社会网络）——共享子域（neglected-arena compound 互证——'largely under-researched'）。
- **与 Bapuji 系连接**（li2026——Bapuji 共同作者——危机/供应链学者网络——召回学习/外包文献的连接）。
- **recall 现象域十五讲法**。
- **判别器记录**：assumption-flip 判定基于"垂直溢出=纯现金流"隐含前提（原文 Results 直接锚定）被双通道（印象效应）复杂化。
