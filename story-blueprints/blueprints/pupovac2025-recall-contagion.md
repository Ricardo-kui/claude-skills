# Story Blueprint — Pupovac, Astvansh, Carrillat & Legoux (2025) POM

## 文件头

```yaml
id: pupovac2025
paper: "Pupovac, Astvansh, Carrillat & Legoux (2025, POM) — Product Recall Contagion in the Supply Chain"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（OCR 全文回读）→ ROBUST
source_records: [OCR parsed full text]
vault_reports:
  intro: null（OCR 全文回读）
  methods_results: null（OCR 全文回读：896 dyads、事件研究 + 两阶段横截面）
  story_arc: null
corpus_links:
  write-introduction: "传染场景（'supplier's shareholders may perceive uncertain future demand... react punitively'）+ 两阶段筛选理论——路径待验证"
  write-methods: "事件研究 CAR + 两阶段横截面（披露/收入依赖）——路径待验证（write-methods 事件研究文件已有 pupovac 条目）"
  write-results: "传染 0.40% + 披露缓解 + 依赖加剧——路径待验证"
```

## Story

### one_liner

> 制造商的召回不只伤害自己——还传染供应商（CAR −0.40%）——但传染不是盲目的：供应商股东的信息不对称触发**两阶段筛选**——第一筛：供应商是否自愿披露客户信息（披露缓解惩罚）；第二筛：对披露者，收入依赖度（依赖加剧惩罚）——"披露是双刃剑"。

### knot

```yaml
knot:
  primary_type: neglected-arena         # 第六原型：垂直传染子域空白（召回后果研究做制造商自身/水平、供应商传染空白）
  compound_types: []                    # 两阶段筛选是机制，非子类型
  statement: "召回后果研究做了制造商自身（市场反应/学习）与水平溢出（竞争对手）——供应商的垂直传染空白（与 li2026 共享子域）——
              实证：制造商大召回→供应商 CAR −0.40%（传染存在）；且传染不是盲目的——供应商股东信息不对称→两阶段筛选
              （披露缓解/依赖加剧）——'double-edged nature of this disclosure'"
  tied_at:
    - "Intro：制造商-供应商互缠（'a supplier may become more prosperous... but also suffer steep losses'）→ 传染场景 → 筛选理论引入"
    - "Theory：两阶段筛选（Stage 1 自愿披露——缓解；Stage 2 收入依赖——加剧）"
  untied_at:
    - "Theory H1-H3：传染 + 披露调节 + 依赖调节"
    - "Results：传染 −0.40% + 披露缓解 + 依赖加剧"
  antagonist: "召回后果研究的单主体导向（只做制造商自身/水平溢出——供应商被忽略）"
  antagonist_built_by:
    - "传染场景（'a manufacturer's product recall... can spur a sharp, near-term drop in the demand... by extension, forecast uncertain demand for the supplier'——传染链条）"
    - "两阶段筛选设计（'shareholders' information asymmetry may cause them to screen'——理性的惩罚而非盲目）"
    - "披露双刃（'the double-edged nature of this disclosure'——披露缓解 vs 依赖暴露）"
```

### characters

```yaml
characters:
  protagonist: [manufacturer recall（X——大型召回）, supplier CAR（DV——股东惩罚）]
  supporting:
    - "两阶段筛选（机制——Stage 1 自愿披露客户信息 [缓解]；Stage 2 收入依赖度 [加剧——'the higher the dependence, the more punitive']）"
    - "recall severity 五代理（规模/新闻量/新闻情感/消费者伤害/软件 vs 非软件——情境筛选）"
    - "supplier shareholders（筛选者——信息不对称下的理性惩罚）"
    - "supplier managers（实践端——事前披露决策）"
  ensemble: [896 dyads/28 大型召回/11 制造商/46 供应商（⚠️ Abstract 写 27——原文内部矛盾，正文 28 为准）、事件研究 CAR + 两阶段横截面、FASB/SEC 披露规则背景]
```

### resolution_logic

`revelation` 揭幕（揭幕传染的理性面——两阶段筛选机制——披露的双刃）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：制造商-供应商互缠（'intertwined'——繁荣与损失同源）→ 传染场景（大召回→供应商需求不确定→股价下跌）→ 筛选理论引入（'screening for supplier-provided cues'）"
  rising_action: "两阶段筛选理论（Stage 1 自愿披露——透明度信号；Stage 2 收入依赖——精确筛）+ 五代理情境筛选 + Methods（896 dyads/事件研究 + 两阶段横截面）"
  climax: "Results——传染揭晓：制造商大召回→供应商 CAR −0.40%（'evidence supports supply-chain contagion from recalls'）——传染的首揭"
  falling_action:
    - "Stage 1 揭晓（披露供应商受罚更轻——'shareholders are less punitive toward suppliers that disclosed'）"
    - "Stage 2 揭晓（依赖度越高惩罚越重——'the higher the supplier's revenue dependence, the more punitive'——披露的双刃）"
    - "情境变量（召回规模/新闻量/情感也影响股东反应——五代理）"
  denouement: "Discussion——供应链传染文献扩展（'a recall's consequences can propagate through the supply chain'）；
              筛选理论贡献（两阶段筛选——理想筛不可得时的程序）；披露双刃（'the double-edged nature of this disclosure'——
              事前披露决策的战略含义）"
```

### stakes

```yaml
stakes:
  theoretical: "垂直传染子域空白——召回后果研究只做制造商自身/水平溢出——供应商股东反应的机制未知"
  practical: "供应商事前披露决策（缓解 vs 暴露的双刃）；召回传染的供应链成本"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 制造商后果版——recall→制造商市场反应/学习（recall 文献主流——单主体）"
  - "讲法B: 水平溢出版——recall→竞争对手（Borah & Tellis/Zavyalova——水平传染）"
  - "讲法C: 供应链运营版——recall 的供应链运营风险（现金流/中断——不接股东反应）"
  - "本文: 垂直传染+筛选揭幕版——供应商 CAR + 两阶段筛选（'double-edged nature of disclosure'）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "无具名企业（896 dyads 集体样本——11 制造商/46 供应商）；披露规则背景（FASB/SEC——'SEC has never taken disciplinary action'——制度细节）"
  rhetorical_question: "未见【已核实】"
  pacing_notes: "互缠场景→传染链条→筛选理论→两阶段设计；climax=传染揭晓（−0.40%）；falling action 两阶段+五代理"
  showing_telling: "'intertwined'（互缠意象——繁荣与损失同源）；'screen'（筛选隐喻——信息不对称的理性反应）；'double-edged'（披露双刃）"
  voice: "POM 实证口吻；'react punitively'（惩罚反应）；'unfortunately'（不利方向的诚实表述）"
```

### cross_paper_notes

- **neglected-arena 六原型（垂直传染子域）**：desai2012/park2013/eilert2017/kashmiri2017/kalaignanam2013/**pupovac2025**——与 li2026 共享子域（垂直传染家族 2 篇）。
- **垂直传染家族对照对**：pupovac（股东筛选视角——信息不对称——'披露双刃'）↔ li2026（管道/棱镜视角——社会网络——现金流+印象双通道）——同现象双篇不同透镜。
- **与 fang2025 的 Astvansh 系连接**（pupovac + fang2025——Astvansh 共同作者——recall 传染/竞争家族网络）。
- **识别家族**：事件研究 CAR（与 pfarrer2010/darby2024/fang2025 同款）。
- **判别器记录**：neglected-arena 判定基于垂直传染子域空白（供应商后果被忽略——与 li2026 的 'largely under-researched' 互证）。
