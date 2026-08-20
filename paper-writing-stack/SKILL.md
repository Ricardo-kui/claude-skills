---
name: paper-writing-stack
description: "管理学顶刊论文写作全流程路由总控：判断当前写作阶段、真实瓶颈与修改顺序，按 Pollock story contract 把任务分派到 write-introduction/write-theory/write-methods/write-results/paper-review/pollock-qc 等专用 skill；不在本 skill 内起草正文。触发词：论文写作、写作瓶颈、下一步写哪节。"
whenToUse: "当用户在做管理学论文写作，不确定当前处于哪个写作阶段、瓶颈在哪、下一步该写或先改哪个 section，或需要跨章节对齐与任务路由时使用。触发词：论文写作流程、写作瓶颈、该先写哪部分、章节修改顺序、写作总控、写作路由、整篇论文怎么推进、先写 introduction 还是 theory"
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
- existing Discussion draft → `discussion-review`
- request to generate Discussion → explain that this stack intentionally has no standardized Discussion writing skill

## Gate Rules

- Full-section generation must pass `paper-story-contract`; local fragments may use its labelled local-only bypass.
- Do not polish a downstream section while its upstream promise remains structurally unstable.
- Keep outcome domain, main characters, storyline IDs, and evidence strength stable across sections.
- When evidence is mixed or unstable, narrow the front-end promise rather than upgrading the claim.
- Discussion review may test whether an existing draft delivers the evidence and promised reader shift, but it does not supply a template.

## Output

Return the selected skill, stage/gate status, one-sentence reason, and any dependency that must be repaired first. For multi-section work, return a short ordered sequence.

## Boundaries

- Do not draft the manuscript inside this router.
- Do not activate several section skills when one bottleneck dominates.
- Do not route theoretical implications, practical implications, limitations, or future research to a Discussion generator.
