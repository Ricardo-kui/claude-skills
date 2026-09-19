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



methods 腿 Batch 7 验收 **通过**：骨架索引/借句表/coverage/布尔判据/新资产全链路在真实稿件上闭合。theory/results 两腿仍未跑（各需一次真实生成），仍是两轮方案共同剩余缺口。本记录不写回项目文件；改写示例段以对话交付，由作者决定采纳。
