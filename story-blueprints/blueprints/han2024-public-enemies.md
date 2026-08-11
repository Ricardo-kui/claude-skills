# Story Blueprint — Han, Pollock & Paruchuri (2024) SMJ

## 文件头

```yaml
id: han2024
paper: "Han, Pollock & Paruchuri (2024, SMJ) — Public Enemies? The Differential Effects of Reputation and Celebrity on Corporate Misconduct Scandalization"
distilled_sections: [intro, theory, methods, results]      # 2026-08-09 读全文定稿 → ROBUST
source_records: [vault narrative: narrative_analysis/mvp30/han2024_public_enemies_smj_narrative.md]
vault_reports:
  intro: "narrative_analysis/mvp30/han2024_public_enemies_smj_narrative.md"
  theory: "parsed_texts/mvp30/Public enemies...（§2 理论：reputation/celebrity 理性 vs 情感内容）"
  methods_results: "parsed_texts/mvp30/Public enemies...（§3-4：数据泄露 224 起/2 周窗口；RE 负二项）"
  story_arc: null
corpus_links:
  write-introduction: "Framework-Anchored 双构念区分（reputation 理性 vs celebrity 情感，2×2 矩阵）；对角线对称假设结构（H1↔H4 正 / H2↔H3 负）"
  write-results: "平均边际效应（AME）分析（非线性模型交互的正确解释——Busenbark et al. 2022）；对角交叉点检验（reputation vs celebrity 效应差异的显著区间）"
```

## Story

### one_liner

> 文献把 reputation 和 celebrity 当成同一种"社会认可资产"——本文说它们是两种不同的资产，且在不端行为曝光时走向相反：事故越严重，声誉好的公司被报道得越狠（理性评价按事实定罪），明星光环的公司反而被轻轻放下；但关注度越高，光环越被点燃（情感共鸣随热度放大），声誉的作用反而消退。同一个"社会认可"，两种命运，各赢一个维度。

### knot

```yaml
knot:
  primary_type: tangled-constructs   # 双原型（pollock2015 + han2024）
  compound_types: [neglected-arena]   # scandalization 研究关注事后、忽略过程（P2-P3）
  statement: "reputation 与 celebrity 被文献混同为同一种 social approval asset——但二者对 misconduct scandalization 的效应随严重度类型交叉反转：objective severity 高时 reputation 赢（2.20→12.59 篇/日），perceived severity 高时 celebrity 赢（2.50→4.20 篇/日）"
  tied_at:
    - "Intro P4：social approval assets 同一屋顶引入（reputation & celebrity 并置）"
    - "Intro P5：构念混淆缺口——'现有文献未区分不同 social approval assets 的差异效应'"
  untied_at:
    - "Theory §2.1：理性 vs 情感 sociocognitive content 的机制区分（两种资产的内容属性决定交互方向）"
    - "Results：四个交互 + 两个对角交叉点（objective ≥11 时 reputation 超过 celebrity；perceived ≥35.6 篇时 celebrity 超过 reputation）"
  antagonist: "文献的构念混同——reputation 与 celebrity 被当同一种资产（'same roof' 假设），差异效应不可见"
  antagonist_built_by:
    - "P4 同一屋顶引入 → P5 拆开（先立混同再解混同）"
    - "Facebook vs Chegg 对比案例 Hook（相似规模、不同覆盖——混同的后果先露破绽）"
```

### characters

```yaml
characters:
  protagonist: [reputation (X1，理性评价), celebrity (X2，情感光环), scandalization (Y，违规报道日计数)]
  supporting:
    - "objective misconduct severity（账户数——理性维度）"
    - "perceived misconduct severity（累积报道量/可得性级联——情感维度）"
  ensemble: [224 起数据泄露/157 家公司 2015-2018、2 周观察窗口、Factiva 5,118 篇文章（64% 零报道）、TNIC-3 竞争对手池、LIWC 情感测量]
```

### resolution_logic

`revelation` 揭幕——把 celebrity 的情感面从 reputation 的理性面里翻出来：2×2 对角交叉（objective 高→reputation 赢；perceived 高→celebrity 赢）。研究者是拆结人+记分员：同一个屋顶下的两个构念各走各路，且各赢一个条件维度——与 wowak2025 的 dimension-split 家族相似但这里是构念区分（Constructs 贡献）而非 DV 拆维。

### five_acts

```yaml
five_acts:
  exposition: "Intro：Facebook vs Chegg 对比案例 Hook（反差型）；scandalization 定义；'现有研究关注事后，忽略过程'"
  rising_action: "social approval assets 同一屋顶引入 → 构念混淆缺口 → 理论：理性 vs 情感内容（§2.1）+ 双重交互（objective/perceived severity × 两资产）——2×2 矩阵架构；Methods：数据泄露 224 起、2 周窗口、RE 负二项；reputation=Fortune/WSJ 前 50；celebrity=关注量×情感正性（LIWC）+1SD；objective=账户数；perceived=累积报道"
  climax: "Results Table 7：四个交互全部成立——reputation × objective 正（p=.004：低严重度 2.20 n.s. → 高严重度 12.59***）、celebrity × objective 负（4.43 → 1.79）；reputation × perceived 负（6.47 → 2.57）、celebrity × perceived 正（2.50 → 4.20）——对角交叉"
  falling_action:
    - "两个对角交叉点检验：objective ≥ ~60,000 账户（78th pct）后 reputation 显著超过 celebrity；perceived ≥ ~36 篇（96th pct）后 celebrity 显著超过 reputation——'各赢一维度'的精确分界"
    - "Post hoc：兼具两资产的 firm 永远有新闻价值（平线——both 交互不显著）——'high-reputation celebrities' 的违规必然被丑闻化"
    - "RIR 内生性（24.7%/42.3%/53.8%/72.0% 需偏误才能推翻）"
  denouement: "Discussion：超越 social approval assets 的'新sworthiness 角色'——内容属性（理性/情感）决定相对影响；兼具资产的叠加效应；理论+实践含义（危机公关该经营哪种资产）"
```

### stakes

```yaml
stakes:
  theoretical: "social approval assets 文献若继续混同 reputation 与 celebrity，'何种认可保护企业、何种认可招致苛责'不可判定——且 scandalization 的过程视角（如何被丑闻化）缺失"
  practical: "危机公关的资产盘点：事故严重时声誉是双刃（更被报道），关注度高涨时光环是燃料（更被点燃）；兼具两者则必然被丑闻化——'被爱有时比被尊重危险'"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 混同故事 — 'reputation 与 celebrity 是同一种社会认可资产'（文献惯例——本文要解开的结）"
  - "讲法B: 单资产故事 — 只做 reputation 或只做 celebrity（半个 2×2）"
  - "讲法C: 事后惩罚故事 — 只研究 scandal 的后果（scandalization 文献惯例）"
  - "本文: 双构念差异效应 + 对角交叉 — 同一屋顶拆开，两个条件维度各赢一局。选择理由：'differential effects' 标题级承诺；对角交叉点给 2×2 以精确的戏剧性（'从哪一刻起 reputation 让位给 celebrity'）"
```

### storytelling_tools

```yaml
storytelling_tools:
  human_face: "Facebook vs Chegg（对比案例）；具名企业表（Apple/Chipotle/Disney/McDonald's 等——高声誉×明星四象限）；Yahoo! 10 亿账户、Equifax 1.43 亿、Marriott 5 亿（客观严重度的 headline 数字）"
  rhetorical_question: "未见（已核实 2026-08-09：intro 无问句）"
  pacing_notes: "P4 并置 → P5 拆开 → Theory 机制区分 → Results 四交互 + 两交叉点（先给象限再给分界线）——'拆结'节奏"
  showing_telling: "四象限企业表（showing——谁在哪个格）；交叉点数字（telling——精确分界）"
  voice: "we used/we tested/we collected 中性学术语态（已核实 2026-08-09）"
```

### cross_paper_notes

- **与 Pollock 2015（tangled-constructs 双原型，最强对照对）**：同 Pollock 系 reputation 家族——2015 动态共演（age 反转）、2024 静态差异（severity 类型交叉）——'构念纠缠'的系紧与解法空间被钉死。
- **与 Wowak 2025（各赢一维度家族）**：wowak = 同一 X 两极对双 DV 各赢（dimension-split）；han2024 = 双构念对同一 DV 的条件交叉（construct-differentiation）——'各赢一局'的两种实现。
- **与 paruchuri2020（reputation 家族第三篇）**：纠缠/区分/翻转——reputation 家族三篇三故事。
