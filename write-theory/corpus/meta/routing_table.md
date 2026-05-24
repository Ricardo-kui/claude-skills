# Introduction → Theory 快速路由表

本表建立在 Introduction 的 Gap 类型、Tension 模板、Makadok 贡献维度与 Theory 构建变体之间的映射关系。

**使用方式**：write-theory 在 Phase 0 诊断时，如果检测到上游传入了 Introduction 输出，先查本表给出默认推荐，再进入交互式确认。

---

## 一级路由：Gap × Makadok → Theory Variant

| Gap | Makadok | 典型 Tension | Theory Variant | 置信度 | 说明 |
|-----|---------|-------------|----------------|--------|------|
| Incompleteness | Mechanism | `01-despite-progress-unaddressed` | **机制推演型** | 高 | 标准配置：已有文献遗漏了中介机制 |
| Incompleteness | Boundary | `01-despite-progress-unaddressed` | **假设树型** 或 **调节效应型** | 中 | 取决于 moderator 是核心贡献还是补充分析 |
| Incompleteness | Constructs | `05-construct-confusion` | **构念辨析型** | 高 | 文献用不同标签指同一现象，需要厘清 |
| Incompleteness | Phenomenon | `01-despite-progress-unaddressed` | **机制推演型**（现象驱动） | 中 | 新现象需要建立 baseline 机制 |
| Inadequacy | Mechanism | `02-implicit-assumption-wrong` | **机制推演型** | 高 | 现有机制假设错误，需要替换 |
| Inadequacy | Mechanism + Boundary + Output | `15-practical-puzzle` / `14-debate-unresolved` | **调节效应型** (E) | 高 | 实践信念与研究发现矛盾，需机制解释 + 边界条件 + 输出预测。JOM/JM/AMJ 常见配置 |
| Inadequacy | Constructs | `05-construct-confusion` | **构念辨析型** | 高 | 构念误置导致理解偏差 |
| Inadequacy | Boundary | `03-structural-blindspot` | **假设树型** 或 **调节效应型** | 中 | 现有边界设定有误 |
| Incommensurability | Constructs | `06-theoretical-imbalance` | **竞争假设型** | 高 | 两个理论对同一构念关系给出相反预测 |
| Incommensurability | Mechanism | `06-theoretical-imbalance` | **竞争假设型** 或 **构念辨析型+机制** | 中 | 竞争机制需要实证裁决 |
| Incommensurability | Boundary | `04-reality-contradicts-consensus` | **假设树型**（对立调节） | 中 | 矛盾发现需要条件化解释 |

---

## 二级路由：Introduction 信号 → Theory 子协议

| Introduction 信号 | 检测方法 | 推荐子协议 |
|-------------------|----------|-----------|
| Preview 提及"双重效应""两种路径""相反预测" | 字符串匹配：dual / opposite / competing / contrasting | **B2 双轨并行**（若在同一构念的两个维度）或 **F 竞争假设型**（若两种理论对立） |
| Preview 提及"取决于""因...而异""边界条件" | 字符串匹配：contingent / depends / boundary / moderate | **E 调节效应型** 或 **C 假设树型** |
| Preview 含 "practical puzzle" / "widely believed among practitioners" / "contradiction leads to a puzzle" | 字符串匹配：practical puzzle / widely believed / conventional wisdom | **E 调节效应型**（常配 E3/E4/E5 扩展协议） |
| Tension 含 "On the one hand... On the other hand..." 对立发现 | 字符串匹配：on the one hand / on the other hand / competing predictions | **E 调节效应型** 或 **C 假设树型**（若 moderator 是核心贡献） |
| Preview 提及"过程""阶段""随时间演化" | 字符串匹配：process / stage / over time / unfold | **D 质性过程理论型** |
| Contribution 声明含 "distinguish A from B" | Makadok=Constructs + 关键词 distinguish / differentiate | **A 构念辨析型** |
| Contribution 声明含 "explain why / identify mechanism" | Makadok=Mechanism + 关键词 explain / mechanism / mediate | **B 机制推演型** |
| Contribution 声明含 "reconcile conflicting findings" | Makadok=Boundary + 关键词 reconcile / contingent | **C 假设树型** 或 **E 调节效应型** |

---

## 三级路由：Gap 能量 → Theory 论证深度

| Gap 能量 | Theory 机制深度要求 | 假设结构倾向 |
|----------|---------------------|-------------|
| 低 (Incompleteness) | 两步链 (X→M→Y) 即可 | 主效应 + 中介 |
| 中 (Inadequacy) | 两步链 + 一个调节嵌入点 | 主效应 + 中介 + 调节 |
| 高 (Incommensurability) | 至少两步链，且需要解释"为什么两种理论都看似合理" | 竞争假设对 或 主效应 + 多条件调节 |

---

## 非标准模块序列

### T3-T5-T3-T5 交替序列

对于具有**双重机制**和**双重边界条件**的论文，模块顺序可能不是标准的 T3→T5 或 T3→T3→T5，而是交替出现：

```
Mechanism → Hypothesis → Boundary → Hypothesis → Mechanism → Hypothesis → Boundary → Hypothesis
(T3)       (T5)        (T3)       (T5)        (T3)       (T5)        (T3)       (T5)
```

**适用条件**：
- 两个机制各自对应独立的边界条件
- 机制之间相对独立，不宜合并为单一 T3 段落
- 论文采用 "假设树" 结构而非线性推导

**语料锚定**：
- Darby 2023 (MSOM) — dual mechanisms (ownership→timing, ownership→spillover) with dual boundaries (severity, defect type)

---

## 路由冲突处理

当一级路由和二级路由给出不同推荐时：
1. 优先二级路由（基于 Introduction 中的具体措辞信号）
2. 如果二级路由信号弱（只出现1次关键词）， fallback 到一级路由
3. 如果 Gap=Incommensurability 且 Makadok=Constructs，强制走竞争假设型（这是 write-theory 2.1.0 新增的核心映射）
