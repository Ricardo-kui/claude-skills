---
name: paper-writing-stack
description: "Route paper-writing work across the Pollock-structured section-specialized writing stack for management-journal papers (ASQ/AMJ/OrgSci/SMJ). Use when Codex needs to decide which paper section to revise first, which writing skill should handle the current bottleneck, how to sequence front end, theory, methods, and discussion revisions, or how to keep cross-section promises aligned across a manuscript."
---

# Paper Writing Stack

## Overview

Use this skill as the meta-router for the Pollock-based paper-writing stack. It does not replace the section-specialized skills; it decides which one should handle the current bottleneck, in what order the manuscript should be revised, and whether the paper's front end, theory, evidence, and discussion are still promising the same paper.

Default Pollock stack (diagnose → write → review):

1. `diagnose-introduction` — Diagnose Gap type, Makadok dimension, Hook strategy
2. `write-introduction` — Execute Introduction template from diagnosis
3. `write-theory` — Theory & Hypotheses section templates
4. `write-methods` — Methods section templates (5 model types)
5. `write-results` — Results section templates (5 model types, 4-beat rhythm)
6. `write-discussion` — Discussion section templates (5 contribution types)
7. `paper-review` — Full-manuscript story architecture diagnosis + routing
8. `pollock-qc` — Pre-submission QC checklist (lightweight health check)

Section-level review skills (use after writing):
- `intro-review` / `intro-review --deep` — Introduction QC
- `theory-review` — Theory & Hypotheses QC
- `methods-review` — Methods QC (Completeness, Clarity, Credibility)
- `results-review` — Results QC (4-beat rhythm, robustness)
- `discussion-review` — Discussion QC (4 defects, positive standards, Findings/Contributions)

Exemplar distillation skills (use when processing new papers to generate Vault evidence assets):
- `distill-methods-exemplar` — Distill Methods sections into structured skeletons, expression DNA, and Vault reference notes. Outputs are human-reviewed before any skill adoption (Phase 0–5 pipeline)
- `distill-results-exemplar` — Distill Results sections into structured skeletons, rhythm maps, and Vault reference notes. Outputs are human-reviewed before any skill adoption (Phase 0–5 pipeline)

## Inputs

Collect the minimum workable set from these buckets:

- `paper identity`: topic, target journal or field, manuscript language
- `current stage`: outline, first draft, revision, R&R, pre-submission
- `current bottlenecks`: user complaints, reviewer comments, weak sections, missing sections
- `available artifacts`: title, abstract, introduction, theory, methods, results, discussion, conclusion
- `evidence state`: whether findings are stable, mixed, still changing, or not yet credible

If information is missing, make the minimum reasonable assumptions and label them. Do not pretend to route confidently if the paper's basic stage is genuinely unclear.

## Router

Resolve the route in this order: `scope -> bottleneck -> sequence`.

### Scope

- `single-section task`
- `multi-section revision`
- `whole-paper planning`
- `pre-submission alignment`

### Bottleneck

- `front-end weakness`
- `theory weakness`
- `methods/results weakness`
- `discussion/closure weakness`
- `cross-section inconsistency`

### Sequence

- `front-end first`
- `theory first`
- `evidence first`
- `discussion first`
- `submission preflight`

### Default Routing

- title, abstract, opening, gap, roadmap, front-end fit → `write-introduction`
- Gap/Makadok diagnosis before writing → `diagnose-introduction`
- construct clarity, mechanism logic, theory underdevelopment, weak hypotheses → `write-theory`
- sample, measures, model explanation → `write-methods`
- results narration, interactions, robustness → `write-results`
- theoretical implications, practical implications, limitations, future research, conclusion → `write-discussion`
- whole-paper structure diagnosis, weakest-section routing → `paper-review`
- pre-submission QC (quick health check) → `pollock-qc`
- Introduction QC, rewrite suggestions → `intro-review`
- Theory QC, why-chain audit → `theory-review`
- Methods QC, 3C audit → `methods-review`
- Results QC, rhythm audit → `results-review`
- Discussion QC, contribution alignment → `discussion-review`

## Core Rules

- Route by the real bottleneck, not by whichever section the user happens to mention first.
- Fix logic before polish. If theory or evidence is weak, do not spend the first cycle polishing prose elsewhere.
- Keep outcome domain stable across sections. Do not let one section promise event occurrence while another only studies timing, speed, or intensity.
- Keep contribution language synchronized across front end, theory, methods/results, and discussion.
- When evidence is still unstable, revise front-end claims downward rather than letting them drift upward.
- Prefer the minimum number of active skills needed to move the paper forward.
- When the user only needs one section, route directly and do not force a whole-paper workflow.
- If the user doesn't know their Gap type or Makadok dimension yet, route to `diagnose-introduction` before `write-introduction`.

## Outputs

- `single-section task`: return the exact skill to use next and one-sentence reason
- `multi-section revision`: return a prioritized revision order with one bottleneck per step
- `whole-paper planning`: return a section-by-section revision plan
- `pre-submission alignment`: return a findings-first diagnosis of which sections still promise different papers

## Execution

### Single-Section Routing

1. Identify the paper section actually under strain.
2. Identify the main failure mode in that section.
3. Route to the specialized Pollock skill that owns that failure mode.
4. State why that skill, not another one, should go first.

### Multi-Section Revision

1. Identify the highest-risk bottleneck.
2. Decide whether front end, theory, evidence, or discussion should move first.
3. Put later sections behind earlier dependencies.
4. Return a short ordered plan.

### Cross-Section Alignment

1. Compare the front-end promise with the theory claim.
2. Compare the theory claim with the evidence actually reported.
3. Compare the evidence with the discussion contribution.
4. Surface the first place where the paper stops being the same paper.

## Boundaries

- Do not directly rewrite the whole manuscript from inside this meta-skill.
- Do not keep multiple specialized skills active if one clear bottleneck dominates.
- Do not recommend polishing the discussion while theory or evidence is still structurally weak.
- Do not treat all section problems as prose problems; route to the section where the argument actually breaks.
