# Journal Fit — 期刊适配画像表（证据化重写，v0.2）

> 由 write-introduction 在用户提及目标期刊时**读取**（期刊差异优先于通用规则）。
> **重写依据**：方案 §8 Decision D-01（完成判据由「每取值附 ≥5 卡证据」改为四类**来源标签**）。本表遵循 `catalog≥5`（同 outlet ≥5 张 v4 卡，标卡 id）｜`corpus-hooks`（`corpus/hooks/*.md` 的 `## 期刊适配` 表）｜`routing-journal_styles`（`corpus/_routing_tables.yaml` §9）｜`未核查`。
> **证据层级纪律**：`corpus-hooks` 与 `routing-journal_styles` 都是**语料手工证据，非范文现货证据**（证据基是 MVP30 / distills，不是 78 张 v4 卡）；证据不足处一律 `未核查`，不用手工印象补。
> **表结构**：行 = outlet，列 = 13 列（`outlet` + 12 个画像维度）。方案 §8 D-01 称「13 个画像维度」，将 `outlet` 计入列数。

**来源标签速记**（格内）：
- `⟨H:…⟩` = `corpus-hooks`，列出 hooks 卡编号；对应文件 `corpus/hooks/<编号>-*.md`。
- `⟨R:§9:<行号>⟩` = `routing-journal_styles`，位置 `corpus/_routing_tables.yaml` 该行。
- `catalog≥5` = 同 outlet v4 卡 ≥5 张（本表无格达标，见下「catalog 口径」）。
- `未核查` = 本机证据不足。

| outlet | Hook 类型偏好 | 现象 vs 理论起点 | Stakes 形态 | Contribution 写法（t/p/p 配比） | 显式 RQ | Differentiation 段 | robustness preview 容忍度 | 显式 caveat 容忍度 | 具名案例容忍度 | 段落节奏 | 元句容受 | 段数区间 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **ASQ** | 理论引语/经典文本 · 制度轶事 · 范式挑战；忌纯数据开场 ⟨H:02,06,11,18；反例 03⟩ | 理论起点 ⟨R:§9:418⟩ | 未核查 | 理论整合 · facet 分解 · 反讽对仗；t/p/p 配比 未核查 ⟨R:§9:419⟩ | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 |
| **ASR** | 经典理论引语 · 范式挑战；忌社会事件/新闻引语 ⟨H:02,06,16⟩ | 理论起点 ⟨R:§9:439⟩ | 未核查 | 理论深度优先，实验设计概述在后；t/p/p 配比 未核查 ⟨R:§9:440⟩ | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 |
| **AMJ** | 沉浸式叙事 · 读者共鸣（Rhetorical question） · 制度轶事 ⟨H:04,11,13,24,25⟩ | 现象起点 ⟨R:§9:429⟩ | 未核查 | 机制链清晰 · 三维度贡献；t/p/p 配比 未核查 ⟨R:§9:430⟩ | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 |
| **SMJ** | 反例+数据 · 辩论驱动 · 声誉/信号反问 · 跨行业案例 ⟨H:07,12,13,17-debate,24,25⟩ | 现象/反例起点 ⟨R:§9:424⟩ | 未核查 | 多层次贡献 · 理论精细化；t/p/p 配比 未核查 ⟨R:§9:425⟩ | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 |
| **JM** | 数据冲击 · 成本收益张力（决策困境） · 反直觉 ⟨H:03,07,12⟩ | 现象/数据起点 ⟨R:§9:444⟩ | 未核查 | 管理相关性+理论机制；t/p/p 配比 未核查 ⟨R:§9:445⟩ | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 |
| **JMR** | 同 JM/JMR 合并表：数据冲击 · 成本困境 · 营销后果 stakes ⟨H:03,07,11,24⟩ | 现象/数据起点 ⟨R:§9:444⟩ | 未核查 | 管理相关性+理论机制；t/p/p 配比 未核查 ⟨R:§9:445⟩ | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 |
| **MS** | 制度轶事 + 理论共识 ⟨H:11⟩ | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 |
| **POM** | 供应链/运营传染轶事（与 JOM/MSOM 同列） ⟨H:26⟩ | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 |
| **OS** | 实践张力→理论 puzzle · 制度冲突 · 经典辩论+实证 pivot ⟨H:02,04,07,10-practical,14,16,17-debate⟩ | 现象起点 ⟨R:§9:434⟩ | 未核查 | 系统性/结构性论证；t/p/p 配比 未核查 ⟨R:§9:435⟩ | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 |
| **JOM** — 未核查 — 需先向 v4 卡扩样 ≥5 篇 JOM 论文（现 1 张，`darby2026`） | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 |
| **JMS**（Journal of Management Studies，≠ Journal of Management）— 未核查 — 需先向 v4 卡扩样 ≥5 篇 JMS 论文（现 0 张） | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 | 未核查 |

## 本机证据口径（哪些列必然 `未核查`，以及升级路径）

**必然 `未核查` 的列（9 列）**——本机证据不含该维度，且无任一来源覆盖：

| 列 | 为何本机必然 `未核查` | 扩样到 ≥5 卡后的升级方式 |
|---|---|---|
| Stakes 形态 | §9 无 stakes 字段；hooks 表无 stakes 维 | 从 v4 卡抽 Stakes 段独立/嵌入的事实 → 升级 `catalog≥5` |
| 显式 RQ | §9 / hooks 表均无 | 从卡正文抽显式 RQ 有无 → `catalog≥5` |
| Differentiation 段 | §9 / hooks 表均无 | 从卡正文抽 Differentiation 是否独立段 → `catalog≥5` |
| robustness preview 容忍度 | §9 / hooks 表均无 | 从卡正文抽 robustness 披露位置/次数 → `catalog≥5` |
| 显式 caveat 容忍度 | catalog 唯一可派生维（`section_learning.introduction.caveat` 存在性），但 78/78 卡全为真、各 outlet 100% → **无区分度**，不作为容忍度取值 | 需从卡正文抽 caveat 出现的位置/次数/强度，而非存在性 → `catalog≥5` |
| 具名案例容忍度 | §9 / hooks 表均无 | 从卡正文抽具名案例有无 → `catalog≥5` |
| 段落节奏 | §9 / hooks 表均无 | 从卡正文抽句长/长短交替 → `catalog≥5` |
| 元句容受 | §9 无元语言字段；hooks 表无 | 从卡正文抽 `estimand/locked/adjudication` 类元句有无 → `catalog≥5` |
| 段数区间 | 全量 78/78 卡有 `### Five acts`（语义节拍，非段数）；显式给 intro 段数的仅 2/78（均 SMJ）→ 不足门槛 | 若卡正文补段数标注，或 SMJ 卡增至 ≥5 张含段数 → `catalog≥5` |

**已完成来源标注的列（3 列）**：Hook 类型偏好⟨`corpus-hooks`⟩、现象 vs 理论起点⟨`routing-journal_styles`⟩、Contribution 写法⟨`routing-journal_styles`，仅风格子项；`theory–practice–policy` 配比仍 `未核查`⟩。

**catalog 口径（2026-09-14 实测）**：达 ≥5 卡的 outlet 为 SMJ 11 / AMJ 10 / JM 9 / MS 7 / POM 6；合并 ASQ 三种拼写别名（`Administrative Science Quarterly` 4 + `Administrative Science Quarterly 52(1): 32-69` 1 + `ASQ` 1）后 ASQ 6；JOM 仅 1 卡（`darby2026`）、JMS（Journal of Management Studies）0 卡（catalog 另有 `Journal of Management` 1 卡 `malik2025`，与本行 JMS 非同一 outlet）。因 12 个画像维度中无一能由 catalog 派生到具区分度的 ≥5 卡证据，**本表 `catalog≥5` 格数 = 0**；达到 ≥5 卡的 outlet 不自动使任一格升级，须先补卡正文抽取（见上表「升级方式」）。

**corpus-hooks 覆盖实测**：`corpus/hooks/` 共 30 个 `.md`（含 `_index.md`）；有 `## 期刊适配` 表的 **26 个**（任务书与 D-01 所称「28/28」已过时）；缺表 4 张：`08-consequence-cascade` / `09-psychological-construct-hook` / `10-immersive-narrative` / `27-theory-testbed-arena`（`_index.md` 仅正文提及）。

## 元句容受列与水位门的对齐

`元句容受` 列取值回答「该期刊正文是否接受 `estimand / locked / adjudication` 一类项目管理式元句」。本机证据下全列为 `未核查`，故 `references/water-level-gate.md` §三「元语言例外」按默认执行（转论文语言）；待该列升级为 `catalog≥5` 且取值为「允许」时，水位门相应放松。

## 来源标签分布（11 行 × 12 维度 = 132 格）

| 标签 | 格数 | 说明 |
|---|---|---|
| `catalog≥5` | **0** | 无任一维度可由 catalog 派生到 ≥5 卡且具区分度 |
| `corpus-hooks` | **9** | Hook 类型偏好列：ASQ / ASR / AMJ / SMJ / JM / JMR / MS / POM / OS |
| `routing-journal_styles` | **14** | 现象 vs 理论起点 7 格（ASQ/ASR/AMJ/SMJ/JM/JMR/OS）+ Contribution 写法 7 格 |
| `未核查` | **109** | 其余全部格（含 JOM / JMS 两整行 24 格） |
| 合计 | 132 | 9 + 14 + 109 = 132 |
