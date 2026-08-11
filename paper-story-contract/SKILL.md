---
name: paper-story-contract
description: Diagnose and maintain a Pollock-style whole-paper story contract before drafting Introduction, Theory, Methods, or Results. Use when defining the research question, central knot, characters, storylines, stakes, evidence state, or writing stage; auditing cross-section alignment; migrating legacy paper-state fields; or when another Pollock writing skill needs its story gate.
---

# Paper Story Contract

> **核心理念（Pollock 2025 Ch01）**：把自己当作 storyteller 而非 reporter——写出来的不是 research report，是故事。本 skill 维护的正是这个故事的状态：theme（研究问题）、central knot（张力）、characters（构念）、storylines（旅程）、reader shift（读者改变）。Ch02 的告诫同样适用：**plot 从角色与情境中长出，不要强加**——故事框架（story_frame）是供你选择的范本，不是套上去的模具。

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
5. **故事框架选择（Story Frame Selection，可选但推荐）**：若用户提供研究描述且未指定故事框架，加载 `references/story-frame-menu.md`，从 `../story-blueprints/` 语料生成 2-3 个候选框架卡（knot 类型 × 解法性格 × 原型 blueprint），由用户拍板；选定结果写入 `story.story_frame`，被拒候选记入 `story_frame.alt_frames`。若用户已指定框架，或旧字段足以推断（`introduction.theory_hints.narrative_arc` 等），跳过本步并说明推断依据。`story_frame` 是契约的一部分但**不是门禁字段**——缺失不阻塞 Story Intake。
6. Mark inferred values as assumptions. Use `status: provisional` until the user or manuscript evidence confirms them.
7. Apply `references/stage-gates.md`. Stop at Story Intake when a required field is missing or contradictory.
8. Return the canonical YAML block, validation result, unresolved assumptions, and the permissions granted to downstream writing skills.

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
- **故事框架选择菜单（Story Frame Menu）**: `references/story-frame-menu.md` — 研究描述 → 候选故事框架（knot × resolution × 原型 blueprint），消费 `../story-blueprints/` 语料（59 份 blueprint、9 型 knot 有实证样本、6 型 resolution、对照对家族；布局实证见 `../story-blueprints/layout-inventory.md`）
- Deterministic validation: `python scripts/validate_story_contract.py <paper-state.yaml>`
- Workflow contract tests: `python scripts/test_story_workflow.py`

## Boundaries

- Never invent findings, citations, constructs, measures, or identification claims.
- Keep one central knot. Treat additional questions as storylines only when they help resolve that knot.
- Do not use a template slot as evidence that a story function is present.
- Do not draft Discussion. Discussion is outside the standardized Pollock writing chain.
