# Outline Protocol — 大纲协议（Phase 2 的 O1–O3）

> **单一事实源**：本文件是 leading word「大纲」（outline）的唯一权威定义处。`SKILL.md` 与其余 reference 只引用本协议，不复述其定义。
> **位置**：Phase 2。前置输入 = Phase 1 的 gap 三元组 + Phase 1.5 的推荐主 blueprint 卡。下游 = G1 借句表，G1 按大纲表逐段填底本。
> **分工**：段落**内部**的论证角色组装见 `../story-blueprints/v4/rhetoric-moves/_argument-grammar.md`，模块**渲染**检查见 `render-rules.md`。本协议只负责**段序列**的取材、合成与登记，不重复上述两处内容。层边界与底本授权见 `library-contract.md`。

## 一、大纲是什么

大纲 = 一张四列表，逐段记录「这一段承担什么功能、承载什么信息、依据什么来源」。它是 Phase 2 的产物，并进入输出合同。

| 段号 | 主导功能 | 承载信息 | 来源 |
|---|---|---|---|
| P1 | Hook + tension | 结构性条件如何改变治理结果 | `ball2018-product-competition-recalls:Exposition` |
| P2 | Literature turn | 内部治理研究向外部压力扩展 | `shape:portfolio-governance` |
| ... | ... | ... | ... |

> 上表为格式示意，不是可套用的段落清单。

**大纲不是**：故事类型（由 Story Contract 锁定）、句子底本（由 G1/G2 负责）、模块清单（由 Phase 2 开篇功能合同约束）。

## 二、O1 取材

1. 取 Phase 1.5 推荐的主 blueprint 卡（L-Story），读 `Five acts` 与 `section_learning.introduction.learn`。
   - `Five acts` 提供段序列形状：Exposition / Rising action / Climax / Falling action / Denouement。
   - `section_learning.introduction.learn` 提供该卡的 Introduction 侧可迁移结构动作（至多两条）。
2. 从 `corpus/packs/_index.md` 取 1 个形状最近的对照 pack，用于校准段序列的极端写法与边界。
3. 取材结果按 `来源` 枚举登记：blueprint 卡段落记 `<blueprint-id>:<act名>`，pack 段落记 `shape:<pack-id>`。

## 三、O2 合成

1. 读 `corpus/_routing_tables.yaml` 的 `paragraph_structures`，按 `gap_type` 取骨架与段数区间。
2. **合成规则**：叙事形状以 blueprint 卡优先，`gap_type` 只定能量与复杂度（段数区间、Hook/Tension 候选的能量档）。
3. 当 blueprint 的 act 序列与 routing 模板冲突时，保留 blueprint 的段序列形状，把 routing 推荐降为能量与复杂度约束。
4. 未被 blueprint/pack 承接、仅由路由模板给出的段落记 `routing:<gap_type>`。
5. 开篇功能合同（前三单元的功能约束）逐条映射到段落，每段一个主导功能。

## 四、O3 登记

1. 逐段登记四列表，每段 `来源` 非空且可核。
2. 无底本段落记 `self-drafted`，并如实记录其在全表占比。
3. 跳过或压缩的模块在对应段标注 `[skipped: 理由类型]`。
4. 大纲表进入输出合同，作为 G1 的准入产物。

## 五、来源取值枚举

| 取值 | 含义 | 何时使用 |
|---|---|---|
| `<blueprint-id>:<act名>` | 段序列取自某张 blueprint 卡的某一幕 | O1 主卡取材 |
| `shape:<pack-id>` | 段序列取自某个叙事形状包 | O1 对照 pack 取材 |
| `routing:<gap_type>` | 段序列由 routing 模板给出 | O2 回填 |
| `self-drafted` | 无底本，本文自拟 | 前三种来源都无对应 |

## 六、完成判据

- 大纲表四列齐全，每段 `来源` 非空且可核。
- `self-drafted` 占比已如实记录。
- 每个模块跳过或压缩决策在段内标注 `[skipped: 理由类型]`。
- 形状冲突已按「形状以 blueprint 卡优先」处理并留痕。
