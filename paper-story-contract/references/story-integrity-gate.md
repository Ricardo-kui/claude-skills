# Story Integrity Gate

Apply this gate to the project's own research story before any section-writing skill may retrieve an exemplar. It tests defensibility; it does not select a story type or prescribe a plot.

## Evidence discipline

Use only supplied research materials, manuscript text, and confirmed project evidence. Mark an inference `provisional`; mark a claim with no stated basis `unsupported`. Do not use a prestigious journal, a familiar blueprint, or a desired result as evidence that a project story is valid.

## Four tests

| Test | Ask | Pass condition |
| --- | --- | --- |
| Theme grounding | Does the theme question name the actual theoretical object and empirical phenomenon? | It can be stated without promising an unobserved result. |
| Knot authenticity | Is the knot a real literature conflict, consequential anomaly, or specified mechanism incompleteness? | The supplied material identifies what is incompatible, surprising, or missing and why it matters. |
| Character discipline | Do main and supporting constructs each have one story function? | No construct is included solely to imitate a multi-actor or multi-path exemplar. |
| Payoff feasibility | Can the stated theory, design, and evidence answer the promised resolution? | The project can name what evidence would resolve each storyline and what remains untestable. |

## Outcome

- **PASS:** all four tests are `grounded`; full-section writing may proceed.
- **PROVISIONAL:** no test is `unsupported`, but one or more depend on clearly labelled assumptions; generate only a provisional contract and preserve the assumptions.
- **BLOCKED:** theme or knot is unsupported or contradictory, a character has no project role, or the promised payoff exceeds available theory/design/evidence. Stop before prose generation.

## Required output ledger

```yaml
integrity:
  theme_grounding: grounded | provisional | unsupported
  knot_authenticity: grounded | provisional | unsupported
  character_discipline: grounded | provisional | unsupported
  payoff_feasibility: grounded | provisional | unsupported
  unsupported_moves: []
  notes: ""
```

`unsupported_moves` must name story actions that must not enter the manuscript yet—for example, “claim a genuine theory conflict,” “promise a mediated mechanism,” or “preview a curvilinear resolution.” It must not name a blueprint, story family, or exemplar.

## Relation to exemplar learning

After PASS or PROVISIONAL, a section-writing skill may make a stateless v0.4 retrieval using only conditions established by this ledger and the current section request. Retrieval may clarify an already defensible move or warn against an unsupported one; it cannot change the ledger, create a contribution, or supply missing evidence.
