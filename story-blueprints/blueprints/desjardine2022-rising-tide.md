# Story Blueprint — DesJardine, Grewal & Viswanathan (2022) OrgSci

## 文件头

```yaml
id: desjardine2022
paper: "DesJardine, Grewal & Viswanathan (2022, Organization Science) — A Rising Tide Lifts All Boats: The Effects of Common Ownership on Corporate Social Responsibility"
distilled_sections: [intro, theory, methods, results]      # 2026-08-09 vault 检索确认四区段报告齐全 → ROBUST
source_records: [project-mvp30-desjardine2022-intro]
vault_reports:   # ⚠️ 勘误：vault 中 desjardine2023_rising_tide_* 命名的报告实为本文（source_text 标题确认），2022 与 2023 勿再混淆
  intro: "narrative_analysis/introduction/mvp30/fine_grained/batch_2026-05-24/desjardine2022_orsc_distilled_introduction.md"
  theory: "narrative_analysis/theory/mvp30/fine_grained/batch_2026-07-09/common_ownership_csr_distilled_theory.md（frontmatter 明示 2022 OrgScience；build_type=机制推演型+假设树型+反共识视角）"
  methods_results: "narrative_analysis/methods_results/mvp30/deep_distillation/papers/desjardine2023_rising_tide_methods_results_deep_profile.md + methods/results/desjardine2023_rising_tide_*_narrative.md（paper_key 误标 2023）"
  story_arc: null
corpus_links:
  write-introduction: "tensions/11-overlooked-alternative 变体C（主导视角批评型：'Most research underscores... and overlooks... We propose an alternative but overlooked strategy'）"
  write-theory: "E 系假设树结构（H1 主效应 + H2-H4 三 contingency 小节）；portfolio perspective lens"
  write-methods: "面板 OLS FE（13F 持股数据、CSR 主/非物质拆分、Bushee 长短期分类）"
  write-results: "R1-R9 全槽位（经济显著性转译 Di Giuli & Kostovetsky 法、自然实验内生性、替代测量）"
```

## Story

### one_liner

> 共同所有权被主流文献讲成一个危险的故事（竞争协调的阴暗面、反垄断担忧），本文讲另一个故事：共同所有者是"涨潮"——从组合视角看，他们推动组合内公司普遍提升 CSR，因为它降低系统性风险、抬高组合总回报。同一个现象，主流看的是协调危害，本文看的是组合风险管理。

### knot

```yaml
knot:
  primary_type: overlooked-alternative   # 主导视角批评型（现象已被研究，主流视角看漏一个替代面）
  compound_types: []
  statement: "共同所有权如何影响 CSR？文献过度关注共同所有权的竞争协调阴暗面（反竞争担忧），忽视其 systematic risk 管理功能——从 portfolio perspective 看，共同所有者推动 CSR（CSR spillovers → reduced systematic risk → higher aggregate returns）——'Most research underscores [dominant view] and overlooks [overlooked aspect]'"
  tied_at:
    - "Intro Tension：主导视角批评型（'Most research underscores... and overlooks...'）——变体C 标志句法直接点名主流共识"
    - "Intro：Authority 引用加固（'[Authority] summarizes the state of this literature: \"[direct quote]\"'）"
    - "Theory T1/T2：投资困境开篇（CalPERS 引语：climate risk / divestment dilemma）+ common ownership 三条 scope clarification——共识与透镜在同段对撞"
  untied_at:
    - "Theory：H1 主效应（机制链：common ownership → portfolio perspective → CSR spillovers → reduced systematic risk）"
    - "Results：H1 主结果（Results paragraph 1）→ H2-H4 三 contingency 逐层展开"
  antagonist: "主流共识视角——共同所有权文献对'竞争协调阴暗面'的过度关注（反竞争/协调危害叙事）；被忽视的是 portfolio perspective 的 systematic risk 管理功能。反派是文献的集体视角而非某个具体理论"
  antagonist_built_by:
    - "主导视角批评句法：'Most research underscores [dominant view] and overlooks [overlooked aspect]. A number of studies conclude that... [Authority] summarizes: \"[quote]\"'——先给共识立牌坊，再掀桌子"
    - "标题隐喻反用：'A Rising Tide Lifts All Boats' 用乐观意象命名本文主张，与主流叙事的阴暗基调形成标题级对抗"
    - "Theory 开篇用真实投资困境（CalPERS divestment dilemma）替共识的'阴暗面'叙事立靶——反派有具名代言人"
```

### characters

```yaml
characters:
  protagonist: [common ownership (X，出现 ~45 次), CSR performance (Y)]
  supporting:
    - "systematic risk / CSR spillovers / portfolio perspective（机制链配角：H1 的 why）"
    - "H2 投资期限（long-term vs short-term，Bushee 分类）、H3 行业敏感度（stakeholder sensitive industries，声誉/规制两子维度）、H4 CSR 重要性（material vs immaterial）——三个 contingency 小节各管一个条件"
  ensemble: [13F 持股数据（Thomson Reuters）、控制变量、firm FE（面板 OLS）]
```

### resolution_logic

`revelation` 揭幕（翻硬币）——提出被主流看漏的替代视角并检验：不是修正测量，而是把共同所有权从"竞争危害"翻到"组合风险管理"。双重贡献段（P1 对共同所有权主流文献 "a new and opposing view" + P2 对 CSR 前置文献）把"翻面"动作锚定到两条文献。研究者是翻硬币的人。

### five_acts

```yaml
five_acts:
  exposition: "Intro：主导视角批评型 Tension（共识立牌坊 → Authority 代言 → 提出替代策略）；双重贡献段（P1 对共同所有权文献：'Our study offers a new and opposing view'；P2 对 CSR 前置文献）；Stakes 后置——实践意义放 Contribution 之后，借政策辩论（反垄断法、OECD/FTC 警告）建立重要性"
  rising_action: "Theory（8 段 ~3,500 词）：T1/T2 合并界定（CalPERS 投资困境开篇 + common ownership 定义三条 scope clarification + portfolio perspective 透镜）；T3 机制链（common ownership → portfolio perspective → CSR spillovers → reduced systematic risk → higher aggregate returns）；H1 主效应；H2-H4 三个独立 contingency 小节（investor horizon / industry sensitivity / CSR materiality）——假设树结构，T5 嵌入；Methods：13F 数据样本漏斗；DV = CSR performance（material/immaterial 拆分——'investor-relevant vs non-equity stakeholders'）；IV = common institutional ownership（Bushee 长短期分类）；OLS + firm FE"
  climax: "Results paragraph 1：描述统计 + 主结果（H1 长短期共同所有权 × CSR 正相关）——'涨潮'叙事首验"
  falling_action:
    - "Results paragraph 2：经济显著性转译（Di Giuli & Kostovetsky 金融学方法把系数翻译成可感幅度——'make our main results more concrete'）"
    - "Results paragraph 3-4：H2 长短期拆分、H3 stakeholder sensitive industries 调节（声誉/规制两子维度分别验证）——'涨潮'何时最强"
    - "Natural Experiment（内生性：omitted variable 担忧——共同所有权与 CSR 同时受驱动）"
    - "Robustness Checks（按威胁组织）：CSR 替代测量三法、共同所有权替代测量（1% 门槛排除等）"
  denouement: "Discussion（2026-08-09 原文核实）：主结果回顾（1 SD 共同所有权 → +0.06 CSR ≈ 9% SD；ASSET4/MSCI 替代一致；长期主义/利益相关者敏感行业/实质性 CSR 更强；DID 外生变异性支持）；四层理论贡献——①超越竞争视角（'manipulating competitive dynamics does not explain... managing systematic risk'——'我们是首个超越竞争动态的实证'）②共同所有者作为 CSR 投资者（'This is surprising not only because...'）③CSR 的第三个理由（组合溢出回报——超越社会偏好/公司特定利润两理由）④material vs immaterial CSR 分割；Practical（ESG 是迫使企业内化负外部性的市场机制——'政策制定者不应急于限制共同所有权'）；Conclusion 收口：'tragedy of the commons' 对照——没有激励看见更大图景的企业各自为政，共同所有者迫使企业内化外部性——'涨潮'与'公地悲剧'的意象对照收束"
```

### stakes

```yaml
stakes:
  theoretical: "共同所有权文献的主流视角（竞争协调阴暗面）若不与组合视角对质，'共同所有权 × 企业社会行为'的理论图景就停在单面；systematic risk 管理的组合逻辑是文献的系统性遗漏"
  practical: "反垄断执法与机构投资者的治理实践：OECD/FTC 对共同所有权的政策警告基于主流视角——如果涨潮叙事成立，政策辩论的靶子就变了（Stakes 后置、借政策辩论背书）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 竞争危害故事 — 共同所有权 → 协调/竞争弱化（finance/IO 主流叙事；本文的靶子，theory 报告确认：'过度关注竞争协调的阴暗面'）"
  - "讲法B: 中性/混合效应故事 — '证据不一，再测一次'（gap-filling 版，无视角翻转）"
  - "讲法C: 政治阴谋故事 — '共同所有者在操纵市场'（最阴暗版；反垄断叙事的一端）"
  - "本文: 涨潮叙事 — 共同所有者推动组合 CSR 普遍提升（portfolio perspective：CSR spillovers 降低系统性风险）。选择理由：'a new and opposing view' 是标题级的视角翻转而非增量补充；机制链完整（spillovers → systematic risk → aggregate returns），不是口号式反转"
```

### storytelling_tools

```yaml
storytelling_tools:
  human_face: "CalPERS 高管引语（Theory 开篇：climate risk / divestment dilemma——真实投资困境具名化）；TD Bank parental leave + harassment scandal 作 CSR spillover 的具象例子"
  rhetorical_question: "未见（Discussion 已核实 2026-08-09——'Does it pay to be green?' 是引用的学术辩论问句，非论文修辞问）"
  pacing_notes: "Stakes 后置（政策辩论收尾）；Theory stroke/glide ~70:30；showing 断裂点：H2-H4 边界推导案例密度下降（理论报告明示——contingency 小节常见弱点）；Results 顺序 R1 描述+主结果 → 经济显著性转译 → 条件展开 → 内生性 → 稳健性"
  showing_telling: "标题隐喻 'A Rising Tide Lifts All Boats' 是贯穿性 metaphor；TD Bank 案例作 spillover 的 showing；Conclusion 的 'tragedy of the commons' 对照收口（涨潮 vs 公地悲剧的意象对）"
  voice: "主动语态高频（'We argue...', 'We predict...', 'We hypothesize...'）；被动仅用于定义"
```

### cross_paper_notes

- **与 DesJardine 2023（同第一作者、同 common ownership 语境，最强对照对）**：同一现象域、两篇论文、两种故事——2022 = overlooked-alternative（主流看漏组合视角，翻硬币）；2023 = irony-reversal（共同所有者用媒体作战略工具，监督驱动地下化，换镜头）。"同作者同现象不同故事"。
- **与 Lashley & Pollock 2020（overlooked-alternative 双原型）**：desjardine2022 = deductive 宣战（'Most research underscores'）；lashley2020 = inductive 长出（remove 从数据里长出来）——同型两种系紧方式。
- **⚠️ vault 勘误**：`desjardine2023_rising_tide_*` 命名的 M/R 报告与 `mvp30/desjardine2023_rising_tide_narrative.md` 实为本文（source_text 标题 = "A Rising Tide Lifts All Boats"）；theory 报告 `common_ownership_csr_distilled_theory.md` frontmatter 明示 2022。vault 报告命名体系里 2022/2023 混标，引用时以 source_text/frontmatter 为准。
- 勿与 desjardine2023（The New Invisible Hand，ASQ）混淆——注册表历史：早前会话曾误把 2023 挂入 11-overlooked-alternative，2026-07-30 已修正（2023 的变体Z/AA 在 01-despite-progress-unaddressed）。
