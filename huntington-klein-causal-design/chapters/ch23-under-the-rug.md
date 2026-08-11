# Chapter 23: Under the Rug

## Core Idea

Every causal design rests on assumptions beyond its headline identification condition. Audit model choice, measurement, data processing, missingness, treatment versions, interference, and distributional behavior before calling an estimate credible.

## Final Threat Audit

### Model Uncertainty

List all substantively plausible DAGs, control sets, functional forms, timing rules, samples, and estimators. Distinguish a multiverse of defensible choices from a specification search over arbitrary models. Report which conclusions survive and which design assumptions all models share.

### Construct and Measurement Validity

For every variable, map construct → operationalization → data-generation process. Ask:

- Does the measure cover the theoretical construct?
- Is measurement affected by treatment, outcome, observer, or incentives?
- Are alternative measures different operationalizations or different constructs?
- Does measurement error differ by treatment or time?
- Did the coding/aggregation change the estimand?

### Observer and Processing Effects

Data collection can change behavior. Cleaning, linkage, deduplication, coding, and sample rules can also move estimates. Preserve a reproducible raw-to-analysis pipeline, justify each decision, and audit plausible alternatives.

### Missing Data and Selection

Draw missingness and sample inclusion in the DAG. Describe missingness by treatment, outcome proxies, time, and covariates. Listwise deletion is valid only under restrictive conditions. Use multiple imputation, weighting, likelihood, bounds, or selection models when their assumptions fit; include the analysis model and design structure in imputation.

### SUTVA, Treatment Versions, and Spillovers

Define treatment versions and exposure mapping. Model interference across networks, markets, geography, firms, or time. If one unit's treatment affects another's outcome, redefine the unit/estimand or use a design that models spillovers.

### Heavy Tails and Nonexistent Moments

Inspect whether means, variances, and asymptotic approximations are meaningful. Use robust summaries, transformations tied to the estimand, influence diagnostics, or tail-aware methods. A large sample may not stabilize a pathological distribution.

### The Treatment Mystery

After closing back doors, ask why treatment still varies. A credible answer should point to the identifying assignment mechanism. If the remaining variation has no plausible source, the design may be relying on residual noise, error, or an unmodeled selection process.

## Epistemic Report

Separate:

1. **Established by design facts**: assignment rules, timing, observed support.
2. **Supported but not established**: falsification tests and robustness patterns.
3. **Required assumptions**: unobserved counterfactual restrictions.
4. **Project judgments**: transport, mechanism, and measurement interpretations.
5. **Unknowns**: threats the data cannot resolve.

## Cross-Cutting Evidence Ledger

| Domain | Record | Typical consequence if wrong |
|---|---|---|
| Construct | Definition and measure coverage | Claim addresses the proxy, not the theory |
| Data collection | Who reports/records and when | Observer, incentive, or treatment-induced measurement |
| Cleaning | Every consequential rule | Analyst degrees of freedom and sample change |
| Missingness | Causes and timing | Selection/collider bias |
| Treatment versions | Dose, implementation, compliance | Incoherent average effect |
| Interference | Exposure network/geography/market | Control outcomes are contaminated |
| Model uncertainty | Plausible DAGs/specifications | Understated uncertainty |
| Distribution tails | Influence and moment behavior | Unstable means, SEs, and tests |
| Transport | Target versus identified population | Local evidence overgeneralized |

For each domain, assign one status: resolved by design, empirically probed, sensitivity-analyzed, or unresolved. “Discussed in limitations” is not a status unless the likely direction and consequence for the claim are stated.

## Failure Modes

- Treating default data cleaning as neutral.
- Imputing outcomes using post-treatment information without respecting the estimand.
- Calling multiple treatment versions one binary treatment.
- Ignoring market or network spillovers.
- Reporting only sampling uncertainty.
- Using many robustness checks while omitting the one shared identifying assumption.

## Completion Check

Do not finalize a causal claim until every audit domain is addressed or explicitly marked unresolved, with the likely direction and consequence of failure.

## Worked Example

> Source-grounded reconstruction from Huntington-Klein (2025); compressed and paraphrased.

A theory uses “trust,” but the dataset contains a one-to-ten self-report item. The construct-to-measure chain raises several threats: respondents interpret trust differently, treatment changes willingness to disclose, scale use differs across groups, and cleaning choices determine which responses count as valid.

Create a measurement multiverse before estimating: alternative defensible item codings, scale treatments, inclusion rules, and missing-data models. Separate changes in the theoretical construct from changes in reporting. If treatment itself changes reporting, a causal effect on the recorded score is not automatically an effect on latent trust.

Then ask the treatment mystery: after adjustment, why does treatment still vary? If the answer is “residual model variation,” the causal design is incomplete. If the answer is a documented assignment rule, connect that rule to the identifying observations and remaining assumptions.

## Connects To

- [Ch2](ch02-research-questions.md): construct and treatment definition.
- [Ch3](ch03-describing-variables.md): distributions and missingness.
- [Ch11](ch11-causality-with-less-modeling.md): robustness.
- [Ch21](ch21-partial-identification.md): honest uncertainty under relaxed assumptions.
