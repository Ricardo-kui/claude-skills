---
corpus: write-methods-micro-templates
description: 句法微模板库（Sentence-Level Micro-Templates）。从顶刊 Methods 段落中提取的可复用句法单元，供 write-methods 在组装骨架时替换默认措辞，丰富表达多样性。
organization: by_functional_unit
categories_count: 18
created: 2026-05-22
updated: 2026-08-03
---

# 句法微模板库（Micro-Templates）

## 设计目标

段落级骨架（`corpus/[设计类型].md`）解决"段落的结构功能"问题；
句法微模板解决"段落内部的表达多样性"问题。

同一骨架填入不同微模板，可生成风格迥异的段落，避免同质化。

## 与段落骨架的关系

```
段落 = 骨架（结构功能）
       + 微模板选择（句法单元替换）
       + 用户填入的具体事实（变量名、样本量、估计器名）
```

## 分类索引

| 分类 | 文件 | 功能 | 对应槽位 |
|------|------|------|---------|
| [段首锚定短语](opening-anchors.md) | 告诉读者"本段做什么" | M1–M10 所有段首 |
| [because 从句架构](because-clauses.md) | 论证控制变量、样本排除、构念效度的理由 | M2, M3, M4, M6；微模板 A：理论驱动观察窗 because 从句（窗口=构念活跃期证据 + 数据窗/事件窗 lag 结构分离），westphal_zajac_1998_symbolic_management，VERIFIED (expert_audit_override 2026-08-28)；变体 B：M4 测量窗对齐 because 从句 — 累积窗与另一解释变量统一以使交互项可估（窗口由估计设计而非构念证据决定），anand_mukherjee_2024 |
| [因果动词梯度](causal-hedging.md) | 根据设计强度选择因果声称力度 | M3, M4, M7 |
| [过渡衔接短语](transitions.md) | 段落内部的逻辑推进标记 | M1–M10 任意多句段落 |
| [样本漏斗节奏](funnel-rhythm.md) | 数字叙事的句法序列 | M2；起始总体补充：样本框三理由枚举辩护（数据可得性/响应率/研究缺口），westphal_bednar2005，EMERGING；响应率工程链（反差定位→编号步骤→对标收口），carpenterwestphal2001，EMERGING |
| [识别策略预告](identification-foreshadowing.md) | 在 Methods 中预告 Results 的诊断检验 | M8 |
| [变量操作化句式](variable-operationalization.md) | 构念→测量→来源→方向的表述方式 | M3, M4, M5 |
| [稳健性检验预告](robustness-foreshadowing.md) | Methods 中预告 Results 的稳健性检验 | M8, M10；样本选择补充：问卷非应答 K-S+Heckman 双重防御链，westphal_bednar2005，EMERGING；非应答 K-S+双层代表性检验（IV/控制变量分别代表性声明+限定语收口），carpenterwestphal2001，EMERGING |
| [模型选择比较](model-selection-comparison.md) | 分布/连接函数/规格比较时的叙事单元 | M7 |
| [识别策略外生性](identification-exogeneity.md) | IV 排他性约束、自然实验外生性来源、控制函数识别变量的理论论证 | M4, M7, M8 |
| [多源数据匹配](multi-source-matching.md) | 多个独立数据源交叉合并的叙述 | M2 |
| [手工编码与效度检验](manual-coding-validation.md) | 从原始文本/痕迹提取构念并进行编码效度验证 | M3, M4；微模板 A：反规则手册编码协议（规则书推高信度牺牲效度的预辩 + recording unit 声明 + pre-negotiation 信度三件套），westphal_zajac_1998_symbolic_management，VERIFIED (expert_audit_override 2026-08-28)；变体 B：问卷量表开发六环效度链（预测试→题项依据→反偏差→信度→双界因子→计分），carpenterwestphal2001，EMERGING |
| [子样本分组与平行方程](subsample-grouping.md) | 样本分组估计、多方程并行呈现的结构说明 | M4, M5, M7 |
| [CMB 预防论证](common-method-bias-prevention.md) | 问卷数据 CMB 预防的设计+统计论证 | M8；变体 D：多源评价者分离+Kappa一致性链（五拍，换源互换收口），carpenterwestphal2001，EMERGING；变体 E：单波截面 CMB 退路链——预试+Harman+验证子样本 congruence 审计（gulati_2007 ASQ；无时间分离退路+随机子样本档案基准比对 >.90；区别于变体 A/B 时间分离、变体 C 标记变量、变体 D 多源 Kappa），EMERGING |
| [高管信心/人格特质操作化](executive-confidence-operationalization.md) | 期权 moneyness、媒体描述、显著性—薪酬复合代理、双代理收敛、继任者对照与构念形成窗—结果观察窗分离 | M2, M4, M8 |
| [四分位距经济显著性](interquartile-economic-significance.md) | 用自变量 IQR（25th–75th）移动解释回归系数的经济显著性 | M7, M8, M10, Results |
| [Heckman 同行 Prevalence 排他性限制](heckman-peer-prevalence-exclusion.md) | Heckman 选择模型中同行 prevalence 作为排除限制的理论论证与跨 segments 加权 | M7, M8 |
| [替代 DV Falsification](alternative-dv-falsification.md) | 用行为者领域外的替代因变量进行 falsification 检验并讨论替代/转换 | M8, M10 |

## 使用协议

1. **提取**：`distill-methods-exemplar` Phase 2.6 从论文 Methods 段落中提取微模板，存入对应分类文件。
2. **评级**：每个微模板标注：
   - `frequency`：在 MVP30 语料库中出现次数（高/中/低）
   - `transferability`：跨设计类型可迁移性（通用/条件/受限）
   - `risk_level`：误用风险（安全/需注意/高风险）
3. **组装**：`write-methods` 输出段落骨架时，在 `[placeholder]` 层级之下，为关键句法位置提供 2–3 个微模板选项供用户选择。
4. **累积**：同一骨架的同一槽位，应支持多套微模板轮换，避免所有论文读起来像同一个人写的。

## 诚实边界

- 微模板不是"万能句式"，必须匹配骨架的功能定位才能填入。
- 高风险的微模板（如强因果动词）只能在对应设计强度的骨架中使用。
- 不虚构微模板的来源论文或出现频次。
