---
name: wooldridge-econometrics
description: "Wooldridge 计量经济学知识库（Introductory Econometrics, 8th ed.）：估计量选择与辩护、识别假设检查、诊断与补救。Use when choosing/defending an estimator (OLS, IV/2SLS, FE/RE, DiD, RD, logit/Tobit/Heckit), checking identifying assumptions (MLR/TS/FD/ATE ladders), diagnosing heteroskedasticity, serial correlation, endogeneity, weak instruments, or running treatment-effect/panel analyses. 触发词：Wooldridge、计量经济学、回归假设、工具变量、弱工具变量、双重差分、固定效应、随机效应、异方差、序列相关、单位根、时间序列回归、样本选择、稳健标准误、内生性、处理效应、estimator choice、identifying assumptions、Heckman selection、unit root、cointegration"
---

<!-- argument-hint: [topic, estimator name, or chapter number] -->

# Introductory Econometrics: A Modern Approach (8th ed.)
**Author**: Jeffrey M. Wooldridge | **Pages**: ~940 | **Chapters**: 20 | **Generated**: 2026-08-21

## How to Use This Skill

Topic or chapter question → find it in the Topic Index or Chapter Index below, read that chapter file before answering. Estimator-choice or diagnostic question → start from [cheatsheet.md](cheatsheet.md) and [patterns.md](patterns.md). Every answer should name the assumption rung it rests on (e.g. "unbiased under MLR.1–4").

---

## Core Frameworks & Mental Models

**Everything is an assumption ladder.** Each estimator's credibility comes from a numbered assumption set; learn what each rung buys (full ladder table in [cheatsheet.md](cheatsheet.md)). When a claim fails, name the rung that failed — that is the diagnosis.

**Zero conditional mean is the whole game (Ch 2–3).** E(u|x)=0 separates description from causation. Omitted variable bias: Bias(β̃₁) = β₂δ̃₁ — sign it with the Table 3.2 matrix before running anything. Use partialling out (Frisch-Waugh) to explain what any control actually does.

**Ceteris paribus first, estimator second (Ch 1, 20).** Write the population model (no hats) and state the counterfactual question; OLS/WLS/2SLS/FE are competing estimators of that model, never "models" themselves. There is no such thing as "an OLS model."

**Bad controls are worse than no controls (Ch 3, 6).** Never hold fixed mediators, colliders, or components of the outcome. Add controls that are treatment-uncorrelated only to shrink error variance. "Control for everything" is not a strategy.

**R² is not evidence (Ch 2, 3, 10).** High R² between trending series is spurious; low R² with an unbiased causal coefficient is fine. Compare nonnested models with adjusted R²; never select for significance.

**Robust inference by default (Ch 8, 12).** Cross-sections: White/robust SEs always; BP or special White test only as diagnostics. Time series: Breusch-Godfrey test, then Newey-West/HAC (safe, needs only contemporaneous exogeneity) — reach for FGLS (Cochrane-Orcutt/Prais-Winsten) only under strict exogeneity, and if OLS≠FGLS, keep OLS.

**Panel data trades assumptions for variation (Ch 13–14).** FD at T=2 ≡ DiD; FE (within) is the default for T≥2, RE only if Cov(x,aᵢ)=0 — test with Mundlak/CRE (add time-averages, F-test γ=0). Always cluster by unit. Strict exogeneity fails with lagged dependent variables and feedback.

**IV is an argument, not a command (Ch 15–16).** Exogeneity (Cov(z,u)=0) is untestable — you must argue it; relevance is testable — first-stage |t|>3.2 / F>10. Run 2SLS in software (manual two-step gives wrong SEs). Diagnose with VAT/control-function and overid tests. SEMs additionally need autonomy: each equation must have its own ceteris paribus interpretation.

**Potential outcomes unify causal inference (Ch 2, 19).** ATE/ATT under unconfoundedness (ATE.1) + overlap (ATE.2): RA → IPW → IPWRA (doubly robust), trim p̂∉[0.1,0.9]. IV without unconfoundedness gives LATE on compliers. RD gives local effects at the cutoff (local linear, IK bandwidth; fuzzy RD = IV). DiD needs parallel trends — show pre-trends or add a control dimension (DDD).

**Match the estimator to the limited dependent variable (Ch 17).** Binary → LPM (robust) or logit/probit, report APEs not coefficients. Counts/corners → Poisson QMLE with exp-mean and robust SEs; never log(1+y). True censoring → Tobit with Φ-scaled partial effects. Selected sample → Heckit with a real exclusion restriction.

**Persistence changes everything in time series (Ch 11, 18).** ρ̂ > 0.9 ⇒ treat as I(1): difference or use growth rates. Levels regressions of I(1) series are spurious unless cointegrated (Engle-Granger test → ECM). Forecast out-of-sample with RMSE/MAE; never trend-extrapolate a random walk.

**Specification search discipline (Ch 9, 20).** RESET for functional form; proxy variables and plug-in solutions for OVB; CEV in x attenuates. t/F inference assumes one model estimated once — stepwise selection is data mining; run sensitivity grids and report them all.

---

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

- [glossary.md](glossary.md) — all key terms with definitions
- [patterns.md](patterns.md) — estimator recipes and diagnostic techniques
- [cheatsheet.md](cheatsheet.md) — estimator selection table, tells & smells, thresholds

---

## Scope & Limits

This skill covers the book content only (8th edition, incl. its Ch-19 causal-inference methods). For modern staggered-DiD estimators beyond the book, combine with the `staggered-did` skill; for identification-first design audits, `huntington-klein-causal-design`; for Stata execution, the `stata` skill. For topics beyond this book, check related skills or ask the agent directly.
