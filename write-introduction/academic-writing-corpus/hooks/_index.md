# Hooks 索引 — Pollock 2025 分类体系

本索引按照 Pollock (2025) 的四种 Hook 类型（Quote / Trend / Anecdote / Rhetorical question）组织所有 hooks，并标注其 Gap 强度、验证状态和期刊适配度。

---

## Pollock 类型速查

| Pollock 类型 | 核心机制 | 能量 | 最佳适配 Gap |
|-------------|---------|------|-------------|
| **Quote** | 权威外部声音建立合法性 | 中/高 | Incompleteness / Inadequacy |
| **Trend** | 数据/趋势/模式建立规模感 | 低/中 | Incompleteness / Inadequacy |
| **Anecdote** | 叙事案例建立真实感和共情 | 低/中 | Incompleteness / Inadequacy |
| **Rhetorical question** | 读者自我推理建立参与感 | 低/中 | Incompleteness / Inadequacy |

---

## Quote（引语/权威声音）

| Hook | canonical_id | 核心特征 | 验证状态 | 代表范文 |
|------|-------------|---------|---------|---------|
| **权威引语/新闻个案 Hook** | `02-epigraph-quote-pivot` | 新闻引语/内部文件/沉浸式叙事作为开场 | ROBUST (≥4 papers) | darby2026 (JOM), desjardine2023 (OS), singh2023 (JMR), lashley_pollock2020 (ASQ) |

*Quote 类型当前仅 1 个 hook，但 `02-epigraph-quote-pivot` 包含 4 个变体（新闻个案型、权威声明型、内部文件型、沉浸式叙事型），覆盖范围较广。*

---

## Trend（趋势/数据/模式）

| Hook | canonical_id | 核心特征 | 验证状态 | 代表范文 |
|------|-------------|---------|---------|---------|
| **数据冲击 Hook** | `03-data-shock` | 具体数字 → scale → "yet little is known" | VERIFIED | eilert2017 (JM), vadakkepatt2022 (JM) |
| **文献共识盲点 Hook** | `05-literature-consensus-blindspot` | "While important... considers... broadly" | ROBUST (≥5 papers) | gamache2020 (SMJ), shipilov2020 (SMJ), shen2022 (JOM) |
| **范式挑战 Hook** | `06-paradigm-challenge` | "According to conventional view... In reality, however..." | ROBUST (≥6 papers) | zhou2017 (ASQ), hahl2017 (ASR), gamache2023 (SMJ) |
| **跨学科类比 Hook** | `01-cross-disciplinary-analogy` | 领域A概念 → 领域B类似问题 | VERIFIED (≥2 papers) | pollock2015 (ASQ), malshe2015 (JM) |
| **后果清单 Hook** | `08-consequence-cascade` | 负面事件递进式后果清单 | VERIFIED | mayo2021 (POM) |
| **"Contrary to Belief" Hook** | `12-contrary-to-belief` | 打破普遍认知的制度事实（含变体C：直觉反转保留共识型 habel2016 — "despite its intuitive appeal, this logic may be misleading"） | VERIFIED | eilert2017 (JM), darby2023 (MSOM), habel2016 (JM) |

*Trend 是最丰富的 Pollock 类型（6 个 hooks），覆盖从低能量数据开场到高能量范式挑战的全谱系。*

---

## Anecdote（轶事/叙事/案例）

| Hook | canonical_id | 核心特征 | 验证状态 | 代表范文 |
|------|-------------|---------|---------|---------|
| **沉浸式故事 Hook** | `10-immersive-narrative` | 五幕结构叙事（时间精确、人物有名） | VERIFIED (≥2 papers) | desai2012 (AMJ), lashley_pollock2020 (ASQ) |
| **制度轶事 Hook** | `11-institutional-anecdote` | 客观制度叙事 → "unremarkable"理论常态化 | VERIFIED | lehman2014 (MS) |
| **心理构念直觉 Hook** | `09-psychological-construct-hook` | 压力共识 → 案例落地 → 因果链 → 学术空白 | VERIFIED | mannor2016 (SMJ) |
| **成本收益张力 Hook** | `07-cost-benefit-tension` | 决策两难：行动成本 vs 延迟成本 | VERIFIED | eilert2017 (JM) |
| **实践困境 Hook** | `10-practical-puzzle` | 从业者面临的具体困境 | VERIFIED (≥3 papers) | ceo_regulatory_focus_ijrm (IJRM), desjardine2023 (OS), kalaignanam2017 (JM) |
| **谜题/悖论 Hook** | `04-puzzle-paradox` | 反直觉现象，制造认知失调 | VERIFIED (≥4 papers) | paruchuri2020 (SMJ), pontikes2012 (ASQ) |
| **成对灾难 Hook** | `14-paired-disasters` | 两次时间跨度大的相似灾难，建立"历史重演"谜题 | VERIFIED | haunschild2015 (OS) |

*Anecdote 类型有 7 个 hooks，覆盖从完整叙事到精简案例的多种长度。注意：`04-puzzle-paradox` 同时包含 Trend 元素（反直觉数据）和 Anecdote 元素（第二人称推理），但因其核心功能是叙事性 puzzle，归入 Anecdote。*

---

## Rhetorical question（修辞问句）

| Hook | canonical_id | 核心特征 | 验证状态 | 代表范文 |
|------|-------------|---------|---------|---------|
| **修辞问句 Hook** | `13-rhetorical-question` | 日常选择三联 → 读者自我确认 → 概念转译 | VERIFIED (≥2 papers) | gomulya2019 (SMJ), paruchuri2020 (SMJ) |

*Rhetorical question 是最新补充的 Pollock 类型，此前在语料库中完全缺失。*

---

## 按 Gap 强度选择 Hook

| Gap 强度 | 推荐 Hooks（按 Pollock 类型分组） |
|---------|--------------------------------|
| **低** | Trend: `03-data-shock`, `08-consequence-cascade` <br> Anecdote: `10-practical-puzzle`, `09-psychological-construct-hook` <br> Rhetorical: `13-rhetorical-question` |
| **中** | Trend: `05-literature-consensus-blindspot`, `01-cross-disciplinary-analogy`, `12-contrary-to-belief` <br> Anecdote: `04-puzzle-paradox`, `10-immersive-narrative`, `11-institutional-anecdote`, `07-cost-benefit-tension` |
| **高** | Trend: `06-paradigm-challenge` <br> Quote: `02-epigraph-quote-pivot` <br> Anecdote: `14-paired-disasters` |

---

## 按期刊选择 Hook

| 期刊 | 偏好 Pollock 类型 | 推荐 Hooks |
|------|------------------|-----------|
| **ASQ** | Quote > Trend (理论) | `02-epigraph-quote-pivot`（经典理论引语）, `06-paradigm-challenge` |
| **ASR** | Quote > Trend (理论) | `02-epigraph-quote-pivot`（理论象征文本）, `06-paradigm-challenge` |
| **SMJ** | Trend (数据) ≈ Anecdote | `03-data-shock`, `06-paradigm-challenge`, `04-puzzle-paradox`, `13-rhetorical-question` |
| **AMJ** | Anecdote ≈ Rhetorical | `10-immersive-narrative`, `09-psychological-construct-hook`, `13-rhetorical-question` |
| **OS** | Anecdote > Trend | `11-institutional-anecdote`, `07-cost-benefit-tension`, `04-puzzle-paradox` |
| **JM/JMR** | Trend (数据) | `03-data-shock`, `08-consequence-cascade`, `12-contrary-to-belief` |
| **JOM** | Trend ≈ Anecdote | `02-epigraph-quote-pivot`（监管/召回）, `07-cost-benefit-tension`, `08-consequence-cascade` |
| **MS** | Anecdote | `11-institutional-anecdote` |

---

## 互斥矩阵

以下 Hooks **不能同用**（一个 Introduction 只能有一个 Hook）：

| 冲突对 | 原因 |
|--------|------|
| `02-epigraph-quote-pivot` + `03-data-shock` | 情感/叙事张力 + 数据冲击 = 信息过载 |
| `02-epigraph-quote-pivot` + `06-paradigm-challenge` | 现实案例 vs 理论颠覆，焦点分裂 |
| `02-epigraph-quote-pivot` + `13-rhetorical-question` | 外部声音 vs 读者声音，叙事机制冲突 |
| `03-data-shock` + `06-paradigm-challenge` | 低能量数据 vs 高能量颠覆，能量不匹配 |
| `03-data-shock` + `08-consequence-cascade` | 两者都依赖数字，造成数字疲劳 |
| `10-immersive-narrative` + `13-rhetorical-question` | 叙事沉浸 vs 主动推理，读者参与机制冲突 |

---

## 必须配对（Hook → Tension）

| Hook | 必须配对的 Tension | 原因 |
|------|-------------------|------|
| `06-paradigm-challenge` | `04-reality-contradicts-consensus` | 高能量颠覆需要高能量 Gap 支撑 |
| `05-literature-consensus-blindspot` | `02-implicit-assumption-wrong` 或 `03-structural-blindspot` | 共识建立后需要系统性盲点的解释 |
| `03-data-shock` | `01-despite-progress-unaddressed` | 数据建立 stakes，递进缺口转化为学术问题 |
| `04-puzzle-paradox` | `02-implicit-assumption-wrong` | puzzle 需要假设错误的解释 |
| `12-contrary-to-belief` | `02-implicit-assumption-wrong` | 反差直接证明隐性假设错误 |
| `07-cost-benefit-tension` | `01-despite-progress-unaddressed` 或 `08-cost-vs-benefit` | 决策困境需要文献如何/未如何处理的解释 |
| `14-paired-disasters` | `13-sequential-phenomenon-gap` | 极端案例建立的修正-复发谜题需要 sequential cycling 缺口来解释 |

---

## 编号总览

| 编号 | Hook 名称 | Pollock 类型 |
|------|----------|-------------|
| 01 | cross-disciplinary-analogy | Trend |
| 02 | epigraph-quote-pivot | Quote |
| 03 | data-shock | Trend |
| 04 | puzzle-paradox | Anecdote |
| 05 | literature-consensus-blindspot | Trend |
| 06 | paradigm-challenge | Trend |
| 07 | cost-benefit-tension | Anecdote |
| 08 | consequence-cascade | Trend |
| 09 | psychological-construct-hook | Anecdote |
| 10 | immersive-narrative | Anecdote |
| 10 | practical-puzzle | Anecdote |
| 11 | institutional-anecdote | Anecdote |
| 12 | contrary-to-belief | Trend |
| 13 | rhetorical-question | Rhetorical question |
| 14 | paired-disasters | Anecdote |

*注：编号 10 被 immersive-narrative 和 practical-puzzle 共享。这两个 hook 分别由不同 distill 文件提取，保留原编号以维持向后兼容。*

---

## 新增 Hook（待编号）

| Hook | 核心特征 | 验证状态 | 代表范文 |
|------|---------|---------|---------|
| **Cold-Start Cost Cascade Hook** | `cold-start-cost-cascade` | 从 dreaded word 到直接/间接成本递进 | VERIFIED | mayo_poms (POM) |

- cold-start-cost-cascade.md — Cost cascade hook from dreaded word to direct/indirect costs

---

## 新增 Hook（编号 21）

| Hook | canonical_id | 核心特征 | 验证状态 | 代表范文 |
|------|-------------|---------|---------|---------|
| **双行业趋势对比 Hook** | `21-dual-industry-trend` | 数字化/宏观趋势 → 两个行业的对比案例建立现象普遍性 | EMERGING (1 paper) | zhao-ding_gaba (ORSC) |

- `21-dual-industry-trend` — Trend/Phenomenon Hook: macro-trend → dual-industry contrasting examples → "Across [contexts], firms not only [A] but also choose among [B], deciding [trade-off] across multiple dimensions." 适用于需要建立"跨行业普遍现象"可信度的研究。Pollock 类型: Trend。能量: 中。最佳适配 Gap: Inadequacy（首选，依据 P35 "challenges an implicit premise... mechanically translate into" 语言）/ Incompleteness（适配）× Constructs + Phenomenon。canonical 文件已于 2026-06-17 创建。

---

## 新增 Hook（编号 22）

| Hook | canonical_id | 核心特征 | 验证状态 | 代表范文 |
|------|-------------|---------|---------|---------|
| **同时异果对比 Hook** | `22-paired-simultaneous-incidents` | 同一天、同规模、不同媒体反应的对比案例→ Puzzle question | EMERGING (1 paper) | han_pollock_paruchuri (SMJ) |

- `22-paired-simultaneous-incidents` — Anecdote/Puzzle Hook: "On [date], [Firm A]'s [N] million users were exposed... The same day, [Firm B] had exposed [N] million users... Although similar in magnitude, [Firm B]'s breach was only covered by specialist media. Why were two incidents of similar magnitude that occurred at the same time publicized to different extents?" 适用于 misconduct/scandal/event studies。Pollock 类型: Anecdote。能量: 中。最佳适配 Gap: Incompleteness × Constructs + Boundary。

---

## 新增 Hook（编号 23）

| Hook | canonical_id | 核心特征 | 验证状态 | 代表范文 |
|------|-------------|---------|---------|---------|
| **流行观点对立 Hook** | `23-popular-debate` | TED talk vs 畅销书对立观点 → "This debate illustrates..." pivot → 学术 gap | EMERGING (1 paper) | falchetti2022 (SMJ) |

- `23-popular-debate` — Anecdote Hook: "In an exceptionally popular [TED talk], [Author A] argues... [Author B], on the other hand, in [their best-selling book], points out... This debate illustrates one of the central challenges..." 两个大众文化中的对立观点并置→争论的 resolution 不在 A vs B 本身，而在被双方忽略的 contingency factor。Pollock 类型: Anecdote。能量: 中。最佳适配 Gap: Incompleteness × Boundary + Constructs。禁忌: ASQ 投稿避免使用（偏好理论深度而非 practitioner relevance）。
