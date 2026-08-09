# Phase 3 — 论证手法诊断

不量化机械指标（句数、对齐密度），而是诊断这篇 Methods 在论证上的强弱之处。

## 诊断维度

| 维度 | 诊断问题 | 输出 |
|------|---------|------|
| **because 密度** | 控制变量/样本排除中有多少附带了 because 理由？ | 定性判断 + 对 skill 模板的启示 |
| **因果语言自律** | "effect of" vs "associated with" 的分布是否匹配设计强度？ | 越级/一致/过于保守 |
| **审计链完整性** | 样本漏斗是否可让审稿人复现？ | 完整/可改进/不可审计 |
| **时间逻辑清晰度** | t-1 / contemporaneous / event window 标记是否明确？ | 清晰/模糊 |
| **新颖度**（替代旧的对齐度） | 这篇 Methods 的论证组织方式与 write-methods 当前模板**有多少不同**？不同才值得学 | 高度新颖 / 部分新颖 / 与模板一致 |

每个诊断维度输出时附带 skill 对比：
```
[定性判断] → 与 write-methods 当前模板的关系 → [skill 改进方向]
```

## 结构化报告输出（fine_grained profile）

```markdown
# Fine-Grained Profile: [作者_年份_期刊]

## Paper Identity
- 设计分类: [来自 Phase 0]
- 期刊: [journal]
- 新颖度: 这篇 Methods 的论证组织与现有模板的差异程度

## Slot Coverage (M1–M10) — 含 quality + learn_worth
[Phase 1 输出]

## 值得学的骨架（skill_gap != SKIP）
[来自 Phase 2.2 — 仅列出真正新增的]

## 论证手法诊断
[Phase 3 诊断维度]

## Validity Logic Map
[来自 Phase 2.3]

## 不可迁移的事实
[论文特有的数据库名、行业背景、样本量——仅当判断骨架可迁移性时需要参考]
```
