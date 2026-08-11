# Chapter 11: Causality with Less Modeling

## Core Idea

When the full DGP cannot be modeled credibly, replace broad ignorance with narrower design assumptions, derive their observable implications, and report sensitivity or bounds when point identification demands too much.

## Strategy Ladder

1. **Explicit adjustment**: model and close known back doors.
2. **Comparable control design**: argue that treated and control units are comparable on a narrower dimension.
3. **Change-based or local comparison**: remove stable differences and require comparability of changes or local potential outcomes.
4. **Assumption-specific falsification**: test implications that should fail if the design story is wrong.
5. **Sensitivity or partial identification**: vary uncertain assumptions and report a range.
6. **Plausibility audit**: inspect whether magnitude, sign, timing, or implied mechanism is credible.

Moving down the ladder does not remove assumptions; it trades one set for another.

## Robustness Contract

For every robustness test, write:

- the identifying assumption being probed;
- the observable implication derived from it;
- the test and expected null/shape;
- what a failure means;
- what a pass cannot establish.

A robustness check is informative only when it either seeks to disprove an assumption or estimates under a meaningfully relaxed/different assumption.

## Placebos and Negative Evidence

A placebo assigns a fake treatment, outcome, cutoff, or date where no causal effect should exist. A nonzero estimate can reveal design failure. A zero estimate is reassuring only against threats that would also generate the placebo result; it does not validate all assumptions.

## Partial Identification

When an assumption cannot be defended, parameterize its plausible range and map that range into bounds on the effect. Precision should shrink or expand transparently with assumption strength.

## Robustness Interpretation Grid

| Result | Interpretation |
|---|---|
| Falsification fails strongly | The tested implication contradicts the design; revise or stop |
| Falsification is imprecise | Evidence is uninformative; do not call it a pass |
| Alternative valid design agrees | Reassuring triangulation if assumptions differ |
| Cosmetic specifications agree | Little new identification evidence |
| Sensitivity range preserves sign | Sign is robust only within the calibrated violation range |
| Bounds include large positive and negative effects | Data/design do not determine direction |
| Implausible magnitude | Audit units, coding, treatment versions, and assumptions before theorizing |

Design robustness around decisions: specify in advance what outcome would change the causal claim.

## Failure Modes

- Specification curves in which every model shares the same confounding failure.
- Treating a nonsignificant placebo as proof of validity.
- Adding the covariate that failed a balance test while ignoring what the failure implies about unmeasured variables.
- Declaring a surprising implausible result credible because the code ran and standard errors are small.
- Hiding assumption sensitivity behind one preferred estimate.

## Completion Check

The robustness package must include at least one design-specific falsification, one assumption-relaxation analysis, and an explanation of residual uncertainty.

## Worked Example

> Source-grounded reconstruction from Huntington-Klein (2025); compressed and paraphrased.

Suppose a policy applies above an electricity-use threshold. The design compares customers just above and below the true threshold. A placebo test moves the cutoff to a nearby value where no policy changes and reruns the same procedure.

- A visible placebo jump indicates that the outcome or composition changes at thresholds even without treatment, weakening the design.
- No placebo jump rejects that particular failure pattern only; it does not prove no sorting at the real cutoff or no concurrent policy.

Next relax the identifying assumption: allow an untreated outcome discontinuity over a substantively calibrated range and recompute the treatment-effect bounds. The placebo and sensitivity analysis answer different questions—one seeks evidence of failure, the other shows how much failure the conclusion can tolerate.

## Connects To

- [Ch15](ch15-simulation.md): simulate bias and inferential behavior.
- [Ch21](ch21-partial-identification.md): formalize bounds and sensitivity.
- [Ch23](ch23-under-the-rug.md): broaden the threat model.
