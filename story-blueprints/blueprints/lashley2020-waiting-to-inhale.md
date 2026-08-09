# Story Blueprint — Lashley & Pollock (2020) ASQ（首份定性 blueprint，ROBUST）

## 文件头

```yaml
id: lashley2020
paper: "Lashley & Pollock (2020, ASQ) — Waiting to Inhale: Reducing Stigma in the Medical Cannabis Industry"
paper_type: qualitative        # 纯定性归纳过程研究（grounded theory + process analysis）——五幕按 Pollock Fig 2.3 定性 overlay
distilled_sections: [intro, theory, methods, results]      # 2026-08-09 vault 检索确认四区段报告齐全 → ROBUST（theory 融入 Findings/Discussion，无独立 Theory 段）
source_records: [project_mvp30_lashley_pollock2020_methods_results, project_mvp30_lashley_pollock2020_intro（vault 报告重建）]
vault_reports:
  intro: "narrative_analysis/introduction/mvp30/fine_grained/batch_2026-05-24/lashley_pollock2020_asq_distilled_introduction.md"
  theory: "narrative_analysis/theory/mvp30/fine_grained/batch_2026-07-09/lashley2020_waiting_to_inhale_distilled_theory.md"
  methods_results: "narrative_analysis/methods_results/mvp30/fine_grained/batch_13_lashley_pollock2020/lashley_pollock2020_waiting_to_inhale_fine_methods_results.md；deep_distillation/papers/lashley_pollock2020_waiting_to_inhale_methods_results_deep_profile.md"
  story_arc: null
corpus_links:
  write-introduction: "hooks/10-immersive-narrative 变体B（沉浸式叙事 Hook：'Imagine...' 六约束排比——本 blueprint 即该变体原文来源）；三层递进 Literature Turn；contributions 'remove as opposed to manage' 定位"
  write-theory: "质性过程理论型（Findings+Discussion 承载理论：T1 嵌入叙事 / T4 隐性命题 / 无 T6 独立段）"
  write-methods: "定性过程研究（Q1-Q8：方法正当化/极端情境/多源数据角色/编码进阶/可信性机制）"
  write-results: "定性过程研究（F1-F6：Process-Model Overview / Front-Stage-Backstage Contrast / Side-Stage Negotiation / Audience-Specific Success）"
```

## Story

### one_liner

> 一个合法却仍被污名的行业（医用大麻）里，企业不是"管理"污名，而是在"去除"污名——先从道德议程出发，再树立道德原型，最后注入道德性；前台讲着体面的话，后台做着活下去的事（甚至违规），侧台与人谈判出共识。三个舞台并置，等来的不是法律放行，而是被当作正当行业"吸进去"。

### knot

```yaml
knot:
  primary_type: overlooked-alternative   # 双原型（desjardine2022 deductive 宣战 + lashley2020 inductive 长出）
  compound_types: []   # 内层 Incompleteness：stigma 文献做的是 manage，remove 路径无人做
  statement: "组织如何应对污名？stigma 文献讲'管理污名'（应对策略），但这些企业实际上在'去除污名'（把行业变成可接纳的正当存在）——'remove as opposed to manage'；且核心污名（core stigma）与组织身份紧密耦合、无法通过解耦消除，单企业 tactics 不足以降低整个类别的污名"
  tied_at:
    - "Intro P2：core stigma 定义 + 'exiting the category is often not an option'（约束不可逃避）+ 'by themselves' 铺垫集体行动必要——显式研究问题收段"
    - "Intro P3-P4：三层递进 Literature Turn（org-level coping → category-level tactics → process gap），Tension 嵌入"
    - "Findings：core stigma 与身份耦合的张力在过程模型开头再次系紧"
  untied_at:
    - "Findings：三阶段过程模型（moral agenda → moral prototyping → morality infusion）——'去除'路径从数据中长出来"
    - "Discussion：P1-P3 隐性命题归纳（三阶段顺序+触发外生转内生 / 关系空间分离 / 符号先于物质的反向顺序）"
  antagonist: "stigma 文献的管理范式（'企业只能应对污名'的隐含前提）+ [记录在案] backstage survival violations（backstage 生存违规——theory 报告明示'作为反派制造张力'）：企业为了活下去在后台做的违规行为（依赖黑市/未合规做法）与前台道德形象互斥，反派在组织内部"
  antagonist_built_by:
    - "三层递进 Literature Turn：先铺满'管理污名'文献（org-level coping：shielding/straddling/co-opting），再露 category-level tactics 少数尝试，最后收窄到 process gap——共识惯例立起来再拆"
    - "合法-污名并存的极端情境（medical cannabis：法律允许 + 社会排斥）：情境本身让'管理 vs 去除'的对立可见"
    - "backstage 违规的张力设定：道德前台 vs 生存后台的冲突贯穿始终（theory 报告 Plot Emergence 确认）"
```

### characters

```yaml
characters:
  protagonist: [category-level core stigma reduction process（过程，Y——定性论文的主角是过程/模型而非单一构念）]
  supporting:
    - "moral agenda / moral prototyping / morality infusion（三阶段机制链，各阶段都有前台/后台/侧台三个关系空间）"
    - "front-stage 公开道德形象 vs backstage 生存行为（两套行为体系的对立，反派载体）"
    - "side-stage 部分可见冲突 → 规范澄清（第三个关系空间，P2 命题核心）"
  ensemble: [多源数据（observations/interviews/archives 各捕获一角色）、Colorado/Oregon/Washington 情境、行业受众（按受众分别评估成功）、州与联邦政府（Success 评估的对手方）]
```

### resolution_logic

`revelation` 揭幕（定性版）——**把后台露出来 + 关系空间分离**：front-stage/backstage/side-stage 并置 = 展示被公开话语遮蔽的背面；P2 命题（关系空间分离使集体去污名目标与个体生存行为共存）把"矛盾"转成"分工"。研究者是"拉开舞台幕布"的人，且从数据里长出来（inductive）。另：P3 命题（符号/叙事先于物质变化的反向顺序）是 category emergence 透镜的兑现。

### five_acts（Pollock Fig 2.3 定性 overlay）

```yaml
five_acts:
  exposition: "Intro（5 段 ~750 词）：P1 沉浸式叙事 Hook（'Imagine starting a business when... banks will not let you open a checking account...' 六约束排比：制度→金融→运营→社会→市场，10-immersive-narrative 变体B 原文来源）；P2 core stigma 定义 + 'exiting the category is often not an option' + 显式 RQ；P3-P4 三层递进 Literature Turn（org coping → category tactics → process gap）+ Stakes 嵌入（failure consequence chain：stigma 阻碍增长 → 不理解过程导致无效努力）；P5 Theory Lens（category emergence）+ Preview（定性方法+数据类型）+ Contribution（remove as opposed to manage）"
  rising_action: "定性版 rising = 方法可信性蓄积 + knot 保持系紧：Data Collection（CO/OR/WA 三州因有运营中 dispensary 而入选）；Direct observations（行业会议 + dispensary 参观）；Interview data（会前访谈失败 → 会议提供机会，先失败后成功的田野叙事）；Archival（与田野并行）；Data Analysis（grounded theory + process analysis 双方法）；Establishing Trustworthiness（triangulation/prolonged engagement/peer debriefing）——注意：质性论文的 Methods 同时承担 rising action 与 arena 搭建"
  climax: "Findings 开头——Process-Model Overview（F1：三阶段 + 分析透镜 + 竞争目标预览）：'去除污名'的过程模型首次亮相（Initiating a Moral Agenda 起点）"
  falling_action:
    - "Moral Prototyping（F3 前线）：Identifying the category with healing + Disidentifying with recreational use and the black market——道德原型的塑造"
    - "Front-Stage / Backstage Contrast（F3/F4）：Showcasing a squeaky-clean front-stage image vs Committing backstage survival violations——揭幕时刻（反派现场）"
    - "Side-Stage Negotiations（F5）：部分可见冲突 → 规范澄清（mixed/unexpected 的诚实处理）"
    - "Morality Infusion + Audience-Specific Success Assessment（F6）：按受众（state/federal governments 等）分别评估有限进展；Success of the Stigma Reduction Process 收束"
  denouement: "Discussion：P1-P3 隐性命题归纳（三阶段顺序+触发外生转内生 / 关系空间分离共存 / 符号先于物质的反向顺序）；'remove as opposed to manage' 贡献收口（stigma 文献从此多一条路径）；implications for strategic entrepreneurship 收尾（无独立 conclusion 段——ASQ 标准）；回到'等待被接纳'的开头"
```

### stakes

```yaml
stakes:
  theoretical: "stigma 文献默认组织只能'管理'污名（应对），看漏'去除'路径；核心污名与身份耦合意味着单企业 tactics 永远不够——不补，'污名组织如何改变自身合法性'的理论图景停在应对层面"
  practical: "医用大麻行业的生死：合法性合法但社会污名仍在，企业如何让行业被正当接纳（banks 拒开户、政策与公众认知的缓慢进程——'waiting to inhale' 的双关：等待被吸/被接纳）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: stigma management 故事 — '组织用策略应对污名'（文献惯例：shielding/straddling/co-opting 印象管理）"
  - "讲法B: 法律救赎故事 — '等立法放开，污名自然消失'（被动等待版：waiting 的消极读法）"
  - "讲法C: 个体英雄故事 — '单个企业家用道德叙事改变公众'（忽略集体性与过程）"
  - "本文: remove 叙事 — 组织主动去除污名（道德议程→道德原型→道德注入三阶段 + 三舞台分工）。选择理由：'remove as opposed to manage' 把贡献从'补充一种应对策略'升为'指出文献错误预设了问题的性质'——问题不是怎么应对污名，是怎么消除污名；三阶段过程模型让'去除'可教可复制（这是与单企业 tactics 的层级差别：类别级 vs 组织级）"
```

### storytelling_tools

```yaml
storytelling_tools:
  human_face: "定性研究最富的一篇：'Imagine starting a business when...' 第二人称开篇（沉浸式）；大量受访者原话（Peron、dispensary owners、conference presenters）；历史场景（Anslinger campaign、Robert Randall 案、AIDS 危机）作机制触发事件"
  rhetorical_question: "未见（待补确认）"
  pacing_notes: "Stroke/Glide ~70:30（theory 报告量化）；illustration 分布：田野引用 55% / 历史媒体叙事 30% / 理论陈述 15%；showing 断裂点：Discussion 理论升华较抽象（少具体事例）——质性的 denouement 常见弱点；三阶段各有前台/后台/侧台小节，平行节奏"
  showing_telling: "front-stage/backstage/side-stage 舞台隐喻 = 贯穿性 metaphor（Goffman 式 showing：三个空间名词即整个理论模型）；'Imagine' 六约束排比 = 开场即 showing"
  voice: "主动语态高频（'We find...', 'We argue...', 'Our findings suggest...'）；被动仅用于文献综述"
```

### cross_paper_notes

- **与 DesJardine 2022（overlooked-alternative 双原型）**：同型两种实现——desjardine2022 = 预设替代视角（deductive：'Most research underscores X' 直接宣战）；本文 = 归纳替代路径（inductive：remove 从数据里长出来）。对照价值：overlooked-alternative 的系紧方式可 deductive 可 inductive，五幕布局因此不同（前者 Tension 在 intro，后者在 findings）。
- **首份定性 blueprint 的形态差异**：五幕 overlay 按 Pollock Fig 2.3（context 承担 exposition、方法可信性作 rising、findings 开头作 climax、归纳模型作 falling、理论贡献作 denouement）；Theory 无独立段（T1 嵌入叙事、T4 隐性命题、无 T6）——theory 报告确认"质性过程论文：T1 嵌入叙事；T4 为隐性归纳命题而非正式假设；T5 以范围条件与比较命题形式出现"。
- **与 Pollock 2015 同作者跨范式**：Pollock 的定量（Untangled，解结）与定性（Waiting to Inhale，揭幕）两篇 blueprint 并存——同一 storyteller 两套范式，且 2015 是"解开构念之结"、2020 是"揭开幕布看后台"。
