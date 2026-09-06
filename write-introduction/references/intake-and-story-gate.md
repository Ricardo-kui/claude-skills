# Intake and Story Gate — Introduction（从 SKILL.md Phase 0 下沉，v0.1）

> **权威词表**：`../../paper-story-contract/references/stage-gates.md`（写作四阶段 preparing/blocking/refining/finishing；门控结果 PASS/PROVISIONAL/BLOCKED）。本文件只写 Introduction 侧的门控细则，与 write-theory / write-methods / write-results 同一词表。

## 模式（--mode）

`introduction`（默认）｜`front-end`（标题+Abstract+promise 对齐，读 `front-end-mode.md`）｜`align`（只审查对齐）。

## Story Intake

1. 读 canonical `story`（`/paper-story-contract` 门控；旧字段按 `../paper-story-contract/references/schema.md` 迁移标 provisional），并读取 project-owned `story.integrity` ledger。忽略任何 legacy `story.story_frame`。
2. 无法同时陈述 theme question 与 central knot → 停止在 Story Intake。
3. `story.integrity` 有任一 `unsupported` → 停止在 Story Intake（Intro 特有门：项目自身完整性台账）。

## 阶段行为（对齐 stage-gates 词表）

| 阶段 | Introduction 行为 |
|---|---|
| `preparing` | 只做诊断与设计需求（Gap 三元组、异议预判清单、Vault 检索、范文学习对象）；不写正文 |
| `blocking` | 可输出带占位符的骨架（跳过润色）；gate 结果为 PROVISIONAL 时，骨架中的假设性内容须显式标注 |
| `refining` / `finishing` | 要求 `story.status: confirmed`，且满足 Intro 附加门：stakes.theoretical 与 reader_shift 非空（stage-gates §Section Gate Matrix） |

## Local-only bypass

单模块请求可 local-only bypass：输出标记"未经整篇故事契约验证"，不更新 paper state。

**完成判据**：门控满足或显式记录跳过；项目自身 story integrity 已确认。
