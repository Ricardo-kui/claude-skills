# Story Blueprint — Pfarrer, Pollock & Rindova (2010) AMJ

## 文件头

```yaml
id: pfarrer2010
paper: "Pfarrer, Pollock & Rindova (2010, AMJ) — A Tale of Two Assets: The Effects of Firm Reputation and Celebrity on Earnings Surprises and Investors' Reactions"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 全文补实（文献笔记库论文导入）→ ROBUST
source_records: [project_mvp30_pfarrer2010_intro, project_mvp30_pfarrer2010_methods,
                 theory fine report (vault), 全文（文献笔记库）]
vault_reports:
  intro: "narrative_analysis/introduction/mvp30/fine_grained/batch_2026-05-24/pfarrer2010_amj_distilled_introduction.md + mvp30/pfarrer2010_tale_of_two_assets_distill-introduction-exemplar.md"
  theory: "narrative_analysis/theory/mvp30/fine_grained/batch_2026-07-09/han_tale_of_two_assets_distilled_theory.md（⚠️ 注册键误标 han_pollock_paruchuri_smj，内容实为本文）"
  methods_results: "narrative_analysis/methods_results/mvp30/fine_grained/batch_2026-05-18/pfarrer_2010_amj.md（仅 Methods）+ **全文：文献笔记库/01 导入/论文导入/Pfarrer, Pollock, and Rindova 2010.md**（2026-08-09 Results/Discussion 回读补实——此前 `_parsed_texts/` 穷尽检索无此文，实际存于文献笔记库）"
  story_arc: null
corpus_links:
  write-introduction: "corpus/tensions/05-construct-confusion.md 变体A（双层构念混淆，来源）+ 变体C（操作化错配，adapted）；无 Hook 冷启动（与 gamache2020 同型）"
  write-theory: "pattern 候选（construct_differentiation_dual_lens / formation_mechanism_contrast / positive_negative_boundary_embedded）——theory 报告建议入库，路径待验证"
  write-methods: "corpus/事件历史+事件研究.md 变体5（事件窗口+市场模型+EVENTUS 声明，待交叉）；memory 记录：sample-justification 模板H/I、model-selection 模板G、endogeneity-defense 模板F（路径待验证）"
  write-results: null
```

## Story

### one_liner

> 文献把 reputation 与 celebrity 当作可互换的社会认可资产，本文证明它们由相反的行为过程形成（稳定价值创造 vs 戏剧化叙事）、产生相反的盈余意外倾向，并以两种社会认知框架（理性 vs 情感）塑造投资者对同一意外的相反反应——解开纠缠，才能解释为什么同样的"名气"既是缓冲也是放大器。

### knot

```yaml
knot:
  primary_type: tangled-constructs   # reputation 家族第三原型（pollock2015/han2024/pfarrer2010）
  compound_types: []                 # 2×2 对比矩阵是布局而非子类型，纯型
  statement: "社会认可资产文献把 reputation 与 celebrity 混为一谈（同一指标测不同构念、不同标签指同一现象），但两者由相反过程形成并产生相反效应——reputation 基于稳定价值创造（理性框架），celebrity 基于戏剧化叙事（情感框架）"
  tied_at:
    - "Intro P2：双层构念混淆 Tension（general/specific 分析层次 + labels/proxies 操作化）"
    - "Theory T1：双构念并行定义 + 区分澄清（rational vs emotional sociocognitive content）"
  untied_at:
    - "Theory H1-H4：相反预测对位（H1a/b reputation 抑制正意外/促进负意外；H2a/b celebrity 双增；H3a-3c/H4a-4c 反应对比）"
    - "Results Table 2/3（H1a 0.48 支持 + H2a 1.60 支持——同一 DV 镜像方向）+ Table 4/5（H3a-c 全支持 + H4a/b 支持——CAR 跨资产对比）"
  antagonist: "文献的构念混淆——社会认可资产研究的标签/代理混用（非某个理论派别，而是领域整体的操作化混乱）"
  antagonist_built_by:
    - "双层混淆排布（general/specific 分析层次 + labels/proxies 操作化）"
    - "引用内部批评（Deephouse & Carter 2005 等）证明非稻草人"
    - "'fragmented body of work' + 'limiting the development of theory' 上升论证"
```

### characters

```yaml
characters:
  protagonist: [reputation（理性/分析框架）, celebrity（情感/联想框架）]
  supporting:
    - "earnings surprises（DV——正负偏差构成检验两种框架的天然舞台）"
    - "investors（反应者——用两种框架解读意外）"
    - "media（celebrity 的制造者——戏剧化叙事的源头）"
    - "analysts' consensus estimates（期望基准——意外的参照系）"
  ensemble: [无形资产文献、战略/组织研究、心理学信息加工文献]
```

### resolution_logic

`revelation` 揭幕（解结版）——不否定两类资产的价值，而是展示被混用的同一标签下是两张不同的脸（理性 vs 情感、稳定 vs 戏剧），按形成机制 + 信息加工拆开再对位预测。研究者是拆线人：knot 不是"谁对谁错"，而是"一个词指了两样东西"。

### five_acts

```yaml
five_acts:
  exposition: "Intro P1-P2：无形资产→social approval assets 聚焦，领域共识建立后立即转入双层构念混淆 Tension（无 Hook 冷启动——直接进入文献共同语言）"
  rising_action: "Intro P3-P6（双构念定义 + 双理论来源分工 + DV 正负不对称的方法论辩护）+ Theory（形成机制对比→H1/H2 相反倾向；信息加工机制→H3/H4 差异化反应）+ Methods（1:3 SIC 匹配样本、理想型二分、RE logit + 事件研究 CAR 双 DV 架构）"
  climax: "Results 'Effects of Reputation and Celebrity on the Likelihood of Surprises'（Table 2/3）——H1a 支持（odds 0.48, p<.01：高声誉抑制正意外）+ H2a 支持（odds 1.60, p<.05：名企放大正意外）——同一 DV 上两资产镜像方向，构念区分首次实证兑现"
  falling_action:
    - "H1b/H2b 双 null（负面意外倾向不受两资产影响——2×2 第一阶段的非对称，诚实报告）"
    - "H3a-c 全支持（Table 4 正意外 CAR：reputation 2.30% vs none 1.74% [0.56%, p<.05]；celebrity 3.32% vs 1.74% [1.58%, p<.001]；celebrity>reputation [-1.02%, p<.05]——情感框架放大好事收益）"
    - "H4a/b 支持 + H4c null（Table 5 负意外 CAR：双双缓冲 0.42%/0.36% vs none -0.59% [1.01%/0.95%]，资产间无差——'好事差、坏事无差'的镜像不对称）"
    - "稳健性：GEE 回归（reputation b=2.74, celebrity b=2.44, p<.05——正意外直接关系）+ Heckman（Bascle 标准：第一段显著、选择修正不显著→内生性无碍）+ 替代市场代理/窗口/样本排除（footnote：结果不变）"
  denouement: "Discussion——回到开头：'making clear distinctions in terms of the intangible assets studied may be critical for reconciling contradictory findings'（构念纠缠的解开=文献矛盾调和钥匙——buffering vs double-edged sword 对照，Rhee & Haunschild 产品 vs 企业声誉对比）+ visibility-only/affect-only 分解检验（celebrity 3.32% > 组件之和 1.38%/2.09%——整体大于部件）+ 打破 'no such thing as bad publicity' 俗语（showing 收口）+ 'bold versus steady' 管理启示（社会认可资产无产权、易被管理者忽视）"
```

### stakes

```yaml
stakes:
  theoretical: "构念混淆使社会认可资产文献碎片化——无法解释和预测不同资产的不同效应（原文：'limiting the development of theory'）；Discussion 升级：区分不清也是文献结论矛盾的根源（buffering vs double-edged sword 之争）"
  practical: "管理者忽视无产权依傍的社会认可资产——'bold versus steady' 战略风格会固化不同的集体诠释框架且后果比预想持久；打破'没有坏名声宣传'迷思——无认可无情感共振的纯 visibility 可能无益（Discussion 原文）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 单构念深化版——只做 celebrity 对市场反应的影响（领域现状即如此：reputation 文献、celebrity 文献各自为政）"
  - "讲法B: 构念辨析 essay 版——纯概念区分不做实证（缺'相反效应'的实证冲击力）"
  - "讲法C: 单情境版——只做负面意外的投资者反应（'坏消息'更具新闻性；但丢失正负不对称这一天然检验场）"
  - "本文: 双构念对比实证（2×2 矩阵）——只有并置检验才能证明'不是同一资产'；DV 正负不对称性为两种框架提供天然对照实验场（P5 方法论辩护原文）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "密度低——全文无具名企业案例【已核实】（theory 报告：'H3/H4 心理机制后缺少具体市场案例'；intro 无轶事开场）；Discussion 用 'bold versus steady' 战略风格意象让抽象资产可感"
  rhetorical_question: "未见【已核实】——冷启动 intro P1-P6 无问句 pivot"
  pacing_notes: "冷启动直接进文献共识（六段式均匀推进，无钩子蓄积）；Theory 2×2 对位排列（H1a/b↔H2a/b、H3a-3c↔H4a-4c）制造矩阵节奏；climax=Table 2/3 镜像方向并置（0.48 vs 1.60）；falling action 先双 null 后三组 CAR 对比再稳健性——'支持-空-反转'的非对称节奏"
  showing_telling: "斜体构念+破折号并置（reputation—celebrity）定义；'social facts' 概念隐喻；正负不对称三段对比（Both types.../Further, negative.../Positive..., on the other hand...）；Discussion 打破 'no such thing as bad publicity' 俗语收口；分解检验（celebrity > 组件之和）作实证版 '整体大于部分'"
  voice: "主动语态高（~80%：We suggest/argue/hypothesize）；'we begin to address these questions' 谦逊策略语气；'first that we are aware of' 精确例外式贡献声明（Discussion）"
```

### cross_paper_notes

- **reputation 家族最强对照对（同构念对不同拆法）**：pfarrer2010（形成机制端+正负边界——tangled-constructs 第三原型，reputation↔celebrity 原始拆解）↔ han2024（后果端 2×2 对角交叉，scandalization DV）↔ pollock2015（status↔reputation 动态共演）↔ paruchuri2020（负事件→正溢出效价翻转）——同一 reputation 概念空间四种故事：解开、区分、共演、翻转。
- **无 Hook 冷启动家族双原型达成**：gamache2020 ↔ pfarrer2010——冷启动=假设读者是领域专家，直接进入文献共识（无轶事/数据/引语开场）。
- **tangled-constructs 类型表更新**：`_schema.md` 原型状态同步为三原型（pollock2015/han2024/pfarrer2010）。
- **与 section 级互证**：05-construct-confusion 变体A/B（双层构念混淆/构念纠缠）与 story 级 tangled-constructs 互相印证；PFarrer 2010 即变体A 来源。
