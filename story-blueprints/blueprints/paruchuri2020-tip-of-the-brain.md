# Story Blueprint — Paruchuri, Pollock & Kumar (2020) SMJ

## 文件头

```yaml
id: paruchuri2020
paper: "Paruchuri, Pollock & Kumar (2020, SMJ) — On the Tip of the Brain: Understanding When Negative Reputational Events Can Have Positive Reputation Spillovers, and for How Long"
distilled_sections: [intro, theory, methods, results]      # 2026-08-09 读全文定稿 → ROBUST
source_records: [vault narrative: narrative_analysis/mvp30/paruchuri2020_tip_of_brain_smj_narrative.md]
vault_reports:
  intro: "narrative_analysis/mvp30/paruchuri2020_tip_of_brain_smj_narrative.md"
  theory: "parsed_texts/mvp30/On the tip of the brain...（§2：associability/salience）"
  methods_results: "parsed_texts/mvp30/On the tip of the brain...（§3-4：Chipotle E. coli 自然实验/Yelp）"
  story_arc: null
corpus_links:
  write-introduction: "tensions/02-implicit-assumption-wrong 变体D（效价反转例外型——本文即故事层对应）；hooks/04-puzzle-paradox 变体B（假设解构）"
  write-methods: "自然实验（Chipotle E. coli 西雅图 2015）；Heckman 选择（无评论周缺失校正——IMR 不显著后剔除）；RE 回归"
  write-results: "三向交互（Salience × Same category × Geographic proximity，p=.06）；效应持久性检验（salience 消退→溢出消失）"
```

## Story

### one_liner

> 文献默认负面事件只产生负面溢出（竞争者同遭池鱼之殃），本文说：负面事件有时让竞争者**获益**——Chipotle 的 E. coli 危机让西雅图同区同类的墨西哥餐厅评分上涨 16.3%（3.1→3.6 星，排名跳升 90 位）——但只有当危机被记得（salience 高）且它们离事件够近（同类+同区）时；新闻热度一退，荣誉就消失。同一场危机，同行是遭殃还是渔利，取决于关联性与可得性。

### knot

```yaml
knot:
  primary_type: assumption-flip   # 首独立故事层原型——挑战 valence 单向假设
  compound_types: []
  statement: "文献隐含假设负面事件只产生负面声誉溢出（valence 单向）；本文挑战——负面事件可产生正面溢出（竞争者渔利），且持久性由 salience 决定（危机被记得时存在、热度退去即消失）"
  tied_at:
    - "Intro P2-P3：假设解构——'类别成员资格 ≠ associability'、'溢出持久性未被检验'"
    - "Intro P4：valence 反转缺口——多数研究负向溢出，仅 1 篇正向且方法有局限"
  untied_at:
    - "Theory：associability（§2.1——类别关联性机制）+ salience（§2.2——认知可得性/持久性机制）"
    - "Results：三向交互（Salience × Same category × Geographic proximity 正，p=.06）——渔利的完整条件"
  antagonist: "文献的 valence 单向假设（负面事件 → 负面后果不言自明）+ associability/salience 两个隐含前提"
  antagonist_built_by:
    - "P2-P3 逐层解构（先拆'类别成员资格即关联性'，再拆'溢出无持久性差异'）"
    - "P4 精确例外（'仅 1 篇研究正向溢出且方法有局限'）"
```

### characters

```yaml
characters:
  protagonist: [Chipotle E. coli 危机 (X，salience 作时变强度), 竞争者的 reputation (Y，周均 Yelp 评分)]
  supporting:
    - "same category（墨西哥餐厅——associability 的类别维度）"
    - "geographic proximity（同邮编——associability 的空间维度）"
    - "salience（新闻计数——可得性/持久性机制）"
  ensemble: [2,672 家西雅图餐厅、24 周窗口（危机前 8/中 8/后 8）、22,137 restaurant-week、Yelp 过滤评论、天气/人口控制]
```

### resolution_logic

`revelation` 揭幕——把"正面溢出"从 valence 单向假设里翻出来：associability × salience 条件化 + 自然实验给因果地位。研究者是翻硬币的人 + 定时器：不仅翻出渔利的一面，还测出这面能亮多久（salience 消退 → 溢出消失——持久性本身就是假设的胜利）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：Epigraph + 反问 Hook（兄弟会欺凌类比——读者参与式）；现象登台"
  rising_action: "假设解构（associability ≠ category membership；持久性未检验）→ valence 反转缺口（多数负向/仅 1 篇正向）→ 论点：associability × salience → 正向溢出；Methods：Chipotle E. coli 西雅图自然实验（2015.10.16-12.1，11 天关店）；DV=周均 Yelp 评分；salience=ABI/INFORM 新闻计数；Heckman 校正无评论周（IMR 不显著→剔除）"
  climax: "Results：三向交互 Salience × Same category × Geographic proximity 正（p=.06）——危机热度 × 同类 × 同区 = 评分上涨 16.3%（3.1→3.6，排名 746→656）——渔利的完整条件揭晓"
  falling_action:
    - "可替换类别检验：fast food / price range 交互全部 n.s.——associability 的特异性（不是任何相似都行，是'同类'才行）"
    - "持久性假设：去掉危机前期重跑——效应仍在且危机期后随 salience 消退消失（'荣誉是借来的'）"
    - "Robustness：LIWC 情感 DV（Janis-Fadner 系数）、距离半径敏感性（>5 英里消失）、Heckman 纳入"
  denouement: "Discussion：理论贡献——负行为→正效应的条件与持久性；认知可得性理论的应用；直接测量声誉（Yelp 评分）；limitations（单一事件、单一城市）"
```

### stakes

```yaml
stakes:
  theoretical: "声誉溢出文献默认 valence 单向——不挑战，'负面事件何时反而利他'不可见；associability 与 salience 的隐含假设使溢出机制停在粗粒度"
  practical: "危机公关的竞争视角：同行危机中该规避关联还是借机凸显？——关联性把你拉进泥潭还是送上海岸，取决于危机是否被记得"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 负向溢出故事 — '负面事件拖累竞争者'（文献惯例）"
  - "讲法B: 无溢出/null — '危机只在当事企业内部消化'"
  - "讲法C: 当事人故事 — '被危机企业如何自救'（换主角：研究 Chipotle 而非竞争者）"
  - "本文: 正向溢出 + 条件 + 持久性 — 负面事件可让竞争者渔利（associability × salience），且荣誉随热度消退。选择理由：valence 反转是标题级反直觉；自然实验给因果地位；持久性把'何时'扩展为'多久'——贡献从发现升为条件+时限"
```

### storytelling_tools

```yaml
storytelling_tools:
  human_face: "Qdoba 顾客的真实评论（'Didn't start regularly going here until the Chipotle E. coli crisis... No E. coli'——正面溢出的消费者声音）；兄弟会类比（Epigraph+反问）"
  rhetorical_question: "P1 反问 Hook（读者自我确认）"
  pacing_notes: "P2-P3 慢速解构 → P4 例外收窄 → P5 论点+预览 → climax 三向交互 → falling 特异性/持久性/稳健性（先给条件再给边界）"
  showing_telling: "Qdoba 引语（showing——渔利者的声音）；3.1→3.6 星、746→656 名（telling——溢出的幅度）；三向交互图"
  voice: "待补"
```

### cross_paper_notes

- **assumption-flip 首独立故事层原型**：与 section 家族 02-implicit-assumption-wrong 变体D（效价反转例外型）互证——故事层判定与 section 变体分类一致，双通道成立。
- **与 Pollock 2015 / Han 2024（reputation 家族三篇）**：纠缠（2015）/ 区分（2024）/ 翻转（2020）——同作者群（Pollock 参与两篇）、同构念家族三故事。
- **与 Cutolo 2024（反转家族）**：cutolo 反转惩罚共识（叙事缓解）；paruchuri2020 反转 valence 假设（负面事件→正面溢出）——'共识反转'的两种切法。
