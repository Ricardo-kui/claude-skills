# Product validation and boundaries

> Imported from the upstream protocol. Resolve relative resource paths from this reference file's directory.

## Phase 6 — 成品验证模式（Product Validation Mode）

> 成品验证模式（`--validate` 调用）的完整协议——五维评分卡、优先修正清单、验证报告模板、验证反馈自动回写——已外置：见 `../protocols/product_validation.md`。用户请求验证已写出的 Introduction 时加载。

## 诚实边界

本 skill 必须 not：
- **复制原文**：不提取连续 8+ 词的原文短语进入骨架。骨架必须是句法抽象。
- **虚构复现性**：不声称某骨架"出现在多篇论文中"除非确实有证据。
- **泛化特殊组合**：不把 Incommensurability 的叙事模式套用到 Incompleteness，不把 Constructs 辨析套用到 Mechanism。
- **跳过薄弱模块**：即使原文某模块（如 Stakes）处理得很弱，也要如实记录，不能为了让骨架"好看"而美化。
- **强制覆盖所有模块**：如果某 Introduction 确实缺失某模块，记录为 missing，不捏造。
- **混淆 Gap 类型**：如果原文的 Gap 语言模糊，明确标记为 "ambiguous between Incompleteness and Inadequacy"，不强行分类。

---

## 反模式（蒸馏过程中主动排查）

| 反模式 | 表现 | 处理方式 |
|--------|------|----------|
| **原文依赖型骨架** | 骨架中包含论文特有的现象名、行业名、具体学者名 | 泛化为 [phenomenon] / [industry] / [scholars] |
| **过度抽象** | 骨架抽象到只剩 "We study X"，失去组织叙事的启示 | 保留关键功能短语（"This omission is theoretically important because" / "A consensus is building that"） |
| **Gap 类型错配** | 将 Inadequacy 的 "overlooks" 语言标记为 Incompleteness | 在骨架中标注准确的 Gap 适用范围 |
| **忽略 Stakes 缺失** | 只提取"写得好的"部分，忽略原文 Introduction 的薄弱点 | 在 Rhetorical Logic 和 QC 中明确记录薄弱点 |
| **批量同质化** | 批量处理时忽视 Gap 类型差异，用同一套骨架覆盖不同组合 | Phase 0 分类必须先行，不同 Gap 类型分桶处理 |
| **混淆 Puzzle 与 Gap** | 将 "few studies have examined" 记录为 Puzzle 陈述 | Puzzle 必须是 broad management question；Gap 是文献中的具体遗漏 |

---

## 与外部 Skill 的接口

- **`write-introduction`** — 两层接口：(1) Phase 4 `governance_plan` → dry-run → 审核后由事务治理更新 `_evidence_registry.yaml` 与 corpus；(2) `skill_design_feedback` → 缺陷证据账本。风格观察保留在蒸馏报告，直到存在可消费的治理接口。Phase 6 即时 QC 可生成 `RECORD_VALIDATION`，由 catalog 汇总为健康警示；它不自动改变路由或核心规则。
- **`diagnose-introduction`** — Phase 0 的组合分类可作为 diagnose 的验证基准
- **`intro-review`** — Phase 1.5 的模块覆盖检查可作为 intro-review 的预检清单；Phase 6 的验证报告可作为 intro-review 的预诊断输入
- **`paper-review`** — Rhetorical Logic Map 可用于跨 section 对齐检查（Introduction 承诺 vs Discussion 兑现）
- **Vault** — Fine-Grained Profile 存入 Vault 的 `fine_grained/batch_*/[paper]_distilled_introduction.md`；Phase 6 验证报告存入 `fine_grained/validation_runs/`

## 外部资产位置

- **外置协议文件**: `../protocols/`（quick_reference.md、batch_mode.md、story_architecture_fields.md、profile_template.md、phase4_output_blocks.md、corpus_file_templates.md、product_validation.md、json_output_schema.md）
- **write-introduction 语料库**: `../../write-introduction/academic-writing-corpus/`（hooks/, tensions/, stakes/, literature-turns/, previews/, transitions/）
- **共享证据注册表**: `../../write-introduction/academic-writing-corpus/_evidence_registry.yaml`（distill 写入，write-introduction 消费）
- **现有语料库索引（本机路径，不随 repo 同步）**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/introduction/mvp30/_mvp30_introduction_index.md`（待创建）
- **蒸馏产出存放（本机路径，不随 repo 同步）**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/introduction/mvp30/fine_grained/batch_*/[paper]_distilled_introduction.md`
- **成品验证报告存放（本机路径，不随 repo 同步）**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/introduction/mvp30/fine_grained/validation_runs/[date]_validation_report.md`

## JSON Output Schema

> 机器可读 JSON 输出的完整 schema 已外置：见 `../protocols/json_output_schema.md`。仅在用户要求 `--output-format=json` 时加载。
