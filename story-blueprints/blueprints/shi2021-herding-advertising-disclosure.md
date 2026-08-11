# Story Blueprint — Shi, Grewal & Sridhar (2021) JMR

## 文件头

```yaml
id: shi2021
paper: "Shi, Grewal & Sridhar (2021, JMR) — Organizational Herding in Advertising Spending Disclosures: Evidence and Mechanisms"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（vault 报告 + parsed 全文）→ ROBUST
source_records: [vault narrative/fine/theory/methods/results 报告, parsed full text]
vault_reports:
  intro: "narrative_analysis/mvp30/shi2021_organizational_herding_jmr_narrative.md"
  theory: "narrative_analysis/theory/mvp30/fine_grained/batch_2026-07-09/shi2021_organizational_herding_distilled_theory.md"
  methods_results: "narrative_analysis/methods_results/mvp30/methods/ + results/ + deep_distillation/papers/ + fine_grained/batch_05_shi2021_paruchuri2020/（报告齐全）"
  story_arc: null
corpus_links:
  write-introduction: "Apple Business Insider 案例（'share that kind of data with competitors'）+ FRR44 1994 自愿披露转折——路径待验证"
  write-methods: "部分重叠战略组识别（Bramoullé 法——多战略组成员身份）——路径待验证"
  write-results: "羊群效应（+10% 同行→+4.8%-8.9% 披露概率）+ 相似同行主导——路径待验证"
```

## Story

### one_liner

> 1994 年 FRR44 让广告支出披露从强制变自愿——披露率骤降后又回升——这是**组织羊群**：披露决策不是独立的，企业从同行决策中学习以缓解不确定性（信息级联）；用部分重叠战略组的新识别法证明因果羊群（同行披露 +10%→本企披露概率 +4.8%-8.9%）——企业更信相似规模同行而非标杆领导者。

### knot

```yaml
knot:
  primary_type: half-domain-gap         # 第八原型：羊群研究的披露情境半区（羊群文献做了实践采纳——披露决策空白）
  compound_types: []                    # 信息级联是机制，非子类型
  statement: "组织羊群文献研究实践采纳（Angst 2010/Gaba & Meyer 2008——'adoption of new organizational practices'）；信息披露决策
              的羊群空白——'one of the first studies to examine temporal aspects of the contagion process in firms' strategic
              information disclosure decisions'——1994 FRR44 自愿化后披露率下降又回升=羊群传染——同行披露 +10%→本企披露
              +4.8%-8.9%——企业更信相似规模同行而非标杆"
  tied_at:
    - "Intro：Apple Business Insider 案例（'not want to share that kind of data with competitors'——披露的战略两难）→ FRR44 1994 自愿化（Figure 1：32.81%-40.61%→15.84%→回升 38.61%）→ 两个 RQ（羊群 vs 共同因素；信息源）"
    - "Theory：信息级联（Banerjee/Bikhchandani——披露不确定性 + 同行可信信息源 + 理性信念更新）"
  untied_at:
    - "Theory H1-H4：羊群 + 四子群（高影响/相似/低影响/不相似）"
    - "Results：羊群确认（+4.8%-8.9%）+ 相似规模同行主导 + 财务地位相似性"
  antagonist: "羊群研究的实践采纳导向（'adoption of new organizational practices'——信息披露决策被跳过）"
  antagonist_built_by:
    - "Apple 案例（'share that kind of data with competitors'——披露两难的具象——财务市场有用 vs 产品市场泄露）"
    - "Figure 1 披露率 V 型（FRR44 后骤降又回升——'correlation among firms' reporting behaviors'——传染的视觉证据）"
    - "双 RQ 排布（羊群 vs 共同因素——识别问题；信息源——基准 vs 相似）"
```

### characters

```yaml
characters:
  protagonist: [peer disclosure（X——同行披露决策）, firm disclosure probability（DV——广告支出披露）]
  supporting:
    - "信息级联机制（披露不确定性 + 同行可信性——'a rational firm will update its prior belief'）"
    - "四子群（高影响/相似/低影响/不相似——基于规模/盈利/市值——相似规模同行主导）"
    - "战略组成员身份（部分重叠——'firms belong to multiple strategic groups'——识别设计）"
    - "FRR44 制度断点（1994——自愿披露的准自然实验）"
  ensemble: [美国上市公司、FRR44 前后、部分重叠战略组（Bramoullé 法）、Apple Business Insider 案例]
```

### resolution_logic

`exploration` 拓荒（补羊群披露情境半区——信息级联机制 + 部分重叠识别 + 四子群信息源地图）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：Apple Business Insider（'share that kind of data with competitors'——披露两难）→ FRR44 1994 自愿化（Figure 1：32.81%-40.61%→15.84%→回升 38.61%）→ 双 RQ（羊群 vs 共同因素；信息源）"
  rising_action: "信息级联理论（披露不确定性 + 同行可信信息源 + 理性信念更新——Banerjee/Bikhchandani）+ 部分重叠战略组识别（Bramoullé 法——多战略组成员身份）+ Methods"
  climax: "Results——羊群揭晓：同行披露 +10%→本企披露概率 +4.8%-8.9%（'robust evidence for herding effects among peer firms in the same strategic group'——传染的因果确认）"
  falling_action:
    - "信息源揭晓（相似规模同行主导而非标杆领导者——'firms believe that similar-sized peers... provide information to resolve uncertainty'）"
    - "相似性维度（财务地位相似性影响强、业务范围相似性不显著——'financial standing similarity... relatively stronger influences'）"
    - "识别稳健（部分重叠组解决 simultaneity/correlated unobservables——Manski 批评的回应）"
  denouement: "Discussion——披露决策的传染性（'upward trend of disclosures... at least partially due to peer effects'）；
              战略含义（企业可预测竞争者的披露决策条件概率——'use knowledge of competitors' predicted advertising disclosure decisions... to their strategic advantage'）；
              政策含义（监管者面临披露要求的成本-收益权衡）"
```

### stakes

```yaml
stakes:
  theoretical: "羊群研究的披露情境空白——'one of the first studies to examine temporal aspects of the contagion process in firms' strategic information disclosure decisions'"
  practical: "披露决策的战略两难（财务市场信号 vs 产品市场泄露——Apple 案例）；监管者披露政策（FRR44 的后果）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 披露决定版——披露决策的决定因素（voluntary disclosure 文献——Ellis et al./Simpson——不接同行传染）"
  - "讲法B: 羊群采纳版——实践采纳的羊群（组织羊群文献——Angst/Gaba & Meyer——非披露决策）"
  - "讲法C: 广告效果版——广告支出的绩效效果（广告文献——不接披露）"
  - "本文: 披露羊群揭幕版——信息披露决策的传染（信息级联 + 部分重叠识别 + 相似同行信息源）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "Apple（Business Insider——'share that kind of data with competitors'——具名企业+引语）；Wells Fargo 分析师（'disappointing'——财务市场视角的声音）"
  rhetorical_question: "核心问句（'So should firms disclose the amount they spend on advertising?'——披露与否的决策问句）"
  pacing_notes: "Apple 案例→FRR44 转折（Figure 1 V 型）→双 RQ→信息级联→部分重叠识别；climax=羊群揭晓（+4.8%-8.9%）；falling action 信息源+相似性维度+识别稳健"
  showing_telling: "Figure 1（披露率 V 型曲线——传染的视觉证据）；'share that kind of data'（Apple 引语——披露两难）；'partially overlapping strategic groups'（识别设计的概念）"
  voice: "JMR 实证口吻；'notoriously difficult'（识别困难承认）；'robust evidence'（稳健强调）"
```

### cross_paper_notes

- **half-domain-gap 八原型（羊群披露情境半区）**：malshe/wu/malik/mayo/lun/liu2016/denicolo2025/**shi2021**——羊群研究的披露情境（与 malik2025/mayo2022 同构的"情境半区"）。
- **MVP30-28 全覆盖达成（28/28）**。
- **与 paruchuri2020 的 batch 连接**（fine_grained/batch_05_shi2021_paruchuri2020——同批蒸馏）。
- **判别器记录**：half-domain-gap 判定基于羊群文献做了实践采纳、披露决策情境空白（'one of the first studies'——原文锚）。
