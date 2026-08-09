# Story Blueprint — Zhao-Ding & Gaba (2022) Organization Science

## 文件头

```yaml
id: zhao_ding2022
paper: "Zhao-Ding & Gaba (2022, OrgSci) — Positioning in Digital Markets: A Demand-Side View"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（vault 报告 + 全文回读）→ ROBUST
source_records: [project_mvp30_zhao-ding_gaba_orsc, vault narrative/methods_results 报告, parsed full text]
vault_reports:
  intro: "narrative_analysis/mvp30/zhao_ding2022_positioning_digital_markets_os_narrative.md"
  theory: "（memory 双区段蒸馏 2026-05-26——self-built lens + 对称反向双轨 + 三层递进 T1）"
  methods_results: "narrative_analysis/methods_results/mvp30/methods/zhao_ding2022_positioning_digital_methods_narrative.md + results/zhao_ding2022_positioning_digital_results_narrative.md + deep_distillation/papers/zhao_ding2022_..._deep_profile.md + fine_grained/batch_10_zhao2022_shen2022/zhao_ding2022_positioning_digital_fine_methods_results.md"
  story_arc: null
corpus_links:
  write-introduction: "hooks/21-dual-industry-trend.md（来源：双行业趋势对比 Hook）；contributions 变体J（Challenge Implicit Assumption——contributions/_index.md）；tensions/02-implicit-assumption-wrong.md、11-overlooked-alternative.md（相关）"
  write-theory: "corpus/sentences/construct_definition.md 变体H（三层递进 T1——来源）；mechanism_chain.md（对称反向双轨）"
  write-methods: "LDA 主题建模（文本测量）——路径待验证"
  write-results: "路径待验证"
```

## Story

### one_liner

> 定位文献从供给侧理解入场（厂商禀赋决定位置），本文翻到需求侧：入场者在需求不确定下通过顾客对其他产品的评价学习环境——但同一反馈源发出两种相反指令：不满度→聚焦核心+差异化（发现），评价异质性→分散核心+模仿成功品（模仿）——顾客的信号把入场者推向相反的两极。

### knot

```yaml
knot:
  primary_type: overlooked-alternative   # 第四原型（需求侧视角揭幕——供给侧文献看漏）
  compound_types: []                     # 对称反向双轨是机制结构而非子类型
  statement: "定位研究从供给侧看入场决策（厂商内部特征驱动位置选择），但需求不确定下入场者的关键输入是外部市场反馈——顾客对其他产品的评价；且同一反馈源的两种信号发出相反指令（不满→发现/差异化，异质性→模仿）"
  tied_at:
    - "Intro P2-P3：定位复杂化 → 新概念化（functional space）+ 外部反馈论点（In principle... In practice...）"
    - "Theory：双轨对称反向机制链"
  untied_at:
    - "Theory H1a-H2b：双 DV 镜像预测"
    - "Results Table 3/4：双 DV 相反指令兑现"
  antagonist: "定位文献的供给侧视角（隐含前提：位置选择由厂商内部禀赋/供给侧逻辑决定）"
  antagonist_built_by:
    - "Challenge Implicit Assumption 贡献变体（'Although prior work often assumes that... we show that...'）"
    - "需求侧信号作为'唯一可得学习输入'的论证（In principle... In practice...）"
    - "发现-模仿张力的概念化（定位=功能组合选择）"
```

### characters

```yaml
characters:
  protagonist: [external market feedback（X——dissatisfaction + heterogeneity 双信号）, positioning（DV——core focus + peripheral overlap 双维度）]
  supporting:
    - "overall customer dissatisfaction（信号1——未满足需求→发现/差异化）"
    - "evaluation heterogeneity（信号2——碎片化需求→模仿）"
    - "entrants（决策者——无一手经验的入场者）"
    - "successful apps（模仿参照系）"
  ensemble: [Apple App Store Photo & Video 类目、4,957 apps、LDA 功能主题、film/music 行业趋势]
```

### resolution_logic

`revelation` 揭幕（换镜头——供给侧→需求侧）+ 双轨机制分工（两种信号=两种 cue）+ 条件化（初始 vs 后续定位——信号只在无内部经验时主导）。研究者是镜头切换师 + 信号解码员：不推翻定位文献，装上一台"外部反馈"望远镜。

### five_acts

```yaml
five_acts:
  exposition: "Intro P1-P3：双行业趋势 Hook（film+music 数字化——21-dual-industry-trend）→ 定位复杂化挑战 → functional space 概念化 + 外部反馈论点（Concept-Framework-First 非标准：无独立 Lit Turn/Tension）"
  rising_action: "Theory（三层递进 T1：Context→Conceptual Framework→Construct Dimensions；对称反向双轨机制链：dissatisfaction→core(+)/overlap(−)；heterogeneity→core(−)/overlap(+)）+ Methods（App Store Photo & Video、LDA 提取功能、4,957 apps、双 DV）"
  climax: "Results Table 3/4——双 DV 镜像揭晓：dissatisfaction 正（0.0642***）/heterogeneity 负（−0.334***）于 core focus；dissatisfaction 负（−0.0328***）/heterogeneity 正（0.221***）于 overlap——同一反馈源两种信号的相反指令全部兑现"
  falling_action:
    - "Initial vs Subsequent 定位（Table 5）：后续定位符号反转（dissatisfaction −0.0299**、heterogeneity +0.0995*）——经验替代外部信号，'not merely less but differently'（信号解释随内部知识积累改变）"
    - "联合效应（Table 6）：heterogeneity 仅在 dissatisfaction 高时显著——两信号互补（碎片化需求信息在未满足需求在场时才有行动价值）"
    - "替代测量（Table 7：peripheral distance to core——0.01002***）——novelty seeking 附加证据"
  denouement: "Discussion——回到开头：外部反馈理论收口（不满=未满足需求→发现；异质性=碎片化→模仿）；贡献三段（数字市场定位文献——先例记录了品种扩张未解释位置选择；需求侧市场进入视角；pre-entry learning——外部知识在内部知识缺乏时主导）；市场细分内生化 + 汽车业泛化 + 行为 vs 表述反馈局限"
```

### stakes

```yaml
stakes:
  theoretical: "需求侧信号在入场决策中的角色被忽视——pre-entry learning 是需求不确定下入场者唯一可得的学习输入"
  practical: "入场者错读信号→定位失败；数字市场（含汽车业数字化）产品爆炸下'发现 vs 模仿'的抉择"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 供给侧定位版——位置由厂商能力/资源决定（定位文献主流）"
  - "讲法B: 效果评估版——只问'什么位置赚钱'（绩效后果视角——本文明确留作未来研究）"
  - "讲法C: 半区补缺版——需求侧作为供给侧的反面补上（half-domain-gap 折中讲法）"
  - "本文: 需求侧镜头揭幕版——外部反馈双信号相反指令 + functional space 概念化 + LDA 量化——选择理由：不是补半区而是换到入场者决策视角（pre-entry learning）；'评价影响顾客选择'升级为'评价同时塑造企业战略选择'"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "film+music 双行业趋势（Hook 具名行业）；Apple App Store Photo & Video 设定；汽车业数字化泛化（Discussion）"
  rhetorical_question: "未见 pivot【已核实】——Concept-Framework-First 不用修辞问；Discussion 局限段有一研究问句（do detailed reviews amplify...?——非 pivot）"
  pacing_notes: "Concept-Framework-First（~50% intro 篇幅建框架，无独立 Lit Turn/Tension/Stakes）；Theory 双轨完全平行反向（矩阵节奏）；Results 双 DV 对位呈现（Table 3/4）；falling action 三组补充含符号反转惊喜"
  showing_telling: "functional space 概念隐喻（产品=功能集合）；LDA 功能主题作量化 showing（文本→功能空间）；Figure 5 交互图（高/低 dissatisfaction 下 heterogeneity 斜率对比）；'In principle... In practice...' 对比句式"
  voice: "主动语态；概念化口吻（'We therefore conceptualize...'）；克制（T5 缺失、无 T6——theory-empirics 不对称诚实报告）"
```

### cross_paper_notes

- **overlooked-alternative 四原型**：desjardine2022（理论宣战）/ lashley2020（数据长出）/ singh2023（丑闻+识别）/ zhao_ding2022（供给侧→需求侧镜头）——"看漏一面"四种系紧方式。
- **与 malshe2015 的"跨域"对照**：malshe 跨学科补半区（finance→marketing），zhao_ding 同域内换镜头（供给侧→需求侧）——"跨域"≠"换侧"。
- **与 cutolo2024（在线市场文本构念测量家族）**：LDA vs 叙事文本——测量同源、故事不同。
- **无 Tension 段的非标准故事**：与 singh2023（极简 Intro）同属"非标准模块"家族——singh 无 Lit Turn 靠 Should-be-Yet，zhao_ding 无 Tension 靠框架先行——knot 不一定要在 intro 系紧（Tension 在 Theory 系紧）。
