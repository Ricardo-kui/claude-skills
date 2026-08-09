# Story Blueprint — Darby, Wowak, Ketchen & Connelly (2025) JSCM

## 文件头

```yaml
id: darby2025
paper: "Darby, Wowak, Ketchen & Connelly (2025, JSCM) — An Agency Theory Perspective on Activist Investors and Supply Chain Failures: The Case of Product Recalls"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（vault 报告 + 全文回读）→ ROBUST
source_records: [vault distill 报告（intro/methods/results fine）, parsed full text]
vault_reports:
  intro: "narrative_analysis/mvp30/darby2025_activist_investors_spillover_distill-introduction-exemplar.md"
  methods_results: "narrative_analysis/methods_results/mvp30/fine_grained/batch_2026-05-18/darby2025_activist_investors_recall_distilled_methods.md + batch_2026-05-20/darby2025_jscm_distilled_results.md"
  story_arc: null
corpus_links:
  write-introduction: "Vioxx 具名案例 Hook（88,000 心脏病/38,000 死）+ CEO 引语（'We track share ownership...'）——路径待验证"
  write-methods: "spillover 测量（activist 瞄准他企的持股）+ AFT + PSM——路径待验证"
  write-results: "威慑主效应（−23 天）+ defect type/severity 条件——路径待验证"
```

## Story

### one_liner

> 激进投资者通常被视为企业的威胁者/破坏者——但溢出效应反转了这个身份：当激进投资者瞄准**其他**企业时，本企业反而更快召回（−23 天）——威慑机制（"避免成为下一个目标"——快速召回=果断与消费者优先的信号）——activist 是隐性治理者，不是破坏者。

### knot

```yaml
knot:
  primary_type: assumption-flip         # 第五原型：activist=破坏者身份前提翻转成威慑者（spillover 家族与 paruchuri2020 对照）
  compound_types: []                    # 威慑机制是解法，非子类型
  statement: "激进投资者被默认视为企业的威胁者（activist 攻击/施压）；但 spillover 效应反转身份——activist 瞄准其他企业时，
              本企业更快召回（−23 天）——威慑机制（'避免成为下一个目标'）——activist 是隐性治理者而非破坏者"
  tied_at:
    - "Intro：Vioxx 案例（88,000 心脏病/38,000 死/2000-2004——Merck）→ 'what can encourage more timely recalls?' → 内部治理已做（女董事/CEO 持股）→ 外部监控缺口"
    - "Theory：agency theory + 威慑机制（CEO 引语：'We track share ownership... carefully watch their actions'）"
  untied_at:
    - "Theory H1-H3：activist 持股→更快 + defect type/severity 条件"
    - "Results：H1-H3 全支持（PSM：−23.10 天 ATE, p=.001）"
  antagonist: "activist=破坏者的默认身份（激进投资者的威胁叙事）"
  antagonist_built_by:
    - "Vioxx 死亡规模（38,000——召回延迟的代价具象化——'every day counts'）"
    - "CEO 引语（'We track share ownership and monitor both the owner and their share movement... carefully watch their actions'——实践中的威慑意识）"
    - "spillover 设计（activist 瞄准他企——本企业的反应——外部事件的内部效应）"
```

### characters

```yaml
characters:
  protagonist: [activist investor stock ownership（X——瞄准他企的 spillover）, time-to-recall（DV）]
  supporting:
    - "威慑机制（避免成为下一个目标——快速召回=果断信号 [Wowak 2021] + 消费者优先 [Hora 2011]）"
    - "defect type（H2——设计缺陷 spillover 更强：−0.26, p=.000）"
    - "defect severity（H3——高严重度 −0.06, p=.028 显著/低 n.s.）"
    - "executives（被威慑者——'carefully watch their actions'）"
  ensemble: [医疗设备召回、AFT + frailty/shared frailty、PSM（−23.10 天 ATE）、反向因果滞后检验]
```

### resolution_logic

`revelation` 揭幕（揭幕 activist 的隐性治理面——威慑者身份——外部监控的第二张脸）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：Vioxx（88,000 心脏病/38,000 死/2000-2004——Merck）→ 'what can encourage more timely recalls?' → 治理研究转向（女董事 [Wowak 2021]/CEO 持股 [Darby 2023]——内部治理）→ 外部监控缺口"
  rising_action: "agency theory + 威慑机制（CEO 引语）+ Methods（spillover 测量——activist 瞄准他企的持股、AFT、PSM）"
  climax: "Results——H1 揭晓：activist 持股（瞄准他企）→ 更快召回（PSM：−23.10 天 ATE, p=.001——'firms with activist investor ownership recall, on average, 23 days faster'）——破坏者变威慑者"
  falling_action:
    - "H2 defect type（设计缺陷 spillover 更强：−0.26, p=.000——设计缺陷更可见/更易成为 activist 目标）"
    - "H3 severity（高严重度 −0.06, p=.028 显著/低 n.s.——危险缺陷的威慑更有效）"
    - "稳健性（frailty/shared frailty 未观测异质性 + 反向因果滞后 [−0.05, p=.034] + 渐进控制向量）"
  denouement: "Discussion——外部监控的威慑价值：'every day counts'——time-to-recall 是供应链质量管理的'最重阶段'
               （Ni & Huang——'most important stage of the entire recall process'）；activist 的隐性治理面"
```

### stakes

```yaml
stakes:
  theoretical: "recall timing 前因只做内部治理——外部监控（activist spillover）被忽视；'every day counts' 的延迟代价"
  practical: "Vioxx 38,000 死的延迟代价；activist 威慑作为监管之外的加速机制"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: activist 威胁版——激进投资者攻击/施压企业（activist 文献主流——破坏者叙事）"
  - "讲法B: 内部治理版——女董事/CEO 持股对召回的影响（Darby 2023/Wowak 2021——内部因素）"
  - "讲法C: 召回特征版——缺陷特征对召回时机的影响（Hora 2011/Ni & Huang——召回本身属性）"
  - "本文: 威慑揭幕版——activist 瞄准他企→本企更快（spillover 威慑——外部监控的隐性治理面）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "Vioxx（88,000 心脏病发作/38,000 死亡/2000-2004——具名药物+死亡规模）；CEO 匿名引语（'We track share ownership... carefully watch their actions'——实践者声音）"
  rhetorical_question: "核心问句（'what can encourage more timely recalls?'——实践性 RQ——非修辞 pivot）"
  pacing_notes: "Vioxx 死亡规模开场→内部治理已做→外部缺口→威慑机制→spillover 设计；climax=PSM −23 天揭晓；falling action 两条件+三稳健性"
  showing_telling: "'every day counts'（时间紧迫意象）；'most important stage of the entire recall process'（引语加持）；CEO 引语（实践者权威）"
  voice: "供应链管理实证口吻；'life-or-death consequences'（生死措辞）；'all too common'（普遍性）"
```

### cross_paper_notes

- **assumption-flip 五原型（外部治理者身份前提翻转家族）**：paruchuri2020（负面事件→正面溢出——valence）↔ shipilov2020（负面偏好）↔ hahl2017（distinction 动机）↔ lovelace2021（浪漫领导力）↔ **darby2025（activist 破坏者→威慑者——spillover 家族与 paruchuri2020 对照：paruchuri 是危机本身的溢出、darby2025 是 activist 行动的溢出）**。
- **Darby 系同作者不同故事（治理光谱）**：darby2024（内部激励反果——irony）/ darby2025（外部威慑——assumption-flip）/ darby2026（外部监督——overlooked-alternative）——同一现象三个治理透镜。
- **recall 现象域八讲法**：3 后果/机制（wowak2025/desjardine2023/singh2023）+ 5 前因（eilert2017 组织/malik2025 CEO 激励/darby2024 持股治理/darby2025 外部威慑/darby2026 外部监督）。
- **判别器记录**：assumption-flip 判定基于 actor 身份前提翻转（activist=破坏者→威慑者）——spillover 家族。
