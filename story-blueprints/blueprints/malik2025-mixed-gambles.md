# Story Blueprint — Malik, Wang, Martin & Gomez-Mejia (2025) JM

## 文件头

```yaml
id: malik2025
paper: "Malik, Wang, Martin & Gomez-Mejia (2025, JM) — Mixed Gambles in Product Recalls: How CEO Stock Options Drive Impression Management Tactics"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（memory intro + vault fine 报告 + 全文回读）→ ROBUST
source_records: [project_mvp30_malik2025_intro, vault fine intro/theory 报告, parsed full text]
vault_reports:
  intro: "narrative_analysis/introduction/mvp30/fine_grained/batch_2026-05-24/Malik_etal_2025_JM_distilled_introduction.md"
  theory: "narrative_analysis/theory/mvp30/fine_grained/batch_1/Malik_2025_JM_distilled_theory.md + batch_2026-05-24/Malik_etal_2025_JM_distilled_theory.md"
  methods_results: "（fine methods/results 报告未检索到——全文回读补实）"
  story_arc: null
corpus_links:
  write-introduction: "Data-point Hook（75% CEO pay）+ Construct Preview 前置（非标准模块序列）+ 'two reasons' 结构化 Stakes——变体来源，路径待验证"
  write-theory: "mixed gamble/BAM 双轨（wealth-preservation vs wealth-maximizing）——路径待验证"
  write-methods: "Heckman 选择 probit（FDASIA IV）+ 2SLS（Bartik IV + lagged exercisable options）——路径待验证"
```

## Story

### one_liner

> 股票期权研究知道正常条件下期权如何塑造 CEO 决策（风险承担、R&D、并购），但危机条件下"little is known"——召回中 CEO 面对双重财富压力（mixed gamble）：现有期权财富驱动印象管理战术（择机召回 inattentive recall + 战略沉默 strategic silence），未来期权财富抑制之，负面媒体报道遏制之——"保护已有财富"与"追求未来财富"在同一期权组合内反向拉扯。

### knot

```yaml
knot:
  primary_type: half-domain-gap         # 第三原型：malshe 维度半区 / wu2025 行为半区 / 本文情境半区（正常 vs 危机条件）
  compound_types: []                    # 双轨机制（current→IM / prospective→反 IM）是理论结构，非子类型
  statement: "股票期权研究充分覆盖正常/战略条件（风险承担、R&D、并购——mixed gamble 常规应用），但 adverse events
              （召回等危机）条件下'little is known'——CEO 在危机中面临双重财富压力：现有期权财富驱动 IM 战术
              （择机+沉默）、未来期权财富抑制之、负面媒体遏制之"
  tied_at:
    - "Intro P2-P3：文献 turn（正常条件已知）→ Tension（'little is known about how stock options shape CEO
      decision-making during adverse events'——Context-Restricted Incompleteness）"
    - "Intro P4-P5：Construct Preview 前置（两种 IM 战术先定义再引入理论——proactive timing vs passive silence 对比）"
  untied_at:
    - "Theory H1-H4：双轨财富动机 + 媒体调节"
    - "Results Table 3/4：双轨镜像（current 0.002*/0.012***、prospective −0.001*/−0.002**）+ 媒体遏制"
  antagonist: "期权研究的正常条件导向（Context-Restricted——危机条件的期权作用被忽略）"
  antagonist_built_by:
    - "'However, little is known about...'（Context-Restricted 缺口句式）"
    - "'This oversight is important for two primary reasons'（结构化 Stakes——危机行动后果 + 期权-股东对齐可能破裂）"
    - "Construct Preview 前置（战术先于理论——现象前推叙事）"
```

### characters

```yaml
characters:
  protagonist: [CEO option wealth（X——current vs prospective 双成分）, IM tactics（DV——inattentive recall + strategic silence 双战术）]
  supporting:
    - "mixed gamble/BAM（透镜——财富保护 vs 财富追求的双重压力）"
    - "negative media coverage（调节——监督遏制：silence 被遏制 −0.064/−0.008）"
    - "stakeholders（受害方——信息不对称：消费者无法及时知情）"
    - "boards/compensation committees（实践端——期权组合平衡）"
  ensemble: [医疗设备召回（FDA）、Heckman probit（FDASIA IV）、2SLS（Bartik IV）、Boeing 737 Max（Discussion 案例）]
```

### resolution_logic

`exploration` 拓荒（补上危机情境半区——双轨财富动机分工 + 媒体监督条件化——"保护"与"追求"的动机地图）。

### five_acts

```yaml
five_acts:
  exposition: "Intro P1-P3：Data-point Hook（'nearly 75% of total CEO pay'——股票期权占比）→ 文献 turn（正常条件已知）→ Tension（adverse events 下 little is known）→ Stakes（two reasons）"
  rising_action: "Intro P4-P5（Construct Preview 前置——proactive timing vs passive silence 定义对比）+ P6-P8（BAM/mixed gamble 透镜 + 预览 + 双流贡献）+ Theory（wealth-preservation vs wealth-maximizing 双轨）+ Methods（医疗设备召回、Heckman probit + 2SLS Bartik）"
  climax: "Results Table 3/4——双轨揭晓：current wealth → IM 战术（inattentive 0.002, p=.041 / silence 0.012, p<.001——90%→93%）、
           prospective wealth → 抑制（−0.001, p=.04 / −0.002, p<.01——23%→21%、91%→89%）——同一期权组合内两种财富动机反向驱动"
  falling_action:
    - "媒体监督条件化（H3a/H4a 部分支持——inattentive 效应在媒体阈值两侧 [0.15] 变化；H3b/H4b 支持——silence 被媒体遏制 −0.064, p<.001 / −0.008, p<.05——监督有效）"
    - "内生性三层（Heckman 选择 [FDASIA IV：b=0.288, p<.05] + 2SLS [Bartik shift-share + lagged exercisable options] + CEO FE）"
    - "稳健性（媒体窗口 60 天、IM 差异检验、替代测量）"
  denouement: "Discussion——回到开头：wealth-preservation vs wealth-maximizing 双效应（相对权重决定主导）；
               mixed gamble 扩展到 adverse events（'looming losses'——Kahneman & Tversky）；stakeholder welfare
               （IM 战术转移对利益相关者的注意力——**Boeing 737 Max**：2012 已知安全问题隐瞒 FAA、157 死、Calhoun 解职、
               2024 门塞事故——具名案例）；媒体作为社会监督者（'watchdog'）"
```

### stakes

```yaml
stakes:
  theoretical: "期权研究正常条件充分、危机条件空白——mixed gamble 未扩展到 adverse events（'looming losses' 决策情境）"
  practical: "召回中的 IM 战术威胁消费者安全（医疗设备——身体伤害甚至死亡）；Boeing 737 Max 157 死；董事会需平衡期权组合
              （prospective 导向可抑制 IM 战术）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 期权-风险承担版——正常条件下期权如何塑造 R&D/并购/风险（期权文献主流——mixed gamble 常规应用）"
  - "讲法B: 危机沟通版——只做 IM 策略类型学（危机沟通文献——不接 CEO 激励）"
  - "讲法C: 召回后果版——召回的市场反应/学习（recall 文献主流——换 DV）"
  - "本文: 情境半区补缺版——正常→危机条件的期权研究补全 + 双轨财富动机 + 媒体监督遏制"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "**Boeing 737 Max**（Discussion——2012 隐瞒 FAA、157 死、Calhoun 解职、2024 门塞事故——具名企业+死者规模）；
               Friday recalls（Diestre——周五召回延迟公众知晓）"
  rhetorical_question: "未见 pivot【已核实】——'This oversight is important for two primary reasons'（陈述式结构化 Stakes）"
  pacing_notes: "Construct Preview 前置（非标准——战术先于理论）；双 DV 镜像呈现（Table 3/4 对位——inattentive/silence）；
                 climax=双轨揭晓；falling action 媒体条件化+三层内生性"
  showing_telling: "'looming losses'（Kahneman 概念引用）；75% CEO pay（数据点 Hook）；'two primary reasons'（结构化 stakes）；
                    边际效应图（Figure 1-8——媒体阈值 0.15 的可视化）"
  voice: "中立实证；'This oversight is important'（重要性标注）；谨慎（'partially supported'——H3a/H4a 部分支持的诚实报告）"
```

### cross_paper_notes

- **half-domain-gap 三原型（半区的三种形态）**：malshe2015（equity/debt——**维度**半区+跨学科嫁接）↔ wu2025（reactive/proactive——**行为**半区+制度冲击）↔ malik2025（正常条件/危机条件——**情境**半区）。
- **recall 现象域前因侧对照对（本批内部）**：eilert2017（组织层面——problem severity/品牌特征决定召回时机）↔ malik2025（CEO 层面——期权财富决定 IM 战术）——recall 行为前因的两视角。
- **与 singh2023 的媒体监督对照**：singh（媒体制衡游说——减少召回扭曲）↔ malik（媒体遏制 IM 战术——减少信息操纵）——"媒体作为监督者"家族 2 例。
- **BAM 动机透镜家族**：与 gamache2020（regulatory focus）同属 CEO 动机透镜——gamache 统一引擎（cross-domain-unification）、malik 双轨分裂（half-domain-gap）。
- **判别器记录**：half-domain-gap 判定基于天然双极（正常/危机）+ 一极空白（Context-Restricted Incompleteness——memory 分类互证）。
