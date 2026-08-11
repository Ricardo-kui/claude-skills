# 完整示例 — Methods 审查

仅在需要端到端示例时阅读本文件；常规审查不预加载。

### 输入
```
/methods-review
We used panel data from Compustat for U.S. publicly traded firms from 2010 to 2020. Digital transformation was measured as IT investment intensity (IT expenditure / total assets). Organizational routine updating was measured using a survey-based scale adapted from prior research. Firm innovation performance was measured as R&D expenditure / total assets. We controlled for firm size, firm age, and industry. We used OLS with standard errors clustered at the firm level.
```

### 输出
```
## 样本漏斗重建
初始数据：Compustat U.S. 上市公司面板数据（2010-2020）
步骤1：未报告初始 N 和筛选标准 ⚠️
步骤2：未报告缺失值处理 ⚠️
最终样本：未报告最终样本量 ✗

**评估**：样本漏斗严重缺失。必须补充：
1. 初始观测值数量（firm-year）
2. 每一步 attrition 的原因和数量（如剔除金融企业、剔除缺失值）
3. 最终样本量，并与 Results 表格中的 N 对比验证

## 变量排列检查
| 顺序 | 变量名 | 类型 | 一致性 | 信效度报告 |
|-----|--------|------|--------|-----------|
| 1 | R&D expenditure / total assets | DV | ⚠️ | ✗ 未报告信效度 |
| 2 | IT investment intensity | IV | ⚠️ | ✗ 未报告 adapted scale 的来源 |
| 3 | Organizational routine updating | Mediator | ⚠️ | ✗ 未报告 survey scale 的信度（Cronbach's α） |
| 4 | Firm size, firm age, industry | Controls | ✓ | — |

**变量排列问题**：
- DV 使用 R&D intensity 代理创新绩效，但 Methods 未解释为什么不用专利数或新产品收入（construct validity 问题）
- Mediator 使用 survey-based scale，但在 Compustat 样本中如何获得 survey 数据？（数据来源矛盾）

## 控制变量逻辑
| 控制变量 | 控制理由 | 评价 |
|---------|---------|------|
| Firm size | 未提供 | ✗ 必须补充：大公司有更多资源进行数字化转型和创新 |
| Firm age | 未提供 | ✗ 必须补充：老企业惯例更僵化，可能抑制 routine updating |
| Industry | 未提供 | ✗ 必须补充：不同行业数字化程度和创新模式差异显著 |

**建议控制但未控制的关键变量**：
- **Prior innovation performance**：遗漏变量偏差，因为创新可能有路径依赖
- **CEO characteristics**：数字化转型决策通常由 CEO 推动
- **Competitive intensity**：竞争压力同时影响数字化和创新投入

## 分析方法
| 检查项 | 状态 | 问题 |
|-------|------|------|
| 模型选择理由 | ✗ | 未解释为什么用 OLS 而非面板数据模型（FE/RE） |
| 标准误调整 | △ | Clustered at firm level 正确，但未解释为什么不用 two-way clustering |
| 诊断检验报告 | ✗ | 未报告 VIF、异方差检验、自相关检验 |

**模型选择问题**：
面板数据使用 OLS 会忽略 unobserved heterogeneity。建议：
1. 报告 Hausman 检验，选择 FE 或 RE
2. 如果使用 OLS，必须解释为什么 firm fixed effects 不必要（如已有充分控制变量）

## 最需补强的 2 处
1. **样本漏斗缺失** — 补充完整的样本筛选过程（初始 N → 每一步 attrition → 最终 N），并报告选择偏差检验
2. **Mediator 数据来源矛盾** — Compustat 是二手数据库，survey-based mediator 需要明确说明数据来源（如匹配的 survey 数据、或改用二手指标）
```
