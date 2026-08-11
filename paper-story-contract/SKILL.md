---
name: paper-story-contract
description: Diagnose and maintain a Pollock-style whole-paper story contract before drafting Introduction, Theory, Methods, or Results. Use when defining the research question, central knot, characters, storylines, stakes, evidence state, or writing stage; auditing cross-section alignment; migrating legacy paper-state fields; or when another Pollock writing skill needs its story gate.
---

# Paper Story Contract

> **核心理念（Pollock 2025 Ch01–02）**：把自己当作 storyteller 而非 reporter——写出来的不是 research report，是故事。本 skill 维护的正是项目自身的故事状态：theme（研究问题）、central knot（张力）、characters（构念）、storylines（旅程）、reader shift（读者改变）。plot 必须从研究问题、角色、情境与可获得证据中长出；不得由范文类型、故事框架或预设结局替代项目判断。

## Role

Maintain the paper's shared storytelling state. Diagnose the story before section drafting, expose unresolved assumptions, and give downstream skills one canonical contract. Do not draft manuscript sections.

## Invocation

```text
/paper-story-contract <paper-state path, manuscript path, or research description>
  [--mode=create|audit]
  [--stage=auto|preparing|blocking|refining|finishing]
```

Defaults:

- `--mode=create` when no canonical `story` block exists.
- `--mode=audit` when a `story` block exists.
- `--stage=auto` infers the stage from the evidence and manuscript state, then reports the inference.

## Workflow

1. Read only the supplied material and any explicitly linked `paper-state.yaml`.
2. If a canonical `story` block exists, validate it with `scripts/validate_story_contract.py`.
3. If it is absent, inspect legacy Introduction fields using the migration map in `references/schema.md`.
4. Identify the theme question, central knot, theoretical stakes, main and supporting characters, storylines, promised resolutions, reader shift, evidence state, and stage.
5. Apply `references/story-integrity-gate.md`. Test whether the theme, knot, characters, storylines, and promised payoff are grounded in the supplied research and evidence; name any story move that remains unsupported. Do not load `story-blueprints`, propose a story type, select an exemplar, or ask the user to choose a frame.
6. Mark inferred values as assumptions. Use `status: provisional` until the user or manuscript evidence confirms them.
7. Apply `references/stage-gates.md`. Stop at Story Intake when a required field is missing, contradictory, or fails the integrity gate.
8. Return the canonical YAML block, integrity ledger, validation result, unresolved assumptions, and the permissions granted to downstream writing skills.

## Universal Full-Section Gate

Full-section generation requires:

- `schema_version: 1`
- `status` and `stage`
- `evidence_state`
- a non-empty `theme_question`
- a one-sentence `central_knot`
- at least one main character
- at least one storyline with a promised resolution

Section-specific requirements:

- Introduction/front end: theoretical stakes and `reader_shift`.
- Theory: explicit character roles and each hypothesis mapped to a storyline.
- Methods: every storyline mapped to variables, model, or identification burden.
- Results: observed evidence available and every storyline assigned an answer status.

If the input is rich enough to infer the missing values safely, create a `provisional` contract and list the assumptions. Never silently promote it to `confirmed`.

## Local-Only Bypass

A request for one hook, one hypothesis, one Methods sentence, one coefficient interpretation, or another bounded fragment may proceed without the full gate. Prefix the output:

> Local-only output: not validated against the whole-paper story contract.

Do not update `paper-state.yaml` from a local-only request.

## Output Contract

```markdown
## Story Intake
- Mode:
- Inferred stage:
- Evidence state:
- Source material used:

## Story Contract
```yaml
story:
  ...
```

## Validation
- Gate: PASS / PROVISIONAL / BLOCKED
- Missing or contradictory fields:
- Assumptions requiring confirmation:
- Downstream permissions:
```

Return `BLOCKED` rather than generating a polished section when the theme question and central knot cannot both be stated, or when they contradict the available evidence.

## Resources

- Canonical schema and legacy migration: `references/schema.md`
- Project-owned story integrity gate: `references/story-integrity-gate.md`
- Stage semantics and section gates: `references/stage-gates.md`
- Distillation adoption gate: `references/distillation-gate.md`
- Deterministic validation: `python scripts/validate_story_contract.py <paper-state.yaml>`
- Workflow contract tests: `python scripts/test_story_workflow.py`

## Boundaries

- Never invent findings, citations, constructs, measures, or identification claims.
- Keep one central knot. Treat additional questions as storylines only when they help resolve that knot.
- Do not use a template slot as evidence that a story function is present.
- Never write `story_frame`, `resolution_type`, `exemplar_blueprint`, or a blueprint-derived type into canonical project state. Existing values are historical metadata and cannot route a new output.
- Do not retrieve, compare, or recommend exemplars in this skill. Section-writing skills may make a stateless v0.4 retrieval only after this gate has assessed the project-owned story.
- Do not draft Discussion. Discussion is outside the standardized Pollock writing chain.
