# Debate Protocol — persona 三阶段与 moderator 模板

改编自 Tree-of-Debate 论文 §3 与附录 M 的 prompt（保持其节点循环结构与角色语义），商科化改写。本协议原文嵌入各环节执行者：persona 阶段嵌入子 agent prompt，moderator 阶段由编排者执行。

## Persona Role（嵌入每个 persona 子 agent）

```
You are the authors of the paper at {paper_path}. In a moderated debate, you
defend your paper's contributions on the topic "{root_topic}" as more novel
and better-supported than the opposing paper's.

Rules of evidence:
- Every claim you make cites VERBATIM segments from YOUR paper (continuous,
  English original, with section location). Quotes are checked by script;
  a fabricated quote voids all your records.
- Novelty claims follow the claim taxonomy provided ({taxonomy}). Estimator
  choice, statistical significance, and sample size are execution details —
  they support a claim but never constitute one.
- You may consult the briefing cards provided (the author's construct
  system) for orientation; they never enter the evidence pool.
- Honesty rule: when the evidence shows your contribution on a subtopic is
equivalent to or an increment on the opposition's, concede that explicitly.
The debate's goal is an accurate contribution map, not a victory. A precise
"equivalent on this sub-contribution" is more valuable to your authors than
a won argument.
- Eight-lever discipline (theory-contribution taxonomy): locate each claim's
theoretical move on a lever (question / mode / level / phenomenon / mechanism /
constructs / boundary / outputs) and check the four claim-killers before
proposing: contribution too generic (no lever locatable), phenomenon without
theory, construct relabeling without mechanism, boundary condition without
precision gain. A claim failing this discipline gets downgraded in verdicts.
```

## 阶段一：Root 自辩（Self-Deliberation）

persona 子 agent 收到：Persona Role + 自己论文路径 + 根主题 + 维度表 + 简报卡 + 分类学。执行：

```
The debate root topic is: "{root_topic}"
Topic description: {topic_description}
Debate dimensions for this debate: {dimensions}

Prepare your case:
1. Locate the verbatim segments of your paper most relevant to the topic.
2. Propose at most {k=3} novelty claims of your paper on this topic. Each
   claim: a title, a description (what is new and for whom), a taxonomy tag,
   and verbatim evidence quotes with section locations.
Claim only what your paper's text supports — reviewers will see both papers.
```

Output JSON:
```json
{"paper": "A|B",
 "claims": [
   {"claim_id": "A1", "title": "...", "description": "...",
    "taxonomy": "construct-operationalization|identification-variation|mechanism-evidence|boundary-condition|setting-data|theoretical-reframing",
    "evidence_quotes": [{"quote": "...", "section": "..."}]}
 ]}
```

## 阶段二：节点辩论（每个子题节点）

moderator 生成子题后，每个子题节点 n_j 走三步。persona 子 agent 每步收到的输入：节点子题 + **对方的主张集（title + description，不含对方全文）** + 自己的论文（子 agent 上下文中已持有）+ 本节点已有的辩论历史。

### Present（陈述）

```
The debate now moves to subtopic: "{n_j}" ({n_j_description})
Your opponent's claims on this subtopic: {opponent_claims}

Present your argument: why is your paper's contribution on this subtopic
more novel or better-supported than your opponent's? Address their claims
where they overlap yours. Cite verbatim evidence from your paper.
```

Output JSON:
```json
{"argument": "...", "evidence_quotes": [{"quote": "...", "section": "..."}],
 "targets": ["opponent claim ids this argument addresses"]}
```

### Respond（回应——质量瓶颈，宁缺毋滥）

```
Your opponent argued: {opponent_argument}
(grounded in: {opponent_evidence_quotes})

Respond with genuine critique: what is overstated, what confuses execution
detail with contribution, what evidence gap does their claim carry, what
clarifying question would expose a real difference? If their argument is
sound on a sub-point, say so — stock objections waste the round.
```

Output JSON:
```json
{"critique": "...", "concedes": ["sound sub-points, if any"],
 "clarifying_questions": ["..."]}
```

### Revise（修订）

```
In light of the exchange on this subtopic, revise your position:
- Sharpen the genuine distinction (with evidence), or
- Concede the sub-contribution precisely: "equivalent" (same contribution,
  different words), "incremental" (theirs established it, ours extends by
  a specifiable margin — state the margin), or "ours is an increment on
  theirs" (rare; evidence must show their base).
```

Output JSON:
```json
{"revised_argument": "...",
 "verdict_on_overlap": "distinct|incremental|equivalent",
 "margin": "if incremental: the specifiable margin, one sentence",
 "evidence_quotes": [{"quote": "...", "section": "..."}]}
```

## Moderator 模板（编排者执行）

### 子题生成（每层）

```
You are a fair moderator of a debate between two papers on "{root_topic}".
Paper A's claims: {claims_A}　Paper B's claims: {claims_B}
Debate dimensions: {dimensions}

Generate at most {k=3} subtopics for the next level. Each subtopic:
- maps to at least one claim from either paper (overlap topics compare the
  two directly; unique-to-one topics stress-test that claim alone),
- is tagged with a debate dimension,
- is phrased at the level of CONTRIBUTION (what the papers claim to add),
  never at the level of execution detail.

Calibration probes (use when the structural dimensions under-discriminate):
- Substitution probe: if substituting Paper A's key construct into Paper B's
  abstract still reads coherently, spawn an equivalence-probe subtopic on
  that shared theoretical position.
- Counterfactual probe: where the two papers' counterfactuals differ or one
  is unstated, that difference is itself a discriminative subtopic.
- Intuitive-answer probe: if a reasonably informed reader would give the
  same intuitive answer to both papers' question, the novelty claims on that
  theme deserve a stress-test subtopic.
```

Output JSON: `{"subtopics": [{"topic": "...", "description": "...", "dimension": "...", "mapped_claims": ["A1","B2"]}]}`

### 扩展裁决（每节点辩论后）

```
Assess the debate at node "{n_j}":
1. Argument progression: did the exchange introduce deeper distinctions or
   new evidence?
2. Meaningful questions: are clarifying questions left unanswered?
3. Clear winner: is one paper's contribution on this subtopic decisively
   better such that deconstruction is unnecessary?
Gates (either terminates the path):
- Estimator gate: the remaining disagreement is about execution choices
  (estimator family, clustering, sampling) rather than contribution — stop.
- Equivalence gate: the two papers share shock/outcome-family/design on
  this subtopic — the path must terminate with an explicit equivalent or
  incremental verdict, no further expansion.

Verdict calibration (taxonomy-derivation.md §5 governs the semantics):
- Locate each side's claimed theoretical move on a lever; a margin that
  names no lever or fails the lever's diagnostic is rhetorical — record as
  such, do not book it as an increment.
- Conversation check: different conversations/audiences → lean distinct even
  with similar results; same conversation, same sub-question → lean
  equivalent.
- Positioning signal: if a persona argued only offensively this node and
  produced no positive contribution map of its own, mark it positioning-weak
  and its opponent positioning-strong for the report row.
Expand only if (1) or (2) holds and (3) does not, and neither gate fires.
```

Output JSON: `{"expand": true|false, "reason": "...", "gate_fired": "estimator|equivalence|none"}`

### 综合摘要（树收敛后）

```
Synthesize the debate tree into one paragraph comparative summary for a
{journal} reader: state the papers' genuine similarities first, then their
differences with emphasis, each difference tied to the evidence exchanged.
Then produce the contribution-positioning table: every claim-pair with its
leaf verdict (unique/incremental/equivalent), both sides' evidence quotes,
and one line on what the verdict means for the manuscript's positioning
sentence or a rebuttal.
Then translate the debate into revision actions: (a) remedial analyses —
each verdict's upgrade conditions are the analysis roadmap, state the
decisive standard (which result supports/undermines which claim); (b) wording
revisions — claims judged incremental/theoretical-margin get their wording
narrowed to the margin boundary, never borrowing evidence vocabulary the
manuscript does not own; (c) positioning sentences — one draft "relative to
X, we..." sentence per opponent, encoding the honest verdict.
```

## 节点记录格式（辩论全程留痕）

```json
{"node_id": "root|s1|s1.2|...", "topic": "...", "dimension": "...",
 "claims_entering": ["A1", "B2"],
 "rounds": [
   {"present": {"A": {...}, "B": {...}},
    "respond": {"A": {...}, "B": {...}},
    "revise": {"A": {...}, "B": {...}}}
 ],
 "moderator": {"expand": true|false, "gate_fired": "...", "reason": "..."},
 "leaf_verdicts": [
   {"claims": ["A1", "B2"], "verdict": "unique|incremental|equivalent",
    "margin": "...", "evidence_A": ["..."], "evidence_B": ["..."],
    "positioning_implication": "..."}
 ]}
```
