# Theory Governance Plan

When Phase 4 identifies a corpus action, emit a `governance_plan`; do not edit
`write-theory/corpus/` in place. Apply it through:

```powershell
python ../write-theory/scripts/theory_corpus_governance.py apply-plan plan.yaml --dry-run
```

Use this decision order:

```text
NONE → REUSE → EXTEND_SOURCE → ADD_REFERENCE → PROPOSE_VARIANT
```

- `NONE`: paper signature, domain filling, syntax, hypothesis count, or model form adds no transferable capability.
- `REUSE`: an existing asset already supplies the same capability.
- `EXTEND_SOURCE`: an existing asset is replicated by this paper; add a source only.
- `ADD_REFERENCE`: retain a useful single-paper example as a hidden `reference_exemplar`.
- `PROPOSE_VARIANT`: review-only. State what a nearest governed neighbor cannot generate; lacking a concrete answer, use one of the earlier actions.

`PROMOTE` requires VERIFIED/ROBUST status, one unique source identifier per claimed paper, a verification basis, and an explicit review. `MERGE` and `DEPRECATE` preserve aliases and provenance. Routing, story-schema, stage-gate, and cross-skill contract changes remain review-only.

```yaml
governance_plan:
  actions:
    - action: "EXTEND_SOURCE"
      target_asset_id: "theory:pattern:two_step_mechanism_chain"
      source_paper: "author_year_journal"
    - action: "ADD_REFERENCE"
      pattern_id: "time_ordered_two_step_operator"
      target_architecture_id: "theory:architecture:B"
      home_file: "subprotocols/hypothesis_derivation_patterns.md"
      slot: "T3"
      title: "Time-ordered two-step operator"
      source_paper: "author_year_journal"
      template: "[X] changes [state at t1], which changes [state at t2] and [Y]."
      nearest_neighbor_id: "theory:pattern:two_step_mechanism_chain"
      capability_loss_if_merged: "Preserves an explicitly time-ordered mechanism operator."
      capability_signature:
        operator: "time_ordered_transmission"
        prediction_topology: "main_effect"
        time_logic: "t1_to_t2_to_t3"
```

For every proposal, record the paper-level evidence separately from
`skill_design_feedback`; a corpus gap is not evidence that a core Theory rule is wrong.
