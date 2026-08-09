# Story Blueprints — 整篇论文故事蒸馏语料（v0.3）

> 状态：**skill 接管 + 写侧已接入**。蒸馏协议归 `distill-story-exemplar`（v0.1，独立 skill，Phase 0–5 + 人工预览-确认 gate）；本目录是语料库（数据层），非 skill。当前 **59 份 blueprint：59 份全 ROBUST**（2026-08-09 共同所有权第四波收尾——reporting_comparability / crash_risk 完成，无 PARTIAL）。knot 类型表（2026-08-09 实证对账）：**九原型** neglected-arena / half-domain-gap ＞ **八原型** irony-reversal / overlooked-alternative / paradigms-at-war ＞ 七原型 consensus-puzzle ＞ 六原型 assumption-flip ＞ 三原型 tangled-constructs ＞ 单原型 cross-domain-unification（候选排除记录）＞ compound-only counterevidence ＞ 待建 paradox。**写侧消费已接通**：`paper-story-contract` 新增 `references/story-frame-menu.md`（研究描述 → 候选故事框架），选定后写入 `story.story_frame`（非门禁字段）。

## 目的

现存 distill-* 体系按 **section** 蒸馏：每篇论文被拆成 intro/theory/methods/results 四块，产出模块骨架与表达 DNA 落入各 write-* 的 section 语料。**整篇论文作为一个故事**的形态（knot 类型、反派构造、五幕落点、解法性格、同一 X→Y 的另类讲法）从未被蒸馏——这就是本库要补的层。

对应 Pollock Ch02 末尾练习：选一篇范文 → 写 2 页 synopsis：(1) 五幕各落在哪里、knot 怎么系紧又怎么解开；(2) 主/配角及为什么；(3) storylines 与 theme 的关系。本库的每份 blueprint 即该练习的结构化产物。

## 与现有体系的关系

| 资产层 | 归属 | 产出 |
|--------|------|------|
| Section 级语料 | `write-introduction/academic-writing-corpus`、`write-theory/corpus`、`write-methods/econometric-models`、`write-results/econometric-models` | 模块骨架、表达 DNA、slot 模板 |
| **Story 级蓝图（本库）** | `story-blueprints/blueprints/` | 每篇论文一份：knot/角色/五幕/解法/另类讲法 |
| **讲法汇编（本库）** | `story-blueprints/tellings/alternative-tellings-compilation.md` | 12 讲法家族 × 实例聚合——两初心事的交点（蒸馏产物 → 设计原料） |
| 故事契约 | `paper-story-contract` | 自己论文的 story 字段（消费本库做故事框架选择） |
| 审查 | `paper-review` Step 1、`pollock-qc` | 草稿的故事架构审计 |

**语料不淘汰原则**：blueprint 不复制、不取代 section 变体——只通过 `corpus_links` 链接已有变体（如 Pontikes 的 intro 变体 `04-reality-contradicts-consensus` 变体G）。story 层与 section 层是同一论文的两个投影，不是竞争关系。

## 覆盖度规则

- **全四区段蒸馏过的论文** → 五幕完整，climax/falling action 有实证落点。
- **部分区段蒸馏** → 缺失幕标注 `待补`（如 Desai 2012 的 Methods/Results），不允许编造。
- 快照事实来源：蒸馏记录（memory）+ 必要时的全文回读。corpus_links 路径在接入时需对照 `_index.md` 验证（本原型按蒸馏时记录引用）。

## 核心资产（其他语料没有的字段）

1. **antagonist（反派构造）**——故事里"对手"是谁、用什么修辞手法构造的（两派理论 / 学术共识本身 / 文献的注意力转移…）。
2. **knot 复合结构**——一个故事通常是多型复合（如 Zhou = 范式对决 + 现实反证），section 语料会把各组分拆成独立变体，blueprint 还原组合关系。
3. **alternative_tellings（同一 X→Y 的另类讲法）**——本文故事的"未被选中的版本"，即故事设计空间。这是"同样的自变量因变量可以讲出不同故事"的直接落库。
4. **resolution_logic（解法性格）**——研究者以什么姿态解开 knot：仲裁（拆地整合）/ 揭幕（换视角展示）/ 拓荒（补上被忽视的战场）。

## 下一步（未做，待用户确认）

- [x] 独立 `distill-story-exemplar` skill 已建（v0.1，Phase 0–5 + 人工预览 gate）
- [x] **Phase 0 vault 检索协议已入 skill**（2026-08-09）：按论文短名检索 `narrative_analysis/` 下 intro/theory/methods_results/deep_distillation/_story_arcs 报告，更新 distilled_sections；vault `_story_arcs/` 为早期故事层资产（链接不复制）
- [x] 用 vault 检索升级 PARTIAL：lashley2020 与 desjardine2022 已升 ROBUST（9 ROBUST + 2 PARTIAL：desai2012 / desjardine2023）
- [x] **knot 类型表定稿评审（2026-08-09）**：11 型定稿（paradox 保留待建、counterevidence 降 compound-only、overlooked-alternative/irony-reversal/consensus-puzzle/paradigms-at-war 双原型达成、其余单原型标注）；resolution 6 型定稿（remedy 独立保留 + 边界规则 + paradigms-at-war→裁决类倾向配对）；knot×resolution 正交性验证通过（11 组合无重复）
- [x] 回填剩余已深度蒸馏论文（2026-08-09 已扩至 59 份全 ROBUST——含 Mayo 2022、Desai 2011、Pfarrer 2010、Malik 2025 等；新类型全部找到多原型：tangled 三原型 / half-domain 九原型 / cross-domain-unification 单原型 / assumption-flip 六原型）
- [x] 接入 `paper-story-contract`（story-frame-menu：研究描述 → 2-3 个候选故事框架；2026-08-09 实证回填 layout-inventory 锚 + 写侧接通方向 1——story-modulation/knot-architecture-modulation）
- [x] Ch03 工具层从 intro 扩展到全篇（storytelling_tools 五字段已全量补齐；pacing/布局实证聚合入 `layout-inventory.md`）
- [x] knot 类型表定稿（2026-08-09：11 型定稿 + 原型计数持续演进——详见第 3 行状态行与 `_schema.md` 词表）
