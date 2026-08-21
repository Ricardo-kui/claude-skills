# Chapter 20: Carrying Out an Empirical Project

## Core Idea
A credible empirical project runs from a precisely posed, data-answerable question through deliberate data collection and cleaning, a justified separation of model and estimation method, sensitivity analysis that avoids data mining, to a transparently structured paper. The t and F inference the whole book rests on assumes one model estimated once on one sample — every specification search erodes that foundation.

## Frameworks Introduced
- **Posing a question**: a specific question answerable with data, in an area where data sources exist within the allotted time.
  - When to use: before any data collection. Test: can you say "I'm studying the effects of community policing on city crime rates" rather than "my paper is on crime"?
  - How: pick a field, search the literature (JEL codes, EconLit, Social Sciences Citation Index, Google Scholar), confirm data exist, then collect.
- **Data structure choice**: cross-section, time series, pooled cross sections, or panel, matched to the question.
  - When to use: at project design. Panel data on the same units over time lets you control for time-constant unobserved effects (fixed effect $a_i$) that confound a single cross section.
  - How: ask whether a single cross section permits convincing ceteris paribus analysis; if not, seek panel data, natural experiments, or IVs.
- **Model vs. estimation method**: a model is a population relationship; OLS, WLS, FGLS, 2SLS are methods for estimating it.
  - When to use: in the models-and-methods section of any paper.
  - How: write population equations with no hats on the $\beta_j$, then justify why the chosen estimator is valid (exogeneity, instrument validity, panel transformation). Never write "an OLS model."
- **Sensitivity analysis**: re-estimate under reasonable modifications — alternative measures, dropped outliers, different functional forms.
  - When to use: after the main results, before writing conclusions.
  - How: a conclusion significant in only a small fraction of reasonable specifications is likely spurious; dropping variables is justified via an F test, not by significance-hunting.
- **Panel data options with $T \geq 2$**: pooled OLS, lagged dependent variable, first differencing, fixed effects, possibly combined with IV.
  - When to use: whenever panel data are available.
  - How: apply several reasonable methods and compare — divergence reveals which identifying assumption is likely false. With $T = 2$, FE = differencing.

## Key Concepts
- **Data mining / specification search**: estimating model variants on the same data until results look "good"; invalidates the unbiasedness results and t/F distributions, which assume the model is estimated once.
- **Stepwise regression**: automated forward/backward variable selection by p-values; a severe form of data mining whose final model depends on drop/add order — t and F statistics in it are uninterpretable.
- **Self-selection**: units sort into treatment based on unobservables (e.g., families with a taste for saving open IRAs), endogeneity that controls alone may not fix.
- **Phantom observations**: bogus rows created by differencing panel data across unit boundaries (1992 value of city $i$ minus 1997 value of city $i-1$); ensure the first period is missing for all differenced variables.
- **Missing-value codes**: numeric sentinels (-99, 999) treated as real data by software; recode to a nonnumeric missing indicator before computing anything.
- **Ordinal variable misuse**: raw occupation codes or a 1–7 satisfaction scale entered linearly impose quantitative meaning that does not exist; use dummy sets, or ordered probit/logit for ordinal dependent variables.
- **Hedonic price model**: regression of price on characteristics (e.g., house value on size, rooms) — descriptive, useful as a baseline, weak as a contribution.
- **Natural experiment / RDD setting**: arbitrary cutoffs (poverty-rate thresholds, election results, composite scores) that generate treatment/control near the cutoff.

## Mental Models
- Think of the project as a funnel: question → data structure → data cleaning → population model → estimator → sensitivity → paper. Skipping a stage corrupts everything downstream.
- Use min/max/mean/SD as a lie detector when inheriting any dataset: min education = -99 reveals the missing code; mean conviction rate = 0.632 reveals proportions, not percentages; a proportion above 1 flags mixed coding.
- Think of the unobserved effect $a_i$ as the reason panel data exist: if it is correlated with regressors, no cross-sectional control set fully rescues OLS.
- Use "would a reader believe this identifying assumption?" as the filter when choosing between OLS, IV, RDD, and panel methods — then run several and compare.

## Anti-patterns
- **Collecting data before posing the question**: leads to missing key variables, the wrong population, or the wrong time period.
- **Differencing an unsorted panel**: creates phantom observations; always order chronologically within unit and set the first period to missing.
- **Leaving numeric missing codes in the data**: software treats -99 as data, silently distorting every estimate.
- **Entering categorical codes as numeric regressors**: a one-unit increase in occupation code means nothing; build dummies.
- **Saying "an OLS model"**: conflates the population model with the estimation method; every model admits several estimators.
- **Searching specifications until significant, then reporting only that one**: invalidates t/F inference; a variable significant in a small fraction of specifications probably has no population effect.
- **Using log(1 + x) for zero-valued regressors**: not invariant to units of measurement and lacks a clean interpretation.
- **Reporting coefficients in scientific notation or 8 decimals**: rescale units; false precision misleads.

## Key Equations & Formulas
Population model (no hats; cross-sectional):

$$colGPA = \beta_0 + \beta_1 alcohol + \beta_2 hsGPA + \beta_3 SAT + \beta_4 female + u$$

Time-series model with distributed lags:

$$thefts_t = \beta_0 + \beta_1 unem_t + \beta_2 unem_{t-1} + \beta_3 cars_t + \beta_4 convrate_t + \beta_5 convrate_{t-1} + u_t$$

Per-capita scaling, two equivalent ways — restricted:

$$\log(div/pop) = \beta_0 + \beta_1 mlb + \beta_2 perCath + \beta_3 \log(inc/pop) + \dots$$

unrestricted (nested test of the population effect):

$$\log(div) = \gamma_0 + \gamma_1 mlb + \gamma_2 perCath + \gamma_3 \log(inc) + \gamma_4 \log(pop) + \dots, \quad \gamma_4 = 1 - \beta_3 \text{ under the restriction}$$

Panel model with unobserved effect (remove $a_i$ by differencing or time-demeaning):

$$\log(manuf_{it}) = \beta_0 + \delta_1 d87_t + \delta_2 d92_t + \beta_1 tax_{it} + \dots + a_i + u_{it}$$

Estimated equation reported with standard errors below:

$$\widehat{\log(salary)} = 2.45 + 0.236\log(sales) + 0.008\,roe + 0.061\,ceoten,\qquad n = 204,\ R^2 = 0.351$$

## Reference Tables

Empirical paper architecture (20-5):

| Section | Must contain |
|---|---|
| Introduction | Objectives, importance, brief literature, possibly a motivating table/graph; may summarize findings |
| Conceptual framework | Economic theory or intuitive discussion guiding variable choice and control set |
| Econometric models & methods | Population equations (no hats), functional form choices, estimator justification, IV validity argument |
| Data | Sources (reproducible), units, variable-definition table, summary statistics table, observation counts per year/unit |
| Results | Estimates in equation or table form, SEs in parentheses, $R^2$ and $n$ always, magnitudes and economic vs. statistical significance, method comparisons |
| Conclusions | Key magnitude, caveats, directions for further research |

Data inspection checklist (20-3c):

| Check | What it catches |
|---|---|
| Missing-value coding | -99/999 treated as real data |
| Units and nominal vs. real dollars | Scale and base-year confusion |
| Percentage vs. proportion | Mixed entries (e.g., 0.632 and 63.2 in one column) |
| Chronological order + time indicators | Garbage differencing; seasonality/trends |
| Panel unit identifier + adjacency | Phantom observations |
| Min/max/mean/SD of key variables | Typos, outliers, coding errors |

## Worked Example
Alcohol consumption and college GPA (Eq. 20.1). Question: does drinking lower GPA, ceteris paribus? Model: $colGPA = \beta_0 + \beta_1 alcohol + \beta_2 hsGPA + \beta_3 SAT + \beta_4 female + u$ for the population of undergraduates at one university. Endogeneity concern: unobserved factors in $u$ (motivation, family environment) correlate with drinking, so OLS needs a defense. Candidate IV: $dorm$ (lives in dormitory) — valid only if dorm residence has no direct effect on GPA and is uncorrelated with $u$ (both assumed), and is partially correlated with alcohol, which is testable by regressing alcohol on dorm, hsGPA, SAT, female. Estimation: OLS under exogeneity, 2SLS otherwise; report both and comment on differences. Sensitivity: replace the alcohol quantity measure with a binary usage dummy — if only the dummy is significant, usage may proxy an unobserved attribute rather than a dose effect.

## Key Takeaways
1. Pose the specific question and confirm data exist before collecting anything; a vague topic guarantees the wrong variables, population, or period.
2. Audit every inherited dataset: recode numeric missing sentinels, verify units, proportions vs. percentages, nominal vs. real dollars, and chronological/panel ordering.
3. Write the population model and the estimation method as separate objects; justify the estimator against the four endogeneity sources (omitted variables, self-selection, measurement error, simultaneity).
4. With panel data, run several reasonable methods (pooled OLS, lagged DV, FD, FE) — agreement across them is itself evidence.
5. Sensitivity analysis yes, data mining no: report the specification grid honestly; results significant in only a few specifications are likely spurious.
6. Every results table needs $R^2$, $n$, and SEs in parentheses; distinguish economic from statistical significance; never use scientific notation.
7. Structure the paper so a reader could redo the analysis: full data sources, variable definitions, and summary statistics.

## Connects To
- **Ch 13/14**: pooled cross sections, first differencing, fixed effects — the panel options this chapter weighs.
- **Ch 15/16**: IV/2SLS validity requirements invoked in the alcohol-GPA example.
- **Ch 19**: RDD and natural experiments as design options at the question-posing stage.
- **Ch 6**: functional form guidelines (logs, quadratics, interactions) and the log(1+x) pitfall.
- **Ch 8/12**: heteroskedasticity-robust inference and serial-correlation corrections as estimator variants.
- **xianzhu-skill / empirical-intake**: this chapter's anti-data-mining stance is the book-level justification for locked designs and documented specification searches.
