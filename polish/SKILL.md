---
name: polish
description: "修辞动作润色路由——用顶刊范文语料润色/升级用户自己的句子或段落（语料优先改编、跨源合成、流畅性门八查）。Use when 独立的润色/改写/表达升级请求；触发词：润色、改写这句、表达升级、跨源合成、句子太 AI。Not for: write-* 骨架生成中的润色（各 skill 内建）；纯去 AI 腔→humanizer。"
---

# Polish — 修辞动作润色路由

**执行协议（唯一权威）**：`story-blueprints/v4/rhetoric-moves/_polish-protocol.md`——六步工作流：识别动作 → 取蓝图+信号词（允许多源）→ 保内容升执行（Pollock 五病灶扫描）→ 生成变体 ×3（A 单蓝图重排 / B 跨源合成 / C 换主宾视角）→ 流畅性门八查 → 输出。本文件只路由，不重复协议内容。

## 路由规则

1. **默认**：按协议完整执行。识别动作读 `story-blueprints/v4/rhetoric-moves/_index.md` 动作表；无法归类的草稿只做微观打磨。
2. **主诉是去 AI 腔**（"这段太像 AI 写的"）：走 `humanizer` skill；协议 §AI 腔速查表（13 型）与误报护栏同样适用。
3. **在 write-introduction/theory/methods/results 会话内**：不进本 skill——各 skill 的渲染与措辞阶段已内建润色（共用纪律见 `_polish-protocol.md` §write-* 共用纪律）。

## 边界

- 语料语句可直接采用，仅替换来源特异性内容（专名/数字/系数/表号）防串稿；唯一闸门 = 流畅性门（通顺/学术表达/句长 20–30 词）。
- specificity gate：替换后的句子能原样放进任何一篇论文 = 不合格。
- 保留用户的领域术语、数字、因果主张与限定语；绝不编造内容。
