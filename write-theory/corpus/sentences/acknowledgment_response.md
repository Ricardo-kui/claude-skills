<!--
corpus_id: acknowledgment_response
function: objection handling voice
type: sentence corpus
source: Booth et al. 2024 The Craft of Research Ch9 (Acknowledgments and Responses); §5 Rogerian 四步源自 Greene & Lidinsky 2017 Ch04
confidence: high (句式逐字源自 Booth；Rogerian 序列源自 G&L；管理实证适配为本库添加)
status: EMERGING
-->

# 承认与回应句语料库（Acknowledgment & Response）

> **功能**：为"主动处理读者异议"提供可复用句式——替代解释、反例、证据局限、定义分歧四类异议的承认句与回应句。
> **来源**：Booth et al. (2024) Ch9（§9.4 处置优先级 / §9.5 回应作为次级论证 / §9.6 词汇表 / Quick Tip 三种可预见异议），定量实证适配为本库添加。
> **与上游协议的关系**：何时承认、承认什么由 `../subprotocols/reasoning_soundness_protocol.md` §4（反例压力测试 + 处置 4 承认但不回应）决定；本文件负责**怎么写**。

---

## 1. 处置优先级（写之前先排序，Booth §9.4.1）

**优先回应**（必须写承认+回应）：
1. 可反驳的可信弱点（plausible charges of weaknesses that you can rebut）
2. 领域内重要的替代论证线索（alternative lines of argument important in your field）
3. 读者**希望为真**的替代结论（alternative conclusions that an audience *wants* to be true）
4. 读者已知的替代证据（alternative evidence that an audience knows）
5. 必须处理的重要反例（important counterexamples）

**承认但不回应**（诚实承认即可）：无法修复的弱点、无法回答的问题——回应姿态见 §3。

**与 soundness §4 的衔接**：本节排序决定**是否 engage** 一个异议；engage 之后的落地方式（补 scope condition / 升级为 moderation 假设 / 删除该步骤 / 承认但不回应）由 `../subprotocols/reasoning_soundness_protocol.md` §4 的四种处置决定。先排序，后处置。

**Goldilocks 纪律**：承认太多分散论证核心，承认太少显得 dismissive 或无知。只承认读者**真实可能想到**的异议。

---

## 2. 四类异议 × 承认/回应句式矩阵

### 2.1 替代解释 / 多因性（"There are causes in addition to the one you claim"）

**规则**：没有结果只有单一原因。聚焦某一原因时，承认其他原因存在并解释为何聚焦本因；读者可能认为某原因更重要时，承认并解释为何弱化它（Booth Quick Tip #1）。

```
[承认] Granted, [X] is not the only factor that can [affect Y]: [cause B] and [cause C] also play a role ([citations]).
[回应] We focus on [X] because [theoretical reason why X is the focal mechanism in this context].
```

```
[承认] It is easy to [think/imagine/argue] that [Y] results primarily from [alternative cause].
[回应] But there is another line of argument: [your mechanism], which [why it better accounts for the specific pattern].
```

**原文锚点** (Booth et al. 2024, The Craft of Research, Ch09 Quick Tip #1):
> "If your argument is about cause and effect, remember that no effect has a single cause and no cause has a single effect. If you argue that X causes Y, everyone will think of other causes. Honeybee colonies may be collapsing because of pesticide use, but someone knowledgeable about honeybees could also list other possible factors, including loss of habitat, disease, genetically modified crops, and parasites. So if you focus on one cause out of many, acknowledge the others."

### 2.2 反例（"What about these counterexamples?"）

**规则**：主动提出**生动且可信**的反例（尤其变异大的现象），承认后解释为何不视为致命（Booth Quick Tip #2）。警惕读者把正态分布内的异常个案当反例。

```
[承认] It might seem that [counterexample] undermines this logic: [why it appears damaging].
[回应] However, [counterexample] reflects [boundary condition / measurement artifact / within-normal-range variation], not a violation of [mechanism].
```

```
[承认] Admittedly, [case] does not fit our account.
[回应] But a single [case/observation] within the normal range of variation does not disconfirm a claim about [population-level relationship]; the mechanism we propose predicts [pattern], which is precisely what we observe in [test].
```

**原文锚点** (Booth et al. 2024, The Craft of Research, Ch09 Quick Tip #2):
> "No matter how rich your evidence, some skeptical members of your audience are likely to think of exceptions and counterexamples that they believe undermine your argument. So you must think of them first, acknowledge the more plausible ones, especially if they are vivid, and then explain why you don't consider them as damaging as those skeptics might." ... "People who do not understand statistical reasoning will focus on an aberrant case, even though it falls within a normal distribution: a cold Fourth of July in Miami does not disprove a claim about climate change, any more than a warm New Year's Day in Montreal proves it."

### 2.3 证据局限（acknowledge without response 的主场）

**规则**：无法修复的弱点诚实承认，用三种姿态之一回应（Booth §9.4.2）；**禁止**忽略（读者发现后质疑 competence，认为你隐藏则质疑 honesty）。

```
[补偿姿态] Although our [measure/sample] cannot [limitation], the convergence of [evidence A] and [evidence B] more than compensates for this weakness.
[未来研究姿态] While this limitation is serious, further research with [better data/design] will show a way around it.
[洞见姿态] While this weakness makes it impossible to accept our claim fully, our argument offers important insight into [question] and suggests what attributes a better answer would have.
```

**原文锚点** (Booth et al. 2024, The Craft of Research, Ch09 §9.4.2):
> "Candidly acknowledge the issue and respond that the rest of your argument more than compensates for the weakness. ... while the weakness is serious, more research will show a way around it. ... while the weakness makes it impossible to accept your claim fully, your argument offers important insight into the question and suggests what attributes a better answer would have." ... "It might seem that when jurors hear the facts of a case in a form that focuses on victims' suffering, they will be more likely to blame the accused. That is, after all, the standard practice of plaintiffs' lawyers and what we expected our research to affirm. But in fact, we found no correlation between . . ."

**失败转成功变体**（Booth §9.4.2）：把本想支持却未能支持的 claim 写成"看似合理但被证伪的假设"——
> "It might seem that [expected relationship]. That is, after all, [standard practice / what we expected to affirm]. But in fact, we found no correlation between ..."

（与 write-results 的 null 结果报告语料衔接；理论段用前三姿态为主。）

### 2.4 定义分歧（"I don't define X as you do"）

**规则**：论证依赖某术语含义时，定义它并配**次级论证**支持该定义；**禁令：勿以词典定义作权威**（"never begin, 'According to Webster's, ...'" — Booth Quick Tip #3）。技术含义与日常含义冲突时，承认日常含义并解释为何采用技术含义（或反之）。

```
[承认+定义] Although [construct] is often used loosely to mean [common meaning], we use it in the technical sense of [technical definition], because [subordinate argument: what this definition buys theoretically].
```

```
[次级论证] This definition is preferable to [alternative definition] for two reasons. First, [reason 1]. Second, [reason 2] ([citations]).
```

**原文锚点** (Booth et al. 2024, The Craft of Research, Ch09 §9.4.3 / Quick Tip #3):
> "When your argument hinges on the meaning of a term, define it to support your solution and offer a subordinate argument for your definition. Don't treat a dictionary definition as authoritative (never begin, 'According to Webster's, "addiction" means . . .')." ... "If you use a technical term that also has a common meaning (like social class or theory), acknowledge that common meaning and explain why you have adopted the technical one."

---

## 3. 标记词库（Booth §9.6，按给予异议的权重排序）

### 3.1 承认标记（从"最轻描淡写"到"最尊重"）

| 权重 | 标记 | 例 |
|------|------|-----|
| 弱化 | Despite / Regardless of / Notwithstanding / Although / While / Even though | "**Although** some smaller banks have failed, the sector as a whole remains strong." |
| 间接信号 | seem / appear / may / could / plausibly / arguably | "This proposal **may have** some merit, but we ..." |
| 匿名来源 | It is easy to [think/imagine/claim] that / Some evidence [might/may] suggest | "**It is easy to imagine** that X causes Y. But ..." |
| 泛化对话者 | There are [some/many] who [say/argue/object] / Some researchers argue | "**Some researchers argue** that ..., our analysis shows ..." |
| 自己声音（最尊重） | I/We understand that / It is true that / Granted / Admittedly / To be sure / Of course / It must be admitted that | "**Granted**, Adams has claimed ..., however ..." |

**Ethos 警告（Booth §9.6.1）**：禁止在承认句里贬损异议持有者（"the ill-conceived claim" / "some naive researchers"）——批评留给回应句，且对事不对人（"Save criticism for the response, and direct it at the work rather than the person."）。

### 3.2 回应标记（从委婉到直接）

| 力度 | 标记 | 例 |
|------|------|-----|
| 自谦式 | But I do not quite understand how / It is not clear to me how | "But **it is not clear to me how** X can claim that, when ..." |
| 指出未决问题 | But there are other issues here / But there remains the problem of | — |
| 无关/不可靠 | But it [ignores/is irrelevant to/does not bear on] the issue at hand / But the evidence is [unreliable/shaky/thin] | — |
| 文明指正（推荐默认） | but we must look at all the available evidence / but it is too complex for a single explanation / but not in all cases | "Smith's evidence is important, **but we must look at all the available evidence**." |

---

## 4. 回应的强度梯度（Booth §9.5：回应作为次级论证）

回应不能只是断言对立 claim——按需要三级递进：

1. **一句解释**（最小回应）："While some organizations recommend against [X], we are concerned specifically with [scope where objection does not apply]."
2. **追加让步 + 证据**："We recognize that [additional concession], but [Author] et al. ([year]) have shown that [counter-evidence]."
3. **完整次级论证**：异议足够重要时，为回应本身配 reason + evidence 的完整小论证。

**原文锚点** (Booth et al. 2024, The Craft of Research, Ch09 §9.5):
> "While some organizations, such as the US Preventive Services Task Force (USPSTF), recommend against routine PSA screening of men over 55, we are concerned specifically with the value of screenings for higher-risk populations such as men with a family history of prostate cancer." ... "We recognize that routine PSA screenings have resulted in overdiagnosis and overtreatment, subjecting many men to adverse side effects unnecessarily, but Tsai et al. (2021) have shown that coupled with effective counseling, the testing of at-risk populations reduces the incidence of . . ."

---

## 5. Rogerian 四步对话结构（高威胁异议的降防御序列，G&L 2017 Ch04）

§2 的矩阵管**句子级**承认-回应；当异议持有者是论文核心对话对象（被挑战的理论阵营、关键审稿人）时，单句承认不足以解除防御——用 Rogerian 序列组织**整个段落**。G&L："The objective of a Rogerian strategy is to reduce listeners' sense of threat so that they are open to alternatives."

| 步骤 | 功能 | 句式 |
|------|------|------|
| 1. 理解 | 向读者传达"你的不同观点被理解了"——准确重述对方立场，满强度（Outer Limits 同一纪律） | "[Theory X] offers a coherent account of [phenomenon]: [steelmanned version]." |
| 2. 承认成立条件 | 承认对方观点**在何种条件下**成立 | "To be sure, [view] holds when [conditions] ([citations])." |
| 3. 共同地基 | 帮助读者看到双方共享的问题或前提 | "We share with this literature the premise that [common ground]." |
| 4. 共创方案 | 在共同承认的问题上给出双方可接受的推进 | "Building on this shared premise, we propose [solution that preserves what was valid in step 2]." |

**范式例**（G&L 引 Radcliffe）：先让步 *"To be sure, 'deliberative democracy' is an ideal to which existing democratic systems only roughly approximate"*，再收回 *"Nevertheless, the concept provides a plausible standard for evaluating democracies."*——让步具体、收回有据。

**与 §2 矩阵的分工**：§2 处置读者**可能想到**的异议（防御侧）；Rogerian 处置论文**主动挑战**的阵营（建设侧）——它同时是 thesis 修正模型（[`../../../write-introduction/corpus/micro-templates/thesis-models.md`](../../../write-introduction/corpus/micro-templates/thesis-models.md) 模型 3）的段落级展开：共同地基 = 步骤 3，extend/refine/limit = 步骤 4。

**频次预算**：一篇 Theory section 最多 1 个 Rogerian 段落（用于最核心的对话对象）；其余异议走 §2 句子级矩阵。滥用会形成讨好型节律，触发 soundness protocol §7 防火墙。（注：此"最多1段"频次上限为 **skill 操作化建议**，G&L 原书只说 Rogerian 适用于 high-threat 异议、目标是降防御，未限定频次。）

---

## 5b. Audience-Foil Pivot（异质受众切换句；非完整异议处置）

<!--
pattern_id: audience_foil_pivot_sentence
function: foil→focal audience switch
source: chenganesanliu2009
source_papers: ["Chen_Ganesan_Liu_2009_JM"]
confidence: medium
status: VERIFIED
note: VERIFIED（expert_audit_override 2026-08-29 召回主题单源裁决，chenganesanliu2009 = 召回策略→财务价值）；配套架构见 ../subprotocols/argumentation_patterns.md → audience_foil_then_focal_signal_single_H
-->

**适用**: 文献默认受众 A 对行动 X 正向；论文 DV 由受众 B 定价。一句完成 **foil → focal** 受众切换，随后进入 B 侧信号机制——**不成对写出 Audience A/B 假设**（那是变体 G）。

**验证状态**: VERIFIED（召回主题单源裁决，chenganesanliu2009）

**模板**:
```
However, it is likely that [audience B] view the implications of [action] differently from [audience A].
```

**变体（同功能）**:
```
However, [audience B] may view the same [action] differently from [audience A]:
[they infer downside / severity / forced disclosure].
```

**原文锚点** (Chen, Ganesan & Liu 2009, JM):
> "However, it is likely that the stock market and investors view the implications of a proactive product-recall strategy differently from consumers."

**语料锚定**:
- Chen, Ganesan & Liu (2009, *JM*) — consumer-positive foil → investor focal pivot → single comparative H1

**与邻近语料的分工**:
| 本句 | §2 承认-回应矩阵 | 变体 G 辩证对立 |
|------|------------------|----------------|
| 切换评价者，**不**处理对自己论证的异议 | 处置读者对**本论证**的异议 | 成对受众机制 + 成对 H |
| 后接 focal 信号链 → 单 H | 后接回应/让步姿态 | 后接 Audience B 独立假设族 |

**反模式**:
- 写完切换句后仍为受众 A 另立假设（升格为 G）
- 用本句替代 focal 机制 warrant（However  alone 不够）
- 每段都做受众切换（频次：通常 0–1；仅反直觉单 DV 比较主效应需要）

---

## 6. 定量实证适配与分工

- **与 `mechanism_chain.md`「替代机制排除骨架」的分工**：排除骨架用于**中介提出之后**的系统性排他（Results/Discussion 方向）；本文件用于**假设推导段内**的即时异议处置（Theory 内）与"承认但不回应"的诚实出口。
- **与 GBL Outer Limits 的分工**：Outer Limits 约束你**构造文献稻草人**时满强度；本文件约束你**处置针对自己的异议**时同样满强度（§2.2 反例必须"生动且可信"，不许挑软柿子）。
- **反模式**：
  - 稻草人式承认：承认没人真实持有的异议，只为表演全面
  - 承认后无回应且无理由（属于处置失当，除非走 §2.3 承认不回应路径）
  - 词典定义当论证（§2.4 禁令）
  - 承认句贬损异议者（ethos 损伤，§3.1 警告）
  - **套路化承认**：每段一个 Granted/Admittedly 形成防御性节律——本语料有**频次预算**：仅用于 soundness protocol §4 锁定的最弱前提步骤与反直觉步骤，一篇 Theory section 通常 0–2 处；零使用是合法且常见的正确答案（形式完美的推导段不需要承认句）。防御性技术说明文风的完整防火墙见 `../subprotocols/reasoning_soundness_protocol.md` §7


### 变体 A：对立观点→权变调和式调节开场（contingency reconciliation opener）

<!--
pattern_id: contingency_reconciliation_opener
build_type: 跨类型（调节/假设树开场句式）
source_papers: ["anand_mukherjee_2024_org_science"]
confidence: medium（单篇，产品召回主题 expert_audit_override 2026-08-29 升 VERIFIED）
-->

**适用场景**: 文献对"经验是否产生学习/绩效"存在正反两派时，把僵局转化为调节假设的论证许可证——调和句先于任何 moderator 引入即命名"条件"这一调节类属。
**句位**: 假设发展开篇（T3 机制推演之前的立场铺垫段）。

**骨架**:
```
One perspective applying [theory] to [phenomenon] is that [experience] experiences
are more effective at generating [outcome] because they activate [attention
mechanism] and result in more focused [search] ([citations]).
The opposite view is that [actors] do not [learn] because their reactions are
[myopic objection], [uncertainty/complexity objection], and [non-persistence
objection] ([citations]).
The contingency view of [phenomenon] reconciles these opposing views by focusing
on conditions under which [experience] may or may not lead to [outcome].
```

**为什么有效**: 正反两派各有 citation 支撑后被"conditions under which"一句收编——后续每个调节假设都自动成为对该僵局的回答，moderator 不再是控制项而是裁决项。
**注意事项**: 调和句必须真正命名条件维度，且后续 moderator 需逐一兑现"条件"承诺；只摆两派不调和则是空洞平衡。
**反模式**: 用此句式包装实则单边论证（只驳反方不吸收其洞察）。

**原文锚点**: "The opposite view is that firms do not learn from failure experiences because their reactions are myopic in only focusing on the recent failure, there is too much uncertainty and complexity to be able to pinpoint underlying causes"（§3.1 首段）

<!-- wb:anand_mukherjee_2024_learning_from_failures_di:contingency_reconciliation_opener -->
