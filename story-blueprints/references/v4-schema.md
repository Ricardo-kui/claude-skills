# Story Blueprints v0.4-lite Schema

## Purpose

v0.4-lite cards are learning objects for whole-paper storytelling. They separate a descriptive reading from an assessment and from section-specific learning advice. They do not prescribe a story for a user's project.

## Required metadata

| Field | Rule |
|---|---|
| `schema_version` | Must be `4.0-lite`. |
| `id` | Stable lowercase identifier. |
| `paper` | Record known publication facts; use `null` or `unverified` rather than guessing. |
| `reading_scope` | State which sections were actually read and whether coverage is complete or partial. |
| `analysis_focus` | Declare which sections received primary story analysis. The default is Introduction + Theory; Results + Discussion test payoff; Methods audits story–evidence alignment. Record a reason only when departing materially from this default. |
| `mechanism_evidence` | Optional calibration for newly read cards: record one status—`directly_tested`, `partly_probed`, `not_directly_tested`, or `not_assessable`—and one brief basis. It does not displace the theoretical mechanism from the story reading. |
| `section_learning` | Include all five section keys; use `suitable: no` when not assessed. |
| `story_assessment` | Start as `descriptive_only` until assessment is completed. |

## Required story reading

Every v0.4-lite card requires a theme question, whole-story synopsis, characters and storylines, and a five-act map. These are whole-paper interpretations. They need a declared reading scope, not a paragraph-level citation for every field.

`tension` is optional. Do not invent an antagonist. If the paper has no useful personified opponent, describe the central challenge or leave this section absent.

## Mechanism discipline

Read the middle mechanism first as a **theoretical story engine**: it gives the main characters motives, connects the opening tension to a prediction, and makes the Results consequential. Do not convert a story card into a causal-process audit or require every intermediate link to be measured before treating the theoretical account as the paper's narrative.

Then add only one empirical calibration where useful: `directly_tested`, `partly_probed`, `not_directly_tested`, or `not_assessable`, plus a short basis. This judgment limits what a writer may claim about evidence; it does not downgrade the mechanism's role in the theory story.

## Attention discipline

For ordinary empirical papers, story reading is front-end weighted: Introduction (about 40%) and Theory (about 25%) establish the theme, knot, characters, and plot promise. Results (about 15%) and Discussion (about 15%) establish whether the promise is fulfilled and meaningfully closed. Methods (about 5%) is read for design-to-story alignment, not re-distilled as technical instruction; the dedicated Methods and Results exemplar skills own that deeper work. These are default reading allocations, not a scoring rule or a claim that every paper has the same architecture.

## Required learning discipline

For any section marked `suitable: yes` or `partial`:

- provide at most two learnable structural moves;
- state at least one caveat or non-transferable dependency;
- ensure the relevant section was read;
- never present the move as a writing template.

Section learning may add `requires: []`, a short list of invocation-level conditions that must be explicitly validated before runtime retrieval can recommend that section. Use this only for a real transfer boundary, not as a taxonomy label.

## Assessment terms

Use `works`, `partly_works`, `does_not_work`, or `not_assessable`. The assessment applies to storytelling only. Do not infer that a paper has weak theory, invalid methods, or low journal value because a story element does not work.

## Classification

`theoretical_problem_form`, `narrative_dynamics`, and `retrieval_signals` are optional retrieval tags, not forced type assignments. `retrieval_signals` are soft similarities that can improve ranking; they must not be treated as a project diagnosis or a prerequisite for transfer. Existing v0.3 knot labels may be retained as notes during migration but must not determine a card's learning recommendation.
