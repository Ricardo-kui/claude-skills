# Story Blueprint — Hoffmann, Cheong, Phan & Zurbruegg (2024) JM

## 文件头

```yaml
id: hoffmann2024
paper: "Hoffmann, Cheong, Phan & Zurbruegg (2024, JM) — So, Sue Me...If You Can! How Legal Changes Diminishing Managers' Risk of Being Held Liable by Shareholders Affect Firms' Likelihood to Recall Products"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（parsed 全文回读）→ ROBUST
source_records: [parsed full text]
vault_reports:
  intro: null（parsed 全文回读）
  methods_results: null（parsed 全文回读：Compustat 1986-2018、交错 DiD）
  story_arc: null
corpus_links:
  write-introduction: "'So, Sue Me...If You Can!' 标题挑衅 + 法律责任前因缺口（'antecedents of recalls... relatively sparse'）——路径待验证"
  write-methods: "UD laws 交错 DiD（Goldfarb 指南）+ 无伤亡召回子样本——路径待验证"
  write-results: "UD→召回减少 + customer focus/机构监控缓解 + 替代解释排除——路径待验证"
```

## Story

### one_liner

> 召回前因研究"relatively sparse"且未考虑法律变化——UD 法律（降低股东诉讼风险）本意防止无聊诉讼，但**意外后果**：诉讼约束减弱后管理者自利抬头，受影响企业**更不愿意召回**；顾客导向文化与机构投资者监控可缓解；运营改善的替代解释被排除。

### knot

```yaml
knot:
  primary_type: neglected-arena         # 第七原型：recall 前因的法律维度空白（'antecedents of recalls... relatively sparse'——Bendig 2018 批评）
  compound_types: []                    # UD 法律意外后果是发现，非子类型
  statement: "recall 前因研究'relatively sparse'且未考虑法律变化（Bendig et al. 2018 批评：前因仅限运营问题）——UD 法律（防止无聊
              诉讼——'well-intended'）降低股东诉讼风险→意外后果：管理者自利抬头→受影响企业更不愿意召回；
              customer focus 文化/机构投资者监控可缓解"
  tied_at:
    - "Intro：'So, Sue Me...If You Can!'（标题挑衅——管理者免于被诉的得意）→ 前因稀疏（'antecedents of recalls, instead of their consequences, is relatively sparse'）→ UD 法律引入（'well-intended... unintended negative consequences'）"
    - "Theory：代理冲突（Jensen & Meckling——诉讼作为治理机制）+ 边界（corporate culture/normative control——Husted 区分）"
  untied_at:
    - "Theory H1-H3：UD→召回减少 + 两边界"
    - "Results：UD→召回可能性下降（模型自由证据 99% 置信）+ 缓解 + 替代解释排除"
  antagonist: "recall 前因研究的运营导向（前因仅限运营问题——法律/治理维度空白——Bendig 2018 批评）"
  antagonist_built_by:
    - "标题挑衅（'So, Sue Me...If You Can!'——管理者视角的得意与隐患）"
    - "'well-intended... unintended negative consequences'（意图与后果的落差）"
    - "前因稀疏声明（'relatively sparse and has not considered... legal changes'——Bendig 2018 批评引用）"
```

### characters

```yaml
characters:
  protagonist: [UD law adoption（X——交错自然实验）, recall likelihood（DV）]
  supporting:
    - "诉讼治理机制（UD 法律降低——管理者自利抬头——'private incentives to try to avoid a recall'）"
    - "customer focus（边界——市场导向的客户维度——内在治理）"
    - "institutional investor monitoring（边界——规范性控制——外在治理）"
    - "consumers（受害方——召回减少=安全风险增加）"
  ensemble: [Compustat 1986-2018 + CPSC、交错 DiD（Goldfarb 指南）、无伤亡召回子样本、30,679 firm-years]
```

### resolution_logic

`exploration` 拓荒（补 recall 前因的法律维度——UD 法律意外后果地图 + 双治理边界条件化）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：'So, Sue Me...If You Can!'（标题挑衅）→ 前因稀疏（'antecedents of recalls... relatively sparse'——Bendig 2018 批评）→ UD 法律引入（'well-intended'——诉讼治理机制）"
  rising_action: "代理冲突理论（Jensen & Meckling——诉讼作为治理机制——'private incentives to avoid a recall could come to dominate'）+ 双边界（customer focus 文化/机构投资者监控——Husted 内在 vs 外在治理）+ Methods（Compustat 1986-2018、交错 DiD、无伤亡子样本）"
  climax: "Results——UD 揭晓：法律采纳后受影响企业更不愿意召回（模型自由证据 99% 置信——'unintended negative consequences of imposing less discipline on managers'）"
  falling_action:
    - "customer focus 缓解（'less pronounced for firms with a more customer-focused market orientation'——内在治理）"
    - "机构投资者监控缓解（'normative control through monitoring'——外在治理）"
    - "替代解释排除（运营改善/产品质量提升不解释发现——'do not find support'）"
  denouement: "Discussion——UD 法律意外后果（'unintended negative consequences'——消费者福利）；立法修订建议（'suggested amendments to UD laws... to strengthen consumer protection'）；
              董事会结构与股东/消费者倡导者的建议"
```

### stakes

```yaml
stakes:
  theoretical: "recall 前因的法律维度空白——'antecedents of recalls... relatively sparse and has not considered... legal changes'——代理冲突在召回决策"
  practical: "UD 法律减少召回=消费者安全风险（'unintended negative consequences'）；立法修订建议；董事会结构建议"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 召回后果版——recall→市场反应/学习（recall 文献主流——后果导向）"
  - "讲法B: 运营前因版——召回前因只做运营问题（Bendig 2018 批评——现状）"
  - "讲法C: UD 正面版——UD 法律促进创新（Lin et al. 2021——法律保护的正面后果）"
  - "本文: 法律前因揭幕版——UD 法律意外后果（'well-intended... unintended negative consequences'——召回回避 + 双治理边界）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "'So, Sue Me...If You Can!'（标题挑衅——管理者视角的声音）；无具名企业（Compustat 全样本——30,679 firm-years）"
  rhetorical_question: "标题即问句变体（'So, Sue Me...If You Can!'——挑衅式感叹问——标题家族新形态）"
  pacing_notes: "标题挑衅→前因稀疏→UD 引入→代理冲突→双边界；climax=UD 揭晓（99% 置信——'unintended negative consequences'）；falling action 双缓解+替代排除"
  showing_telling: "'So, Sue Me...If You Can!'（标题挑衅——管理者得意与隐患并置）；'well-intended... unintended'（意图落差）；'demand that the firm's board'（程序细节）"
  voice: "JM 实证口吻；'unintended negative consequences'（意外后果强调）；'well-intended'（意图承认——中立）"
```

### cross_paper_notes

- **neglected-arena 七原型（recall 前因法律维度）**：desai2012/park2013/eilert2017/kashmiri2017/kalaignanam2013/pupovac2025/**hoffmann2024**。
- **UD laws 家族 2 篇（同一法律冲击两个故事）**：park2025（stakeholder 转向——paradigms-at-war——外生冲击裁决）↔ hoffmann2024（召回回避——neglected-arena——意外后果）——同一自然实验双故事。
- **recall 现象域十九讲法**（法律前因 +1）。
- **与 mayo2022 的代理对照**：mayo（CEO 继任 blame/hide——代理政治）；hoffmann（诉讼约束减弱——代理自利——法律维度）——代理冲突×召回两场景。
- **判别器记录**：neglected-arena 判定基于 recall 前因的法律维度空白（'relatively sparse'——Bendig 2018 批评引用）。
