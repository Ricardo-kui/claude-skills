# Story Blueprint — Pollock, Lee, Jin & Lashley (2015) ASQ

## 文件头

```yaml
id: pollock2015
paper: "Pollock, Lee, Jin & Lashley (2015, ASQ) — (Un)Tangled: Exploring the Asymmetric Coevolution of New Venture Capital Firms' Reputation and Status"
distilled_sections: [intro, theory, methods, results]
source_records: [project-mvp30-pollock2015-untangled]
corpus_links:
  write-introduction: "literature-turns/02-synthesized-coherence 变体E（让步-权威定义锚定-推测/系统分层四步）；transitions/12-setting-justification 变体B；stakes/06-two-reason-enumerated 变体B（4层 ascending-cascade）；hooks/01-cross-disciplinary-analogy 变体A（共演类比）"
  write-theory: "subprotocols/hypothesis_derivation_patterns（developmental reversal of reciprocal-causation asymmetry H1a/H1b + differential persistence/ρ 调节 H2）；variants/A_construct_differentiation（构念四维区分）"
  write-methods: "动态面板-GMM 变体1–4；同时方程 变体1–2（堆叠非嵌套 Wald χ²）；同伴效应-网络效应 变体4（Bonacich）；实证对象构建 变体4（multi-item formative reputation index）"
  write-results: "OLS-FE 变体35–39（ρ 持久性%对比 / 分样本 Wald+partial support / GMM 零结果 Monte Carlo 功效 / post-hoc spline / 3SLS LDV 偏误警示）"
```

## Story

### one_liner

> status 和 reputation 被文献当成同一个东西（或单向因果），其实这两个主角在一张网上不对称地共演——谁驱动谁随公司年龄反转，谁更"粘"也不同；把结解开的关键不是选方向，而是让两个方向同时上场，再在时间轴上找出反转点。

### knot

```yaml
knot:
  primary_type: tangled-constructs   # 构念纠缠型（新类型候选，见 skill_design_feedback）
  compound_types: [assumption-flip]  # 隐含假设错误：两构念可互换/单向因果
  statement: "status 与 reputation 纠缠不清——文献或混同两者、或假设单向因果；实为不对称共演，且不对称方向随 firm age 反转（H1a/H1b）"
  tied_at:
    - "Intro literature turn：四步文献对话——让步（concession-as-credibility）→ 权威定义锚定（Washington & Zajac 逐字定义，暴露'定义上就纠缠'）→ 推测 vs 系统研究分层（'之前只有 speculation，没有 systematic'）"
    - "Theory：reciprocal-causation 设定（双方程互为因变量）把纠缠结构化为双向"
  untied_at:
    - "Theory：H1a/H1b 不对称随 age 反转（解结的时间轴）；H2 differential persistence（ρ 调节——status 粘、reputation 不粘）"
    - "Results：堆叠非嵌套 Wald χ² 检验 H1a/H1b 方向（解结的关键证据）"
  antagonist: "文献对两构念的混同与单向假设——'tangle' 是文献打死的结：定义上纠缠（权威定义逐字锚定证明两者常被互用）、因果方向被默认单向"
  antagonist_built_by:
    - "让步-定义锚定四步：先承认文献价值（concession 建立可信度），再用权威定义逐字锚定暴露出'两构念在定义层面就纠缠'——反派不是某派理论，而是集体性的构念混同"
    - "推测 vs 系统分层：'只有推测没有系统研究' 把缺口从'没人做'升格为'一直停留在推测层'"
```

### characters

```yaml
characters:
  protagonist: [status, reputation]   # 共演双主角：两个构念都承担主线（Pollock Ch02: 双主角各走一条 storyline）
  supporting:
    - "firm age：H1a/H1b 方向反转的切换器（时间轴角色）"
    - "blockbuster deals：H3a/H3b DV-条件效应随 age 翻转；H4 对 low-status/low-rep 帮助更大"
  ensemble: [网络位置（Bonacich 中心性）、跨年 rescaling 的 reputation index 构念测量、VC 行业情境与控制变量]
```

### resolution_logic

`revelation` 揭幕（解结）——**让双向同时上场**：同时方程（动态双方程）+ Arellano–Bond difference GMM 把"谁驱动谁"从二选一改为"两个方向各自多大、何时反转"；age 作为时间轴揭示不对称反转；ρ 对比揭示"粘性差异"。研究者是解结人：不剪断结，而是把结拆开摊平。

### five_acts

```yaml
five_acts:
  exposition: "Intro：status/reputation 对 VC 的重要性；'tangle'意象（标题即预告）；四步文献对话暴露定义纠缠与推测层停滞；setting-justification 把研究场所（新创 VC）理论化"
  rising_action: "Theory：H1a/H1b 不对称共演 + age 反转（共演 baseline 本身'unsurprising' → 不立假设，把张力放在不对称上）；H2 differential persistence（ρ 调节）；H3/H4 blockbuster 条件效应；Methods：433 新创 VC（1990–2000 立、跟至 2010）动态同时方程面板；AB difference 而非 system GMM 的选择论证（young firms 未达稳态）——arena 搭建本身是 Rising Action 的一部分"
  climax: "Results：堆叠非嵌套 Wald χ²（Weesie 1999，stack + vce(cluster) 恢复跨方程协方差）——H1a/H1b '哪个方向更强'的裁决瞬间"
  falling_action:
    - "ρ 持久性% 跨构念对比（H2：status 粘 vs reputation 不粘）"
    - "分样本 Wald + partial support 诚实叙事（部分假设只在部分年龄段成立）"
    - "GMM 零结果 Monte Carlo 功效分析：理论关键的'不变'那半（H1b 某方向在 age 后期的 null 是理论预测）——把 null 从失败转成证据"
    - "post-hoc spline 重解释意外负效应（信息递减 → diminishing returns）"
    - "3SLS 替代估计器 LDV 偏误诚实警示——反向佐证 AB 选择（自曝替代方案缺陷换取方法可信度）"
  denouement: "Discussion：不对称共演的完整图景收口；双主角的 storyline 在 denouement 发散（age 后期 reputation 继续增长而 status 粘住——'heroes end up following different paths'，呼应标题 (Un)Tangled 的解开意象）"
```

### stakes

```yaml
stakes:
  theoretical: "两个核心无形资产构念被混同或单向化，导致文献对'谁驱动谁、何时反转'的系统性误读；不解开，地位/声望理论在动态问题上停滞在推测层"
  practical: "新创 VC 的声望管理：创始人/基金该经营 status 还是 reputation、随 age 何时切换策略——blockbuster 策略对 low-status/low-rep 的帮助（H4）直接是实践决策"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 单向地位叙事 — 'status 决定 reputation'（社会地位文献常见讲法；静态、单向）"
  - "讲法B: 单向声望叙事 — 'reputation 决定 status'（反向文献；同样静态）"
  - "讲法C: 构念等价 — 'status 和 reputation 是一回事，换个测量而已'（混同版；正是要解开的结）"
  - "本文: 不对称共演 + age 反转 — 两个方向同时在场、权重随年龄反转、粘性各异。选择理由：与'tangle'意象完全一致（解开而非剪断）；同时方程设计让双向共同在场；age 反转产生文献没有的动态预测；'unsurprising baseline 不立假设'把叙事预算留给不对称"
```

### storytelling_tools

```yaml
storytelling_tools:
  human_face: "自然界共演类比作 Hook 的 showing 变体（2026-08-09 原文核实）：狼与驯鹿、植物与传粉者、黑洞与星系——'共演无处不在'的具名自然例子，人类 face 的生态学版本"
  rhetorical_question: "未见（已核实 2026-08-09）"
  pacing_notes: "Intro 四步文献对话自带节奏控制（让步慢 → 定义锚定中速 → 推测/系统分层收束）；Theory 把叙事预算集中在不对称与反转（baseline 不立假设=省篇幅）；Results 是'裁决（Wald）→ 分层（ρ对比）→ 补洞（Monte Carlo 功效）→ 重释（spline）→ 自曝（3SLS 警示）'的 falling action 五连——每步都在加固同一个解开动作"
  showing_telling: "'tangle/(Un)Tangled' 标题隐喻是贯穿性 allusion；自然界共演类比（Hook 开场 showing）"
  voice: "we explore/we focus 中性学术语态（已核实 2026-08-09）"
```

### cross_paper_notes

- **与 Malshe 2015（同期重蒸馏，同时方程对）**：同一估计家族（同时方程/动态面板），故事完全不同——Malshe = 跨学科补半区（half-domain-gap，敌人是学科边界）；本文 = 解开构念纠缠（tangled-constructs，敌人是构念混同）。对照价值：**设计类型相同 ≠ 故事相同**，这是"同一模型不同故事"的又一实例。
- 与 Pontikes 2012：都处理"两个东西被当成一个"的表象，但 Pontikes 是同一构念对两类受众相反意义（irony），本文是两构念的动态关系被误读（tangled）——同家族不同故事。
