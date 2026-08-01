---
type: phrasebank
corpus_id: phrasebank-hedging-strength
function: 谨慎表达强度阶梯（hedging 强度分级选择库）
source_tier: auxiliary
source: "Morley, J. (2021). Academic Phrasebank (3rd ed.). University of Manchester. Ch.07 Being Cautious."
top_journal_validated: false
status: EMERGING
risk_level: needs-context
created: 2026-08-01
---

# Phrasebank: Hedging 强度阶梯（Morley 07 章收割）

> **层级定位**：auxiliary 语言实现层。顶刊蒸馏模板与 `write-*` slot 骨架决定**说什么**；本文件在 Discussion 段解释非显著结果、外推 generalizability、提出未来研究，或 Theory 段推导假设时，提供**按认识论强度分级的短语选择库**。
>
> **填补的空白**：现有 skills 有 `prose-craft-checklist.md` §5.6 Overclaiming（管确定性过高）和 §5.7 Defensive prose（管确定性过低）——但那是**改稿判别规则**。本文件是**写作时的强度选择梯子**，与判别规则互补：先按本文件选合适强度的短语，再用 §5.6/§5.7 校验是否过强/过弱。
>
> **使用规则**（每次调用必读）：
> 1. **调用顺序**：确定 claim 与证据 → 判断该用哪档强度 → 本文件取短语 → 语境化改写 → 用 §5.6/§5.7 + `causal-hedging.md` 校验。
> 2. 每个位置最多取 **2–3 个候选**；同一段落不连续堆叠两个以上 hedge（否则触发 §5.7 defensive prose）。
> 3. **必须替换占位符**并具体化（构念、机制、数据）。
> 4. **Specificity gate**：替换后的句子若可不加修改放进任何论文 → 不合格。
> 5. **因果上限**：涉及因果的 hedge 同时受 `write-methods/econometric-models/micro-templates/causal-hedging.md` 设计家族词汇表约束——强度档位不得突破设计允许的因果语言上限。
>
> **退役规则**：某强度档位一旦被顶刊蒸馏语料覆盖（经 distill-* 验证），对应条目从本文件删除。本文件不计入 MVP30 paper_count。

---

## 核心强度阶梯（epistemological strength）

Morley 的核心价值是把 hedge 按认识论强度（strength of knowledge）分级。 Discussion 段（尤其解释非显著、意外发现、外推时）每篇都用。选错档位 = 过度声明（被审）或不足声明（贡献被稀释）。

### 情态动词强度梯（5 档，由弱到强）

| 强度档 | 情态动词 | 适用场景 |
|--------|---------|---------|
| 极弱（推测） | **may / might / could** | 探索性解释、无直接证据的机制推测、意外发现的可能归因 |
| 弱（可能） | **is likely to / appears to** | 有间接证据但未确认；Theory 段假设推导的方向性但非确定性陈述 |
| 中（较可能） | **is probable / it is probable that** | 多源证据指向同一方向但缺直接检验 |
| 强（很可能） | **is almost certain to / it is almost certain that** | 强证据 + 稳健性检验一致，但保留统计不确定 |
| 确定（少用） | **is / does / shows**（无 hedge） | 仅限 Results 已证实的主效应直接报告；Discussion 外推禁用 |

**选档原则**：Discussion 解释机制 → 极弱/弱档；Theory 假设推导 → 弱档（方向性非确定性）；Results 主效应 → 无 hedge（直接报告）。**禁忌**：Discussion 用无 hedge 的确定句外推 = 越级（触发 §5.6）；Results 主效应用 may/might = 不当弱化（稀释贡献）。

### 认识论句式强度梯（"It..."结构）

| 强度 | 句式 | 适用 |
|------|------|------|
| 极弱 | It is possible that [X]... / It seems possible that... | 探索性解释 |
| 弱 | It is likely that [X]... | 间接证据推断 |
| 中 | It is probable that [X]... | 多源证据 |
| 强 | It is almost certain that [X]... | 强证据外推 |
| 名词短语型 | A likely/probable/possible explanation is that [X]... | 归因解释（Discussion 高频） |

---

## Discussion 段解释非显著/意外结果（高频场景）

这是 hedging 最关键的场景——审稿人最警惕"过度解释意外发现"和"强行抹平矛盾"。

### 归因解释（explaining results cautiously）

- This inconsistency may be due to [specific methodological/theoretical reason].
- It is possible that this result is due to [mechanism].
- This discrepancy could be attributed to [factor].
- A possible explanation for this might be that [mechanism].
- This rather contradictory result may be due to [boundary condition not theorized].

### 多解释并列（避免过早收敛到单一解释）

- There are several possible explanations for this result. First, [explanation A]. Alternatively, [explanation B].
- A possible explanation for these results may be the lack of adequate [measurement/temporal scope/context].

### 建议谨慎解读（advising cautious interpretation）

- These findings must be interpreted with caution because [limitation].
- We cannot exclude the possibility that [alternative explanation].
- It should be noted that [boundary condition limiting generalizability].
- Further research is needed to confirm whether [finding] holds in [different context].

---

## 与现有 hedging 判别规则的关系（重要）

本文件提供**短语选择**，不提供**判别标准**。判别见：
- **§5.6 Overclaiming**（`prose-craft-checklist.md`）：检测绝对化词（all/never/always/prove）——若你的 hedge 选了"确定"档但证据只支持"弱"档，§5.6 会标记。
- **§5.7 Defensive prose**：检测 hedge 堆叠（may possibly might / it could perhaps be）——若你连叠多个极弱档，§5.7 会标记防御姿态。
- **`causal-hedging.md`**：因果动词的设计家族上限——即使 Discussion 用弱档 hedge，因果动词仍受设计约束（OLS 不能用 "cause"，即使 hedged 为 "may cause"）。

**闭环**：选短语（本文件）→ 校验强度匹配（§5.6）→ 校验未过度堆叠（§5.7）→ 校验因果动词未越级（causal-hedging）。

---

## 反模式

- **Discussion 用无 hedge 确定句外推**（"This shows that X causes Y in all contexts"）——越级，触发 §5.6。
- **Results 主效应用 may/might**（"X may be negatively associated with Y, p<0.01"）——不当弱化已证实结果。
- **连叠 hedge**（"It might possibly perhaps suggest..."）——触发 §5.7 defensive prose。
- **所有解释都收敛到单一机制**——Discussion 应列多可能解释（本文件"多解释并列"），避免 cherry-pick 有利解释。
- **用 hedging 掩盖设计缺陷**——hedge 不能替代稳健性检验；若某威胁严重，应做检验而非用 "may be due to" 推给未来。
