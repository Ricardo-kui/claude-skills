# Logical Fallacy Self-Check — 逻辑谬误自检（审稿人视角）

> **何时加载**：`pollock-qc` 执行全稿或 Theory/Introduction/Discussion section QC 时，用本清单做"审稿人视角的逻辑自检"——检测你的论证是否含有审稿人常用来拒稿的逻辑谬误。
> **来源**：Greene & Lidinsky (2017) *From Inquiry to Academic Writing* Ch09 *Recognizing Logical Fallacies*（15 类原始清单）。
> **裁剪原则**：G&L 原始 15 类涵盖政治/广告语境（bandwagon、appeal to fear、ad hominem）。本清单只收 **6 类管理顶刊高频致命谬误**——这些是 Reviewer 2 常见的杀伤性评语背后的逻辑命名。

---

## 为什么 FT50 写作需要这个

现有 skills 教你怎么写（结构、骨架、句式），但**不教你怎么躲审稿人的逻辑审查**。审稿人拒稿时常用的修辞武器——"作者搭了个 straw man"、"这是 false dichotomy"、"post hoc 而非因果"、"小样本过度外推"——背后全是这套逻辑谬误命名。投稿前用本清单自检，可预防这类拒稿理由。

这与 Pollock Ch04 五病（语言层）不同：五病管**怎么表达**，谬误管**推理本身是否成立**。五病可改稿修复，谬误常需重构论证。

---

## 六类顶刊高频逻辑谬误

### 1. Straw Man（稻草人）

**定义**：曲解、夸大或误述对立观点，然后攻击那个被曲解的版本，而非真实观点。常表现为"对一群人信仰什么做泛化，却不引用具体作者/作品"。

**FT50 触发场景**：Introduction 的 problematization——把 prior literature 描绘成"全都认为 X"，然后说"但我们发现 Y"，而实际上已有研究讨论过 Y。

**自检问题**：
- 我批判的"prior literature 的立场"是否有具体引用支撑？还是我在攻击一个无人真正持有的观点？
- 我是否把 nuance 的文献立场简化成了容易击败的极端版本？

**修正**：引用具体的 prior study + 准确转述其立场 + 承认其 nuance，再指出你的增量。

### 2. Either/Or Fallacy（伪二元 / 虚假二分）

**定义**：设置两个极端立场，强迫读者二选一，而现实中两者不互斥。

**FT50 触发场景**：Gap framing——"要么理论 A 对，要么理论 B 对"，而实际两者可在不同条件下都成立（这正是调节效应研究的价值所在，但 framing 不能假装只有两个极端）。

**自检问题**：
- 我的 gap 是否预设了两个互斥理论，而实际它们可能互补或在不同边界下各自成立？
- 我是否忽略了第三、第四种可能？

**修正**：用 boundary condition 框架替代伪二元——"理论 A 在 [条件 X] 下成立，理论 B 在 [条件 Y] 下成立，本研究识别这个边界"。

### 3. Post Hoc / Confusing Cause and Effect（后此谬误 / 因果倒置）

**定义**：因为 B 在 A 之后发生（或与 A 相关），就断言 A 导致 B，而未排除反向因果、共同原因或巧合。

**FT50 触发场景**：Theory→H 推导时，把相关当因果；或截面设计却做因果声明。

**自检问题**：
- 我的假设推导是否从"X 与 Y 相关"跳到了"X 导致 Y"而未论证机制？
- 我的识别策略是否真的支持因果语言，还是只能支持关联？（参见 `write-methods` causal-hedging 设计家族表）

**修正**：用 `causal-hedging.md` 校准因果语言强度；截面设计用 "associated with"；做因果声明须有识别策略 + 机制论证 + 反向因果处理。

### 4. False Analogy（错误类比）

**定义**：基于两个事物在某些方面的相似，推断它们在另一关键方面也相似，而该关键方面其实不相似。

**FT50 触发场景**：跨情境泛化——"在 [情境 A] 发现的机制，也应在 [情境 B] 成立"，而 A 与 B 在该机制的关键前提上不同。

**自检问题**：
- 我是否把一个情境的发现类比到另一个情境，而未论证两情境在机制关键前提上的相似性？
- Discussion 的 generalizability 声明是否 overclaim？

**修正**：论证类比成立的关键前提（两情境在哪些与机制相关的维度上相似）；用 `hedging-strength.md` 弱档表达跨情境外推；承认 boundary condition。

### 5. Hasty Generalization（仓促概括）

**定义**：基于过小或不具代表性的样本，对整体下结论。

**FT50 触发场景**：定性研究从小样本过度外推；或定量研究从单一情境/单一时段推广到普适理论。

**自检问题**：
- 我的样本（N 个案例 / 单一行业 / 单一时段）是否支持我所做的普遍性声明强度？
- 定性研究的 transferability 声明是否 overclaim？（参见 `write-results/定性过程研究.md` 变体 4 受众区分的有限成功评估）

**修正**：用 `hedging-strength.md` 匹配声明强度与样本代表性；定性研究讨论 transferability 而非 generalizability；用 three-horned dilemma 自我定位（见 `write-methods` Credibility 段）承认情境真实度 vs 可推广性的取舍。

### 6. Fallacy of the Middle Ground（中庸谬误）

**定义**：假设两个极端之间的中间立场必然正确，而无证据支撑。

**FT50 触发场景**：Discussion 的"折中贡献"——"既不是 A 也不是 B，而是两者都对"，却未论证为何中间立场理论上有依据。

**自检问题**：
- 我的贡献是否是"两边都对"型折中，而缺乏独立的机制论证？
- 中间立场是否有理论依据，还是仅为调和矛盾的妥协？

**修正**：中间立场必须有独立机制支撑（为什么中间条件产生中间效果？）；否则明确站一边并用证据论证。

---

## 与其他 QC 维度的关系

- **Pollock Ch04 五病**（`prose-pathology.md`）：语言表达层。五病管"怎么说"，谬误管"推理是否成立"。
- **`write-theory/reasoning_soundness_protocol.md`**：论证可靠性——审计 1 查推理形式（跳跃/堆砌），本清单查推理的逻辑谬误。互补：soundness 查链条完整性，fallacy 查链条中的逻辑错误类型。
- **`write-methods` causal-hedging**：post hoc 谬误的语言层防线——设计家族词汇表强制因果语言匹配设计强度。
- **`hedging-strength.md`**：false analogy / hasty generalization 的语言层防线——用弱档 hedge 表达外推。

---

## 执行方式（pollock-qc 集成）

在 pollock-qc 的全稿或 Theory/Introduction/Discussion 检查中，追加一个"逻辑谬误自检"子模块：
- 逐条对照 6 类，每类标 ✓（未触发）/ △（潜在风险，需作者复核）/ ✗（明显触发，需重构论证）。
- 触发的谬误归入"最需要修复的 3 个问题"，推荐路由：straw man/either-or → `write-introduction`（重做 gap framing）；post hoc → `write-theory`（补机制）+ `write-methods`（校准因果语言）；false analogy/hasty generalization → `discussion-review`（限制外推）；middle ground → `write-theory`（补独立机制）。

## 反模式

- **把谬误标签当武器攻击他人**——本清单用于**自检自己的稿件**，不是用来在 peer review 里给别人贴标签。
- **过度敏感**——不是所有简化都是 straw man，不是所有二选一都是 either/or。需判断是否真的曲解/虚假二分，而非合理的学术简化。
- **只检测不修正**——检测出谬误后必须重构论证，不能只标注了事。
