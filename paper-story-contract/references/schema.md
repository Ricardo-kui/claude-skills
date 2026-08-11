# Canonical Story Contract Schema

The top-level key is always `story`. New outputs write only this schema.

```yaml
story:
  schema_version: 1
  status: provisional | confirmed
  stage: preparing | blocking | refining | finishing
  evidence_state: unstable | mixed | stable
  theme_question: "[research question]"
  central_knot: "[one-sentence tension]"
  stakes:
    theoretical: "[why the omission, error, or contradiction matters]"
    practical: "[optional]"
  characters:
    main:
      - name: "[construct]"
        role: focal_predictor | focal_outcome | core_process
        level: individual | team | firm | field | multilevel
    supporting:
      - name: "[construct or context]"
        role: mediator | moderator | context | boundary
        level: "[level]"
  storylines:
    - id: "S1"
      question: "[sub-question]"
      constructs: ["[names declared under characters]"]
      promised_resolution: "[what evidence would resolve it]"
  reader_shift:
    from: "[prior understanding]"
    to: "[target understanding]"
  integrity:  # 新输出必须经 project-owned integrity gate 填写；不包含范文或故事类型
    theme_grounding: grounded | provisional | unsupported
    knot_authenticity: grounded | provisional | unsupported
    character_discipline: grounded | provisional | unsupported
    payoff_feasibility: grounded | provisional | unsupported
    unsupported_moves: ["[尚不可辩护、不得写入正文的故事动作]"]
    notes: "[基于项目材料的简短判断；不写范文推荐]"
```

## Invariants

- `central_knot` is one concise tension, not a list of gaps.
- Main characters are limited to constructs or processes needed to answer the theme question.
- Every construct named by a storyline is declared as a main or supporting character.
- Storyline IDs are unique and stable across Theory, Methods, and Results.
- `provisional` means one or more values were inferred or remain unconfirmed.
- `confirmed` means the user or manuscript evidence supports all fields needed at the current stage.
- `integrity` records whether the project can defend its own story. It must contain no exemplar identifier, taxonomy label, or recommended rhetorical frame.

## Legacy Read Compatibility

When `story` is absent, read these legacy fields:

| Legacy field | Canonical target |
|---|---|
| `introduction.theory_hints.central_knot_statement` | `story.central_knot` |
| `introduction.theory_hints.core_constructs` | initial `story.characters` candidates |
| `introduction.theory_hints.narrative_arc` | evidence for stage diagnosis only |
| Introduction research question or preview | `story.theme_question` |
| `introduction.contribution_contract` | evidence for `story.reader_shift` and stakes |

Migration behavior:

1. Emit a migration warning.
2. Create a canonical `story` block with `status: provisional`.
3. Do not write legacy aliases into new output.
4. Preserve unrelated legacy fields so existing consumers do not lose data.
5. If a legacy `story.story_frame` exists, preserve it as historical metadata but do not use, update, validate, or propagate it. Do not migrate it into new output.

## Section Extensions

Sections own their operational mappings without duplicating the canonical story:

- `theory.hypotheses[*].storyline_id`
- `methods.story_alignment`
- `results.story_resolution`
