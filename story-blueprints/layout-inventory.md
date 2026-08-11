# Layout Inventory — 类型 × 五幕布局实证分布（v0.1）

> **数据来源**：59 份 blueprint 的 `five_acts` / `knot` / `storytelling_tools.pacing_notes` 字段（`scripts/extract_layout.py` 提取 + 人工编码，2026-08-09）。
> **现用途**：Legacy Evidence Layer 的历史布局观察，用于发现复读候选与形成反例问题。不得用于选择项目故事框架、调制 write-introduction / write-theory，或推断“商科论文默认”叙事规则。
> **编码口径**：climax 落点分四类——A=Results 开头首揭 / B=主表或具体 Model/Table 揭晓 / C=多研究 Study 级递进 / D=理论揭晓（纯理论论文）。
> **质量保证**：2026-08-09 **全量复核通过（59/59 零差异）**——完整 climax 文本逐份独立判定（`scripts/full_review.py`），A/B/C/D 编码与分布表完全吻合；falling_action 项数双轨解析（extract_layout.py × full_review.py）diff=0。边界口径记录：employee_free_speech 的 climax 叙述主语为 "Results——"（A 型），落点细节在 Study 2-3；kundro2023/hahl2017 的 climax 主语为 "Study N"（C 型）。

## 总体分布（n=59）

| knot 类型 | 样本 | falling_action 项数范围（中位） | climax 落点分布 |
|-----------|------|-------------------------------|-----------------|
| irony-reversal | 8 | 2-6（4） | A×5、B×3 |
| paradigms-at-war | 8 | 3-6（3） | A×7、B×1 |
| neglected-arena | 9 | 3-5（3） | A×6、B×3 |
| overlooked-alternative | 8 | 3-5（4） | A×6、B×2 |
| half-domain-gap | 9 | 2-4（3） | A×6、B×2、D×1 |
| consensus-puzzle | 7 | 2-4（3） | A×4、B×2、C×1 |
| assumption-flip | 6 | 3-4（3） | A×4、B×1、C×1 |
| tangled-constructs | 3 | 3-5（4） | A×1、B×2 |
| cross-domain-unification | 1 | 4 | B×1 |

**历史观察，不是规范**：这 59 篇旧读本中多数 climax 标注为 Results 开头或主表。该分布不能推出“商科实证论文默认 climax 布局”，也不能作为任何项目的写作指令；只有经 v0.4 复审并与当前项目可比的证据才能形成 section-level 学习动作。

## 历史 knot × resolution 联合分布

| knot × resolution | n | 占比 |
|-------------------|---|------|
| half-domain-gap × exploration | 9 | 100% |
| overlooked-alternative × revelation | 8 | 100% |
| irony-reversal × revelation | 8 | 100% |
| paradigms-at-war × arbitration | 7 | 88% |
| neglected-arena × exploration | 7 | 78% |
| assumption-flip × revelation | 6 | 100% |
| consensus-puzzle × revelation | 5 | 71% |
| tangled-constructs × revelation | 3 | 100% |
| consensus-puzzle × remedy | 2 | 29%（cutolo2024、kundro2023） |
| neglected-arena × revelation | 2 | 22%（park2013 逆马太、desjardine2025 信息竞争） |
| paradigms-at-war × dimension-split | 1 | 12%（wowak2025） |
| cross-domain-unification × unification | 1 | 100% |

**实证校准**：
- `revelation` 兼容性最高坐实：irony / overlooked / assumption-flip / tangled **全 100%**；neglected 与 consensus 的主流候选。
- `half-domain-gap → exploration` 是 **100% 强配对**（Step B 若未标此倾向，补上——补半区的解法性格天然是拓荒）。
- `paradigms-at-war → arbitration` 88% + `dimension-split` 12%：裁决类垄断，dimension-split 仅 wowak2025 一例（两极战各赢一维度）。
- 例外值得注意：neglected-arena 里 park2013/desjardine2025 选 revelation（逆马太/信息竞争——"换镜头"而非"拓荒"），consensus 里 cutolo/kundro 选 remedy（解药家族）。

## 逐类型布局样板

### irony-reversal（8 份）——反直觉揭晓型

**样本**：pontikes2012 / desjardine2023 / toh2023 / keeves2017 / darby2024 / wowak2015 / chen2009 / employee_free_speech

- **climax**：A×5（chen2009 主动反果、darby2024 26 天延迟、keeves2017 怨恨 1.5-2 点、wowak2015 dy/dx=0.17、employee_free_speech 受众分裂）+ B×3（desjardine2023 Table 4 Model 2 镜像、pontikes2012 主表双模型镜像系数、toh2023 Model 2 镜像 ±3.2%/18%）
- **falling_action**：2-6 项（中位 4，**全部类型中最宽**——机制检验+边界反转+替代解释空间大）
- **系紧**：intro 反直觉/反转开场（Vioxx、J&J 案例、Epigram）+ 悖论声明；**解开**：Results 首揭"反直觉系数本身"（揭晓内容=反果/镜像，不是普通主效应）
- **布局样板**：① 开场即反转或悖论（hook 能量高）；② Theory 铺"共识单向预期"做靶；③ climax=Results 首段反果/镜像系数揭晓（读者预期被翻）；④ falling_action 宽松（2-6 项）——机制检验、边界反转、替代解释可连放；⑤ denouement 回到开场意象（J&J/Epigram 回响）

### paradigms-at-war（8 份）——裁决揭晓型

**样本**：zhou2017 / wowak2025 / park2025 / shen2022 / bendig2024 / haunschild2004 / csr_decoupling / crash_risk

- **climax**：A×7（裁决揭晓：倒 U 平方项双负、voluntary 胜出、coordinated 胜出、稳定作用、−.339 翻 conventional wisdom、+43% 外生冲击、model-free 均值预览）+ B×1（park2025 Table 6）
- **wowak2025 特殊**：climax 前移——model-free 均值预览（liberal 3.78 vs conservative 5.73）先于 Table 4，倒金字塔节奏
- **falling_action**：3-6 项（中位 3）
- **系紧**：intro 两派相反预测声明（'predicts an opposite effect' / 'two competing hypotheses'）+ 裁决必要性的 stakes；**解开**：Results 开头裁决表/首揭（胜出一方点名）
- **布局样板**：① intro Tension=两派相反预测并置（各给文献锚）；② Theory 可给竞争假设（H 相对立）或单一理论+裁决设计；③ climax=Results 首段"胜负揭晓"（引用胜出方假设）；④ falling_action 含"败方解释的排除/条件化"；⑤ denouement 升维（两派其实各对一半）

### neglected-arena（9 份）——拓荒揭晓型

**样本**：desai2012 / park2013 / eilert2017 / kashmiri2017 / kalaignanam2013 / pupovac2025 / hoffmann2024 / desjardine2025 / top_mgmt_incentives

- **climax**：A×6（渗透揭晓、UD 揭晓 99% 置信、学习效应首揭、自恋 +2.25、传染 −0.40%、激励斜率）+ B×3（desai2012 Tables 2-3、eilert2017 Table 7、park2013 Table 1）
- **falling_action**：3-5 项（中位 3）
- **系紧**：intro 子域空白声明（'none of them examine' / 'largely under-researched'）+ 黑箱/过程空白；**解开**：Results 首揭"空白域的第一张图"
- **布局样板**：① hook 可走数据冲击或现象规模（召回频率增长、Vioxx、黑箱）；② intro Tension=空白声明（被忽视的战场有多重要——stakes 抬升）；③ climax=Results 首揭空白域主发现（常带反直觉地形：severity→更慢）；④ falling_action 边界/条件化+替代解释；⑤ denouement 回到"这片域为什么一直被忽视"

### overlooked-alternative（8 份）——视角翻转型

**样本**：desjardine2022 / lashley2020 / singh2023 / zhao_ding2022 / darby2026 / vadakkepatt2022 / anton2025 / product_market_threats

- **climax**：A×6（亮面揭晓、watchdog 24 天、净效应、'涨潮'首验、H2 暗面 −8.37、Findings 开头 F1）+ B×2（singh2023 Table 4、zhao_ding2022 Table 3/4 双 DV 镜像）
- **falling_action**：3-5 项（中位 4）
- **系紧**：intro "主导视角看漏一面"声明（'neglects' / 'much less work on'）+ 换镜头预告；**解开**：Results 首揭被漏的那面（亮面/暗面/watchdog）
- **布局样板**：① intro 可冷启动（直接进文献共识）或数据冲击；② Tension=视角翻转声明（deductive 宣战或 inductive 从数据长出）；③ climax=Results 首揭"另一面"（常与既有面同表对位）；④ falling_action 含条件化（新视角何时成立）；⑤ denouement 与既有视角调和（互补而非推翻）

### half-domain-gap（9 份）——补半区型

**样本**：malshe2015 / wu2025 / malik2025 / mayo2022 / lun2026 / liu2016 / denicolo2025 / shi2021 / reporting_comparability

- **climax**：A×6（mayo2022 +77%/−52% 双系数、lun2026 EO 正相关、reporting_comparability 溢出揭晓、shi2021 羊群 +4.8-8.9%、wu2025 anti-SLAPP→CSP 主效应、liu2016 H2 β=.477）+ B×2（malik2025 Table 3/4 双轨对位、malshe2015 floodlight 双转折点）+ D×1（denicolo2025 理论揭晓均衡解）
- **falling_action**：2-4 项（**全部类型中最窄**——补半区后收束快）
- **系紧**：intro 双段式——直接效应已做（'Prior literature focuses on...'）/半区空白（'Little is known about...'）+ 半区 pivot（权威/现实落差）；**解开**：Results 首揭补上的半区
- **布局样板**：① intro Tension=互补半区双段式（已做极→空白极）；② Theory 常双轨并行（直接效应机制 + 半区机制）；③ climax=Results 首揭半区效应（可带反直觉：'problem severity → 更慢'）；④ falling_action 收束快（2-4 项：机制+边界即可）；⑤ 与跨学科嫁接常配合（finance→marketing、politics→operations）

### consensus-puzzle（7 份）——复现-消解型

**样本**：cutolo2024 / gamache2023 / kundro2023 / han2020 / fang2025 / haunschild2015 / gao2015

- **climax**：A×4（威胁主导 −50%、条件揭晓缓冲/加剧并存、振荡确认、复现后三交互消解）+ B×2（cutolo 主表三调节、han2020 Table 2 复现+双向调制）+ C×1（kundro2023 Study 1）
- **falling_action**：2-4 项（中位 3）
- **独特节奏（全库最鲜明的类型签名）**：**复现-消解**——climax 段落先复现共识主效应（gamache2023 β=−0.552 复现、han2020 Table 2 复现 0.073***、kundro2023 主效应 b=−.12），**同一段或紧接段揭晓消解条件**（三交互/双向调制/gender 交互）。读者先看到"共识成立"，再看到"共识只在条件下成立"
- **布局样板**：① intro Tension=强共识预测 vs 现实持续违背（puzzle 声明）；② Theory=共识基线 → 异质性/条件推导；③ climax=复现-消解两拍（先复现后消解——消解即揭晓）；④ falling_action 条件地图展开（gao2015 四象限）；⑤ denouement=共识被改写成条件命题

### assumption-flip（6 份）——前提翻转型

**样本**：paruchuri2020 / shipilov2020 / hahl2017 / lovelace2021 / darby2025 / li2026

- **climax**：A×4（PSM −23 天、三主效应+绩效不显著、三向交互、垂直溢出确认）+ B×1（shipilov2020 Model 2/3）+ C×1（hahl2017 Study 1）
- **falling_action**：3-4 项（中位 3，最紧凑）
- **独特节奏**：**replicate-then-flip**（shipilov2020：先 H1a/H2a 复现预期，再 H1b/H2b 翻出反直觉）或挑战先行→替代机制推导（paruchuri2020 三假设批评链、lovelace2021 浪漫领导力前提）
- **布局样板**：① intro=前提挑战声明（Alvesson 问题化家族：'focused almost entirely on' / 效价反转例外）；② Theory=挑战段（旧前提）→ 替代机制推导（新前提）；③ climax=Results 首揭翻转后效应；④ falling_action 紧凑（3-4 项）；⑤ 标题常为问句或俗语翻转（'Is All Publicity Good Publicity?'）

### tangled-constructs（3 份）——拆解揭晓型

**样本**：pollock2015 / han2024 / pfarrer2010

- **climax**：B×2（han2024 Table 7 四交互、pfarrer2010 Table 2/3）+ A×1（pollock2015 堆叠 Wald χ² 裁决瞬间）
- **falling_action**：3-5 项（中位 4）
- **系紧**：intro 构念混同/单向化声明（'focused almost entirely on' 同家族）+ 定义锚定；**解开**：Results 交互/裁决（两个构念的动态关系揭晓）
- **布局样板**：① intro 常冷启动或定义锚定慢铺（pfarrer2010 六段式均匀推进）；② Theory=构念辨析（2×2 矩阵/区分维度）；③ climax=交互表或裁决检验（'哪个方向更强'）；④ falling_action 含构念层面的边界；⑤ denouement=构念关系调和（缓冲/double-edged 矛盾化解）

### cross-domain-unification（1 份）——统一引擎型

**样本**：gamache2020

- **climax**：B×1（Results 主结果 2×2 四格逐格揭晓——expectation→model→coefficient→interpretation→magnitude 循环）
- **布局样板**：① Theory=2×2 对称映射（两分离域共用引擎）；② climax=四格逐格揭晓（每格一轮微揭晓，匀速推进）；③ falling_action 4 项（跨域复制+边界）

## 跨类型节奏观察（写作侧可直接取用）

1. **复现-消解两拍**是 consensus-puzzle 的签名节奏（gamache2023/han2020/kundro2023），**replicate-then-flip** 是 assumption-flip 的签名节奏（shipilov2020）——两者共享"先复现后翻转"的读者预期管理，但消解=条件化、翻转=方向反。
2. **climax 前移**（wowak2025 model-free 均值预览先于主表）是罕见但强效的节奏变体——倒金字塔：全景先于系数。
3. **多研究实验**（hahl2017/kundro2023/employee_free_speech）把 climax 循环化——每 study 一轮揭晓，falling_action 含"机制实验/复现"作为下一轮。
4. **falling_action 项数谱**：half-domain 最窄（2-4，补半区收束快）、irony 最宽（2-6，反转空间大）、tangled 偏宽（3-5，构念边界多）。
5. **揭晓内容**：irony/paradigms 揭晓的是"反直觉/胜负"（内容本身带 surprise）；neglected/half-domain/overlooked 揭晓的是"新地图/新一面"（surprise 在空白本身）；consensus/assumption-flip 揭晓的是"条件/翻转"（两拍结构）。
