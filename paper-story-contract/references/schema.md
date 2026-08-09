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
  story_frame:   # 可选（Story Frame Selection 产物，非门禁字段）
    frame_type: "[knot 类型，见 ../story-blueprints/_schema.md 类型表]"
    resolution_type: "[resolution 类型]"
    one_liner: "[一句话故事——即 GBL 2007 的 theorized storyline：贯穿全文的理论主张线，不是摘要]"
    exemplar_blueprint: "[story-blueprints/blueprints/ 中的原型 id]"
    assumption_type: "[仅 frame_type=assumption-flip 时填写：in-house | root-metaphor | paradigm | ideology | field——见 ../diagnose-introduction/references/assumption-challenging.md]"
    alt_frames:
      - frame: "[被拒候选]"
        rejected_reason: "[理由]"
    risk_notes: "[前提风险核对结果]"
```

## Invariants

- `central_knot` is one concise tension, not a list of gaps.
- Main characters are limited to constructs or processes needed to answer the theme question.
- Every construct named by a storyline is declared as a main or supporting character.
- Storyline IDs are unique and stable across Theory, Methods, and Results.
- `provisional` means one or more values were inferred or remain unconfirmed.
- `confirmed` means the user or manuscript evidence supports all fields needed at the current stage.

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

## Section Extensions

Sections own their operational mappings without duplicating the canonical story:

- `theory.hypotheses[*].storyline_id`
- `methods.story_alignment`
- `results.story_resolution`
