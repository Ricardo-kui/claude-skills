# Story Blueprint — Haunschild & Rhee (2004) Management Science

## 文件头

```yaml
id: haunschild2004
paper: "Haunschild & Rhee (2004, MgmtSci) — The Role of Volition in Organizational Learning: The Case of Automotive Product Recalls"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（OCR 全文回读）→ ROBUST
source_records: [OCR parsed full text]
vault_reports:
  intro: null（OCR 全文回读）
  methods_results: null（OCR 全文回读：美国汽车业 1966-1999、学习曲线传统）
  story_arc: null
corpus_links:
  write-introduction: "'Do we learn more when we choose to or when we are told to?'（学习问句）+ volition 两派冲突——路径待验证"
  write-methods: "学习曲线传统（voluntary/involuntary 召回→后续召回率）——路径待验证"
  write-results: "voluntary 学更多 + generalist/specialist 条件——路径待验证"
```

## Story

### one_liner

> 组织学习是"自愿学得多"还是"被告知学得多"？两派理论冲突（volition 派：自主→承诺；mandate 派：外部冲击→深度探索）——汽车业实证裁决：**自愿召回带来更多学习**（后续非自愿召回减少——非自愿召回的学习更浅）；组织形态（generalist/specialist）调节——volition 是被忽视的学习决定因素。

### knot

```yaml
knot:
  primary_type: paradigms-at-war        # 第六原型：volition vs mandate 两派——conflicting answers——实证裁决偏向 voluntary + 形式条件化
  compound_types: []                    # 裁决方式=实证偏向 + 组织形态条件化
  statement: "组织学习两派——volition 派（自主→承诺→深层学习——'when decisions are imposed... greater resistance and poorer decision quality'）
              vs mandate 派（外部强制→冲击→克服惯性——'external pressures act as jolts'）——'existing literature provides conflicting
              answers'——汽车业实证裁决：自愿召回→更多学习（后续非自愿召回减少——非自愿学习更浅）；generalist/specialist 调节"
  tied_at:
    - "Intro：'What is the role of volition in organizational learning? Do firms learn better in response to internal procedures or external mandates?'（核心问句）→ 'Existing literature provides conflicting answers'"
    - "Theory：volition 派（Marcus & Nichols——自主承诺）vs mandate 派（Ocasio——注意力/冲击）"
  untied_at:
    - "Theory H1-H4：voluntary 学习 + generalist/specialist"
    - "Results：voluntary→更多学习（后续非自愿召回减少）+ generalist/specialist 条件"
  antagonist: "学习理论对 volition 的沉默（'an important, yet understudied, determinant of the rate and effectiveness of learning——volition'）"
  antagonist_built_by:
    - "核心问句（'Do we learn more when we choose to or when we are told to?'——通俗化表达）"
    - "两派冲突排布（volition 派 vs mandate 派——'conflicting answers'——各持完整理论）"
    - "学习曲线传统承接（cumulative production experience→改进——学习效果测量的传统）"
```

### characters

```yaml
characters:
  protagonist: [recall volition（X——voluntary vs involuntary）, subsequent recall rates（DV——学习效果）]
  supporting:
    - "volition 机制（自主→承诺→永久改变——'more permanent change to the organization's routines'）"
    - "mandate 机制（外部强制→防御性反应——'shallower learning processes'）"
    - "organizational form（generalist vs specialist——学习过程的组织形态条件）"
    - "NHTSA（强制者——involuntary 召回的执行者）"
  ensemble: [美国汽车业 1966-1999 全部召回、学习曲线传统、voluntary/involuntary 分类、generalist/specialist]
```

### resolution_logic

`arbitration` 仲裁（实证裁决——volition 派胜出但部分——organizational form 条件化——两派各对一部分）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：'What is the role of volition in organizational learning? Do firms learn better in response to internal procedures or external mandates?'→ 'Existing literature provides conflicting answers'（volition 派 vs mandate 派）"
  rising_action: "volition 派理论（Marcus & Nichols——自主承诺）+ mandate 派理论（Ocasio——外部冲击）+ Methods（美国汽车业 1966-1999 全部召回、学习曲线传统）"
  climax: "Results——裁决揭晓：自愿召回→更多学习（后续非自愿召回减少——'voluntary recalls result in more learning than mandated recalls'）——volition 派胜出"
  falling_action:
    - "非自愿学习更浅（'at least partly because of shallower learning processes that result from involuntary recalls'）"
    - "organizational form 条件（generalist/specialist 学习不同——'the effect of volition... is different for generalist and specialist automakers'）"
    - "稳健性"
  denouement: "Discussion——volition 是被忽视的学习决定因素（'an important, yet understudied, determinant'）；
              政策含义（政府强制召回 vs 自愿召回的监管设计——'policy regarding the government enforcement of product recalls'）；
              学习曲线传统的扩展（经验→误差减少——'The effects of experience on error reduction have not been studied'）"
```

### stakes

```yaml
stakes:
  theoretical: "volition 在学习理论中未研究——'What is the role of volition in organizational learning?'——学习率变异的一个来源"
  practical: "政府召回执法政策（强制 vs 自愿的监管设计）；汽车安全（学习→后续召回减少）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 学习曲线版——累积生产经验→改进（学习传统——'substantial variation' 未解释来源）"
  - "讲法B: 强制学习版——外部强制促进学习（mandate 派——Marcus 1988 核电站）"
  - "讲法C: 召回后果版——召回的市场/声誉后果（recall 文献主流——不接学习）"
  - "本文: volition 裁决版——自愿 vs 强制（两派冲突实证裁决——voluntary 学更多 + generalist/specialist 条件）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "无具名企业（汽车业全样本 1966-1999）；'Do we learn more when we choose to or when we are told to?'（通俗化问句——人化表达）"
  rhetorical_question: "核心问句（'Do we learn more when we choose to or when we are told to?'——全文 knot 的载体）"
  pacing_notes: "核心问句开场→两派冲突→学习曲线传统→裁决；climax=voluntary 胜出揭晓；falling action 浅学习+形式条件"
  showing_telling: "'choose to vs told to'（自愿/被告诉的通俗对立）；'shallow learning'（浅学习意象）；'jolts'（外部冲击意象——mandate 派语言）"
  voice: "MgmtSci 理论实证口吻；'conflicting answers'（分歧承认）；'understudied'（未研究强调）"
```

### cross_paper_notes

- **paradigms-at-war 六原型（volition 裁决）**：zhou/wowak2025/park2025/shen/bendig/**haunschild2004**——两派冲突（volition vs mandate）实证裁决。
- **recall 学习家族源头确认**：haunschild2004（源头——volition 学习——wowak2015/kalaignanam2013 都引）→ kalaignanam2013（学习后果）→ haunschild2015（振荡）——学习家族谱系完整。
- **recall 现象域二十一讲法**（volition 学习 +1）。
- **与 mayo2022 的强制对照**：mayo（强制 vs 自愿召回——裁量权——隐藏）；haunschild2004（强制 vs 自愿——学习——volition）——同一 voluntary/involuntary 双极两个故事。
- **判别器记录**：paradigms-at-war 判定基于两派冲突（volition/mandate——'conflicting answers' 原文锚）实证裁决。
