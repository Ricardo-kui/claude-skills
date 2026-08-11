# Survival and Duration Models in Stata

Use this branch when the outcome is time until an event and censoring is part of the data-generating process. The Design Packet must define time origin, entry, failure, censoring, recurrent events, competing events, covariate timing, and target estimand.

## Default model ladder

1. Declare the survival data with `stset` and audit failures, censoring, delayed entry, gaps, and risk-set construction.
2. Use Kaplan–Meier or cumulative-incidence descriptions for transparent group patterns when appropriate.
3. Use Cox proportional hazards as the generic baseline for duration models on this machine.
4. Test the proportional-hazards assumption with Schoenfeld-residual diagnostics and inspect functional form.
5. Use a prespecified AFT model when the scientific target is a time ratio or when proportional hazards is not defensible and the distributional assumption is justified.
6. Use competing-risk, recurrent-event, frailty, stratified, or time-varying-covariate models only when the event process requires them.

Do not use OLS on log duration as a substitute for a censoring-aware baseline. It may appear only as a clearly justified auxiliary analysis.

## Execution contract

The Analysis Manifest must fix:

- clock origin, scale, entry, exit, failure, and censoring rules
- unit and risk-set structure
- baseline and time-varying covariates
- clustering or dependence rule
- Cox/AFT/competing-risk estimand and interpretation
- PH and functional-form diagnostics
- handling of ties, delayed entry, recurrent events, and competing risks

## Interpretation

- Cox coefficients or hazard ratios describe relative instantaneous hazard under the model; they are not time ratios.
- AFT coefficients/time ratios describe acceleration or deceleration of event time under a distributional model.
- Sign agreement across model families does not by itself establish robustness because estimands and assumptions differ.
- A failed PH diagnostic requires a prespecified response such as stratification, time interactions, or an alternative estimand; it does not automatically authorize whichever model gives the preferred result.

## Outputs

Return risk-set diagnostics, event/censor counts, model and version information, PH or distributional diagnostics, estimates with uncertainty, predicted survival/cumulative-incidence figures when authorized, deviations, and claim limits. Remove all project-specific numerical claims from reusable skill output.

