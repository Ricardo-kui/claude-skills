# Story Blueprint — （2025, JCF）The Information Advantage of Industry Common Owners and Crash Risk

## 文件头

```yaml
id: crash_risk
paper: "（2025, JCF — Journal of Corporate Finance）— The Information Advantage of Industry Common Owners and Its Spillover Effect on Stock Price Crash Risk"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（共同所有权/07 原文）→ ROBUST
source_records: [parsed full text（共同所有权/07 原文）]
vault_reports:
  intro: null（共同所有权文件夹原文回读）
  methods_results: null（全文回读：美国 1980-2017、OLS + 多测量）
  story_arc: null
corpus_links:
  write-introduction: "两解释相反预测（constraint-based vs information-based——'predicts an opposite effect'）+ 说明性模型（A/B 两企业 + I/J 两机构）——路径待验证"
```

## Story

### one_liner

> 共同所有权对崩盘风险的影响——既有"约束解释"（第二矩效应——波动/联动）预测**更高**崩盘风险——本文"identifying an information-based spillover story that predicts an **opposite** effect"：行业共同所有者的信息优势（区分企业特定 vs 行业-wide 坏消息）使其避免因同行虚假溢出信号而抛售（"smart exit"）——**降低**崩盘风险——1980-2017 实证：有行业共同所有者的企业崩盘风险显著更低。

### knot

```yaml
knot:
  primary_type: paradigms-at-war        # 第八原型：constraint-based vs information-based 两解释相反预测——实证裁决
  compound_types: []                    # 信息优势/智能退出是机制，非子类型
  statement: "共同所有权对崩盘风险——既有'约束解释'（'second moment' 效应——indexing/资本流出约束——'induce higher return
              volatilities and return co-movements'——预测更高崩盘风险）；本文信息优势解释（'identifying an information-based
              spillover story that predicts an opposite effect'）——行业共同所有者信息优势（区分企业特定 vs 行业-wide 坏消息）
              →'smart exit'（避免虚假溢出信号的错误抛售）→降低崩盘风险——1980-2017 实证：有行业共同所有者→崩盘风险显著更低"
  tied_at:
    - "Intro：行业共同所有者上升（10%→80%+——1980-2017）→ 约束解释（既有——第二矩效应）→ 'information-based spillover story that predicts an opposite effect'（相反预测声明）→ 说明性模型（A/B 企业 + I/J 机构——机构 J 的智能退出）"
    - "Theory：信息优势机制（多行业持股——信息协同——'smart exit'）"
  untied_at:
    - "Theory H1-H3：共同所有权→崩盘风险降低"
    - "Results：OLS 支持（有共同所有者→负偏度显著更低）+ 多测量 + FE"
  antagonist: "共同所有权的约束解释（'second moment' 效应——波动/联动——'uninformed trading may narrate average institutional investors' impact'）"
  antagonist_built_by:
    - "'predicts an opposite effect'（相反预测声明——与既有解释对立）"
    - "说明性模型（A/B 企业 + 块持有者 I vs 共同所有者 J——'institution J understands that the underlying causes of write-offs were isolated to firm B and thus chooses not to sell'——智能退出的故事化）"
    - "'smart exit'（概念命名——有知退出 vs 盲目抛售）"
```

### characters

```yaml
characters:
  protagonist: [industry common ownership（X）, stock price crash risk（DV——负偏度）]
  supporting:
    - "信息优势机制（多行业块持有——信息协同——区分企业特定/行业-wide 坏消息）"
    - "smart exit（'informed common owners avoid selling on false spillover signals'——稳定作用）"
    - "约束解释（既有——indexing/资本流出——第二矩效应——被裁决的一派）"
    - "机构 A/B 模型（块持有者 I vs 共同所有者 J——说明性故事）"
  ensemble: [美国 1980-2017（10%→80%+ 企业有行业共同所有者）、OLS + 多测量 + 控制（机构所有权/块所有权/共同所有权）、FE]
```

### resolution_logic

`arbitration` 仲裁（两解释相反预测实证裁决——信息优势解释胜出——stabilizing 确认）+ 多测量稳健。

### five_acts

```yaml
five_acts:
  exposition: "Intro：行业共同所有者上升（10%→80%+）→ 约束解释（第二矩——波动/联动）→ 'information-based spillover story that predicts an opposite effect'（相反预测）→ 说明性模型（A/B + I/J——J 的智能退出）"
  rising_action: "信息优势理论（多行业块持股——信息协同——'smart exit'——避免虚假溢出信号抛售）+ Methods（美国 1980-2017、OLS、多测量）"
  climax: "Results——稳定作用揭晓：有行业共同所有者的企业崩盘风险显著更低（'firms with at least one industry common owner have significantly lower stock price crash risk'——信息优势解释胜出）"
  falling_action:
    - "多测量稳健（行业共同所有权/崩盘风险替代测量——'holds with alternative measures'）"
    - "控制完备（机构所有权/块所有权/共同所有权——'after controlling for various institutional investor characteristics'）"
    - "FE + 已知崩盘风险决定因素"
  denouement: "Discussion——共同所有权的稳定作用（'a stabilizing effect is provided by the more informed industry common owners'）；
              信息优势的崩盘含义（坏消息囤积的抑制——'discourage the focal firm's management from hoarding bad news'）；
              'uninformed trading' vs 'smart exit'（盲目交易与有知退出的分野）"
```

### stakes

```yaml
stakes:
  theoretical: "共同所有权崩盘效应——约束解释之外的信息优势解释（'identifying an information-based spillover story that predicts an opposite effect'）"
  practical: "崩盘风险（'abrupt large drops in stock prices'——投资者财富）；共同所有权的稳定功能（金融市场的稳定作用）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 约束解释版——共同所有权→更高波动/联动（既有——'second moment' 效应）"
  - "讲法B: 崩盘决定版——崩盘风险的决定因素（负偏度文献——不接共同所有权）"
  - "讲法C: 治理版——共同所有权治理（监督/退出——不接崩盘）"
  - "本文: 稳定作用揭幕版——信息优势→崩盘降低（'predicts an opposite effect'——smart exit + 多测量）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "说明性模型故事化（机构 I vs 机构 J——'institution J's blockholding in firm B allows it... to acquire better information'——小故事讲述）；无具名企业"
  rhetorical_question: "未见【已核实】"
  pacing_notes: "共同所有者上升→约束解释→相反预测→说明性模型→实证；climax=稳定作用揭晓；falling action 多测量+控制完备"
  showing_telling: "'predicts an opposite effect'（相反预测声明）；'smart exit'（有知退出命名——vs 盲目抛售）；'over concerned'（投资者过度担忧意象——虚假溢出信号）；说明性模型（A/B/I/J 的故事化）"
  voice: "JCF 金融实证口吻；'Our contribution is identifying'（贡献定位）；'we do not argue that this is the only channel'（谦虚限定）"
```

### cross_paper_notes

- **paradigms-at-war 八原型（两解释相反预测裁决）**：zhou/wowak2025/park2025/shen/bendig/haunschild2004/csr_decoupling_china/**crash_risk**——'predicts an opposite effect'（原文锚）。
- **共同所有权家族九篇成型**（+crash_risk 崩盘稳定——paradigms 第二篇）。
- **与 csr_decoupling 的裁决对照**：csr（协调 vs 合谋——CSR 治理）；crash（约束 vs 信息——崩盘稳定）——共同所有权两场"相反预测裁决"。
- **判别器记录**：paradigms-at-war 判定基于两解释相反预测（'predicts an opposite effect'——原文锚）实证裁决。
