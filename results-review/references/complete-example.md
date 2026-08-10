# 完整示例 — Results 审查

仅在需要端到端示例时阅读本文件；常规审查不预加载。

### 输入
```
/results-review
Table 2 presents the main results. Model 1 includes only control variables. Model 2 adds digital transformation, which is positively related to innovation performance (β = 0.32, p < 0.01). Model 3 adds organizational routine updating, and the coefficient for digital transformation decreases but remains significant (β = 0.18, p < 0.05), supporting mediation. Model 4 includes the interaction between digital transformation and absorptive capacity, which is positive and significant (β = 0.15, p < 0.05).

We conducted several robustness checks. First, we used patent count as an alternative measure of innovation. Second, we used fixed effects. Third, we excluded high-tech firms. All results remain consistent.
```

### 输出
```
## 假设-结果对齐表
| 假设 | 结果位置 | 方向 | 显著性 | 支持判断 | 问题 |
|-----|---------|------|--------|---------|------|
| H1 | Model 2 | + | p<.01 | Supported | 未报告经济显著性 |
| H2 | Model 3 | + | p<.05（推断） | Supported | 未明确报告 mediator 系数 |
| H3 | Model 3 | Mediation | p<.05 | Supported | 仅报告系数下降，未报告 Sobel/z-test |
| H4 (interaction) | Model 4 | + | p<.05 | Supported | 未报告简单斜率 |

## 结果节奏检查
| 假设 | 重述 | 指向模型 | 报告系数 | 判断支持 | 缺失拍子 |
|-----|------|---------|---------|---------|---------|
| H1 | ✗ | ✓ | ✓ | ✗ | 第1拍、第4拍 |
| H2 | ✗ | ✓ | △ | ✗ | 第1拍、第4拍、效应量 |
| H3 | ✗ | ✓ | △ | ✗ | 第1拍、第4拍、正式中介检验 |
| H4 | ✗ | ✓ | ✓ | ✗ | 第1拍、第4拍 |

**核心问题**：所有假设都缺失第1拍（Restate hypothesis）和第4拍（State support）。读者无法直接知道每行结果对应哪个假设。

## 交互/非线性效应
| 检查项 | 状态 | 建议 |
|-------|------|------|
| 主效应解释警告 | ✗ 缺失 | 必须警告：交互存在时，主效应不能单独解释 |
| 边际效应图 | ✗ 缺失 | 建议绘制 digital transformation × absorptive capacity 的边际效应图 |
| 条件效应数值 | ✗ 缺失 | 报告 high/low absorptive capacity 下的 conditional effects |
| 简单斜率检验 | ✗ 缺失 | 补充 simple slope analysis |

## 稳健性检验
| 检验类型 | 目的 | 组织方式 | 评价 |
|---------|------|---------|------|
| Alternative DV (patent count) | 测量效度 | 未说明 threat | △ 仅罗列，未解释为什么 patent count 更好/更差 |
| Fixed effects | 未观察异质性 | 未说明 threat | △ 未解释为什么选择 FE 而非 RE |
| Exclude high-tech firms | 样本敏感性 | 未说明 threat | △ 未解释为什么 high-tech firms 可能不同 |

**稳健性问题**：
1. **无 threat 组织逻辑**：每项检验应遵循 "问题→为什么重要→做了什么→结果如何→对解释的影响"
2. **缺少关键稳健性检验**：
   - Endogeneity：IV / 2SLS / GMM
   - Alternative model：Logit/Probit（如果 innovation 是计数或二元变量）
   - Sample sensitivity：按行业/规模分样本

## 最需改写的 2 个结果段落
1. **所有假设结果的开头** — 问题：缺失 "Restate hypothesis" 拍子。建议每段开头增加："Hypothesis 1 predicted that digital transformation is positively related to innovation performance."
2. **稳健性检验段落** — 问题：简单罗列，无 threat 逻辑。建议按以下结构重组：
   ```
   5.1 Endogeneity Concerns
   [为什么内生性是 threat → 用了什么方法 → 结果如何 → 对核心解释的影响]
   5.2 Alternative Measures
   [为什么测量选择可能影响结果 → 替代测量是什么 → 结果如何]
   ```
```
