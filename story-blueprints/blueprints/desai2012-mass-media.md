# Story Blueprint — Desai (2012) AMJ

## 文件头

```yaml
id: desai2012
paper: "Desai, V. M. (2011, AMJ) — Mass Media and Massive Failures: Determining Organizational Efforts to Defend Field Legitimacy Following Crises"   # ⚠️ 勘误（2026-08-09）：id 沿用 desai2012，实为 2011（DOI amj.2011.60263082，AMJ 54(2)；desai2011 memory 即同篇，非不同论文）
distilled_sections: [intro, theory, methods, results]      # 2026-08-09 读全文定稿（parsed_texts/mvp30/）→ ROBUST
source_records: [project-mvp30-desai2012-intro, project-mvp30-desai2012-theory]
vault_reports:
  intro: "narrative_analysis/introduction/mvp30/fine_grained/batch_3/desai2012_amj_distilled_introduction.md"
  theory: "narrative_analysis/theory/mvp30/fine_grained/batch_3/desai2012_amj_distilled_theory.md；batch_2026-07-09/mass_media_massive_failures_distilled_theory.md"
  methods_results: "parsed_texts/mvp30/Mass Media and Massive Failures Determining Organizational Efforts to Defend Field Legitimacy Following Crises Academy of Management Journal.md（2026-08-09 全文定稿）"
  story_arc: null
corpus_links:
  write-introduction: "01-despite-progress-unaddressed 变体M（Inadequacy 加深 Incompleteness 双层 Tension）；01-hook-to-literature 变体E（叙事回响型过渡）；contributions 变体I（延迟贡献声明型）"
  write-theory: "moderation.md Competing Baseline → Moderation Resolution 模式；Extension Logic 型；construct_definition.md 变体F（Typology Alignment 定义型）"
  write-methods: "条件 FE 负二项（全零面板自动剔除的审计）；手工文本编码（347 声明 → 三类型，kappa 0.91）；媒体分层随机抽样（4,828 篇 → 705 安全相关，tenor 编码 kappa 0.81/0.95）"
  write-results: "主效应为负 + 交互转正（条件化叙事）；H2 不支持诚实报告；稳健性三角（严重度替代/退出检验/有效性检验）"
```

## Story

### one_liner

> 媒体曝光酿成的大失败之后，组织会站起来保卫**整个领域**的合法性——但"何时"会？铁路事故越多，企业反而越少开口辩护（主效应为负）——除非整个领域的目光都盯着安全问题（审视度高）时，它们才站出来；而与事故企业越相似、越可能被殃及的企业，反而越沉默（怕被污名牵连）。

### knot

```yaml
knot:
  primary_type: neglected-arena   # 双原型（desai2012 + park2013）：子域空白 + 注意力转移
  compound_types: []   # 内层 Inadequacy（注意力转移）是成因
  statement: "危机后组织为何（以及何时）投入 effort 保卫 field-level legitimacy？现有文献聚焦 firm-level 合法性防御，field-level 防御无理论框架——且主效应反直觉为负（field accidents 越多防御声明越少），条件（审视/相似性）决定何时防御"
  tied_at:
    - "Intro P3：直接缺口（field-level defensive response 无理论解释）"
    - "Intro P4：深层 Inadequacy——制度理论'从 stability 转向 change'的注意力转移"
    - "Theory：competing baseline（defend vs avoid 两派推论）→ H1-H4 全调节"
  untied_at:
    - "Results：主效应为负（反直觉）+ H1 交互正（fieldwide scrutiny 高时防御增加）——'何时防御'揭晓"
    - "Results：H3 负交互（core similarity——相似企业更沉默，stigma）、H4 正交互（external causes——可外归因时更防御）"
  antagonist: "文献的集体注意力（制度理论转向 change，稳定导向的领域防御成盲区）+ 反直觉的现实（事故越多越沉默——防御有风险，不防御是默认）"
  antagonist_built_by:
    - "双层 Tension（变体M）：P3 直接缺口 + P4 'Indeed, although [theory] originally aimed to explain [X], much attention has turned to [Y]'"
    - "Hook 叙事回响（变体E）：媒体大失败案例 scale-up 为系统问题"
```

### characters

```yaml
characters:
  protagonist: [组织对 field legitimacy 的防御 effort (Y，defensive institutional statements 计数), others' accidents (X)]
  supporting:
    - "issue scrutiny（fieldwide / focal 双变量——媒体负面审视：H1/H2）"
    - "core similarity（passenger service——与被事故企业共享核心特征：H3，stigma 逻辑）"
    - "externally-induced similarity（collisions——可外归因的事故相似性：H4）"
  ensemble: [36 家 class I 铁路 1980-2003（391 company-years，deregulation 制度断点辩护）、控制变量（自身事故/严重度/规模/并购/年龄）]
```

### resolution_logic

`exploration` 拓荒 + 条件化——**competing baseline → moderation resolution**：先让 defend vs avoid 对峙，再用条件（审视度/相似性）决定胜负。研究者是拓荒者+条件测绘者：地图上没人画过的 field-level 防御被画上，且标出"何时防御"的等高线（主效应负、条件转正——防御不是默认，是条件触发的勇敢行为）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：媒体 watchdog → massive failures → field-level 合法性防御（Hook 具名案例 + 叙事回响）；P3 直接缺口 + P4 深层原因（双层 Tension）；7 段标准 Intro，Stakes 嵌入 Tension"
  rising_action: "Theory：Competent Arguments 透镜（defend vs avoid 对峙）；Extension Logic（Oliver 1991 firm-level → field-level）；Typology Alignment 定义 defensive institutional statements；H1-H4 全调节（无纯主效应假设）；Methods：36 家铁路 1980-2003（deregulation 断点辩护）；DV=手工编码 347 声明（三类型：领域优越/外归因/进步沟通，kappa 0.91）；IV=他人事故数；审视=媒体分层随机抽样 4,828 篇 tenor 编码；条件 FE 负二项（全零面板自动剔除 391→234）"
  climax: "Results Tables 2-3：主效应为负（他人事故越多，防御声明越少——反直觉揭晓）+ H1 交互正（fieldwide scrutiny 高时防御增加，支持）——'何时防御'的答案：防御是条件触发的"
  falling_action:
    - "H2 不支持（focal firm scrutiny 交互不显著）——当场诚实报告"
    - "H3 支持（core similarity 负交互——相似企业更沉默，stigma 逻辑）"
    - "H4 支持（externally-induced similarity 正交互——可外归因时更防御）"
    - "稳健性三角：严重度替代测量（成本/伤者数）/ stigma 退出检验（相似企业更可能退出 passenger service——logistic Table 4）/ 防御有效性检验（防御声明降低 fieldwide scrutiny——Table 5，'PR 能影响整个领域审视'的首个直接证据）"
  denouement: "Discussion：field-level defensive work 理论贡献——与 Maguire & Hardy (2009) 两点差异（本文回答'哪些企业会防御'；且防御可以成功——M&H 案例失败的对照反转）；limitations（stakeholder 异质性、单行业 collectivism 情境）；未来方向（正向事件的领域推广——'好事也值得保卫'）"
```

### stakes

```yaml
stakes:
  theoretical: "制度理论关心'领域合法性如何被维持'，但注意力已转向 change；不补这块，'危机如何重塑领域'就只有 firm-level 半张图——且防御行为有风险（非直接涉事企业辩护=引火烧身），'何时有人敢做'是理论空白"
  practical: "媒体曝光后的组织行为：整个行业在事故后是集体沉默还是集体辩护？——审视度高时防御增加、相似企业沉默（stigma 自保），危机公关的行业层含义"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: firm-level 防御故事 — '危机后组织保卫自己的合法性'（已有文献的讲法；level 下移）"
  - "讲法B: 制度稳定叙事 — '制度是稳定的，合法性危机是例外'（旧制度理论视角）"
  - "讲法C: 媒体责任归属故事 — '媒体夸大失败、组织被迫回应'（换 antagonist 为媒体）"
  - "本文: 拓荒+条件化版 — 补上 field-level 战场，且不选边：defend/avoid 各有道理，审视度与相似性决定胜负。选择理由：level 上移产生新构念；主效应为负 + 条件转正把贡献从'发现'升为'解释何时'——防御不是默认，是条件触发的勇敢"
```

### storytelling_tools

```yaml
storytelling_tools:
  human_face: "具体企业声明：Conrail '99.99 percent reach their destination without incident'、Illinois Central 'city officials share IC's concerns'、CSX 'identifying and evaluating best safety practices'——防御声明的三类型各配具名实例"
  rhetorical_question: "待补"
  pacing_notes: "Theory 是'对峙→条件化'序列；climax 的主效应为负是意外转向（读者预期事故多→防御多，实际相反）——反直觉即悬念；falling action 三角稳健性逐层加固（严重度→退出→有效性）"
  showing_telling: "三类型声明的具名实例（showing——防御长什么样）；'99.99%' 数字作 telling 锚"
  voice: "第一人称单数 I（Desai 手工编码的个人在场——'I read and coded all releases'）；透明排除段（'other factors may also influence... but I do not consider them here'）"
```

### cross_paper_notes

- **与 Park 2013（neglected-arena 双原型）**：desai = 注意力转向（学科转向，field-level 空白）；park2013 = 主题失衡（access 已做/treatment 空白）——同型两种"注意力偏斜"来源。
- **与 DesJardine 2023（注意力-缺口家族）**：desai = 被动遗忘（静态遗漏）；desjardine2023 = 注意力在场且再生产盲区（irony 动态版）——'文献造成缺口'的两种讲法。
- **与 Malshe 2015（条件化家族）**：malshe 主效应非单调（floodlight 双转折）；desai 主效应为负 + 条件转正——'反直觉主效应 + 条件化'的两种形态。
