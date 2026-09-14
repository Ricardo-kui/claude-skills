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

本目录存放 Pollock 2025 故事架构层的叙事诊断工具与写作工具。它们与功能模块语料库（hooks、tensions、stakes 等）互补，供 write-introduction 在需要时按文件读取。

> **运行时状态（2026-09-14 死资产处置后）**：判定规则 = 内容已被 `paper-story-contract` 或现有 Phase 覆盖且无外部指针 → 删除；有独有内容 → 保留并在下表写明入口与触发条件。
> 已删除：`central-knot-diagnostic.md`（`story.central_knot` 字段与 Phase 0 门已覆盖）、`central-knot-throughout-check.md`（`post-generation-validator.md` 验证 1 已覆盖）、`hook-type-mapping.md`（`hooks/_index.md`「Pollock 类型速查」已覆盖）。旧描述「被 SKILL.md 的 Story Architecture Layer 引用」已作废——该层不存在。

## 核心文件

| 文件 | 功能 | Pollock 章节 | 运行时入口 / 触发条件 |
|------|------|-------------|---------------------|
| `prose-craft-checklist.md` | Human Face / Showing vs Telling / Conversational Voice | Ch03 | SKILL.md Phase 4 措辞润色 §0/§5（write-introduction + write-theory 共享） |
| `daviss-index.md` | Davis's Index of the Interesting（26 种有趣性） | Ch05 | `references/render-rules.md` Contribution #5 |
| `reader-conversion-sequence.md` | Title→Abstract→Introduction 漏斗一致性 | Ch05 | 仅注释引用，无生成步骤入口 |
| `character-map.md` | 构念到叙事角色的映射（Introduction 前 3 段出场） | Ch02 | 独有内容保留：write-theory `corpus/subprotocols/character_ordering.md` 的分工指针；Introduction 角色出场/主角判定不清时按需读 |
| `tension-escalation-protocol.md` | 叙事阶段定义与倒退检测（唯一源）+ `conversation_strategy` 双轴纪律 | Ch02 | 独有内容保留：`diagnose-introduction/references/intertextual-construction-playbook.md` 与 hooks 卡弧线分析引用；阶段倒退或非对角组合时读 |
| `post-generation-validator.md` | Introduction 后生成叙事验证器（消费 canonical `story`） | Ch02-Ch05 | 独有内容保留：完整草稿生成后的自检入口；`distill-theory-exemplar` 作为 target_validator 引用 |

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
storytelling/（叙事工具层）
    ├── prose-craft-checklist.md   → SKILL.md Phase 4 措辞润色（活跃入口）
    ├── daviss-index.md            → render-rules Contribution #5（活跃入口）
    ├── character-map.md           → write-theory character_ordering.md 分工指针
    ├── tension-escalation-protocol.md → diagnose-introduction playbook / hooks 弧线分析
    └── post-generation-validator.md   → 完整草稿后自检
corpus/（功能层）
    ├── hooks/     → 功能模块句法变体
    ├── tensions/  → 功能模块句法变体
    ├── stakes/    → 功能模块句法变体
    └── ...
```

## 使用方式

1. 有运行时入口的文件按各自指针被读取。
2. 被保留的独有内容卡（`character-map.md` / `tension-escalation-protocol.md` / `post-generation-validator.md`）在被外部指针或自检任务触发时读取，不进入默认工作流。
3. 任何修复后的接线都必须同步更新本表，避免再次出现失效指针。

## 命名规则

- 文件使用 kebab-case
- 每个文件必须包含：定义、检查清单、反模式、修复动作、范文示例
- 与功能层语料库文件的交叉引用使用相对路径
- frontmatter 必须包含：`type`、`canonical_id`、`source`、`created`、`required`、`estimated_lines`、`dependencies`
