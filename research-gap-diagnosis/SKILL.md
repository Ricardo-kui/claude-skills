---
name: research-gap-diagnosis
description: "Diagnose a paper's contribution type, gap strength, and framing strategy via Zuckerman genre theory, Simsek knowledge-weaving, Makadok taxonomy, Greene-Lidinsky synthesis. Use when testing whether a gap is genuine or reframing a weak one."
when_to_use: "判断贡献类型、gap 是否成立、如何重构 gap、或从文献笔记生成候选 gap 时使用。"
whenToUse: "Use when diagnosing what kind of contribution a paper makes, whether its research gap is genuine and compelling, or how to reframe a weak gap before drafting. Trigger words: research gap, contribution type, 研究缺口, 贡献诊断, gap 太弱, contribution 不清晰, 论文定位, 诊断 gap, 研究空白"
---

# Research Gap Diagnosis

## Overview

Use this skill **before** any writing skill is invoked. Its job is to answer three questions that every paper must resolve before drafting begins:

1. **What kind of contribution is this?** — Genre diagnosis (Zuckerman 2017)
2. **Is the gap real and compelling?** — Gap-strength audit (Zuckerman 2008 + Simsek et al. 2022)
3. **Which theory lever does the contribution pull?** — Contribution-mechanism mapping (Makadok et al. 2018)

If these three questions are unanswered or answered weakly, no amount of prose polishing will save the paper. This skill does the structural diagnosis first and prescribes the framing fix second.

Typical triggers:

- `我不知道这篇论文属于什么类型的贡献`
- `我的gap是不是太弱了，只是"文献忽视了X"`
- `评审说 contribution 不 clear，帮我诊断`
- `我有数据/想法但不知道怎么 frame 成一篇论文`
- `帮我判断这个 puzzle 是否成立`

## Inputs

Collect the minimum workable set from these buckets:

- `research idea or draft`: a few sentences, an abstract, an outline, or a full introduction
- `target outlet`: journal name or at least field (management, strategy, organization theory, sociology)
- `literature context`: what is known, what is debated, what is assumed (can be informal notes)
- `evidence and design`: data, method, identification, main expected finding (can be tentative)
- `current framing`: how the author currently describes the contribution (if any)

If information is missing, make the minimum reasonable assumptions and label them explicitly. Do not invent puzzles, gaps, or literature states.

## Router

Resolve the route in this order: `diagnosis type -> depth -> output`.

### Diagnosis Type

- `genre mode`: identify which of the ten productive genres (or three pseudo-genres) the paper belongs to
- `gap-audit mode`: evaluate whether the stated or implied gap is genuine, compelling, and properly aligned with its knowledge-claim status
- `contribution-mechanism mode`: identify which theory lever(s) the paper pulls and whether that lever is appropriate for the outlet
- `incommensurability-resolution mode`: verify that a directional conflict is genuine, then locate its resolution on X, Y, opposing mechanisms, or context
- `full diagnosis mode`: run all three in sequence (default for first-time users)
- `generation mode`: gap not yet formed — run Part IV synthesis chain + counterfactual generator to generate candidate gaps, then audit them with Parts I–III

### Depth

- `quick scan`: label the genre and flag obvious problems (5-minute check)
- `standard diagnosis`: genre + gap audit + lever mapping with recommendations
- `deep diagnosis`: all of the above plus alternative framings, outlet-specific adjustments, and a reframe prescription

### Output

- `diagnostic label`: one-sentence genre call + pass/fail on gap strength
- `diagnostic report`: structured report with genre, gap status, lever map, and recommendations
- `reframe prescription`: same as diagnostic report plus 2-3 alternative framings with outlet-fit analysis

### Default Routing

- first-time user or unclear contribution type -> `full diagnosis mode` at `standard depth`
- "what genre is this?" or "what type of contribution?" -> `genre mode`
- "is my gap strong enough?" or reviewer says "gap is not compelling" -> `gap-audit mode`
- "what is my theoretical contribution?" or reviewer says "theoretical contribution unclear" -> `contribution-mechanism mode`
- reviewer says "contribution not clear" without further specification -> `full diagnosis mode` at `deep depth`
- prior findings or theories make incompatible directional claims -> add `incommensurability-resolution mode`; read `references/incommensurability-resolution-routes.md`

## Part I: Genre Diagnosis (Zuckerman 2017)

### Ten Productive Genres

| # | Genre | Core Logic | Introduction Structure |
|---|---|---|---|
| 1 | **Known puzzle** | Literature already acknowledges the puzzle; paper advances resolution | State puzzle -> review progress -> show what remains -> propose resolution |
| 2 | **Obscured puzzle** | Puzzle was hiding in plain sight; paper reveals and resolves it | Point to observable pattern -> show it contradicts received theory -> resolve |
| 3 | **Found puzzle** | Puzzle discovered in fieldwork or data; must generalize to gain traction | Frame puzzle in general terms -> use case/data to make it concrete -> generalize -> resolve |
| 4 | **No warrant** | Existing theory cannot actually explain what it claims; paper provides correct account | Show theory claims X -> demonstrate scope conditions are violated -> provide proper account |
| 5 | **Alternative hypothesis** | Competing explanation that fits evidence as well or better than the dominant one | Acknowledge dominant explanation -> introduce alternative -> show where alternative outperforms |
| 6 | **Missing evidence** | Evidentiary basis for accepted belief is thin; paper provides cleaner identification | State accepted belief -> show evidence is weak -> provide strong evidence -> clarify theory in passing |
| 7 | **Clarifying confusion** | Theoretical foundations are muddled; paper restates and stabilizes them | Map the confusion -> show where assumptions/logic are unclear -> restabilize -> show what follows |
| 8 | **Extending theoretical scope** | Established theory applies to a surprising new domain | Establish theory's success -> identify unexpected domain -> show theory explains it -> warn against overclaim |
| 9 | **Horse race** | Rival explanations adjudicated with distinctive data or design | Present rival explanations -> explain why current evidence is insufficient -> provide adjudicating evidence -> discuss conditional implications |
| 10 | **False debate** | Apparent disagreement dissolves once constructs are properly specified | Describe the debate -> show it rests on construct confusion -> dissolve -> integrate |

### Three Pseudo-Genres (Block These)

| Pseudo-genre | Why it fails | Diagnostic test |
|---|---|---|
| **"Literature has overlooked X"** | Only valid if the overlooked phenomenon challenges existing theory. Otherwise it is territorial planting, not a contribution. | Ask: "If I describe this pattern to a sophisticated user of the theory, would they be surprised or just say 'yes, we would expect that'?" If no surprise, reject. |
| **"Open the black box"** | Only valid if unpacking process generates new predictions, not merely adds complexity. Parsimony is a value; adding detail without explanatory gain is a cost. | Ask: "Does opening this box change any prediction, or does it merely add steps?" If no prediction changes, reject. |
| **"Literature-based puzzle"** | Only valid if the puzzle has a real-world referent. Puzzles internal to a theoretical paradigm that cannot occur in reality are not contributions. | Ask: "Can this puzzle arise in the real world, or does it only exist inside the literature's assumptions?" If only inside, reject. |

### Genre Diagnosis Procedure

1. Read the research idea or introduction.
2. Identify the opening move: does it state a puzzle, point to missing evidence, challenge an assumption, propose an alternative, or something else?
3. Match the opening move to one of the ten genres.
4. If the opening move is "X has been overlooked," "we need to understand the process," or "the literature has a debate," flag as pseudo-genre and require the author to articulate what real-world trouble this creates for existing theory.
5. If the genre is ambiguous between two candidates, name both and specify what evidence would distinguish them.
6. Label the genre at the top of all output.

### Outlet-Specific Genre Notes

- **ASQ / Organization Science**: favor genres 1-5 and 7 (puzzle and theory-driven). Genre 6 (missing evidence) often rejected unless paired with conceptual clarification. Genre 8 (extending scope) welcome but reviewers may allow overclaim.
- **AMJ / SMJ**: favor genres 1-6 and 9 (puzzle + evidence-driven). Genre 7 (clarifying confusion) difficult to publish. Genre 10 (false debate) possible if tied to empirical resolution.
- **AMR**: pure theory; genres 4, 5, 7, 8, 10 most viable.
- **Sociology journals (AJS, ASR, Social Forces)**: genre 6 (missing evidence) more accepted than in management journals. Genre 7 (clarifying confusion) also more accepted.

## Part II: Gap-Strength Audit (Zuckerman 2008 + Simsek et al. 2022)

### Zuckerman's Ten Writing Principles (Gap-Relevant Subset)

1. **Motivate the paper**: the introduction must make the reader want to keep reading.
2. **Know your audience**: different communities have different tastes for what counts as interesting.
3. **Use substantive motivations, not aesthetic ones**: do not argue that an approach is "better" because it aligns with a tribe's preferences.
4. **Always frame around the dependent variable**: start with the question/puzzle, not the answer/independent variable.
5. **Frame around a puzzle in the world, not a literature**: the only reason anyone cares about a literature is because it clarifies real-world puzzles.
6. **One hypothesis (or a few tightly related) is enough**: if people remember a paper, they remember it for one idea.
7. **Build up the null hypothesis to be as compelling as possible**: no interesting paper without a compelling alternative.
8. **Save the null**: the author's job is to help the reader shift from x to x', not to trash x.
9. **Orient the reader**: every sentence must fit the narrative arc.
10. **Never write literature reviews**: review literature only to show what is compelling but flawed about existing answers.

### Simsek et al.: Knowledge-Claim Developmental Status

For each knowledge claim the paper engages, assess its developmental status:

| Status | Definition | Gap strength |
|---|---|---|
| **Stable** | Large body of direct and indirect support; unlikely to be overturned short of paradigm shift | Low (refinement only) unless challenging the claim itself |
| **Fragile** | Resilient to limited probing, but significant boundary conditions remain unexplored | Medium-High (boundary specification) |
| **Unstable** | Held only tenuously; inconsistent findings; can be modified by emerging evidence | High (revision or replacement possible) |

Cross-reference with four types of knowledge claims:

| Claim type | Stable -> question | Fragile -> question | Unstable -> question |
|---|---|---|---|
| **Key assumptions** | Confirmed assumption: question boundary conditions | Qualified assumption: specify where it breaks | Unfounded assumption: what changes if we replace it? |
| **Stylized facts** | Robust fact: how far does it generalize? What mechanism underpins it? | Emerging fact: establish or revise boundary conditions | Incipient fact: establish new stylized fact or overturn |
| **Enduring critiques** | Resolved critique: less compelling basis | Partially addressed: build consensus | Blind spot: significant unresolved critique |
| **Substantive omissions** | Known known: already addressed | Known unknown: gap identified but unfilled | Unknown unknown: entirely overlooked territory |

### Gap-Strength Audit Procedure

1. Identify the primary knowledge claim(s) the paper engages.
2. Classify each claim by type (assumption / stylized fact / critique / omission).
3. Assess developmental status (stable / fragile / unstable).
4. Evaluate gap strength using the cross-reference table above.
5. Check alignment: does the research question match the developmental status of the claim it engages? Mismatch = weak gap.
6. Apply Zuckerman's principles as a checklist, especially:
   - Is the framing around a real-world puzzle (principle 5)?
   - Is there a compelling null hypothesis (principle 7)?
   - Does the paper try to save the null (principle 8)?
7. Rate gap strength: **Strong** / **Moderate** / **Weak** / **Pseudo-gap**.

### Gap-Strength Rating Criteria

| Rating | Criteria |
|---|---|
| **Strong** | Real-world puzzle + unstable or fragile claim + compelling null + saves existing theory |
| **Moderate** | Real-world puzzle + fragile claim but null is thin, OR stable claim but with genuine surprise |
| **Weak** | Literature-gap framing ("overlooked X") + stable claim + no compelling null |
| **Pseudo-gap** | No real-world referent + literature-internal puzzle + pseudo-genre detected |

## Part III: Contribution-Mechanism Mapping (Makadok et al. 2018)

### Eight Theory Levers

| Lever | Question | Contribution moves |
|---|---|---|
| **Research question** | What is asked? | Ask new question, modify existing question, apply theory to different question |
| **Mode of theorizing** | How? | Shift inductive/deductive, process/variance, static/dynamic, formal/informal, analytical/numerical |
| **Level of analysis** | Who? | Introduce new level, apply to different level, question validity of existing level |
| **Phenomenon** | Where? | Apply existing theory to new phenomenon, question application to existing phenomenon |
| **Causal mechanism** | Why? | Introduce new mechanism, question existing mechanism, articulate similarity/difference between mechanisms, synthesize mechanisms |
| **Constructs/variables** | What? | Introduce new construct, question existing construct, redefine/clarify construct, change construct's role |
| **Boundary conditions** | When? | Expose hidden assumptions, expose internal inconsistencies, identify inter-theory inconsistencies, relax or restrict assumptions |
| **Outputs** | So what? | Derive outputs from new theory, derive different output types, derive more specific outputs, derive outputs by combining theories |

### Contribution-Mechanism Mapping Procedure

1. Identify which lever(s) the paper primarily pulls.
2. Check that the lever matches the genre: e.g., genre 5 (alternative hypothesis) should pull the "causal mechanism" lever; genre 6 (missing evidence) should pull "boundary conditions" or "outputs"; genre 7 (clarifying confusion) should pull "constructs" or "boundary conditions."
3. Flag lever-genre mismatches: if the paper claims genre 1 (known puzzle) but only pulls "phenomenon" (applying to new context), it is actually genre 8 (extending scope), not genre 1.
4. Identify the primary lever (most papers pull one or two) and any secondary levers.
5. Check outlet fit: ASQ/OS expect primary lever to be causal mechanism, constructs, or boundary conditions. AMJ/SMJ accept research question + phenomenon + outputs more readily.

### Incommensurability resolution routing

When the gap rests on incompatible predictions or findings, read `references/incommensurability-resolution-routes.md` before recommending a genre, lever, or writing architecture. Run its two-stage authenticity gate: first establish a shared theoretical object or defensible higher-order family without demanding identical low-level Y indicators; then apply the route-specific formal lock (strict concrete X/Y/level/horizon/estimand for R3/R4). Identify one primary route (`R1 X-side differentiation`, `R2 Y-side disaggregation`, `R3 opposing mechanisms`, or `R4 contextual contingency`) and state an adjudicating prediction. Do not select a route mechanically from the contribution lever.

## Part IV: Counterfactual Gap Generation & Synthesis Chain (Greene & Lidinsky 2017)

Parts I–III 诊断**已有**的 gap；本部分是**生成性**工具——当用户只有模糊兴趣或一堆文献笔记、gap 尚未成形时使用（呼应 Boundaries 的 ideation-stage 条款）。来源：Greene & Lidinsky (2017) Ch05 (issues→questions) 与 Ch08 (synthesis)，管理学适配为本 skill 添加。

### 1. Synthesis 操作链：比较 → 追问差异 → 反事实

G&L 的核心认识论："a synthesis creates a context for your own argument"——文献综合不是文献报告，是为自己的论点搭建舞台。操作化为三步链：

1. **比较（Compare）**：并置两篇以上文献的论断，标出冲突型分歧（"X says this, but Y asserts just the opposite"）与解释型分歧（"X interprets this way, while Y sees it differently"）。
2. **追问差异原因（Why-they-differ）**："Comparing different points of view prompts you to ask why they differ."——不停留在"发现不一致"，追问不一致的**来源**：样本？情境？测度？理论前提？这一步的答案往往就是 boundary condition 或机制候选（对应 Makadok 的 causal-mechanism / boundary-condition 杠杆）。
3. **反事实生成器（What-if-neither）**："'Neither X nor Y has taken this into account. What if they had?'"——构造双方都未考虑的反事实。这是超越 gap-spotting 的最强启发式：gap 不是"没人做 C"，而是"A 派和 B 派共享一个未检验的盲区"。

**产出判定**：三步链跑完后，若 why-they-differ 的答案是理论性的（前提/机制差异）→ 走 genre 4/7/10；若是经验性的（样本/测度/设计差异）→ 走 genre 6/9；反事实揭示共享盲区 → 走 genre 2/5。

### 2. Either-Or 伪二元探针

G&L Ch04/Ch09 警告：学术文献中的分歧"rarely ... simplistic pro/con pairs"；把复杂议题压成 either/or 是 fallacy。诊断时的探针：

- 用户把文献描绘成"完全支持 A vs 完全支持 B"两个极端，再推出"综合/调和"贡献 → 检查中间立场是否真实不存在（resist binary thinking: "the real issue combines these arguments with a third or even a fourth"）。若第三立场存在但被忽略，该 gap 是**人造二元**，降级处理。
- 与 Part I 的 false debate（genre 10）互补：genre 10 是"辩论因构念混淆而虚假"，本探针是"对立因忽略中间立场而虚假"。

### 3. 问题形式纪律

- **Issue = 可争议的张力**（不是主题）："an issue is ... a fundamental tension between two or more conflicting points of view." 用户输入只有主题（"我想研究 X"）时，先逼出张力再谈 gap。
- **"To what extent" 句式**：把 yes/no 问题改写为程度问题（"To what extent can [A] coexist with [B]?"），避免是非题过早关闭探究空间——天然适配边界条件研究（under what conditions），但输出时必须进一步转化为可检验命题（接 `hypothesis-generation`）。
- **悬置判断**：生成阶段先承认对立观点的合理之处（suspending judgment），再寻找突破——与 Zuckerman 原则 8（save the null）同一纪律：强 gap 建设强对手，不建设稻草人。

### 4. Post-Generation Audit（强制闭环）

Part IV 生成的每个候选 gap **必须**回流审计，禁止直接输出给用户：

1. 过 Part I genre diagnosis：候选是否形似 pseudo-genre？特别注意 `what-if-neither` 生成的候选极易被表述成 "A 派和 B 派都忽略了 X"——这是 "Literature has overlooked X" 伪 genre 的变体，必须用 Zuckerman 的 surprise 测试（"sophisticated user of the theory 会惊讶吗？"）过滤；通不过时，按 Part I 的处方把"共享盲区"改写为对既有理论的 real-world trouble。
2. 过 Part II gap-strength audit：给出 Stable/Fragile/Unstable 评级与 Strong/Moderate/Weak/Pseudo-gap 判定。
3. 输出时每个候选必须带 `pseudo-genre alert: YES/NO` 标记——无标记的候选视为审计未执行。

## Full Diagnosis Output Template

```
## Research Gap Diagnosis

### Genre
- Primary genre: [name + number]
- Secondary genre (if mixed): [name + number]
- Pseudo-genre alert: [YES/NO; if YES, which one and why]

### Gap Strength
- Primary knowledge claim engaged: [description]
- Claim type: [assumption / stylized fact / critique / omission]
- Developmental status: [stable / fragile / unstable]
- Real-world puzzle: [YES/NO; one-sentence statement of the puzzle]
- Compelling null hypothesis: [YES/NO; what is the null?]
- Saves the null: [YES/NO; how?]
- Gap rating: [Strong / Moderate / Weak / Pseudo-gap]

### Contribution Mechanism
- Primary lever: [lever name + specific move]
- Secondary lever(s): [lever name + specific move, if any]
- Lever-genre alignment: [ALIGNED / MISALIGNED; explanation]

### Incommensurability Resolution (only when applicable)
- Authenticity gate: [PASS / FAIL / UNCERTAIN]
- Conversation-level comparability: [PASS / FAIL / UNCERTAIN; shared theoretical object or higher-order family]
- Member mapping: [how lower-order X/Y indicators belong to the shared object/family]
- Formal lock: [R3/R4 concrete X, Y, unit/level, horizon, estimand fixed? PASS / FAIL / PENDING]
- Conflict location: [X / Y / mechanism / context / measurement-or-design]
- Primary route: [R1 / R2 / R3 / R4]
- Secondary route: [R1 / R2 / R3 / R4 / none]
- Adjudicating prediction: [directly testable contrast]
- Misclassification risk: [closest alternative diagnosis]

### Outlet Fit
- Target outlet: [journal name]
- Genre-outlet fit: [GOOD / MODERATE / POOR; explanation]
- Lever-outlet fit: [GOOD / MODERATE / POOR; explanation]

### Recommendations
1. [Most important fix]
2. [Second priority]
3. [Third priority]

### Alternative Framings (deep diagnosis only)
- Framing A: [genre + lever combination + one-sentence logic]
- Framing B: [genre + lever combination + one-sentence logic]
- Recommended framing: [A or B] because [reason]
```

## Execution

### Quick Scan

1. Read the input.
2. Identify the opening move.
3. Label the genre (or flag pseudo-genre).
4. Rate gap strength in one sentence.
5. Output diagnostic label only.

### Standard Diagnosis

1. Run genre diagnosis (Part I).
2. Run gap-strength audit (Part II).
3. Run contribution-mechanism mapping (Part III).
4. If incompatible directional claims are present, run the Incommensurability authenticity gate and R1–R4 route diagnosis.
5. Fill in the full diagnosis output template.
6. Prioritize recommendations by impact.

### Deep Diagnosis

1. Complete standard diagnosis.
2. Generate 2-3 alternative framings by:
   - Trying different genres for the same core idea
   - Shifting the primary lever
   - Recalibrating the knowledge-claim status
3. Evaluate each alternative for outlet fit.
4. Recommend the strongest framing and explain why.
5. If the current framing is a pseudo-genre, prescribe the minimum reframe that converts it into a productive genre.

## Boundaries

- This skill diagnoses and prescribes framing; it does not write introduction prose. After diagnosis, hand off to `write-introduction` for prose work.
- Do not invent knowledge-claim statuses. If the literature context is insufficient, state what additional reading is needed.
- Do not override the author's substantive judgment. If the author insists on a framing that this skill rates as weak, document the risk but do not refuse to proceed.
- If the user's project is at the earliest ideation stage (no data, no literature review), focus on genre diagnosis and gap-strength heuristics rather than demanding full evidence.

## Reference Loading

This skill embeds its core frameworks directly. For an Incommensurability claim, load `references/incommensurability-resolution-routes.md`; otherwise no separate reference is needed for standard use. For deep diagnosis on a specific outlet, apply the outlet-specific heuristics inline (management-journal conventions, theory-tension emphasis, or empirical-contribution emphasis) based on the diagnosed genre and lever, rather than loading overlay files.
