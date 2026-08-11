# Output Format — Introduction 骨架输出模板（从 SKILL.md 下沉，v0.1）

> 由 write-introduction 输出骨架时**对照使用**：模板结构 + 模块跳过指南。

## [Gap类型] × [贡献维度] Introduction 骨架

### 功能序列与压缩决策
[列出路由后的实际序列，例如：P1 Hook+Literature（主导功能=现象张力）→ P2 Tension+Stakes（主导功能=problematization）→ P3 Theory Lens → P4 Preview → P5 Contribution。说明合并/跳过理由与期刊差异。]

### 前三段合同
| 段落 | 主导功能 | 必须完成 | 失败风险 |
|------|---------|---------|---------|
| P1 | 现象张力 | 前三句出现 anomaly/puzzle + theory trouble | 背景先行、埋没主旨 |
| P2 | 学术对话 | 已知什么、证据角色、现有预测 | 罗列而非对话 |
| P3 | Problematization | 诊断失败 + theoretical consequence + response pivot | 只有空白，没有理论问题 |

> 紧凑型如合并 P1/P2 或 P2/P3，在表中标明功能落在哪个段落；按实际序列生成段落，不生成空的固定段号。

### 段落骨架（按实际序列动态渲染）

#### P[N]: [主导功能] — [所选模块/策略]
[直接写句法骨架；占位符用 [brackets]；标注本段包含的次级功能。按实际段数重复。]

### 提醒
- **必须配对**: [检查 Hook→Tension 强制配对（见 `_routing_tables.yaml` §7）；标注是否满足]
- **能量一致性**: Hook 能量 ≤ Gap 能量 ≤ Stakes 能量？[检查并标注 "高开低走" 风险]
- **模块跳过**: [如有模块满足跳过条件，注明理由]
- **期刊注意**: [如用户提了目标期刊]
- **替代变体**: [可选的其他变体]

### 证据置信度
- Hook `[id]`: ROBUST/VERIFIED/EMERGING（N papers, N journals）
- Tension `[id]`: ROBUST/VERIFIED/EMERGING（N papers, N journals）
- Stakes `[id]`: ROBUST/VERIFIED/EMERGING（N papers）[如 Stakes 未被跳过]
- Literature Turn `[策略名]`: ROBUST/VERIFIED/EMERGING（N papers）
- **EMERGING 变体必须标注单/双源**（"单篇来源，待第二篇交叉验证"或"双源"）——不仅写 EMERGING；采用 EMERGING 时在「替代变体」栏给出 VERIFIED/ROBUST 替代或说明为何无成熟替代。

### GBL Four-Move 对齐
| Move | 状态 | 对应段落功能 | 修复 |
|------|------|--------------|------|
| Significance | [pass / partial / missing] | [Hook/Stakes] | [...] |
| Literature situation | [pass / partial / missing] | [Literature Turn] | [...] |
| Problematization | [pass / partial / missing] | [Tension] | [...] |
| Response foreshadow | [pass / partial / missing] | [Theory Lens/RQ/Preview/Contribution] | [...] |

**总体状态**：[aligned / partial / incomplete]
**优先修复**：[只列一个最重要修复]

## 模块跳过指南

| 模块 | 可跳过/压缩的条件 | 风险 |
|------|-------------------|------|
| **Stakes** | Hook 已含具体量化损失（人命/安全/精确经济损失）且理论 Stakes 已嵌入 Tension 末尾 | 审稿人追问 "So what?" |
| **Contribution** | Theory Lens 区分性本身即贡献声明（如 pontikes2012 的 market-taker vs market-maker） | Discussion 缺锚点 |
| **Theory Lens** | Gap 末尾已含理论来源名称+方向性预测 | Theory 缺 Introduction 锚定 |
| **Literature Turn** | ≤5段 Intro 且 Hook 已充分展示跨文献流共识/对话 | 读者无法定位学术对话 |
| **Preview** | 方法/发现方向已在 Theory Lens 或 Contribution 中暗示 | 极罕见——不建议完全跳过 |
| **Differentiation** | 不存在极易混淆的 prior work（同一IV/同一DV/同一theory的变体）或审稿人不太可能混淆 | 省略无风险——多数论文不需要此模块 |

**跳过决策**: 模块功能是否通过相邻模块间接完成？→ 是且满足条件 → 可压缩。不确定时，写出来比不写好。

## 快速模式

用户只请求特定模块（如"给我一个 Hook 句式"）时，跳过完整骨架，仅输出该模块的句法骨架 + 槽位提示 + 1 个反模式提醒。
