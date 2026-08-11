# Story Blueprint — （2025, JBE）Can Common Institutional Ownership Govern CSR Decoupling?

## 文件头

```yaml
id: csr_decoupling_china
paper: "（2025, JBE）— Can Common Institutional Ownership Govern CSR Decoupling? Evidence from China"   # ⚠️ 作者信息待验证（vault 共同所有权文件夹导入）
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（共同所有权/07 原文）→ ROBUST
source_records: [parsed full text（共同所有权/07 原文）]
vault_reports:
  intro: null（共同所有权文件夹原文回读）
  methods_results: null（全文回读：中国上市公司 2009-2022）
  story_arc: null
corpus_links:
  write-introduction: "两竞争假设（coordinated governance vs collusive fraud）+ 中国情境（正式制度不足/CSR 披露弱）——路径待验证"
```

## Story

### one_liner

> CSR 脱钩（说一套做一套）被广泛批评，但如何从投资者层面治理未知——中国上市公司 2009-2022 实证：**共同机构所有权降低 CSR 脱钩**（"协调治理假说"胜出）——共同所有者通过委派高管、威胁退出、减少控股股东自利三个渠道治理——且在中国正式制度不足的情境中作用更强。

### knot

```yaml
knot:
  primary_type: paradigms-at-war        # 第七原型：coordinated governance vs collusive fraud 两竞争假设——实证裁决
  compound_types: []                    # 三渠道是机制，非子类型
  statement: "CSR 脱钩（impression management——'organized hypocrisy'）被广泛批评但投资者层面治理未知——两竞争假设（作者构建、
              扎根于文献阵营——治理正面派 vs 反竞争派）：
              'coordinated governance'（共同所有者协调行业治理——减少脱钩）vs 'collusive fraud'（共同所有者合谋——鼓励夸大披露）——
              实证裁决：共同机构所有权降低 CSR 脱钩（coordinated 胜）——委派高管/威胁退出/减少控股股东自利三渠道；
              非国企/CSR 密集/法律环境低效时更强"
  tied_at:
    - "Intro：CSR 脱钩被批评（'organized hypocrisy'——Cho et al.）→ 投资者层面治理空白 → CIO 上升（2016 后超 20%——'industry-wide normative effects'）→ 两竞争假设排布"
    - "Theory：coordinated governance vs collusive fraud（同行负外部性——DesJardine 2023 引用——vs 组合价值最大化合谋）"
  untied_at:
    - "Theory H1/H2：两假设对立预测"
    - "Results：coordinated 胜出（CIO→脱钩↓）+ 三渠道 + 三条件"
  antagonist: "CSR 治理的正式制度导向（中国正式制度不足——'laws and regulations, internal control systems, or board supervision have limited effectiveness'——CIO 作为非正式制度）"
  antagonist_built_by:
    - "两竞争假设排布（'We propose two competing hypotheses'——'coordinated governance' or 'collusive fraud'）"
    - "同行负外部性论证（DesJardine 2023 引用——'A rising tide lifts all boats'——脱钩的行业传染）"
    - "中国情境（正式制度不足 + CSR 披露弱 + 信息不对称——'a suitable research context'）"
```

### characters

```yaml
characters:
  protagonist: [common institutional ownership（X——CIO）, CSR decoupling（DV）]
  supporting:
    - "协调治理机制（'negative externalities among firms within the same industry'——共同所有者协调监督）"
    - "三渠道（委派高管/威胁退出/减少控股股东自利——channel tests）"
    - "三条件（非国企/CSR 密集/法律环境低效——作用更强）"
    - "中国市场（正式制度不足——CIO 作为非正式制度）"
  ensemble: [中国上市公司 2009-2022、DesJardine 2023 引用（A Rising Tide——OrgSci 34(5) 印刷版年份）、2016 后 CIO 超 20%]
```

### resolution_logic

`arbitration` 仲裁（两假设实证裁决——coordinated governance 胜出）+ 三渠道 + 三条件化。

### five_acts

```yaml
five_acts:
  exposition: "Intro：CSR 脱钩被批评（'organized hypocrisy'——Cho et al.）→ 投资者层面治理空白 → CIO 上升（2016 后超 20%——'industry-wide normative effects'）→ 两竞争假设"
  rising_action: "协调治理 vs 合谋欺诈理论（同行负外部性 vs 组合价值最大化）+ 中国情境论证（正式制度不足 + CSR 披露弱）+ Methods（中国 2009-2022）"
  climax: "Results——裁决揭晓：CIO 显著降低 CSR 脱钩（'supporting the coordinated governance hypothesis'——协调治理胜出）"
  falling_action:
    - "三渠道（委派高管/威胁退出/减少控股股东自利——'delegating executives, threatening to exit, and reducing controlling shareholders' self-interest'）"
    - "三条件（非国企/CSR 密集/法律环境低效——作用更强——'compensate for the shortcomings of China's formal institutions'）"
    - "稳健性（系列检验——'main conclusion holds'）"
  denouement: "Discussion——共同所有权作为道德约束工具（'an ethics constraint tool rooted in market logic'——金融塑造新兴市场伦理规范）；
              投资者层面治理 CSR 脱钩（业务伦理视角的治理贡献）；中国情境的非正式制度（'informal institutional arrangement'）"
```

### stakes

```yaml
stakes:
  theoretical: "CSR 脱钩的投资者层面治理空白——'how to govern this phenomenon from the investor level is still lacking'"
  practical: "CSR 脱钩（greenwashing——'impression management'）；共同所有权的道德约束（中国新兴市场——正式制度不足）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 脱钩决定版——CSR 脱钩的决定因素（企业特征/治理——不接共同所有权）"
  - "讲法B: 合谋版——共同所有权合谋（collusive fraud——Azar et al. 反竞争——被证伪的一派）"
  - "讲法C: CSR 决定版——机构投资者驱动 CSR（Chen et al./Dyck——非共同所有权）"
  - "本文: 协调治理裁决版——CIO 降低脱钩（两假设实证裁决 + 三渠道 + 中国情境）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "中国情境（信息不对称/正式制度不足——'laws and regulations... have limited effectiveness'——制度具象）；无具名企业"
  rhetorical_question: "标题即问句（'Can Common Institutional Ownership Govern CSR Decoupling?'——标题问句家族第 9 例）"
  pacing_notes: "脱钩批评→治理空白→CIO 上升→两假设→裁决；climax=coordinated 胜出；falling action 三渠道+三条件+稳健性"
  showing_telling: "'coordinated governance' vs 'collusive fraud'（两假设命名——对称排布）；'organized hypocrisy'（组织伪善意象）；'A rising tide lifts all boats'（DesJardine 引用——行业传染意象）"
  voice: "JBE 实证口吻；'widely criticized'（批评共识）；'suitable research context'（情境论证）"
```

### cross_paper_notes

- **paradigms-at-war 七原型（两假设裁决）**：zhou/wowak2025/park2025/shen/bendig/haunschild2004/**csr_decoupling_china**——备注：与 haunschild2004（两既有文献阵营）的细微差别——本文是作者构建的竞争假设（扎根于治理正面派/反竞争派文献阵营）——同家族可辩护。
- **共同所有权家族七篇成型**：desjardine2022（CSR——overlooked）/anton2025（创新——overlooked）/denicolo2025（治理——half-domain）/desjardine2025（评级——neglected）/**csr_decoupling（CSR 治理——paradigms）/PMT（竞争——overlooked）/JPE（激励——neglected）**。
- **与 desjardine2022 的 CSR 对照**：desjardine（CSR 提升——涨潮）；csr_decoupling（CSR 脱钩减少——治理）——CSR 双视角（注意：JBE 引用 DesJardine 为 2023 印刷版——blueprint id 沿用 2022 在线版）。
- **标题问句家族第 9 例**。
- **判别器记录**：paradigms-at-war 判定基于两竞争假设（'We propose two competing hypotheses'——原文锚）实证裁决。
