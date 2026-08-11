# Story Blueprint — Haunschild, Polidoro & Chandler (2015) Organization Science

## 文件头

```yaml
id: haunschild2015
paper: "Haunschild, Polidoro & Chandler (2015, OrgSci) — Organizational Oscillation Between Learning and Forgetting: The Dual Role of Serious Errors"
paper_type: quantitative   # 定性（NASA Challenger/Columbia）+ 定量（制药面板）混合
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（memory methods/results + parsed 全文）→ ROBUST
source_records: [project_mvp30_haunschild2015_methods_results, parsed full text]
vault_reports:
  intro: null（parsed 全文回读）
  methods_results: "（memory 记录：NASA 定性 + 制药量化面板、负二项计数模型——2026-08-09 前已蒸馏）"
  story_arc: null
corpus_links:
  write-introduction: "'why they might change back'（振荡反问）+ Challenger/Columbia 双灾难开场——路径待验证"
  write-methods: "NASA 定性 + 制药 1997-2004 定量混合 + 负二项——已入 write-methods（memory 记录）"
  write-results: "振荡确认（learn→forget→learn）+ errors 双角色——路径待验证"
```

## Story

### one_liner

> 组织会学习也会遗忘——但为什么学了会**退回**？Challenger 事故后 NASA 修正了问题，却再次发生 Columbia——严重错误的**双角色**：既把组织推向安全焦点、又把它拉离效率/创新焦点——学习后遗忘、遗忘后再学——组织的振荡循环。

### knot

```yaml
knot:
  primary_type: consensus-puzzle         # 第七原型：'学习=累积'共识 vs 学习/遗忘振荡（'learning, then forget; then learn, then forget again'）
  compound_types: []                    # errors 双角色是机制，非子类型
  statement: "学习曲线传统——累积经验→改进（'learning curves show substantial variation' 但隐含累积假设）；组织振荡——
              'organizations learn, then forget; then learn, then forget again'——严重错误的双角色：把组织推向安全焦点
              同时拉离效率/创新焦点——时间推移后遗忘进程（虚假安全感/人员流动）让替代焦点回归→再次错误"
  tied_at:
    - "Intro：Challenger/Columbia 双灾难（'How could this happen to an organization, NASA, that employs some of the country's best minds?'——学了为何退回）→ 'learning theory has not dealt with this sequential phenomenon in a systematic way'"
    - "Theory：errors 双角色（推安全/拉效率创新）+ 遗忘进程（虚假安全感/人员流动）"
  untied_at:
    - "Theory H1-H4：振荡 + 后果"
    - "Results：振荡确认（制药 1997-2004——learn→forget 循环）"
  antagonist: "学习理论的累积假设（学习曲线传统——学了就累积——振荡未理论化——'not dealt with in a systematic way'）"
  antagonist_built_by:
    - "Challenger/Columbia 反问（'How could this happen... best minds?'——学了为何退回的震撼）"
    - "'learning, then forget; then learn, then forget again'（振荡的循环表述）"
    - "errors 双角色排布（'push firms toward a focus on safety while also pulling them away from other foci'——推拉对称）"
```

### characters

```yaml
characters:
  protagonist: [serious errors（X——双角色触发器）, safety focus oscillation（DV——学习/遗忘循环）]
  supporting:
    - "双角色机制（推安全——'we will not launch until proved safe'；拉效率/创新——'we will launch unless it is proved unsafe'）"
    - "遗忘进程（虚假安全感/人员流动——时间推移后安全焦点衰减）"
    - "资源约束（'resources devoted to one activity cannot be devoted to another'——焦点转移的根本张力）"
    - "NASA Challenger/Columbia（定性——极端案例）"
  ensemble: [NASA Challenger/Columbia 定性 + 制药 1997-2004 定量、负二项计数模型、安全/创新焦点测量]
```

### resolution_logic

`revelation` 揭幕（揭幕振荡机制——errors 双角色 + 遗忘进程——"学了为何退回"的循环地图）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：Challenger/Columbia 双灾难（'corrected in the immediate aftermath... only to resurface and ultimately cause the Columbia accident'）→ 'why might they change back' → 学习理论未系统处理振荡"
  rising_action: "errors 双角色理论（推安全/拉效率创新——'we will not launch until proved safe' vs 'we will launch unless it is proved unsafe'）+ 遗忘进程（虚假安全感/人员流动）+ Methods（NASA 定性 + 制药 1997-2004 负二项）"
  climax: "Results——振荡确认：制药企业 learn→forget 循环（'confirm our theory'——学习、遗忘、再学、再忘的循环实证）"
  falling_action:
    - "errors 双角色验证（安全焦点上升 + 效率/创新焦点下降——资源约束的推拉）"
    - "遗忘进程（时间推移后安全焦点衰减——虚假安全感/人员流动）"
    - "振荡后果（焦点转移影响后续创新与错误——'shifts in foci subsequently affect innovation and future organizational errors'）"
  denouement: "Discussion——振荡机制（学习与遗忘的循环——'a mechanism by which organizations learn, then forget; then learn, then forget again'）；
              双角色理论贡献（'this dual effect has not previously been theorized'）；
              管理的安全启示（虚假安全感的危险）"
```

### stakes

```yaml
stakes:
  theoretical: "学习理论未解释振荡——'why they might change back'——学与忘如何结合制造连续错误"
  practical: "Challenger/Columbia 双灾难（学了为何退回——NASA 教训）；制药安全焦点振荡（消费者安全）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 学习曲线版——累积经验→改进（学习传统——'substantial variation' 未解释）"
  - "讲法B: 遗忘文献版——组织遗忘（Martin de Holan & Nelson——遗忘过程——不接振荡）"
  - "讲法C: 单案例版——只做 NASA Challenger（灾难案例研究——不接定量验证）"
  - "本文: 振荡揭幕版——learn→forget→learn（errors 双角色 + 遗忘进程——NASA 定性 + 制药定量混合）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "NASA Challenger/Columbia（双灾难——'some of the country's best minds' 的困惑——具名事件+人性化）；'we will not launch until proved safe' vs 'we will launch unless it is proved unsafe'（两条口号的对立意象）"
  rhetorical_question: "核心反问（'How could this happen to an organization, NASA, that employs some of the country's best minds?'——震撼性反问）"
  pacing_notes: "双灾难开场→振荡困惑→双角色理论→遗忘进程→混合方法；climax=振荡确认；falling action 双角色+遗忘+后果"
  showing_telling: "'we will not launch until proved safe' vs 'we will launch unless it is proved unsafe'（两条口号的对立——安全/效率焦点的具象）；'oscillation'（振荡意象）；'resurface'（问题重现意象）"
  voice: "OrgSci 理论口吻；'Intriguingly'（困惑标记）；'How could this happen'（震撼反问）"
```

### cross_paper_notes

- **consensus-puzzle 七原型（学习/遗忘振荡）**：pontikes/cutolo/gamache/kundro/han2020/fang2025/**haunschild2015**——'学习=累积'共识被振荡违背。
- **recall 学习家族三连（跨三类型）**：haunschild2004（源头——volition 学习——paradigms-at-war）→ kalaignanam2013（学习后果——neglected-arena）→ haunschild2015（振荡——consensus-puzzle）——学习家族谱系完整。
- **recall 现象域二十讲法**（学习振荡 +1）。
- **与 haunschild2004 的同作者对照（Haunschild 系）**：2004（volition 学习——正面学习）↔ 2015（振荡——学了会退）——同作者同主题的深化。
- **判别器记录**：consensus-puzzle 判定基于学习曲线的累积共识 vs 振荡违背（原文锚：'learning theory has not dealt with this sequential phenomenon in a systematic way'）。
