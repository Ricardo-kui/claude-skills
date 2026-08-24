---
name: wooldridge-econometrics
description: "Wooldridge 计量经济学知识库（Introductory Econometrics, 8th ed.）：估计量选择与辩护、识别假设检查、诊断与补救，以及完整实证分析的理论指导。Use when choosing/defending an estimator (OLS, IV/2SLS, FE/RE, DiD, RD, logit/Tobit/Heckit), checking identifying assumptions (MLR/TS/FD/ATE ladders), diagnosing heteroskedasticity, serial correlation, endogeneity, weak instruments, running treatment-effect/panel analyses, or whenever you need the theoretical basis for an empirical analysis — estimator choice, diagnostics, robustness, or reviewer defense. 触发词：Wooldridge、计量经济学、回归假设、工具变量、弱工具变量、双重差分、固定效应、随机效应、异方差、序列相关、单位根、时间序列回归、样本选择、稳健标准误、内生性、处理效应、estimator choice、identifying assumptions、Heckman selection、unit root、cointegration、计量实证、实证分析怎么做"
---

<!-- argument-hint: [topic, estimator name, chapter number, or an empirical/diagnosis question] -->

# Introductory Econometrics: A Modern Approach (8th ed.)
**Author**: Jeffrey M. Wooldridge | **Pages**: ~940 | **Chapters**: 20 | **Generated**: 2026-08-21

## How to Use This Skill

Pick your entry point:

- **Running an empirical analysis end-to-end** → [workflow.md](workflow.md): the 7-step procedure with completion criteria — the "how to do it" spine.
- **Diagnosing a problem** (null results, SEs that collapse, weak IV, a test firing, a reviewer objection) → [diagnostics.md](diagnostics.md): symptom → test → remedy → recheck.
- **Choosing or defending an estimator** → [cheatsheet.md](cheatsheet.md) for the decision table and thresholds, [patterns.md](patterns.md) for the recipe, and the chapter file for the theory.
- **Definitions** → [glossary.md](glossary.md). **A deep book question** → the chapter file (Chapter Index below).

Every answer names the assumption rung it rests on (e.g. "unbiased under MLR.1–4"). If the question is modern staggered DiD, few-cluster inference, or identification-first design audits, the book is superseded — [workflow.md](workflow.md) routes you to the newer tool.

## The Doing Spine (7 steps — full procedure in [workflow.md](workflow.md))

1. **Pose the question** — population model (no hats) + ceteris paribus counterfactual. *Done when* you can name Y, X, population P, and the data structure in one sentence.
2. **Audit the data** — lie-detector checklist (missing sentinels, units, proportions vs percentages, panel ordering, phantom obs). *Done when* every inherited dataset passes.
3. **Declare the target & endogeneity sources** — causal coefficient vs prediction vs description; rule out omitted vars, self-selection, measurement error, simultaneity. *Done when* the load-bearing assumption rung is named.
4. **Choose the estimator** — cheatsheet decision table; route the registered exceptions (staggered DiD → `staggered-did`, few clusters → wild bootstrap, weak IV → MOP, survival → beyond the book). *Done when* the estimator is justified against the endogeneity sources.
5. **Run, then diagnose** — never read starred coefficients without the diagnostic pass. *Done when* every applicable diagnostic in diagnostics.md is run and interpreted.
6. **Robustness grid** — defined ex ante, reported fully. *Done when* the grid is run and the main conclusion's survival is stated.
7. **Report theory-first** — population equations, SEs/R²/n always, APEs for LDV, exact dummy-in-log effects. *Done when* a reader could redo the analysis.

One-model-once: t/F inference assumes one model estimated once — the grid documents the search so the assumption is honored by transparency.

## Mental Models & Leading Words

**assumption ladder** — every estimator's credibility is a numbered assumption set; learn what each rung buys (full ladder in [cheatsheet.md](cheatsheet.md)). When a claim fails, name the rung that failed — that is the diagnosis.

**E(u|x) = 0 is the whole game** (Ch 2–3) — separates description from causation. Omitted variable bias: sign it with the Table 3.2 matrix before running anything (formula and recipe in [patterns.md](patterns.md)).

**ceteris paribus first, estimator second** (Ch 1, 20) — the population model (no hats) comes first; OLS/WLS/2SLS/FE are competing estimators of it, never "models" themselves. There is no such thing as "an OLS model."

**estimand first, estimator second** (Ch 19) — name the causal estimand (ATE/ATT/LATE) before choosing an estimator; an unnamed estimand is a red flag. ATE, ATT, and LATE answer different policy questions and need different assumption sets — estimators are competing implementations of the named estimand.

**bad controls are worse than no controls** (Ch 3, 6) — never hold fixed mediators, colliders, or components of the outcome. Controls that only shrink error variance are optional, not required.

**R² is not evidence** (Ch 2, 3, 10) — high R² between trending series is spurious; low R² with an unbiased causal coefficient is fine.

**robust inference by default** (Ch 8, 12) — White/robust SEs for cross-sections, HAC/Newey-West for time series; FGLS only under strict exogeneity, and if OLS ≠ FGLS, keep OLS (recipes in [patterns.md](patterns.md)).

**panel trades assumptions for variation** (Ch 13–14) — FD at T=2 ≡ DiD; FE is the default for T≥2; RE only if Cov(x,aᵢ)=0, tested via Mundlak/CRE; always cluster by unit.

**IV is an argument, not a command** (Ch 15–16) — exogeneity is untestable, you must argue it; relevance is testable (thresholds in [cheatsheet.md](cheatsheet.md)). Diagnose with VAT/overid tests.

**potential outcomes unify causal inference** (Ch 2, 19) — ATE/ATT under unconfoundedness + overlap; IV gives LATE; RD gives local effects at the cutoff; DiD needs parallel trends (details and trims in [cheatsheet.md](cheatsheet.md)).

**match the estimator to the LDV** (Ch 17) — binary → LPM or logit/probit, report APEs; counts/corners → Poisson QMLE (never log(1+y)); true censoring → Tobit; selected sample → Heckit with a real exclusion.

**persistence changes everything** (Ch 11, 18) — ρ̂ > 0.9 ⇒ treat as I(1): difference or use growth rates; levels are spurious unless cointegrated.

**specification search discipline** (Ch 9, 20) — RESET for functional form; proxies for OVB; CEV attenuates; t/F assumes one model estimated once — run sensitivity grids and report them all.

## Chapter Index

| # | Title | Key Frameworks |
|---|-------|----------------|
| [ch01](chapters/ch01-the-nature-of-econometrics-and-economic-data.md) | The Nature of Econometrics and Economic Data | econometric model, ceteris paribus, data structures |
| [ch02](chapters/ch02-the-simple-regression-model.md) | The Simple Regression Model | SLR.1–5, zero conditional mean, ATE with binary treatment |
| [ch03](chapters/ch03-multiple-regression-estimation.md) | Multiple Regression Analysis: Estimation | MLR.1–5, partialling out, omitted variable bias, bad controls |
| [ch04](chapters/ch04-multiple-regression-inference.md) | Multiple Regression Analysis: Inference | MLR.6/CLM, t and F tests, linear combinations |
| [ch05](chapters/ch05-ols-asymptotics.md) | Multiple Regression Analysis: OLS Asymptotics | consistency, asymptotic normality, LM test |
| [ch06](chapters/ch06-multiple-regression-further-issues.md) | Multiple Regression Analysis: Further Issues | functional forms, adjusted R², prediction intervals |
| [ch07](chapters/ch07-qualitative-information.md) | Multiple Regression Analysis with Qualitative Information | dummies, interactions, Chow test, LPM |
| [ch08](chapters/ch08-heteroskedasticity.md) | Heteroskedasticity | robust SEs, BP/White tests, WLS/FGLS |
| [ch09](chapters/ch09-specification-and-data-issues.md) | More on Specification and Data Issues | RESET, proxy variables, measurement error (CEV) |
| [ch10](chapters/ch10-basic-time-series-regression.md) | Basic Regression Analysis with Time Series Data | TS.1–6, FDL/LRP, trends and seasonality |
| [ch11](chapters/ch11-ols-time-series-further-issues.md) | Further Issues in Using OLS with Time Series Data | TS.1′–5′, I(0)/I(1), dynamic completeness |
| [ch12](chapters/ch12-serial-correlation-heteroskedasticity-time-series.md) | Serial Correlation and Heteroskedasticity in Time Series | BG test, Newey-West, Cochrane-Orcutt/Prais-Winsten |
| [ch13](chapters/ch13-pooling-cross-sections-panel-methods.md) | Pooling Cross Sections across Time: Simple Panel Data Methods | DiD/DDD, FD estimator, FD.1–7 |
| [ch14](chapters/ch14-advanced-panel-data-methods.md) | Advanced Panel Data Methods | FE/RE, Mundlak/CRE, cluster-robust inference |
| [ch15](chapters/ch15-iv-and-2sls.md) | Instrumental Variables Estimation and Two Stage Least Squares | IV conditions, weak instruments, overid/VAT |
| [ch16](chapters/ch16-simultaneous-equations-models.md) | Simultaneous Equations Models | autonomy, order/rank conditions, 2SLS systems |
| [ch17](chapters/ch17-limited-dependent-variable-models.md) | Limited Dependent Variable Models and Sample Selection | logit/probit APE, Tobit, Poisson QMLE, Heckit |
| [ch18](chapters/ch18-advanced-time-series-topics.md) | Advanced Time Series Topics | Dickey-Fuller, cointegration/ECM, forecasting |
| [ch19](chapters/ch19-advanced-causal-inference.md) | Advanced Methods for Causal Inference | ATE/ATT, IPWRA, LATE, RD, control functions |
| [ch20](chapters/ch20-carrying-out-an-empirical-project.md) | Carrying Out an Empirical Project | project workflow, data mining critique, sensitivity |

## Topic Index

- **Adjusted R² / model comparison** → ch06
- **Asymptotic theory (consistency, CLT)** → ch05
- **ATE / ATT / treatment effects** → ch02, ch19
- **Attenuation / measurement error** → ch09
- **Bad controls** → ch03, ch06
- **Binary response (logit, probit, LPM)** → ch07, ch17
- **Censoring / Tobit** → ch17
- **Chow test / interactions** → ch07
- **Cluster-robust SEs** → ch13, ch14
- **Cointegration / ECM** → ch18
- **Count data / Poisson QMLE** → ch17
- **DiD / DDD / parallel trends** → ch13, ch19
- **Duration / survival (Cox, AFT, competing risks, frailty)** → references/survival-duration-models.md (beyond the book)
- **Dummy variables** → ch07
- **Endogeneity (general)** → ch03, ch15, ch16
- **Fixed effects / random effects / Mundlak** → ch14
- **First differencing** → ch13, ch14
- **Forecasting** → ch18
- **Functional form / RESET** → ch06, ch09
- **Heteroskedasticity (robust SE, BP, White, WLS)** → ch08
- **IV / 2SLS / weak instruments** → ch15, ch16
- **LATE / compliers** → ch19
- **Limited dependent variables** → ch17
- **Omitted variable bias / proxy variables** → ch03, ch05, ch09
- **Panel data** → ch13, ch14
- **Prediction intervals / smearing** → ch06
- **Propensity score / IPW / doubly robust** → ch19
- **Regression discontinuity** → ch19
- **Sample selection / Heckit** → ch17
- **Serial correlation (BG, Newey-West, FGLS)** → ch11, ch12
- **Simultaneous equations** → ch16
- **Spurious regression / unit roots** → ch10, ch11, ch18
- **t/F/LM inference** → ch04, ch05
- **Time trends / seasonality / FDL** → ch10
- **Writing an empirical paper** → ch20

## Supporting Files

- [workflow.md](workflow.md) — **the doing layer**: 7-step empirical analysis procedure with completion criteria, assumption rungs, and routing of book-superseded methods
- [diagnostics.md](diagnostics.md) — symptom → test → remedy → recheck for the problems that actually stop an analysis
- [cheatsheet.md](cheatsheet.md) — estimator decision table, tells & smells, thresholds, assumption ladders
- [patterns.md](patterns.md) — estimator recipes and diagnostic techniques
- [glossary.md](glossary.md) — all key terms with definitions
- [references/](references/) — **beyond the book**: synthetic cards for methods Wooldridge 8e does not cover (currently: [survival-duration-models.md](references/survival-duration-models.md))
- [chapters/](chapters/) — the book itself, one file per chapter

---

## Scope & Limits

This skill covers the book content only (8th edition, incl. its Ch-19 causal-inference methods), organized as reference (chapters, cheatsheet, patterns) plus a doing layer (workflow, diagnostics) that turns the theory into procedure.

**Where the book is superseded (registered exceptions, per the Academic Baseline):**
- Staggered / multi-period DiD with heterogeneous effects → `staggered-did` skill (ch13/14's general w_it framework is the flexible starting point, but TWFE is biased under heterogeneity).
- Few clusters (policy varies across a handful of units) → wild cluster bootstrap / randomization inference (beyond the book).
- Modern weak-IV practice → Montiel Olea–Pflueger F ≳ 20 under heteroskedasticity/serial correlation (cheatsheet thresholds).
- Identification-first design audits → `huntington-klein-causal-design`.

**Beyond the book (synthetic reference cards in [references/](references/), clearly marked):** duration/survival models (Cox PH, AFT Weibull, competing risks) → [survival-duration-models.md](references/survival-duration-models.md). Modern ML prediction is not covered — flag it. For Stata execution generally, combine with the `stata` skill.
