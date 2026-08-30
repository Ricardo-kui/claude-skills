---
type: storytelling_index
canonical_id: "storytelling-index"
source: "Pollock 2025 Ch02-Ch05"
created: 2026-06-01
required: false
estimated_lines: 55
dependencies: []
---

# Storytelling 语料库总览

本目录存放 Pollock 2025 故事架构层的叙事诊断工具和协议。这些文件**不替代**现有的功能模块（hooks、tensions、stakes 等），而是被 SKILL.md 的 Story Architecture Layer **引用**，用于在功能模块选择完成后执行叙事检查。

## 核心文件

| 文件 | 功能 | Pollock 章节 | 共享 |
|------|------|-------------|------|
| `central-knot-diagnostic.md` | Central Knot 诊断流程 | Ch02 | write-introduction |
| `central-knot-throughout-check.md` | Central Knot 贯穿检查（输出后） | Ch02 | write-introduction |
| `character-map.md` | 构念到叙事角色的映射 | Ch02 | write-introduction |
| `reader-conversion-sequence.md` | Title→Abstract→Introduction 漏斗一致性 | Ch05 | write-introduction |
| `daviss-index.md` | Davis's Index of the Interesting（26 种有趣性） | Ch05 | write-introduction |
| `tension-escalation-protocol.md` | 模块能量级定义与断裂检测 | Ch02 | write-introduction |
| `hook-type-mapping.md` | Pollock 4 种 Hook 类型到 Skill Hooks 的映射 | Ch05 | write-introduction |
| `prose-craft-checklist.md` | Human Face / Showing vs Telling / Conversational Voice | Ch03 | **write-introduction + write-theory 共享** |
| `post-generation-validator.md` | Introduction 后生成叙事验证器 | Ch02-Ch05 | write-introduction |

## 共享文件（write-theory 引用）

write-theory 的 `corpus/storytelling/` 目录存放 Theory-specific 的叙事工具：

| 文件 | 功能 | Pollock 章节 |
|------|------|-------------|
| `../write-theory/corpus/storytelling/rising-action-protocol.md` | Theory Rising Action 四阶段协议 | Ch02 |
| `../write-theory/corpus/storytelling/plot-emergence-check.md` | 情节浮现 vs 强加检查 | Ch02 |
| `../write-theory/corpus/storytelling/knot-continuity-check.md` | 跨 Section Knot 连续性 | Ch02 |
| `../write-theory/corpus/storytelling/post-generation-validator.md` | Theory 后生成叙事验证器 | Ch02-Ch06 |

## 与其他语料库的关系

```
Story Architecture Layer（叙事层）
    ├── storytelling/（本目录）
    │   ├── central-knot-diagnostic.md      → 决定 knot 是什么
    │   ├── central-knot-throughout-check.md → 决定 knot 是否贯穿
    │   ├── character-map.md               → 决定谁是主角/配角
    │   ├── tension-escalation-protocol.md → 决定能量曲线
    │   ├── hook-type-mapping.md           → 决定 Hook 类型
    │   ├── reader-conversion-sequence.md  → 决定前端一致性
    │   ├── daviss-index.md                → 决定有趣性
    │   └── prose-craft-checklist.md       → 决定 prose 质量
    └── corpus/（功能层）
        ├── hooks/     → 被 storytelling 引用，标注叙事功能
        ├── tensions/  → 被 storytelling 引用，标注叙事功能
        ├── stakes/    → 被 storytelling 引用，标注叙事功能
        └── ...
```

## 使用方式

1. SKILL.md 的 Story Architecture Layer 在执行功能模块选择**之后**、渲染骨架**之前**读取本目录文件
2. 叙事检查的结果（central knot、characters、energy levels 等）附加到每个模块的"槽位提示"和"提醒"中
3. 叙事检查**不修改**功能模块的选择结果——如果叙事检查与功能检查冲突，以功能检查为准，叙事检查输出 ⚠️ 警告

## 命名规则

- 文件使用 kebab-case
- 每个文件必须包含：定义、检查清单、反模式、修复动作、范文示例
- 与功能层语料库文件的交叉引用使用相对路径
- frontmatter 必须包含：`type`、`canonical_id`、`source`、`created`、`required`、`estimated_lines`、`dependencies`
