# Golden-Biddle & Locke Four-Move Alignment

Use this reference to complement Pollock's story architecture with Golden-Biddle
and Locke's theorized-storyline test. Apply the compact four-move check to every
management-journal Introduction. Load the qualitative interpretation only for
qualitative/process studies or when the user explicitly requests it.

## Canonical Mapping

Do not create a parallel taxonomy. Reuse the existing diagnostic and story
fields:

| GBL move | Canonical evidence | Passing condition |
|---|---|---|
| 1. Articulate significance | `puzzle`, `story.stakes.theoretical`, `jtbd.gain_or_pain` | The study is contextualized in a consequential phenomenon or theoretical problem, not merely labeled important. |
| 2. Situate the study in literature | `conversation_strategy`, `jtbd.target_audience`, audience common ground | The selected literature is organized as Synthesized, Progressive, or Non-Coherence and establishes a specific disciplinary conversation. |
| 3. Problematize the literature | `gap_type`, `risk`, `jtbd.gain_or_pain` | The diagnosed limitation changes what the literature can explain and is supported without a straw-man construction (operational criteria: see §Outer Limits below). |
| 4. Foreshadow the response | `story.storylines[].promised_resolution`, `story.reader_shift`, Introduction preview and contribution contract | The proposed theory, question, design, or evidence directly occupies the research space created by Move 3. |

Use these exact taxonomy mappings:

| GBL term | Existing skill value |
|---|---|
| synthesized coherence | `Synthesized Coherence` |
| progressive coherence | `Progressive Coherence` |
| noncoherence | `Non-Coherence` |
| incomplete | `Incompleteness` |
| inadequate | `Inadequacy` |
| incommensurate | `Incommensurability` |

GBL found no one-to-one pairing between literature coherence and
problematization. Do not infer `gap_type` from `conversation_strategy`, or vice
versa. For the nine-combination design space and construction techniques, see
`intertextual-construction-playbook.md` (§2 matrix).

## Outer Limits: Straw-Man Criteria (operationalizing Move 3)

GBL's premise is that any literature has enough fluidity to be authentically
shaped in several directions — but the shaping has outer limits (Kilduff 1993
on March & Simon; Bazerman 1993 on Gould & Lewontin). A problematization
crosses the limit into straw-man construction when it fails any of:

1. **Representativeness**: the constructed field includes the works a
   knowledgeable reader would expect. Omitting canonical counter-evidence that
   would change a reviewer's assessment is over the limit.
2. **Attributability**: every position attacked is citable to specific works —
   never "the literature says" without names.
3. **Acknowledgment**: the cited authors would recognize their own work in
   your characterization. Multiple authentic readings are allowed; the reading
   must be one the text supports.
4. **Full-strength construction first**: for Inadequacy and Incommensurability,
   the literature must be constructed at full strength (Move 2 done well)
   before being subverted. Move 2 quality gates Move 3 legitimacy.
5. **Anticipated-objection test**: if a reviewer from the problematized camp
   would call the characterization a misreading, it is over the limit.

Legitimate selectivity (March & Simon omitting inconsistent works to intensify
their construction) passes tests 1–5 only when the omission does not change
the reader's assessment of the claim being attacked; use it to sharpen a
construction, never to manufacture one.

## Diagnostic Procedure

Assign each move one status:

- `pass`: the move is explicit, consequential, and aligned with the next move.
- `partial`: the move is inferable but generic, weakly evidenced, or poorly
  connected.
- `missing`: the move cannot be recovered from the supplied research
  description or draft.

Assign `overall` as:

- `aligned`: all four moves pass.
- `partial`: at least one move is partial and none is missing.
- `incomplete`: at least one move is missing. This describes Four-Move
  alignment only; it is not a story-stage or generation gate.

Output only one `repair_priority`: the earliest missing move; if none is
missing, choose the partial move whose repair most improves the Move 3 to Move 4
connection.

```yaml
diagnostic_schema_version: 2
gbl_four_moves:
  significance: "pass | partial | missing"
  literature_situation: "pass | partial | missing"
  problematization: "pass | partial | missing"
  response_foreshadow: "pass | partial | missing"
  overall: "aligned | partial | incomplete"
  repair_priority: "[one concrete repair]"
```

## Writing Use

Map the moves to paragraph functions rather than fixed paragraph numbers:

1. Significance is usually carried by Hook and Stakes.
2. Literature situation is carried by the Literature Turn.
3. Problematization is carried by Tension and its theoretical consequence.
4. Response foreshadowing is carried by Theory Lens, Research Question,
   Preview, and Contribution.

For qualitative/process studies, additionally check that the proposed
theoretical storyline connects field engagement to a disciplinary question.
Do not force field-story language onto quantitative papers.

## Boundaries

- Do not add GBL-specific fields to canonical `story` or `paper-state.yaml`.
- Do not add a new writing mode or a second Gap/Conversation taxonomy.
- Do not require one paragraph per move; moves may share a paragraph or sentence.
- Do not turn book examples into mandatory prose templates.
- Do not use Four-Move alignment to bypass evidence-state or story-stage gates.
- Treat a missing `diagnostic_schema_version` as legacy input. Consumers may
  derive Four-Move status from existing fields. Reject unknown versions greater
  than `2` rather than guessing their semantics.
