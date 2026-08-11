# Story Blueprint — Wowak, Busenbark, Ball & Natarajan (2025) MS

## 文件头

```yaml
id: wowak2025
paper: "Wowak, Busenbark, Ball & Natarajan (2025, MS) — The Politics of Product Safety: TMT Political Ideology and Serious Medical Product Recalls"
distilled_sections: [intro, theory, methods, results]      # 全四区段 → ROBUST
source_records: [project-mvp30-wowak2025-intro]
corpus_links:
  write-introduction: "hooks/02-epigraph-quote-pivot 变体E（JFK 名言→政治极化悖论）；tensions/14-debate-unresolved 变体B（竞争机制预言型）；literature-turns/02-synthesized-coherence 变体D（双文献流交叉沉默）；previews/findings-preview 变体L（双 DV 竞争方向+Post Hoc 预告）；transitions/12-setting-justification 变体A；contributions 变体O（双向文献扫描收敛+觉察与缓解双价值）"
  write-theory: "variants/F_competing_hypotheses（范文）：自反性反机制（Conversely self-counter-mechanism）+ 多 DV 递进竞争（4-mechanism 2×2 折叠为竞争假设）"
  write-methods: "IV-2SLS 变体1-3（Lewbel 三步法/IV 诊断链/四指标操作化）+ 变体8（双估计器双层级两阶段 IV）+ 变体9（simultaneity 先证伪后 IV abundance-of-caution 叙事）"
  write-results: "IV-2SLS 变体1-6（竞争假设赢家报告/model-free 预览/IV 诊断嵌入 R3/去 IV 元稳健性）；计数模型 变体1-3（NB IV FE 四拍/双 DV 并行/post hoc mediation）；OLS-FE 变体2（threat-based 稳健性）"
```

## Story

### one_liner

> "自由派 TMT 更安全还是保守派 TMT 更安全？"——这个问题本身就问错了。答案是各赢一个维度：自由派召回更少（质量优先）但更慢（过度自信），保守派召回更多但更快（财务驱动）；而政治多样性 TMT 两头兼得。不是谁对谁错，是每个维度都有一方赢。

### knot

```yaml
knot:
  primary_type: paradigms-at-war   # 第二原型（zhou2017 外部理论战 + wowak2025 同构念两极战）：对立阵营对同一现象相反预测
  compound_types: []   # 内层 mild Inadequacy（竞争假设）：两派价值观各自合理
  statement: "TMT 政治意识形态如何影响产品安全？liberal（社会福祉/最小化消费者伤害）与 conservative（股东价值/风险厌恶/最优配置）对召回数量与召回速度推出相反预测——两派不是谁对，而是各赢一个维度（H1a/H1b + H2a/H2b）"
  tied_at:
    - "Intro：JFK epigraph（'right answer' 名言）→ 政治极化悖论 → 25/36/35% 三分光谱；双文献流交叉沉默（政治意识形态流 × 召回前因流：'has eluded academic attention' + 'existing research is silent on'）"
    - "Theory：§3.1 双极价值观界定（liberal vs conservative 各三条价值轴）；§3.2 'On the one hand... On the other hand...' 竞争推导"
  untied_at:
    - "Theory：H2a/H2b 的 4-mechanism 2×2 折叠为一对竞争假设（丰富机制→简洁假设的压缩）"
    - "Results：model-free 均值预览 → Table 4 主结果（H1a β=-0.113***、H2b β=0.453**）"
  antagonist: "'谁更好'这个错误问题——双文献流的交叉沉默（意识形态流不看产品、召回流不看意识形态）+ 党派直觉（读者/政策预设 liberal 或 conservative 单方正确）；反派是单向思维的惯性"
  antagonist_built_by:
    - "双文献流交叉沉默：两流各自'已知→未知'收敛到同一缺口（召回前因流：CEO turnover/female directors/CEO comp 已做→TMT 意识形态未做；意识形态结果流：CSR/dismissals/activism 已做→产品质量未做）——'Although... Similarly...' 平行结构"
    - "JFK epigraph：'right answer' 被政治极化悖论反噬——名言与现状的对比让'谁对'的问题显得天真"
```

### characters

```yaml
characters:
  protagonist: [TMT 政治意识形态 (X，liberal/conservative 双极双主角), 产品安全 (Y，双 DV：recall count / time-to-recall)]
  supporting:
    - "政治多样性 TMT（post hoc 兼得者：'best of both' 处方）"
    - "不良事件中介（FAERS+MAUDE，post hoc '为什么'）"
  ensemble: [CEO/TMT/board/firm 四层控制（表1）、firm FE（88 召回 + 41 非召回企业，2002-2015，4,072 recalls）、行业情境（High-Risk/High-Reward 论证）]
```

### resolution_logic

`dimension-split` 维度分裂（新解法性格候选，单篇原型）——**对立预测在 DV 不同维度各成立**：不裁决谁对，而是把 Y 拆成两个维度（数量/速度），每个维度让一方赢；post hoc 再用政治多样性证明"兼得"存在（best of both = 调和两极张力的处方）。研究者是"改判比赛规则"的裁判：不是判谁赢，而是说明这场比赛本来就该分两场比。

### five_acts

```yaml
five_acts:
  exposition: "Intro：JFK epigraph → 政治极化悖论 → 25/36/35% 三分光谱（数据光谱式 Hook）；双文献流交叉沉默定位缺口；RQ；Preview 预告双 DV 竞争方向 + Post Hoc（⚠️ 已登记叙事风险：Preview 过度详细——预告了所有 post hoc 结果）"
  rising_action: "Theory：§3.1 双极价值观界定（liberal：社会福祉/集体责任/最小化伤害；conservative：个人财富/股东价值/风险厌恶/资源最优配置）；§3.2 H1a/H1b（count：'On the one hand' quality-first vs 'On the other hand' 质量长期财务价值）；H2a/H2b（time-to-recall：4-mechanism 2×2——liberal-faster 责任/liberal-slower 过度自信/conservative-faster 财务/conservative-slower false-alarm 恐惧+层级流程——折叠为一对竞争假设）；Methods：双估计器双层级两阶段 IV（NB FE@firm-year 计数 + 2SLS FE@recall 层时长）；Lewbel 三步 IV（Pagan-Hall p=0.084 / Breusch-Pagan / partial F=59.534 / Andrews 不含0 / Sargan）；'abundance of caution' 先证伪后 IV 叙事（命名威胁→双理由证伪→行为证据 92% 不切换政党→才上 IV）"
  climax: "Results 开头 model-free 均值预览：liberal 3.78 vs conservative 5.73 recalls；78.11 vs 55.39 days——两行数字并置即'各赢一维度'（先给全景再给系数）；Table 4 主结果（H1a 支持 β=-0.113***；H2b 支持 β=0.453**；1.10 fewer recalls/SD、22 days longer/SD）"
  falling_action:
    - "六稳健性按 threat 组织（去控制/去 IV/召回率 fractional response/拆 CEO/去 nondonor/RE 纳入非召回企业）"
    - "'去 IV'元稳健性：移除识别策略重跑，'非 IV 与 IV 一致'反向论证内生性偏误低（区别于'加 IV 防御'的常规）"
    - "Post hoc 1：不良事件中介（FAERS+MAUDE，indirect=-0.130**）——'为什么'（机制）"
    - "Post hoc 2：政治多样性 CV 兼得（更少 β=-0.230*** 且更快 β=-0.462**）——'怎么办'（处方，best of both）"
  denouement: "Discussion：'各赢一维度'的调和图景收口——竞争假设不是输赢而是分工；政治多样性 TMT 作 mitigation 处方（贡献段变体O 的 awareness/mitigation 双价值兑现）"
```

### stakes

```yaml
stakes:
  theoretical: "两个文献流（政治意识形态 × 召回前因）各自沉默——谁都没问'高管政治价值观如何塑造产品安全'；且单向预设（liberal 好/conservative 坏）会让政策与董事会构成判断系统性偏误"
  practical: "医疗产品召回的生死后果（serious recalls）；召回制度该奖励速度还是数量？董事会构成该不该考虑政治多样性（两全其美）——产品安全治理的真决策"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: liberal 安全故事 — 只测召回数量：'自由派更安全'（半个故事，只赢 count 维度）"
  - "讲法B: conservative 效率故事 — 只测召回速度：'保守派反应更快'（另半个故事，只赢 timing 维度）"
  - "讲法C: 意识形态无关故事 — '产品安全与技术、监管有关，与政治无关'（desk-reject 版：回避问题）"
  - "本文: 各赢一维度 + 多样性兼得 — 不选边，改判规则。选择理由：竞争假设的结构天然让两个替代故事并存（每篇单 DV 文献都讲了一个）；'各赢一维度' + post hoc 兼得把贡献从'谁对'升为'维度分工与调和处方'——读者与政策的两难被回答而不是被裁决"
```

### storytelling_tools

```yaml
storytelling_tools:
  human_face: "JFK epigraph（'right answer' 名言——文化重量）+ 医疗产品召回的生死风险（stakes 的人面）；[推断] 召回个案案例"
  rhetorical_question: "待补"
  pacing_notes: "model-free 均值预览先于 Table 4（两维度全景 → 系数细节——climax 前移的倒金字塔节奏）；falling action 六稳健性按 threat 组织（防御式展开）+ 两 post hoc 收束（为什么→怎么办的上升收尾）"
  showing_telling: "25/36/35% 三分光谱（数据光谱式 showing：意识形态不是二分而是光谱）；model-free 双均值并置（78.11 vs 55.39 days 的并排即'各赢一局'的图形化"telling"）"
  voice: "待补"
```

### cross_paper_notes

- **与 Zhou 2017（paradigms-at-war 第二原型）**：同'对立阵营相反预测'故事家族，解法不同——Zhou = 拆地整合（arbitration：facet 分解出倒U）；本文 = 维度分裂（dimension-split：DV 拆维各赢一局）。对照价值：**冲突形态可以相同，解法性格可以不同**——这是 knot 类型 × resolution 类型正交性的首个实证。
- **与 Malshe 2015（非单调发现家族）**：floodlight 双转折点（杠杆符号随水平反转）vs 各赢一维度（竞争假设随 DV 维度分胜负）——'反直觉不是单一结论而是结构拆分'的两种形态。
- **与 Mayo 2022（召回文献家族）**：同召回文献语境（CEO turnover 相关）不同故事——recall 文献内部的故事多样性。
