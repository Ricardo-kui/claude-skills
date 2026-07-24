---
name: paper-story-contract
description: Diagnose and maintain a Pollock-style whole-paper story contract before drafting Introduction, Theory, Methods, or Results. Use when defining the research question, central knot, characters, storylines, stakes, evidence state, or writing stage; auditing cross-section alignment; migrating legacy paper-state fields; or when another Pollock writing skill needs its story gate.
---

# Paper Story Contract

## Role

Maintain the paper's shared storytelling state. Diagnose the story before section drafting, expose unresolved assumptions, and give downstream skills one canonical contract. Do not draft manuscript sections.

## Invocation

```text
$paper-story-contract <paper-state path, manuscript path, or research description>
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
5. Mark inferred values as assumptions. Use `status: provisional` until the user or manuscript evidence confirms them.
6. Apply `references/stage-gates.md`. Stop at Story Intake when a required field is missing or contradictory.
7. Return the canonical YAML block, validation result, unresolved assumptions, and the permissions granted to downstream writing skills.

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
- Stage semantics and section gates: `references/stage-gates.md`
- Distillation adoption gate: `references/distillation-gate.md`
- Deterministic validation: `python scripts/validate_story_contract.py <paper-state.yaml>`
- Workflow contract tests: `python scripts/test_story_workflow.py`

## Boundaries

- Never invent findings, citations, constructs, measures, or identification claims.
- Keep one central knot. Treat additional questions as storylines only when they help resolve that knot.
- Do not use a template slot as evidence that a story function is present.
- Do not draft Discussion. Discussion is outside the standardized Pollock writing chain.
