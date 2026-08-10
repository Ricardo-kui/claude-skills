# 完整示例 — Theory 审查

仅在需要端到端示例时阅读本文件；常规审查不预加载。

### 输入
```
/theory-review
Drawing on organizational routine theory, we argue that digital transformation prompts firms to update their existing routines. Organizational routine updating refers to the deliberate modification of repetitive organizational processes to accommodate new technological capabilities. We hypothesize that digital transformation is positively related to organizational routine updating (H1). Furthermore, organizational routine updating is positively related to firm innovation performance (H2). Therefore, we hypothesize that organizational routine updating mediates the relationship between digital transformation and firm innovation performance (H3).
```

### 输出
```
## 构念地图
| 角色类型 | 构念 | 评价 |
|---------|------|------|
| Main character | Digital transformation (IV) | ✅ 贯穿全文 |
| Main character | Firm innovation performance (DV) | ✅ 明确 |
| Main character | Organizational routine updating (Mediator) | ✅ 但定义较单薄 |
| Ensemble | Controls (未提及) | ⚠️ 需在 Methods 中补充 |

**评价**：主角共 3 个，在合理范围内。但组织惯例更新的定义缺少 scope condition（什么类型的惯例？更新到什么程度？）。

## Why Chain 审查
| 假设 | 机制链 | 问题 | 建议 |
|-----|--------|------|------|
| H1 | 数字化转型 → 技术压力 → 惯例更新 | △ 跳跃：为什么技术压力必然导致惯例更新而非惯例僵化？ | 补充：在动态能力视角下，面对技术 disruption，拥有学习导向的企业更可能主动更新惯例... |
| H2 | 惯例更新 → 减少惯性 → 提升创新 | △ 隐含假设：所有惯例更新都促进创新？ | 补充：关键在于更新的是 core routines 还是 peripheral routines... |
| H3 | H1 + H2 的串联 | ✓ 逻辑形式正确 | 但需确保 H1 和 H2 的 why chain 独立成立 |

**核心问题**：机制链缺少 **boundary condition** 和 **contingency**。数字化转型不一定总是导致惯例更新（如资源约束下的企业可能选择路径依赖）。

## Theory Story 与 Citation 检查
| 审查项 | 评分 | 问题摘要 | 建议 |
|-------|------|---------|------|
| Theory story vs summary | ✓ | 段落以 "Drawing on organizational routine theory..." 开头，以理论视角引领叙事 | 保持 |
| Big picture first | △ | 提供了理论视角但未给出 overarching figure 或 roadmap | 建议增加概念模型图，或在首段末尾增加 "As illustrated in Figure 1, we theorize that..." |
| Citation coherence | ✓ | 全文围绕 organizational routine theory，未混入冲突理论 | 保持 |
| Two-literature clarity | ✓ | Theory section 专注于惯例理论的解释逻辑，未重复 Introduction 的 gap 文献回顾 | 保持 |

## Hypothesis Form 检查
| 假设 | IV | DV | 方向 | 格式问题 |
|-----|----|----|------|---------|
| H1 | Digital transformation | Organizational routine updating | Positive | ✓ 格式正确 |
| H2 | Organizational routine updating | Firm innovation performance | Positive | ✓ 格式正确 |
| H3 | Digital transformation → Organizational routine updating | Firm innovation performance | Positive mediation | ✓ 格式正确 |

## Character Ordering
- P1 定义了 mediator（organizational routine updating）✅
- P2 提出 H1（IV→Mediator）✅
- P3 提出 H2（Mediator→DV）✅
- P4 提出 H3（Mediation）✅

**顺序合理**，但建议在定义段落增加 **理论视角定位**（Drawing on organizational routine theory...），而非仅给出构念定义。

## 最需补强的机制推导
H1 的 why chain 最弱。当前逻辑："digital transformation prompts firms to update routines" 过于直白，缺少理论张力。

## 改写建议
**英文模板**：
"Drawing on organizational routine theory (Feldman & Pentland, 2003), we argue that digital transformation creates **performative tension**—a misalignment between existing routines and new technological affordances—that compels firms to modify their repetitive processes. However, not all firms respond equally. Firms with **higher absorptive capacity** are more likely to interpret digital technologies as opportunities for routine improvement rather than threats to existing practices. Thus:"

**H1**: Digital transformation is positively related to organizational routine updating, particularly when firms possess high absorptive capacity.

**说明**：
1. 引入 "performative tension" 机制，增加理论深度
2. 加入边界条件（absorptive capacity），避免过度概括
3. 将 H1 从直白陈述升级为有条件的理论预测

**变体**（如需保持简单中介模型）：
保留原 H1，但在 why chain 中增加："When digital technologies fundamentally alter the inputs, processes, or outputs of core organizational routines, firms must engage in deliberate routine reconfiguration to maintain operational coherence (Feldman, 2000)."
```
