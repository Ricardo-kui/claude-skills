# Story Blueprint — （2025, CAR）How Do Institutional Investors Facilitate Reporting Comparability?

## 文件头

```yaml
id: reporting_comparability
paper: "（2025, CAR — Contemporary Accounting Research）— How Do Institutional Investors Facilitate Reporting Comparability? Evidence from Common Institutional Ownership in the United States"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（共同所有权/07 原文）→ ROBUST
source_records: [parsed full text（共同所有权/07 原文）]
vault_reports:
  intro: null（共同所有权文件夹原文回读）
  methods_results: null（全文回读：美国 firm-pairs 1980-2016、DiD——金融机构并购）
  story_arc: null
corpus_links:
  write-introduction: "直接效应已做/溢出效应未知（'Little is known about the potential spillover effects'）+ CII 上升数据（17%→81%）——路径待验证"
```

## Story

### one_liner

> 共同机构投资者（CII）如何促进财务报告可比性（FRC）？既有研究只做直接效应——本文揭示**溢出效应**：共同所有权不仅提升直接持有企业的可比性，还通过共同公司连接传播到其他企业、甚至传染到无共同所有权企业——且溢出效应合计（11.79% SD）大于直接效应（9.67% SD）——机制：共同审计师 + 相似会计实务。

### knot

```yaml
knot:
  primary_type: half-domain-gap         # 第九原型：CII 效应的溢出半区（直接效应 done/溢出 not——'Little is known about the potential spillover effects'）
  compound_types: []                    # 两机制是结构，非子类型
  statement: "报告可比性研究——机构投资者对组合企业的直接效应已研究（Peng et al. 2023——'via a direct effect'）；溢出效应未知
              （'Little is known about the potential spillover effects of institutional ownership on other firms' reporting
              comparability'）——CII 直接提升持有企业 FRC + 两类溢出（共同公司连接/无共同所有权模仿）——
              溢出合计 11.79% SD > 直接 9.67% SD——机制：共同审计师 + 相似会计实务"
  tied_at:
    - "Intro：可比性基础属性（FASB）→ 直接效应已做（Peng et al.）→ 'Little is known about the potential spillover effects'（溢出空白）→ CII 上升（17%→81%——Lewellen & Lowry）"
    - "Theory：直接效应（股东提案/威胁退出——Edmans et al.）+ 两类溢出（连接传播/资本竞争模仿）"
  untied_at:
    - "Theory H1-H4：直接 + 两溢出 + 机制"
    - "Results：三类型 firm-pairs FRC 上升 + 溢出 > 直接 + 两机制"
  antagonist: "报告可比性研究的直接效应导向（'Prior literature focuses on how institutional investors facilitate the comparability of their portfolio firms'——溢出被忽略）"
  antagonist_built_by:
    - "直接效应已做/溢出未知声明（'Little is known about the potential spillover effects'）"
    - "CII 上升数据（S&P 500 17%（1990）→81%（2015）——Big 3 预测 2039 年 40% 投票权——规模叙事）"
    - "溢出 > 直接的量化（'combined spillover effects... larger than the direct effect'——11.79% vs 9.67%）"
```

### characters

```yaml
characters:
  protagonist: [common institutional ownership（X——CII）, financial reporting comparability（DV——FRC）]
  supporting:
    - "直接效应（股东提案/威胁退出——Edmans et al.——组合企业政策）"
    - "溢出效应 1（共同公司连接——'commonly owned by different institutional investors but are connected through common firms'——实务传播）"
    - "溢出效应 2（无共同所有权模仿——'mimic the accounting practices of their peers'——资本竞争/避免批评）"
    - "两机制（共同审计师 + 相似会计实务——'hiring of common auditors and their adoption of similar accounting practices'）"
  ensemble: [美国 firm-pairs 1980-2016、FRC（De Franco et al. 测量）、DiD（金融机构并购——He & Huang）、SEM 路径分析]
```

### resolution_logic

`exploration` 拓荒（补 CII 溢出半区——直接+两溢出效应地图 + 两机制 + DiD 因果识别）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：可比性基础属性（FASB——'basic property of financial reporting'）→ 直接效应已做（Peng et al.）→ 'Little is known about the potential spillover effects'（溢出空白）→ CII 上升（17%→81%——Big 3 预测 40% 投票权）"
  rising_action: "直接效应理论（股东提案/威胁退出）+ 两溢出理论（连接传播/资本竞争模仿）+ Methods（美国 firm-pairs 1980-2016、FRC 测量、DiD——金融机构并购）"
  climax: "Results——溢出揭晓：共同所有权提升三类型 firm-pairs 的 FRC（直接 + 两溢出——'the effect of common ownership goes beyond commonly owned firms'——溢出首揭）"
  falling_action:
    - "溢出 > 直接（'combined economic magnitude of the spillover effects is 11.79%... whereas... direct effect is 9.67%'——量化的反直觉）"
    - "两机制（共同审计师——Francis et al. 依据；相似会计实务——两步法验证 + SEM）"
    - "因果识别（金融机构并购外生冲击——'the increase in reporting comparability appears only after the mergers'——反向因果排除）"
  denouement: "Discussion——共同所有权溢出超越持有企业（'extends to non-commonly owned firms'）；
              可比性的行业传播（审计师/会计实务的扩散通道）；投资者信息处理成本的降低"
```

### stakes

```yaml
stakes:
  theoretical: "报告可比性的溢出效应未知——'Little is known about the potential spillover effects'——直接效应之外的行业传播"
  practical: "财务报告可比性（FASB 概念框架——投资者识别相似/差异）；审计师选择与会计实务的行业扩散"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 直接效应版——机构投资者提升组合企业可比性（Peng et al. 2023——既有研究）"
  - "讲法B: 可比性决定版——FRC 的决定因素（De Franco et al./Barth et al.——公司特征——不接共同所有权）"
  - "讲法C: 治理版——共同所有权治理效应（监督/退出——不接报告可比性）"
  - "本文: 溢出半区拓荒版——直接+两溢出（'Little is known about the spillover effects'——溢出 > 直接 + 两机制）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "Big 3（BlackRock/State Street/Vanguard——Bebchuk & Hirst 预测 40% 投票权——具名机构+规模叙事）；无具名企业（firm-pairs 样本）"
  rhetorical_question: "标题即问句（'How Do Institutional Investors Facilitate Reporting Comparability?'——标题问句家族第 10 例——'How' 型）"
  pacing_notes: "可比性基础属性→直接已做→溢出空白→CII 规模→三效应→机制；climax=溢出揭晓；falling action 量化比较+两机制+DiD"
  showing_telling: "'goes beyond commonly owned firms'（超越持有企业——传播意象）；'direct effect... spillover effects'（直接/溢出二元）；'imitate the accounting practices'（模仿意象）"
  voice: "CAR 会计实证口吻；'Little is known'（空白强调）；'plausibly exogenous shock'（识别谨慎）"
```

### cross_paper_notes

- **half-domain-gap 九原型（CII 溢出半区）**：malshe/wu/malik/mayo/lun/liu2016/denicolo2025/shi2021/**reporting_comparability**——直接效应 done/溢出 not（'Little is known'——原文锚）。
- **共同所有权家族九篇成型**（+reporting_comparability 可比性——half-domain 第四篇）。
- **与 desjardine2025 的信息对照**：desjardine（信息操纵——评级渗透——neglected）；reporting_comparability（信息传播——可比性——half-domain）——共同所有权的信息维度两故事。
- **标题问句家族第 10 例**。
- **判别器记录**：half-domain-gap 判定基于直接效应已做、溢出效应半区空白（'Little is known about the potential spillover effects'——原文锚）。
