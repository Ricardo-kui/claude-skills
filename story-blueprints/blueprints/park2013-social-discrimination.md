# Story Blueprint — Park & Westphal (2013) ASQ

## 文件头

```yaml
id: park2013
paper: "Park & Westphal (2013, ASQ) — Social Discrimination in the Corporate Elite"
distilled_sections: [intro, theory, methods, results]      # 2026-08-09 读全文定稿 → ROBUST
source_records: [vault narrative: narrative_analysis/mvp30/park2013_social_discrimination_asq_narrative.md]
vault_reports:
  intro: "narrative_analysis/mvp30/park2013_social_discrimination_asq_narrative.md"
  theory: "parsed_texts/mvp30/Social Discrimination...（intergroup bias → internal attributions → journalist reports 跨层次链）"
  methods_results: "parsed_texts/mvp30/Social Discrimination...（§Method-Results：CEO 调查 + 记者调查 + Heckman 负二项）"
  story_arc: null
corpus_links:
  write-introduction: "'共识→缺口'结构（access 已研究/treatment 空白）；跨层次桥接（微观 CEO 归因→中观记者→宏观声誉）"
  write-methods: "调查+档案混合（CEO dyad 18,147 / journalist dyad 21,235）；三编码者 ICC .93；Heckman 选择（响应率 39.7%/40.8%）"
  write-results: "三向交互（相对地位 × 种族/性别对——逆马太）；负二项 RE + 聚类稳健 SE"
```

## Story

### one_liner

> 文献研究的是少数群体**怎么进**企业精英层（进入障碍），本文问的是**进去之后**：白男 CEO 对少数族裔/女性 CEO 的绩效归因偏差——同样的低绩效，他们的失败被归给领导力，而且**越成功越危险**：地位越高的少数族裔/女性 CEO 反而越被责备（逆马太效应）。记者再把这种归因写进报道，歧视从董事会流传到公众。

### knot

```yaml
knot:
  primary_type: neglected-arena   # 双原型（desai2012 + park2013）
  compound_types: [counterevidence]   # 逆马太效应（高地位少数群体更可能被责备——反直觉对照点）
  statement: "少数群体进入高管层的不利已被广泛研究（access），但已进入者的歧视（treatment）被忽视——白男 CEO 对少数族裔/女性 CEO 的绩效归因偏差（内部归因），经记者报道放大为声誉损害，且地位越高责备越重（逆马太）"
  tied_at:
    - "Intro P1：共识+缺口——'大量研究关注少数群体进入高管层的不利，但忽视了已进入者的歧视'"
    - "Intro P2：核心机制——白男 CEO 的归因偏差（intergroup bias → internal attributions）"
  untied_at:
    - "Results：H1a/H1b（白男 source × 少数族裔/女性 target 交互显著——内部归因更多）+ H2（相对地位三向交互——逆马太）+ H3-H4（记者报道传导与调节）"
  antagonist: "文献的注意力偏斜（access 研究充分、treatment 空白）+ 白男 CEO 的归因偏差（'成功了是运气，失败了是能力'——机制层反派）"
  antagonist_built_by:
    - "P1 共识-缺口结构（access 文献完整度先立起来，treatment 空白才显眼）"
    - "P2 机制引入（归因偏差从'文献盲区'落到'具体行为'——可检视的微观反派）"
```

### characters

```yaml
characters:
  protagonist: [CEO 归因偏差 (X，source CEO 对 target CEO 的内部归因), 已进入少数族裔/女性 CEO 的声誉损害 (Y)]
  supporting:
    - "relative status（source vs target——逆马太的调节：H2）"
    - "journalist 报道（跨层次桥接：H3 传导 + H4 记者种族/性别调节）"
  ensemble: [3,000 target CEOs 2005-2007、18,147 CEO dyads / 21,235 journalist dyads、21+17 预访谈、调查响应率 ~40%、Heckman 负二项 RE]
```

### resolution_logic

`exploration` 拓荒——补"进入后"战场（treatment 子域空白），跨层次桥接（微观归因 → 中观记者 → 宏观声誉）把机制连到后果。研究者是补地图的人 + 显微镜操作员：画上"进入后的歧视"，用逆马太标出反直觉地形（越成功越危险）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：共识+缺口（access 充分/treatment 空白）；核心机制（归因偏差）；跨层次桥接预告；逆马太贡献（反转经典马太）"
  rising_action: "Theory：intergroup bias → internal attributions（对低绩效的内部归因：领导力/战略决策）；CEO 归因 → 记者报道的传导链；Methods：CEO 调查（39.7% 响应率，18,147 dyads）+ 记者调查（40.8%，21,235 dyads）+ 三编码者内容编码（ICC .93）+ Heckman 负二项 RE"
  climax: "Results Table 1：H1a/H1b——白男 source CEO 对少数族裔/女性 target CEO 显著更多内部归因（white×minority、male×female 交互显著）——'进去了不等于被接纳'的量化揭晓"
  falling_action:
    - "H2 逆马太：相对地位三向交互——target CEO 地位越高（相对 source），少数族裔/女性被内部归因的概率越高——'越成功越危险'（counterevidence 落地）"
    - "H3-H4 传导：CEO 内部归因 → 记者报道中的内部归因（.26 相关基线）；记者同族/同性别的调节（谁报道影响损害程度）"
    - "Robustness：时间窗口/归因比例/自监控控制/随机单 dyad 抽样"
  denouement: "Discussion：三贡献——逆马太效应（反转'高地位受保护'的常识）/ 从自利归因到社会影响（归因偏差的他人导向）/ 记者在歧视传导中的角色；实践含义（多元化治理不能停在'进入'指标）"
```

### stakes

```yaml
stakes:
  theoretical: "多样性研究只看'进入'不看'进入后'——若已进入者的歧视不被揭示，'企业精英层多元化的价值'可能被高估；且逆马太与'地位保护'的常识相悖"
  practical: "少数族裔/女性 CEO 的真实处境：低绩效被归因偏差扭曲（内部归因→声誉损害），越成功越被苛责——董事会监督与多元化评估的真问题"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: access 故事 — '少数群体如何克服进入障碍'（文献惯例——大量研究在讲）"
  - "讲法B: 马太效应故事 — '高地位者受益更多'（经典马太——本文反转的对象）"
  - "讲法C: 组织制度故事 — '歧视来自组织制度而非个体归因'（换机制层反派）"
  - "本文: 进入后歧视 + 逆马太 + 跨层次传导 — 进来了不等于被接纳，且越成功越危险，歧视从董事会流传到公众。选择理由：'进入 vs 进入后'是文献注意力的结构性偏斜；逆马太把反直觉钉在标题级；跨层次桥接给机制完整传导链"
```

### storytelling_tools

```yaml
storytelling_tools:
  human_face: "21 位高管 + 17 位记者的预访谈（人面在场）；'成功了是运气，失败了是能力'的归因语言（机制的人格化）"
  rhetorical_question: "未见（已核实 2026-08-09：intro/methods 无问句）"
  pacing_notes: "P1 共识快铺 → P2 机制引入 → 跨层次展开 → 三贡献收束；Results 按 H1→H2（逆马太）→H3-H4（传导）递进——先主效应再反转再放大"
  showing_telling: "归因示例（Online Appendix——showing：'what attributions look like'）；逆马太交互图（待补——原文图表未在蒸馏范围）"
  voice: "we conducted/we measured 中性学术语态（已核实 2026-08-09）"
```

### cross_paper_notes

- **与 Desai 2012（neglected-arena 双原型）**：同刊（ASQ）同型——desai=学科转向（field-level 空白）、park2013=主题失衡（access/treatment）——'注意力偏斜'的两种来源。
- **与 desjardine2023 的 neglected-arena 动态版区分**：park2013/desai2012 静态遗漏 vs desjardine2023 动态再生产——同型两档。
- **与 Wowak 2025（三向交互家族）**：wowak 三向交互作竞争假设检验；park2013 三向交互作逆马太条件——三向交互的两种故事用途。
