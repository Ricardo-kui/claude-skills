# Story Blueprint — Antón, Ederer, Giné & Schmalz (JPE) — Common Ownership, Competition, and Top Management Incentives

## 文件头

```yaml
id: top_mgmt_incentives
paper: "Antón, Ederer, Giné & Schmalz（JPE）— Common Ownership, Competition, and Top Management Incentives"
paper_type: quantitative   # 理论模型 + 实证
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（共同所有权/07 原文）→ ROBUST
source_records: [parsed full text（共同所有权/07 原文）]
vault_reports:
  intro: null（共同所有权文件夹原文回读）
  methods_results: null（全文回读：面板 + 多共同所有权测量）
  story_arc: null
corpus_links:
  write-theory: "激励合约机制（WPS——共同所有权→产品市场结构的传导）——路径待验证"
```

## Story

### one_liner

> 共同所有权影响产品市场结构的机制——被忽略的**激励合约通道**：共同所有权水平决定高管激励斜率（WPS——财富-绩效敏感性）——"various previously documented (but unmodeled) results"的建模解释——核心预测"has not been tested thus far"——本文理论建模 + 实证检验。

### knot

```yaml
knot:
  primary_type: neglected-arena         # 第九原型：激励合约机制子域（'documented but unmodeled'——'not been tested thus far'）
  compound_types: []                    # 激励合约传导是机制，非子类型
  statement: "共同所有权→产品市场结构的结果已被记录（'various previously documented results'）但未建模（'unmodeled'）——
              缺失机制=高管激励合约（'provide a mechanism—namely, managerial incentive contracts—through which common ownership
              can affect product market structure'）——核心预测（激励斜率随共同所有权水平变化）'has not been tested thus far'——
              本文理论建模 + 面板实证（多共同所有权测量）"
  tied_at:
    - "Intro：共同所有权→产品市场结构的既有结果（'previously documented (but unmodeled) results'）→ 激励合约机制引入（'provide a mechanism'）→ 核心预测未检验声明"
    - "Theory：激励合约模型（cosine similarity/利润权重——所有权相似性→利润内部化）"
  untied_at:
    - "Theory：激励斜率 × 共同所有权水平"
    - "Results：WPS 随共同所有权变化（面板实证——多测量）"
  antagonist: "共同所有权研究的直接路径理解（结果已记录但机制未建模——'documented but unmodeled'）"
  antagonist_built_by:
    - "'various previously documented (but unmodeled) results'（已记录未建模声明）"
    - "'provide a mechanism—namely, managerial incentive contracts'（机制引入——传导通道）"
    - "'central prediction... has not been tested thus far'（未检验预测——子域空白声明）"
```

### characters

```yaml
characters:
  protagonist: [common ownership（X——多测量）, top management incentives（DV——WPS 斜率）]
  supporting:
    - "激励合约机制（'managerial incentive contracts'——共同所有权→产品市场结构的传导）"
    - "cosine similarity/利润权重（所有权相似性→利润内部化——'origin of the incentive to internalize the profits of another firm'）"
    - "多测量（cosine/AP/HJL/MHHID/Top5——测量三角）"
    - "对称 vs 非对称（'cosine similarity is the symmetric component... relative shareholder concentration term is inherently asymmetric'）"
  ensemble: [美国上市公司面板、WPS 测量、多共同所有权测量、行业-年份/公司 FE]
```

### resolution_logic

`exploration` 拓荒（补激励合约机制子域——理论建模 + 实证检验——"已记录未建模"的机制地图）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：共同所有权→产品市场结构的既有结果（'documented (but unmodeled)'）→ 激励合约机制引入（'provide a mechanism'）→ 核心预测未检验（'not been tested thus far'）"
  rising_action: "激励合约模型（cosine similarity/利润权重——所有权相似性→利润内部化——对称/非对称分解）+ 多测量 + Methods（面板 + FE）"
  climax: "Results——核心预测揭晓：高管激励斜率随共同所有权水平变化（'the strength of top management incentives varies across firms by the level of common ownership'——未检验预测的首次实证）"
  falling_action:
    - "多测量稳健（cosine/AP/HJL/MHHID/Top5——'rank-transformed measures... to allow for straightforward comparisons'）"
    - "识别（行业-年份 FE 排除共同趋势 + 公司 FE 排除遗漏特征——'remaining source of identifying variation is mainly differences across firms in changes over time'）"
    - "稳健性（winsorize 1% + 双聚类）"
  denouement: "Discussion——激励合约作为共同所有权的传导机制（'provide an explanation for various previously documented (but unmodeled) results'）；
              理论贡献（建模此前未建模的机制）；实证含义（WPS 随共同所有权的系统性变化）"
```

### stakes

```yaml
stakes:
  theoretical: "共同所有权→产品市场结构的机制未建模——'documented but unmodeled'——激励合约通道空白"
  practical: "高管激励设计（WPS 随共同所有权的变化）；竞争政策（激励合约作为传导通道的政策含义）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 反竞争版——共同所有权减少竞争（Azar et al.——市场力量——结果已记录）"
  - "讲法B: 效率版——共同所有权促进溢出（efficiency——结果已记录）"
  - "讲法C: 治理版——共同所有权治理效应（blockholder 监督——denicolo2025——治理通道）"
  - "本文: 激励合约揭幕版——高管激励作为传导机制（'documented but unmodeled'——理论建模 + 实证）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "无具名企业（面板实证）；cosine similarity（'effective sympathy'——概念拟人化——'the intensity of the influence of potentially asymmetric common ownership links'）"
  rhetorical_question: "未见【已核实】"
  pacing_notes: "已记录未建模→机制引入→理论模型→多测量实证；climax=激励斜率随共同所有权变化揭晓；falling action 多测量+识别+稳健性"
  showing_telling: "'documented but unmodeled'（已记录未建模——缺口表述）；'effective sympathy'（有效同情——所有权连接的拟人化）；'origin of the incentive to internalize the profits of another firm'（内部化起源）"
  voice: "JPE 理论实证口吻；'central prediction'（核心预测标注）；'we remain agnostic'（功能形式谦逊）"
```

### cross_paper_notes

- **neglected-arena 九原型（激励合约机制子域）**：desai2012/park2013/eilert2017/kashmiri2017/kalaignanam2013/pupovac2025/hoffmann2024/desjardine2025/**top_mgmt_incentives**——'documented but unmodeled'（原文锚）。
- **共同所有权家族七篇成型**——激励通道与 denicolo2025（blockholder 监督）对照：治理双通道（监督 vs 激励合约）。
- **与 denicolo2025 的姊妹对照**：denicolo（治理均衡——blockholder 监督）；JPE（激励传导——WPS）——共同所有权的两个治理机制。
- **判别器记录**：neglected-arena 判定基于机制子域未建模（'documented but unmodeled'——'not been tested thus far'——原文锚）。
