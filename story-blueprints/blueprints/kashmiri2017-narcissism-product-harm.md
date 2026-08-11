# Story Blueprint — Kashmiri, Nicol & Arora (2017) JAMS

## 文件头

```yaml
id: kashmiri2017
paper: "Kashmiri, Nicol & Arora (2017, JAMS) — Me, Myself, and I: Influence of CEO Narcissism on Firms' Innovation Strategy and the Likelihood of Product-Harm Crises"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（Clippings 全文回读——vault 无报告）→ ROBUST
source_records: [parsed full text（Clippings——检索协议路径命中）]
vault_reports:
  intro: null（无 vault 报告——Clippings 全文回读）
  methods_results: null（无 vault 报告——全文回读：395 公司 2006-2010、媒体自恋测量、KLD 危机）
  story_arc: null
corpus_links:
  write-introduction: "black box problem（Lawrence 1997——demographic 噪音代理）+ Table 1 文献表格可视化——路径待验证"
  write-methods: "媒体自恋测量 + GLS/负二项/分数 logit/RE logit 多模型——路径待验证"
  write-results: "双刃揭晓（创新+/危机+2.25）+ 中介（competitive aggressiveness）+ 解药（marketing power）——路径待验证"
```

## Story

### one_liner

> upper echelon 研究用人口学变量（年龄/社会阶层/职能背景）作 CEO 心理的噪音代理（"black box problem"）——人格变量空白；本文打开黑箱：自恋 CEO 是创新的引擎（NPI +.20/激进创新 +.68）也是产品伤害危机的温床（+2.25）——"Me, Myself, and I" 的自恋者害人害己（竞争侵略性中介）；营销部门权力与顾客导向是治理缓冲。

### knot

```yaml
knot:
  primary_type: neglected-arena         # 第四原型：product-harm 前因的人格视角空白（'black box problem'——与 wowak2015 成因空白同族）
  compound_types: []                    # 双刃后果是发现，非子类型
  statement: "upper echelon 研究聚焦 demographic 变量（年龄/社会阶层/职能背景——噪音代理——'black box problem' [Lawrence 1997]）；
              CEO 人格在营销结果（创新+产品安全）上的研究空白——'largely ignoring the possible role of CEOs' personality traits'——
              自恋 CEO 是创新引擎也是危机温床（竞争侵略性中介）——'Me, Myself, and I' 的双刃"
  tied_at:
    - "Intro：upper echelon（demographic 噪音——black box problem）→ 双 RQ（创新+危机）→ 'CEOs largely irrelevant' 假设 vs 人格空白 → narcissism 引入（'individuals in leadership positions, on average, have a moderate to high level of narcissism' [Maccoby 2000]）"
    - "Theory：自恋双后果（创新：NPI/激进创新；安全：product-harm crisis——competitive aggressiveness 中介）"
  untied_at:
    - "Theory H1-H5：自恋→侵略性→双后果 + 中介 + marketing power 解药"
    - "Results：H4a 支持（危机 +2.25, p<.01）+ H2b/H4b 中介支持 + H5a/b 解药支持"
  antagonist: "upper echelon 研究的人口学导向（demographic 变量的噪音代理——'black box problem'——人格被忽略）"
  antagonist_built_by:
    - "Table 1 文献表格可视化（12 篇研究全为 demographic——'noisy, incomplete, and imprecise proxies'）"
    - "'black box problem'（Lawrence 1997 概念引用——心理学过程未知）"
    - "双 RQ 排布（创新+危机——'Are CEOs with certain personality traits likely to introduce more new products? Are firms led by CEOs with particular personalities more likely to encounter product-related controversies?'）"
```

### characters

```yaml
characters:
  protagonist: [CEO narcissism（X——媒体测量）, product-harm crisis（DV）+ NPIs/radical innovation（双后果）]
  supporting:
    - "competitive aggressiveness（中介——机制通道：+.023, p<.05——NPI .303/危机 .062 间接效应）"
    - "marketing department power（H5 解药——×自恋 −1.33, p<.05——mediated moderation via customer orientation）"
    - "customer orientation（mediated moderation 通道——×自恋 −1.38, p<.05）"
    - "consumers（受害方——产品伤害危机的承担者）"
  ensemble: [395 公司 2006-2010、媒体自恋测量、KLD 危机数据、GLS/负二项/分数 logit/RE logit、t-1 前置变量内生性]
```

### resolution_logic

`exploration` 拓荒（补人格前因战场——自恋双后果地图 + 竞争侵略性中介 + marketing power 解药条件化）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：upper echelon（demographic 噪音——'black box problem'——Table 1 文献表格 12 篇全 demographic）→ 双 RQ（创新+危机）→ 'CEOs largely irrelevant' 假设 → narcissism 引入（领导人普遍自恋 [Maccoby]——Chatterjee & Hambrick 先例）"
  rising_action: "自恋双后果理论（创新：NPI/激进创新；安全：product-harm crisis——competitive aggressiveness 中介）+ Methods（395 公司 2006-2010、媒体自恋测量、KLD 危机）"
  climax: "Results——H4a 揭晓：自恋 → product-harm crisis（β=+2.25, p<.01）——'Me, Myself, and I' 的自恋者害人害己（创新 +.20/+.68 与危机 +2.25 并置）"
  falling_action:
    - "H1 中介首站（competitive aggressiveness +.023, p<.05——自恋→侵略性）"
    - "H2b/H4b 中介（NPI 间接 .303/危机间接 .062——CI 排除 0——侵略性作为机制通道——% mediated 18.3%/7.5%）"
    - "H3b 不支持（激进创新中介 n.s.——诚实报告——激进创新由直接效应驱动）"
    - "H5a/b 解药（marketing power ×自恋 −1.33, p<.05——mediated moderation：marketing power→customer orientation→危机缓解——部分中介）"
    - "内生性（t-1 前置变量——Chatterjee & Hambrick 法——自恋吸引型公司）"
  denouement: "Discussion——自恋 CEO 的创新收益与安全代价（营销含义）；marketing department power/customer orientation 作为治理缓冲
               （'marketing power 是自恋危机的解药'）；对营销部门的战略含义"
```

### stakes

```yaml
stakes:
  theoretical: "upper echelon 的人格变量空白（black box problem——demographic 噪音代理）；营销结果（创新/安全）与 CEO 人格的关系未研究"
  practical: "自恋 CEO 的创新收益与产品伤害风险（消费者安全）；营销部门权力的治理缓冲（'marketing power 减少自恋危机'）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 人口学变量版——年龄/社会阶层/职能背景（upper echelon 主流——Table 1 文献现状）"
  - "讲法B: 创新成果版——只做自恋→创新（Chatterjee & Hambrick 战略活力/并购——正面叙事）"
  - "讲法C: 危机激励版——product-harm 前因只做企业激励（Kashmiri & Brower/Nagler/Kopalle——忽视人格）"
  - "本文: 人格双刃版——自恋→创新+危机（'Me, Myself, and I'——竞争侵略性中介 + marketing power 解药）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "无具名企业（395 公司样本——媒体自恋测量）；'Me, Myself, and I' 标题（自恋者第一人称——showing 手段）"
  rhetorical_question: "双 RQ 开场问句（'Are CEOs with certain personality traits likely to introduce more new products? Are firms... more likely to encounter product-related controversies?'——开场双问——非修辞 pivot）"
  pacing_notes: "black box→双 RQ→自恋引入→双后果理论→中介+解药；climax=H4a 危机揭晓（+2.25）；falling action 中介+调节+内生性"
  showing_telling: "'Me, Myself, and I'（标题——自恋的第一人称意象）；'black box problem'（Lawrence 概念引用）；'Surprisingly, existing research provides us very few answers'（意外性开场）"
  voice: "JAMS 营销实证口吻；'Surprisingly'（意外性强调）；'dearth of work'（稀缺性措辞）"
```

### cross_paper_notes

- **neglected-arena 四原型（成因前因家族）**：desai2012（注意力转向）/ park2013（主题失衡）/ eilert2017（prerecall 过程）/ **Kashmiri 2017（人格视角空白——'black box problem'——与 wowak2015 的成因空白 compound 呼应——成因研究的人格通道）**。
- **recall 现象域十一讲法**（8 前因 + Kashmiri 人格——前因侧第八视角）。
- **与 wowak2015 的 CEO 特质对照**：wowak（期权激励——外部激励）；Kashmiri（自恋——内部人格）——CEO 驱动召回的前因两端（激励 vs 人格）。
- **与 malik2025 的营销后果对照**：malik（CEO 动机→IM 战术——沟通层）；Kashmiri（CEO 人格→创新+安全——战略层）——营销期刊的 CEO 故事。
- **判别器记录**：neglected-arena 判定基于前因子域空白（人格变量——'largely ignoring'）。
