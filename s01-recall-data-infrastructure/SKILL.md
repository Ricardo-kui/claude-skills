---
name: s01-recall-data-infrastructure
description: Use when setting up, auditing, or extending product recall data infrastructure across recall projects, including NHTSA recall data, FirmAwarenessDate, recall date, time to recall, left-censoring, recall count, Cox proportional hazards models, and shared variable definitions for product recall research.
---

# Product Recall Data Infrastructure

Use this skill when a product recall project needs a common data backbone. The goal is to keep variable definitions, cleaning code, and model choices consistent across recall timing, recall likelihood, and recall count projects.

## Expected Inputs

- Raw NHTSA recall data with recall dates, firm identifiers, product categories, and public disclosure fields.
- Firm financial and market data such as Compustat or CRSP.
- Industry classifications such as SIC or NAICS.
- Existing project Context Packet or project workroom when available.

## Expected Outputs

- A cleaned recall timing dataset with `FirmAwarenessDate`, `RecallDate`, `time_to_recall`, and left-censoring indicators.
- Reusable Stata or Python cleaning code.
- A variable definition ledger that can be referenced by all recall projects.
- Notes on identification threats, measurement ambiguity, and robustness checks.

## Workflow

1. Read the relevant project Context Packet and any existing recall data documentation.
2. Locate the current NHTSA raw data and prior cleaning scripts before creating new code.
3. Define core dates consistently:
   - `FirmAwarenessDate`: the earliest defensible date when the firm or public record indicates awareness.
   - `RecallDate`: the firm's actual recall start or NHTSA recall date, depending on project design.
   - `time_to_recall`: elapsed days from awareness to recall.
   - `left_censored`: cases where awareness predates the observable sample window.
4. Deduplicate recall records by the project-specific recall identifier and document the rule.
5. Merge firm-level data using an auditable firm-year or firm-date bridge.
6. Use Cox proportional hazards as the baseline survival model for recall timing unless the project has a documented reason to use another estimator.
7. For recall counts, consider Poisson or negative binomial models and document overdispersion diagnostics.
8. Plan robustness checks around date definitions, left-censoring treatment, industry controls, firm matching, and alternative model forms.

## Guardrails

- Do not create a second variable definition if one already exists; update the shared ledger instead.
- Do not default to OLS on log duration for recall timing without explaining why survival analysis is unsuitable.
- Do not silently change date definitions across projects.
- Every variable definition change should identify affected projects and downstream tables.

## Related Routing

- Use `stata-data-cleaning` for Stata data construction.
- Use `stata` for a single Cox/table task or `empirical-pipeline-stata` for the locked full execution chain.
- Use `python-panel-data` only when Python is the better execution environment for the specific data task.
- Consult `rules/axioms/e03_construct_measure_alignment.md` and `rules/axioms/p05_standardize_data_infrastructure_across_projects.md` in the academic infrastructure when making measurement or shared-infrastructure decisions.
