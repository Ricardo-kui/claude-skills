# Story Blueprint — Darby, Ketchen, Ball & Mukherjee (2023/2024) MSOM

## 文件头

```yaml
id: darby2024
paper: "Darby, Ketchen, Ball & Mukherjee (2023/2024, MSOM) — CEO Stock Ownership, Recall Timing, and Stock Market Penalties"   # ⚠️ vault 双年份标注（Darby_et_al_2023_MSOM 与 darby2024 同篇——parsed text Year: 2023，MSOM 2023 在线/2024 出版；id 沿用 darby2024）
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（vault 报告 + 全文回读）→ ROBUST
source_records: [vault narrative/methods_results 报告, parsed full text]
vault_reports:
  intro: "narrative_analysis/mvp30/darby2024_ceo_stock_ownership_recall_timing_narrative.md（⚠️ vault 另存 Darby_et_al_2023_MSOM_distilled_introduction.md——同篇）"
  methods_results: "narrative_analysis/methods_results/mvp30/methods/darby2024_ceo_stock_ownership_methods_narrative.md + results/... + deep_distillation/papers/... + fine_grained/batch_06_darby2024_toh2023/...（报告齐全）"
  story_arc: null
corpus_links:
  write-introduction: "Epigram 开场（起搏器故障）+ 'Contrary to popular belief' 反转句——路径待验证"
  write-methods: "复发事件 AFT + CEM（CEO 变更外生冲击）+ 访谈黑箱打开（三步决策过程）——路径待验证"
  write-results: "主效应反果 + severity 分样本 + 市场惩罚（CAR 四窗口）——路径待验证"
```

## Story

### one_liner

> 股权激励被当作对齐 CEO 与股东利益的治理工具（Jensen & Murphy 经典共识），但实证发现反果：CEO 持股越多召回越慢（+2% 持股 → 26 天延迟）——持股放大了延迟坏消息的动机（护股价/权力威严/个人财富三机制）——危险缺陷尤甚；而延迟本身被市场重罚（三周延迟惩罚近翻倍）——治理工具在召回情境中反噬。

### knot

```yaml
knot:
  primary_type: irony-reversal          # 第五原型：反果形态第二例（desjardine2023 同型——治理机制反噬）
  compound_types: [neglected-arena]     # timing 前因空白（三篇 CEO-recalls 文献但 'none of them examine recall timing'）
  statement: "股权激励共识——stock ownership aligns CEO with shareholders（Jensen & Murphy——对齐工具）；但实证反果：
              CEO 持股越多召回越慢（+2% → 26 天延迟）——持股放大延迟坏消息的动机（公司财务利益/CEO 权力/个人财富三机制），
              危险缺陷尤甚——治理工具在召回情境中反噬"
  tied_at:
    - "Intro：Epigram（起搏器电池/接线故障——知晓近两年才召回——15 伤 1 死）→ 'Contrary to popular belief——executives 决定召回时机'"
    - "Theory：三机制（Kothari 坏消息延迟——'withhold bad news and gamble that subsequent events will allow them to bury the bad news'）"
  untied_at:
    - "Theory H1/H2：持股→延迟 + severity 条件"
    - "Results：H1 支持（β=0.23, p<.01——26 天）+ H2 支持（高严重度 0.25, p<.01/低 n.s.）"
  antagonist: "股权激励=利益对齐的经典共识（Jensen & Murphy——把持股当解药）"
  antagonist_built_by:
    - "'Contrary to popular belief'（反转开场——executives 而非 regulators 决定召回时机）"
    - "三机制排布（公司财务利益/CEO 权力/个人财富——持股的三重暗面）"
    - "经典引用对照（Jensen & Murphy 1990 对齐共识 vs Kothari 坏消息延迟）"
```

### characters

```yaml
characters:
  protagonist: [CEO stock ownership（X）, time-to-recall（DV1——缺陷知晓到召回的天数）+ stock market penalty（DV2——CAR）]
  supporting:
    - "recall severity（H2/H4——高严重度 Class I/II vs 低 Class III——CEO 更深度介入高严重度）"
    - "三机制（公司财务利益——股价在脑海；CEO 权力——工程师不敢上报 [Boeing 737 Max 引例]；个人财富——自身损失规避）"
    - "三步决策过程（访谈黑箱打开：问题识别→管理团队建议→高管决定——Global VP Quality/FDA 副总监）"
    - "market（惩罚者——延迟被识别并重罚）"
  ensemble: [2,144 医疗设备召回/50 公司/2002-2015、复发事件 AFT、CEM（CEO 变更外生冲击）、LeMaitre/Boston Scientific/Teleflex/Allergan 具名案例]
```

### resolution_logic

`revelation` 揭幕（揭幕对齐工具的另一面——持股放大延迟的三机制——内部治理的暗面）+ 后果链（延迟→市场惩罚——完整因果链：持股→慢→罚）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：Epigram（起搏器故障——近两年才召回——15 伤 1 死）→ 'Contrary to popular belief——executives 决定召回时机' → 三篇 CEO-recalls 文献但 'none of them examine recall timing' → RQ"
  rising_action: "三步决策过程（访谈——黑箱打开）+ 三机制理论（Kothari 坏消息延迟）+ Methods（2,144 召回/50 公司/2002-2015/复发事件 AFT）"
  climax: "Results——H1 揭晓：CEO 持股越多召回越慢（β=0.23, p<.01——+2% 持股 → 26 天延迟）——对齐工具反果首揭"
  falling_action:
    - "H2 severity（高严重度 0.25, p<.01 显著/低严重度 n.s.——危险缺陷尤甚——'recall-slowing effects accentuated for high-severity'）"
    - "H3 市场惩罚（延迟→CAR 惩罚 −1.82% 至 −4.46%——三周延迟 [10→33 天] 惩罚 +82-124%——'waiting an extra three weeks nearly doubles the penalty'——效应随窗口消散 [−1,10] n.s.）"
    - "H4（高严重度 −1.94% 至 −4.51%/低 n.s.——市场同样只重罚危险缺陷的延迟）"
    - "机制验证（混合效应 within/between + 替代测量：equity comp 0.13/0.17、monetary ownership 0.17/0.15——三机制在位）"
    - "内生性（CEO 变更外生冲击 + 反向因果检验 + CEM + Cox/GLM）"
    - "post hoc 部分中介（持股→更长 TTR→更差市场回报——完整因果链）"
  denouement: "Discussion——董事会治理机制需求（'need for corporate governance mechanisms that mitigate the recall-slowing effects'）；
               FDA 识别 recalcitrant firms 的洞察——回到开头（起搏器患者的延长风险——'Fifteen injuries and one death'）"
```

### stakes

```yaml
stakes:
  theoretical: "recall timing 前因空白（三篇 CEO-recalls 文献均未做 timing）；股权激励=对齐的共识未考虑延迟坏消息的暗面"
  practical: "医疗设备患者的延长风险（15 伤 1 死案例）；董事会治理机制；FDA 监管资源分配"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 股权对齐版——持股让 CEO 与股东利益一致（Jensen & Murphy 经典——治理文献共识）"
  - "讲法B: 召回后果版——只做召回公告的市场反应（recall 文献主流——mixed findings）"
  - "讲法C: 召回概率版——只做召回发生/频率（Wowak 2015/Mayo 2022——timing 未做）"
  - "本文: 工具反果版——持股→延迟→重罚（对齐工具的反噬 + timing 前因 + 完整因果链）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "Epigram 起搏器案例（近两年延迟/15 伤 1 死）；LeMaitre Vascular 2013 移植片（Class I）、Boston Scientific ICD 电池（Class II）、Teleflex 2012 导管标签（Class III）、Allergan 2019 乳房植入物条码；Boeing 737 Max 工程师'afraid to speak up'（CEO 权力机制的引例）"
  rhetorical_question: "未见 pivot【已核实】——'Contrary to popular belief' 反转句作开场"
  pacing_notes: "Epigram→反转开场→前因缺口→三机制→双 DV（TTR + CAR）；climax=H1 反果揭晓（26 天）；falling action severity 条件+市场惩罚+机制+内生性+中介"
  showing_telling: "'Contrary to popular belief'（反转开场）；'withhold bad news and gamble that subsequent events will allow them to bury the bad news'（Kothari 引语——坏消息赌博意象）；'black box' 打开（访谈）"
  voice: "运营管理实证口吻；'Contrary to popular belief'（挑战常识）；'all too common'（现象普遍性）"
```

### cross_paper_notes

- **irony-reversal 五原型（反果形态第二例）**：darby2024（股权激励反噬——对齐工具→延迟）与 desjardine2023（监督反噬——oversight→underground）同构——**"治理机制反噬"家族**。
- **Darby 系同作者不同故事（最强批次——同现象三透镜）**：darby2024（内部激励反果）/ darby2025（外部威慑前提翻转）/ darby2026（外部治理面看漏）——治理光谱：内部工具/外部威慑/外部监督。
- **recall timing 前因家族 +1**：eilert2017（severity/品牌组织层面）↔ malik2025（期权财富 CEO 层面）↔ darby2024（持股治理层面）——前因侧第三视角。
- **与 eilert2017 的 delay→penalty 呼应**：eilert（汽车——晚召回市场惩罚更重）；darby2024（医疗设备——三周延迟惩罚翻倍）——跨行业同发现互证。
- **判别器记录**：irony-reversal 判定基于"治理工具产生与预期相反结果"（现象内反果——与 desjardine2023 同型）。
