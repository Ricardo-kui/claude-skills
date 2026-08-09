# Knot Architecture Modulation — frame_type 对假设架构的约束（v0.1）

> **定位**：`story.story_frame.frame_type` 选定后，本文件提供该 knot 类型对 Theory 假设**架构**的约束（假设结构形态、机制推导次序、条件化位置）。形式化现有 Story gate 的 "Theory is rising action"——knot 类型决定 rising action 的骨架。
> **原则**：frame_type 是**架构调制不是路由轴**——7 种理论构建变体（构念辨析型 A / 机制推演型 B / 假设树型 C / 质性过程理论型 D / 调节效应型 E / 竞争假设型 F / 辩证对立型 G）仍由 Gap×Makadok 矩阵选定；本文件只约束选定变体内部的**假设组织形态**。story_frame 缺失时跳过，走默认路径。
> **实证锚**：blueprint 假设结构 + `../../../story-blueprints/layout-inventory.md` 逐类型节（59 份聚合，2026-08-09）。

## 架构检查（Story gate 后执行，非门禁）

若 `story.story_frame.frame_type` 存在，生成假设前对照下表检查目标架构与 knot 签名是否一致；不一致时在输出中标注架构偏差与理由（或建议回契约调整 frame_type）。

| frame_type | 签名假设架构（实证） | 与变体组合要点 |
|-----------|--------------------|---------------|
| irony-reversal | 双边/对立假设（同一 X 对两类 Y——H1a/H1b 镜像对置）或反果型单假设（主效应本身就反直觉）；机制段必须含"为什么反直觉成立" | 变体 A/B 均可；镜像对置=keeves2017/pontikes2012 形态，反果单假设=darby2024/chen2009 形态 |
| paradigms-at-war | 竞争假设（H 相对立，各扎根一阵营——'two competing hypotheses'）或裁决型单假设（'predicts an opposite effect' 声明后单方向检验） | 变体 F 天然契合；裁决型可走 B 单轨 + 竞争声明 |
| neglected-arena | 主效应型 H1（空白域主效应）+ 条件化 H2+（'何时'问题）；机制推导=空白为什么存在 | 变体 B/E；desai2012 对峙→条件化序列 |
| overlooked-alternative | 替代视角主假设（与既有视角对位）；常双 DV 镜像（同一 X 对两个 DV 相反/互补） | 变体 B；zhao_ding2022 双 DV 镜像、malik2025 双轨 |
| half-domain-gap | 双轨并行：直接效应 H1（已做极复现）+ 半区效应 H2/H3（空白极）+ 机制假设 | 变体 B 双轨；reporting_comparability H1-H4（直接+两溢出+机制）、wu2025 双轨 |
| consensus-puzzle | **复现-消解架构**：H1 复现共识主效应 → H2/H3 揭晓消解条件（异质性/边界） | 变体 E 天然契合；gamache2023 复现 β=−0.552 后三交互、han2020 Table 2 复现+双向调制 |
| assumption-flip | 挑战先行→替代机制：挑战段（旧前提为什么可疑，可引 Alvesson 五类定位）→ 替代机制推导 → 条件化假设（Given 格式） | 变体 B；paruchuri2020 三假设批评链→条件化、shipilov2020 replicate-then-flip（复现假设+翻转假设） |
| tangled-constructs | 构念辨析先行（定义锚定/2×2 矩阵）→ 交互或裁决假设（'哪个方向更强'） | 变体 A 天然契合；pollock2015 H1a/H1b 方向裁决、han2024 四交互 |
| cross-domain-unification | 2×2 对称映射（两域×两条件四格假设，逐格推导） | 变体 B 对称并行；gamache2020 四格循环 |

## 逐类型架构细节（实证样板）

### irony-reversal（8 份）
- **双边镜像形态**（受众/对象分裂）：H1a/H1b 对置（同一 X，两类 Y 相反——keeves2017 H1a/H1b 逢迎→怨恨、pontikes2012 双独立模型镜像系数）；机制段=同一机制的两面如何在不同对象上分化。
- **反果单假设形态**（行动反果）：H1 主效应本身就反直觉（darby2024 持股→更慢召回；chen2009 主动→更受罚；wowak2015 期权→更多召回）；why-chain 的 punchline 是"为什么激励反噬"（规避/信号机制）。
- **机制要求**：反直觉必须有机制依据——不是惊悚，是机制驱动的 surprise（规避激励/可见性不对称/信息失真）。

### paradigms-at-war（8 份）
- **竞争假设形态**：H 相对立，各扎根一文献阵营，对称推导（'on the one hand... on the other hand...'）；climax=Results 裁决（胜负揭晓）。csr_decoupling 双竞争假设、shen2022 拆地整合（分解后逐项假设）。
- **裁决单轨形态**：'predicts an opposite effect' 声明后单方向检验（crash_risk）；机制段必须排除败方解释（rival mechanism 逐条排除）。
- **纪律**：两派各自要有完整立场与证据（anti-strawman 硬约束）；败方解释在 falling action 排除或条件化。

### neglected-arena（9 份）
- **主效应+条件化**：H1=空白域主效应（常带反直觉地形——eilert2017 severity→更慢）；H2+=条件化（审视度/相似性/边界——desai2012 '何时防御'）。
- **机制推导**：为什么这个子域被忽视 + 为什么空白域里效应成立（注意力转移/结构盲区）。

### overlooked-alternative（8 份）
- **对位假设**：替代视角主假设与既有视角形成对位（desjardine2022 涨潮 vs 竞争危害）；双 DV 镜像（zhao_ding2022 dissatisfaction 正/heterogeneity 负——同一 X 对两个 DV 的互补证据）。
- **机制推导**：替代面为什么被看漏（manage vs remove 的路径差异——lashley2020）。

### half-domain-gap（9 份）
- **双轨并行**：H1 直接效应（已做极——可为复现或延伸）+ H2/H3 半区效应（空白极）+ 机制假设（两机制——reporting_comparability 共同审计师/相似会计实务）。双轨共享理论 trunk（malik2025 双轨机制 current→IM/prospective→反 IM）。
- **注意**：与 consensus 的"复现-消解"不同——half-domain 的双轨是**对称并行**（两半区独立成立），consensus 是先复现后消解（共识被条件化）。

### consensus-puzzle（7 份）
- **复现-消解架构（签名）**：H1=复现共识主效应（理论段给共识基线——'prior work predicts...'）→ H2/H3=消解条件（异质性/边界/交互）。climax=Results 中消解揭晓。
- **机制推导**：共识为什么在平均层面成立 + 什么条件让它失效（审视信息处理/权力不对称/情境调制）。

### assumption-flip（6 份）
- **挑战先行**：挑战段=旧前提为什么可疑（引反例/悖论/边界案例——paruchuri2020 例外收窄）；联 diagnose Step 3.5 五类假设定位。
- **替代机制** → **条件化假设**（Given 格式——paruchuri2020 条件假设）；replicate-then-flip 形态=先复现预期假设再翻转假设（shipilov2020）。

### tangled-constructs（3 份）
- **辨析先行**：定义锚定/2×2 矩阵（构念区分维度）→ 交互假设（动态关系）或裁决假设（'哪个方向更强'——pollock2015 堆叠 Wald χ²）。
- **机制推导**：两构念为何被混同（历史/测量/理论传统）+ 区分后的动态关系。

### cross-domain-unification（1 份）
- **2×2 对称映射**：两分离域×两条件四格假设，逐格推导（expectation→model→coefficient→interpretation→magnitude 循环——gamache2020）；共享机制声明在开头。

## 联动

- 与 write-introduction：frame_type 来自 Introduction 输出的 `story.story_frame`（story-modulation.md 消费同一字段做 Intro 模块调制——Intro 调制 Theory 骨架：intro Tension 预告什么，Theory 就铺什么架构）。
- 与 Results：knot 签名架构决定 climax 落点（layout-inventory 逐类型节）；复现-消解架构的 Results 必须两拍呈现。
- 与 QC：`theory-review` / `pollock-qc` 检查假设结构与 frame_type 签名一致性（对照本文件表）。
