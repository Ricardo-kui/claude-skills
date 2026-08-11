# 完整示例 — Discussion 审查

仅在需要端到端示例时阅读本文件；常规审查不预加载。

### 输入
```
/discussion-review
Our findings show that digital transformation has a positive effect on innovation performance. This is consistent with prior research. Our study contributes to the literature by showing that organizational routine updating matters. Managers should update their routines to improve innovation. Our study has some limitations. Future research should examine other mechanisms.
--journal=SMJ
```

### 输出
```
## Introduction-Discussion 对齐表
| 承诺 | 交付 | 状态 |
|-----|------|------|
| "We explain why digital transformation affects firm innovation performance by identifying organizational routine updating as the mediating mechanism..." | "Our study contributes by showing that organizational routine updating matters" | △ 过于笼统，未具体解释机制如何运作 |
| Mechanism 维度声明 | "organizational routine updating matters" | ✗ 未使用 Makadok 维度精准表述 |

**对齐问题**：Discussion 的交付过于笼统（"matters"），未兑现 Introduction 中承诺的精确理论贡献（mechanism identification）。

## 四大缺陷检查
| 缺陷 | 状态 | 证据 |
|-----|------|------|
| Rehashing | ✗ | 整段都在复述结果（"digital transformation has a positive effect..."），超过 2 句 |
| Superficial interpretation | ✗ | "Managers should update their routines" 是日常语言翻译，无理论升华 |
| Meandering | ✗ | 一段内混杂结果复述、贡献声明、实践启示，焦点不清 |
| Overreaching | △ | "Our study contributes to the literature" 范围过大，未限定到具体文献对话 |

## Discussion 正向标准检查
| 正向标准 | 状态 | 证据 |
|---------|------|------|
| Understanding change | ✗ | 未说明读者现在应如何不同地理解数字化转型→创新绩效的关系；缺少 "I never thought of that" 时刻 |
| Contribution expansion | ✗ | "organizational routine updating matters" 仅一句带过，未扩展为 1-2 段反思 |
| Implications 受众对齐 | ✗ | "Managers should update their routines" 未锁定具体受众（如 entrepreneurship/technology strategy 学者） |
| Two-literature return | ✗ | 未回馈组织惯例理论（Literature 2）的任何新理解 |

## 意外/非显著发现处理
| 发现 | 处理方式 | 评价 | 建议 |
|-----|---------|------|------|
| 未提及任何非显著/意外发现 | — | ⚠️ 如果 Results 中存在非显著假设，必须在此解释 | 检查 Results 中是否有 unsupported hypothesis，补充理论解释 |

## Findings vs Contributions 区分度
| 检查项 | 状态 | 证据 |
|-------|------|------|
| Findings 陈述清晰度 | ✗ | 整段都在复述系数，未区分 findings 和 contributions |
| Contributions 理论升华 | ✗ | "organizational routine updating matters" 未上升到 "change the way we think" |
| Findings ≠ Contributions 混淆 | ✗ | 把 "has a positive effect" 直接等同于 "contributes to the literature" |
| 多受众贡献 | ✗ | 未考虑 entrepreneurship/technology strategy 以外的学术社群 |

## Boundary Conditions 与 Limitations
| 检查项 | 子类型 | 状态 | 建议 |
|-------|--------|------|------|
| 情境适用性（Boundary） | Boundary | △ | 未讨论数字化转型在不同行业或制度环境下的适用性差异 |
| 可推广性（Boundary） | Boundary | △ | 未说明 Compustat 上市公司的结论能否推广到中小企业或新兴市场 |
| 数据局限（Limitation） | Limitation | ✗ | 样本局限于 Compustat 上市公司 |
| 测量局限（Limitation） | Limitation | ✗ | R&D intensity 代理创新测量可能不全面 |
| 方法局限（Limitation） | Limitation | ✗ | 面板数据但未用 IV，因果推断受限 |
| 结论升华 | — | ✗ | 无 elevated plane 结尾 | 必须增加 conclusion 段落，回到 Introduction 的 paradox，展示 conversation 已改变 |

## 实践意义
| 检查项 | 状态 | 建议 |
|-------|------|------|
| 具体 actors/decisions | ✗ | "Managers should update their routines" 过于笼统 | 改为具体 actor（如 "CEOs of established manufacturing firms"）和具体决策（"allocate 15-20% of digital investment to routine reconfiguration before technology deployment"） |
| 受众对齐 | ✗ | 未锁定具体决策者 |
| 可操作性 | ✗ | "should update" 不够具体 |

## 最需改写的 2 个段落
1. **第一段（结果复述段）** — 问题：严重的 Rehashing。Discussion 开头不应再报告系数，而应直接回答研究问题并进入理论解释。
   
   **改写建议**：
   "Our study demonstrates that digital transformation enhances firm innovation performance **not merely through technological investment, but through the mediating mechanism of organizational routine updating**. This finding moves beyond the direct-effects paradigm that has dominated prior research by revealing the organizational infrastructure through which technological change translates into innovation outcomes."

2. **实践启示段** — 问题：Superficial + 不具体。
   
   **改写建议**：
   "Our findings provide insights into how **CEOs of established manufacturing firms** should **allocate resources to routine reconfiguration before large-scale technology deployment**. For example, firms that invest in digital tools without revising procurement, production, or quality control routines may find that technological capabilities fail to translate into innovation gains. **Overall innovation performance could suffer if managers focus on technology acquisition at the expense of the organizational processes that must adapt to absorb technological change.**"

## 推荐下一步
基于本 Discussion 的严重 Rehashing 和 Superficial 问题，建议作者结合本文实际文献对话进行结构性重写；本 skill 只给出问题定位、证据和局部修订目标。
```
