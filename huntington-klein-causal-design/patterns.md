# Reusable Causal-Design Patterns

Start by selecting the output mode in SKILL.md. Apply the **Identification Gate** to Design and Handoff modes, then use only the branch-specific contract needed for the request.

## Design Packet

**Use when**: turning a substantive question into an empirical design.

### Output Contract

1. **Causal question** — treatment contrast, outcome, unit, population, setting, horizon.
2. **Estimand** — ATE/ATT/LATE/local/dynamic effect with explicit weights.
3. **DGP** — assignment, outcome process, selection, measurement, timing, spillovers.
4. **Variation map** — every source of treatment variation; mark the source used for identification.
5. **Candidate designs** — 2–3 feasible approaches.
6. **Selected design** — why its comparison fits better than the closest rival.
7. **Assumptions** — one sentence per assumption, each linked to the relevant path or counterfactual.
8. **Estimator and inference** — method, identifying observations, clustering/dependence, weighting.
9. **Evidence plan** — diagnostics, falsification tests, sensitivity/bounds.
10. **Claim boundary** — what can be concluded, transported, or not learned.

### Completion Rule

Every assumption must have either supporting design evidence, a falsification implication, a sensitivity range, or an explicit “not empirically checkable” label.

## Candidate-Design Tournament

**Use when**: several methods appear plausible.

| Criterion | Candidate A | Candidate B | Candidate C |
|---|---|---|---|
| Source of variation | | | |
| Identifying comparison | | | |
| Estimand/population | | | |
| Main assumption | | | |
| Most credible supporting fact | | | |
| Strongest rival DGP | | | |
| Diagnostic that can fail | | | |
| Dependence/inference | | | |
| Extrapolation required | | | |
| Residual threat | | | |

Select the winner by assumption credibility and estimand fit. Do not select by expected precision, significance, familiarity, or software convenience.

### Completion Rule

Finish the tournament only when every candidate targets the same stated question or its estimand difference is explicit, all candidates are evaluated on identical support and timing, and the output either selects one design or declares that none clears its Stop Rules.

## Causal Claim Audit

**Use when**: evaluating a paper, result, or proposed causal statement.

Work backward:

1. **Claim**: quote or paraphrase the exact causal claim.
2. **Estimate**: identify the statistic actually reported.
3. **Estimand**: determine what population and contrast the statistic represents.
4. **Estimator**: identify its comparison and weights.
5. **Variation**: locate the units, cohorts, periods, cutoff neighborhood, or compliers supplying it.
6. **Assumptions**: reconstruct what must be true.
7. **Diagnostics**: classify each as falsification, calibration, implementation check, or precision check.
8. **Threats**: measurement, selection, anticipation, spillovers, treatment versions, missingness, model uncertainty.
9. **Verdict**:
   - **Credible for the stated estimand**
   - **Conditionally credible with material unresolved assumptions**
   - **Associational evidence only**
   - **Not interpretable for the stated claim**

Give the smallest claim supported by the design rather than a binary “causal/not causal” label.

### Completion Rule

Finish the audit only when every material causal claim is traced to the actual estimand, identifying observations, estimator weights, unresolved assumptions, and a verdict whose scope matches the evidence.

## Robustness Ladder

**Use when**: designing robustness checks.

For each rung, state the assumption changed and the expected diagnostic behavior.

1. **Implementation replication** — same design, independently reproduced code.
2. **Functional-form alternatives** — different defensible representations of the same comparison.
3. **Support alternatives** — bandwidth, trimming, donor pool, event window, or cohort support.
4. **Falsification** — placebo time/cutoff/outcome, negative controls, impossible effects.
5. **Comparison alternatives** — other valid control groups, not-yet-treated cohorts, donor sets.
6. **Inference alternatives** — assignment-consistent clustering, randomization, weak-IV robust, HAC, small-cluster methods.
7. **Assumption relaxation** — sensitivity analysis or partial-identification bounds.
8. **Measurement and sample multiverse** — defensible construct, cleaning, linkage, and missing-data choices.

A check earns space only if its result would change the interpretation.

### Completion Rule

Finish the robustness plan only when every check names the assumption it changes or probes, the result that would alter the claim, and the residual threat it leaves unresolved.

## Simulation Specification

**Use when**: validating an estimator, power calculation, or failure mode.

### DGP Card

- units, periods, clusters;
- treatment assignment;
- true effect and heterogeneity;
- confounding and selection;
- outcome equation;
- dependence and errors;
- missingness and measurement;
- assumption-violation parameters.

### Evaluation Card

- estimand;
- estimators;
- repetitions and seed;
- bias and RMSE;
- empirical versus reported SE;
- confidence-interval coverage;
- rejection/power;
- convergence/failure;
- Monte Carlo uncertainty.

Include a baseline, realistic scenarios, and adversarial scenarios. Explain why the chosen parameter ranges fit the application.

### Completion Rule

Finish the simulation specification only when another analyst can reproduce the DGP, scenario grid, estimator pipeline, true estimand, Monte Carlo uncertainty, and failure accounting without inferring an unstated parameter.

## Methods Write-Up Contract

**Use when**: converting a finished design into prose.

Write six functional paragraphs:

1. **Question and estimand** — define the causal object.
2. **Institution and variation** — explain why treatment changes.
3. **Identification** — state the counterfactual comparison and assumptions.
4. **Estimation** — map the estimator to the design and weights.
5. **Inference and diagnostics** — dependence, uncertainty, falsification, sensitivity.
6. **Limits** — local population, transport, measurement, interference, and residual assumptions.

Separate design facts, empirical diagnostics, identifying assumptions, and researcher judgments. Avoid presenting a passed diagnostic as proof of its parent assumption.

### Completion Rule

Finish the write-up only when each causal sentence can be classified as a design fact, supported inference, identifying assumption, project judgment, or limitation and the prose does not enlarge the identified population or estimand.

## Execution Handoff

**Use when**: code or estimation is requested.

Pass this YAML-shaped Design Packet to the execution skill. Preserve `unknown` values; let `blocked` prevent causal estimation until the missing design choice is resolved.

```yaml
protocol: huntington-klein-causal-design-v1.2
design_status: ready | blocked
question:
claim_type: descriptive | predictive | causal
treatment_variable:
treatment_definition:
treatment_contrast:
treatment_versions:
assignment_process:
adoption_timing:
reversibility:
anticipation_window:
outcome_variable:
outcome_definition:
outcome_timing:
unit:
population:
setting:
time_horizon:
estimand:
data:
  path:
  observation_level:
  variable_dictionary:
  variable_timing:
variation_map:
  sources: []
  identifying_source:
  identifying_observations:
candidate_designs: []
selected_design:
closest_rival:
comparison_groups: []
identifying_sample:
assumption_ledger:
  - assumption:
    role:
    evidence:
    falsification:
    sensitivity:
estimation:
  estimator:
  fixed_effects:
  weights:
  software_target:
inference:
  assignment_level:
  dependence:
  clustering:
  small_sample_strategy:
diagnostics: []
stop_rules: []
expected_outputs: []
authorized_next_scope: none | descriptive_audit | causal_estimation
unknowns: []
epistemic_split:
  facts: []
  supported_inferences: []
  assumptions: []
  judgments: []
  unknowns: []
```

Require the execution result to return coefficient evidence, design diagnostics, Stop Rule status, deviations from the packet, and the updated Epistemic Split as separate fields.

### Completion Rule

Set `design_status: ready` only when the execution skill can implement the design without guessing the treatment definition, assignment and timing, estimand, comparison group, identifying sample, estimator, inference level, or required diagnostics. Otherwise set `blocked`, list the missing decisions in `unknowns`, set `authorized_next_scope` to the narrowest safe level, and return only that authorized analysis.
