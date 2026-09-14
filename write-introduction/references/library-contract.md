# Library Contract — 两库分层合同（四层所有权与交接物）

> **单一事实源**：本文件是 write-introduction 引用 story-blueprints / corpus 两库时的**层边界与交接物**唯一权威声明。`SKILL.md` 与各 reference 只引用本文件，不复述。
> 依据：优化方案 §4 的三条边界与 §1.3 的两处硬冲突裁决。

## 一、四层所有权与交接物

| 层 | 所有者 | 职责 | 产物 | 消费方式 |
|---|---|---|---|---|
| **L-Story** | `story-blueprints/v4/blueprints/`（78 卡） | 整篇叙事怎么讲 | 读解卡 | 只供选叙事形状，不作句子来源 |
| **L-Outline** | write-introduction Phase 2 | 段落序列 + 主导功能 + 承载信息 + 来源 | **大纲表**（进输出） | 下游 G1 按 `generation-protocol.md` §一 取底本 |
| **L-Sentence** | `corpus/` 段级卡 verbatim 半 + `phrasebank/` + `micro-templates/` | 段内句子与词汇 | **借句表**（格式唯一源 = `generation-protocol.md` §一） | G2 落句 |
| **L-Move** | `story-blueprints/v4/rhetoric-moves/` | 跨节通用修辞动作 | 动作清单 | 句子级润色，只引 corpus id |

**编排顺序**：L-Story → L-Outline → L-Sentence（G1/G2）→ L-Move 句级动作。

## 二、三条边界

### 边界 1：`../story-blueprints/references/v4-schema.md` 的精确放宽授权

`v4-schema.md` 的两句硬规则：

> "They do not prescribe a story for a user's project."
> "never present the move as a writing template."

它们针对的是「照搬整个故事」。精确放宽为：**叙事形状包与 blueprint 卡的 `Five acts`、`section_learning` 可作段落大纲形状来源**；句子底本来源与「底本」定义以 `generation-protocol.md` §一 为唯一权威。

### 边界 2：故事选择保留给上游契约

引 `paper-story-contract/SKILL.md:37` 原文：

> "Do not load `story-blueprints`, propose a story type, select an exemplar, or ask the user to choose a frame."

叙事形状包只在**故事已锁定之后**提供形状与底本，并保持不反推故事类型。

### 边界 3：rhetoric-moves ↔ corpus 划界

- 同一 verbatim 原句只作为**底本**存一处，存 corpus 卡或索引。
- 信号词表归 `micro-templates/transition-signals.md`。
- rhetoric-moves 只保留动作名 + 判据 + 来源 id。
- 推论：worked example 只保留「本项目适配后的成品段落 + 底本 id 引用 + 槽位说明 + 为什么这样换」，不复制原始底本清单。

## 三、硬交接物约束

- **G1 的准入产物是大纲表**：先有大纲表，G1 的借句表才逐段启动。大纲表定义见 `outline-protocol.md`。
- **句子润色的准入产物是借句表**：先有借句表，句子级润色才启动。借句表定义见 `generation-protocol.md`。
- **humanizer 不入学术路径**（方案 §1.3 裁决 4）。
