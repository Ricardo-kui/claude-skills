# Story Blueprint — Chen, Ganesan & Liu (2009) JM

## 文件头

```yaml
id: chen2009
paper: "Chen, Ganesan & Liu (2009, JM) — Does a Firm's Product-Recall Strategy Affect Its Financial Value? An Examination of Strategic Alternatives During Product-Harm Crises"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（OCR 全文回读）→ ROBUST
source_records: [OCR parsed full text]
vault_reports:
  intro: null（OCR 全文回读）
  methods_results: null（OCR 全文回读：CPSC 1996-2007、事件研究 + 横截面 + Heckman）
  story_arc: null
corpus_links:
  write-introduction: "召回策略四分类（denial/involuntary/voluntary/super-effort——公司响应连续体）+ 'contrary to the conventional wisdom' 反直觉——路径待验证"
  write-methods: "事件研究 CAR + 横截面 + 中介 + Heckman——路径待验证"
  write-results: "主动策略反果（更负面）+ 信号解释——路径待验证"
```

## Story

### one_liner

> 直觉与消费者视角说主动召回=负责任=该获奖励——但"contrary to the conventional wisdom"：市场把主动策略解读为损失严重的信号（"no choice but to act swiftly"）——主动召回反而带来更负面的股票回报——召回策略的投资者视角与消费者视角分歧。

### knot

```yaml
knot:
  primary_type: irony-reversal          # 第七原型：策略反果（proactive→更负面——市场信号——反果形态第五例，与 wowak2015/darby2024 同构）
  compound_types: []                    # 信号解释是机制，非子类型
  statement: "直觉共识——主动召回=负责任=应获市场奖励（消费者视角：更积极的召回缓冲品牌损害）；但'contrary to the conventional
              wisdom'：市场把主动策略解读为损失严重信号（'no choice but to act swiftly'）——主动召回反而带来更负面股票回报——
              投资者与消费者的视角分歧"
  tied_at:
    - "Intro：召回策略四分类（denial/involuntary/voluntary/super-effort——公司响应连续体）→ 'whether a proactive strategy helps attenuate the effects'——'theoretical and empirical evidence... equivocal'"
    - "Theory：信号机制（市场解读主动=严重损失）"
  untied_at:
    - "Theory H1-H3：策略→股票回报"
    - "Results：主动更负面（'regardless of firm and product characteristics'）+ 信号解释 + 横截面/中介/Heckman"
  antagonist: "'主动=好'的常规智慧（Dawar & Pillutla 2000/Siomkos & Kurzbard 1994——消费者视角的正向结论）"
  antagonist_built_by:
    - "四分类连续体（denial→super-effort——'proactively and responsibly' 的正向语境）"
    - "'contrary to the conventional wisdom'（反直觉声明）"
    - "投资者 vs 消费者视角分歧（'investors may view proactive recall strategies differently from consumers'——信号解读）"
```

### characters

```yaml
characters:
  protagonist: [recall strategy（X——proactive vs passive）, firm financial value（DV——股票回报）]
  supporting:
    - "信号机制（市场解读主动=严重损失——'the consequence of the product-harm crisis is sufficiently severe'）"
    - "investors vs consumers（视角分歧——消费者缓冲品牌损害/投资者读信号）"
    - "firm reputation（低声誉企业更常用主动策略——'little buffer against the negative impact'）"
    - "Vioxx/Topps（具名案例——Merck $45.07→$33.00 单日/Topps 破产 2,170 万磅）"
  ensemble: [CPSC 召回 1996-2007、事件研究 CAR + 横截面 + 中介 + Heckman、Merck Vioxx/Topps 案例]
```

### resolution_logic

`revelation` 揭幕（揭幕策略的投资者视角——信号反果——市场解读机制 + 声誉条件化）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：召回代价（Merck Vioxx 单日 $45.07→$33.00/Topps 破产 2,170 万磅）→ 四分类响应连续体（denial→super-effort——'proactively and responsibly'）→ 'theoretical and empirical evidence... equivocal'"
  rising_action: "信号理论（市场解读主动=损失严重——'no choice but to act swiftly'）+ Methods（CPSC 1996-2007、事件研究 + 横截面 + 中介 + Heckman）"
  climax: "Results——反直觉揭晓：主动策略比被动策略带来更负面股票回报（'contrary to the conventional wisdom'——'regardless of firm and product characteristics'）"
  falling_action:
    - "信号解释（市场解读主动=严重损失信号——'investors may view proactive recall strategies differently from consumers'）"
    - "声誉条件（主动策略更常被低声誉企业使用——'little buffer'——信号含义）"
    - "横截面/中介/Heckman 稳健（策略是异常回报的主要影响因素——内生性处理）"
  denouement: "Discussion——策略的投资者视角（召回策略须考虑市场信号解读——'firms need to be sensitive to how the stock market might interpret proactive strategies'）；
              管理含义（主动策略的潜在负面后果）"
```

### stakes

```yaml
stakes:
  theoretical: "'主动=好'的常规智慧未检验投资者视角——召回策略的市场信号解读未知"
  practical: "主动召回策略的股票市场负面后果（Merck 单日暴跌/Topps 破产）；管理者须警惕信号解读"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 主动=好版——主动召回缓冲品牌损害（Dawar & Pillutla/Siomkos & Kurzbard——消费者视角主流）"
  - "讲法B: 召回后果版——召回本身的市场反应（recall 文献主流——不区分策略）"
  - "讲法C: 策略分类版——只做召回策略类型学（响应连续体——不接市场反应）"
  - "本文: 策略反果揭幕版——主动→更受罚（市场信号解读——'contrary to the conventional wisdom'）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "Merck Vioxx（2004 单日 $45.07→$33.00——具名企业+单日暴跌）；Topps 破产（2,170 万磅冷冻汉堡）；Toyota 情境"
  rhetorical_question: "未见【已核实】"
  pacing_notes: "召回代价开场（Vioxx/Topps）→四分类→equivocal→信号理论；climax=主动反果揭晓；falling action 信号+声誉+三稳健"
  showing_telling: "'contrary to the conventional wisdom'（反直觉声明）；'company response continuum'（响应连续体意象——denial→super-effort）；'no choice but to act swiftly'（信号意象）"
  voice: "JM 实证口吻；'equivocal'（证据分歧）；'surprising result'（意外标记）"
```

### cross_paper_notes

- **irony-reversal 七原型（策略反果——反果形态第五例）**：wowak2015（期权）/darby2024（持股）/desjardine2023（监督）/**chen2009（策略——主动→更受罚）**——治理/策略机制反果家族持续钉死。
- **recall 现象域十八讲法**（策略维度 +1——主动/被动）。
- **与 fang2025 的对照（同一主动性的两面）**：fang（替代品牌降广告——威胁主导）；chen（主动召回——信号反果）——"主动行为在召回语境的反直觉后果"家族。
- **判别器记录**：irony-reversal 判定基于策略产生与预期相反结果（'contrary to the conventional wisdom'——原文锚）。
