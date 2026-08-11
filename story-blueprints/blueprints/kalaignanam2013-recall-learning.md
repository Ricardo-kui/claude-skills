# Story Blueprint — Kalaignanam, Kushwaha & Eilert (2013) JM

## 文件头

```yaml
id: kalaignanam2013
paper: "Kalaignanam, Kushwaha & Eilert (2013, JM) — The Impact of Product Recalls on Future Product Reliability and Future Accidents: Evidence from the Automobile Industry"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（vault fine 报告 + OCR 全文回读）→ ROBUST
source_records: [vault fine intro/theory 报告, OCR parsed full text]
vault_reports:
  intro: "narrative_analysis/introduction/mvp30/fine_grained/batch_2026-06-02/kalaignanam2017_distilled_introduction.md"
  theory: "narrative_analysis/theory/mvp30/fine_grained/batch_2026-06-02/kalaignanam2017_distilled_theory.md"
  methods_results: null（OCR 全文回读：459 make/year/27 制造商/1995-2011、中介模型）
  story_arc: null
corpus_links:
  write-introduction: "行业案例 Hook（Toyota/Boeing 外包案例）+ 辩证对立 Tension（make vs buy——mixed conclusions）——路径待验证"
  write-methods: "中介模型（recall→reliability→未来事故/召回）+ 双调节（transfer/attention enabler）——路径待验证"
  write-results: "学习效应揭晓 + 中介验证 + 双条件——路径待验证"
```

## Story

### one_liner

> 召回项目的目标是提升安全，但企业是否从召回中学习未知（GM 的 WSJ 反例："rear wheel and axle fall off 不危险"）——实证发现：召回幅度越大，未来事故与召回越少（部分中介于产品可靠性）——**企业确实从召回中学习**；共享产品资产促进学习转移（transfer enabler）、低质量品牌学习更努力（attention enabler）——监管者"召回有益"的主张首次获得系统证据。

### knot

```yaml
knot:
  primary_type: neglected-arena         # 第五原型：recall 学习后果子域空白（'no research has tested the impact of product recalls on subsequent product reliability'）
  compound_types: []                    # 中介+双 enabler 是结构，非子类型
  statement: "recall 后果研究做了市场反应/声誉/成本——'there is no research that has tested the impact of product recalls
              on subsequent product reliability'——学习后果子域空白（Haunschild & Rhee 2004/Thirumalai & Sinha 2011 例外确认）——
              实证：召回幅度→未来事故/召回减少（可靠性部分中介）——企业确实从召回中学习（GM 反例 vs 学习现实）"
  tied_at:
    - "Intro：召回频率增长（CPSC 2010/Evenflo 2007/Toyota 2009）→ 'little is known about whether firms respond to product recalls beyond withdrawing and repairing' → GM WSJ 1983 引语（不学习的反例）"
    - "Theory：组织学习（Cyert & March 行为观——problem-driven search）+ 双 enabler（transfer/attention）"
  untied_at:
    - "Theory H1-H3：recall→未来事故/召回 + 可靠性中介 + 双调节"
    - "Results：学习效应支持 + 中介验证 + 双调节"
  antagonist: "recall 后果研究的外部导向（市场反应/声誉——学习后果被跳过——'beyond withdrawing and repairing' 的未知）"
  antagonist_built_by:
    - "GM WSJ 1983 引语（'persuade the Federal Government that it isn't dangerous if the rear wheel and axle fall off'——不学习企业的讽刺形象）"
    - "精确缺口（'no research has tested the impact of product recalls on subsequent product reliability'）"
    - "监管主张的悬空（'regulatory agents contend that product recalls are beneficial... there is no systematic evidence to support this contention'）"
```

### characters

```yaml
characters:
  protagonist: [recall magnitude（X——t−1）, future accidents + future recalls（DV——t+1，reliability 中介 t）]
  supporting:
    - "product reliability（中介——学习成果——'learning... from the intensity of off-line activities' [Levin 2000]）"
    - "shared product assets（transfer enabler——共享资产促进学习转移——Toyota 2009 知识共享争议）"
    - "prior brand quality（attention enabler——低质量品牌注意力更强、学得更多）"
    - "GM/Toyota（反例与正例——具名）"
  ensemble: [459 make/year/27 制造商/1995-2011/汽车行业、中介模型、CPSC/NHTSA 情境]
```

### resolution_logic

`exploration` 拓荒（补学习后果战场——recall→reliability→未来事故/召回的完整学习链 + 双 enabler 条件化）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：召回频率增长（CPSC 2010/Evenflo 2007 婴儿座椅/Toyota 2009）→ 'little is known about whether firms learn from product recalls' → GM WSJ 1983 引语（不学习反例）→ 监管主张无系统证据"
  rising_action: "组织学习理论（Cyert & March 行为观——problem-driven search——Haunschild & Rhee 例外）+ 双 enabler（transfer——shared product assets；attention——prior brand quality）+ Methods（459 make/year/27 制造商/1995-2011、中介模型）"
  climax: "Results——学习效应揭晓：召回幅度→未来事故/召回减少（可靠性部分中介）——'firms do learn from recalls'（GM 反例 vs 学习现实的首揭）"
  falling_action:
    - "中介验证（product reliability 部分中介——'learning across these aspects increases with cumulative recall experience... could lead to improved product quality' [Thirumalai & Sinha]）"
    - "双调节（shared product assets 强化——transfer enabler——知识共享促进学习；prior brand quality 弱化——attention enabler——低质量品牌学得更多——Toyota 2009 知识共享争议的实证回应）"
    - "稳健性（替代测量/模型规格——'robust across alternate measures'）"
  denouement: "Discussion——监管者主张的验证（'regulatory agents contend that product recalls are beneficial... our evidence supports this'）；
               学习能力条件（能学——transfer enabler；愿学——attention enabler——'not all firms learn equally'）；
               管理含义（共享资产的学习价值 vs 质量风险）"
```

### stakes

```yaml
stakes:
  theoretical: "recall 学习后果未知——'little is known about whether firms learn from product recalls'——监管者主张无系统证据"
  practical: "召回项目的学习价值（未来事故/召回减少——消费者安全）；GM 不学习的反例（'rear wheel and axle fall off' 的傲慢）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 召回后果版——recall→市场反应/声誉/成本（recall 文献主流——stakeholder 反应）"
  - "讲法B: 召回前因版——什么导致召回（外包/激励——前因视角——本文不做）"
  - "讲法C: 学习能力版——只做组织学习理论框架（learning 文献——不接召回实证）"
  - "本文: 学习后果拓荒版——recall→reliability→未来事故/召回（'firms do learn'——双 enabler 条件化——监管主张首次获证）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "Evenflo 2007 婴儿座椅召回（具名产品——handle 故障）；Toyota 2009（召回——生命损失——知识共享争议）；GM WSJ 1983 引语（不学习反例——'rear wheel and axle fall off'——讽刺细节）"
  rhetorical_question: "未见【已核实】——辩证对立 Tension 用陈述句式"
  pacing_notes: "召回频率增长→学习未知→GM 反例→组织学习理论→双 enabler→中介模型；climax=学习效应揭晓；falling action 中介+双调节+稳健性"
  showing_telling: "GM 引语（不学习企业的讽刺形象——'persuade the Federal Government that it isn't dangerous'）；'transfer/attention enabler'（能力/动机框架——概念隐喻）"
  voice: "JM 实证口吻；'little is known'（精确缺口）；'no systematic evidence'（监管主张的悬空）"
```

### cross_paper_notes

- **neglected-arena 五原型（recall 学习后果）**：desai2012/park2013/eilert2017/kashmiri2017/**kalaignanam2013**。
- **与 mayo2022 的"组织学习版"对照（被拒讲法的正典化）**：mayo 被拒讲法 B（组织学习——recall 的学习效应——'无视角增量'）；kalaignanam2013 正是学习讲法的正典实证（学习后果 + 中介 + 双条件——增量充分）。
- **同作者不同故事第 5 组**：eilert2017（召回时机前因）↔ kalaignanam2013（召回学习后果——Eilert 共同作者）——同作者同类型（neglected-arena）不同子域。
- **学习家族谱系**：wowak2015 引 Haunschild & Rhee（成因例外）→ kalaignanam2013 引（学习例外）→ 库内 haunschild2015 待蒸馏——谱系完整。
- **判别器记录**：neglected-arena 判定基于学习后果子域整体空白（'no research has tested'——例外确认）。
