# Story Blueprint — Gamache, Devers, Klein & Hannigan (2023) SMJ

## 文件头

```yaml
id: gamache2023
paper: "Gamache, Devers, Klein & Hannigan (2023, SMJ) — Shifting Perspectives: How Scrutiny Shapes the Relationship Between CEO Gender and Acquisition Activity"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（vault 报告 + 全文回读）→ ROBUST
source_records: [vault narrative/methods_results 报告, parsed full text]
vault_reports:
  intro: "narrative_analysis/mvp30/gamache2023_scrutiny_gender_acquisition_smj_narrative.md"
  theory: "parsed_texts/mvp30/Shifting perspectives...（§1 全文回读——机制链核实）"
  methods_results: "narrative_analysis/methods_results/mvp30/methods/gamache2023_scrutiny_gender_acquisition_methods_narrative.md + results/... + deep_distillation/papers/... + fine_grained/batch_08_malshe2015_gamache2023/...（四报告齐全）"
  story_arc: null
corpus_links:
  write-introduction: "共识挑战 Hook（'too simplistic' 批评 + 具名反例三连）——路径待验证"
  write-theory: "信息加工×job demands 双理论整合（低审视放大/高审视消解机制链）——路径待验证"
  write-methods: "负二项+Tobit 双 DV；ITCV + 治疗效应（交互免疫论证）——路径待验证"
  write-results: "边际效应分析（Table 6 分层）——路径待验证"
```

## Story

### one_liner

> "女性 CEO 保守"被当作普遍共识（平均效应确实存在——收购少 41.88%），但它是信息加工×审视情境的产物而非固有风险偏好：低审视下女性 CEO 的细致处理优势让差异放大，**高审视消耗她们的细致处理资源→与男性趋同**——审视不是让女性更谨慎，而是让她们"失去"谨慎的能力；不是"女性天生保守"，是"情境如何塑造信息处理"。

### knot

```yaml
knot:
  primary_type: consensus-puzzle        # 第三原型：pontikes 完整性 / cutolo 无条件性 / 本文条件性消解
  compound_types: [assumption-flip]     # "女性 CEO 保守=风险偏好差异"前提被翻转成信息加工差异
  statement: "共识——女性 CEO 普遍保守（收购显著更少）；具名反例（Mayer 53 家公司、Fiorina $25B、Rometty $34B）显示并非如此——审视情境（动态行业/媒体覆盖/董事会权力）调节：高审视下性别差异消失"
  tied_at:
    - "Intro P1-P2：共识建立+简化论批评 → 具名反例三连"
    - "Theory：信息加工×job demands 整合（三前提：女性全面处理/需求削弱处理/审视对女性更显著）"
  untied_at:
    - "Theory H1-H3：三审视情境预测（低审视放大、高审视消解）"
    - "Results 三交互全部支持（0.357/0.311/0.439——差异消解）"
  antagonist: "'女性 CEO 普遍保守'的简化论共识（把情境效应固化为性别特质）"
  antagonist_built_by:
    - "共识-批评句式（'may paint too simplistic a picture'）"
    - "具名反例三连（Mayer/Fiorina/Rometty——$2B/$25B/$34B 具体金额）"
    - "复现主效应再消解（Results 先报 −0.552 再报三交互）"
```

### characters

```yaml
characters:
  protagonist: [CEO gender（X——female CEO）, acquisition activity（DV——数量+支出双测量）]
  supporting:
    - "scrutiny（核心调节——动态行业/媒体覆盖/董事会权力三情境）"
    - "information processing（机制——女性更细致的信息处理，非风险偏好；高审视消耗之）"
    - "job demands（理论透镜——executive job demands：高需求→启发式处理）"
    - "male CEOs（对照组——差异的参照）"
  ensemble: [Mayer/Fiorina/Rometty（具名反例）、10,351 firm-years、ITCV/治疗效应（稳健性）]
```

### resolution_logic

`revelation` 揭幕（换视角——从"性别特质"镜头切到"情境审视"镜头——共识条件化消解）+ 机制替换（风险偏好→信息加工）。研究者是镜头切换师：先给共识特写（复现主效应），再切近景露出审视情境的调节面。

### five_acts

```yaml
five_acts:
  exposition: "Intro P1-P2：共识建立+简化论批评 → 具名反例三连（$2B/$25B/$34B）→ RQ（什么情境条件影响性别-并购关系）"
  rising_action: "Intro P3-P5（信息加工×job demands 整合 + 审视机制 + 发现预览）+ Theory（三前提机制链：低审视放大/高审视消解）+ Methods（负二项+Tobit 双 DV、10,351 firm-years、三调节）"
  climax: "Results——复现主效应（β=−0.552, p=.000，女性 CEO 少 41.88% 收购）后三交互揭晓：
           dynamism（0.357, p=.004）/ media（0.311, p=.022）/ board power（0.439, p=.004）全部正向——
           高审视下性别差异消失（高动态环境女性收购 +78.57%）"
  falling_action:
    - "边际效应分析（Table 6：低审视全负显著、高审视 95 分位不显著——消解的可视化）"
    - "内生性：交互项免疫论证（Bun & Harrison）+ ITCV（54% 阈值）+ 治疗效应（IV：行业女性 TMT 代表 + TSR 自然工具）"
    - "绩效审视补充（above-referents 交互 1.636, p=.014——超额绩效也消解差异；below 无效应——三解释：资源约束/威胁僵化/目标意愿）"
  denouement: "Discussion——回到开头：'female CEOs are not naturally conservative decision-makers'
               （'gender differences driven by information processing, not inherent differences in risk preferences'）；
               job demands 文献的意料外（标准预期是 job demands 强化天然特质——本文显示审视削弱保守）；
               未来情境（多元化/国际化/高声誉——Rhee & Haunschild 高声誉审视）"
```

### stakes

```yaml
stakes:
  theoretical: "'女性 CEO 保守'被固化为人格特质——情境视角（审视/信息加工）被忽略——upper echelons 性别研究 'in its infancy'"
  practical: "董事会与投资者对女性 CEO 的审视管理；女性 CEO 在高审视下反而更积极收购的决策含义"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 性别差异版——女性 CEO 更保守（性别-风险文献主流；元分析共识）"
  - "讲法B: 特质深化版——女性 CEO 风险偏好再测（把差异归因于人格——本文明确反驳）"
  - "讲法C: 董事会多样性版——只做女性董事比例的影响（Chen et al. 2016 已做——本文复现后区分）"
  - "本文: 情境消解版——审视三情境下性别差异消失——共识在低审视下成立、高审视下消解；机制从风险偏好换成信息加工"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "具名反例三连：Marissa Mayer（Yahoo! 53 家公司、$2B+/4 年）、Carly Fiorina（Compaq $25B）、
               Ginni Rometty（Redhat $34B）——反例即人面"
  rhetorical_question: "未见 pivot【已核实】——反例论证用陈述句式（'raise the question of whether...' 半问句过渡）"
  pacing_notes: "共识→反例→整合→机制→预览五步 Intro；Results 复现-消解节奏（先 −0.552 主效应，再三交互消解）；
                 falling action 含边际效应可视化+三层内生性防御"
  showing_telling: "具名反例金额并置（$2B/$25B/$34B）；Figure 1/2/3 交互图（差异消失的视觉证据）；
                    'too simplistic a picture'（简化论批评）"
  voice: "主动语态；共识-批评平衡（先承认共识再质疑）；'We do not believe that either type of information
          processing is inherently better'（价值中立声明）"
```

### cross_paper_notes

- **同作者不同故事家族第 3 组**：gamache2020（cross-domain-unification——统一引擎）↔ gamache2023（consensus-puzzle——共识条件化消解）——与 desjardine2022↔2023 并列；同 gamache 姓氏、同 SMJ、故事完全不同。
- **consensus-puzzle 三原型**：pontikes（完整性）/ cutolo（无条件性）/ gamache2023（条件性消解）——与 toh2023 对照：toh 平均成立后**劈开**（反向）、gamache 平均成立后**消解**（归零）。
- **识别家族**：负二项+Tobit 双 DV 与 pfarrer2010（RE logit+CAR 双 DV）同构——双 DV 镜像呈现。
- **判别器记录**：consensus-puzzle 判定基于贡献维度=条件（审视情境 Boundary）——与 assumption-flip（机制贡献）区分。
