# Story Blueprint — Eilert, Jayachandran, Kalaignanam & Swartz (2017) JM

## 文件头

```yaml
id: eilert2017
paper: "Eilert, Jayachandran, Kalaignanam & Swartz (2017, JM) — Does It Pay to Recall Your Product Early? An Empirical Investigation in the Automobile Industry"
paper_type: quantitative
distilled_sections: [intro, theory, methods, results]   # 2026-08-09 story 蒸馏（vault 报告 + 全文回读）→ ROBUST
source_records: [vault narrative/fine 报告（intro/methods/results 三份 fine + deep profile）, parsed full text]
vault_reports:
  intro: "narrative_analysis/mvp30/eilert2017_recall_timing_jm_narrative.md + introduction/mvp30/fine_grained/batch_2026-05-24/eilert2017_JM_distilled_introduction.md"
  methods_results: "narrative_analysis/methods_results/mvp30/methods/eilert2017_recall_timing_methods_narrative.md + results/... + deep_distillation/papers/... + fine_grained/batch_03_eilert2017_pollock2015/... + batch_2026-05-18/eilert2017_recall_timing_car_distilled_methods.md + batch_2026-05-20/eilert2017_jm_distilled_results.md（报告最齐全的一篇）"
  story_arc: null
corpus_links:
  write-introduction: "数据 Hook（390 recalls/数亿辆）+ 双向成本矛盾（Thus...However...Therefore...）+ Table 1 文献缺口表格可视化——路径待验证"
  write-methods: "Weibull AFT（time-to-recall）+ 2SLS 残差（时机→绩效）——路径待验证"
  write-results: "severity 反直觉主效应 + 三调节 + 时机价值相关性——路径待验证"
```

## Story

### one_liner

> recall 文献只做后果（市场反应）与学习（预防），"召回行为本身"是空白——为什么有的企业早召回有的晚？反直觉发现：**问题越严重召回越慢**（威胁刚性——面对问责企业转向内部、逃避暴露），但可靠品牌、过往召回经验会加速；而晚召回被市场惩罚更重——"Does It Pay to Recall Your Product Early?" 答案是：是的，尤其是严重问题。

### knot

```yaml
knot:
  primary_type: neglected-arena         # 第三原型：desai2012 注意力转向 / park2013 主题失衡 / 本文 prerecall 过程空白
  compound_types: []                    # 反直觉主效应（severity→延迟）是拓荒后的地形发现，非子类型
  statement: "recall 文献只研究召回的后果（市场反应、营销效果）与学习（预防、恢复），'召回行为本身'（prerecall 过程——
              为什么有的企业早召回有的晚）被整体忽略——'no study to our knowledge has examined the factors that
              influence the timing of product recalls'"
  tied_at:
    - "Intro P2-P3：双向成本矛盾（早召回有成本/晚召回成本更高——Toyota $17.35M 罚款）"
    - "Intro P4：RQ（'Why do some firms recall earlier?'）+ time-to-recall 定义"
  untied_at:
    - "Theory H1：severity → 延迟（威胁刚性）"
    - "Results Table 7：H1 支持（.84, p<.01）+ 三调节 + 绩效后果"
  antagonist: "recall 文献的后果/学习导向（把召回当作事后事件——prerecall 决策过程被跳过）"
  antagonist_built_by:
    - "Table 1 文献缺口表格可视化（gap 的视觉化论证——营销期刊惯例）"
    - "双重贡献声明（'First, to date, no study to our knowledge has examined...'）"
    - "双向成本矛盾（Thus... However... Therefore...——做 A 有成本、不做 A 成本更高的张力）"
```

### characters

```yaml
characters:
  protagonist: [problem severity（X——问题严重度）, time to recall（DV——Weibull AFT 生存时间）]
  supporting:
    - "brand reliability（调节——可靠品牌严重问题反而更快：期望违背惩罚驱动声誉保护）"
    - "brand diversification（调节——多元化品牌更慢：负面溢出威胁——增长 vs 脆弱权衡）"
    - "past recall intensity（调节——过往召回多→更快：学习论证 + 媒体关注催化剂）"
    - "stock market（后果——时机价值相关性：晚召回惩罚更重）"
  ensemble: [NHTSA 调查、美国汽车行业、Toyota $17.35M 罚款（Hook 案例）、Table 6 具名厂商召回时间对比（Toyota 最快）]
```

### resolution_logic

`exploration` 拓荒（补上被忽视的 prerecall 战场——severity 反直觉地图 + 品牌条件化 + 时机绩效后果——完整的前因后果地图）。

### five_acts

```yaml
five_acts:
  exposition: "Intro P1-P3：数据 Hook（390 recalls 2014 + NHTSA 数亿辆）→ 双向成本矛盾（早召回有成本/晚召回成本更高——Toyota $17.35M 罚款）→ RQ + time-to-recall 定义"
  rising_action: "Intro P5-P8（Table 1 文献缺口表格可视化 + BTOF 机制 [ability + motivation] + 调节预览 + 绩效后果贡献）+ Methods（NHTSA 调查、Weibull AFT、时机测量）"
  climax: "Results Table 7——H1 揭晓：**problem severity 显著延长召回时间（.84, p<.01）**——'问题越严重召回越慢'——威胁刚性的反直觉首揭（直觉预测应更早）"
  falling_action:
    - "品牌可靠性调节（可靠品牌严重问题反而更快——期望违背惩罚驱动——声誉资产保护）"
    - "品牌多元化调节（多元化品牌更慢——负面溢出威胁——供应链共同部件暴露）"
    - "过往召回强度调节（过往召回多→更快——学习论证 + 负面媒体催化注意力——政策含义：公开的大规模召回有监管效应）"
    - "绩效后果（晚召回被市场惩罚更重——时机具有价值相关性——2SLS 残差法 [RESIDUALFS]）"
    - "附加分析（美欧亚铭牌差异、价格层级、右删失处理、长期异常收益、严重度分项）"
  denouement: "Discussion——回到开头：prerecall 过程的前因后果完整地图；satisficing 响应（竞争压力下品牌位置决定）；
               问责威胁导致刚性（Staw threat-rigidity——保护自己免受政治余波）；政策含义（召回监管的调节效应）"
```

### stakes

```yaml
stakes:
  theoretical: "recall 文献只做后果与学习——召回行为本身（prerecall 过程）整体空白"
  practical: "消费者安全（延迟召回的风险敞口）；政策制定者（召回监管的调节效应——公开化加速后续响应）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 召回后果版——市场反应、营销工具有效性、危机学习（recall 文献主流）"
  - "讲法B: 品牌危机版——只做品牌资产/可靠性对召回的反应（品牌管理视角——无 prerecall 增量）"
  - "讲法C: 行业监管版——只做 NHTSA 监管政策评估（政策视角——换研究对象）"
  - "本文: prerecall 拓荒版——召回行为本身（时机前因 [severity 反而延迟] + 品牌条件 + 绩效后果——完整地图）"
```

### storytelling_tools（Ch03）

```yaml
storytelling_tools:
  human_face: "Toyota $17.35M 罚款（Hook 案例——具名）；Table 6 具名厂商召回时间对比（GM/Ford 高于均值、Toyota 最低——企业级人面）"
  rhetorical_question: "标题即问句（'Does It Pay to Recall Your Product Early?'——标题问句家族第 3 例——成本收益问句）"
  pacing_notes: "双向成本矛盾（Thus... However... Therefore... 逻辑链）；climax=severity 反直觉揭晓（.84 正系数——预期相反）；falling action 三调节+后果+五组附加"
  showing_telling: "Table 1 文献缺口表格可视化（gap 的视觉化论证）；标题问句（knot 载体）；hazard shape 参数（1.76——风险随时间上升）"
  voice: "营销实证口吻；'Thus... However... Therefore...' 逻辑推进；'no study to our knowledge'（精确例外声明）"
```

### cross_paper_notes

- **neglected-arena 三原型**：desai2012（注意力转向——field 防御）↔ park2013（主题失衡——进入门槛）↔ eilert2017（**prerecall 过程空白——召回行为本身**）。
- **标题问句家族第 3 例**：shipilov2020（"Is All Publicity Good Publicity?"）↔ kundro2023（"Does Power Protect Female Moral Objectors?"）↔ eilert2017（"Does It Pay to Recall Your Product Early?"——成本收益问句）。
- **recall 现象域 +1（前因侧）**：wowak2025 / desjardine2023 / singh2023（后果/机制侧）+ eilert2017 / malik2025（前因侧——组织 vs CEO 两视角）。
- **与 desai2012 的危机响应时间轴对照**：desai（危机后 field-level 防御）↔ eilert（危机中 firm-level 召回时机）——危机响应的时间轴两端。
- **判别器记录**：neglected-arena 判定基于"子域整体空白"（'no study to our knowledge'——recall 行为本身未研究）。
