# 完整示例 — 全稿诊断端到端

仅在需要端到端示例时阅读本文件；常规诊断不预加载。

## 输入

```
/paper-review
[粘贴论文全文：Introduction + Theory + Methods + Results + Discussion]
--journal=SMJ
```

## 输出（摘要）

```
## 全稿故事架构诊断

### Knot 评估
- **状态**: 模糊
- **一句话概括**: 数字化转型如何影响创新绩效？（过于宽泛，缺少理论张力）
- **问题**: Knot 是描述性问题而非 puzzle。缺少 "why" 或 "when" 的理论缺口。

### 五幕结构映射
| 幕 | 对应段落 | 评价 |
|---|---------|------|
| Exposition | Introduction P1-P2 | ✅ Hook + Conversation 完整 |
| Rising | Introduction P3-P4 + Theory P1-P3 | ⚠️ Problematization 薄弱， tension 不足 |
| Climax | Results P1-P3 | ✅ 假设检验完整 |
| Falling | Results P4-P5 + Discussion P1 | ⚠️ 稳健性检验组织松散 |
| Denouement | Discussion P2-P6 | ✗ Discussion 复述 Results，未兑现 Introduction 承诺 |

### 角色评估
| 角色类型 | 构念 | 评价 |
|---------|------|------|
| Main character | Digital transformation (IV) | ✅ 明确 |
| Main character | Innovation performance (DV) | ✅ 明确 |
| Supporting character | Organizational routine updating (Mediator) | ⚠️ 主角化程度不足，why chain 弱 |

### Theme 一致性
- **核心 Theme**: 数字化转型通过组织惯例更新影响创新绩效
- **漂移检查**: Methods 和 Results 中变量名一致，但 Discussion 未回到 "routine updating" 机制

### 讨论兑现
- **Introduction 承诺**: "We explain why... by identifying organizational routine updating as the mediating mechanism"
- **Discussion 交付**: "Our findings show that digital transformation has a positive effect..."（复述结果，未解释机制）
- **状态**: 落空

### Two-literature 架构
- **Literature 1（Gap 文献）**: 数字化转型与创新绩效文献（技术战略/创业研究）
- **Literature 2（理论文献）**: 组织惯例理论（组织理论）
- **分工清晰度**: 清晰
- **主要风险**: 无。本文符合 Two-literature 原则：用组织惯例理论（Lit 2）解释数字化转型文献（Lit 1）中的机制缺口。Discussion 如修复后应同时回馈两个文献。

## 写作阶段判定
**阶段**: Stage 2 — Blocking in the scene
**理由**: 粗稿结构完整，但 Problematization 薄弱、why chain 不完整、Discussion 未打磨。

**最该做的 3 个动作**:
1. **强化 Introduction Problematization**：当前 "few studies have examined" 是典型禁忌，需升级为 theoretically important omission
2. **补全 Theory why chain**：H1 和 H2 的机制推导过于直白，缺少 performative tension 等理论张力
3. **重写 Discussion 开头**：停止复述 Results 系数，直接回答研究问题并进入理论解释

## Section 优先级排序
1. **Discussion** — 问题：严重的 Rehashing 和 Superficial，未兑现 Introduction 的 Mechanism 承诺 — 根因：作者可能未意识到 Discussion 是 denouement 而非 Results 加长版
2. **Introduction** — 问题：Problematization 薄弱，Knot 缺少理论张力 — 根因：Gap 诊断不明确，可能混淆了 Incompleteness 和 Inadequacy

## 建议调用的 Skill

**首选**:
```
/discussion-review <文件路径>
```
**理由**: Discussion 是全稿最薄弱环节，Rehashing 和 Superficial 问题严重，需要专项审查。

**备选**:
```
/intro-review <文件路径>
```
**理由**: Introduction 的 Problematization 问题根源于 Knot 不清晰，修复后可能改善全稿理论合法性。

**长期建议**:
```
/pollock-qc all <文件路径>
```
**理由**: 当 Discussion 和 Introduction 修复后，执行全稿 Pollock QC 确保跨 section 一致性。
```
