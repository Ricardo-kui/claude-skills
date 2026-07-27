# Reasoning Soundness Protocol（论证可靠性协议）

**核心定位**：`hypothesis_derivation_patterns.md` 保证推理**形式有效**（validity：链条步步写出、无跳跃）；本协议保证论证**可靠**（soundness：前提可信、机制必要、推导经得住反例）。审稿人攻击的是前提，不是推理形式——一条形式完美的链条，只要最弱前提被击穿，整段推导塌陷。

**与三层追溯的关系**：本协议是"理论前提 → 因果机制 → 实证预测"三层追溯的审计显式化——Anchor→Mechanism→Warrant→Prediction 解决了追溯的书写，本协议解决追溯的**可靠性**。

**使用时机**：Phase 3 每个假设推导段落成稿后、进入 Phase 4 之前执行；theory-review 在 Step 2 why chain 审查后对称执行。

---

## 1. 前提三分法（Premise Typing）

推导链中每个 Anchor 和 Warrant 的前提，必须能标注为以下三类之一。标注不出类型的前提 = 伪装成前提的断言，删除或改写。

| 类型 | 定义 | 可攻击面 | 防守方式 |
|------|------|---------|---------|
| **Definitional（构念定义性前提）** | 由构念定义直接给出（"X 意味着 Y"） | 定义本身被质疑（循环定义、与相邻构念无区分） | 引构念文献锚定定义；过 Phase 4 审计 2（Construct Clarity 四字段） |
| **Stipulation（理论规定）** | 某理论框架内部的命题（"根据 [理论]，行动者会…"） | 理论适用性被质疑（该理论是否适用于本情境/本分析层次） | 引理论权威原典 + 一句情境适用性论证；层次混合时显式声明桥接 |
| **Empirical（经验概括）** | 前人实证发现的概括（"已有研究表明 X→Y"） | 证据的情境/样本/测度与本文不匹配；证据本身是混合的 | 总结 finding 而非罗列名字；边界不一致时降级为"mixed evidence"并转化为 puzzle |

**标注操作**：对推导段落逐句扫描，给每个承载前提的句子打 [D]/[S]/[E] 标记。一段标准推导通常含 1 个 [D]（构念锚定）+ 1–2 个 [S]（理论机制）+ 1–2 个 [E]（文献支撑）。

---

## 2. 最弱环节标记（Weakest-Link Marking）

**链条强度 = 最弱前提的强度**。标注类型后，按防守成本排序找出最弱前提：

- [E] 前提若证据来自**不同情境/不同层次/不同测度** → 通常最弱
- [S] 前提若理论是**跨界借用**或**层次桥接**（个体理论解释组织现象） → 次弱
- [D] 前提若构念是**新引入或重新界定** → 最弱（定义尚未取得读者共识）

**处置规则**：
1. 最弱前提必须有**单独一句防守**（不能混在 warrant 里顺带带过）
2. 防不住的最弱前提 → **降级 claim**：把 "X causes Y" 降级为 "X makes Y more likely when…"，或把该前提转化为明确假设前提（"We assume that…"）——显式假设比隐含脆弱前提更不易被攻击
3. 一段推导有 ≥2 个 [E] 前提跨情境借用 → 考虑改用 Multi-Mechanism Trunk（多路径并行），让读者即使不接受某条路径也可接受假设（参见 `hypothesis_derivation_patterns.md`）

---

## 3. 机制必要性门控（Necessity Gate）

在承诺一个新机制之前，必须过三问——这是 Ilicic & Brennan "M_new 推不出 D_reversed" 反模式的泛化，从事后检查上升为事前门控：

| 问 | 通过标准 | 不通过的处置 |
|---|---------|-------------|
| **Q1 替代充分性** | 主流/更简单的机制（field 默认 M_old）**不能**推出同一预测 | 若 M_old 已能推出同一预测 → 你的机制是装饰：删除，或降级为 Discussion 中的替代解释讨论 |
| **Q2 可区分性** | 你的机制能推出 M_old 推不出的**额外可检验预测**（不同方向/不同边界条件/不同中介） | 若两机制预测完全等价 → 补一个可区分预测（通常是一个 moderation），否则删除 |
| **Q3 反事实塌陷** | 删掉你的机制后，故事**不**照样成立 | 若删掉后推导链仍完整 → 该机制从未承重，删除 |

**与 `sentences/mechanism_chain.md`「替代机制排除骨架」的关系**：那是提出中介**之后**的排他性句法（写作层）；本门控是承诺机制**之前**的取舍纪律（设计层）。先过门控，再用排除骨架书写。

**与 Outer Limits 的关系**：`golden-biddle-locke-four-moves.md` §Outer Limits 约束你**攻击文献**时不得稻草人；本门控约束你**建设自己**时不得装饰。两者是同一诚实纪律的两个方向。

---

## 4. 反例压力测试（Counterexample Stress Test）

对每个 Mechanism Move 问一个问题：**"什么条件下这一步不成立？"**

三种处置，按优先级：

1. **补 scope condition**：答得上来的条件 → 写进推导（"when [condition], this step holds because…"）。这是 moderation 假设的天然生成器——压力测试答出的条件往往就是下一个 moderator
2. **生成新假设**：条件差异本身有理论趣味 → 升级为 E 调节效应型假设（调用 `variants/E_moderation.md`）
3. **删除该步骤**：条件答不上来且步骤非必要 → 删除（链条越短，可攻击面越小）

**反模式**：
- 把压力测试答出的条件**藏起来不写**——审稿人会替你发现，且以 "theory is under-specified" 的形式
- 对每个步骤都补 scope condition → 推导变成条件清单，失去主线；只为**最弱前提所在的步骤**和**反直觉步骤**做测试即可

---

## 5. 输出格式（Soundness Card）

每个假设推导段落完成 soundness 审计后，输出一张卡片（内部工作文档，不进正文）：

```
H[X] Soundness Card
├─ 前提清单: [D]×n / [S]×n / [E]×n
├─ 最弱前提: [引用该句] → 防守句: [已写 / 已降级 claim / 已转显式假设]
├─ 必要性门控: Q1 ✓/✗ · Q2 ✓/✗ · Q3 ✓/✗ → 处置: [保留 / 补可区分预测 / 删除]
└─ 反例测试: 步骤 [k] 条件 "[condition]" → 处置: [scope / 新假设 / 删除 / 不适用]
```

Phase 4 审计 4 复核所有卡片的处置列是否兑现。

---

## 与相邻文件的关系

- [`hypothesis_derivation_patterns.md`](hypothesis_derivation_patterns.md)：validity 层（形式有效的动作序列），本文件是其 soundness 镜像
- [`../sentences/mechanism_chain.md`](../sentences/mechanism_chain.md)：替代机制排除的**句法**（事后书写），本文件 §3 是门控（事前取舍）
- [`evidence_patterns.md`](evidence_patterns.md)：Warrant 的证据类型与引用句式；本文件 §1 决定该前提**该不该用、用什么类型防守**
- `../../diagnose-introduction/references/golden-biddle-locke-four-moves.md` §Outer Limits：攻击文献的诚实纪律；本文件 §3–4 是建设自己的同一纪律
