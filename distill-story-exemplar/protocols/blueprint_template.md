# Story Blueprint 填充模板

> 字段权威定义见 `../story-blueprints/_schema.md`（含 knot 类型表）。本模板是生成 blueprint 时的填充骨架。全部字段中文描述，YAML 键保持英文。

```markdown
# Story Blueprint — <作者> (<年份>, <期刊>)

## 文件头

```yaml
id: <kebab-case>
paper: "<作者 (年份), 期刊> — <标题>"
paper_type: <quantitative / qualitative / theory>   # 见 _schema.md；定性/理论按 Fig 2.3/2.4 overlay
distilled_sections: [intro, theory, methods, results]   # 缺失区段 → 对应五幕字段标待补
source_records: [<memory 文件名 / distill 产物>]
vault_reports:   # Phase 0 vault 检索结果（narrative_analysis/ 下的报告路径）
  intro: "<introduction/mvp30/fine_grained/.../<key>*distilled_introduction.md 或 null>"
  theory: "<theory/mvp30/fine_grained/.../<key>*distilled_theory.md 或 null>"
  methods_results: "<methods_results/mvp30/fine_grained/batch_*/... 或 deep_distillation/papers/... 或 null>"
  story_arc: "<_story_arcs/<key>_story_arc.md 或 null>"
corpus_links:
  write-introduction: "<目录>/<变体名> 变体X（<一句话说明>）"
  write-theory: "..."
  write-methods: "..."
  write-results: "..."
```

## Story

### one_liner

> <一句话故事：冲突与解法，不是发现>（= GBL 2007 theorized storyline：贯穿全文的理论主张线，读者读完能复述的那句话——区别于 Pollock storylines 的构念旅程）

### knot

```yaml
knot:
  primary_type: <类型表之一>
  compound_types: [<子结构>]
  statement: "<含冲突双方的一句话>"
  tied_at: [<系紧位置：intro 模块 / theory 段落>]
  untied_at: [<解开位置：theory 假设 / results 位置>]
  antagonist: "<反派是谁>"
  antagonist_built_by: ["<构造反派的修辞手法>"]
```

### characters

```yaml
characters:
  protagonist: [<主角构念>]
  supporting: ["<配角及其故事功能>"]
  ensemble: [<群演>]
```

### resolution_logic

<解法性格 + 一句话说明：仲裁拆地整合 / 揭幕换视角 / 拓荒补战场…>

### five_acts

```yaml
five_acts:
  exposition: "<Intro（+theory 前段）：证据位置>"
  rising_action: "<Theory + Methods：张力蓄积与 arena 搭建>"
  climax: "<Results 开头：第一揭晓位置>"
  falling_action: ["<解开 + 反转/稳健/补充，逐个列>"]
  denouement: "<Discussion：回到开头、收口>"
```

### stakes

```yaml
stakes:
  theoretical: "<理论 stakes>"
  practical: "<实践 stakes>"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: <版本名> — <一句话讲法>（<谁讲过/谁可能这么讲>）"
  - "本文: <所选版本> — <选择理由>"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "<具体 actor / 案例 / 场景；无则待补>"
  rhetorical_question: "<修辞问位置与功能>"
  pacing_notes: "<节奏决策：climax 落点、反转数、节长、多研究起伏>"
  showing_telling: "<图解/比喻等 showing 手段>"
  voice: "<对话语气特征>"
```

### cross_paper_notes

<与现有 blueprints 的对照：同对角线不同故事 / 同设计不同故事 / 同现象域不同讲法；无则写"暂无对照对">
