# Story Blueprint — Cutolo & Ferriani (2024) JM

## 文件头

```yaml
id: cutolo2024
paper: "Cutolo & Ferriani (2024, JM) — Now It Makes More Sense: How Narratives Can Help Atypical Actors Increase Market Appeal"
distilled_sections: [intro, theory, methods, results]      # 2026-08-09 补蒸馏 intro+theory → ROBUST
source_records: [project_mvp30_cutolo2024_methods_results, project_mvp30_cutolo2024_intro_theory]
corpus_links:
  write-introduction: "hooks/04-puzzle-paradox 变体D（历史人物受难悖论型：Cézanne）；literature-turns/01-progressive-coherence 变体P（共识-让步-反证-目标收窄）；tensions/01-despite-progress-unaddressed 变体AF（外生条件清单→可操作杠杆缺口）；contributions 变体S（三流贡献：机制+理论+方法论）；theory-lens/02-dual-theory-layered 变体B（fluency 主机制 + Bloom & Lahey 三维度框架，期刊标签已修 JOM→JM）"
  write-theory: "variants/E_moderation.md E10（taxonomy 驱动 N 平行缓解调节，含 baseline-from-consensus + 最小对比对）"
  write-methods: "文本构念测量 变体5-7（复合文本指标 / 类别相对常规性 / 人工验证）；非线性模型 变体1（负二项+过度分散诊断）"
  write-results: "计数模型 变体4-6（Count-Model Moderation Translation / Text-Measure Robustness Bundle / Composite Text Component Disaggregation）"
```

## Story

### one_liner

> 类别理论说非典型者被市场惩罚——共识如此，连塞尚都被沙龙每年拒绝。但"怎么讲自己的故事"能改变这个判决：叙事（抽象度、内聚度、常规性——语言的内容/形式/使用三个维度）让非典型变得"说得通"。标题本身就是故事的宣言：Now It Makes More Sense——以前说不通，现在说得通了。

### knot

```yaml
knot:
  primary_type: consensus-puzzle   # 双原型（pontikes2012 完整性 + cutolo2024 无条件性）：强共识预测 vs 条件持续违背
  compound_types: []
  statement: "非典型参与者被市场惩罚（类别理论共识，H1 基线），但非典型者仍在市场上存在且常获超额回报——被忽略的条件是 actor 可操控的'叙事'：文本特征（abstraction/cohesion/conventionality）能否缓解惩罚、提高市场吸引力？"
  tied_at:
    - "Intro P1：Cézanne Hook（现代艺术之父被沙龙每年拒绝 1864-1869）→ 惩罚共识现象 + 多域证据加固"
    - "Intro P2：Foucault 'normalizing society'/'penalty of the norm'——理论权威把惩罚共识升到制度哲学层（共识被理解而非被推翻）"
    - "Theory：H1 文献基线（'the conceptualized mechanisms in the existing literature suggest the following baseline hypothesis'——主效应是引用不是推导）"
  untied_at:
    - "Theory：H2-H4 三调节（抽象度/内聚度/常规性 = 解药机制，统一落到 processing fluency 透镜）"
    - "Results：计数模型主效应 + 三调节（predicted count at moderator min/max，penalty reduction %）"
  antagonist: "类别理论的惩罚共识 + 条件研究的功能局限——共识单方面认定受众只惩罚非典型；条件研究（audience/flux/signals/status）虽多但全部外生、不能给行动者开处方（'limited in their ability to offer prescriptive advice'）"
  antagonist_built_by:
    - "P2 Foucault 权威深化：惩罚不是偶然而是制度机制（normalizing society 的双重功能）——反派有哲学纵深"
    - "P3 让步-反证：'Luckily, despite abundant evidence regarding the penalties... noncompliance can still be a risk worth taking'——先给共识让步（证据充分），再反证受益面（突破/超额回报）"
    - "P4-P5 条件清单→外生性诊断：多流条件研究逐类列出，再统一诊断'全部不可控'——反派的残余势力是'文献开了处方但病人拿不到药'"
```

### characters

```yaml
characters:
  protagonist: [叙事文本特性 (X：abstraction/cohesion/conventionality，三特征群), market appeal (Y)]
  supporting:
    - "Bloom & Lahey 语言三维度（content/form/use）→ 三特征 1:1 映射：配角成建制登场（taxonomy 驱动，预先回答'为什么是这三个'）"
    - "processing fluency（统一机制透镜：所有调节落到同一机制状态）"
  ensemble: [在线市场情境（Etsy，78,758 crafters / 146 类别）、类别结构与常规性基准（LDA topic weights → category-average slope）]
```

### resolution_logic

`remedy` 解药（新解法性格，与 write-theory moderator-as-remedy / E10 手法同族）——**给已知惩罚加解药条件**：惩罚共识不撤销，而是被条件化——叙事是解药，且解药是 actor 可操控的（这正是与条件研究的分界：audience/flux/status 都不可控，文本特征可控）。研究者是"配解药的人"：承认毒性的存在（H1 基线），给出解毒配方（三特征）。

### five_acts

```yaml
five_acts:
  exposition: "Intro P1-P4：Cézanne Hook（历史人物受难悖论）→ 惩罚共识 + Foucault 制度哲学深化 → 让步-反证（'Luckily...' 受益面）→ 目标收窄 pivot（'Our goal, however, is different. We are not interested in demonstrating the performance upsides of atypicality'——显式排除受益故事）→ 条件研究进展清单"
  rising_action: "Theory：H1 文献基线（主效应引自共识）；Bloom & Lahey 三维度 taxonomy → 三特征映射；三个平行机制小节（每节：学科证据 → 机制 → 应用到非典型 → 假设），统一落到 processing fluency；Leah 最小对比对（'painter and musician' vs 'artist'）作 theory 级 showing；Methods：文本构念测量三段效度链（理论语言组件→字典/工具→聚合规则→人工验证）；类别相对常规性（LDA topic weights → category-average slope）；负二项 + 过度分散诊断"
  climax: "Results 主表：负二项主效应 + 三调节（log-count 系数 → predicted count at moderator min/max → penalty reduction %）——'惩罚被叙事缓解'的量化瞬间"
  falling_action:
    - "Text-Measure Robustness Bundle：按 dictionary/tool 替代、topic granularity、component disaggregation 组织（测量威胁驱动）"
    - "Composite Text Component Disaggregation：复合文本指标拆回子维度——哪个特征驱动缓解（解药成分分析）"
  denouement: "Discussion：三流贡献收口（对 atypicality 条件研究——叙事机制缓解需求侧惩罚；对 cultural entrepreneurship——microlinguistics 微观基础升级 discourse/storytelling 宏观路线；方法论——计算文本分析独立成条）——'Now It Makes More Sense' 的完整兑现（叙事让非典型变得可理解，惩罚不是必然）"
```

### stakes

```yaml
stakes:
  theoretical: "类别理论的核心预测（非典型惩罚）若不条件化，会对'非典型者如何生存'产生系统误判；条件研究只做不可控因素导致'文献知道惩罚可解但行动者拿不到解药'——叙事视角把惩罚从规律变成有条件判断，且条件在 actor 手中"
  practical: "在线市场/平台上的非典型卖家（独立创作者、小众产品、跨界工匠）：如何用叙事争取市场接纳——差异化不靠模仿靠讲故事（Etsy 平台鼓励'craft stories'是设计证据）"
```

### alternative_tellings

```yaml
alternative_tellings:
  - "讲法A: 惩罚必然故事 — '非典型者受罚，类别理论已定论'（原版共识；H1 就是它的引用）"
  - "讲法B: 受益故事 — '非典型带来突破与超额回报'（P3 显式列出并排除：'Our goal, however, is different. We are not interested in demonstrating the performance upsides of atypicality'——本文在 intro 里亲手拒绝了它）"
  - "讲法C: 同化策略故事 — '非典型者应该变得典型（模仿/模糊化）'（战略版：消灭非典型性；本文的反面——保留非典型，改变叙事）"
  - "讲法D: 受众宽容故事 — '受众其实不惩罚非典型'（挑战惩罚本身——Pontikes 式双面，不是本文）"
  - "本文: 叙事解药 — 非典型不用变典型，讲好故事就能'说得通'。选择理由：'make more sense' 把解法放在叙事（意义生成）而非同化（身份放弃）；既保留惩罚共识的威慑力（诚实，H1 基线），又给出可操作出路（解药，actor 可控）——与条件研究的根本分界是可控性"
```

### storytelling_tools

```yaml
storytelling_tools:
  human_face: "Cézanne（历史人物人格化——被拒的伟人）；Leah 最小对比对（Theory 内的具名示例人物）；78,758 个 Etsy 匠人的样本规模"
  rhetorical_question: "未见（待补确认）"
  pacing_notes: "Intro 节奏：共识慢铺（P1-P2 含 Foucault 深化）→ 'Luckily' 急转（P3 受益反证）→ 目标收窄 pivot（'Our goal, however, is different'）→ 条件清单快进（P4）→ 操作性缺口急停（P5）→ 三特征预告（P6）；Theory 三小节平行匀速（每节学科证据→机制→应用→假设）；climax 在 Results 主表（惩罚缓解的量化），falling action 的'成分拆解'是解药配方的最后一步"
  showing_telling: "标题 'Now It Makes More Sense' 是贯穿性声言（论文自身示范叙事力量——meta-level showing）；Leah 最小对比对（Theory 级 showing：两个只差抽象层级的句子并置）；minimal pair 是本文对 showing 工具库的贡献"
  voice: "待补"
```

### cross_paper_notes

- **与 Pontikes 2012（consensus-puzzle 双原型）**：同一"惩罚共识被挑战"家族，挑战方式不同——Pontikes = 共识的**完整性**（受众异质性：同一标签两受众相反）；本文 = 共识的**无条件性**（叙事条件：惩罚可被缓解）。对照价值：挑战共识有两种切法——"共识忽略了谁" vs "共识忽略了什么条件"。
- **与 Zhou 2017（remedy 手法同族）**：moderator-as-remedy 从理论层（竞争/start-up 作低效解药）扩展到文本层（叙事作惩罚解药）——'解药'是可跨层复用的故事骨架（write-theory E10 与 E 系 moderator-as-remedy 互证）。
- **与 Gamache 2020（文本测量家族）**：同用文本测量作 Methods 资产，故事地位不同——Gamache 文本测**心理构念**（文本是探针）；本文文本测**叙事本身**（文本是主角/解药本体）。
- **与 Malshe 2015（跨域家族）**：Malshe 用源学科证据为 gap 背书（finance 证据支持 debt 半区重要性）；本文用语言学证据为解药背书（Bloom & Lahey 既成框架）——跨学科 credibility 转移的两种用法。
