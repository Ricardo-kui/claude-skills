---
kind: worked-example
derived_from: [anton2025, ball2018, darby2026, hoffmann2024, lu2022, wowak2020]
runtime_eligibility: no
created: 2026-09-14
---

# Worked Example: Portfolio Governance / External-Actor Objective

> **定位**：本文件是**管线的使用示范**（worked example），不是规则来源。它不参与故事类型选择、不进 `../catalog.json`、不被 `../../scripts/retrieve_exemplars.py` 返回（与 `write-introduction/references/library-contract.md` 边界 2 一致）。
> **单源纪律**：只保留本项目适配后的成品段落 + 每段底本 id 引用 + 槽位说明 + 为什么这样换。原始底本全文在 `write-introduction/corpus/_skeleton/`，失败写法在 `write-introduction/corpus/contrast-pairs/`，本文件均不复写。
> **适用**：论文核心故事是「一个跨越多个单位的结构性条件，通过改变行动者的目标或外部性权重，塑造一个双边际治理结果；边界条件由该结构本身的机制推出」。形状与可用底本清单见 `write-introduction/corpus/packs/portfolio-governance.md`。

**本文型范例（原 archetype 头部；Wowak 引注已修正为 catalog 实有卡）**：
- anton2025, Management Science — ownership topology + two opposed cross-firm payoffs
- denicolo2025, Management Science — softened competition vs weakened monitoring
- lu2022, Management Science — common ownership → concrete firm action
- wowak2020, M&SOM — severity assigns count vs timing decision margins（原写「Wowak et al. 2021, MSOM」错误；catalog 实有卡为 `wowak2020`）
- ball2018, SMJ — competition → manufacturing recalls + discretion
- darby2026, JOM — external monitoring + unified opacity boundaries

## P1 Hook：先立裁量空间，再引入结构性条件

**本项目适配后的成品段落**

> "A fundamental premise of [safety regulation] is that firms will convert known defects into timely corrective action. [Actor discretion] complicates this premise. Firms choose [design, investigation, initiation]. The [outcome] therefore reflects [more than incidence]; it also records [conversion into public action]."

**底本 id 引用**：模板底本 ball2018 / wowak2020；verbatim 补位 `03-data-shock#3`（darby2025，裁量空间）、`03-data-shock#8`（lu2022，跨单位条件 + 行为轶事）。

**槽位说明**：结构性条件 = common institutional ownership between rivals；双边际结果 = annual serious recall count（defect occurrence + initiation willingness）；裁量来源 = problem investigation and recall initiation。

**为什么这样换**：ball2018 / wowak2020 在本库无 verbatim 锚，故以模板承担「裁量空间→结构条件」句法，用同功能索引 verbatim 补「裁量」与「跨单位」两个承重点；「reflects more than incidence」正是把结果从质量读数改写为治理读数的关键换血。

## P2 Literature turn：内部治理 → 外部压力 → 所有权条件

**本项目适配后的成品段落**

> "Research on [recall governance] has largely been limited to [internal decision makers]. Recent work has begun to extend this view to [external pressures]. [Closest paper] show that [their finding], but their account retains a [focal-firm premise]. [Our structural condition] complicates that premise because [outcome redistributes value across units]."

**底本 id 引用**：模板底本 darby2026 + hoffmann2024；verbatim `03-disciplinary-gap-stakes#1`、`02-actor-funnel#1/#2/#3`（darby2026）、`01-progressive-coherence#4`（hoffmann2024）。

**槽位说明**：closest paper = Darby et al. 2026；focal-firm premise = monitoring capacity anchored in the monitored firm；structural condition = ownership spanning product-market rivals。

**为什么这样换**：用 darby2026 的文献段骨架把 closest paper 的 focal-firm premise 点出来，再用 hoffmann2024 的 progressive-coherence verbatim 把对话从「只盯内部」推到「外部压力」再落到所有权条件——避免把本文化约为又一篇内部治理研究。

## P3 Theory lens：先摆对立机制，再给裁定

**本项目适配后的成品段落**

> "A first reading is that [X should increase Y]. [Rival mechanism]. We develop the opposing account. [Our mechanism: motive + means]. [Conditional mechanism language]."

**底本 id 引用**：模板底本 anton2025；verbatim `02-dual-theory-layered#1/#2`（hoffmann2024）、`01-agency-theory-standard#2`（darby2026）。

**槽位说明**：rival mechanism = weakened monitoring / quiet life → more recalls；our mechanism = spillover internalization（motive）+ competition softening（means）→ fewer recalls；conditional language = `can` / `may` / `we theorize`。

**为什么这样换**：anton2025 / denicolo2025 在本库只有填槽模板、无 verbatim 锚，故以 anton2025 模板承载「对立机制→裁定」节奏，用 hoffmann2024 的两套治理机制句作 verbatim 支撑；条件化语言把未观察机制写成 `can/may`，避免 `is/shows` 式上帝视角。

## P4 Boundary：一个构念统摄两个边界

**本项目适配后的成品段落**

> "We then consider possible boundary conditions by examining [N] features of [one theoretical dimension]. Both are grounded in [the same logic]. [Boundary 1 definition + mechanism]. [Boundary 2 definition + mechanism]."

**底本 id 引用**：模板底本 darby2026；verbatim `03-unified-moderator-framework#1`（darby2026）。

**槽位说明**：one dimension = partial nature of internalization；boundary 1 = competitive proximity（meaningful rivalry to internalize）；boundary 2 = competitive potency（force to alter discipline given outside leaders）。

**为什么这样换**：用一个理论构念（internalization 的不完全性）统摄两条边界，避免「独立情境加成」失败写法——两条边界共享同一逻辑，而非并列的三个条件分量。

## P5 Preview：量级 + 一次集中披露边界

**本项目适配后的成品段落**

> "To test these arguments, we combine [data]. [Sample and estimator]. [Main magnitude]. [One honest boundary sentence]. [One supplementary-evidence sentence]."

**底本 id 引用**：模板底本 lu2022 / darby2026；verbatim `findings-preview#12/#13`、`mechanism-preview#21/#22`、`01-despite-progress-unaddressed#14`（lu2022）、`findings-preview#4`（wowak2025）。

**槽位说明**：main magnitude = one-standard-deviation increase → 22.3% reduction；boundary sentence = proximity interaction under one alternative measure / potency interaction under firm-clustered inference；supplementary sentence = adverse events + longer initiation times（只出现一次）。

**为什么这样换**：把边界披露压成一句集中句（而非散点 caveat），主量级用 lu2022 的经济显著性 verbatim 支撑；用 wowak2025 的样本规模句收束，避免防御堆叠。

## P6 Contribution：理论问题转变 + 实践/政策收束

**本项目适配后的成品段落**

> "Theoretically, we contribute to [literature] by changing the question from [capacity question] to [objective question]. [Closest paper] show [capacity]. [Our condition] changes [valuation]. We also extend [explaining literature] by showing [when the condition has force]. For practice, [implication]. For public policy, [bounded implication]."

**底本 id 引用**：模板底本 hoffmann2024 + darby2026；verbatim `three-layer-contribution#3`、`01-despite-progress-unaddressed#27`（hoffmann2024）、`contributions-index#11/#12`（wowak2025）、模板 id `01-agency-theory-standard#T3`（darby2026）。

**槽位说明**：capacity question = how strongly an investor can monitor one firm；objective question = which firms' consequences enter the investor's governance calculus；explaining literature = common ownership / competition internalization；bounded implication = fewer recalls are not an unambiguous safety gain。

**为什么这样换**：贡献不写成「我们做了 X」，而写成问题转换（能力问题 → 目标函数问题），再用 hoffmann2024 的贡献锚定与 wowak2025 的双价值 verbatim 支撑；实践与公共政策分开、政策侧有界收束，避免把治理读数写成安全收益。
