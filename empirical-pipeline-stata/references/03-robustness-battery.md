# Step 6 · Threat-Matched Verification Menu

There is no universal robustness battery. Select the smallest sufficient set whose assumptions match the design and whose purpose is named in the Analysis Manifest. A test without a named threat is optional noise, not credibility.

## Threat-to-test map

| Threat | Eligible evidence | Important boundary |
|---|---|---|
| Few or influential assignment clusters | wild-cluster bootstrap, randomization inference when assignment was actually randomized, leave-one-cluster-out influence | Do not change clustering levels to hunt for a larger p-value |
| Multiple outcomes or hypothesis family | Romano–Wolf or another prespecified multiplicity procedure | Define the family before seeing results |
| Staggered-treatment heterogeneity | cohort-aware estimators, support tables, TWFE decomposition as diagnostic | Never use uncorrected TWFE as the preferred effect |
| Parallel-trend violations | design-specific pre-period evidence, HonestDiD or other prespecified sensitivity | Nonsignificant pretrends do not prove the assumption |
| Omitted-variable sensitivity in a compatible linear selection setting | Oster-style sensitivity or another justified bound | Do not apply mechanically; document the proportional-selection and R-max assumptions |
| Functional form or measurement | theory-supported transformations and alternative measures | Lock the admissible set; retain every result |
| Sample construction or attrition | sample-funnel audit, balanced-support checks, attrition models/tests tied to the threat | Do not drop observations because they weaken significance |
| Instrument weakness or invalidity | first-stage strength, weak-IV-robust inference, overidentification only when applicable, exclusion evidence | A large first-stage statistic does not establish exclusion |
| RDD manipulation or bandwidth sensitivity | density, covariate continuity, bandwidth and polynomial checks | Keep the running-variable and cutoff contract fixed |
| Weighting/matching support | overlap, balance, weight diagnostics, estimand sensitivity | Do not hide trimmed or unsupported populations |
| Influential observations | leverage/residual diagnostics and prespecified influence analysis | Deletion requires a data-quality or estimand rationale |

## Selection rules

1. Start from the Design Packet's threat ledger and stop rules.
2. For each proposed test, record `threat`, `assumption`, `test`, `decision_rule`, and `claim_impact` before execution.
3. Preserve the baseline sample and specification unless the test itself is a declared sample/specification sensitivity.
4. Run a governed multiverse through `xianzhu-skill` when many admissible measures or specifications exist. Never select the headline model by p-value.
5. Record null, adverse, failed, and dependency-skipped results in the Run Manifest.

## Dependency and output discipline

- Check dependencies with `which` and record versions before estimation.
- Do not run unconditional `ssc install ..., replace`. Install only missing packages when authorized.
- Write every test to a run-scoped output directory fixed by the Analysis Manifest.
- Fixed filenames with `replace` are allowed only inside a newly created, verified run directory.

## Verification matrix

Return one row per test:

```text
threat | test | prerequisite_status | result | stop_rule_status | claim_impact | artifact_path
```

The conclusion may strengthen, narrow, or invalidate a claim. It must never be filtered by significance.

