# Story Blueprint — Vadakkepatt, Arora, Martin & Paharia (2022) JM

## 文件头

```yaml
id: vadakkepatt2022
paper: "Vadakkepatt, Arora, Martin & Paharia (2022, JM) — Shedding Light on the Dark Side of Firm Lobbying: A Customer Perspective"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（vault intro distill + 全文回读）→ ROBUST
source_records: [vault distill-introduction-exemplar, parsed full text]
vault_reports:
  intro: "narrative_analysis/mvp30/vadakkepatt2022_lobbying_customer_jm_distill-introduction-exemplar.md"
  methods_results: null（无 vault 报告——全文回读：ACSI 满意度 + 2SLS IV）
  story_arc: null
corpus_links:
  write-introduction: "03-data-shock Hook（130%/22,000% ROI/$325M→$338B）+ 01-despite-progress-unaddressed（'effects on customer outcomes remain largely unknown'）——路径待验证"
  write-methods: "ACSI + 2SLS（industry lobbying/lobbyist supply IV）+ 文本分析 10-K——路径待验证"
  write-results: "暗面揭晓（−8.37）+ 价值复现（+4.70）+ 中介抵消 + 4 调节——路径待验证"
```

## Story

### one_liner

> 游说被当作企业价值工具（18 项前期研究全是正向），但客户结果维度完全空白——实证发现：游说显著**降低**客户满意度（−8.37，顾客不知情也受损）——ABV 注意力权衡（有限注意力：游说 vs 客户关注的取舍）——"赚了监管、丢了客户"：企业价值收益被满意度损失部分抵消；CEO 营销背景/广告/R&D/产品市场游说可重新对齐注意力。

### knot

```yaml
knot:
  primary_type: overlooked-alternative  # 第六原型：游说文献做了一面（企业层面）、顾客面被看漏——dark side of lobbying 家族第二例
  compound_types: []                    # ABV 注意力权衡是机制，非子类型
  statement: "游说文献积累了大量企业价值正向结果（18 项前期研究——firm value/returns/contracts），客户结果维度完全空白——
              'effects on customer outcomes remain largely unknown'——监管俘获理论暗示但未检验——ABV 机制（有限注意力：
              游说 vs 客户关注的权衡）——实证：游说显著降低客户满意度（−8.37，独立于游说可见性）"
  tied_at:
    - "Intro P1-P2：Data-shock Hook（130% 增长/Ford-Cisco-Facebook-Delta/$325M→$338B/22,000% ROI）→ Gap（01-despite-progress-unaddressed——'no research in marketing directly examines this relationship'——Oracle 轶事）"
    - "Intro P3：ABV 透镜（有限注意力——游说 vs 客户关注权衡）"
  untied_at:
    - "Theory H1/H2：价值复现 + 满意度暗面"
    - "Results：H2 支持（α=−8.37, p<.01）+ H1 支持（+4.70）+ 中介 + 4 调节"
  antagonist: "游说文献的企业层面导向（18 项研究全做 firm value/returns/contracts——客户结果被看漏——跨学科壁垒）"
  antagonist_built_by:
    - "Table 1 文献表格（18 项前期研究——'all previous research focuses on firm-level outcomes'）"
    - "01-despite-progress-unaddressed 缺口句式（'Despite these arguments, the effects of firm lobbying on customer outcomes remain largely unknown'）"
    - "跨学科壁垒论证（游说研究在政治经济/财务——监管俘获理论不关注客户；营销未纳入游说）"
```

### characters

```yaml
characters:
  protagonist: [firm lobbying（X）, customer satisfaction（DV——ACSI）+ firm value（Tobin's q 双后果）]
  supporting:
    - "ABV 注意力权衡（机制——Ocasio 有限注意力——游说 vs 客户关注的取舍）"
    - "customer focus（中介——客户关注转移——文本分析 10-K 验证）"
    - "4 调节（CEO 营销背景 [80.61 vs 77.80]/广告 [80.01 vs 76.45]/R&D [79.73 vs 76.91]/产品市场游说 [76.46 vs 75.05]——注意力重新对齐）"
    - "customers（受害方——不知情也受损——'regardless of whether customers are aware of firm lobbying'）"
  ensemble: [ACSI 满意度 + 游说数据、2SLS（industry lobbying/lobbyist supply IV——Kleibergen-Paap/Hansen J）、10-K 文本分析、Oracle 轶事、音乐流媒体案例]
```

### resolution_logic

`revelation` 揭幕（揭幕游说的顾客面——ABV 注意力转移机制 + 4 调节解药——"赚了监管、丢了客户"的双刃）。

### five_acts

```yaml
five_acts:
  exposition: "Intro P1-P2：Data-shock Hook（130% 增长/Ford-Cisco-Facebook-Delta 案例/$325M→$338B/22,000% ROI）→ Gap（'effects on customer outcomes remain largely unknown'——Oracle 轶事——监管俘获暗示）"
  rising_action: "Intro P3-P6（ABV 透镜——有限注意力权衡——RO1-RO3 + 4 调节 + 中介预览）+ Methods（ACSI 满意度 + 游说数据 + 2SLS IV [industry lobbying/lobbyist supply]）"
  climax: "Results——H2 揭晓：游说显著降低客户满意度（α=−8.37, p<.01——独立于游说可见性控制 −.14, p<.05——顾客不知情也受损）——暗面首揭"
  falling_action:
    - "H1 复现（游说→Tobin's q +4.70, p<.01——企业价值正向——双刃的正面——18 项研究互证）"
    - "中介抵消（客户满意度负向中介游说→企业价值——'赚了监管、丢了客户'——价值收益被满意度损失部分抵消）"
    - "4 调节解药（CEO 营销背景/广告/R&D/产品市场游说——注意力重新对齐——model-free 分差显著）"
    - "文本分析验证（10-K 客户关注——机制在位）"
    - "内生性（2SLS——Kleibergen-Paap 相关 p<.00/Hansen J 有效 p>.10）"
  denouement: "Discussion——ABV 注意力权衡（'a firm's attention is even more constrained and limited than the expenditures
               it can dedicate to various initiatives'——Ocasio 1997）；披露强制（LDA——游说披露让顾客看到亲客户游说——
               音乐流媒体案例）；2018 股东决议（50 公司要求游说透明度）；'lobbying issues matter'（游说议题方向的重要性）"
```

### stakes

```yaml
stakes:
  theoretical: "游说文献 18 项研究全做企业层面——客户结果空白；监管俘获暗示但未检验；ABV 注意力权衡在营销的应用"
  practical: "数十亿美元游说损害客户满意度——'赚了监管、丢了客户'的双刃；披露强制（LDA）政策含义——2018 股东决议 50 公司"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 游说收益版——游说→企业价值（18 项前期研究——政治经济/财务主流——Table 1 文献现状）"
  - "讲法B: 监管俘获版——只做监管政策后果（政治科学视角——监管俘获理论——不接客户）"
  - "讲法C: 企业绩效版——只做游说→绩效/合同（政治经济主流——换 DV 不换视角）"
  - "本文: 顾客面揭幕版——游说→客户满意度负（ABV 注意力转移 + 4 调节解药——'赚了监管、丢了客户'）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "Ford/Cisco/Facebook/Delta（政府事务部门案例——具名企业四连）；Oracle 轶事（Gap 支撑）；音乐流媒体案例（亲客户游说的对照——Discussion）"
  rhetorical_question: "未见 pivot【已核实】——数据冲击型 Hook 用陈述句式"
  pacing_notes: "Data-shock→Gap→ABV 透镜→调节预览→发现预览；climax=H2 暗面揭晓（−8.37）；falling action 价值复现+中介抵消+4 调节+文本验证"
  showing_telling: "Data-shock 数字并置（130%/22,000%/$325M→$338B）；'Shedding Light on the Dark Side'（标题隐喻——照亮暗面）；model-free 分差（80.61 vs 77.80 等）"
  voice: "JM 营销实证口吻；'remain largely unknown'（缺口精确声明）；'regardless of whether customers are aware'（反直觉强调）"
```

### cross_paper_notes

- **dark side of lobbying 家族（overlooked-alternative 第六原型）**：singh2023（政治面——游说扭曲召回）↔ vadakkepatt2022（**顾客面——游说损害满意度**）——同 X 两个暗面；且共享 ABV 注意力基础观（singh 的 H3 媒体调节也用注意力基础观——理论同源）。
- **与 singh2023 的对照对（游说暗面双情境双 IV）**：singh（召回情境——IV：county 政治捐款）；vadakkepatt（满意度情境——IV：行业游说/说客供给）——同一现象的两种暗面揭幕。
- **overlooked-alternative 六原型**：desjardine2022/lashley2020/singh2023/zhao_ding2022/darby2026/**vadakkepatt2022**——"看漏一面"家族饱和。
- **ABV 透镜家族**：singh2023 + vadakkepatt2022（注意力基础观——Ocasio）——注意力权衡理论在游说研究的应用。
- **判别器记录**：overlooked-alternative 判定基于游说文献做了一面（企业层面）、顾客面被看漏——deductive 宣战（'no research in marketing directly examines this relationship'）。
