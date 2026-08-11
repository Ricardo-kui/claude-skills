# Story Blueprint — Gao, Xie, Wang & Chen (2015) JM

## 文件头

```yaml
id: gao2015
paper: "Gao, Xie, Wang & Chen (2015, JM) — Should Ad Spending Increase or Decrease Before a Recall Announcement? The Marketing–Finance Interface in Product-Harm Crisis Management"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（OCR 全文回读）→ ROBUST
source_records: [OCR parsed full text]
vault_reports:
  intro: null（OCR 全文回读）
  methods_results: null（OCR 全文回读：汽车召回 + 广告支出 2005-2012）
  story_arc: null
corpus_links:
  write-introduction: "标题问句（'Should Ad Spending Increase or Decrease...?'）+ 召回股价损失开场（Boston Scientific 13%/Toyota 22%）——路径待验证"
  write-methods: "事前广告调整 × 产品新旧 × 危害严重度——路径待验证"
  write-results: "条件缓冲（新/小→缓冲、老/大→加剧）+ 利润-股东价值冲突——路径待验证"
```

## Story

### one_liner

> 召回前调整广告支出能否缓冲股价损失？直觉与营销常识说"加广告=缓冲"——但条件是关键：**新产品+小危害时加广告缓冲损失；老产品+大危害时加广告反而加剧损失**；削减广告在新产品时总是更糟——广告是双刃的预防工具，且利润最大化与股东价值最大化在此冲突。

### knot

```yaml
knot:
  primary_type: consensus-puzzle         # 第八原型：'广告=缓冲工具'直觉共识被条件化（产品新旧 × 危害严重度）
  compound_types: []                    # 条件地图是发现，非子类型
  statement: "直觉共识——召回前加广告=缓冲股价损失（营销常识：广告提升品牌资产/消费者信心）；但条件关键：新产品+小危害时
              加广告缓冲（'softens the stock price loss'）；老产品+大危害时加广告加剧（'sharpens the loss'）；削减广告
              在新产品时总是更糟——广告是双刃预防工具——利润最大化与股东价值最大化冲突"
  tied_at:
    - "Intro：召回股价损失（Boston Scientific 13%/Cochlear 20%/Toyota 22%）→ 'identify effective preventive marketing strategies... to mitigate such financial damage'→ 事前广告作为战略工具"
    - "Theory：广告调整的条件效应（产品新旧 × 危害严重度——'depending on the direction of advertising adjustment and the recall characteristics'）"
  untied_at:
    - "Theory H1-H4：四条件预测"
    - "Results：条件缓冲/加剧 + 削减更糟 + 利润-价值冲突"
  antagonist: "'广告=缓冲'的营销直觉（事前广告提升品牌资产的常规逻辑——未考虑召回特征的信号解读）"
  antagonist_built_by:
    - "召回股价损失开场（Boston Scientific 13%/Cochlear 20%/Toyota 22%——具名事件四连）"
    - "条件排布（'either mitigate or amplify... depending on the direction of advertising adjustment and the recall characteristics'——双刃框架）"
    - "利润-股东价值冲突声明（'profit maximization and shareholder value maximization can conflict with each other'——营销-财务接口）"
```

### characters

```yaml
characters:
  protagonist: [prerecall ad spending adjustment（X——增/减）, postrecall stock value（DV）]
  supporting:
    - "产品新旧（条件 1——new product vs established model——信号含义不同）"
    - "危害严重度（条件 2——minor vs major hazard）"
    - "信号机制（加广告在特定条件下=欲盖弥彰——'sharpens the loss'）"
    - "Boston Scientific/Cochlear/Toyota/GM（具名案例——股价损失四连）"
  ensemble: [汽车召回 + 详细广告支出 2005-2012、事件研究、营销-财务接口]
```

### resolution_logic

`revelation` 揭幕（揭幕广告的条件地图——何时缓冲何时加剧——预防策略的细粒度 + 利润-价值冲突的揭示）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：召回股价损失（Boston Scientific 13%/Cochlear 20%/Toyota 22%/GM——具名四连）→ 召回频率增长+财务后果 → 'identify effective preventive marketing strategies' → 事前广告作为战略工具"
  rising_action: "广告条件理论（增/减 × 产品新旧 × 危害严重度——四条件预测）+ Methods（汽车召回 + 详细广告支出 2005-2012、事件研究）"
  climax: "Results——条件揭晓：加广告在新产品+小危害时缓冲（'softens the stock price loss'）、在老产品+大危害时加剧（'sharpens the loss'）——广告双刃首揭"
  falling_action:
    - "削减广告更糟（新产品时无论危害——'worsens the stock price loss when the recall involves a new product, regardless of the hazard'）"
    - "条件地图完整化（增/减 × 新旧 × 危害——四象限）"
    - "利润-股东价值冲突（'profit maximization and shareholder value maximization can conflict'——营销-财务接口的深层揭示）"
  denouement: "Discussion——事前广告作为危机管理预防工具（'prerecall advertising spending as a strategic tool'）；整合危机管理策略
               （'importance of developing an integrated crisis management strategy'——营销与财务的整合）"
```

### stakes

```yaml
stakes:
  theoretical: "'广告=缓冲'直觉未检验召回特征条件——预防营销策略的信号解读"
  practical: "召回前的广告决策（何时加何时减——条件地图）；利润与股东价值的冲突（整合危机管理）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 广告缓冲版——召回后加广告缓冲损失（Cleeren 2008——召回后广告——常规逻辑）"
  - "讲法B: 召回后果版——召回的市场反应（recall 文献主流——不接预防策略）"
  - "讲法C: 广告一般版——广告支出与绩效（广告文献——不接召回）"
  - "本文: 条件地图揭幕版——事前广告增/减 × 产品新旧 × 危害（双刃工具 + 利润-价值冲突）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "Boston Scientific（13%——植入除颤器 2010）/Cochlear（20%——Nucleus 5 植入物 2011）/Toyota（22% 两周——230 万辆 2010）/GM（'Stock Below IPO Price as Recall Talk Swirls'——USA Today 标题）——具名事件四连"
  rhetorical_question: "标题即问句（'Should Ad Spending Increase or Decrease Before a Recall Announcement?'——标题问句家族第 8 例——'Should' 型决策问句）"
  pacing_notes: "股价损失四连开场→预防策略动机→条件理论→四象限；climax=条件揭晓（缓冲/加剧并存）；falling action 削减更糟+利润冲突"
  showing_telling: "'softens... sharpens'（缓冲/加剧对立意象）；'either mitigate or amplify'（双刃框架）；'Stock Below IPO Price'（具名新闻标题引用）"
  voice: "JM 营销-财务接口口吻；'not merely bad luck'（否认偶然性）；'can conflict with each other'（冲突揭示）"
```

### cross_paper_notes

- **consensus-puzzle 八原型（广告条件化）**：pontikes/cutolo/gamache/kundro/han2020/fang2025/haunschild2015/**gao2015**——'广告=缓冲'直觉被条件违背。
- **recall 现象域二十二讲法**（预防广告 +1）。
- **与 fang2025 的广告家族对照（召回×广告双篇）**：fang（对手召回→替代品广告——竞争反应）；gao（自己召回前→广告调整——预防策略）——召回×广告的两面。
- **标题问句家族第 8 例**（'Should' 型决策问句）。
- **判别器记录**：consensus-puzzle 判定基于'广告=缓冲'直觉共识被条件化（产品新旧×危害——'depending on... recall characteristics' 原文锚）。
