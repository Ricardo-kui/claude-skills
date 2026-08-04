# Incommensurability resolution routes

Load this reference when prior studies make incompatible directional claims, when an introduction is framed as Incommensurability, or when the author wants to reconcile mixed findings. Diagnose the source of conflict before selecting a writing architecture.

Treat R1–R4 as a working, defeasible taxonomy: it should organize current cases without forcing every apparent conflict into four boxes. Record full-text counterexamples or recurring hybrid routes for later skill-design review.

## Two-stage authenticity and comparability gate

Do not use one low-level sameness test for every route. Separate conversation-level authenticity from formal hypothesis-level locking.

### Stage A — conversation-level comparability

Treat a conflict as genuine only after all four checks pass:

1. **Shared theoretical object or family**: the studies address the same theoretical question, a shared umbrella construct, or members of a defensible higher-order X/Y family. They need not use an identical concrete Y indicator, level, or horizon at this stage. The author must map each lower-order construct or outcome into the shared object and explain why the claims are commensurable there.
2. **Directional conflict**: after that mapping, the theories or estimates imply incompatible directions or states. An effect-versus-null conflict qualifies only when the null is deductively predicted and the conditional difference is tested directly; “significant” versus “not significant” by itself does not qualify.
3. **Theoretical consequence**: resolving the conflict changes an explanation, prediction, or boundary—not merely the coding of variables.
4. **Real-world referent**: the disagreement matters for an observable decision, outcome, or phenomenon.

Stage A fails when the studies merely share a topic label, when no coherent higher-order family links their constructs, or when the difference is only measurement, sample, or design quality. Different proxies alone do not create different constructs. Route such cases to missing evidence or a horse race rather than manufacturing Incommensurability.

Bundled X or aggregated Y is not a comparability failure when the paper can define the umbrella object and its members ex ante; it is the substantive problem that R1 or R2 resolves.

### Stage B — route-specific formal lock

- **R1/R2**: do not require identical lower-order X or Y, because differentiating those members is the resolution. Require an explicit umbrella construct/family, ex ante member definitions, and a stable comparison frame. R1 varies X members while holding the outcome frame stable; R2 varies Y members while holding the predictor frame stable.
- **R3/R4**: before formal hypothesis derivation, lock the concrete X, concrete Y, unit/level of analysis, time horizon, and estimand. R3 changes mechanism dominance; R4 changes W states. Neither route may manufacture conflict by switching X, Y, level, or horizon across rival predictions.

Thus, “same X and Y” is a formal derivation requirement for R3/R4, not a universal entry condition for the Incommensurability conversation.

## Four-route matrix

| ID | Resolution route | Hidden source of conflict | Required theoretical move | Typical contribution levers |
|---|---|---|---|---|
| **R1** | **X-side differentiation** | Prior work treats theoretically distinct types, dimensions, or facets of X as one predictor | Define the X categories ex ante and show why each activates a different mechanism or prediction for the same Y | Constructs + Mechanism |
| **R2** | **Y-side disaggregation** | Prior work treats distinct outcomes, audiences, functions, time horizons, or levels as one Y | Define a coherent Y family, separate its members, and derive why the same X affects them differently | Outputs + Constructs + Mechanism |
| **R3** | **Opposing mechanisms** | The same X activates countervailing processes toward the same Y | Specify both mechanisms symmetrically and explain when their relative strength changes or which evidence adjudicates them | Causal mechanism + Mode |
| **R4** | **Contextual contingency** | The X→Y direction depends on W because W changes exposure, capacity, interpretation, or mechanism dominance | Specify W theoretically and derive conditional directions, not merely an interaction term | Boundary conditions + Mechanism |

## Decision sequence

1. Ask **where the hidden aggregation sits**.
   - Different meanings or types of X were pooled → R1.
   - Different meanings or types of Y were pooled → R2.
   - The formal X/Y/level/horizon can be fixed and two causal pathways oppose one another → R3.
   - The formal X/Y/level/horizon can be fixed and a theoretically prior condition changes the direction → R4.
2. Select one **primary route**. Add at most one secondary route when it performs a distinct task, such as R3 explaining why the R4 moderator changes the sign.
3. Write an **adjudicating prediction** that could distinguish the resolution from the strongest prior account.
4. Map the route to the contribution lever only after locating the conflict. Do not infer the route mechanically from a Makadok label.

## Route-specific burden and failure tests

### R1: X-side differentiation

- Require a conceptual basis for the categories before examining results.
- Show that the categories are not merely alternative proxies or a post-hoc median split.
- Derive type-specific predictions; “X is multidimensional” without changed predictions is construct description, not conflict resolution.

### R2: Y-side disaggregation

- Require outcomes to be distinct members of a defensible higher-order family.
- Explain why aggregation masks offsetting effects or collapses theoretically different functions.
- Reject opportunistic multiple-DV stories that select outcomes after seeing coefficients.

### R3: opposing mechanisms

- Give each mechanism a distinct action chain and a plausible domain of dominance.
- Do **not** infer U- or inverted-U shape merely because two mechanisms have opposite signs. Countervailing mechanisms may instead yield a null average, threshold, sign reversal, or context dependence.
- Predict an inverted U only when the positive mechanism dominates at low-to-moderate X and the negative mechanism grows dominant at higher X. Predict a U only for the reverse dominance schedule. State the turning-point logic and test it directly.

### R4: contextual contingency

- Require W to explain why one prior claim holds under one condition and the rival claim under another.
- If W changes only magnitude while the sign is stable, or if no genuine directional conflict exists, classify the project primarily as Inadequacy × Boundary rather than Incommensurability.
- Permit effect-versus-null only when the null is a substantive rival prediction, not an inference from one nonsignificant subgroup coefficient.
- Reject arbitrary moderators added after mixed results or arguments based on significant/non-significant subgroup comparisons without a direct interaction test.

## Output fields

For a diagnosed Incommensurability gap, add:

```yaml
incommensurability_resolution:
  authenticity_gate: "pass / fail / uncertain"
  comparability:
    conversation_level: "pass / fail / uncertain"
    shared_object_or_family: "[umbrella construct, higher-order outcome family, or shared theoretical question]"
    member_mapping: "[how lower-order X/Y measures map into that object or family]"
    formal_lock:
      required_for_route: "yes for R3/R4 / route-specific frame for R1/R2"
      status: "pass / fail / pending"
      concrete_frame: "[X, Y, unit/level, time horizon, estimand]"
  conflict_location: "X / Y / mechanism / context / measurement-or-design"
  primary_route: "R1 / R2 / R3 / R4"
  secondary_route: "R1 / R2 / R3 / R4 / null"
  adjudicating_prediction: "[prediction that distinguishes the resolution]"
  contribution_levers: ["[primary]", "[secondary]"]
  misclassification_risk: "[most plausible alternative diagnosis]"
```

If the authenticity gate fails, do not assign R1–R4 as a confirmed route. Report the conflict as apparent and prescribe the evidence needed to establish it.
