---
type: meta
title: "修辞动作语料库（Rhetoric Moves）—— 语言表达层"
created: 2026-08-24
updated: 2026-08-24
status: seed
tags: [修辞, 语言表达, 润色, 查重安全]
related: ["[[story-blueprints/v4/blueprints]]"]
---

# 修辞动作语料库（Rhetoric Moves）

story-blueprints 的语言表达层：blueprint 卡教**故事结构**（五幕/张力/人物），本层教**修辞动作**（一个动作怎么用语言执行）。两者配套——结构告诉你"用什么手法"，本层告诉你"这个手法在句子上怎么做、怎么用自己的话说"。

## 设计原则（2026-08-24 用户裁决）

> **学的是修辞机制，产出的是你自己的句子。禁止照抄。**

本层是"学习引擎 + 润色引擎"，**不是抄写库**。理由：照抄顶刊句子会触发查重。因此：

1. **可自由复用的资产**：结构蓝图（逻辑槽位）、信号词表（通用功能词）、改写指引（变换操作）、改写演示（展示"怎么转成自己的话"，演示本身就是原创改写，与原文无 n-gram 重叠）。
2. **只读参照（禁止照抄）**：每条 move 附 1 句原文，仅用于**阅读内化**修辞机制，标注 `⚠️ 只读参照，禁止照抄`。润色输出经查重护栏（见 `_polish-protocol.md`）强制**整体（所有参照并集）重合度 ≤40%**、**单句单篇 ≤50%**、**引号整句直接引用豁免**；低于 10%（软目标）提示离骨架太远、超过 40% 用跨源合成压低。查重是**安全护栏，不是质量目标**——质量目标永远是通顺、符合学术表达、句子不过长。
3. **任何产出（润色变体、写作建议）都不得携带原文长句**；允许出现的只是信号词（on the one hand / however 等通用功能词，不触发查重）。

## 动作分类（2026-08-24 P2 填充完成）

| move | 位置 | 动作 | 跨源 | 扩源 |
|---|---|---|---|---|
| `bidirectional-staging` | intro | 双向预测先行：理论裁定前，先用两条对立文献预测把问题立起来 | VERIFIED（3 篇） | saturated |
| `mechanism-two-chain` | theory | 双链汇一：一个假设由两条收敛因果链推出，链间互补不重复 | VERIFIED（3 篇） | saturated |
| `moderator-meta-framework` | theory | 调节元框架：N 个调节变量统摄于一个组织方案下，读作一个论证而非三个附加 | VERIFIED（4 源） | saturated |
| `counterfactual-reversal` | results | 反向证伪：处理撤销/假处理/替代结局，把结果推往相反方向或 null，作为识别确证 | single（等第 2 verbatim） | open |
| `additional-analysis-embedding` | results | 嵌入型补充分析：前提探测/替代冲击/稳健性收束织进正文叙事流，而非压附录 | VERIFIED（3 源） | saturated |
| `conditional-payoff-closing` | results | 条件支付收束：结果只在某条件下兑现，高 W 反转、衰减 (a)(b)、双端兑现 | VERIFIED（5 源） | saturated |

**扩源纪律（2026-08-24 用户裁决）**：`expansion_state` 三态——`saturated`（≥5 锚点 或 ≥3 distinct papers，暂停加锚点，只维护） / `open`（继续扩源）。resume 触发=用户点名、真实写作缺口、新子动作类型。saturated 只闸 source-ADDS，不闸信号词表/改写演示补充。

**VERIFIED 判定（2026-08-24 澄清）**：须 ≥2 篇论文**带 verbatim 锚点**示范该动作；模板/骨架不算。counterfactual-reversal 现仅 1 篇 verbatim（Castellaneta 2017 SMJ），标 single，等第二篇 verbatim。

## 路由

- **润色请求**（用户/agent 给出自己草稿，要升级语言表达）→ 读 `_polish-protocol.md` → 按动作取对应 move 文件 → 生成变体 → 过护栏。
- **写作辅导**（agent 教某动作怎么写）→ 直接读对应 move 文件，用"结构蓝图 + 信号词 + 改写演示"教学，**不**引用只读参照句作为可复用文本。
- **蒸馏管线**（distill-*-exemplar）→ 新论文蒸馏时，若发现既有 move 未覆盖的动作，按本格式新增文件；已有 move 则补充信号词与改写演示（跨论文积累）。
- **write-\* skill（已接线 2026-08-24）**：各分节 SKILL.md 已含路由指针——write-introduction→bidirectional-staging；write-theory→mechanism-two-chain（含调节元框架）；write-methods/write-results→通用润色护栏（其锚点纪律已与 `_polish-protocol.md` 查重护栏衔接）。写作时如需修辞升级，先读本文件动作表再取对应 move。

## 文件规范

每个 move 文件 frontmatter 必备：`type: rhetoric_move`、`canonical_id`、`name_zh`、`cross_paper`（VERIFIED=≥2 篇 verbatim 验证 / single=单 verbatim）、`created`、`updated`、`expansion_state`（saturated / open）、`pattern_count`、`distinct_sources`、`expansion_note`。正文结构固定为七段：动作定义 → 结构蓝图 → 信号词表 → 改写指引 → 只读参照 → 改写演示 → 自查勾子。新 move 创建走同格式（见上「路由」蒸馏管线）。
