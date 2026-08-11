# Story Blueprint — Darby, Wowak, Ketchen & Connelly (2026) JOM

## 文件头

```yaml
id: darby2026
paper: "Darby, Wowak, Ketchen & Connelly (2026, JOM) — Toward Faster Recalls of Dangerous Medical Devices: Does Ownership by Large Institutional Investors Matter?"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（vault 报告 + 全文回读）→ ROBUST
source_records: [vault distill 报告（intro/theory/methods/results fine）, parsed full text]
vault_reports:
  intro: "narrative_analysis/mvp30/darby2026_large_institutional_ownership_recall_distill-introduction-exemplar.md"
  theory: "narrative_analysis/theory/mvp30/fine_grained/batch_2026-07-09/darby2026_large_institutional_ownership_distilled_theory.md"
  methods_results: "narrative_analysis/methods_results/mvp30/fine_grained/batch_2026-05-18/darby2026_faster_recalls_large_institutional_ownership_distilled_methods.md + batch_2026-05-20/darby2026_jom_distilled_results.md"
  story_arc: null
corpus_links:
  write-introduction: "Epigraph 开场（Philips 呼吸机——十多年才召回）+ 'Big Four' 概念引入（BlackRock/Vanguard/Fidelity/State Street——$32 万亿）——路径待验证"
  write-theory: "agency monitoring + 信息不对称双调节（R&D 强度/设备等级）——路径待验证"
  write-methods: "AFT + CEM + 19 项稳健性——路径待验证"
```

## Story

### one_liner

> 管理者、政策制定者与监管者普遍警惕大型机构投资者的影响力——但研究发现被警惕者反而是安全的推动者：Big Four（BlackRock/Vanguard/Fidelity/State Street——$32 万亿）持股越多，危险医疗器械召回越快（1% 持股 → 24 天加速）——watchdog 角色；但信息不对称（高 R&D/高风险设备）削弱监督——外部治理面是召回文献看漏的替代视角。

### knot

```yaml
knot:
  primary_type: overlooked-alternative  # 第五原型：外部治理面被看漏（'research has largely been limited to internal governance factors'）
  compound_types: []                    # 信息不对称边界是条件化，非子类型
  statement: "recall timing 治理研究'largely been limited to internal governance factors'（女董事/CEO 持股）；外部治理面被看漏——
              Big Four 大型机构投资者的 watchdog 角色：持股越多召回越快（1% → 24 天加速）——被警惕者反而是保护者；
              信息不对称（高 R&D/高风险设备）削弱监督"
  tied_at:
    - "Intro：Epigraph（Philips 呼吸机——'more than a decade' 才召回——Trang 2022 引语）→ 内部治理局限（明示缺口）→ Big Four 引入（$32 万亿——'Big Four' 俗称）→ RQ"
    - "Theory：agency monitoring（大股东=监督者）+ 信息不对称双调节（R&D 强度/设备等级——moral hazard 放大）"
  untied_at:
    - "Theory H1/H2a/H2b：大机构持股→更快 + 两调节削弱"
    - "Results：H1 支持（1% → 24 天加速）+ H2a/H2b 支持"
  antagonist: "recall 治理研究的内部导向（'largely been limited to internal governance factors'——外部视角被看漏）"
  antagonist_built_by:
    - "明示缺口（'This is a notable shortcoming because... external governance factors might influence OSCM phenomena'）"
    - "Big Four 规模具象（'$32 trillion by the end of 2024'——'Big Four' 俗称 + Strine 2020）"
    - "被警惕者叙事（'managers, policymakers, and regulators may be wary of the influence that large institutional investors have'——实践 vs 发现的落差）"
```

### characters

```yaml
characters:
  protagonist: [large institutional investor ownership（X——Big Four）, time-to-recall（DV）]
  supporting:
    - "watchdog 角色（agency monitoring——'boundedly rational actors, executives should attend to the demands of such influential shareholders'）"
    - "R&D intensity（H2a——信息不对称削弱：executives 有语境、外部观察者没有 [Aboody & Lev 噪声]）"
    - "device class（H2b——高风险 Class III 削弱：'high degree of task-specific knowledge'）"
    - "FDA/regulators（实践端——'limited monitoring resources' 的分配）"
  ensemble: [2,932 严重缺陷召回/69 公司/2002-2020、AFT + CEM、19 项稳健性、Philips 呼吸机（Epigraph）]
```

### resolution_logic

`revelation` 揭幕（揭幕外部治理面——watchdog 的第二张脸——被警惕者=保护者）+ 信息不对称条件化（监督何时失效）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：Epigraph（Philips 呼吸机——'more than a decade'——Trang 2022）→ 内部治理局限（明示缺口）→ Big Four 引入（$32 万亿——BlackRock/Vanguard/Fidelity/State Street）→ RQ（大机构持股 → time-to-recall?）"
  rising_action: "agency monitoring 理论 + 信息不对称双调节（R&D 强度/设备等级——moral hazard）+ Methods（2,932 严重缺陷召回/69 公司/2002-2020/AFT + CEM）"
  climax: "Results——H1 揭晓：大机构持股 → 更快召回（1% 持股 → 24 天加速）——被警惕者反而是保护者（watchdog 首揭）"
  falling_action:
    - "H2a R&D 强度削弱（信息不对称——executives 有语境、外部观察者没有——监督失灵）"
    - "H2b 高风险 Class III 设备削弱（任务特异性知识——'high degree of task-specific knowledge'——监督失灵）"
    - "19 项稳健性（CEM 替代匹配向量/PSM/frailty/shared frailty/边际风险集/安慰剂/面板 FE 反向因果/替代所有权测量/VIF/winsorize/Cox/线性）"
    - "机制附加（所有权规模/投资视野替代测量 + 非线性探索）"
  denouement: "Discussion——'previously unidentified benefit'（被警惕的势力=更快的召回——管理者/监管者的警惕转向理解）；
               FDA 资源分配洞察（识别快/慢召回者）；外部治理与内部治理的互补"
```

### stakes

```yaml
stakes:
  theoretical: "recall 治理研究内部导向——外部治理面（机构投资者）被看漏；agency monitoring 在 OSCM 现象中的应用"
  practical: "危险医疗器械的召回延迟（Philips 十年案例）；FDA 有限监管资源的分配；管理者对大机构的警惕重新校准"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 内部治理版——女董事/CEO 持股对召回的影响（Wowak 2021/Darby 2023——recall 治理研究现状）"
  - "讲法B: 机构威胁版——大机构投资者的负面影响（finance 文献——代理冲突/短视主义）"
  - "讲法C: 召回特征版——缺陷特征/严重度对时机的影响（Hora/Ni & Huang——召回属性）"
  - "本文: 外部治理面揭幕版——Big Four watchdog（被警惕者=保护者 + 信息不对称条件化）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "Philips 呼吸机 Epigraph（'more than a decade'——具名产品+Trang 2022 引语）；Big Four 具名（BlackRock/Vanguard/Fidelity/State Street——$32 万亿规模感）"
  rhetorical_question: "RQ 问句（'is ownership by large institutional investors associated with a firm's time-to-recall?'——研究问句非修辞 pivot）"
  pacing_notes: "Epigraph→内部局限→Big Four 规模→双 RQ；climax=H1 揭晓（24 天加速）；falling action 双调节+19 项稳健性（最重的稳健性包）"
  showing_telling: "'Big Four' 俗称（规模隐喻——$32 万亿）；'watchdog'（看门狗隐喻）；Philips 十年（时间尺度具象）；'previously unidentified benefit'（贡献定位）"
  voice: "JOM 实证口吻；'managers, policymakers, and regulators may be wary'（实践警惕的承认——再翻转）；'every day counts' 家族呼应"
```

### cross_paper_notes

- **overlooked-alternative 五原型（"看漏一面"家族）**：desjardine2022（理论宣战）/ lashley2020（数据长出）/ singh2023（丑闻+识别）/ zhao_ding2022（换镜头）/ **darby2026（外部治理面——deductive 宣战——'largely been limited to internal governance factors'）**。
- **Darby 系同作者不同故事（治理光谱完整）**：darby2024（内部激励反果——irony-reversal）/ darby2025（外部威慑——assumption-flip）/ darby2026（外部监督——overlooked-alternative）——内部工具反噬 vs 外部威慑 vs 外部监督——同一现象（recall timing 医疗设备）三故事。
- **与 darby2025 的对照**：darby2025 威慑（activist 在别家——溢出）；darby2026 监督（Big Four 在本家——watchdog）——外部治理的两条路径（威慑 vs 监督）。
- **与 desjardine2022 的共同所有权对照**：desjardine2022（common ownership → CSR——组合视角）；darby2026（institutional ownership → 召回加速——监督视角）——同一所有权透镜两个故事。
- **recall 现象域八讲法**（3 后果/机制 + 5 前因——darby 三篇占前因侧三席）。
- **判别器记录**：overlooked-alternative 判定基于外部治理面被看漏（明示缺口——deductive 宣战）。
