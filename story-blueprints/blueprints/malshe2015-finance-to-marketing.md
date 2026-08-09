# Story Blueprint — Malshe & Agarwal (2015) JM

## 文件头

```yaml
id: malshe2015
paper: "Malshe & Agarwal (2015, JM) — From Finance to Marketing: The Impact of Financial Leverage on Customer Satisfaction"
distilled_sections: [intro, theory, methods, results]
source_records: [project-mvp30-malshe2015-intro]
corpus_links:
  write-introduction: "literature-turns/01-progressive-coherence 变体H（新兴交叉流+互补半区缺口型：equity done / debt not）；hooks/01-cross-disciplinary-analogy 变体B（学科交叉型）；tensions/01-despite-progress-unaddressed 变体D（surprising for three reasons）"
  write-theory: "hypothesis_derivation_patterns（Cross-Disciplinary Theoretical Lens；Four-Reason Parallel Mechanism；Intangible Asset Real Options + Financial Constraint Distal Moderation）"
  write-methods: "同时方程 变体3（辅助反向因果方程）+ 变体4（DWH 裁决 SUR vs 3SLS）；面板数据-OLS 变体26（跨库手工匹配五库漏斗）"
  write-results: "OLS-FE 变体40（floodlight 双转折点）；OLS-FE 变体41（系统三条件中介+非对称支持）；OLS-FE 变体42（反直觉反向 H2c 诚实报告）"
```

## Story

### one_liner

> 杠杆是个双极现象：股权那半区营销学者已经做过了，债务这半区没人碰——finance 不关心顾客，marketing 不碰杠杆。本文把 finance 五十年的杠杆传统嫁接进营销学，补上债务半区，结果发现杠杆对顾客满意的影响不是单调的：它在某个水平上由正转负（双转折点），而且两条作用路径（广告 vs 研发）只通了一条。

### knot

```yaml
knot:
  primary_type: half-domain-gap   # 互补半区型（新类型候选：现象有天然双极，前人只做一极，另一极即 gap）
  compound_types: [counterevidence]  # 主发现反直觉：杠杆对满意非单调（floodlight 双转折点）、H2c 方向与假设相反
  statement: "债务杠杆如何影响顾客满意？finance 研究了杠杆五十年但不碰顾客，marketing 研究满意但不碰杠杆；仅有的交叉流（Luo 2008、Kurt & Hulland 2013）只做了 equity 半区——debt 半区空白"
  tied_at:
    - "Intro Move 2 三步文献 turn：源学科纵深（finance 50 年传统）→ 'Recently, marketers have begun to examine...'（新兴交叉流标志）→ 互补半区 pivot（equity done / debt not）"
    - "Intro Move 3：'This is surprising for three reasons. First... Second... Third...'（每条理由用源学科 finance 证据支撑 gap 重要性）"
  untied_at:
    - "Theory：双通道机制（advertising / R&D 无形资产的 real options 视角）+ financial constraint 远端调节"
    - "Results：floodlight 双转折点（符号在 ~65% leverage 处过零、~95% 处进入显著区）"
  antagonist: "两学科各自的边界 + 交叉流的半区覆盖——finance 的领域边界（不碰顾客端）、marketing 的边界（不碰资本结构）、'equity 已做'造成的半区错觉（以为杠杆问题已答）"
  antagonist_built_by:
    - "互补半区 pivot：'equity done / debt not' 一句把前人的贡献同时变成自己的地图——前人的完成度越高，空白的另一半越显眼"
    - "surprising-for-three-reasons：三条理由全部借用源学科 finance 的证据来论证 gap 的重要性（跨学科 credibility 转移）"
```

### characters

```yaml
characters:
  protagonist: [financial leverage（debt 半区）(X), customer satisfaction (Y)]
  supporting:
    - "advertising 强度 / R&D 强度：双中介通道（结果非对称——advertising 成立、R&D 不成立，失败根因定位到条件2 IV→M 不显著）"
    - "financial constraint：远端调节（Intangible Asset Real Options 视角）"
  ensemble: [ACSI↔Compustat 五库手工匹配样本、行业与年份控制]
```

### resolution_logic

`exploration` 拓荒 + 路径分解——把杠杆按 debt/equity 拆开（补半区），把影响按 advertising/R&D 拆成两条通道（路径分解），再加 financial constraint 条件化。研究者是跨界测绘者：把 finance 的地图扩展进 marketing 的领域，并标出哪里通、哪里不通（非对称中介）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：跨学科类比 Hook（finance 50 年传统 → marketing crossover）；三步文献 turn 到互补半区 pivot；surprising-for-three-reasons 把 gap 的代价坐实；贡献段 'among the first + combine finance and marketing' 与半区逻辑回响"
  rising_action: "Theory：Cross-Disciplinary Theoretical Lens（把 finance 的杠杆逻辑移植进营销机制）；Four-Reason Parallel Mechanism（advertising/R&D 双通道）；financial constraint distal moderation；Methods：五库手工匹配（无共同 firm ID → manually matched，漏斗式说明样本构建的诚实）；同时方程系统（辅助反向因果方程吸收'下游需求→政策变量'通道；DWH 裁决后选 SUR——'用 IV 处理内生性'的常规被反向论证）"
  climax: "Results 主效应：floodlight 双转折点（零交叉 ~65% leverage + 显著性交叉 ~95% + 90% CI 带）——杠杆对满意的符号随水平反转，非线性是主角"
  falling_action:
    - "系统三条件中介 + 非对称支持：advertising 路径成立、R&D 路径不成立——失败根因定位到具体条件（IV→M 不显著），'半通'本身就是发现"
    - "H2c 反直觉反向诚实报告：当场 'in contrast to H_c' 声明 + 推迟到 Discussion 解释 + post-hoc 机制 + 数据局限（不掩盖反向）"
  denouement: "Discussion：debt 半区的营销含义收口；H2c 的 post-hoc 机制与数据局限说明；equity/debt 半区整合后的完整杠杆图景——顾客满意视角的资本结构含义"
```

### stakes

```yaml
stakes:
  theoretical: "营销学对'杠杆'只有股权半区认知（Luo 2008、Kurt & Hulland 2013），债务半区空白导致'财务决策如何影响顾客'的理论图景残缺；跨学科嫁接暴露两学科各自边界的盲区"
  practical: "企业资本结构与顾客满意的交叉：CFO 的融资决策（债务水平）会改变 CMO 的广告/研发投资回报——资本结构与营销战略的对话；非单调意味着'加杠杆'不是线性有害"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: equity-only 故事 — '股权融资如何影响顾客相关投资'（Luo 2008、Kurt & Hulland 2013 已讲；半区已覆盖）"
  - "讲法B: 平均效应故事 — '杠杆整体上损害/无关顾客满意'（aggregate leverage 单一路径；会错过非单调与双通道差异）"
  - "讲法C: finance 边界拒绝版 — '杠杆是融资成本问题，与顾客无关'（finance 主流的领域边界；正是本文要拆的墙）"
  - "本文: debt 半区 + 双通道 + 非单调 — 互补半区 pivot 贯穿 hook→turn→gap→contribution 形成紧致回响。选择理由：'equity done / debt not' 让前人的工作成为自己的铺垫而非对手；非单调与半通中介是'补地图'版本的增量——不是重复测一次，而是画出前人没画的半区与形状"
```

### storytelling_tools

```yaml
storytelling_tools:
  human_face: "GM 与 Chrysler 2009 破产失去大量客户（2026-08-09 原文核实：隐性契约违约的具名例证）；'double whammy for marketers'（口语隐喻作概念锚）"
  rhetorical_question: "无（'Does leverage have a negative impact...?' 是研究问题陈述，非修辞问——已核实 2026-08-09）"
  pacing_notes: "Intro 三步文献 turn 自带节奏（源学科纵深慢 → 交叉流中速 → 半区 pivot 急转，'Recently... begun to examine' 是变速信号）；Results 把最大叙事预算给 floodlight（非线性主角先出场），中介与反向 H2c 作 falling action（半通 + 诚实报告）"
  showing_telling: "floodlight 图（双转折点 + 90% CI 带）= showing 核心——'符号何时反转'是只有图形能讲的句子"
  voice: "'we aim to answer two related questions' 第一人称；'double whammy' 口语化隐喻（已核实 2026-08-09）"
```

### cross_paper_notes

- **与 Pollock 2015（同期重蒸馏，同时方程对）**：同一估计家族（同时方程系统），故事完全不同——本文 = 跨学科补半区（half-domain-gap，敌人是学科边界）；Pollock = 解开构念纠缠（tangled-constructs，敌人是构念混同）。**设计类型相同 ≠ 故事相同**——"同一模型不同故事"的又一实例。
- 与 Pontikes 2012 的表面相似要区分：Pontikes = 同一构念对两类受众相反意义（irony-reversal，两面共存）；本文 = 同一维度的两半区，一半已做一半空白（half-domain-gap，一半缺失）。"两面"是同时存在，"半区"是先后覆盖——两种 gap 修辞不能混用。
