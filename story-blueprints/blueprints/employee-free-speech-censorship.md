# Story Blueprint — Kundro, Sun, Song & Wan?（OS）— Employee "Free" Speech vs. Organizational Censorship

## 文件头

```yaml
id: employee_free_speech
paper: "（OS）— Employee 'Free' Speech vs. Organizational Censorship on Social Media: Balancing the Tension Between Free Expression and Safeguards to Foster Psychological Safety"
paper_type: quantitative   # 多方法（探索性 + 预注册观察/实验 + conjoint）
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（vault 四区段报告 + parsed 全文）→ ROBUST
source_records: [vault narrative/fine/theory/methods/results 报告, parsed full text]
vault_reports:
  intro: "narrative_analysis/mvp30/employee_free_speech_censorship_os_narrative.md + introduction/.../employee_free_speech_OS_distilled_introduction.md"
  theory: "narrative_analysis/theory/.../employee_free_speech_distilled_theory.md"
  methods_results: "narrative_analysis/methods_results/mvp30/methods/ + results/ + deep_distillation/papers/（报告齐全）"
  story_arc: null
corpus_links:
  write-introduction: "TikTok 解雇案例 Hook + 悖论声明（'paradoxically, both employee free speech... and its censorship can undermine psychological safety'）——路径待验证"
  write-theory: "边界理论 × 心理安全（同一政策对自由派/保守派相反）——路径待验证"
  write-results: "censorship 受众分裂（民主党↑/共和党↓安全）+ 四调节解药——路径待验证"
```

## Story

### one_liner

> 社交媒体时代的组织困境——审查员工的偏见言论（保护少数群体）还是保护言论自由（尊重个体自主）？实证发现**同一政策的两面**：审查提高民主党员工的心理安全、却降低共和党员工的——"paradoxically, both employee free speech and its censorship can undermine psychological safety"——但可兼得：组织价值观对齐 + 针对反黑人/威胁性/涉组织言论的审查，能提升民主党安全**而不损害**共和党。

### knot

```yaml
knot:
  primary_type: irony-reversal          # 第八原型：censorship 受众分裂（同一政策对自由派/保守派相反——与 pontikes2012 同款；irony 家族实证 8 份）
  compound_types: []                    # 双刃（审查/言论自由都损害安全）是发现，非子类型
  statement: "组织社会媒体政策困境——审查偏见言论（控制/保护少数群体）vs 言论自由（自主/尊重个体）——'a classic moral dilemma'——
              同一政策的两面：审查提高民主党心理安全（'prioritize safeguards'）、降低共和党（'prioritize free speech'）——
              'paradoxically, both employee free speech on social media and its censorship can undermine psychological safety'——
              但价值观对齐+针对特定言论的审查可兼得（民主党↑而不损害共和党）"
  tied_at:
    - "Intro：TikTok 解雇案例（Gaza 2023 后 Citigroup/Delta 解雇）→ 悖论声明（'paradoxically, both... and... can undermine psychological safety'）→ 全国样本（民主党忧偏见帖子/共和党忧雇主审查）"
    - "Theory：边界理论 × 心理安全（'organizational censorship... differentially influence psychological safety because of ideological disagreement'）"
  untied_at:
    - "Theory H1-H4：审查×意识形态 → 安全差异 + 四调节"
    - "Results：Study 2-3 支持（民主党↑/共和党↓）+ Study 4 conjoint（四调节兼得）"
  antagonist: "心理安全文献的'政策=普遍有效'假设（'questioning policies that are assumed to generally promote psychological safety across employees'）"
  antagonist_built_by:
    - "TikTok/Citigroup/Delta 案例（Gaza 2023 解雇——'prominent companies... fired employees for antisemitic and anti-Palestinian posts'——具名）"
    - "悖论声明（'paradoxically, both employee free speech on social media and its censorship can undermine psychological safety'——双刃排布）"
    - "全国样本张力（民主党忧偏见/共和党忧审查——'a compelling tension'——受众分裂的实证铺垫）"
```

### characters

```yaml
characters:
  protagonist: [organizational censorship（X——审查偏见言论）, individual psychological safety（DV）]
  supporting:
    - "意识形态分裂（民主党——'prioritize safeguards'；共和党——'prioritize free speech'——同一政策两面）"
    - "边界控制（机制——'a form of boundary control'——工作/非工作边界模糊）"
    - "四调节解药（组织价值观对齐/目标群体/言论严重度/公司关联——'increase psychological safety for Democrats without undermining... Republicans'）"
    - "Citigroup/Delta/TikTok（具名解雇案例）"
  ensemble: [全国代表性样本（金标准）、Study 1 开放式 + Study 2-3 预注册观察/实验 + Study 4 conjoint、Gaza 2023 背景]
```

### resolution_logic

`revelation` 揭幕（揭幕同一政策的受众分裂——意识形态双面 + 四调节解药——"控制与自主的平衡"）。

### five_acts

```yaml
five_acts:
  exposition: "Intro：自由言论核心原则 vs 社交媒体偏见言论泛滥 → TikTok/Citigroup/Delta 解雇案例（Gaza 2023）→ 悖论声明（'paradoxically, both... and... can undermine psychological safety'）→ 全国样本（民主党忧偏见/共和党忧审查）"
  rising_action: "边界理论 × 心理安全（'organizational censorship... differentially influence psychological safety because of ideological disagreement'）+ 四调节理论 + Methods（全国样本 + Study 1-4 多方法）"
  climax: "Results——受众分裂揭晓：审查提高民主党心理安全、降低共和党（Study 2-3 预注册确认——'censorship increases Democrats' psychological safety but decreases Republicans''）——同一政策的两面首揭"
  falling_action:
    - "四调节解药（Study 4 conjoint——组织价值观对齐 + 反黑人言论 + 威胁性言论 + 涉组织言论——'improve psychological safety for Democrats without undermining... Republicans'）"
    - "多方法三角（开放式 + 观察 + 实验 + conjoint——'triangulate data... to provide a deeper understanding of both experiences and causal relationships'）"
    - "全国样本外效度（'the gold standard for external validity in a population'）"
  denouement: "Discussion——心理安全的边界条件（'efforts to create psychological safety can also subvert this goal'）；
              意识形态平衡（'maintaining the social-relational fabric of organizations will require policies that balance ideological demands'）；
              政策建议（质疑'普遍有效'假设——'questioning policies that are assumed to generally promote psychological safety across employees'）"
```

### stakes

```yaml
stakes:
  theoretical: "心理安全创建'最 glaring gap'（Edmondson & Bransby——how to create safety 未解）；政策=普遍有效的假设未检验"
  practical: "组织社会媒体政策（Gaza 2023 后 Citigroup/Delta 解雇的普遍性）；极化社会中的心理安全平衡（'as political polarization permeates societies'）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 心理安全前因版——领导/支持/工作设计（心理安全文献主流——Edmondson——不接政治）"
  - "讲法B: 言论自由版——自由言论态度的公众研究（政治学/社会学——Kozyreva/Pradel——不接组织）"
  - "讲法C: 边界管理版——线上边界模糊（Ollier-Malaterre——同事连接——不接审查政策）"
  - "本文: 受众分裂揭幕版——审查政策对自由派/保守派相反（'paradoxically, both... and...'——四调节兼得解药）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "TikTok 解雇事件/Citigroup/Delta（Gaza 2023——'fired employees for antisemitic and anti-Palestinian posts'——具名企业+具体事件）；'woke' 标签引用（'labeled woke'——当代政治语汇）"
  rhetorical_question: "核心问句（'organizations may try to limit their employees' free expressions of prejudice... but should they?'——决策问句）"
  pacing_notes: "自由言论原则→解雇案例→悖论声明→全国样本→四研究递进；climax=受众分裂揭晓（Study 2-3）；falling action 四调节解药（Study 4 conjoint）+多方法三角"
  showing_telling: "'paradoxically, both... and...'（悖论排布）；'a classic moral dilemma'（道德困境意象）；'balance... equilibrium'（平衡/均衡意象——'rejecting the conventional and divisive either/or approach'）"
  voice: "OS 理论实证口吻；'paradoxically'（悖论标记）；'the most glaring gap'（Edmondson 引语——文献缺口）"
```

### cross_paper_notes

- **irony-reversal 八原型（censorship 受众分裂——与 pontikes2012 同款）**：pontikes（同一构念对 consumer/VC 相反）/desjardine2023（反果）/toh（类别分裂）/keeves（关系双面）/darby2024（反果）/wowak2015（反果源头）/chen2009（策略反果）/**employee_free_speech（同一政策对自由派/保守派相反——受众分裂第二例）**。
- **与 kundro2023 的性别/意识形态对照**：kundro（权力对男女 objector 不对称——共识条件化）；employee（审查对自由/保守派相反——受众分裂）——"同一政策对不同群体"家族。
- **MVP30-28 全覆盖达成（28/28）**。
- **判别器记录**：irony-reversal 判定基于同一政策（censorship）对两类群体（自由派/保守派）意义相反——与 pontikes2012 的受众分裂同款（'differentially influence... because of ideological disagreement'——原文锚）。
