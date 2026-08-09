# Story Blueprint — Denicolò & Panunzi (2025) Management Science（理论论文）

## 文件头

```yaml
id: denicolo2025
paper: "Denicolò & Panunzi (2025, MgmtSci) — Common Ownership, Competition, and Corporate Governance"
paper_type: theory        # 纯理论论文（无实证——Fig 2.4 overlay）
distilled_sections: [intro, theory, methods, results]   # 理论论文——theory 全文回读；methods/results 不适用
source_records: [OCR parsed full text]
vault_reports:
  intro: null（OCR 全文回读）
  methods_results: null（纯理论——无实证——按理论论文 overlay）
  story_arc: null
corpus_links:
  write-theory: "均衡权衡建模（软化竞争 vs 削弱治理——blockholders 监督激励）——理论论文 overlay——路径待验证"
```

## Story

### one_liner

> 共同所有权的反竞争共识已确立（降低竞争→提价→利润↑）——但本文揭示被忽略的**治理代价**：财务投资者从 blockholders 处购股会削弱其监督激励（agency 恶化）——"软化竞争有利可图 vs 治理恶化有害可图"的权衡决定共同所有权的**均衡水平**——竞争越激烈/治理需求越高，均衡越低。

### knot

```yaml
knot:
  primary_type: half-domain-gap         # 第七原型：共同所有权研究的治理效应半区（反竞争共识 done/治理代价 not——理论版）
  compound_types: []                    # 均衡权衡是解法，非子类型
  statement: "共同所有权研究——反竞争效应共识已确立（'new consensus... companies with common ownership engage in less intense competition'）；
              但治理效应被忽略——'common ownership also undermines effective corporate governance by diminishing blockholders'
              incentives to engage in value-enhancing behaviors'——软化竞争有利 vs 治理恶化有害的权衡决定均衡水平
              （'the equilibrium level of common ownership must strike a balance between these conflicting effects'）"
  tied_at:
    - "Intro：传统观点（分散化被动）→ 新共识（反竞争——'less intense competition... higher prices and profits'）→ 治理代价引入（'also undermines effective corporate governance'——被忽略的另一半）"
    - "Theory：均衡权衡建模（blockholders 监督激励 vs 竞争软化——'a tradeoff emerges'）"
  untied_at:
    - "Theory：均衡所有权结构（多因素决定）"
    - "Results（理论）：竞争越激烈/市场越分散→共同所有权越高；监督需求越高→越低"
  antagonist: "共同所有权的反竞争共识（'consistent with the emerging consensus'——竞争效应一极已做、治理效应空白）"
  antagonist_built_by:
    - "传统→新共识的演进叙事（'traditional view... passive'→'new consensus... less intense competition'）"
    - "治理代价引入（'also undermines effective corporate governance by diminishing blockholders' incentives'——被忽略的另一半）"
    - "'a tradeoff emerges'（权衡声明——'beneficial for profits, but simultaneously... detrimental to profits'）"
```

### characters

```yaml
characters:
  protagonist: [common ownership level（X——均衡决定）, corporate profits（DV——竞争软化↑ vs 治理恶化↓的净效应）]
  supporting:
    - "竞争软化机制（资本收益——'enhances profitability for the firms involved'）"
    - "治理恶化机制（blockholders 监督激励削弱——'diminishing blockholders' incentives to engage in value-enhancing behaviors'）"
    - "financial investors（不完美替代者——'lack of ability or incentives to engage in value-enhancing behaviors'）"
    - "blockholders/dispersed shareholders（购股对象——free-riding 问题）"
  ensemble: [均衡模型（2 对称企业→多企业→非对称）、内/外部共同所有权、Grossman-Hart 搭便车、附录证明]
```

### resolution_logic

`exploration` 拓荒（理论版——补治理效应半区 + 均衡权衡建模——"冲突效应的均衡"作为理论 deliverable）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：传统观点（分散化被动）→ 新共识（反竞争——'less intense competition... higher prices and profits'）→ 治理代价引入（'also undermines effective corporate governance'）→ 'a tradeoff emerges'"
  rising_action: "均衡权衡建模（blockholders 监督激励 vs 竞争软化——Grossman-Hart 搭便车——购股来源（blockholders/分散））+ 模型设定（2 企业→多企业→非对称——内/外部共同所有权）"
  climax: "理论揭晓——均衡所有权结构：'as competition becomes more intense or the market more fragmented, the degree of common ownership increases'——权衡的均衡解"
  falling_action:
    - "监督需求条件（'the greater the need for monitoring managers... the lower the degree of common ownership'——治理半区的地图）"
    - "内/外部共同所有权区分（内部可从分散股东购股获利——'internal common ownership may be profitable even if the acquisition is solely from dispersed shareholders'）"
    - "政策含义（治理改善→股东受益但消费者受损——'greater common ownership and ultimately higher prices'——治理与竞争的深层张力）"
  denouement: "理论收口——共同所有权的均衡决定（竞争强度 × 治理质量——'among the most significant'）；
              治理-竞争张力（'improvements in corporate governance... benefit shareholders but have adverse effects on consumers'）；
              实证/政策含义（机构投资者配置——'allocate more weight to sectors where market concentration is lower'）"
```

### stakes

```yaml
stakes:
  theoretical: "共同所有权研究的治理效应半区——'also undermines effective corporate governance'——均衡决定因素未建模"
  practical: "机构投资者配置（'allocate more weight to sectors where market concentration is lower'）；治理改善的消费者后果（更高价格）；反垄断政策"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 反竞争版——共同所有权减少竞争（IO 新共识——'emerging consensus'——竞争效应一极）"
  - "讲法B: 治理实证版——共同所有权影响治理（实证文献——监督/协调——不接均衡）"
  - "讲法C: 组合分散版——共同所有权=分散化被动（传统观点——本文起点）"
  - "本文: 治理半区+均衡版——竞争软化 vs 治理恶化的权衡（'a tradeoff emerges'——均衡所有权结构——理论 deliverable）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "无具名企业（纯理论——模型设定）；Grossman-Hart 搭便车（概念人物——'farsighted dispersed shareholders'——人化表达）"
  rhetorical_question: "未见【已核实】——理论论文用陈述式权衡"
  pacing_notes: "传统→新共识→治理代价→权衡→均衡模型（2→N 企业递进）→政策含义；climax=均衡解揭晓；falling action 条件+内外部区分+政策"
  showing_telling: "'a tradeoff emerges'（权衡意象）；'strike a balance between these conflicting effects'（均衡意象）；'free-riding problem'（搭便车概念）"
  voice: "MgmtSci 理论口吻；'consistent with the emerging consensus'（共识承接）；'It is important to note'（理论推进标记）"
```

### cross_paper_notes

- **half-domain-gap 七原型（治理效应半区——理论版）**：malshe/wu/malik/mayo/lun/liu2016/**denicolo2025**——共同所有权研究的治理半区（理论补全）。
- **共同所有权家族三篇成型**：desjardine2022（CSR 实证）+ anton2025（创新理论+实证）+ **denicolo2025（治理均衡——纯理论）**——同一现象三透镜三类型（overlooked/overlooked/half-domain）。
- **理论论文 overlay 首个案例**（schema Fig 2.4——理论论文的 five_acts 映射——theoretical background 系 knot、falling action=理论 deliverable）。
- **判别器记录**：half-domain-gap 判定基于共同所有权研究的竞争效应一极已做（反竞争共识）、治理效应半区空白（'also undermines'——原文锚）——理论版均衡补全。
