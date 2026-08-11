# Story Blueprint — Wu, Bruton & Krause (2025) SMJ

## 文件头

```yaml
id: wu2025
paper: "Wu, Bruton & Krause (2025, SMJ) — Activism Risk and Corporate Self-Regulation: Investigating How Anti-SLAPP Laws Impact Firms' Institutional Corporate Social Performance"
distilled_sections: [intro, theory, methods, results]      # 2026-08-09 读全文定稿 → ROBUST
source_records: [vault narrative: narrative_analysis/mvp30/wu2025_activism_risk_antislapp_narrative.md]
vault_reports:
  intro: "narrative_analysis/mvp30/wu2025_activism_risk_antislapp_narrative.md"
  theory: "parsed_texts/mvp30/Activism risk...（§2：anti-SLAPP 立法史/行动主义风险/CSP 自我规制/媒体覆盖调节）"
  methods_results: "parsed_texts/mvp30/Activism risk...（§3-4：DiD + 事件研究 + 置换检验）"
  story_arc: "narrative_analysis/_story_arcs/wu2025_activism_risk_antislapp_smj_story_arc.md"
corpus_links:
  write-introduction: "'backward-looking... forward-looking' 贡献时间框架"
  write-methods: "DiD（交错立法 30 个处理、firm/state/year FE、firm 聚类 SE）；平行趋势事件研究 [−6,+6]；置换检验 500 次"
  write-results: "主效应 + 调节（0.22*→0.30***）；技术 CSP/CSR 委员会 placebo 结果（判别效度）"
```

## Story

### one_liner

> 文献研究的是企业**如何回应**利益相关者行动主义（reactive），而日常现实是企业**如何预防**（proactive）——Parker 说"日常现实是预防而非反应"。反 SLAPP 法（降低行动主义诉讼风险）让企业提前自我规制：制度 CSP 提升 0.21 个标准差，且媒体曝光越多的企业提升越大——预防不是口号，是法律冲击下的因果行为。

### knot

```yaml
knot:
  primary_type: half-domain-gap   # 双原型（malshe2015 + wu2025）
  compound_types: []
  statement: "企业如何应对 stakeholder activism？文献研究 reactive 半区（回应/防御），proactive 半区（预防性自我规制）空白——'daily reality is prevention rather than reaction'（Parker 引语）"
  tied_at:
    - "Intro P2：Parker 权威引语（半区 pivot 的代言人）"
    - "Theory §2.1-2.3：anti-SLAPP 立法史 → 行动主义风险上升 → 制度 CSP 作自我规制回应"
  untied_at:
    - "Results：DiD 主效应（anti-SLAPP → institutional CSP β=0.22, p=.004）——预防半区因果成立"
  antagonist: "文献的 reactive 重心——'回应研究充分'被当成'应对研究充分'；预防性自我规制整体缺席"
  antagonist_built_by:
    - "Parker 引语立半区落差（'日常现实是预防而非反应'）"
    - "P1 背景铺陈（activism 定义+形式+后果清单）——先把 reactive 文献完整度立起来"
```

### characters

```yaml
characters:
  protagonist: [anti-SLAPP laws (X，交错立法处理), institutional CSP (Y，预防性自我规制的代理)]
  supporting:
    - "media coverage of CSI（RepRisk——行动主义风险的可见代理：调节）"
    - "activism risk（RRI——机制假设的代理，supplemental 验证）"
  ensemble: [MSCI/Compustat 3,488 家 1991-2018、firm/state/year FE、BoardEx CSR 委员会（placebo）、SigWatch NGO 行动（补充）]
```

### resolution_logic

`exploration` 拓荒——补 proactive 半区，用制度冲击（anti-SLAPP 交错立法）作准实验识别。研究者是跨界测绘者 + 因果鉴定人：文献地图上只有"回应"一块，本文画上"预防"并给出 DiD 证据。与 malshe2015 同型（补半区），识别策略是自然实验（更强）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：activism 背景（定义/形式/后果清单）；Parker 引语缺口（预防 vs 反应的半区落差）"
  rising_action: "Theory：anti-SLAPP 立法史（§2.1——30 个州交错立法）→ 行动主义风险上升（§2.2）→ 制度 CSP 作自我规制回应（§2.3——社区/环境/人权三域）→ 媒体覆盖调节（§2.4）；Methods：DiD（firm/state/year FE + firm 聚类；处理变量不滞后）"
  climax: "Results：anti-SLAPP → institutional CSP β=0.22（p=.004，≈0.21 SD——Model 1 无控制版本防 bad controls）——预防半区因果成立"
  falling_action:
    - "调节：media coverage of CSI × anti-SLAPP β=0.30（p<.001）——行动主义风险可见时预防更用力（图：高覆盖陡线 vs 低覆盖平线）"
    - "事件研究平行趋势 [−6,+6]：处理前无差异、处理后 +1 年起效且持续 6 年——排除预期与反因果"
    - "置换检验 500 次：placebo 系数聚零——排除未观测特征"
    - "Supplemental：技术 CSP/CSR 委员会 placebo 全 null（判别效度——预防是真实的绩效改进非结构性表演）；RRI 行动主义风险上升验证机制假设；SigWatch 证明 CSP 降低被行动主义盯上的概率"
  denouement: "Discussion：三贡献——proactive vs reactive（半区补全）/ multi-level interaction / subnational institutions（州级制度的意外上行）"
```

### stakes

```yaml
stakes:
  theoretical: "行动主义研究只看 reactive 半区，'企业如何预防行动主义'图景空白——不补，企业-行动者互动理论停在回应逻辑；且'预防'需要因果证据而非口号"
  practical: "反 SLAPP 法的政策后果：降低行动主义诉讼风险反而促使企业提前自我规制（预防性 CSP）——法律冲击的意外上行；媒体曝光是预防的放大器"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: reactive 故事 — '企业如何回应行动主义'（文献惯例）"
  - "讲法B: gap-filling 折中 — '回应研究证据不一，再测一次'（无半区翻转）"
  - "讲法C: 法律负面故事 — '反 SLAPP 法压制行动主义、伤害社会监督'（把法律讲成反派）"
  - "本文: proactive 半区 + 自然实验 — 预防是日常现实（Parker），回应只是另一半。选择理由：权威引语立半区落差；DiD 把'预防'从口号变成因果证据；placebo 三重验证防'表演性 CSP'的质疑"
```

### storytelling_tools

```yaml
storytelling_tools:
  human_face: "未见具名 actor（已核实 2026-08-09 intro/methods——现象以机构（anti-SLAPP 法）与法律为主体，人面由 NGO 行动主义数据源（SigWatch）隐性承担）"
  rhetorical_question: "未见（已核实 2026-08-09）"
  pacing_notes: "P1 背景 → P2 引语急转（半区 pivot）→ Theory 立法史-风险-回应-调节四步 → climax 主效应 → falling 调节/平行趋势/置换/placebo 四重加固"
  showing_telling: "Parker 引语作 telling 锚；调节图（高/低覆盖双线）作 showing；平行趋势图（处理前后）作识别策略的 showing"
  voice: "we estimate/we follow 中性学术语态（已核实 2026-08-09）"
```

### cross_paper_notes

- **与 Malshe 2015（half-domain-gap 双原型）**：equity/debt（跨学科嫁接+同时方程）vs reactive/proactive（制度冲击+DiD）——同型两种实现：半区 pivot 都由"权威/现实落差"立起，识别策略不同。'补半区'的 arena 可以是跨学科嫁接、可以是自然实验。
- **与 DesJardine 2023（媒体×机构投资者家族）**：同为媒体/制度叙事——desjardine2023 是共同所有者把媒体当武器（irony）；wu2025 是媒体覆盖放大预防动机（调节）——媒体的两种故事角色。
- **与 wowak2025（制度冲击家族）**：wowak 用法律冲击作 IV（Lewbel）；wu2025 用立法作 DiD 处理——制度冲击的两种用法。
