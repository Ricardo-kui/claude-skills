# Story Blueprint — DesJardine, Li & Shi (2025) AMJ

## 文件头

```yaml
id: desjardine2025
paper: "DesJardine, Li & Shi (2025, AMJ) — Information-Based Competition: The Case of Rival Owners in Rating Agencies"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（OCR 全文回读）→ ROBUST
source_records: [OCR parsed full text]
vault_reports:
  intro: null（OCR 全文回读）
  methods_results: null（OCR 全文回读：MSCI ESG 评级 2,787 公司）
  story_arc: null
corpus_links:
  write-introduction: "'information-based competition' 新概念引入 + 评级渗透场景（MSCI——'leading publicly traded rating agency'）——路径待验证"
  write-theory: "动态信息竞争理论（声誉威胁/机会——投资者的干预动机）——路径待验证"
  write-results: "对手投资者持股评级机构→目标公司评级下降——路径待验证"
```

## Story

### one_liner

> 竞争不仅发生在产品市场——还发生在信息领域：竞争对手的投资者若同时持股评级机构，目标公司的 ESG 评级会被压低——"信息型竞争"（information-based competition）——所有权赋予投资者影响信息中介的能力——声誉威胁与机会决定投资者何时发动信息攻击。

### knot

```yaml
knot:
  primary_type: neglected-arena         # 第八原型：竞争动态研究的信息中介维度空白（'introduces the concept of information-based competition'）
  compound_types: []                    # 动态声誉条件是机制，非子类型
  statement: "竞争动态研究——产品更新/营销/并购等行动（'short-term tactical actions... as well as large and long-term strategic moves'）；
              信息中介维度空白——'introduces the concept of information-based competition'——对手投资者持股评级机构→目标公司
              ESG 评级下降（'firms receive less favorable ratings from rating agencies in which their rivals' investors have
              greater ownership'）——声誉威胁/机会决定投资者的干预动机"
  tied_at:
    - "Intro：竞争行动谱系（战术→战略）→ 负面信息披露先例（Quiznos 诽谤 Subway/Cao et al. 社交媒体负面新闻）→ 信息中介引入（MSCI——'leading publicly traded rating agency'）→ 共同所有权渗透"
    - "Theory：动态信息竞争理论（声誉威胁/机会——投资者的干预动机）"
  untied_at:
    - "Theory H1-H4：评级下降 + 声誉条件"
    - "Results：对手投资者持股→目标评级下降（2,787 公司）"
  antagonist: "竞争动态研究的传统行动导向（'a variety of competitive actions'——产品/营销/并购——信息中介渗透被忽略）"
  antagonist_built_by:
    - "竞争行动谱系（'short-term tactical actions... as well as large and long-term strategic moves'——传统清单）"
    - "负面信息披露先例（Quiznos 诽谤 Subway——'defamed Subway'；Cao et al.——'an emerging corporate strategy'——信息战的既有线索）"
    - "信息中介的权威性（'seen as trusted authorities... shape stakeholders' attitudes'——但'have their own economic agendas'——可被渗透）"
```

### characters

```yaml
characters:
  protagonist: [rival owners' ownership in rating agencies（X）, target firm's ESG rating（DV——MSCI）]
  supporting:
    - "信息中介渗透（机制——'ownership bestows investors with influence over information intermediaries'）"
    - "声誉威胁/机会（条件——'reputational threats and opportunities faced by the firm and its rivals'——干预动机）"
    - "target vs attacker（竞争动态术语——'firms that have their ratings altered by investors in rival firms'）"
    - "MSCI（中介——'leading publicly traded rating agency'——具名机构）"
  ensemble: [MSCI ESG 评级 2,787 公司、共同机构投资者、Quiznos/Subway/Cao et al. 先例]
```

### resolution_logic

`revelation` 揭幕（揭幕信息型竞争——评级渗透机制 + 声誉条件化——"竞争的新战场"）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：竞争行动谱系（战术→战略）→ 负面信息披露先例（Quiznos 诽谤 Subway/Cao et al. 社交媒体）→ 信息中介引入（MSCI——'leading publicly traded rating agency'——信任权威但有经济议程）→ 共同所有权渗透"
  rising_action: "动态信息竞争理论（所有权→影响力→评级倾斜——'rating discounts... shaped by the reputational threats and opportunities'）+ Methods（MSCI ESG 评级 2,787 公司）"
  climax: "Results——渗透揭晓：目标公司 ESG 评级与对手投资者在评级机构的持股负相关（'a target firm's ESG rating by MSCI is negatively associated with the level of ownership its rivals' institutional investors have in MSCI'）——信息型竞争首揭"
  falling_action:
    - "声誉威胁条件（目标/对手的声誉威胁增强攻击动机——'reputational threats... motivate and enable investors'）"
    - "声誉机会条件（声誉机会同样塑造干预——'reputational opportunities'——动态完整）"
    - "稳健性"
  denouement: "Discussion——信息型竞争概念（'introduces the concept of information-based competition'）；评级机构的冲突
               （'conflicts of interest that permeate information intermediaries'）；条件（'the conditions under which investors
               engage in information-based competitive attacks'）"
```

### stakes

```yaml
stakes:
  theoretical: "竞争动态的信息中介维度空白——'how and when information about a firm may be shaped by competitive forces operating through information intermediaries'"
  practical: "评级被对手投资者渗透（ESG 评级操纵——投资者决策）；信息中介的治理（信任权威的可渗透性）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 竞争行动版——产品/营销/并购竞争（竞争动态主流——'short-term tactical actions... strategic moves'）"
  - "讲法B: 共同所有权版——共同所有权的协调/竞争效应（IO 主流——反竞争/亲竞争——不接评级）"
  - "讲法C: 评级决定版——评级的决定因素（评级文献——公司特征——不接竞争渗透）"
  - "本文: 信息型竞争揭幕版——对手投资者渗透评级（'information-based competition'——声誉威胁/机会条件）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "Quiznos 诽谤 Subway（具名企业——'defamed Subway'）；MSCI（具名机构——'leading publicly traded rating agency'）；Washington Post/Yelp（信息中介列举）；Cao et al.（'an emerging corporate strategy'）"
  rhetorical_question: "未见【已核实】"
  pacing_notes: "竞争行动谱系→信息战先例→中介引入→渗透理论→声誉条件；climax=渗透揭晓（负相关）；falling action 双声誉条件"
  showing_telling: "'information-based competition'（新概念命名——竞争的新战场）；'tainting the owned rating agency's coverage'（污染意象）；'targets and attackers'（竞争动态术语）"
  voice: "AMJ 理论实证口吻；'introduces the concept'（概念引入）；'in this spirit'（先例承接）"
```

### cross_paper_notes

- **neglected-arena 八原型（信息竞争子域）**：desai2012/park2013/eilert2017/kashmiri2017/kalaignanam2013/pupovac2025/hoffmann2024/**desjardine2025**。
- **DesJardine 系同作者**：desjardine2022（common ownership→CSR）/desjardine2023（监督反果）/desjardine2025（信息竞争）——DesJardine 三篇三类型（overlooked/irony/neglected）。
- **共同所有权家族第四篇**（desjardine2025 用共同所有权做渗透机制——与 anton2025/denicolo2025/desjardine2022 连接）。
- **判别器记录**：neglected-arena 判定基于竞争动态的信息中介维度空白（'introduces the concept'——原文锚）。
