---
type: micro-template
corpus_id: thesis-models-four
function: 论文中心论点的四种定位模型（thesis 句法权力分配）
source_tier: auxiliary
source: "Greene, S., & Lidinsky, A. (2017). From Inquiry to Academic Writing (4th ed.). Ch06 From Formulating to Developing a Thesis."
top_journal_validated: false
status: EMERGING
risk_level: needs-context
created: 2026-07-28
---
> 论证角色：**Claim**——中心论点定位模型；填位规则见 `_argument-grammar.md`（story-blueprints/v4/rhetoric-moves/）

# Thesis Models：中心论点的四种定位模型（G&L Ch06 收割）

> **层级定位**：auxiliary 定位框架层。`tensions/` 语料决定 **they say**（文献侧的缺口/张力怎么写）；本文件决定 **I say**——你的中心论点与既有观点的**关系类型**，以及该关系在 thesis 句中的**句法权力分配**。
>
> **使用规则**：
> 1. 先选定模型（四种选一），再写 thesis 句——模型选错会导致 contribution 声明与 tension 脱节（见各模型禁忌）。
> 2. 每个模型给出的是**关系骨架**；具体构念、机制、边界必须具体化，禁止只填骨架。
> 3. 陈述被纠正/被修正的他人观点时，受 `../../diagnose-introduction/references/golden-biddle-locke-four-moves.md` §Outer Limits 约束——不许稻草人化。

---

## 模型 1：纠错型（Correcting-Misinterpretations）

**关系**：他人的解读有误，本文纠正。

**句法权力分配（本模型的核心操作）**：把被纠正的观点放进 `Although` 引导的**从属分句**，把己方立场留在**主句**。G&L 原文："The clause beginning with 'Although' lays out the assumption ...; the structure of the sentence reinforces the author's position."——从属化不是礼貌，是句法上的权重分配：读者把从句读成背景共识，把主句读成前景主张。

```
Although many scholars have argued about [A and B], a careful examination suggests [C].
Although prior work often assumes that [assumption] ([citations]), we show that [C].
```

**管理学适配**：与 `tensions/02-implicit-assumption-wrong`（they-say 侧）和 `contributions/_index.md` 变体 J（challenge implicit premise）配套——tension 负责建立"假设存在且可疑"，本模型负责在 thesis 句完成反转。注意变体 J 的适用标签是 **Incompleteness 主导 + mild Inadequacy 混合** gap（且禁忌纯 Incompleteness）：纯 Inadequacy 的纠错用本模型直接驱动，混合 gap 才配变体 J 的贡献句。Although 标记词的权重梯度见 `../../write-theory/corpus/sentences/acknowledgment_response.md` §3.1。

**禁忌**：被纠正的解读必须真实存在且可引用（Outer Limits）；纠正幅度与证据强度匹配——横截面相关数据支撑不了 "X does not cause Y" 的全称纠正。

---

## 模型 2：补缺型（Filling-the-Gap）+ 表象—实质变体

**关系**：某主题尚未被（充分）研究，本文补足。

```
[Topic] remains largely unexplored: although [A] and [B] have been examined, [C] has received little systematic attention.
```

**表象—实质变体（gap × paradox 复合）**：G&L 指出 gap 模型的高张力变体——"although something might appear to be the case, a closer look reveals something different." 缺口不是"没人做过"，而是"表面共识 A 掩盖了实质 B"：

```
Although [phenomenon] might appear to be [surface reading A], a closer look reveals [B].
```

**管理学适配**：标准补缺对应 `tensions/01-despite-progress-unaddressed`；表象—实质变体对应 `hooks/22-twin-complication` 与 `tensions/04-reality-contradicts-consensus` 的 thesis 侧实现。变体的力量在于把 Incompleteness 和 Inadequacy 两种 gap 压缩进同一句。

**禁忌**：裸 gap（"few studies have examined X"）不配本模型——那是 research-gap-diagnosis 判定的 pseudo-genre，先回去过 gap-strength audit。

---

## 模型 3：修正型（Modifying-What-Others-Have-Said）

**关系**：同意前人的共同地基，在此基础上 extend / refine / limit。G&L："Although I agree with the A and B ideas of other writers, it is important to extend/refine/limit their ideas with C."

```
Although we build on [prior framework]'s insight that [A] and [B] ([citations]), 
we [extend / refine / limit] it by [C: new mechanism / new boundary / new scope].
```

**结构纪律**：共同地基先行（mutual understanding），修正边界随后且**边界必须显式**——extend（加机制/加情境）/ refine（换测度/换概念精度）/ limit（收缩适用范围）三者语义不同，不可混用为笼统的 "build on"。

**管理学适配**：这是顶刊 contribution 的主流站位（"extend" 是贡献声明最高频动词）。与模型 1 的选择判据：你否定的是对方的**解读**（模型 1）还是在对方**地基上加建**（模型 3）？误判的代价：该用模型 3 却用模型 1 会显得对抗性过强、制造假对立（见 `../../research-gap-diagnosis/SKILL.md` either-or 伪二元探针）。

**禁忌**："agree with A and B" 必须是真实同意而非战术性客气——后文若实质推翻 A/B，本模型退化为模型 1，句法错位会被审稿人读出。

---

## 模型 4：假设检验型（Hypothesis-Testing / 竞争性解释择优）

**关系**：多个合法解释并存，本文用证据裁决哪个最具解释力。G&L："you are not really proving that something is the case ... but you are helping readers understand what you see as the best case given the available evidence."

```
Some people explain [phenomenon] by suggesting [explanation A], but a close analysis 
reveals several compelling, but competing, explanations: [A] / [B] / [C]. 
We adjudicate among them by [distinctive data / design / test].
```

**管理学适配**：这是 thesis 层的定位声明，与理论层的竞争假设结构配套——Theory 内部的双路径对称推演见 `../../write-theory/corpus/variants/F_competing_hypotheses.md`；genre 诊断（alternative hypothesis / horse race）见 `../../research-gap-diagnosis/SKILL.md` Part I genres 5 与 9。本模型只负责在 Introduction 把论文**定位**为裁决者：卖点是裁决能力（distinctive data/design），不是又一个解释。

**禁忌**：竞争解释必须势均力敌（Zuckerman: build up the null）——一个明显较弱的对手不构成 horse race；裁决承诺必须在 Methods/Results 兑现（识别策略确实能区分 A/B/C），否则退回模型 3。

---

## 选择启发式

| 你的处境 | 模型 |
|---|---|
| 文献的解读/隐含假设是错的，你有反证 | 1 纠错 |
| 主题/情境/机制真没人做，或表面共识掩盖实质 | 2 补缺（或表象—实质变体） |
| 同意前人地基，加机制/边界/适用范围 | 3 修正 |
| 多个合法解释并存，你有裁决性数据或设计 | 4 假设检验 |

## 反模式速查

- **模型混装**：thesis 句同时出现 "correct" 和 "extend" 而无主次——一篇论文一个主定位，其余降为次级贡献。
- **从句主句颠倒**：己方立场进了 Although 从句、他人观点占了主句——句法权重反转，读者记住的是对方。
- **模型 4 空头裁决**：定位成裁决者但设计无法区分竞争解释（最常见于同一回归里放两个 IV 就宣称 adjudication）。
- **模型 2 裸 gap**：无 tension 的 "little research exists"——先过 research-gap-diagnosis 的 pseudo-genre 测试。
