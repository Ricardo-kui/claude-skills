# Chapter 21: Partial Identification

## Core Idea

When point identification requires an assumption too strong to defend, weaken it explicitly and report the set or range of effects consistent with the remaining assumptions. Wider but credible conclusions can be stronger evidence than a precise answer built on hidden certainty.

## Partial-Identification Contract

State:

- target parameter;
- assumptions sufficient for point identification;
- assumption being relaxed;
- parameterization and defensible range of violation;
- resulting identified set or sensitivity curve;
- sampling uncertainty around that set;
- threshold at which the substantive conclusion changes;
- external evidence used to calibrate the range.

## Assumption Ladder

1. Start with assumptions supported strongly by design facts.
2. replace exact-zero restrictions with sign, order, magnitude, or shape restrictions.
3. derive the effect bounds implied by each assumption level.
4. show how bounds narrow as assumptions strengthen.
5. separate the data-driven component from the judgment-driven range.
6. report conclusions robust across the plausible assumption region.

## Common Applications

- attrition and sample-selection bounds;
- omitted-variable sensitivity in regression;
- hidden-bias bounds after matching;
- imperfect exclusion in IV;
- deviations from parallel trends in DiD;
- misclassification and measurement error;
- violations of monotonicity or interference restrictions.

## Sensitivity Analysis

A useful sensitivity analysis asks how strong an unmeasured process must be to alter the conclusion and compares that strength with observed benchmark covariates or institutional knowledge. Benchmarks inform plausibility; they do not prove unobserved confounding is similar.

For matching, choose a sensitivity method consistent with the matching/weighting design. Classical Rosenbaum bounds apply to particular matched designs and should not be treated as universal.

## Formal and Design-Specific Approaches

Formal partial identification derives bounds from probability restrictions and the DGP. Design-specific approaches target a known weak point—for example, bounded violations of DiD parallel trends or IV exclusion. The latter are easier to apply but inherit the rest of the design's assumptions.

## Reporting

Show:

- point estimate under the strongest baseline assumption;
- effect range over calibrated violations;
- robustness value or breakdown frontier;
- uncertainty bands;
- assumptions under which sign, magnitude, or decision changes.

Avoid reducing the exercise to “the result remains significant.”

## Assumption-to-Conclusion Display

Use a table or curve rather than one robustness label:

| Assumption level | Allowed violation | Identified effect set | Substantive conclusion |
|---|---|---|---|
| Minimal design facts | Broad/worst case | Wide bounds | What sign or magnitude is known? |
| Sign/shape restriction | Direction only | Narrower bounds | Which conclusions become possible? |
| Calibrated magnitude | Benchmarked range | Sensitivity interval | Where does the claim break? |
| Point-identifying assumption | Zero violation | Point estimate + sampling CI | What extra belief buys precision? |

There are two uncertainties: sampling uncertainty conditional on assumptions and identification uncertainty across assumptions. Display both. If the sensitivity parameter is abstract, translate it into a comparison with observed covariates, plausible direct effects, or untreated trend deviations so the range can be judged substantively.

## Failure Modes

- Choosing a violation range only because it preserves the claim.
- Calling a conventional specification table sensitivity analysis.
- Reporting bounds without explaining their identifying assumptions.
- Ignoring sampling uncertainty in the bounds.
- Treating an extremely wide identified set as a failed analysis rather than honest evidence.
- Benchmarking against a weak observed covariate and calling the result robust.

## Completion Check

A partial-identification result is complete when readers can see exactly how each added assumption narrows the set and where the substantive conclusion breaks.

## Worked Example

> Source-grounded reconstruction from Huntington-Klein (2025); compressed and paraphrased.

Parents are randomized to receive a cash incentive intended to keep children in school, but untreated parents are more likely to leave the study, and follow-up also depends on schooling. Conditioning on observed follow-up can create selection bias despite random assignment.

Rather than assert missing at random, begin with worst-case outcome bounds for missing children. Then add assumptions one at a time—for example, monotone attrition or a calibrated difference between observed and missing outcome rates. Show how each assumption narrows the treatment-effect interval.

The conclusion may become: “The effect is nonnegative unless missing untreated children attend school at least k percentage points more often than comparable observed untreated children.” That threshold is more informative than one imputed point estimate because readers can evaluate k using contextual evidence.

## Connects To

- [Ch11](ch11-causality-with-less-modeling.md): robustness logic.
- [Ch14](ch14-matching.md): hidden-bias sensitivity.
- [Ch18](ch18-difference-in-differences.md): trend-deviation bounds.
- [Ch19](ch19-instrumental-variables.md): imperfect exclusion.
