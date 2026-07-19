---
type: storytelling_index
canonical_id: "theory-storytelling-index"
source: "Pollock 2025 Ch02-Ch06"
created: 2026-06-01
required: false
estimated_lines: 40
dependencies: []
---

# Theory Storytelling 语料库总览

本目录存放 Pollock 2025 中 Theory & Hypotheses section 专用的叙事诊断工具。这些文件被 `write-theory` SKILL.md 的 Phase 1.3 和 Phase 1.4 **引用**。

## 核心文件

| 文件 | 功能 | Pollock 章节 | 引用位置 |
|------|------|-------------|---------|
| `rising-action-protocol.md` | Theory Rising Action 三阶段协议（Inheritance→Deepening→Tying，最后假设自然收敛进入 METHODS） | Ch02 | Phase 1.3 |
| `plot-emergence-check.md` | 情节浮现 vs 强加检查（5 个问题清单） | Ch02 | Phase 1.3 |
| `knot-continuity-check.md` | 跨 Section Knot 连续性（Intro↔Theory↔Methods↔Results↔Discussion） | Ch02 | Phase 1.3 |
| `post-generation-validator.md` | Theory 后生成叙事验证器 | Ch02-Ch06 | Phase 4 |

## 共享文件（来自 write-introduction）

以下文件由 write-introduction 维护，write-theory 通过相对路径引用：

| 文件 | 路径 | 引用位置 |
|------|------|---------|
| `prose-craft-checklist.md` | `../write-introduction/academic-writing-corpus/storytelling/prose-craft-checklist.md` | Phase 1.4 |
| `central-knot-diagnostic.md` | `../write-introduction/academic-writing-corpus/storytelling/central-knot-diagnostic.md` | 间接（通过 theory_hints） |
| `character-map.md` | `../write-introduction/academic-writing-corpus/storytelling/character-map.md` | 间接 |

## 使用方式

1. SKILL.md Phase 1.3 在路由完成后、输出骨架前读取本目录文件
2. 叙事检查结果附加到 Phase 4 QC 清单，不修改假设结构
3. 如果叙事检查与功能检查冲突，以功能检查为准，叙事检查输出 ⚠️ 警告

## 命名规则

- 文件使用 kebab-case
- frontmatter 必须包含：`type`、`canonical_id`、`source`、`created`、`required`、`estimated_lines`、`dependencies`
