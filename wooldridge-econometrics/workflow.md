# Workflow — Running an Empirical Analysis (Wooldridge theory spine)

**When to use**: any substantive econometric task — a new analysis, a design question, a reviewer challenge, a robustness pass. This is the doing layer that turns the book's reference content into procedure.

**Positioning**: it is the *theory spine*, not a pipeline replacement. `empirical-pipeline-stata` executes, `run-empirical-research` orchestrates, `huntington-klein-causal-design` audits the design — this file supplies the econometric-theory decision at each step: which rung is load-bearing, which estimator the design can defend, which diagnostic must fire.

**How to use**: work the steps in order. Each step ends on a **completion criterion** — if you cannot tell done from not-done, you have rushed the step. Naming the **assumption rung** each step defends is part of the completion criterion, not an afterthought.

**The spine in one line**: question → data → model & target → estimator → diagnose → robustness → report. Skipping a stage corrupts everything downstream (ch20).

---

## Step 1 — Pose the question (before any data)

**Goal.** A question answerable with data, with the population model written and the counterfactual stated.

**Do.**
- Write the population model, no hats: y = β₀ + β₁x + … + u. Decide Y, X, the population P, and the ceteris paribus question.
- Decide the data structure that can answer it: cross-section, time series, pooled cross-section, or panel (ch01, ch20). Panel exists because a time-constant unobserved effect aᵢ may confound one cross-section — if that risk is real, you need panel data or a design.
- Check the data exist and are obtainable within the project.

**Completion criteria.** You can say "I'm studying the effect of X on Y in population P" in one sentence; the population model is written; the counterfactual is stated; the data structure is chosen for a stated reason.

**Rung defended.** None yet — this step decides whether MLR.4 / FE.4 / IV-exogeneity will even be load-bearing.

**Common failure.** Collecting data before posing the question → wrong variables, wrong population, wrong period (ch20 anti-pattern).

**Route.** `empirical-intake` for the intake packet; `run-empirical-research` to orchestrate.

---

## Step 2 — Audit the data (lie detector, before estimating)

**Goal.** Every inherited dataset passes the ch20 lie-detector checklist before it is trusted.

**Do.** Run min/max/mean/SD on key variables. Check: numeric missing sentinels (-99, 999); units and nominal-vs-real dollars; proportion-vs-percentage mixed entries; chronological order + time indicators; panel unit identifier + adjacency (phantom observations from differencing across units); balanced vs unbalanced structure (N, T, missingness pattern).

**Completion criteria.** Missing codes recoded to true missing; every column's min/max makes sense for its claimed unit; differencing/lead-lag verified — no phantom rows; the panel's N, T, and missingness pattern are known.

**Rung defended.** Data integrity precedes every assumption. MLR.1 (model holds for the population) and FE.1–3 (panel linear model, random sample, no perfect collinearity) are all silently violated by a corrupt dataset.

**Common failure.** Leaving -99 as data (ch20); differencing an unsorted panel → phantom observations.

**Route.** `stata-data-cleaning` (audit-only mode).

---

## Step 3 — Declare the target and the endogeneity sources

**Goal.** Separate the model from the estimator, and know what claim you are making before choosing how to make it.

**Do.**
- Name the target: causal coefficient / marginal effect / prediction / descriptive association. Causal → identification machinery (FE, IV, DiD, RD, or credible unconfoundedness) is in play; descriptive → a clean ceteris-paribus model is enough.
- Write the population equation, no hats. Never "an OLS model" — OLS/WLS/2SLS/FE are estimators of one population model (ch01, ch20).
- List the four endogeneity sources and rule each out or design for it: omitted variables, self-selection, measurement error, simultaneity (ch20).

**Completion criteria.** The target is one of the four types; the population equation is written; each endogeneity source is either argued away or assigned a design response; the load-bearing assumption rung for the intended claim is named.

**Rung defended.** MLR.4 (E(u|x)=0) or its panel/IV/ATE counterparts — the *content* of the rung is decided here, before any estimation.

**Common failure.** "Control for everything" — adding bad controls (mediators, colliders, outcome components) that block the causal path (ch03, ch06).

**Route.** `huntington-klein-causal-design` for an identification-first audit; `causal-analysis` to lock the estimand once the design is chosen.

---

## Step 4 — Choose the estimator

**Goal.** Pick the estimator the cheatsheet decision table justifies for this data structure × outcome type × target — and route the cases where the book is superseded.

**Do.** Walk the cheatsheet "Which estimator for my data?" table:

| Data / outcome | Estimator | Assumption rung |
|---|---|---|
| Cross-section, continuous | OLS + robust SE | MLR.1–4 unbiased, +MLR.5 BLUE |
| Binary | LPM (robust) or logit/probit, report APEs | MLR.1–4 / correct distribution |
| Count / corner at zero | Poisson QMLE, exp-mean, robust SEs — never log(1+y) | E(y\|x) = exp(xβ) only |
| Selected sample | Heckit with a real exclusion restriction | exclusion in selection eq. |
| Endogenous regressor | 2SLS: argue exogeneity, test relevance | IV exogeneity + relevance (F>10) |
| Two periods, policy | DiD / FD | parallel trends |
| Panel T≥2 | FE default; RE only if Cov(x,aᵢ)=0 via Mundlak/CRE | FE.1–4 / RE.4 |
| Persistent TS (ρ̂>0.9) | difference first; cointegration check | I(1) vs I(0) |
| Running-variable cutoff | RD local linear | continuity at cutoff |

**Route the registered exceptions — do not apply the book's default without checking:**
- **Staggered / multi-period DiD** → TWFE is biased under heterogeneous effects; run `staggered-did` (de Chaisemartin–D'Haultfœuille, Goodman-Bacon, Sun–Abraham). The book's general w_it framework (ch14) is the flexible starting point.
- **Few clusters** → cluster-robust SEs are unreliable with a handful of treated units; use wild cluster bootstrap / randomization inference (beyond the book).
- **Weak instruments** → first-stage F < 10 is a screen, not a pass; under heteroskedasticity/serial correlation demand Montiel Olea–Pflueger F ≳ 20 (cheatsheet thresholds).
- **Duration/survival outcomes** (time-to-recall, hazard) → beyond the book; start at [references/survival-duration-models.md](references/survival-duration-models.md) (Cox PH / AFT / competing risks / frailty), then `stata` / econometrics-agent for execution.

**Completion criteria.** The chosen estimator is justified against the endogeneity sources of step 3; the assumption rung that makes it valid is named; every registered exception relevant to the design has been checked and routed.

**Common failure.** Picking the estimator by what software defaults to, or by what makes results significant, instead of by the identifying assumption the design can defend.

**Route.** `stata` for syntax; `staggered-did` for the exception; `empirical-pipeline-stata` to lock and execute.

---

## Step 5 — Run, then diagnose (never read starred coefficients first)

**Goal.** The diagnostic pass is mandatory, not optional. A significant coefficient with a violated assumption is not evidence.

**Do.** Run the diagnostics that apply to this design (full procedure in diagnostics.md):
- Robust SEs always for cross-sections; if robust ≠ usual SEs dramatically, that IS the diagnosis.
- Time series: Breusch-Godfrey → Newey-West/HAC; FGLS only under strict exogeneity; OLS ≠ FGLS → keep OLS (ch12).
- Panel: SEs collapse after FE without clustering → cluster by unit (ch14). Test feedback with the lead regressor w_{i,t+1} (ch14).
- IV: first-stage F; overidentification test when over-identified (ch15).
- Functional form: RESET; quadratic turning point |β̂₁/2β̂₂| inside the data range; dummy-in-log as 100[exp(δ̂)−1]% (ch06).
- Heteroskedasticity: robust SEs are the default fix, not a gate to pass (ch08).

**Completion criteria.** Every diagnostic in diagnostics.md that applies to this design has been run and its output interpreted against its assumption rung; none is left unexamined.

**Rung defended.** The rungs claimed in step 4 are verified here: MLR.5 (robust SEs), TS.3′/TS.5 (HAC vs FGLS), FE.4 (feedback lead test), IV relevance.

**Common failure.** Reporting the base table and moving on; treating a diagnostic test as a ✓/✗ gate instead of reading what it says about the identifying assumption.

**Route.** [diagnostics.md](diagnostics.md) for the procedure; `stata` for commands.

---

## Step 6 — Robustness & sensitivity grid

**Goal.** Establish whether the main conclusion is a property of the data or of the specification.

**Do.**
- Define the grid ex ante and report it fully: alternative measures, dropped outliers, different functional forms, alternative clustering, subsamples.
- Justify dropping variables with an F test, never by significance-hunting (ch20).
- A result significant in only a small fraction of reasonable specifications is likely spurious (ch20).

**Completion criteria.** The sensitivity grid is defined before the main table is finalized; every cell is reported (or its omission explained); a sentence states whether the main conclusion survives the grid.

**Rung defended.** t/F inference assumes one model estimated once (ch20). The grid documents the specification search so the "one model" assumption is honored by transparency rather than violated by hiding.

**Common failure.** Stepwise selection (data mining); running ten specs and reporting the significant one — the final model's dependence on drop/add order makes its t/F uninterpretable (ch20).

**Route.** `xianzhu-skill` for disciplined specification search; `check-methodology` for an independent verification pass.

---

## Step 7 — Report theory-first

**Goal.** A paper section a reader could redo, with every number's theoretical basis named.

**Do.**
- Report population equations (no hats) and justify the estimator against the endogeneity sources.
- Every results table: SEs in parentheses, R² and n always, economic vs statistical significance distinguished (ch20).
- Logit/probit: report APEs (margins), not raw coefficients (ch17). Dummy-in-log: exact effect 100[exp(δ̂)−1]%. Log-level prediction: smearing factor (ch06).
- Never "an OLS model"; never 8-decimal false precision.

**Completion criteria.** A reader could redo the analysis from the text; every moving number has its assumption rung named; the strongest claim the design supports is stated, not the strongest-sounding one.

**Rung defended.** The whole ladder — every estimate's validity traceable to a named rung.

**Route.** `write-methods` / `write-results` / `empirical-writeup` to package.

---

## When the answer is "no significant result"

Null results are evidence, not failure — under the right rung. Before touching the specification: (1) distinguish "no effect" from "underpowered" (report the precision of the estimate, not just its p-value); (2) audit the design, not the spec — was the identifying assumption defensible? (3) run the sensitivity grid and report it; (4) never search specs for significance — that invalidates the t/F the whole analysis rests on (ch20). Full procedure in diagnostics.md "Null results". Route to `check-methodology` / `xianzhu-skill` for the discipline layer.
