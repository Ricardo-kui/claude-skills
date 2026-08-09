# Story Blueprint — Lovelace, Bundy, Pollock & Hambrick (2021) AMJ

## 文件头

```yaml
id: lovelace2021
paper: "Lovelace, Bundy, Pollock & Hambrick (2021, AMJ) — The Push and Pull of Attaining CEO Celebrity: A Media Routines Perspective"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（vault 报告 + 全文回读）→ ROBUST
source_records: [vault narrative/methods_results 报告, parsed full text]
vault_reports:
  intro: "narrative_analysis/mvp30/lovelace2021_ceo_celebrity_amj_narrative.md"
  methods_results: "narrative_analysis/methods_results/mvp30/methods/lovelace2021_ceo_celebrity_methods_narrative.md + results/... + deep_distillation/papers/... + fine_grained/batch_01_lovelace2021_pontikes2012/... + mvp30/_pilot_lovelace2021_amj_methods_results_skeleton.md（报告齐全）"
  story_arc: null
corpus_links:
  write-introduction: "后果→前因缺口（'Over the past two decades... However, apart from...'）+ 错误假设解构（浪漫领导力——'This void may be due to an assumption that...'）——路径待验证"
  write-methods: "序数 ordinal 测量（多媒体：报纸/杂志/广播/在线/Wikipedia）+ ordered probit——路径待验证"
  write-results: "序数边际效应（B-list/A-list 分列）+ H4 不支持诚实报告——路径待验证"
```

## Story

### one_liner

> CEO celebrity 研究做了二十年后果，前因被忽略——因为一个隐含假设：celebrity 逻辑上归于最佳绩效 CEO（浪漫领导力）。但绩效只是 celebrity 的次要预测因子。真实机制是媒体惯例的 push-pull：记者把"戏剧性"的 CEO 拉进聚光灯（非从众战略 + 人口学非典型——女性/有色人种），CEO 自我推广把自己推进聚光灯——而自我推广对非典型 CEO 冲 A-list 格外有效。

### knot

```yaml
knot:
  primary_type: assumption-flip         # 第四原型：浪漫领导力前提翻转（celebrity=绩效奖励 → 媒体惯例机制）
  compound_types: [neglected-arena]     # 前因空白（后果文献做了 20 年、前因没人做）
  statement: "CEO celebrity 研究默认'celebrity 逻辑上归于最佳绩效 CEO'（浪漫领导力——'journalists fall prey to the romance of
              leadership'）；但'company performance is only a minor predictor of CEO celebrity'——前提被否定——真机制=
              媒体惯例：记者拉入（非从众战略/人口学非典型）+ CEO 自我推进（push-pull 理论）"
  tied_at:
    - "Intro P2：后果→前因缺口 → 错误假设解构（'This void may be due to an assumption that...'——'Such an assumption, though, is at odds with the reality that...'）"
    - "Intro P3-P5：media routines 框架 + push/pull 双通道"
  untied_at:
    - "Theory H1-H5：pull ×2 + push + push×pull"
    - "Results：三主效应支持（非从众 0.18/非典型 0.60/自我推广 0.11）+ 绩效不显著 + H5 分叉（0.31）"
  antagonist: "浪漫领导力假设（celebrity=绩效奖励——'journalists fall prey to the romance of leadership'）"
  antagonist_built_by:
    - "缺口追溯至假设（'This void may be due to an assumption that...'——问题化引擎）"
    - "'Such an assumption, though, is at odds with the reality that company performance is only a minor predictor'（实证否定）"
    - "'fall prey to'（批评性措辞——记者的归因偏差）"
```

### characters

```yaml
characters:
  protagonist: [media routines（机制透镜）, CEO celebrity（DV——ordinal：noncelebrities/B-list/A-list）]
  supporting:
    - "strategic nonconformity（pull 1——非从众战略：0.18, p<.01）"
    - "demographic atypicality（pull 2——人口学非典型——女性/有色人种：0.60, p<.05）"
    - "self-promotion（push——自我推广：0.11, p<.05；×非典型 0.31, p=.05——冲 A-list）"
    - "journalists（gatekeepers——惯例执行者：'cannot possibly highlight every CEO'）"
  ensemble: [纵向 CEO 样本、多媒体测量（报纸/杂志/广播/在线/Wikipedia）、Musk/Bezos/Legere（具名案例）、Don Roca 引语（'A-list and B-list'）]
```

### resolution_logic

`revelation` 揭幕（揭幕媒体惯例的造星机制——push-pull 双通道——谁被拉入聚光灯、谁自己推进聚光灯）+ 序数概念化（B-list/A-list 分级揭晓 celebrity 的内部结构）。

### five_acts

```yaml
five_acts:
  exposition: "Intro P1-P2：后果→前因缺口（'Over the past two decades... However, apart from Hayward 2004...'）→ 错误假设解构（浪漫领导力——绩效只是次要预测因子）→ RQ（'Why do some CEOs become celebrities, while others with seemingly equal accomplishments do not?'）"
  rising_action: "Intro P3-P7（media routines + push-pull 理论 + 序数概念化 [Don Roca 引语] + 多媒体测量 + 三贡献）+ Theory（pull ×2 + push + push×pull）+ Methods（纵向 CEO 样本、ordinal measure：top quartile/A-list top 10%/B-list next 15%）"
  climax: "Results——三主效应揭晓：非从众战略（0.18, p<.01）+ 人口学非典型（0.60, p<.05）+ 自我推广（0.11, p<.05）都驱动 celebrity——**绩效不显著**（浪漫领导力前提被实证否定——基线验证）"
  falling_action:
    - "H4 不支持（自我推广×非从众 n.s.——诚实报告）"
    - "H5 支持（自我推广×非典型 0.31, p=.05——高自我推广下非典型 CEO 冲 A-list——Figure 1 分叉：A-list 升 B-list 降）"
    - "序数稳健性（4 类 C-list 检验——B/A 无差异确认两级合适——'degree of celebrity attainment' 概念验证）"
    - "二分类敏感性（binary 丢失交互效应——序数概念化的必要性实证——'important nuances in our findings are lost'）"
  denouement: "Discussion——回到开头：celebrity 不是绩效奖励而是媒体惯例的产物（谁有戏剧性、谁配合生产——'the primary
               question is not which people are the most deserving of examination, but which are the most appealing'）；
               push-pull 双通道；序数测量方法贡献（多媒体——Wikipedia reads/edits 等创新指标）"
```

### stakes

```yaml
stakes:
  theoretical: "celebrity 前因被忽视——浪漫领导力假设未检验——'celebrity 归于绩效'的错误归因；binary 概念化丢失序数信息"
  practical: "董事会/投资者理解 celebrity 的来源（非绩效——非从众/非典型/自我推广）；女性与有色人种 CEO 的 celebrity 获得机制"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 后果研究版——celebrity 的后果（20 年文献主流——薪酬/董事会席位/免解职/企业受损）"
  - "讲法B: 浪漫领导力版——celebrity=绩效奖励（隐含假设——本文实证否定）"
  - "讲法C: 单媒体测量版——只做报纸/奖项测量（binary——序数信息丢失——敏感性检验证实）"
  - "本文: 前提翻转+前因拓荒版——媒体惯例 push-pull（绩效前提被否定 + 序数概念化 + 多媒体测量）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "Elon Musk（Tesla 电池投资）、Jeff Bezos（Amazon 机器人/垂直整合）、John Legere（T-Mobile 病毒营销）——具名 CEO 三连；Don Roca 引语（'It's a pyramid'——好莱坞分级）"
  rhetorical_question: "RQ 反问（'Why do some CEOs become celebrities, while others with seemingly equal accomplishments do not?'——'it is essential to ask'）+ 'This begs the question'（第二问句）"
  pacing_notes: "后果→前因→假设解构→RQ；push-pull 双通道理论；climax=三主效应揭晓+绩效不显著；falling action H4 不支持+H5 分叉+序数稳健性"
  showing_telling: "Hollywood 类比（A-list/B-list——'cumulative knowledge or awareness'——Don Roca 引语）；'push-pull'（力学隐喻）；'fall prey to'（批评措辞）"
  voice: "理论发展口吻；'fall prey to the romance of leadership'（对隐含假设的批评）；'apart from... paid little attention'（精确缺口）"
```

### cross_paper_notes

- **assumption-flip 四原型**：paruchuri2020（valence 方向）/ shipilov2020（负面偏好）/ hahl2017（distinction 动机）/ **lovelace2021（浪漫领导力——celebrity=绩效奖励前提）**。
- **celebrity 家族五篇成型（Pollock 系四篇）**：pfarrer2010（声誉 vs 名人区分——形成机制）↔ han2024（reputation vs celebrity 后果 2×2）↔ paruchuri2020（负面事件溢出）↔ lovelace2021（**前因——获得过程**）——pfarrer/paruchuri/han2024/lovelace 均 Pollock 参与。
- **与 han2024 的 celebrity 前因双视角**：han2024 用 celebrity 作 scandalization 的 DV 前因；lovelace 做 celebrity 本身的前因。
- **media routines 家族 2 例**：han2020（丑闻化情境）↔ lovelace2021（造星过程）——同一透镜两个故事。
- **判别器记录**：assumption-flip 判定基于隐含前提（浪漫领导力）被实证否定（绩效不显著——基线验证）。
