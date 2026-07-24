# Story-Fidelity Gate for Exemplar Distillation

Every Introduction, Theory, Methods, or Results exemplar must receive this classification before any adoption recommendation:

```yaml
story_fidelity:
  section_role: exposition | rising_action | empirical_arena | climax | falling_action
  knot_relation: tie | test | unravel | neutral
  character_effect: clarifies_main | supports | none
  pacing_effect: improves | neutral | harms
  classification: core_candidate | section_variant | ritual_only | reject
```

## Classification Rules

- `core_candidate`: recurrent across independent papers and changes a functional principle. Requires explicit human review.
- `section_variant`: a reusable way to perform an existing section function. May enter a reference corpus.
- `ritual_only`: a conventional form with no demonstrated story benefit. It may be documented but never made mandatory.
- `reject`: conflicts with the story contract, weakens pacing, invents evidence, or substitutes template presence for function.

## Adoption Boundary

Automatic writeback is allowed only for `section_variant` or `ritual_only` reference assets. It may not modify:

- a skill entrypoint;
- routing or invocation policy;
- mandatory slot order;
- the canonical story schema;
- stage gates.

`core_candidate` changes require an explicit human review record. A single paper can never change a core rule. `reject` patterns are not written into the reusable corpus.

## Section Interpretation

- Introduction: exposition that establishes and ties the knot.
- Theory: rising action that tightens causal or theoretical logic.
- Methods: empirical arena and credibility infrastructure; do not force literary devices.
- Results: the headline answer is the climax; robustness, heterogeneity, and supplemental analyses are falling action that test or unravel the answer.
