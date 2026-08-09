# Story Blueprint 字段规范（草案 v0.1）

> 每篇论文一份 blueprint。字段事实性来源：蒸馏记录 + 全文回读。缺失标 `待补`，禁止编造。

## 文件头

```yaml
id: <kebab-case，如 zhou2017>
paper: "<作者 (年份), 期刊> — <标题>"
paper_type: quantitative | qualitative | theory   # 定性/理论论文的五幕按 Pollock Fig 2.3/2.4 overlay（见 five_acts）
distilled_sections: [intro, theory, methods, results]   # 已深度蒸馏的区段；缺失者其对应五幕字段标待补
source_records: [<memory 文件名或蒸馏记录>]
vault_reports:   # Phase 0 vault 检索结果（distill-story-exemplar SKILL.md Phase 0 协议）；报告与 memory 冲突时以报告为准
  intro: <路径或 null>
  theory: <路径或 null>
  methods_results: <路径或 null>
  story_arc: <_story_arcs/ 路径或 null>   # 早期故事弧资产，链接不复制
corpus_links:   # 链接现有 section 变体，不复制内容
  write-introduction: "<目录>/<变体名> 变体X"
  write-theory: ...
  write-methods: ...
  write-results: ...
```

## Story 主体

### one_liner
一句话故事（≈论文的叙事电梯演讲，区别于摘要——它说的是"冲突与解法"不是"发现"）。**= GBL 2007 的 theorized storyline**（理论化叙事主线：贯穿全文的理论主张线，读者读完能复述的那句话）——与 Pollock 的 storylines（构念旅程）是不同概念，勿混用。定性论文的 one_liner 尤其承担 storyline 功能（见 write-introduction qualitative-mode 的 GBL 接入段）。

### knot
```yaml
knot:
  primary_type: <草表类型之一>
  compound_types: [<子结构类型>]     # knot 通常复合；空列表=纯型
  statement: "<一句话核心冲突，必须含冲突双方>"
  tied_at: [<knot 在哪里系紧：intro 模块 / theory 段落>]
  untied_at: [<knot 在哪里解开：theory 假设 / results 位置>]
  antagonist: "<反派是谁：两派理论 / 学术共识 / 被忽视的行动者 / 文献的注意力…>"
  antagonist_built_by: ["<构造反派的修辞手法，如：双层 non-coherence 排布、三情境加固、修辞问 pivot>"]
```

**knot 类型表（v0.2 定稿，2026-08-09 评审，基于 11 份 blueprint；2026-08-09 实证对账扩至 59 份——各类型实例计数见词表行）**：

> **元性质**：所有 knot 均具悖论性张力（Pollock: knot 即 central tension）——`paradox` 不作独立主型路由，保留为待建类型（等纯悖论型论文如 Mishina 2010 入库再定）。原型状态词表（**2026-08-09 修订：无硬上限——家族钉死按实例计数，≥2 即交叉验证**）：**九原型**（neglected-arena/half-domain-gap）＞**八原型**（irony-reversal/overlooked-alternative/paradigms-at-war）＞**七原型**（consensus-puzzle）＞**六原型**（assumption-flip）＞**三原型**（tangled-constructs）＞**单原型**（cross-domain-unification——观察中）＞**compound-only**（counterevidence）＞**待建**（paradox）。计数以 `scripts/extract_layout.py` 实证提取为准（2026-08-09 对账）。

| 类型 | 含义 | 原型状态 | 原型样例 | 区分于 |
|------|------|---------|---------|--------|
| `paradox` 悖论 | 同一预测自相矛盾 / 现象违背常理 | 待建 | —（Mishina 2010 候选） | 悖论性是元性质，各类型按冲突位置分化 |
| `irony-reversal` 反讽反转 | 同一构念/行动对双方意义相反，或行动产生与预期相反的结果 | 八原型 | Pontikes 2012（受众分裂）；DesJardine 2023（反果）；Toh & Pyun 2023（类别分裂）；Keeves 2017（关系双面）；Darby 2024（反果）；Wowak 2015（反果源头）；Chen 2009（策略反果——主动→更受罚）；Employee Free Speech（censorship 受众分裂） | 冲突在**现象内**（同一 X 对两类 Y 相反）；consensus-puzzle 的冲突在**文献共识 vs 现实**；子家族：机制/策略反噬（wowak2015/darby2024/desjardine2023/chen2009） |
| `paradigms-at-war` 范式对决 | 对立阵营对同一现象推出相反预测 → 需裁决/整合/拆维（外部理论战 或 同构念两极战） | 八原型 | Zhou 2017（理论仲裁）；Wowak 2025（维度分裂）；Park 2025（外生冲击）；Shen 2022（拆地整合）；Bendig 2024（倒 U 裁决）；Haunschild & Rhee 2004（volition 裁决——voluntary vs mandated）；CSR Decoupling China（协调 vs 合谋）；Crash Risk 2025（约束 vs 信息——'predicts an opposite effect'） | 冲突在**两阵营之间**（各持完整立场）；irony 是同一构念自身的两面 |
| `consensus-puzzle` 共识谜团 | 强共识预测 vs 行为/证据/条件持续违背 → 被忽略的异质性或条件 | 七原型 | Cutolo 2024（无条件性）；Gamache 2023（条件性消解）；Kundro 2023（条件性失效）；Han 2020（情境双向调制）；Fang 2025（机会/威胁共识翻转）；Haunschild 2015（学习/遗忘振荡）；Gao 2015（广告条件化）——Pontikes 2012 为 irony 主型 compound（完整性张力），不计主型 | 冲突在**文献共识 vs 现实/条件**；counterevidence 是它的对照点子结构 |
| `counterevidence` 现实反证 | 理论预测 vs 宏观现实事实相悖（单个宏观对照点） | **compound-only** | Zhou 2017 子结构（dying dinosaurs）；Malshe 2015 子结构 | 不作主型路由；只作其他类型的增强子结构（宏观事实反证 = 对照点，consensus-puzzle = 结构性异质性/条件） |
| `neglected-arena` 被忽视战场 | 重要现象/子域被文献结构性忽视（含注意力转移解释） | 九原型 | Desai 2012；Park & Westphal 2013；Eilert 2017（prerecall 过程空白）；Kashmiri 2017（人格视角空白）；Kalaignanam 2013（学习后果空白）；Pupovac 2025（垂直传染子域）；Hoffmann 2024（法律前因维度）；DesJardine 2025（信息竞争子域）；Top Mgmt Incentives（激励合约机制——'documented but unmodeled'） | **整个子域没人做**；overlooked-alternative = 现象做了但看漏一面 |
| `assumption-flip` 前提倒置 | 挑战共识前提（Alvesson problematization 家族） | 六原型 | Paruchuri 2020（valence 方向）；Shipilov 2020（负面偏好）；Hahl 2017（distinction 动机）；Lovelace 2021（浪漫领导力）；Darby 2025（activist 身份）；Li 2026（现金流前提复杂化——'mainly focused on the cash flow effect'→管道/棱镜）——机制前提翻转家族：方向/极性/动机/归因/actor 身份/机制单通道 | 机制/逻辑前提（Mechanism 贡献）；tangled-constructs = 构念层面纠缠（Constructs 贡献）；判别器=贡献维度（机制→本型，条件→consensus-puzzle） |
| `tangled-constructs` 构念纠缠 | 两构念被混同或单向化，实为动态不对称/共演关系；解法=解开而非剪断 | 三原型 | Pollock 2015；Han 2024；Pfarrer 2010（reputation 家族三拆：共演/区分/机制端+正负边界） | 构念层面（Constructs）；assumption-flip = 机制前提（Mechanism） |
| `half-domain-gap` 互补半区 | 现象有天然双极（equity/debt、success/failure…），前人只做一极，另一极即 gap；常与跨学科嫁接配合 | 九原型 | Malshe 2015（维度半区）；Wu 2025（行为半区）；Malik 2025（情境半区）；Mayo 2022（跨域半区）；Lun 2026（后果半区）；Liu 2016（决策半区）；Denicolò 2025（治理效应半区——理论版——均衡权衡）；Shi 2021（羊群披露半区）；Reporting Comparability 2025（CII 溢出半区——'Little is known about the potential spillover effects'） | **同一维度半区缺失**；cross-domain-unification = 两分离域共用引擎；overlooked-alternative = 换视角 |
| `overlooked-alternative` 主导视角批评 | 现象已被研究，但主流视角看漏一个替代面；解法=提出替代视角（deductive 宣战 或 inductive 从数据长出） | 八原型 | DesJardine 2022（预设）；Lashley & Pollock 2020（归纳 remove）；Singh & Grewal 2023（政策宣战）；Zhao-Ding & Gaba 2022（需求侧镜头）；Darby 2026（外部治理面）；Vadakkepatt 2022（顾客面）；Antón 2025（共同所有权亮面——'much less work on procompetitive role'）；Product Market Threats（效率面——'This view, however, neglects'） | 现象**已研究、做了一面**；neglected-arena = 整个子域空白 |
| `cross-domain-unification` 跨域统一 | 两个分离研究域由同一机制统一解释（2×2 对称映射常见）；解法=发现共同引擎 | 单原型 | Gamache 2020（Serving Differently） | **两分离域统一**；half-domain-gap = 一半缺失；overlooked-alternative = 视角切换 |

**倾向配对（非强制）**：`paradigms-at-war` → 裁决类解法（arbitration / dimension-split——对立阵营必须裁决，59 份 blueprint 实证 8/8 裁决类）；其余类型与 revelation/exploration/unification/remedy 自由组合（revelation 兼容性最高——irony/overlooked/assumption-flip/tangled 100% 实证，见 layout-inventory 联合分布）。

### characters
```yaml
characters:
  protagonist: [<主角构念；IV/DV 均主角或选一>]
  supporting: [<配角：moderator/mediator 及其故事功能>]
  ensemble: [<群演：controls/情境>]
```

### resolution_logic
解法性格（研究者以什么姿态解开 knot）。**定稿 v0.2（2026-08-09 评审）**：
- `arbitration` 仲裁：拆解到 facet 再整合（两派都只对一半）——Zhou 2017（paradigms-at-war 裁决类）
- `revelation` 揭幕：换视角，展示被共识忽略的第二张脸——Pontikes 2012；Pollock 2015（解结）；DesJardine 2022（翻硬币）；DesJardine 2023（换镜头）；Lashley & Pollock 2020（拉开幕布，inductive 版）——**5 原型，最稳**
- `exploration` 拓荒：补上被忽视的战场，条件化解决——Desai 2012；Malshe 2015（补半区 + 路径分解）
- `unification` 统一：同一机制统一两个分离研究域（2×2 对称映射）——Gamache 2020
- `dimension-split` 维度分裂：对立预测在 DV 不同维度各成立（best of both 处方）——Wowak 2025（paradigms-at-war 裁决类）
- `remedy` 解药：给已知惩罚/低效加解药条件（与 write-theory moderator-as-remedy 手法同族）——Cutolo 2024
- **边界规则**：`remedy`（缓解已知惩罚/低效，惩罚研究已存在）vs `exploration`（补未知战场，子域空白）——cutolo 的惩罚研究已有故为 remedy、desai/malshe 的子域空白故为 exploration
- **倾向配对（非强制）**：paradigms-at-war → arbitration / dimension-split（裁决类）；其余自由组合

### five_acts
```yaml
five_acts:
  exposition: "<Intro（+theory 前段）：背景、角色登场、knot 铺设>"
  rising_action: "<Theory + Methods：张力蓄积、knot 系紧、climax 的 arena 搭建>"
  climax: "<Results 开头：最高张力点/第一揭晓位置>"
  falling_action: ["<解开 + 反转/稳健/补充分析，逐个列>"]
  denouement: "<Discussion：回到开头、意义收口、具体结尾图像>"
```
**定性/理论 overlay（Pollock Fig 2.3/2.4）**：定性论文——context（极端情境）承担 exposition；rising action = 方法可信性蓄积（正当化/多源数据/编码进阶）而非假设张力；climax = Findings 开头的过程模型预览（F1）；falling action = Findings 各关系空间展开（归纳出的理论模型本身是解法）；denouement = 理论化收口。理论论文——theoretical background/review 承担 knot 系紧，falling action = 理论 deliverable 本身。见 lashley2020（定性原型）。

### stakes
```yaml
stakes:
  theoretical: "<理论 stakes（审稿人视角：这问题不解，理论理解缺什么）>"
  practical: "<实践 stakes（现象视角：谁在乎、代价是什么）>"
```

### alternative_tellings（核心资产）
同一 X→Y（可放宽到"同一现象域"）的未被选中的故事版本 + 本文选择哪一版及为什么：
```yaml
alternative_tellings:
  - "讲法A: <版本名> — <一句话讲法>（<谁讲过/谁可能这么讲>）"
  - "讲法B: ..."
  - "本文: <所选版本> — <选择理由>"
```

### storytelling_tools（Ch03，凡可推断即记录）
```yaml
storytelling_tools:
  human_face: "<具体 actor / 案例 / 场景；无则待补>"
  rhetorical_question: "<修辞问 pivot 位置与功能>"
  pacing_notes: "<节奏决策：climax 位置、falling action 反转数、节长分配、多研究起伏>"
  showing_telling: "<图解/比喻/明喻等 showing 手段>"
  voice: "<对话语气特征；未知标待补>"
```
