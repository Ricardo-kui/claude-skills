---
type: storytelling_tool
canonical_id: "hook-type-mapping"
source: "Pollock 2025 Ch05"
created: 2026-06-01
required: false
estimated_lines: 30
dependencies:
  - "reader-conversion-sequence.md"
---

# Hook 类型映射（Pollock Ch05 → Skill Hooks）

Pollock Ch05 定义 4 种 Hook 类型，映射到 skill 的 Hook 语料库：

| Pollock 类型 | 功能定义 | 对应 Skill Hooks |
|-------------|---------|-----------------|
| **Quote** | 用具体引语/轶事抓住读者，建立人文面孔 | `02-epigraph-quote-pivot`、`10-immersive-narrative`、`11-institutional-anecdote` |
| **Trend** | 用数据或文献趋势展示重要模式 | `03-data-shock`、`05-literature-consensus-blindspot`、`08-consequence-cascade` |
| **Anecdote** | 用叙事案例引入主角和悖论 | `04-puzzle-paradox`、`10-immersive-narrative`、`14-paired-disasters`、`16-evolving-social-issue` |
| **Rhetorical Question** | 用问题激发读者思考 | `13-rhetorical-question`、`17-classic-debate-constraint` |

## 选择逻辑增强

- 用户偏好"人文面孔" → 优先 Quote/Anecdote
- 用户偏好"理论对话" → 优先 Trend
- 用户偏好"悬念感" → 优先 Rhetorical Question
- Central knot 是 empirical puzzle → 优先 Anecdote/Quote
- Central knot 是 theoretical tension → 优先 Trend/Rhetorical Question

## 与 Human Face 的关系

| Pollock 类型 | 天然 Human Face | 需要补充 Human Face |
|-------------|----------------|-------------------|
| Quote | ✅ 引语/轶事自带具体 actor | — |
| Anecdote | ✅ 叙事案例自带具体 actor | — |
| Trend | ❌ 数据/趋势是抽象的 | 在数据后补充 1 个具体案例 |
| Rhetorical Question | ❌ 问题是抽象的 | 在问题后嵌入 1 个微型场景 |
