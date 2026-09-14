# Outline Protocol — 大纲协议（Phase 2 的 O1–O3）

> **单一事实源**：本文件是 leading word「大纲」（outline）在 write-theory 的唯一权威定义处。`SKILL.md` 与其余 reference 只引用本协议，不复述其定义。
> **位置**：Phase 2。前置输入 = Phase 1 诊断（gap 三元组 + 一级路由选定的变体族 A–G）+ Story Contract。下游 = G1 借句表（`generation-protocol.md`），G1 按大纲表逐段填底本。
> **分工**：段落**内部**论证角色组装见 `../story-blueprints/v4/rhetoric-moves/_argument-grammar.md`；段内四段位（Topic→Reasoning→Tokens→Wrap）见 `corpus/subprotocols/paragraph_layout.md`；底本授权与渲染见 `generation-protocol.md`。本协议只负责**段序列**的取材、合成与登记（含来源列），不重复上述内容。
> **与 Hard constraints 的关系（平行层）**：本协议判据是**执行门**——回答「大纲表是否产出、来源是否可核」。Hard constraints #1–16（见 SKILL.md）是**实质规则层**——回答「论证内容是否合规」。两者平行互补、互不复制：本协议不重述 #1–16 内容，完成判据也不替代 #1–16 逐条过。

## 一、大纲是什么

大纲 = 一张四列表，逐段记录「这一段承担什么功能、承载什么信息、依据什么来源」。它是 Phase 2 的产物，并进入输出合同。「主导功能」列沿用 Phase 2 段落功能图的逐段叙事功能标注（knot inheritance / knot deepening / mechanism tying…）。

| 段号 | 主导功能 | 承载信息 | 来源 |
|---|---|---|---|
| P1 | Hook + knot inheritance | 结构性条件如何改变治理结果 | `sentences-mechanism_chain::zhou-2017-99b15c.a` |
| P2 | Literature turn | 内部治理研究向外部压力扩展 | `self-drafted` |
| ... | ... | ... | ... |

> 上表为格式示意，不是可套用的段落清单。

**来源列填什么**：`_skeleton` 二级 id（`子清单stem::二级id`，见 §六）或 `self-drafted`。

**大纲不是**：故事类型（由 Story Contract 锁定）、句子底本（由 G1/G2 负责）、变体族（由 Phase 1 一级路由锁定）。

## 二、一级轴 + 二级轴 + 三来源子清单（theory 特有机制）

**一级轴 = 变体族 A–G**。对齐 `corpus/meta/routing_table.md` 的 Gap×贡献杠杆→A–G 路由；一级轴已由 Phase 1 选定，本协议不重选、不复制路由规则。

**二级轴 = 功能位**。每个变体族内再按「段落功能位」定位底本，三来源的二级轴各自不同：
- variants 子清单：二级 = 变体号/变体名（如 E 族的 `A` / `B` / `receptivity_displacement_moderator` 等 P 表行）。
- subprotocols 子清单：二级 = pattern 段（pattern_id/pattern 名，如 `anchor_then_mechanism_then_prediction`）。
- sentences 子清单：二级 = 句位（句位名/句式 id，如 `zhou-2017-99b15c` 的 Reason 句位）。

**三来源子清单怎么查**（两步，渲染阶段才读语料文件本体）：
1. 由一级轴族名，打开对应 variants 子清单（`corpus/_skeleton/variants-<族>.md`），按 `func`（二级功能位）匹配段的主导功能，取命中 entry 的 `id`。
2. 若段的主导功能需 subprotocol pattern 或 sentence 句位承接，跨子清单查 `corpus/_skeleton/subprotocols-*.md`（7 pattern 库）或 `corpus/_skeleton/sentences-*.md`（8 文件），同样按 `func` 匹配取 `id`。

entry 字段 = `id | func | citekey | status | kind | text | anchor`（7 字段，三来源字段名一致）。子清单总量与路由见 `corpus/_skeleton/_index.md`。

## 三、O1 取材

1. 取 Phase 1 选定的一级轴变体族（A–G），读该族 variants 子清单的 `func` 列。
2. 按段主导功能，跨三来源子清单取命中 entry（variants P 表 / subprotocols pattern 段 / sentences 句位）。
3. 取材结果按「来源」枚举登记（见 §六）；三来源子清单均无命中的段记 `self-drafted`。

## 四、O2 合成

1. 段内四段位（Topic→Reasoning→Tokens→Wrap）见 `corpus/subprotocols/paragraph_layout.md`；论证角色序列见 `../story-blueprints/v4/rhetoric-moves/_argument-grammar.md`。gap_type 只定能量与复杂度（段数区间），不改变一级轴。
2. 段序列以 Phase 2 架构（`references/phase-2-architecture.md`）为准；变体族内 P 表给出该族的段功能序列形状。
3. 描述型段（如 Institutional Background 情境说明）记 `self-drafted` 或标注 `[skipped: 理由类型]`，不计入来源分母（见 `generation-protocol.md` G3）。

## 五、O3 登记

1. 逐段登记四列表，每段「来源」非空且可核（二级 id 可回 `corpus/_skeleton/<子清单>.md` 定位）。
2. 无底本段记 `self-drafted`，并如实记录其在全表占比。
3. 跳过或压缩的模块在对应段标注 `[skipped: 理由类型]`。
4. **status/citekey = 「未标注」的条目**：可用，但须在借句表「出处核对」列登记并人工核对出处（见 `generation-protocol.md` G1）；不假装有完整溯源。
5. 大纲表进入输出合同，作为 G1 的准入产物。

## 六、来源取值枚举

| 取值 | 含义 | 何时使用 |
|---|---|---|
| `variants-<族>::<二级id>` | 段底本取自某变体族子清单 entry | O1 一级轴取材 |
| `subprotocols-<库>::<二级id>` | 段底本取自 7 pattern 库子清单 entry | O1 跨库取材 |
| `sentences-<文件>::<二级id>` | 段底本取自 8 句式文件子清单 entry | O1 跨库取材 |
| `self-drafted` | 无底本，本文自拟 | 三来源子清单均无命中 |

> `::<二级id>` = 该子清单 entry 的 `id` 字段原值（不重新编号）；回源靠该 entry 的 `anchor`（`corpus/<源文件>.md#fragment`）。

## 七、完成判据（是/否）

- 大纲表四列齐全？
- 每段「来源」非空且可核（二级 id 可在 `corpus/_skeleton/<子清单>.md` 定位，或为 `self-drafted`）？
- `self-drafted` 占比已如实记录？
- 每个模块跳过/压缩决策在段内标注 `[skipped: 理由类型]`？
- 「未标注」条目已按 O3.4 标注并指向借句表出处核对列？
