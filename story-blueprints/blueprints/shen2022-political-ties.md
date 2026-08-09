# Story Blueprint — Shen, Zhou, Wang & Zhang (2022) JOM

## 文件头

```yaml
id: shen2022
paper: "Shen, Zhou, Wang & Zhang (2022, JOM) — Do Political Ties Facilitate Operational Efficiency? A Contingent Political Embeddedness Perspective"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（vault 报告 + 全文回读）→ ROBUST
source_records: [vault narrative/fine 报告（intro fine + methods/results 全报告）, parsed full text]
vault_reports:
  intro: "narrative_analysis/mvp30/shen2022_political_ties_operational_efficiency_jom_narrative.md + introduction/mvp30/fine_grained/batch_2026-05-21/shen2022_JOM_distilled_introduction.md"
  methods_results: "narrative_analysis/methods_results/mvp30/methods/shen2022_political_ties_methods_narrative.md + results/... + deep_distillation/papers/... + fine_grained/batch_10_zhao2022_shen2022/...（报告齐全）"
  story_arc: null
corpus_links:
  write-introduction: "Construct-first Hook（operational efficiency 定义）+ 实践悖论（conventional wisdom vs dark side）——路径待验证"
  write-methods: "DEA 效率 + PSM + Tobit——路径待验证"
  write-results: "主效应暗面 + 四调节 + 获取/利用双轨机制验证——路径待验证"
```

## Story

### one_liner

> 新兴经济体管理者把政治纽带当作获取稀缺资源的策略（conventional wisdom），但运营效率是"如何使用资源"而非"拿到资源"的问题——实证发现政治纽带显著**降低**效率（−.339）：获取成功（补贴/贷款↑）但利用失败（自满/锁定/路径依赖）——两派各对一半：获取派对了、利用派错了；环境四象限决定何时是多余、何时是破坏、何时是双刃剑。

### knot

```yaml
knot:
  primary_type: paradigms-at-war        # 第四原型：zhou 理论仲裁 / wowak 维度分裂 / park 外生冲击 / 本文拆地整合第二例
  compound_types: []                    # 拆地整合（获取/利用分解）是裁决方式，非子类型
  statement: "conventional wisdom——政治纽带帮助新兴经济体企业获取资源（'是否应该追求政治关系'）；dark side 文献警示其负面后果
              ——两阵营相反预测；本文裁决：分解到资源获取（正面）与资源利用（负面）两个 facet——获取成功但利用失败，
              效率净负——环境条件决定净效应"
  tied_at:
    - "Intro P3：实践悖论（conventional wisdom vs dark side——三个问题化任务）"
    - "Intro P4：political embeddedness 论点（获取有利/利用约束）"
  untied_at:
    - "Theory H1：纽带 → 效率下降"
    - "Results：H1 支持（−.339, p<.01）+ 四调节 + 机制双轨验证"
  antagonist: "conventional wisdom（政治纽带=资源获取策略——新兴经济体管理者的默认信念）"
  antagonist_built_by:
    - "实践悖论排布（先呈现 conventional wisdom 再引入 dark side——'是否应该追求政治关系'的实践困惑）"
    - "resource acquisition vs resource utilization 分解（获取环节正面/利用环节负面——两派各对一半）"
    - "'we caution against the dark side'（警示语气）"
```

### characters

```yaml
characters:
  protagonist: [political ties（X）, operational efficiency（DV——DEA）]
  supporting:
    - "resource acquisition vs utilization（分解机制——获取好利用坏：补贴 .277**/贷款 .674** vs ROA/专利 n.s.）"
    - "factor market development（H2——弱化：低市场 −.931 显著/高市场不显著）"
    - "industrial competition（H3——强化：高竞争 −.629/低竞争不显著）"
    - "foreign shareholding（H4——弱化甚至转正：低外资 −.411/高外资 +.946——纽带反变助力）"
    - "customer concentration（H5——弱化：低 −.504/高不显著）"
  ensemble: [中国上市民企 3,410 obs、DEA 效率、PSM（半径/核匹配）、Shandong Molong（具名案例）]
```

### resolution_logic

`arbitration` 仲裁（**拆地整合**——资源获取/利用 facet 分解——与 zhou2017 同款裁决方式；两派各对一半）+ 环境四象限条件化（superfluous/destructive/double-edged sword）。

### five_acts

```yaml
five_acts:
  exposition: "Intro P1-P3：Construct-first Hook（operational efficiency 定义）→ political ties 引入 + RQ → 实践悖论（conventional wisdom vs dark side——是否应追求政治关系）"
  rising_action: "Intro P4-P6（political embeddedness 论点——获取/利用分解 + resource availability 四调节框架 + 中国面板 + 三贡献）+ Methods（3,410 obs、DEA、PSM/Tobit）"
  climax: "Results——H1 揭晓：political ties 显著降低运营效率（b=−.339, p<.01——1.081%）——conventional wisdom 被翻——暗面实证"
  falling_action:
    - "H2 因子市场发育（弱化：低市场 −.931 显著/高市场不显著）"
    - "H3 行业竞争（强化：高竞争 −.629/低竞争不显著）"
    - "H4 外资持股（弱化甚至转正：低外资 −.411/高外资 +.946——纽带反变助力）"
    - "H5 客户集中（弱化：低 −.504/高不显著）"
    - "机制双轨验证（补贴 .277**/贷款 .674**——获取成功；ROA/专利 n.s.——利用失败——'获取好利用坏'实证）"
    - "稳健性（FE、替代测量、PSM 半径/核匹配、加权 Tobit）"
  denouement: "Discussion——四象限框架（Figure 3：superfluous [高市场低竞争]/destructive [双高]/double-edged sword
               [低市场——Red Queen effect]）；外资高时转正（Shandong Molong 具名案例：32.10% 外资、效率 31.26→35.04）；
               管理启示（何时用、如何补救——benchmarking/智力系统/结果控制）"
```

### stakes

```yaml
stakes:
  theoretical: "政治纽带研究只认获取收益——利用环节被忽略；OM 治理文献缺政治纽带维度（商业纽带之外的另一类关系）"
  practical: "新兴经济体管理者是否应追求政治纽带——何时谨慎（四象限）、如何补救（外资/客户结构）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 政治纽带收益版——获取资源的策略（conventional wisdom——新兴经济体默认信念）"
  - "讲法B: 政治纽带暗面版——只讲负面后果（dark side 文献——机制不明）"
  - "讲法C: 商业纽带版——business ties 治理文献（OM 主流——只做商业关系）"
  - "本文: 拆地整合版——获取/利用分解（两派各对一半）+ 环境四象限（何时多余/破坏/双刃剑）+ 补救策略"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "Shandong Molong（具名——32.10% 外资、效率轨迹 31.26→35.04——'政治纽带在特定条件下反变助力'的活案例）"
  rhetorical_question: "标题即问句（'Do Political Ties Facilitate Operational Efficiency?'——标题问句家族第 4 例）"
  pacing_notes: "Construct-first→实践悖论→分解论点→四调节框架；climax=H1 暗面揭晓（−.339——conventional wisdom 被翻）；falling action 四调节+机制双轨+稳健性"
  showing_telling: "四象限框架（Figure 3——superfluous/destructive/double-edged sword）；'Red Queen effect'（隐喻）；
                    'double-edged sword'（双刃剑意象）"
  voice: "JOM 治理口吻；'we caution against the dark side'（警示语气）；'surprisingly, been overlooked'（意外性强调）"
```

### cross_paper_notes

- **paradigms-at-war 四原型（裁决方式演进）**：zhou2017（理论仲裁）↔ wowak2025（维度分裂）↔ park2025（外生冲击）↔ shen2022（**拆地整合第二例**——资源获取/利用分解——与 zhou 同款 facet——"资源获取/利用分解家族"：zhou 得倒U、shen 得"获取好利用坏"）。
- **标题问句家族第 4 例**（"Do...?" 问句——与 eilert2017 的 "Does It Pay to...?" 同型）。
- **中国情境家族**：zhou2017（state ownership）↔ shen2022（政治纽带）——同国情境不同故事。
- **与 wu2025 治理对照**：wu（制度冲击改变行为）；shen（嵌入性暗面损害效率）——"外部治理与嵌入性暗面"。
- **判别器记录**：paradigms-at-war 判定基于两阵营完整立场 + 各对一半裁决（获取派对了、利用派错了）。
