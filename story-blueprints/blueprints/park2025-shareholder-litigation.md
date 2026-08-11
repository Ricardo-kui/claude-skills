# Story Blueprint — Park, Lange & Jeon (2025) SMJ

## 文件头

```yaml
id: park2025
paper: "Park, Lange & Jeon (2025, SMJ) — How Shareholder Litigation Risk Influences Firm Orientation Toward Stakeholders"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（vault 报告 + 全文回读）→ ROBUST
source_records: [vault narrative/methods_results 报告, parsed full text]
vault_reports:
  intro: "narrative_analysis/mvp30/park2025_shareholder_litigation_ud_laws_narrative.md"
  methods_results: "narrative_analysis/methods_results/mvp30/methods/park2025_shareholder_litigation_methods_narrative.md + results/... + deep_distillation/papers/... + fine_grained/batch_04_singh2023_park2025/...（四报告齐全）"
  story_arc: null
corpus_links:
  write-introduction: "经典辩论建立 Hook（'Rather than attempting to settle that disagreement...'——回避姿态）+ 反事实 RQ（'What would... if...'）——路径待验证"
  write-methods: "generalized DiD + CEM + 平行趋势——路径待验证"
  write-results: "主效应+治理条件化（H2/H4 削弱、H3 不支持诚实报告）——路径待验证"
```

## Story

### one_liner

> shareholder primacy 与 stakeholder view 的百年辩论——本文不裁决哲学争论，而是问反事实："如果管理者不再受股东诉讼压力约束，他们会优先服务谁？"——用 UD laws 州级采纳作外生冲击：约束放松后 stakeholder initiatives +43%——被股东压力掩盖的管理者偏好浮出水面，挑战 shareholder primacy 规范。

### knot

```yaml
knot:
  primary_type: paradigms-at-war        # 第三原型：zhou 理论仲裁 / wowak 维度分裂 / 本文外生冲击实证裁决
  compound_types: []                    # 纯型（辩论=背景，knot=被掩盖的真实偏好）
  statement: "shareholder primacy 与 stakeholder view 对'管理者无约束时会做什么'推出相反预测；管理者真实偏好被股东诉讼压力
              掩盖——用 UD laws 外生冲击揭示：约束放松后管理者转向 stakeholder（+43%），挑战 prevailing shareholder primacy norm"
  tied_at:
    - "Intro P1：经典辩论建立（二元对立——'Rather than attempting to settle that disagreement...' 回避姿态）"
    - "Intro P2：反事实 RQ（'What would managers prioritize if less constrained by shareholder pressures?'）"
  untied_at:
    - "Theory H1：约束放松→stakeholder 增加"
    - "Results Table 6：H1 支持（β=0.534, p=.042——+43%）+ 治理条件化"
  antagonist: "shareholder primacy 规范（管理者真实偏好被股东压力/诉讼风险掩盖）"
  antagonist_built_by:
    - "经典辩论建立（两阵营各持完整立场）→ 回避姿态（'Rather than... our interest lies in how these perspectives manifest in practice'）"
    - "反事实 RQ（'What would... if...'——key question 标注）"
    - "缺口论证（内在偏好被制度掩盖→需外生冲击）"
```

### characters

```yaml
characters:
  protagonist: [shareholder litigation risk（X——UD law 外生冲击）, stakeholder orientation（DV——stakeholder initiatives）]
  supporting:
    - "shareholder primacy vs stakeholder view（两阵营——被实证裁决的理论）"
    - "outside director ownership（H2——独立董事持股钉住股东导向：−3.224, p=.004）"
    - "shareholder governance provisions（H4——金降落伞等条款阻碍转向：−0.477, p=.003）"
    - "dedicated institutional investors（H3 不支持 + post-hoc 拆解）"
  ensemble: [UD law 州级采纳、9,670 firm-years、generalized DiD + CEM、平行趋势检验]
```

### resolution_logic

`arbitration` 仲裁（**外生冲击实证裁决**——温和版：不裁决哲学争论，用自然实验裁决行为证据——stakeholder 预测胜出但不断言哲学结论）。

### five_acts

```yaml
five_acts:
  exposition: "Intro P1-P2：经典辩论建立（shareholder primacy vs stakeholder view 二元对立）→ 反事实 RQ（约束放松后管理者会做什么）"
  rising_action: "Intro P3-P5（缺口：内在偏好被掩盖→UD laws 外生冲击；DiD+CEM 设计；三贡献）+ Methods（州级 UD law 采纳、generalized DiD、9,670 obs、平行趋势）"
  climax: "Results Table 6——H1 揭晓：UD law 后 stakeholder initiatives +43%（β=0.534, p=.042）——约束放松揭示被掩盖的 stakeholder 倾向"
  falling_action:
    - "H2 治理条件（outside director ownership 削弱：−3.224, p=.004——独立董事持股锚定股东导向）"
    - "H4（shareholder governance provisions 削弱：−0.477, p=.003——金降落伞等条款阻碍转向）"
    - "H3 不支持（dedicated investor ownership n.s.——诚实报告）+ post-hoc 拆解（dedicated 自由主义持股）"
    - "post-hoc 动机检验（stakeholder 参与源于内在信念而非自利——挑战'管理者自利'假设）"
  denouement: "Discussion——回到开头：'challenging the prevailing shareholder primacy norm'——约束放松后管理者转向 stakeholder；
               诉讼风险的非预期后果（风险规避+短视+诉讼敲诈）；治理机制替代/互补（functional substitutes——Misangyi & Acharya）"
```

### stakes

```yaml
stakes:
  theoretical: "管理者真实偏好被股东压力掩盖——purpose of the firm 辩论长期缺乏实证证据"
  practical: "UD laws 等治理改革对 stakeholder 战略的影响——诉讼风险的隐性成本（短视/风险规避）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 股东优先版——管理者只服务股东（shareholder primacy 正统）"
  - "讲法B: 哲学裁决版——在 shareholder vs stakeholder 辩论中选边（理论 essay——本文明确回避）"
  - "讲法C: 诉讼威慑版——只做诉讼风险对企业的负面后果（诉讼文献常见——风险规避/短视）"
  - "本文: 反事实揭示版——'约束放松后管理者会做什么'（UD laws 外生冲击揭示被掩盖的偏好——不裁决哲学，用证据旁敲侧击）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "低——UD law 州级法律事件（无具名企业）；stakeholder initiatives 计数 DV"
  rhetorical_question: "RQ 半问句（'What would managers prioritize if less constrained...?'——'key question' 明确标注——反事实式 RQ 而非修辞 pivot）"
  pacing_notes: "经典辩论→反事实 RQ→识别策略；climax=Table 6 主效应（+43% 揭晓）；falling action 治理条件化+动机检验"
  showing_telling: "'Rather than attempting to settle...'（回避姿态——不选边的中立立场）；反事实句式（what would... if...）"
  voice: "中立实证口吻（不选边）；克制（'challenging' 而非 'refuting'——温和裁决）"
```

### cross_paper_notes

- **paradigms-at-war 三原型（裁决方式演进）**：zhou2017（理论仲裁——拆地整合）↔ wowak2025（维度分裂——各赢一局）↔ park2025（**外生冲击实证裁决**——不裁决哲学、用自然实验裁决行为）。
- **识别家族对照**：park2025（generalized DiD + CEM）与 shipilov2020（DiD + CEM）、wu2025（制度冲击 DiD）——三个制度冲击识别故事。
- **与 singh2023 的治理对照**：singh（政治面——游说扭曲召回）；park（股东面——诉讼压力掩盖 stakeholder 倾向）——"治理约束的两种掩盖"。
- **判别器记录**：paradigms-at-war 判定基于两阵营完整立场 + 裁决需求；本文裁决方式=外生冲击（新形态）。
