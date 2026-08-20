---
name: paper-writing-stack
description: "Route management-journal paper writing across the Pollock story contract and section skills — decide current writing stage, real bottleneck, revision order, cross-section alignment. Discussion generation excluded."
when_to_use: "不确定当前写作阶段/真正瓶颈/修改顺序时先来这里定路线。"
whenToUse: "Use when 用户要写管理学顶刊论文但不确定当前写作阶段、真实瓶颈、修订顺序或该调用哪个章节 skill，需要整栈路由编排。Trigger words: 论文写作流程, 该从哪开始写, 写作阶段, 修订顺序, paper writing stack, 写作路由"
---

# Paper Writing Stack

## Default Stack

1. `paper-story-contract` — define or audit question, knot, characters, storylines, evidence state, and stage
2. `diagnose-introduction` / `write-introduction` — diagnose and build the front end
3. `write-theory` — develop story-linked constructs, mechanisms, and hypotheses
4. `write-methods` — map promised resolutions to design, variables, models, and validity burdens
5. `write-results` — report the climax and evidence-constrained resolution
6. `paper-review` — diagnose whole-paper alignment and the weakest section
7. `pollock-qc` — run pre-submission health checks
8. `humanizer` — finishing-stage de-AI pass in academic mode, section by section with terminology locked

Section review skills remain available after a draft exists: `intro-review`, `theory-review`, `methods-review`, `results-review`, and `discussion-review`.

## Router

Resolve in this order:

1. `stage` — preparing, blocking, refining, or finishing
2. `story contract` — missing, provisional, confirmed, or contradictory
3. `scope` — local fragment, single section, multi-section, or whole paper
4. `bottleneck` — front end, theory, empirical design, evidence reporting, or cross-section alignment
5. `sequence` — put downstream work behind unresolved upstream dependencies

Default routes:

- missing or contradictory question/knot/storylines → `paper-story-contract`
- title, Abstract, Introduction promise, hook, gap, or contribution → `diagnose-introduction`, then `write-introduction`
- constructs, mechanisms, why-chain, or hypotheses → `write-theory`
- sample, measures, models, identification, or validity → `write-methods`
- evidence narration, interactions, nulls, magnitude, robustness, or headline answer → `write-results`
- whole-paper architecture or weakest-section diagnosis → `paper-review`
- pre-submission health check → `pollock-qc`
- AI tells, 模型腔, 去AI味, or pre-submission language polish at `finishing` → `humanizer` (academic mode; English manuscripts) / `humanizer-zh` (Chinese manuscripts)
- existing Discussion draft → `discussion-review`
- request to generate Discussion → explain that this stack intentionally has no standardized Discussion writing skill

## Gate Rules

- Full-section generation must pass `paper-story-contract`; local fragments may use its labelled local-only bypass.
- Do not polish a downstream section while its upstream promise remains structurally unstable.
- `humanizer` runs only at `finishing` with a confirmed story contract, after structural QC; it changes expression, never structure, evidence, or terminology. Locked tokens from paper-state.yaml (`theory.constructs`, `methods.variables`, hypothesis labels) are do-not-touch inputs to any humanize pass.
- After a heavy humanize pass, re-run alignment (`paper-review` or `pollock-qc prose`) before submission.
- Keep outcome domain, main characters, storyline IDs, and evidence strength stable across sections.
- When evidence is mixed or unstable, narrow the front-end promise rather than upgrading the claim.
- Discussion review may test whether an existing draft delivers the evidence and promised reader shift, but it does not supply a template.

## Output

Return the selected skill, stage/gate status, one-sentence reason, and any dependency that must be repaired first. For multi-section work, return a short ordered sequence.

## Boundaries

- Do not draft the manuscript inside this router.
- Do not activate several section skills when one bottleneck dominates.
- Do not route theoretical implications, practical implications, limitations, or future research to a Discussion generator.
