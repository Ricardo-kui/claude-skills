# Theory & Hypotheses 蒸馏快速参考

> **何时使用**: 当完整 SKILL.md 因上下文压缩不可用时，Read 本文件并按此协议执行蒸馏。本文件是 SKILL.md Phase 0-3 的精简版。
> **目标**: 确保格式一致的 Fine-Grained Profile，即使完整 skill 指令不可用。

---

## 0. 输出文件命名与路径

```
Vault路径: D:\OneDrive\Obsidian Vault\00 工作台\叙述模板训练集\narrative_analysis\introduction\mvp30\fine_grained\batch_2026-05-24\
文件命名: {author_lowercase}_{year}_{journal}_distilled_theory.md
```

---

## 1. Phase 0 — 理论构建类型分类（必须包含证据链）

### 构建类型判断（六选一）

| 类型 | 标志性语言 | 核心标志 |
|------|-----------|---------|
| **A 构念辨析型** | "Although often used interchangeably, A and B are distinct..." / "Whereas A entails..., B involves..." | 对比两个易混淆构念 |
| **B 机制推演型** | "We argue that X influences Y through M..." / "Specifically, X creates [state] that..." / "The mechanism underlying..." | 多步因果链，中介或间接效应 |
| **C 假设树型** | "However, this effect is not uniform; rather, it is contingent on..." / "The strength/direction depends on..." | 条件化预测，moderator 引入 |
| **D 质性过程理论型** | "unfolds through N phases..." / "In Phase 1,... As [transition], the process shifts to Phase 2..." / "Over time,..." | 时间/阶段标记 |
| **E 调节效应型** | "The relationship between X and Y is moderated by W, such that..." / "When W is high, X has a [stronger/weaker] effect" | 交互项是理论核心 |
| **F 竞争假设型** | "Two competing perspectives offer divergent predictions..." / "On the one hand... On the other hand..." | 对立预测裁决 |

### 输出格式（必须严格遵循）
```text
[构建类型判定]: [类型，混合型标注主导+辅助]
[标志性语言证据]: 
  - "具体句1" (段落位置)
[判定理由]: 一句话
[反证排除]:
  - 非 [类型A]: 理由
  - 非 [类型B]: 理由
[置信度]: 高 / 中 / 低

[推理结构判定]: 线性因果链 / 发散树 / 收敛网 / 辩证对立 / 过程演化 / 双路径并行 / [混合]
[假设结构判定]: 纯主效应 / 主效应+中介 / 主效应+调节 / 中介+调节混合 / 三向交互 / 构念分解
```

---

## 2. Phase 1 — 功能模块映射

### 6 个标准模块（T1-T6，标注 located: true/false）

| 模块 | 功能 | 识别标志词 |
|------|------|-----------|
| T1 Construct Definition | 界定核心构念 | "We define..." / "...refers to..." / "...is conceptualized as..." |
| T2 Theoretical Lens | 引入理论视角 | "Drawing on..." / "Building on..." / "We adopt..." |
| T3 Mechanism Chain | 推演因果机制 | step-by-step why chain; "Specifically..." / "This in turn..." / "Consequently..." |
| T4 Hypothesis Derivation | 形式化假设 | "Therefore, we hypothesize:" / "Thus:" / "Accordingly," |
| T5 Boundary Condition | 论证边界条件 | "However, this effect..." / "The relationship is contingent on..." |
| T6 Closure | 收束论证 | "Taken together..." / "In sum..." / "Our theoretical framework suggests..." |

### 输出：标记 actual_module_sequence + deviation_from_standard

---

## 3. Phase 1.5 — 模块覆盖检查

### 构建类型强制模块表（简版）

| 构建类型 | 强制模块 | 高风险缺失 |
|----------|---------|-----------|
| A 构念辨析型 | T1, T2, T4, T6 | T1 缺差异化维度 |
| B 机制推演型 | T1, T2, T3, T4, T6 | T3 缺多步 why chain |
| C 假设树型 | T1, T2, T3, T4, T5, T6 | T5 缺 moderator 理论依据 |
| D 质性过程型 | T1, T2, T3, T6 | T3 缺时间/阶段标记 |
| E 调节效应型 | T1, T2, T3, T4, T5, T6 | T5 缺 moderator 独立理论依据 |
| F 竞争假设型 | T1, T2, T3, T4, T6 | T3 缺双方机制并置 |

### Why-Chain 压力测试（5 个问题）：
1. 如果边界条件不成立，机制是否仍然成立？
2. 反方向是否可能？（反向因果是否排除？）
3. 替代解释是否被排除？
4. 每一步是否有独立的理论依据？
5. 是否会产生未预见的副效应？

---

## 4. Phase 2 — 表达骨架提炼

### 三步节奏（对 T3/T4 假设推导段落）：
```
[拍1-方向]: Topic Sentence — 本段要证明什么
[拍2-机制]: Theoretical Reasoning — 为什么 X 影响 Y（逐步）
[拍3-证据]: Literature Support — 前人研究如何支撑
[拍4-收敛]: Hypothesis Transition — "Therefore, we hypothesize: H[N]..."
```

### 骨架输出格式：
- **句法模板**: 用 `[占位符]` 泛化
- **语料锚定**: {author_year_journal}，具体段落位置
- **可迁移性**: 高/中/低 + 适用条件
- **反模式**: 至少 2 条

---

## 5. Phase 3 — Theory DNA

### 必须包含的量化指标：
| 指标 | 值 |
|------|-----|
| 理论密度 | 总 theory 词数 / 假设数 |
| 机制步数 | 单步 / 两步 / 三步+ |
| 调节器数量 | N |
| 中介变量数 | N（如有） |
| T6 Closure | 是否存在 |
| 假设数 | N |

### Narrative Style Profile（必须包含）：
- **Tone**: 主语气 + 证据
- **Paragraph Rhythm**: 节奏描述（如 "广角→特写"）
- **Distinctive Features**: 该论文特有的理论构建特征（至少3条）
- **Quality Markers**: strongest_aspect / weakest_aspect（weakest_aspect **必须标注未支持假设**）

---

## 6. 跨 Section 对齐检查

| 检查项 | 问题 |
|--------|------|
| T2 ↔ Introduction I5 | Introduction 承诺的理论是否在 Theory 中兑现？ |
| T4 ↔ Introduction I7 | Contribution 声明的维度是否对应实际假设？ |
| T4 ↔ Methods | 假设变量是否在 Methods 中操作化？ |
| T3 ↔ Introduction I3 Gap | 机制是否回应了 Gap？ |
| T6 ↔ Results | 理论总结是否与实证发现一致？ |

如仅处理 Theory（无完整论文），标记为 N/A。

---

## 7. 关键反模式

- ❌ 构建类型判断无证据链（必须有 [标志性语言证据] + [反证排除]）
- ❌ 混合型未标注主导 vs 辅助（如 "B 主导 + E 辅助"）
- ❌ T3 机制链只有 citation 堆砌无 step-by-step 推演
- ❌ Phase 3 Quality Markers 未标注实证上未获支持的假设
- ❌ 骨架中嵌入论文特有机构/政策/行业名
- ❌ 混淆 Dual Mediator（X→M1+M2→Y, 同一DV）与 Twin DV（X→Y1 / X→Y2, 两个DV）
- ❌ T6 Closure 缺失未在 qualidade markers 中标注

---

## 8. 蒸馏后动作

1. 保存报告到 Vault fine_grained 目录
2. 检查是否有**新骨架**需要注册到 `write-theory` 语料库
3. 如有新机制链/调节模式 → 更新 `corpus/sentences/` + 更新 `corpus/_index.md`
4. 如有新 Introduction-Tension → Theory-Variant 路由 → 更新 `corpus/_index.md` 交叉引用表
