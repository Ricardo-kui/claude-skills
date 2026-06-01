---
type: storytelling_tool
canonical_id: "character-map"
source: "Pollock 2025 Ch02"
created: 2026-06-01
required: false
estimated_lines: 103
dependencies: []
---

# Character Map（角色映射）

## 定义

在学术故事中，构念不是变量，而是**角色**。每个构念在故事中扮演特定角色，其"戏份"和"出场时机"决定读者能否追踪故事线。

> "Your theoretical constructs are the characters in your drama, not the individuals and organizations that may be experiencing or personifying them." — Pollock 2025, Ch02

## 角色类型

| 角色 | 定义 | 学术对应 | 出场规则 |
|------|------|---------|---------|
| **主角（Protagonist）** | 故事的核心焦点 | 核心 DV 或研究焦点构念 | Hook 中出现，贯穿全文 |
| **对手/张力源（Antagonist）** | 造成冲突的理论或现象 | 被挑战的共识、制度约束、反直觉现象 | Hook 中暗示，Gap 中明确 |
| **配角（Supporting）** | 推动故事发展的关键角色 | 调节变量、中介变量 | Theory 中出场，不可在 Hook 中抢戏 |
| **群演（Ensemble）** | 让场景更可信的背景角色 | 控制变量 | Methods 中出场，不出现在前 3 段 |

## 主角判定规则

**问题**："如果读者只能记住一个构念，应该是哪个？"

- **DV 为主角**：如果研究核心解释"什么影响了 Y" → Y 是主角
  - 例：Mishina et al. (2010) 中，illegal actions 是主角（焦点是"什么导致好公司做坏事"）
  - 例：Pfarrer et al. (2010) 中，earnings surprises 是主角

- **IV 为主角**：如果研究核心解释"X 如何影响多个结果" → X 是主角
  - 例：Chatterjee & Pollock (2017) 中，CEO narcissism 是主角

- **双主角**：如果研究核心是"X 和 Y 的关系" → X 和 Y 都是主角
  - 例：Han & Pollock (2021) 中，status inconsistency 和 behavioral consequences 都是主角

- **多主角风险**：超过 2 个主角 → 读者无法聚焦。修复：选择最核心的 1-2 个，其余降级为配角。

## 配角判定规则

**问题**："哪个构念推动了主角的 storyline，但不是故事的核心焦点？"

- **Mediator（中介配角）**：解释 X→Y 的机制 → 在 X 和 Y 之间出场
  - 例：Mishina et al. (2010) 中，performance relative to aspirations 是主角，firm prominence 是配角

- **Moderator（调节配角）**：改变 X→Y 的强度或方向 → 在 X→Y 关系建立后出场
  - 例：Pfarrer et al. (2010) 中，firm reputation 和 celebrity 是配角（调节 earnings surprises）

- **关键控制变量**：如果控制变量对理解故事至关重要（如 earnings surprises 中的 investors' responses）→ 可提前到 Theory 开头
  - 例：Pfarrer et al. (2010) 中，earnings surprises 虽是控制变量，但因为不了解它就无法讲故事，所以在 Theory P1 就定义它

## 群演判定规则

**问题**："这个构念只是为了排除替代解释吗？"

- 如果是 → 群演，在 Methods 中出场
- 如果不是 → 考虑是否应升级为主角或配角

## 多主角风险检测

**检测标准**：
- Introduction 前 3 段出现超过 2 个需要定义的构念 → ⚠️ 多主角风险
- Theory section 出现超过 3 个独立 storyline → ⚠️ 多主角风险
- 用户无法一句话说明"故事是关于谁的" → ⚠️ 多主角风险

**修复动作**：
1. 列出所有"主角候选"
2. 问："如果只能保留一个主角，审稿人会选哪个？"
3. 其余降级：
   - 与主角关系密切的 → 配角
   - 只是为了排除替代解释的 → 群演
   - 与 knot 关系弱的 → 删除或移至 future work

## 角色出场时机

| 段落 | 应出现 | 不应出现 |
|------|--------|---------|
| P1 Hook | 主角暗示、对手暗示 | 配角定义、群演 |
| P2 Lit Turn | 主角名称、对手名称 | 配角详细讨论 |
| P3 Gap | 主角、对手的张力 | 群演 |
| P4 Stakes | 主角的代价 | 群演 |
| P5-P6 Theory Lens | 主角、关键配角 | 群演 |
| P7-P8 Contribution | 主角、对手、配角的 resolution | 群演 |

## 范文示例：Mishina et al. (2010)

| 角色 | 构念 | 出场时机 | 理由 |
|------|------|---------|------|
| 主角 | Illegal actions | Hook | 故事核心：好公司为什么做坏事 |
| 主角 | Performance relative to aspirations/expectations | Hook | 与 illegal actions 共同构成核心张力 |
| 配角 | Firm prominence | Theory（moderator） | 改变主效应的强度 |
| 群演 | CEO/Chair separation, board size, slack, year dummies | Methods | 排除替代解释 |

## 常见错误

| 错误 | 表现 | 修复 |
|------|------|------|
| 配角抢戏 | Hook 中详细讨论 moderator | 将 moderator 移到 Theory section |
| 群演越级 | Introduction 中讨论控制变量 | 删除或移至 Methods |
| 主角缺席 | 前 3 段没有明确的核心构念 | 在 Hook 中暗示主角 |
| 角色混淆 | 同一个构念在不同段落扮演不同角色 | 统一角色定位，必要时拆分构念 |
