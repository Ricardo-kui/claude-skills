# Story Blueprint — Lun, Zurbruegg, Mount & Cheong (2026) ETP

## 文件头

```yaml
id: lun2026
paper: "Lun, Zurbruegg, Mount & Cheong (2026, ETP) — The Double-Edged Sword of Entrepreneurial Orientation: Product Recalls and the Role of COO Power"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（OCR 全文回读）→ ROBUST
source_records: [OCR parsed full text（文献笔记库论文导入）]
vault_reports:
  intro: null（OCR 全文回读）
  methods_results: null（OCR 全文回读：1998-2021 美国物理消费品企业）
  story_arc: null
corpus_links:
  write-introduction: "'over-replicated... ad nauseam' 引语（批评主流——Wales 2021）+ Samsung Note 7 具名案例——路径待验证"
  write-theory: "EO-as-experimentation（variance-enhancing——下尾）+ UET 整合（COO power）——路径待验证"
  write-results: "EO→召回正相关 + COO 调节 + 生命周期条件——路径待验证"
```

## Story

### one_liner

> EO 的正面效果被研究到"over-replicated... ad nauseam"，暗面却 substantially underdeveloped——但 EO-as-experimentation 逻辑（variance-enhancing——"creates a distribution of outcomes, both wins and losses"）必然产生下尾：高 EO 企业因大胆实验压缩开发测试周期而暴露于产品召回风险；COO 权力（质量倡导者）嵌入运营纪律可缓冲——但创新组合早期集中会稀释 COO 注意力。

### knot

```yaml
knot:
  primary_type: half-domain-gap         # 第五原型：EO 正面/暗面后果半区（与 malik2025 同构的"后果半区"）
  compound_types: []                    # variance-enhancing 是机制，非子类型
  statement: "EO 研究'continues to privilege its beneficial outcomes'（正面后果 over-replicated——'ad nauseam' [Wales 2021]）；
              downsides substantially underdeveloped——EO-as-experimentation（variance-enhancing——'creates a distribution of
              outcomes, both wins and losses' [Wales 2023]）必然产生下尾：高 EO 企业压缩开发测试周期→产品召回风险；
              COO power（质量倡导者）可缓冲——生命周期早期集中稀释之"
  tied_at:
    - "Intro：EO 正面效果'over-replicated... ad nauseam'（Wales 2021 引语——批评主流）→ 暗面 underdeveloped → EO-as-experimentation（variance-enhancing——Wales 2023 引语）→ Samsung Note 7 案例（$5B 损失）"
    - "Theory：质量机制（bold experimentation 压缩开发测试周期）+ UET 整合（COO power——质量倡导者）"
  untied_at:
    - "Theory H1-H3：EO→召回 + COO 调节 + 生命周期条件"
    - "Results：H1-H3 支持"
  antagonist: "EO 研究的正面导向（'privilege its beneficial outcomes'——下尾后果被忽视——'downsides substantially underdeveloped'）"
  antagonist_built_by:
    - "'over-replicated'... 'ad nauseam'（Wales 2021 引语——对主流的直白批评——引语加持）"
    - "variance-enhancing 逻辑（'creates a distribution of outcomes, both wins and losses'——Wales 2023——下尾的理论必然性）"
    - "Samsung Note 7 案例（2016——电池过热起火爆炸——$5B 损失——具名产品）"
```

### characters

```yaml
characters:
  protagonist: [entrepreneurial orientation（X）, product recalls（DV——下尾结果）]
  supporting:
    - "EO-as-experimentation（机制——variance-enhancing——质量压缩——'a breakdown in quality control within the experimentation process'）"
    - "COO power（调节——质量倡导者——嵌入运营纪律——'the executive responsible for internal operations and quality assurance'）"
    - "product life cycle（条件——早期集中→COO 注意力稀释——设计不确定性/质量风险更大）"
    - "Samsung Galaxy Note 7（具名案例——$5B 损失——消费者伤害）"
  ensemble: [1998-2021 美国物理消费品企业、CPSC 8,000 死亡证明/年（stakes 背景）]
```

### resolution_logic

`exploration` 拓荒（补 EO 暗面半区——variance-enhancing 下尾地图 + COO power 解药 + 生命周期条件化）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：EO 正面效果'over-replicated... ad nauseam'（Wales 2021——批评主流）→ 暗面 underdeveloped → EO-as-experimentation（variance-enhancing——Wales 2023 'both wins and losses'）→ Samsung Note 7（$5B 损失）→ CPSC 8,000 死/年"
  rising_action: "质量机制（bold experimentation 压缩开发测试周期——下尾风险）+ UET 整合（COO power——质量倡导者——嵌入运营纪律）+ 生命周期条件（早期集中→COO 注意力稀释）+ Methods（1998-2021 美国物理消费品企业）"
  climax: "Results——EO→召回正相关揭晓（variance-enhancing 的下尾具象化——'product recalls arguably represent a breakdown in quality control within the experimentation process'）"
  falling_action:
    - "COO power 调节（弱化 EO→召回——质量倡导者嵌入纪律——'a powerful COO is better positioned to embed operational discipline'）"
    - "生命周期条件（创新组合早期集中→COO 缓冲削弱——注意力稀释——'the demands on COO attention increase'）"
    - "稳健性"
  denouement: "Discussion——EO 下尾后果的实证（'we show how variance-enhancing strategies can also generate tangible operational
               failures due to weakened quality control'）；TMT 权力结构（COO 作为质量看门人——'how the composition and power
               structure of the TMT shape the realization of entrepreneurial experimentation'）"
```

### stakes

```yaml
stakes:
  theoretical: "EO 暗面 underdeveloped——'EO research continues to privilege its beneficial outcomes'——variance-enhancing 的下尾理论化缺失"
  practical: "EO 的召回风险（消费者安全——CPSC 8,000 死/年）；Samsung Note 7 $5B 损失；COO 权力作为治理缓冲"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: EO 收益版——EO→绩效/竞争优势（Rauch 元分析——'over-replicated' 主流）"
  - "讲法B: EO 变异性版——只做绩效波动（variance——抽象下尾——上尾研究为主）"
  - "讲法C: 召回前因版——召回的其他前因（激励/治理——既有召回文献——CEO 层面）"
  - "本文: 暗面半区补缺版——EO→召回（variance-enhancing 下尾具象化 + COO power 解药 + 生命周期条件）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "Samsung Galaxy Note 7（2016——电池过热起火爆炸——$5B 损失——具名产品+损失规模）；CPSC 8,000 死亡证明/年（stakes 具象）"
  rhetorical_question: "未见【已核实】——引语式批评开场（'over-replicated... ad nauseam'）"
  pacing_notes: "'over-replicated' 引语开场（批评主流）→ 暗面空白→ experimentation 逻辑→ UET 整合；climax=EO→召回揭晓；falling action COO 调节+生命周期条件"
  showing_telling: "'Double-Edged Sword'（标题双刃意象）；'variance-enhancing strategy'（方差增强——上尾/下尾分布意象）；'both wins and losses'（Wales 2023 引语）"
  voice: "ETP 实证口吻；'over-replicated... ad nauseam'（对主流的大胆批评——引语加持）；'substantially underdeveloped'（空白强调）"
```

### cross_paper_notes

- **half-domain-gap 五原型（EO 正面/暗面后果半区）**：malshe（维度）/wu（行为）/malik（情境——正常/危机）/mayo（跨域）/**lun2026（后果——正面/暗面）**——与 malik2025 同构（"后果半区"）。
- **与 kashmiri2017 的双刃家族对照**：kashmiri（自恋双刃——neglected-arena 人格空白）；lun（EO 双刃——half-domain-gap 暗面半区）——"双刃剑"两故事（人格 vs 姿态）。
- **recall 现象域十三讲法**（前因侧第 10——EO 姿态）。
- **与 malik2025 的 Samsung/Boeing 具名产品案例对照**（Note 7 $5B vs Boeing 157 死——具名产品案例家族）。
- **判别器记录**：half-domain-gap 判定基于 EO 后果的天然双极（正面/暗面——'Double-Edged Sword' 标题即双极意象）——与 malik2025 的"情境半区"同构。
