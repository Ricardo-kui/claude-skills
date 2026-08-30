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

**[S] 前提 = Booth 意义上的 warrant**：连接 reason 与 claim 的一般性原则（"Warrants are general principles that connect reasons to claims." — Booth et al. 2024, Ch8）。其运作逻辑是"一般情境—一般后果"向下授权"具体情境—具体后果"：具体 reason 必须是一般情境的 good instance，具体 claim 必须是一般后果的 good instance。陈述 [S] 前提的**规范形式**：

> **"When X, then Y."**
> 例："When a nation's labor force shrinks, its economic future is grim." / "When an overwhelming majority of competent experts arrive at the same conclusion, we can probably trust it."

压缩形式（专家常用）："Shared DNA is the measure of the relationship between species."（= "When two species share more DNA, they are more closely related."）——检验压缩形式时先还原为 When-X-then-Y 再测。

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

**防守质量检验（warrant 五测试，Booth Ch8 §8.3）**：最弱前提（尤其 [S] 类）的防守句本身必须过五问——读者能对以下五问都说 "yes"，防守才算成立：

| # | 测试 | 判定要点 |
|---|------|---------|
| 1 | **Is that warrant reasonable?** | 一般后果能从一般情境推出（不是 "When children's mental health worsens, social media is to blame" 这种任意归因） |
| 2 | **Is it sufficiently limited?** | 足够限定，不过度绝对（含 all/always/never 的 warrant 默认答否） |
| 3 | **Is it superior to any competing warrants?** | 优于竞争性原则——与 §3 必要性门控 Q1 呼应：存在竞争性 warrant 时须说明为何本 warrant 更适切 |
| 4 | **Is it appropriate to this field?** | 管理学读者社群接受的推理原则；跨学科借用的 warrant 须先论证学科适切性 |
| 5 | **Is it able to cover the reason and claim?** | 一般情境/后果确实覆盖具体 reason/claim（reason 是 good instance，不是勉强套用） |

五问任何一问答否 → 回到上方处置规则 2（降级 claim / 转显式假设）；warrant 不被直接接受时，按 Booth 规则**把它当作一个 claim，配自己的 reasons + evidence 单独论证**。

---

## 3. 机制必要性门控（Necessity Gate）

在承诺一个新机制之前，必须过三问——这是 Ilicic & Brennan "M_new 推不出 D_reversed" 反模式的泛化，从事后检查上升为事前门控：

| 问 | 通过标准 | 不通过的处置 |
|---|---------|-------------|
| **Q1 替代充分性** | 主流/更简单的机制（field 默认 M_old）**不能**推出同一预测 | 若 M_old 已能推出同一预测 → 你的机制是装饰：删除，或降级为 Discussion 中的替代解释讨论 |
| **Q2 可区分性** | 你的机制能推出 M_old 推不出的**额外可检验预测**（方向、边界、时间轨迹、结果维度、非线性或行动者差异等） | 若两机制预测完全等价 → 从机制自身推导一种可区分后果；不得为过门控机械添加 moderation，否则删除或降级贡献 |
| **Q3 反事实塌陷** | 删掉你的机制后，故事**不**照样成立 | 若删掉后推导链仍完整 → 该机制从未承重，删除 |

**与 [`../sentences/mechanism_chain.md`](../sentences/mechanism_chain.md)「替代机制排除骨架」的关系**：那是提出中介**之后**的排他性句法（写作层）；本门控是承诺机制**之前**的取舍纪律（设计层）。先过门控，再用排除骨架书写。

**与 Outer Limits 的关系**：`golden-biddle-locke-four-moves.md` §Outer Limits 约束你**攻击文献**时不得稻草人；本门控约束你**建设自己**时不得装饰。两者是同一诚实纪律的两个方向。

---

## 4. 反例压力测试（Counterexample Stress Test）

对每个 Mechanism Move 问一个问题：**"什么条件下这一步不成立？"**

**系统性攻击面（Booth Ch8 §8.6 六类 warrant 及其挑战方式）**：测试时先问"这一步依赖哪类 warrant"，再用该类的挑战方式攻击：

| Warrant 类型 | 管理学示例 | 挑战方式（= 压力测试的攻击向量） |
|-------------|-----------|------------------------------|
| **Based on Experience** | "Where there's smoke, there's fire" 式经验概括；"收益率曲线倒挂则衰退将至" | 挑战经验的可靠性，或找到**无法被当作特例排除**的反例 |
| **Based on Authority** | "When authority X says Y, Y must be so"（经典理论家/权威综述） | 最温和：权威在该议题上证据不全或越界；最激进：其并非该议题权威 |
| **Based on Systems of Knowledge** | 理论体系内的定义/原则/理论（agent theory 的命题） | "事实"基本无效；须挑战整个体系，或证明**本案例不适用此 warrant** |
| **Cultural Warrants** | "What doesn't kill you makes you stronger" 式文化常识（如"逆境出领导力"） | 提供竞争性 warrant，或指出其文化特殊性（跨文化样本中不成立） |
| **Methodological Warrants** | Generalization / Analogy / Sign（"两类情境相似，故结论可迁移"） | 只挑战其**应用**或指出限定条件："Yes, we can analogize X to Y, but not if …" |
| **Based on Articles of Faith** | 被当作自明真理的断言 | 几乎无法直接挑战；若有人用它把 claim 置于争议之外，已脱离研究论证域——你的推导中**禁止出现**此类前提 |

**四种处置，按优先级**：

1. **补 scope condition**：答得上来的条件 → 写进推导（"when [condition], this step holds because…"）。这是 moderation 假设的天然生成器——压力测试答出的条件往往就是下一个 moderator
2. **生成新假设**：条件差异本身有理论趣味 → 升级为 E 调节效应型假设（调用 [`../variants/E_moderation.md`](../variants/E_moderation.md)）
3. **删除该步骤**：条件答不上来且步骤非必要 → 删除（链条越短，可攻击面越小）
4. **承认但不回应**（acknowledge without response，Booth Ch9 §9.4.2）：弱点无法修复时**诚实承认**——忽略它是 dishonest（读者发现后质疑你的 competence，认为你刻意隐藏则质疑你的 honesty）。三种回应姿态：
   - 其余论证足以补偿（"the rest of your argument more than compensates for the weakness"）
   - 弱点虽严重，更多研究将找到出路（"more research will show a way around it"）
   - 虽无法全盘接受 claim，但论证提供了重要洞见与未来答案的线索
   **位置规则**：可修复的异议就地处置（Theory 内，句式见 `../sentences/acknowledgment_response.md`）；不可修复的承认放 Discussion limitations（该处语料归 write-discussion，本协议不展开）。承认不是削弱论证，是可信度建设——experienced researchers 的目标是推进社群对话，不是终结对话。

**反模式**：
- 把压力测试答出的条件**藏起来不写**——审稿人会替你发现，且以 "theory is under-specified" 的形式
- 对每个步骤都补 scope condition → 推导变成条件清单，失去主线；只为**最弱前提所在的步骤**和**反直觉步骤**做测试即可
- 承认过多或过少（Goldilocks 问题，Booth Ch9 §9.4）：承认太多分散论证核心，承认太少显得 dismissive 或无知——只承认读者**真实可能想到**的异议

---

## 5. 表达纪律：Warrant 的明言与隐去（Booth Ch8 §8.4）

[S] 前提（warrant）默认隐去——本领域专家读者会 take them for granted。只有三个场合必须**明言**：

| 场合 | 规则 | 操作 |
|------|------|------|
| **① 跨领域读者** | 对不共享你专业背景的读者，解释本领域专家如何得出结论（尤其推理方式不寻常时） | 明言 warrant 并配一句学科惯例说明 |
| **② 推理原则在本领域新或有争议** | 依赖非常规推理原则时，预判 skepticism 并提前解除 | 明言 warrant + 引同领域**受尊敬学者**的用法背书；引不到就自己配次级论证 |
| **③ Claim 会被抗拒**（读者不希望它为真） | 先给一个读者**能接受**的 warrant，再摆他们可能抗拒的 reason + claim | "When an overwhelming majority of competent experts arrive at the same conclusion, we can probably trust it. **warrant** We should therefore accept that… **claim** because… **reason**"（Booth 气候变化例）。这是 `hypothesis_derivation_patterns.md` 中 Counterintuitive Anchor / Mechanism Substitution pattern 的泛化——机制替换前先立 warrant |

**隐去纪律（反向）**：明言本该显而易见的 warrant 是居高临下，暴露你不是真专家（"What you don't say says who you are" — Booth）。面向本领域专家时，§1 标注出的 [S] 前提若读者会视同常识，**不在正文写出**——Soundness Card 上标注"隐去"即可。

**硬证据规则（Booth Ch8 Quick Tip）**：**不能用 warrant + reason 单独支撑 claim of fact**（"In particular, you can't support a claim of fact with a warrant and reason alone."）。对应本协议：[E] 类前提的防守必须是**经验证据**，禁止用 [S] 类规定顶替——"X 是 Y 的主要原因"这类事实断言，写 "because [theoretical principle]" 不算防守，必须有数据/文献 finding。研究者对 hard evidence 的信任永远高于 elaborate warrant 推理。

---

## 6. 输出格式（Soundness Card）

每个假设推导段落完成 soundness 审计后，输出一张卡片（内部工作文档，不进正文）：

```
H[X] Soundness Card
├─ 前提清单: [D]×n / [S]×n / [E]×n
├─ 最弱前提: [引用该句] → 防守句: [已写(过五测试) / 已降级 claim / 已转显式假设]
├─ 必要性门控: Q1 ✓/✗ · Q2 ✓/✗ · Q3 ✓/✗ → 处置: [保留 / 补可区分预测 / 删除]
├─ 反例测试: 步骤 [k] 条件 "[condition]" → 处置: [scope / 新假设 / 删除 / 承认不回应]
└─ Warrant 表达: [隐去(读者视为常识) / 明言(场合①②③)] ；[E] 前提均有硬证据: ✓/✗
```

Phase 4 审计 4 复核所有卡片的处置列是否兑现。

---

## 7. 声音防火墙（诊断层 ≠ 文体层）

本协议是**诊断协议**，产出是改稿决策，不是句子。三条铁律防止协议污染正文声音：

1. **协议词汇永不进正文**：[D]/[S]/[E]、"门控"、"五测试"、"Soundness Card"、"最弱前提"是工作语言；正文里它们必须已经被转译成叙述句——前提防守写成机制句或证据句（句式从 `../sentences/` 语料取材），不是写成"本前提基于经验概括"这类自我标注。
2. **防守不得盖过主张**：每段的听觉中心必须是 claim 和机制推进；若一段内防守句多于推进句、claim 被 caveat 包围到找不到，说明防守过度——回到 §5 隐去纪律：领域专家读者默认隐去，明言只限三场合。审稿人要的是"论证有信心、边界有自觉"，不是"每步都先自我怀疑"。
3. **元评论式自辩是反模式**：连续的 "One might object that..., however..." / "Admittedly..., nevertheless..." 堆叠形成的是防御性技术说明文风而非顶刊论证文风——承认-回应句式有频次预算（见 `../sentences/acknowledgment_response.md` §6），零预算常常是正确答案：形式完美的推导段不需要任何承认句。Rogerian 段落（该文件 §5，最多 1 个、用于最核心的对话对象）独立于上述句子级 0–2 预算。

判断标准（读 aloud 测试）：把推导段朗读出来，如果听起来像**作者在回答想象中的审稿人**而不是**作者在向同行讲一个理论故事**，就是防火墙被击穿。

**与 §5.7 的分工**：本节管协议层泄漏；一般性防御措辞（负向自我设限 "This paper does not claim..."、hedge 堆叠、caveat 散射到高影响位置）的识别与转换句式库见 [`../../../write-introduction/corpus/storytelling/prose-craft-checklist.md`](../../../write-introduction/corpus/storytelling/prose-craft-checklist.md) §5.7——其"保留防守实质、删除防御姿态"原则与本节铁律 2 是同一校准。

---

## 8. 谬误探针（Fallacy Probes，G&L 2017 Ch09 管理学转译）

Phase 4 审计时的快速扫描清单。G&L 的 15 条 fallacy 中，大多数已被本协议或相邻层覆盖——本表只列**管理学语境下有独立诊断价值**的条目，并标注各自的处理位置，避免重复建设。

| 探针 | 管理学病征 | 探问 | 处理位置 |
|------|-----------|------|---------|
| **False analogy（错误类比）** | 从经济学/心理学/生物学借机制或隐喻，未检验组织情境适用性 | 类比的两侧在**机制相关维度**上真的相似吗？还是只有表面相似？ | 本协议 §4 Methodological Warrants 行（"Yes, we can analogize X to Y, but not if …"）——借用时必须在 Soundness Card 写出限定条件 |
| **Fallacy of division（分割谬误）** | 行业/公司层结论直接推广到团队/个人（或反向的合成谬误）——多层研究高频病 | 该前提成立的层次与 claim 的层次是否一致？跨层桥接句在哪里？ | 本协议 §1–2：[S] 前提层次桥接 = 次弱标记，需单独防守；方法侧由 methods-review 的多层对齐检查承接 |
| **Either-or（虚假二元）** | 把文献描绘成"完全 A vs 完全 B"两个极端，再推出"综合/调和"贡献，忽略第三立场 | 中间立场真的不存在吗？gap 是否是人造二元？ | **生成侧**（gap 设定）由 `../../../research-gap-diagnosis/SKILL.md` Part IV §2 探针处理；**理论侧**自查：若你的假设推导依赖"两派必有一错"，先确认第三解释不可能 |
| **Straw man（稻草人）** | 把前人简化成"完全忽视 X"以衬托"本文首次考虑 X" | 被批评的立场是否有具体作者/文本锚点，且按满强度重述？ | 已由 GBL Outer Limits（`golden-biddle-locke-four-moves.md`）与本协议 §3 处理，不重复 |
| **Sweeping generalization（过度概括）** | 单个显著结果被写成"改变了我们对 X 的理解" | claim 的范围词（all/always/proves）是否超出证据可支撑范围？ | 已由 Booth overclaiming blacklist（theory-review Step 3 相邻层）与 prose-craft-checklist §5.6 处理，不重复 |
| **Confusing cause and effect（因果混淆）** | 相关当因果——理论段把实证共变写成机制断言 | 该 [E] 前提的原始研究是否支持因果读法？ | 本协议 §1 [E] 前提边界检查 + 硬证据规则（§5） |

**使用规则**：本表是**扫描镜头**，不是第二套协议——命中后回到"处理位置"列指向的既有层执行处置，禁止在本表基础上生长平行流程。

---

## 与相邻文件的关系

- [`hypothesis_derivation_patterns.md`](hypothesis_derivation_patterns.md)：validity 层（形式有效的动作序列），本文件是其 soundness 镜像
- [`../sentences/mechanism_chain.md`](../sentences/mechanism_chain.md)：替代机制排除的**句法**（事后书写），本文件 §3 是门控（事前取舍）
- [`../sentences/acknowledgment_response.md`](../sentences/acknowledgment_response.md)：本协议 §4 处置 4（承认但不回应；三姿态句式见该文件 §2.3）与就地回应异议的**句式库**——四类异议 × 承认/回应标记词 × 位置安排
- [`evidence_patterns.md`](evidence_patterns.md)：Warrant 的证据类型与引用句式；本文件 §1 决定该前提**该不该用、用什么类型防守**
- [`../../../diagnose-introduction/references/golden-biddle-locke-four-moves.md`](../../../diagnose-introduction/references/golden-biddle-locke-four-moves.md) §Outer Limits：攻击文献的诚实纪律；本文件 §3–4 是建设自己的同一纪律
