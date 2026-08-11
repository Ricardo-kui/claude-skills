# Story Blueprint — Wowak, Mannor & Wowak (2015) SMJ

## 文件头

```yaml
id: wowak2015
paper: "Wowak, Mannor & Wowak (2015, SMJ) — Throwing Caution to the Wind: The Effect of CEO Stock Option Pay on the Incidence of Product Safety Problems"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（全文回读——vault 无报告，OCR 导入原文在文献笔记库）→ ROBUST
source_records: [parsed full text（文献笔记库/论文导入——OvisOCR2 导入）]
vault_reports:
  intro: null（无 vault 报告——全文回读补实）
  methods_results: null（无 vault 报告——全文回读补实：GEE 双 DV、386 CEOs/1,314 CEO-years）
  story_arc: null
corpus_links:
  write-introduction: "'interesting paradox' 悖论标记 + big wins/big losses 不对称逻辑（Sanders & Hambrick）——路径待验证"
  write-methods: "GEE（binomial logit + negative binomial）双 DV + 两阶段残差内生性——路径待验证"
  write-results: "主效应反果 + tenure/founder 双调节（边际效应逐年分析）——路径待验证"
```

## Story

### one_liner

> 期权被当作 counterbalance CEO 风险厌恶的对齐工具（agency 共识），但存在"interesting paradox"：期权导致与预期相反的结果（盈余操纵、诉讼、big losses）——本文延伸：期权比例越高，产品安全问题越多（召回发生率 dy/dx=0.17, p<.01）——消费者成为 CEO "big wins" 追逐中的 "big losses" 承担者；且效应因人而异（任期 11 年后消失、创始人免疫）——J&J Weldon 的 70+ 召回是最好的注脚。

### knot

```yaml
knot:
  primary_type: irony-reversal          # 第六原型：反果形态第三例（治理机制反噬家族源头——wowak2015/darby2024/desjardine2023）
  compound_types: [neglected-arena, assumption-flip]   # 产品安全成因空白 + 激励统一效应假设挑战
  statement: "期权共识——stock options align CEO with shareholders（counterbalance 风险厌恶——Sanders & Hambrick big wins/big
              losses 不对称逻辑）；但'interesting paradox'——期权导致相反结果（盈余操纵/诉讼/不谨慎风险）——本文延伸：
              期权→缺乏谨慎→产品安全问题（消费者承担 big losses）——且效应因人而异（任期 11 年后消失/创始人免疫）"
  tied_at:
    - "Intro：agency 共识（期权=对齐）→ 'interesting paradox'（earnings manipulation/lawsuits——Harris & Bromiley/Peng & Roell）→ Sanders & Hambrick big wins/big losses"
    - "Theory：双认知过程（疏忽——无意识忽略；合理化——可接受风险）+ person-pay 交互（'counterpoint to the common assumption that incentives have relatively uniform effects'）"
  untied_at:
    - "Theory H1-H3：期权→安全问题 + tenure/founder 调节"
    - "Results：H1 支持（dy/dx=0.17, p<.01）+ H2/H3 支持（×tenure −1.01**、×founder −2.58**）"
  antagonist: "期权=利益对齐的 agency 共识（'asymmetric payoff from stock options encourages risk taking that is more careless and uncontrolled than that envisioned in the theoretical models justifying stock options'——Sanders & Hambrick）"
  antagonist_built_by:
    - "'interesting paradox'（悖论标记——先承认共识再翻转）"
    - "big wins/big losses 不对称逻辑（'option-loaded CEOs delivered more big losses than big gains'——Sanders & Hambrick 引语加持）"
    - "J&J Weldon 案例铺垫（Tylenol 1982 后安全声誉 → 2002 Weldon 56% 期权 → 70+ 召回）"
```

### characters

```yaml
characters:
  protagonist: [CEO stock option pay（X——总薪酬中期权比例）, product safety problems（DV——召回发生率 binary + 计数）]
  supporting:
    - "tenure（H2——任期保守倾向 dampen 期权效应：11 年后归零——'much to lose and little to gain' [Sanders 2001]）"
    - "founder status（H3——stewardship 动机免疫：非创始人 dy/dx=0.20, p<.01/创始人 −0.10 n.s.）"
    - "big wins/big losses 不对称逻辑（机制——Sanders & Hambrick 2007）"
    - "consumers（受害方——'big losses' 的承担者——NECC 60+ 死）"
  ensemble: [386 CEOs/1,314 CEO-years/FDA 受监管企业 2004-2011、GEE（binomial + negative binomial）、J&J Weldon（具名案例）、Tylenol 1982（对照案例）]
```

### resolution_logic

`revelation` 揭幕（揭幕期权的不谨慎面——big wins/big losses 不对称逻辑 + person-pay 条件化——激励的后果因人而异）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：agency 共识（期权=对齐——counterbalance 风险厌恶）→ 'interesting paradox'（盈余操纵/诉讼——与预期相反的结果）→ Sanders & Hambrick big wins/big losses → 本文延伸（产品安全——消费者承担 big losses——NECC 脑膜炎 60+ 死/700 病）"
  rising_action: "双认知过程（疏忽——无意识忽略 downside；合理化——可接受风险）+ person-pay 交互（tenure/founder——Wowak & Hambrick 2010 模型）+ Methods（386 CEOs/1,314 CEO-years/FDA 2004-2011/GEE 双 DV）"
  climax: "Results——H1 揭晓：期权比例→召回发生率（dy/dx=0.17, p<.01 binary；1.52, p<.01 count）——'Throwing Caution to the Wind'：期权的不谨慎面实证"
  falling_action:
    - "H2 tenure（期权×任期 −1.01**——效应逐年递减、11 年后归零——70% 观测在 11 年内——'much to lose and little to gain'）"
    - "H3 founder（期权×创始人 −2.58**——非创始人 dy/dx=0.20, p<.01/创始人 −0.10 n.s.——stewardship 免疫）"
    - "内生性（两阶段残差法——Wiersema & Zhang——结果一致）"
    - "双 DV 稳健（binary likelihood + count 双模型十列对位）"
  denouement: "Discussion——J&J Weldon 长篇叙事（Tylenol 1982 七死→安全声誉→2002 Weldon 56% 期权 [~1 SD 高于均值]→成本削减→26% vs 20% 利润率→'EZ Pass' 质检→70+ 召回 2007-2011→2012 下台——Fortune 引语：
               'It wasn't Do your job the right way, it was Do your job fast... Make it look good, and get it done as fast as possible'）
               + 贡献收口（超越股东的利益相关者后果 [Werder 2011]；人-酬交互 tandem；产品安全成因空白）"
```

### stakes

```yaml
stakes:
  theoretical: "期权后果研究只做股东财富——消费者福祉被忽略；产品安全成因空白（'sources of product safety problems have received little attention... for rare exceptions, see Haunschild and Rhee, 2004'）；激励统一效应假设未检验"
  practical: "不安全产品入市的生命威胁（NECC 60+ 死/700 病）；董事会期权设计的利益相关者后果（J&J 70+ 召回案例）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 期权对齐版——期权 counterbalance CEO 风险厌恶（agency 共识——治理文献主流）"
  - "讲法B: 股东后果版——期权→并购/盈余管理/诉讼（pay-wealth 文献主流——只做股东财富）"
  - "讲法C: 召回后果版——召回的市场反应/学习（recall 文献主流——Haunschild & Rhee 2004）"
  - "本文: 工具反果+利益相关者版——期权→产品安全问题（消费者承担 big losses + person-pay 条件化——'incentives are far from uniform across executives'）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "**J&J Weldon 长篇叙事**（Tylenol 1982 七死→安全声誉→2002 Weldon 56% 期权→26% vs 20% 利润率→'EZ Pass' 质检绰号→70+ 召回→2012 下台——Fortune 2010 引语——全文最长案例）+ NECC 脑膜炎（60+ 死/700 病——Hook）+ Tylenol 1982（对照）"
  rhetorical_question: "未见 pivot【已核实】——'interesting paradox' 陈述式悖论标记"
  pacing_notes: "共识→悖论→big wins/big losses→延伸→J&J 案例收口；climax=H1 揭晓（dy/dx=0.17）；falling action 双调节（边际效应逐年分析）+双 DV+内生性"
  showing_telling: "'Throwing Caution to the Wind'（标题隐喻——把谨慎抛向风中）；'big wins... big losses'（Sanders & Hambrick 不对称意象）；'EZ Pass system'（J&J 内部绰号——讽刺性细节——'Make it look good, and get it done as fast as possible'）"
  voice: "SMJ 实证口吻；'interesting paradox'（悖论标记）；'somewhat surprisingly in light of the societal implications'（意外性强调）"
```

### cross_paper_notes

- **irony-reversal 六原型（治理机制反噬家族三例——源头确认）**：wowak2015（**options→unsafety——2015 源头**）↔ darby2024（ownership→delay——延续，引 wowak2015 [66]）↔ desjardine2023（oversight→underground——平行）——治理机制反果三例，wowak2015 为家族源头。
- **recall 现象域九讲法**：3 后果/机制 + 6 前因（wowak2015 期权发生率 + darby 三篇 + eilert2017 + malik2025）。
- **Wowak 系同作者**：wowak2015（期权发生率——irony）↔ wowak2025（TMT 意识形态两极战——paradigms-at-war）——同 Wowak 不同故事；且 Kaitlin Wowak 连接 darby2025/2026（共同作者）——recall 家族合作网络：Wowak 2015 → darby 系 2023-2026。
- **与 malik2025 的期权暗面双视角**：malik（期权财富→IM 战术——行为层）；wowak2015（期权→产品安全——后果层）。
- **与 haunschild2015 的互引**：wowak2015 引 Haunschild & Rhee 2004（成因例外）——与库内 haunschild2015（NASA+制药混合方法）连接——成因研究的谱系。
- **判别器记录**：irony-reversal 判定基于治理工具反果（期权→不谨慎→产品安全——与 desjardine2023/darby2024 同族）。
