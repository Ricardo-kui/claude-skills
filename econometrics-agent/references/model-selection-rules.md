# Model Selection Rules

Source: extracted from `RulePlanner.choose_model` and `build_plan` in
`lite_econometrics_agent.py`. This documents the **transparent, rule-based
routing** the CLI uses when `--model auto` is set. The point of recording it as
prose is that the same decision logic applies to estimator choice regardless of
whether execution runs in this CLI or in Stata: selection should be explainable,
never black-box.

## Design principle

The router never lets the model "invent" a method. It matches explicit signals
(an instrument column, a running variable, panel identifiers, or keywords in
the query) to an estimator and emits a **list of human-readable reasons**
(`selection_reasons`). If the user forces `--model`, routing is bypassed and the
reason is simply `user_forced_model=<model>`.

## Routing priority (top wins)

Evaluated in this order; the first branch that fires determines the estimator:

1. **User-forced model** — `spec.model != "auto"` → return that model.
2. **Explicit instrument** — an instrument column is provided → `iv`.
3. **IV keywords** — query mentions IV / 2SLS / instrument / endogeneity / endogenous → `iv`.
4. **Fuzzy RDD with explicit inputs** — running variable + cutoff provided AND query mentions fuzzy RDD → `fuzzy-rdd` (upgrade to global-poly if requested).
5. **Sharp RDD with explicit inputs** — running variable + cutoff provided → `rdd` (upgrade to global-poly if requested).
6. **Fuzzy RDD by query** — query mentions fuzzy RDD and a running variable exists → `fuzzy-rdd`.
7. **Sharp RDD by query** — query mentions discontinuity / cutoff / threshold and a running variable exists → `rdd`.
8. **AIPW** — query mentions AIPW / augmented IPW / doubly robust AND treatment is binary → `aipw`.
9. **IPWRA** — query mentions IPWRA / doubly robust regression adjustment AND treatment is binary → `ipwra`.
10. **IPW** — query mentions IPW / inverse probability weighting AND treatment is binary → `ipw`.
11. **PSM** — query mentions matching / propensity score AND treatment is binary → `psm`.
12. **Event study** — query asks for dynamic effects / pre-trends AND panel structure present → `event-study`.
13. **DID (explicit group-post)** — both `treat_group` and `post` provided → `did`.
14. **DID (by query)** — query describes a policy-shock / DID design AND panel present AND treatment is binary → `did`.
15. **Panel default** — panel structure present and nothing above fired → `fe`.
16. **Fallback** → `ols` (robust).

Two recurring logic checks sit behind these branches:

- **Panel structure** requires both `entity_id` and `time_id` present, in the columns, and with fewer unique entities than rows.
- **Binary treatment** (`is_binary_like`) gates the propensity-score estimators and DID-by-query.

## Keyword sets (lowercased substring match)

| Estimator | Keywords |
| --- | --- |
| iv | iv, 2sls, instrument, instrumental, endogeneity, endogenous |
| fe | fe, fixed effect(s), twfe, panel, within, entity effect, time effect |
| did | did, difference in difference(s), policy shock, treated, staggered adoption |
| event-study | event study, dynamic effect, dynamic treatment, lead, lag, pretrend, pre-trend |
| rdd | rdd, regression discontinuity, discontinuity, cutoff, threshold |
| fuzzy-rdd | fuzzy rdd, fuzzy regression discontinuity, fuzzy discontinuity |
| global-poly | global polynomial, polynomial rdd, higher-order polynomial, global poly |
| psm | psm, matching, matched, propensity score |
| ipw | ipw, inverse probability weighting, propensity weighting |
| aipw | aipw, augmented ipw, double(d) robust, augmented inverse probability weighting |
| ipwra | ipwra, ipw regression adjustment, weighted regression adjustment, doubly robust regression adjustment |

## Output of routing

A successful route produces:

- `selected_model` — the chosen estimator key.
- `selection_reasons` — the ordered list of why (one string per fired signal).
- `knowledge_card` — the matched method card (see `method-cards.md`).
- `plan` — a five-step execution template built from the card.

## Five-step plan template (`build_plan`)

For every estimator the plan is the same skeleton, specialized by the card:

1. Load the dataset and validate requested variables against the econometric design.
2. Apply the routing rule: `<card.core_rule>`.
3. Estimate `<card.display_name>` with the lightweight local tool library.
4. Check diagnostics: first three items of `<card.diagnostics_to_check>`.
5. Report coefficients, identification risks, and reflection notes in a compact summary.

## How to reuse this outside the CLI

When you are choosing an estimator by hand (or in Stata), walk the same priority
list against your data and research question. The value is the discipline: force
an explicit, citable reason for the estimator before you run it, and treat the
fallback to OLS as a signal that the design is underspecified rather than a
neutral default.
