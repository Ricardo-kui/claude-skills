# Story Blueprint — Singh & Grewal (2023) JMR

## 文件头

```yaml
id: singh2023
paper: "Singh & Grewal (2023, JMR) — Lobbying and Product Recalls: A Study of the U.S. Automobile Industry"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏——Results/Discussion 原文回读 → ROBUST
source_records: [project_mvp30_singh_grewal2023_intro, project_mvp30_singh_grewal2023_theory,
                 singh2023 parsed full text（Results/Discussion 直接回读）]
vault_reports:
  intro: "narrative_analysis/mvp30/singh2023_lobbying_product_recalls_jmr_narrative.md"
  theory: "narrative_analysis/theory/mvp30/fine_grained/batch_2026-05-24/Singh_Grewal_2023_JMR_distilled_theory.md"
  methods_results: "narrative_analysis/methods_results/mvp30/fine_grained/batch_04_singh2023_park2025/singh2023_lobbying_product_recalls_fine_methods_results.md + deep_distillation/papers/singh2023_lobbying_product_recalls_methods_results_deep_profile.md + methods/ + results/ singh2023_..._narrative.md"
  story_arc: null
corpus_links:
  write-introduction: "academic-writing-corpus/tensions/17-puzzle-contrast.md 变体A（理论零假设 vs 现象矛盾型——singh_grewal2023 型）；hooks/04-puzzle-paradox.md、03-data-shock.md（Policy 丑闻 Hook 相关）"
  write-theory: "corpus/sentences/mechanism_chain.md（Efficiency vs Legitimacy 双视角 + Iron Triangle 三边论证）；corpus/sentences/closure.md（T6 缺失锚定）；corpus/subprotocols/argumentation_patterns.md、arrangement_patterns.md、evidence_patterns.md"
  write-methods: "econometric-models/micro-templates/identification-exogeneity.md、multi-source-matching.md、subsample-grouping.md；事件历史+事件研究.md（singh 来源）"
  write-results: "econometric-models/_evidence_registry.yaml（Singh_Grewal_2023_JMR 条目 ×5，2026-08-09 核实）"
```

## Story

### one_liner

> 效率逻辑断言游说不该影响召回（它不改变产品质量），但现实与数据显示游说系统性减少自愿与强制召回——recall 文献的商业视角看不到政治面，本文用合法性+铁三角视角揭幕，并用 IV 与自然实验钉死因果。

### knot

```yaml
knot:
  primary_type: overlooked-alternative   # 第三原型（desjardine2022 deductive / lashley2020 inductive / 本文 deductive 政策宣战）
  compound_types: [counterevidence]      # Should-be-Yet 效率预期 vs Toyota 丑闻/数据反证（宏观事实对照点）
  statement: "效率逻辑断言产品质量是召回的唯一定因、游说不应有影响；但 Toyota 国会丑闻与全行业数据显示游说系统性减少自愿与强制召回——recall 文献的商业视角漏掉了政治/监管面"
  tied_at:
    - "Intro P1-P3：政策丑闻 Hook → Should-be-Yet Puzzle（效率预期 vs 证据）→ 双发现预览"
    - "Theory Conceptual Background：效率 vs 合法性双视角（Iron Triangle 三边逐一论证）"
  untied_at:
    - "Theory H1（树干预测：lobbying → 政治影响力 → 更少召回）"
    - "Results Table 4/Table 5（H1-H4 检验）"
  antagonist: "recall 文献的主导商业/效率视角（把召回当作市场与运营问题）——它看不见监管俘获"
  antagonist_built_by:
    - "政策丑闻 Hook（国会报告+企业内部文件——'wins' 加引号制造道德暧昧）"
    - "Should-be-Yet Puzzle（基准预期→挑战预期结构）"
    - "Contribution 段明示 'existing recall literature... mainly adopts a business orientation'"
```

### characters

```yaml
characters:
  protagonist: [lobbying（IV——企业的政治行动）, recalls（DV——voluntary/mandatory 双流）]
  supporting:
    - "media coverage（H3/H4 关键配角——独立于决策过程的制衡工具）"
    - "defect severity/death reports（信息特征——H2/H4 触发者）"
    - "regulator/NHTSA（铁三角一角——监管俘获的落点）"
    - "iron triangle（游说者/政客/监管者——Figure 3 的制度舞台）"
  ensemble: [丰田（Hook 案例）、GM（Flint 自然实验）、消费者/安全倡导组织（stakes 受益者）]
```

### resolution_logic

`revelation` 揭幕（deductive 宣战版）——不推翻效率视角的合理性，翻出被商业导向遮蔽的政治面：合法性机制 + 铁三角框架 + 双因果识别（county 政治捐款 IV + Flint 自然实验）。研究者是揭幕人 + 鉴证师：先换视角，再用识别策略给视角钉上因果地位。

### five_acts

```yaml
five_acts:
  exposition: "Intro P1-P3：Toyota 政策丑闻 Hook（2010 国会报告、2009 内部文件 COO 'wins'、$100M 节省）→ 行业规模数据（6300 万辆/221 亿美元）→ Should-be-Yet Puzzle → 双发现预览（自愿+强制召回负相关 + 'regulators do not compensate' 反直觉）"
  rising_action: "Theory：Institutional Background 前置（Figure 1 召回制度过程——舞台先行）→ Iron Triangle 三边逐一论证 → H1 树干 + H2-H4 条件分支；Methods：多源数据 + Model-free evidence + IV 构建与辩护（county 政治捐款 IV、time-varying omitted variable、relevance/exclusion、经验有效性诊断先行）"
  climax: "Results Table 4——H1 首次揭晓：游说显著减少自愿召回（β=-2.473, p<.05）与强制召回（β=-.600, p<.01），且 'regulators do not compensate'（自愿减少并未换来监管者补位——反直觉点兑现）"
  falling_action:
    - "Table 5 调节揭晓：H2 死亡严重度削弱游说（β=.166, p<.10）/ H3 媒体制衡游说（β=.029, p<.01）/ H4 间接调节 voluntary 全中介（β=.022, p<.10）——mandatory 不显著（部分支持的反转点，诚实报告）"
    - "经济显著性收束：$404,367→1 次更少自愿召回→约 $12M 节省（back-of-the-envelope）"
    - "稳健性：Long-term Koyck 存量模型 → 同时方程 GMM → Exogenous event（Flint 水危机 + GM DiD——9,000 儿童 18 个月铅水的自然实验叙事）→ 非线性 ordered probit（CMP）"
  denouement: "Discussion：回到开头——'These results validate concerns raised in the Congressional Report'（呼应 Toyota 丑闻）；media 作为 actionable lever（消费者/倡导组织可用）；dark side 双重性（'In no way should our results be taken as a recommendation'）；$3.7B 游说产业 + 政策透明呼吁"
```

### stakes

```yaml
stakes:
  theoretical: "recall 文献的效率视角遗漏政治维度——合法性制度理论 × 铁三角整合提供 theory-based generalization（可推广到制药等类似监管情境）"
  practical: "消费者安全（GM ignition 124 死）；每次召回 ~$12M 节省的游说激励；媒体制衡作为公众杠杆；政策制定者透明化需求"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 成本效率版——召回作为市场/运营现象（recall 文献主流：成本、时点、市场反应——商业导向）"
  - "讲法B: 政策建言版——只呼吁监管改革不做因果识别（缺实证冲击力）"
  - "讲法C: 相关性描述版——报告游说与召回负相关（会被内生性批评杀死：游说是战略选择）"
  - "本文: 政治面揭幕+因果识别版——Toyota 丑闻提供道德张力 Hook，county 捐款 IV + Flint 自然实验双识别，'媒体制衡'让论文从揭示问题走向提供解决方案"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "具名权威+具体数字：Toyota 内部文件（COO 列举 'wins'、Camry 召回省 $100M）；Flint 水危机（GM 工厂、9,000 儿童、18 个月铅水）；GM ignition 缺陷（124 死）；Topps Meat 破产"
  rhetorical_question: "未见【已核实】——Should-be-Yet 是陈述对比结构而非问句"
  pacing_notes: "极简 4 段 Intro（无 Lit Turn/Theory Lens——Puzzle 直入的压缩节奏）；Theory 先制度背景后理论（Institutional Background 前置的舞台先行节奏）；Results 诊断先行（IV validity 在假设检验之前——先证明工具可信再谈发现）；falling action 5 组稳健性含一个完整自然实验故事（Flint/GM）"
  showing_telling: "'wins' 加引号（道德暧昧修辞——企业视角的'胜利'）；Figure 1/3/4（召回制度过程、铁三角、调节模型 A/B 可视化）；back-of-the-envelope 计算（经济显著性具象化）"
  voice: "主动语态（We predicted that...）；道德判断克制（'In no way should our results be taken as a recommendation'——反误解声明）；政策关切中立语调"
```

### cross_paper_notes

- **overlooked-alternative 第三原型（"看漏一面"家族）**：desjardine2022（deductive 翻硬币——CSR 涨潮面）↔ lashley2020（inductive 拉幕）↔ singh2023（deductive 政策宣战——recall 的政治面）——三种系紧方式：理论宣战 / 数据长出 / 现实丑闻+数据。
- **recall 现象域三种讲法**：wowak2025（TMT 意识形态两极战）、desjardine2023（oversight→underground irony）、singh2023（政治面 overlooked-alternative）——同一产品召回现象，故事完全不同。
- **效率逻辑冲突的两种对立方式**：zhou2017（efficiency vs institutional 对称两军对决→仲裁）↔ singh2023（效率为基线预期、合法性为挑战视角——不对称挑战→翻面）。"同是 efficiency 冲突，对称对决 vs 不对称挑战"。
- **IV/识别家族故事对照**：malshe2015（同时方程）、wu2025（制度冲击 DiD）、singh2023（county 捐款 IV + 自然实验）——同一识别武器库，三种故事用途。
