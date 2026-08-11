# Story Blueprint — Antón, Ederer, Giné & Schmalz (2025) Management Science

## 文件头

```yaml
id: anton2025
paper: "Antón, Ederer, Giné & Schmalz (2025, MgmtSci) — Innovation: The Bright Side of Common Ownership?"
paper_type: quantitative   # 理论模型 + 实证
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（OCR 全文回读）→ ROBUST
source_records: [OCR parsed full text]
vault_reports:
  intro: null（OCR 全文回读）
  methods_results: null（OCR 全文回读：美国上市公司全样本、BGI 外生变异）
  story_arc: null
corpus_links:
  write-introduction: "标题问句（'The Bright Side of Common Ownership?'）+ 反竞争关注 vs 亲竞争角色（'much less work'）——路径待验证"
  write-methods: "创新投入/产出 × 产品市场邻近度 × 技术邻近度 + BGI 外生变异——路径待验证"
  write-results: "溢出下亮面/无溢出暗面 + 邻近度条件——路径待验证"
```

## Story

### one_liner

> 共同所有权的反竞争效应引发大量关注——但"much less work has been devoted to its procompetitive and potentially welfare-enhancing role"——本文揭示亮面：存在技术溢出时，共同所有权缓解创新激励不足（surplus appropriability 问题）——促进创新；无溢出时创新=抢市场份额、共同所有权反而减少创新——产品市场邻近度↓/技术邻近度↑时亮面更强。

### knot

```yaml
knot:
  primary_type: overlooked-alternative  # 第八原型：共同所有权亮面被看漏（反竞争关注主导——'much less work on procompetitive role'）
  compound_types: []                    # 溢出/业务偷取条件化是机制，非子类型
  statement: "共同所有权的反竞争效应（'much attention has focused on the empirical investigation of anticompetitive effects'）vs
              亲竞争角色（'much less work has been devoted to its procompetitive and potentially welfare-enhancing role'——
              亮面被看漏）——技术溢出时共同所有权缓解创新激励不足（surplus appropriability）；无溢出时创新=业务偷取、
              共同所有权反而减少创新——产品市场邻近度↓/技术邻近度↑时亮面更强"
  tied_at:
    - "Intro：美国经济两趋势（集中度↑+创新↓ vs 共同所有权↑）→ 反竞争关注 vs 亲竞争角色（'much less work'——亮面被看漏）→ 本文双考察（理论+实证）"
    - "Theory：溢出模型（surplus appropriability——创新激励不足）+ 业务偷取（无溢出时）"
  untied_at:
    - "Theory：共同所有权 × 创新（溢出条件下）"
    - "Results：邻近度条件（产品市场邻近度↓/技术邻近度↑→亮面增强）+ BGI 外生变异"
  antagonist: "共同所有权研究的反竞争导向（'much attention... anticompetitive effects'——亮面被看漏）"
  antagonist_built_by:
    - "两趋势并置（集中度+创新↓ vs 共同所有权↑——'spirited discussion'）"
    - "Softbank Vision Fund 案例（ride-hailing——'dominate ride-hailing'——反竞争叙事的具象）"
    - "'much less work has been devoted to its procompetitive and potentially welfare-enhancing role'（看漏亮面声明）"
```

### characters

```yaml
characters:
  protagonist: [common ownership（X）, corporate innovation（DV——投入+产出）]
  supporting:
    - "技术溢出机制（亮面——'common ownership of technologically related firms mitigates this problem'——surplus appropriability）"
    - "业务偷取机制（暗面——'without technological spillovers, innovation has the effect of stealing market share from rivals'）"
    - "product market proximity（条件——邻近度↓→亮面强）"
    - "technology proximity（条件——邻近度↑→亮面强）"
  ensemble: [美国上市公司全样本、BGI 收购外生变异（BlackRock）、Softbank Vision Fund 案例]
```

### resolution_logic

`revelation` 揭幕（揭幕共同所有权的亮面——溢出机制 + 邻近度条件化——"问号标题"的答案）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：两趋势并置（集中度↑+创新↓ vs 共同所有权↑）→ Softbank Vision Fund（'dominate ride-hailing'——反竞争叙事）→ 'much less work has been devoted to its procompetitive role'（亮面被看漏）"
  rising_action: "溢出模型（surplus appropriability——创新激励不足——共同所有权缓解）+ 业务偷取（无溢出时暗面）+ Methods（美国上市公司全样本、邻近度测量、BGI 外生变异）"
  climax: "Results——亮面揭晓：技术溢出下共同所有权促进创新（'common ownership of firms mitigates this impediment to corporate innovation'——问号标题的肯定回答）"
  falling_action:
    - "邻近度条件（产品市场邻近度↓/技术邻近度↑→亮面增强——'decreases with product market proximity and increases with technology proximity'）"
    - "暗面确认（无溢出时共同所有权减少创新——'more common ownership reduces innovation'——双面完整）"
    - "BGI 外生变异（BlackRock 收购——'Some of these results persist'）"
  denouement: "Discussion——共同所有权的福利效应辩论（'inform the debate about the welfare effects of increasing common ownership'）；
              亮面的条件（溢出 vs 业务偷取——'the sign and magnitude... varies considerably across the universe of firms'）；
              政策含义（反垄断评估需考虑亮面）"
```

### stakes

```yaml
stakes:
  theoretical: "共同所有权亮面被看漏——'much less work has been devoted to its procompetitive role'——创新激励的溢出维度"
  practical: "反垄断政策评估（共同所有权的福利效应——亮面 vs 暗面）；Softbank 式并购的竞争后果"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 反竞争版——共同所有权减少竞争（IO 主流——'emerging consensus'——Softbank 叙事）"
  - "讲法B: 治理版——共同所有权影响治理（治理文献——监督/协调——不接创新）"
  - "讲法C: 创新一般版——创新决定因素（R&D 文献——不接所有权）"
  - "本文: 亮面揭幕版——共同所有权→创新（溢出条件——'The Bright Side of Common Ownership?' 问号标题的肯定回答）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "Softbank Vision Fund（ride-hailing 收购——'dominate ride-hailing'——反竞争叙事的具名案例）；BlackRock/BGI（外生变异——具名机构）；Berkshire Hathaway（'pool resources' 例子）"
  rhetorical_question: "标题即问句（'The Bright Side of Common Ownership?'——标题问句家族第 7 例——疑问式标题——答案=条件性肯定）"
  pacing_notes: "两趋势并置→Softbank 案例→反竞争/亲竞争分野→溢出模型→邻近度条件；climax=亮面揭晓；falling action 双面完整+BGI 外生"
  showing_telling: "'The Bright Side...?'（标题问号——亮面/暗面意象）；'surplus appropriability'（概念）；'stealing market share'（业务偷取意象）"
  voice: "MgmtSci 理论实证口吻；'spirited discussion'（激烈辩论）；'much less work'（看漏强调）"
```

### cross_paper_notes

- **overlooked-alternative 八原型（共同所有权亮面家族）**：desjardine2022（CSR 涨潮面）↔ **anton2025（创新亮面）**——同一所有权透镜的两个亮面故事（CSR/innovation）。
- **共同所有权家族三篇成型**：desjardine2022（CSR——实证）+ anton2025（创新——理论+实证）+ denicolo2025（治理均衡——纯理论）——同一现象三透镜。
- **与 desjardine2022 的对照对**：desjardine（组合视角——涨潮——系统风险↓）；anton（溢出视角——创新↑）——共同所有权的双亮面。
- **标题问句家族第 7 例**（疑问式标题——'The Bright Side...?'）。
- **判别器记录**：overlooked-alternative 判定基于共同所有权亮面被看漏（'much less work'——原文锚——与 desjardine2022 同族）。
