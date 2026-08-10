# 完整示例 — Introduction 审查（快速模式）

仅在需要端到端示例时阅读本文件；常规审查不预加载。

### 输入
```
/intro-review
Digital transformation has become a strategic imperative for firms worldwide. Existing research has extensively studied the direct effects of technology adoption on innovation outcomes. However, few studies have examined the mechanisms through which digital transformation affects innovation. Drawing on organizational routine theory, we argue that organizational routine updating mediates this relationship. Our study contributes to the literature by identifying this mechanism.
--journal=SMJ
```

### 输出
```
## Introduction 结构解析
[段落1] Function: Hook — "Digital transformation has become a strategic imperative..."（cold-start definition，符合 SMJ 风格）
[段落2] Function: Conversation — 技术采纳→创新绩效文献回顾（Progressive Coherence）
[段落3] Function: Problematization — "However, few studies have examined..."（⚠️ 薄弱）
[段落4] Function: Preview — 组织惯例理论 + 中介机制 + 贡献声明

## QC 检查表
| QC 项 | 评分 | 问题摘要 | 优先级 |
|-------|------|---------|--------|
| Hook 服务主题 | ✓ | 数字化转型定义 Hook，温和建立领域 | 低 |
| Conversation 理论对话 | △ | 文献回顾较完整，但缺少明确的理论定位（如 RBV vs 动态能力） | 中 |
| Problematization puzzle | ✗ | "few studies have examined" 是典型禁忌，未呈现 puzzle 或理论重要性 | **高** |
| So what 重要性 | ✗ | 未解释为什么机制缺失是理论上重要的 | **高** |
| What we learn 可见性 | △ | Mechanism 维度声明存在，但不够具体 | 中 |
| 段落 transitions | ✓ | 逻辑过渡清晰 | 低 |
| Hook-Gap 匹配 | ✓ | Cold-start 匹配 Incompleteness 低强度 Gap | 低 |
| Gain/Pain 具体性 | ✗ | "few studies have examined" 是典型的 generic gap language，未说明具体 pain | **高** |
| Target audience 可见性 | △ | 第 1 段暗示了技术战略学者，但未明确锁定理论社群 | 中 |
| Preview Credibility | △ | 提到组织惯例理论但未交代为何该理论适合此情境 | 中 |
| Claim fit | △ | 贡献声明（identifying mechanism）与结果范围一致，但不够具体 | 中 |

## 最需改写的段落
段落 3（Problematization）— 原因："few studies have examined" 直接暴露了 Incompleteness Gap 的最大风险——被解读为增量研究。这是 reviewer 最常攻击的点。— 对全文影响：如果 Problematization 不成立，后续所有理论贡献都会失去合法性。

## 改写建议
**模板**：
"Despite the progress made in understanding how digital transformation affects firm performance, **the question of how and through what mechanisms this relationship unfolds has gone largely unaddressed**. This omission is theoretically important because without identifying the mediating mechanisms, we cannot explain why some firms successfully translate digital investments into innovation outcomes while others do not."

**说明**：
1. 保留 "has gone largely unaddressed" 作为 Incompleteness 标志性语言
2. 增加 "theoretically important because..." 论证，超越 "few studies"
3. 引入对比（some firms... while others...）制造轻微 tension

**变体**（如需更强 tension）：
"Although researchers have extensively studied the direct effects of technology adoption, **the mediating mechanisms that translate technological change into innovation remain poorly understood**. Existing theory assumes that digital investment automatically enhances innovation capacity, yet empirical evidence shows mixed results, suggesting that critical organizational processes have been overlooked."

## 推荐写作模板
本 Introduction 呈现 **Incompleteness × Mechanism** 组合特征。推荐参照：
`/write-introduction Incompleteness Mechanism`

## 回流检查
修改后请确认：
- [ ] Hook 是否仍与最后一句话呼应？
- [ ] Discussion 是否能兑现 "organizational routine updating as mediating mechanism" 的承诺？
- [ ] Problematization 是否超越了 "few studies have examined"？
```
