# Story Blueprint — DesJardine, Shi & Cheng (2023) ASQ

## 文件头

```yaml
id: desjardine2023
paper: "DesJardine, Shi & Cheng (2023, ASQ) — The New Invisible Hand: How Common Owners Use the Media as a Strategic Tool"
distilled_sections: [intro, theory, methods, results]      # 2026-08-09 读原文定稿（共同所有权/07 原文/）→ ROBUST
source_records: [project-mvp30-desjardine2023-invisible-hand-intro]
vault_reports:
  intro: "narrative_analysis/introduction/mvp30/fine_grained/batch_2026-05-24（误标 desjardine2022_orsc 目录）——2023 的 intro 蒸馏记录在 memory；原文：共同所有权/07 原文/The New Invisible Hand...2023.md"
  theory: "原文 Theoretical background（Invisible Hands 三小节）+ Hypotheses development（H1/H2a/H2b/H3/H4）"
  methods_results: "原文 Methods（Heckman 两阶段/RavenPack ESS/media-rival CIO/firm-media pair FE）+ Results（Table 4，H1 1.426***）+ Robustness + Supplementary"
  story_arc: null
corpus_links:
  write-introduction: "tensions/01-despite-progress-unaddressed 变体Z（可见-不可见域缺口 + oversight 驱动地下化）；变体AA（权威警告 + 例外枚举 + 规模-忽视悖论）"
  write-methods: "两阶段 Heckman 选择（media coverage 可观测性——exclusion restriction=local media outlets）；firm–media pair FE + 聚类 SE；winsorize 1%"
  write-results: "主效应 + 经济显著性转译（7.7% = CVS 1% 利润下滑 vs Marriott 3% 增长）；incentive/power 机制拆解；四调节（相似性×2/期限/媒体 CEO 激励）"
```

## Story

### one_liner

> 学者们盯着看得见的竞争动态，而共同所有者真正在做的，是水面之下通过媒体当战略武器：机构投资者同时持有媒体公司与竞争对手的股份，就能让媒体对目标公司的报道变得更负面——而且竞争越激烈、持股越长期、媒体 CEO 拿的股权激励越多，这把"新无形之手"越用力。监督得越紧，这只手越隐蔽。

### knot

```yaml
knot:
  primary_type: irony-reversal   # 双原型（pontikes2012 + desjardine2023）：行动产生与预期相反的结果
  compound_types: [neglected-arena]   # 不可见域被忽视（动态版：范式再生产盲区）
  statement: "共同所有者如何影响竞争动态？领域研究聚焦可见域（企业直接行动 + 局外人公开支持），遗漏不可见域——共同所有者借媒体作战略工具：media-rival common ownership → 目标公司媒体负面性上升（'While scholars have paid close attention to [visible X], there exists [Y beneath the surface]'）"
  tied_at:
    - "Intro 变体Z：可见-不可见域缺口 + 'oversight → unintended consequence'（审视不消除操纵，反而驱使更隐蔽路径）"
    - "Intro 变体AA：规模-忽视悖论（机构投资者最大股东却 most overlooked）+ Picard 权威警告 + 例外枚举"
    - "Theory：Invisible Hands 三小节（economic forces → common owners → media as strategic asset）"
  untied_at:
    - "Results：Table 4 Model 2——media-rival CIO 1.426***（+7.7% 负面性/SD）——'新无形之手'的因果揭晓"
    - "Results：incentive/power 拆分（rival ownership 0.103*** / media ownership 0.188***——机制拆解）"
  antagonist: "领域自身的研究范式（盯着可见域）+ 监督的善意（监督本应矫正，实际把操纵赶入地下）——'盯着的动作本身在制造盲区'"
  antagonist_built_by:
    - "'oversight → unintended consequence' 签名：监管/审视越强，隐蔽路径越发达"
    - "规模-忽视悖论：最大股东 85% 却最少被研究（重要性×被忽视度的乘积制造荒谬感）"
    - "三重背书：Picard 权威警告 + 例外枚举（govt control/ad revenue/readers）+ 悖论"
```

### characters

```yaml
characters:
  protagonist: [media-rival common institutional ownership (X，共同所有者对媒体×竞争对手的双重持股), media coverage negativity (Y，RavenPack ESS)]
  supporting:
    - "firm-rival product similarity / geographic market overlap（H2a/H2b——竞争越近，手越用力）"
    - "investment horizon（H3——long-term 3.127*** vs short-term n.s.，diff p<0.001）"
    - "media CEO equity compensation（H4——媒体高管的激励把门打开）"
    - "incentive（rival ownership）/ power（media ownership）——机制拆解双变量"
  ensemble: [firm-media pairs（109,965 obs）、industry/year FE、RavenPack 数据、TNIC-3 竞争对手识别]
```

### resolution_logic

`revelation` 揭幕（换镜头）——把镜头从可见域转向水面之下：不可见域不是没有证据，是没人看。构念命名 canonical inversion（The New Invisible Hand 反转 Adam Smith）在命名层完成视角翻转；Heckman 两阶段处理"媒体覆盖的可观测性"选择（镜头本身的盲区修正）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：可见-不可见域缺口（变体Z：oversight→unintended consequence 签名）；规模-忽视悖论 + Picard 权威警告 + 例外枚举（变体AA）；命名反转（The New Invisible Hand）在标题完成对 Adam Smith 的征用"
  rising_action: "Theory：Invisible Hands 三小节（economic forces 塑造市场 / common owners 的无形之手 / media 作为战略资产）→ 假设发展（H1 主效应 + H2a/H2b 竞争相似性 + H3 投资期限 + H4 媒体 CEO 激励）；Methods：两阶段 Heckman（DV 仅在媒体覆盖时可观测——exclusion restriction = local media outlets，0.092***）；DV = media coverage negativity（RavenPack ESS）；IV = media-rival CIO（共同所有者对 rival 持股 × 对媒体持股）；firm-media pair FE + winsorize + 聚类 SE"
  climax: "Results Table 4 Model 2：media-rival CIO 1.426***（p<0.001）——经济显著性转译：+7.7% 负面性 ≈ 从'3% 利润增长'（Marriott 0.47）变成'1% 利润下滑'（CVS 0.51）、从'延迟扩张'（Google 0.64）变成'危险召回'（Kellogg 0.71）——'新无形之手'现形"
  falling_action:
    - "incentive/power 机制拆解：rival ownership 0.103***（动机）+ media ownership 0.188***（权力）——手的两根手指"
    - "H2a/H2b 支持：product similarity 18.443*、geographic overlap 1.785*（调节图——竞争越近越用力）"
    - "H3 支持：long-term 3.127*** vs short-term n.s.（diff p<0.001）——长期主义者才玩这把刀"
    - "H4 支持：media CEO equity comp 3.980*——媒体高管的激励是开门钥匙"
    - "Robustness（按威胁组织）+ Supplementary（待补细节）"
  denouement: "Discussion：theoretical implications（媒体作为战略资产的 invisible hand 理论化——竞争动态的第三只手）+ practical implications（监管者与学者盯着可见域的政策含义——'监督制造地下化'）+ conclusion（'The New Invisible Hand' 收口——回到 Adam Smith 的征用）"
```

### stakes

```yaml
stakes:
  theoretical: "竞争动态研究只看可见域，会对'竞争如何被扭曲'产生系统性失明——盲区不是证据缺口，是范式制造的；共同所有者×媒体的交叉是无人区"
  practical: "监管者与学者在监督'可见操纵'上投入越多，隐蔽路径可能越发达——反垄断与媒体治理的政策辩论（反 SLAPP 之后的下一战场）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 乐观监督叙事 — '媒体监督/学者关注会矫正企业行为'（共识版；本文的反面）"
  - "讲法B: 传统 invisible hand 故事 — '市场无形之手自动协调竞争'（Adam Smith 意象的原版；本文反转的命名原型）"
  - "讲法C: 可见域补洞版 — '企业直接竞争行为里还有个变量没测'（gap-filling 版）"
  - "本文: 新无形之手 — 可见域监督驱动不可见域地下化（irony：监督制造盲区）。选择理由：命名反转（invisible hands）带文化重量；'oversight→underground' 把缺口从'没发现'升为'关注本身在制造'；Heckman 修正镜头自身的盲区——方法与故事同构"
```

### storytelling_tools

```yaml
storytelling_tools:
  human_face: "Picard 权威警告（具名权威）；经济显著性转译的具名企业对照（CVS/Marriott、Kellogg/Google——'负面性 +7.7%'是什么感觉）；Table 2 新闻事件类型表（headlines 举例）；9 位业内人士访谈（4 记者/2 编辑/3 媒体高管——补充理论的方法论人面）"
  rhetorical_question: "学术呼吁问句收尾：'How can we create a news ecosystem and culture that values and promotes truth?'（Lazer et al. 2018 引用——规范性问句作 P8 收束，与 Picard 警告呼应）"
  pacing_notes: "Theory 三小节递进（economic forces → common owners → media asset——从宏观到微观的漏斗）；climax 后 falling 是'拆手'（incentive/power 两根手指 → 四条件逐条）——揭幕后解剖；经济显著性转译先于系数解释（R3 惯例）"
  showing_telling: "canonical inversion（invisible hands 反转 Adam Smith）= allusion 级 showing；'beneath the surface' 意象贯穿；调节图 ×4（showing——手何时更用力）"
  voice: "we posit/we mobilize 中性学术语态 + 访谈在场（'We complement our theory with interviews with nine individuals'——已核实 2026-08-09）"
```

### cross_paper_notes

- **与 Pontikes 2012（irony-reversal 双原型）**：同型两种 irony——pontikes = 同一构念对两类受众相反意义（静态镜像）；desjardine2023 = 监督行动产生相反结果（动态反噬）。'irony' 家族的两种切法被双原型钉死。
- **与 DesJardine 2022（同作者同现象不同故事，最强对照对）**：同一 common ownership 语境——2022 overlooked-alternative（组合视角翻面：CSR 涨潮）；2023 irony-reversal（媒体战略工具：监督驱动地下化）。两篇合起来是"同一现象域的故事空间"示范。
- **与 Desai 2012（注意力-缺口家族）**：desai = 被动遗忘（静态遗漏）；本文 = 注意力在场且再生产盲区（irony 动态版）。
- **与 Malshe 2015（经济显著性转译家族）**：malshe floodlight 双转折；本文 7.7% 转译（CVS/Marriott）——'系数翻译成可感幅度'的两种形态。
