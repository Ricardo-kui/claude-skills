# Story Blueprints — 整篇论文故事学习语料

> **版本状态（2026-08-11）**：`blueprints/` 的 59 份卡现为 **Legacy Evidence Layer**：不可被运行时推荐、不可定义项目故事、不可因旧覆盖标签而被视为叙事范本。其可查询元数据见 `legacy/legacy-manifest.json`，生成与发现规则见 `references/legacy-evidence-layer.md`。`v4/blueprints/` 是唯一可进入即时学习检索的经复审卡层。

> 状态：蒸馏协议归 `distill-story-exemplar`；本目录是语料库而非 skill。v0.3 的旧 `ROBUST/PARTIAL` 状态统一翻译为 `legacy_coverage_confidence: claimed_complete/claimed_partial`，仅说明旧蒸馏声称的覆盖度。它不表示叙事质量、理论正确性、因果可信度或写作可迁移性。`paper-story-contract` 已不消费本库来选择故事框架；项目故事先通过自身 integrity gate，写作 skill 才可按当次条件检索 v0.4 学习对象。

## 目的

现存 distill-* 体系按 **section** 蒸馏：每篇论文被拆成 intro/theory/methods/results 四块，产出模块骨架与表达 DNA 落入各 write-* 的 section 语料。**整篇论文作为一个故事**的形态（knot 类型、反派构造、五幕落点、解法性格、同一 X→Y 的另类讲法）从未被蒸馏——这就是本库要补的层。

对应 Pollock Ch02 末尾练习：选一篇范文 → 写 2 页 synopsis：(1) 五幕各落在哪里、knot 怎么系紧又怎么解开；(2) 主/配角及为什么；(3) storylines 与 theme 的关系。本库的每份 blueprint 即该练习的结构化产物。

## 与现有体系的关系

| 资产层 | 归属 | 产出 |
|--------|------|------|
| Section 级语料 | `write-introduction/academic-writing-corpus`、`write-theory/corpus`、`write-methods/econometric-models`、`write-results/econometric-models` | 模块骨架、表达 DNA、slot 模板 |
| **Legacy Evidence Layer** | `story-blueprints/blueprints/` + `legacy/legacy-manifest.json` | 历史阅读证据、发现与复读候选；`runtime_eligibility: no` |
| **v0.4 Learning Layer** | `story-blueprints/v4/blueprints/` | 重建、评价、分节学习动作分离后的可检索学习卡 |
| **讲法汇编（历史）** | `story-blueprints/tellings/alternative-tellings-compilation.md` | 旧资产的研究线索；不得直接成为项目故事或写作模板 |
| 故事契约 | `paper-story-contract` | 项目自身 theme、knot、characters、storylines、reader shift 与 integrity，不消费范文类型 |
| 审查 | `paper-review` Step 1、`pollock-qc` | 草稿的故事架构审计 |

**语料不淘汰原则**：legacy blueprint 不复制、不取代 section 变体；它作为历史证据保留。任何由它导出的 section 规则必须在独立 provenance registry 中获得 v0.4 复审支持，不能以旧卡数量或旧 knot 标签直接取得默认推荐资格。

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
- [x] 历史记录：曾以 vault 检索补齐部分 v0.3 覆盖；该阶段的 `ROBUST/PARTIAL` 已由 Legacy Evidence Layer 翻译为 coverage claim，不保留为质量标签。
- [x] **knot 类型表定稿评审（2026-08-09）**：11 型定稿（paradox 保留待建、counterevidence 降 compound-only、overlooked-alternative/irony-reversal/consensus-puzzle/paradigms-at-war 双原型达成、其余单原型标注）；resolution 6 型定稿（remedy 独立保留 + 边界规则 + paradigms-at-war→裁决类倾向配对）；knot×resolution 正交性验证通过（11 组合无重复）
- [x] 历史记录：v0.3 已扩展至 59 份，现整体纳入 Legacy Evidence Layer，作为发现和比较语料，而非类型学或推荐池。
- [x] 已完成旧 story-frame 线路退役：`paper-story-contract` 仅维护 project-owned integrity；范文仅能在 section 调用后以 v0.4 瞬时比较出现。
- [x] Ch03 工具层从 intro 扩展到全篇（storytelling_tools 五字段已全量补齐；pacing/布局实证聚合入 `layout-inventory.md`）
- [x] knot 类型表定稿（2026-08-09：11 型定稿 + 原型计数持续演进——详见第 3 行状态行与 `_schema.md` 词表）
- [x] **`validate_blueprints.py` 校验器接入**（2026-08-11）：对照 `_schema.md` 逐份校验（文件头/Story 节/knot 类型/resolution 类型）+ `_index.md` 同步 + knot 主型计数对账；入口 `python scripts/validate_blueprints.py`，退出码 0=无 ERROR。新增 blueprint 后跑一遍，index 与词表计数须保持对账一致
