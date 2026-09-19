# write-methods 真实生成验收记录（Batch 7 methods 腿，2026-09-19）

- 输入：`D:\OneDrive\Obsidian Vault\00 工作台\项目\共同所有权 × 产品召回\00 Active\Methods_H1_替换稿_20260903.md`（GPT 交接的管线前稿件，frontmatter `authority_map_signed: 2026-09-11`，文内无修订记录）。
- 项目上下文：Story Contract（stage=refining, status=confirmed, evidence_state=mixed；权威边界含 D-20260910-05「DV 可靠质量代理句不重开」）。
- 执行方式：write-methods 全协议 revision 模式（Phase -1 → Phase 0 → 槽位定轴 → 大纲/借句表 → 底本对齐改写 → 生成后检查），主会话执行。

## 判定（Batch 7 验收四问）

| 验收问 | 判定 | 证据 |
|---|---|---|
| 底本 id 在场？ | **是** | G1 借句表 9 个论证位中 7 个锚定 `_skeleton` 真实 id（rare-outcome#T1/T2/T3、construct-object#T4/T10/T11/T13、panel-ols#1/#40），每 id 经 `--verify` 门保证回源可核 |
| coverage 可计算？ | **是** | 论证型分母 9（程序性豁免：公式陈述×2、数据源清单×1）；有底本 id 7 → **coverage 77.8%**；两 self-drafted 位见下方语料缺口 |
| 段级来源可核？ | **是** | 大纲表逐段来源列（id / self-drafted / framing-exempt），豁免口径按 outline-protocol §六 |
| 完成判据布尔？ | **是** | Phase -1（revision 模式✓现稿已读✓约束已提✓）；Phase 0（storyline S1–S4→构念/变量/模型映射✓ refining+confirmed✓无可检验性缺口✓）；即时范文（revision 范围按协议跳过✓）；生成后检查（反模式 0 命中、设计排他性 0 违反、[placeholder] 0 残留） |

## 新资产首次实战

- **`_shared/function-map.md`**：消费 ✓（词汇档位列 → causal-hedging 面板默认档核对 M7 措辞）。
- **`_shared/consumption-log.md`（F5 单源）**：消费 ✓（`fitness_ledger.py log-consumption` 按单源样板落账成功，输出「consumption 已落账」）。
- **`_skeleton` 借句链**：消费 ✓（INDEX 定轴→稀有结果+实证对象构建+panel-ols 三库取 id）。

## 语料缺口发现（真实运行暴露，待蒸馏补）

1. **测度家族比较段缺变体**：IV¶3（MHHI/holdings/incentive 三族对比地图）全库无锚——GGL/kappa/He-Huang 类测度选择争论是共同所有权文献 Methods 高频段位，建议下次蒸馏该族论文时补「测度家族比较与选择辩护」变体（建议载体：`实证对象构建.md`）。
2. **M5 构造边界句轻锚**：moderator 公式段的「The measure is not constructed as…」边界辩护句仅有 pollock#T4 家族影子，无直接变体；优先级低于 1。

## 事后纠错（2026-09-19 用户质询触发）

M7 示范改写初版开场借用了 `rare-outcome#T3`（lun2026）的 extensive/intensive margin 术语——被用户质询"有前例吗"后查证：①该术语全库仅此一条 verbatim（单源 EMERGING），按证据分档纪律不作默认；②lun2026 用 margin 分解是为**二元化 DV** 辩护，与本稿保留计数的 Poisson 设定论证方向相反（借结构借反了箭头）。已换锚 `rare-outcome#T1`（zorn2017 "low base rate" 白话框架）出修正版。**教训入账：EMERGING 单源术语/句式在真实改写中极易被当默认借用——G1 借句表应给 EMERGING 底本加显式"单篇来源"标注位（现状只标状态列，改写时不醒目）。**

**M7 改写 v3（同日，用户要求充分调研后重制）**：全库扫 panel-ols(95)/非线性模型(22)/稀有结果(3) 的 M7 行 + Poisson/QMLE 全文命中——锚点由单源升级为四锚多刊 verbatim：`rare-outcome#1`（zorn2017 SMJ 低基率白话开场）+ `nonlinear#2`（Haunschild 2015 均值-方差违约**问题句**，与 QME 解法构成问题-解对仗）+ `nonlinear#12`（Vidal & Mitchell 2015 OS "保留 Poisson"决策句型，单源 EMERGING 仅结构借用）+ `nonlinear#7`（Desai 2011 AMJ 全零单位"do not add information"**末句直接前例**）。Wooldridge 引证/FE 理由/within-firm 识别三句原稿保留；未虚构任何未做检验。**调研教训：首轮只扫了稀有结果 3 变体即动笔（锚定不足）；非线性模型库才是计数估计器辩护的主库——M7 类借句应先按槽位横扫全设计类型库再选锚。**

**M7 改写 v4（同日，用户第二轮质询触发）**：v3 两处 AI 腔被用户抓出——"we modeled"（model 作动词；write-results 语言锁早有禁令但仅装在 results 侧，Methods 写作未被拦住）与成对破折号插入语。v4 修正：model→estimate（语言锁法定替换词）、破折号清零。**两条规则已家族化入 `_polish-protocol.md` AI 腔速查表 #14（model 动词）/ #15（破折号过密）**。结构性教训：write-results SKILL 第 7 条语言锁原为 results 专属，跨节写作时不可见——动词类硬锁应收口到家族 SSOT（速查表）而非单节内联。

**M7 改写 v5（同日，用户第三轮质询"仍需润色减 AI 痕迹"）**：以速查表 15 型+流畅性门自查 v4，定位三病灶——#13 拼装长句（55 词三动作分号链）、#8 节奏单调（六句等长 21–27 词）、"稀有"冗余双说；元病灶=**改写者增量膨胀**：作者原稿本是语料库式短句一句一动作节奏，v1–v4 持续加饰。v5 回到作者骨架，仅补两个语料锚动作（`nonlinear#2` haunschild 方差关切短句、`nonlinear#7` Desai "contribute no information" 全零退出理由），三句原稿原样保留，句长节奏 24/13/26/24/24/27，破折号/冒号/分号全零。**教训：改写默认保留作者原句骨架、只插缺的动作；对已近语料节奏的稿件，任何"顺手升级"式修饰都是 AI 痕迹。**



methods 腿 Batch 7 验收 **通过**：骨架索引/借句表/coverage/布尔判据/新资产全链路在真实稿件上闭合。theory/results 两腿仍未跑（各需一次真实生成），仍是两轮方案共同剩余缺口。本记录不写回项目文件；改写示例段以对话交付，由作者决定采纳。
