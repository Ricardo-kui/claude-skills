# Story Blueprint — Mayo, Ball & Mills (2022) POM

## 文件头

```yaml
id: mayo2022
paper: "Mayo, Ball & Mills (2022, POM) — CEO Tenure and Recall Risk Management in the Consumer Products Industry"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（vault 四区段报告 + memory methods/results + 全文回读）→ ROBUST
source_records: [project_mvp30_mayo2022_methods_results, vault narrative/fine/theory 报告, parsed full text]
vault_reports:
  intro: "narrative_analysis/mvp30/mayo2021_ceo_tenure_recall_pom_distill-introduction-exemplar.md"
  theory: "narrative_analysis/theory/mvp30/fine_grained/batch_2026-07-09/mayo2022_ceo_tenure_recall_distilled_theory.md"
  methods_results: "narrative_analysis/methods_results/mvp30/methods/mayo2022_ceo_tenure_recall_methods_narrative.md + results/... + fine_grained/batch_10_mayo2022/...（报告齐全）"
  story_arc: null
corpus_links:
  write-introduction: "'recall is a dreaded word' 开场 + finance/accounting 双机制文献移植（Table 1 列表）——路径待验证"
  write-methods: "复发事件风险模型 + CEO Time 三分位 + SEC 10-K 裁量权测量 + 分样本 Wald χ²——已入 write-methods（memory 记录）"
  write-results: "Early +77%/Late −52% + forced-out 交互 + 裁量权分样本——已入 write-results（memory 记录）"
```

## Story

### one_liner

> 召回不仅是安全事件，更是 CEO 的政治工具——finance/accounting 已知的 CEO 继任风险机制（早任期甩锅前任、晚任期隐藏问题）在 OM 召回情境空白：新 CEO 上任召回风险 +77%（blame-shift——揭露前任烂摊子，前任被赶走时尤甚）、晚任期 −52%（hide——只隐藏可裁量性召回）——"recall 的 CEO 政治经济学"。

### knot

```yaml
knot:
  primary_type: half-domain-gap         # 第四原型：跨域半区（finance/accounting CEO 继任机制 → OM 召回情境——跨学科嫁接，schema 原话契合）
  compound_types: []                    # 双机制（blame-shift/hide）是理论结构，非子类型
  statement: "finance/accounting 已研究 CEO 继任的风险管理双机制（早任期加速坏消息以甩锅前任 [Pourciau 1993]；
              晚任期隐藏问题 [Kothari 2009]）；OM 召回情境空白——recall 不仅是安全事件更是 CEO 政治工具：
              新 CEO 上任召回高峰（+77%——blame-shift）、晚任期低谷（−52%——hide 只发生在可裁量召回）"
  tied_at:
    - "Intro：'recall is a dreaded word'（C-suite 视角开场）→ 召回代价 → finance/accounting 双机制文献（Table 1——'contexts... predominantly in finance and accounting'）→ OM 空白"
    - "Theory：blame-shift（早任期——'blame the previous CEO'）+ hide（晚任期——'hidden recalls'）"
  untied_at:
    - "Theory H1-H3：tenure 模式 + forced-out 条件 + 裁量权条件"
    - "Results：H1 支持（Early 0.57***/Late −0.73***）+ H2/H3 支持"
  antagonist: "OM 的召回研究未考虑 CEO 继任政治（recall 被当作纯安全事件——CEO 的 blame/hide 动机被忽略）"
  antagonist_built_by:
    - "'recall is a dreaded word'（情感开场——CEO 视角的召回恐惧）"
    - "finance/accounting 机制引用（Pourciau/Baginski/Kothari——甩锅与隐藏的既有证据）"
    - "双机制对称排布（早任期 blame-shift vs 晚任期 hide——tenure 依赖的风险管理）"
```

### characters

```yaml
characters:
  protagonist: [CEO tenure（X——Early/Late 三分位）, recall hazard（DV——自愿召回）]
  supporting:
    - "prev CEO forced out（H2——被赶走的前任→更强烈的甩锅召回：×Early 0.44***）"
    - "recall discretion（H3——SEC 10-K 披露 vs 非披露——隐藏只发生在可裁量召回：低裁量 n.s./高裁量 −0.90***）"
    - "blame-shifting（机制 1——早任期揭露前任烂摊子）"
    - "hiding（机制 2——晚任期隐藏裁量召回）"
  ensemble: [125 公司/307 新 CEO/584 自愿召回/1992-2016/消费产品、复发事件风险模型、Wald χ² 分样本比较、1 治理建议 + 4 CPSC 政策建议]
```

### resolution_logic

`exploration` 拓荒（补上 OM 的召回情境半区——CEO 继任双机制地图——blame-shift/hide + 两个条件化）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：'recall is a dreaded word'（C-suite 情感开场）→ 召回代价（财务/声誉/CEO 生涯）→ finance/accounting 双机制文献（避免事件 vs 避免责任——tenure 依赖）→ OM 空白"
  rising_action: "双机制理论（早任期 blame-shift——Pourciau 甩锅；晚任期 hide——Kothari 隐藏）+ Methods（125 公司/307 CEO/584 召回/1992-2016/复发事件风险模型 + CEO Time 三分位）"
  climax: "Results——H1 揭晓：Early Tenure 召回风险 +77%（β=0.57, p<.001）/Late Tenure −52%（β=−0.73, p<.001）——'新 CEO 的欢迎仪式是召回'——recall 的 CEO 政治经济学首揭"
  falling_action:
    - "H2 forced-out（Prev CEO Forced × Early 0.44, p<.001——被赶走的前任→更多甩锅召回；×Late −0.68, p<.001）"
    - "H3 裁量权（低裁量 Late n.s. [−0.02]/高裁量 −0.90, p<.001——Wald χ² p<.001——隐藏只发生在可裁量召回——SEC 10-K 披露测量）"
    - "稳健性（reset-time 模型/logistic 确认/ln CEO Time/四分位）"
  denouement: "Discussion——recall 作为 CEO 政治工具（blame-shift early/hide late）；1 治理建议 + 4 CPSC 监管政策建议
               （裁量性召回可隐藏的监管含义——披露透明度）；'low discretion recalls... statistically independent of CEO tenure'——
               隐藏完全由可裁量召回解释"
```

### stakes

```yaml
stakes:
  theoretical: "CEO 继任风险机制在 finance/accounting 已知、OM 召回情境空白——recall 不是纯安全事件而是 CEO 政治工具"
  practical: "裁量性召回的隐藏（晚任期——消费者安全）；CPSC 监管政策建议（4 条）；董事会继任治理（1 条）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 召回代价版——recall 的负面后果（市场/声誉/CEO 生涯——recall 文献主流）"
  - "讲法B: 组织学习版——recall 的学习效应（Haunschild & Rhee 2004——召回促进学习）"
  - "讲法C: 监管视角版——CPSC 政策评估（监管者视角——换研究对象）"
  - "本文: 跨域嫁接版——finance/accounting 的 CEO 继任双机制 → OM 召回（blame-shift early/hide late——recall 的 CEO 政治经济学）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "'recall is a dreaded word'（开场——C-suite 情感）；无具名企业（消费产品样本——125 公司集体角色）"
  rhetorical_question: "未见【已核实】"
  pacing_notes: "代价开场→双机制文献→OM 空白→三分位设计；climax=H1 双系数揭晓（+77%/−52%）；falling action forced-out+裁量权+四稳健性"
  showing_telling: "'recall is a dreaded word'（开场意象）；'blame the previous CEO'（甩锅意象——Pourciau 引语）；'hidden recalls'（隐藏意象）"
  voice: "POM 实证口吻；'dreaded word'（情感开场）；'unique recall pattern'（独特性强调）"
```

### cross_paper_notes

- **half-domain-gap 四原型（跨域嫁接）**：malshe2015（维度半区+跨学科 finance→marketing）/ wu2025（行为半区）/ malik2025（情境半区）/ **mayo2022（跨域半区——finance/accounting CEO 继任机制 → OM 召回——schema 原话'常与跨学科嫁接配合'的第四形态）**。
- **recall 现象域十一讲法**（3 后果/机制 + 8 前因——mayo2022 CEO 继任政治入列）。
- **与 wowak2015 的 tenure 呼应**：wowak（tenure 调节期权效应——11 年后消失）；mayo（tenure 本身驱动召回模式——早高晚低）——同一 tenure 变量两种故事。
- **与 darby2024 的继任对照**：darby（CEO 变更为持股的外生冲击——识别工具）；mayo（CEO 继任本身是研究对象——blame/hide）——继任的两面。
- **与 malshe2015 的跨学科嫁接对照**：malshe finance→marketing；mayo finance/accounting→OM——跨域嫁接家族 2 例。
- **判别器记录**：half-domain-gap 判定基于跨域机制已知、OM 情境空白（跨学科嫁接——schema 定义契合）。
