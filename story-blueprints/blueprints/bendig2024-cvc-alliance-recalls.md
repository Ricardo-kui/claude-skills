# Story Blueprint — Bendig, Hensellek & Schulte (2024)

## 文件头

```yaml
id: bendig2024
paper: "Bendig, Hensellek & Schulte (2024) — Beneficial, Harmful, or Both? Effects of Corporate Venture Capital and Alliance Activity on Product Recalls"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（Clippings 全文回读）→ ROBUST
source_records: [parsed full text（Clippings——检索协议路径命中）]
vault_reports:
  intro: null（无 vault 报告——Clippings 全文回读）
  methods_results: null（无 vault 报告——全文回读：75 FDA S&P 500 公司 2009-2017、GEE、U-test）
  story_arc: null
corpus_links:
  write-introduction: "标题三选一问句（'Beneficial, Harmful, or Both?'）+ CVC 数据 Hook（$169.3B 记录投资）——路径待验证"
  write-methods: "GEE（Wowak 2015 规格）+ U-test（Haans 三标准/Fieller）——路径待验证"
  write-results: "倒 U 揭晓（CVC −.021/联盟 −.071 平方项）+ 市场动荡调节——路径待验证"
```

## Story

### one_liner

> 外部风险投资被当作创新资本（RBV 共识——"attain ends they could not achieve alone"），但 meta-analysis 显示效果暧昧（mixed findings 无根因）——本文用产品召回作为后果揭晓根因：CVC 与联盟活动与召回概率呈**倒 U**——"不做或大做受益、stuck-in-the-middle 最差"——资源基础学习视角（经验学习曲线抵消成本）；市场动荡下 CVC 需更多交易、联盟更少。

### knot

```yaml
knot:
  primary_type: paradigms-at-war        # 第五原型：beneficial vs harmful 两阵营——倒 U 裁决（与 zhou2017 同款"倒 U 裁决"）
  compound_types: []                    # 倒 U 是裁决方式，非子类型
  statement: "外部风险投资两阵营——RBV 正面派（CVC/联盟=创新资本——'attain ends they could not achieve alone'）vs 暗面派
              （meta-analysis ambiguous——Huang & Madhavan——50-70% 联盟失败率——'we lack theoretical knowledge about these
              negative impacts and their root causes'）；本文用召回裁决：CVC/联盟与召回概率倒 U——不做/大做受益、
              stuck-in-the-middle 最差——mixed findings 的根因=非线性"
  tied_at:
    - "Intro：CVC 数据 Hook（$169.3B 记录投资 2021/KPMG 56% CEO）→ RBV 共识 → 暗面（meta-analysis ambiguous）→ 'root cause for the mixed prior findings'"
    - "Theory：RBV + learning（problemistic search）+ 倒 U 理论"
  untied_at:
    - "Theory H1-H4：倒 U ×2 + 市场动荡调节 ×2"
    - "Results：倒 U 确认（CVC 平方 −.021, p<.05/联盟平方 −.071, p<.05）+ U-test + 调节"
  antagonist: "外部风险投资的 mixed findings（正面派与暗面派各自为证——无根因理论）"
  antagonist_built_by:
    - "RBV 共识建立（'attain ends they could not achieve alone, or at least not as quickly'——Grunwald & Kieser 引语）"
    - "暗面证据排布（meta-analysis ambiguous——50-70% 失败率——'dark side of external venturing'）"
    - "标题三选一问句（'Beneficial, Harmful, or Both?'——直接呈现两派）"
```

### characters

```yaml
characters:
  protagonist: [CVC activity + alliance activity（X——双模式）, product recall likelihood（DV）]
  supporting:
    - "RBV + learning（透镜——problemistic search——经验学习曲线）"
    - "market turbulence（调节——环境条件——CVC × turbulence 平方 −.049, p<.01/联盟 × turbulence 平方 −.278, p<.001）"
    - "mixed findings 根因（问题——'a potential root cause for the mixed prior findings'）"
    - "FDA 药物召回（情境——75 家受监管公司）"
  ensemble: [75 FDA S&P 500 公司 2009-2017、GEE（Wowak 2015 规格）、U-test（Haans 三标准/Fieller）、CPSC 扩展样本 125 公司]
```

### resolution_logic

`arbitration` 仲裁（**倒 U 裁决**——与 zhou2017 同款裁决工具——两阵营各对一半：正面派对了低强度/大强度区间、暗面派对了中等区间）+ 市场动荡条件化。

### five_acts

```yaml
five_acts:
  exposition: "Intro：CVC 数据 Hook（$169.3B 记录投资 2021/KPMG 56% CEO 认为联盟是增长基石）→ RBV 共识（创新资本）→ 暗面（meta-analysis ambiguous——50-70% 联盟失败率——'dark side of external venturing'）→ 'root cause for the mixed prior findings'"
  rising_action: "RBV + learning 理论（problemistic search——Greve 学习曲线）+ 倒 U 理论（CVC/联盟 × 召回）+ Methods（75 FDA S&P 500 公司 2009-2017、GEE、U-test 三标准）"
  climax: "Results——倒 U 揭晓：CVC 平方项 −.021, p<.05/联盟平方项 −.071, p<.05——'either no or rather bold external resource-seeking seems to pay off more than small-scale stuck-in-the-middle initiatives'"
  falling_action:
    - "H3/H4 市场动荡（CVC × turbulence 平方 −.049, p<.01/联盟 × turbulence 平方 −.278, p<.001——动荡下 CVC 需更多交易、联盟更少——高联盟动荡下召回归零）"
    - "U-test 确认（Haans 三标准全部满足——斜率低端正/高端负 + Fieller 区间）"
    - "稳健性六重（2-4 年滞后/召回计数/泊松 FE/CPSC 扩展 125 公司/2SLS 行业工具/交易价值替代）"
  denouement: "Discussion——RBV 资源难转移（Barney——'strategically important resources are indeed hard to transfer'）；经验学习曲线
               （Greve——greater external search offsets costs）；'stuck-in-the-middle' 的管理教训（适中风险投资最差）"
```

### stakes

```yaml
stakes:
  theoretical: "外部风险投资的 mixed findings 无根因——'we lack theoretical knowledge about these negative impacts and their root causes'——非线性的缺失"
  practical: "风险投资活动的消费者后果（FDA 药物召回——公众伤害）；'stuck-in-the-middle' 的实践教训（要么不做要么大做）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 风险投资收益版——CVC/联盟→创新/价值（RBV 主流——'attain ends they could not achieve alone'）"
  - "讲法B: 风险投资暗面版——只做负面后果（meta-analysis ambiguous——无根因）"
  - "讲法C: 专利输出版——CVC/联盟→专利（innovation output 主流——Marhold 等）"
  - "本文: 倒 U 裁决版——不做/大做受益、适中最差（recall 作为根因后果——市场动荡调节）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "数据型（CVC $169.3B 记录投资/KPMG 56% CEO——无具名企业）；FDA 药物召回情境（75 公司集体角色）"
  rhetorical_question: "标题即问句（'Beneficial, Harmful, or Both?'——三选一问句——标题问句家族第 5 例——新变体）"
  pacing_notes: "数据 Hook→RBV 共识→暗面→倒 U 理论→U-test 三标准；climax=倒 U 揭晓（平方项双负）；falling action 双调节+U-test+六稳健性"
  showing_telling: "'stuck-in-the-middle'（居中困境意象——'either no or rather bold... pays off'）；'Beneficial, Harmful, or Both?'（标题三选一）；'dark side of external venturing'（暗面术语）"
  voice: "创业研究实证口吻；'dark side'（暗面术语）；'root cause'（根因定位）"
```

### cross_paper_notes

- **paradigms-at-war 五原型（倒 U 裁决家族）**：zhou2017（资源获取/利用→倒U）↔ bendig2024（风险投资→召回倒U）——同款"倒 U 裁决"工具——两阵营各对一半。
- **标题问句家族第 5 例**（三选一型——'Beneficial, Harmful, or Both?'——新变体）。
- **recall 现象域十二讲法**（前因侧第 9——战略风险投资）。
- **与 wowak2015 的 GEE 规格互引**（bendig 直接采用 Wowak 2015 的 GEE 规格——方法谱系）。
- **判别器记录**：paradigms-at-war 判定基于两阵营（beneficial/harmful）+ 倒 U 裁决（各对一半——适中时都不对）。
