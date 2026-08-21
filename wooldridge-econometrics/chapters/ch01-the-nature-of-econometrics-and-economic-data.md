# Chapter 1: The Nature of Econometrics and Economic Data

## Core Idea
Empirical economic analysis turns an economic question into an estimable econometric model and uses nonexperimental data to approximate ceteris paribus causal effects. Everything later in the book — estimation, inference, identification — hangs on whether "enough other factors have been held fixed" and on matching the method to the data structure.

## Frameworks Introduced
- **Steps in empirical economic analysis**: formulate the question → (optionally) build a formal economic model → specify an econometric model (functional form + error term u) → collect data → estimate parameters → test hypotheses as restrictions on parameters (e.g., β₁ = 0) → possibly predict.
  - When to use: every empirical project; this is the default project workflow.
  - How: state the hypothesis in terms of the unknown parameters before touching data; merge economic reasoning into variable selection rather than deriving everything from utility maximization.
- **Economic model → econometric model**: an economic model $y = f(x_1, \dots, x_k)$ leaves f(·) unspecified; the econometric model fixes the form (usually linear) and sweeps unobservables into u, e.g. $wage = \beta_0 + \beta_1 educ + \beta_2 exper + \beta_3 training + u$.
  - When to use: whenever translating theory into an estimating equation.
  - How: choose observable proxies for unobservables (freqarr for arrest probability); acknowledge u can never be eliminated — "dealing with u" is the core of econometrics.
- **Ceteris paribus / counterfactual (potential outcomes) reasoning**: define the causal effect for one unit as the difference in outcomes across two states of the world (treated vs. untreated), holding everything else fixed. Each unit is observed in only one state — that is the estimation problem, separate from the definition of causality.
  - When to use: framing any policy or causal question (job training, minimum wage, police size).
  - How: ask "if the key variable had been assigned independently of other determinants of y, would the comparison be valid?" If yes, simple comparisons identify the effect; if no (as in almost all nonexperimental data), extra assumptions/methods are needed.
- **Data structure taxonomy**: cross-sectional / time series / pooled (repeated) cross section / panel (longitudinal).
  - When to use: before choosing any estimator or inference correction.
  - How: check the unit dimension, whether the same units are re-observed, and whether ordering carries information (see Reference Tables).

## Key Concepts
- **Econometric model**: an economic model made estimable — functional form specified, unobserved factors collected in an error term u.
- **Error term / disturbance (u)**: all unobserved or unmeasured determinants of y (ability, land quality, measurement error); omitted factors live here and drive bias.
- **Ceteris paribus**: holding all other relevant factors fixed while varying one; most economic questions are ceteris paribus by nature.
- **Counterfactual / potential outcomes**: imagining the same unit in two states of the world; causality means the outcomes differ for at least some units.
- **Experimental vs. nonexperimental data**: random-assignment data vs. passively observed (observational/retrospective) data; nonexperimental data dominate economics and make the key variable correlated with u.
- **Random sampling**: drawing units randomly from the population; justifies i.i.d. inference and makes observation order irrelevant.
- **Sample selection problem**: a violation of random sampling where inclusion in the sample depends on the outcome (e.g., wealthier families refuse to report wealth).
- **Cluster sampling**: sample clusters (schools, villages) then units within; outcomes within a cluster are not independent → needs cluster-robust inference (Ch 14).
- **Cross-sectional data**: many units at one point in time; order irrelevant under random sampling.
- **Time series data**: one or few units over time; chronological order conveys information; observations are serially dependent, often trending or seasonal.
- **Pooled (repeated) cross section**: independent random samples from the same population at different times, combined with a time variable; used to study how a relationship changes or to evaluate policy before/after.
- **Panel (longitudinal) data**: the same cross-sectional units followed over multiple periods; enables controlling time-invariant unobserved heterogeneity and studying lagged effects.
- **Data frequency**: daily/weekly/monthly/quarterly/annual; matters for seasonality and persistence.

## Mental Models
- Think of every regression's key regressor as a fertilizer dose: valid only if its assignment was independent of the "land quality" (unobservables) — when the assistant doses better plots more heavily, the yield–fertilizer correlation is spurious (return-to-education ↔ ability is the same story).
- Use the "planner's experiment" test when judging a causal claim: describe the random-assignment experiment that would settle it, then ask how far the actual data fall short of it and why.
- Think of the error term u as a budget line you can never zero out: you can shrink it with controls and proxies, but identification strategy is about what remains inside it.
- Use data structure as the first diagnostic, not the last: the same question (minimum wage → unemployment) implies different methods depending on whether the data are cross-sectional, time series, pooled, or panel.

## Anti-patterns
- **Reading causality from a raw correlation**: e.g., negative class size–score correlation or positive executions–murders correlation; both directions of selection and simultaneity contaminate the comparison (police and crime are simultaneously determined).
- **Ignoring that units self-select the "treatment"**: people choose their education, cities choose police force size, firms choose training — so the key variable is correlated with unobserved determinants of y (the defining feature of nonexperimental data).
- **Treating a pooled cross section as a panel**: different houses sold in 2018 and 2020 are not the same units; no within-unit transformations are possible.
- **Assuming i.i.d. when sampling is clustered or policy is set at a higher level**: students within a school share the intervention; standard errors must account for within-cluster correlation.
- **Analyzing time series as if cross-sectional**: chronological order carries information; trends, seasonality, and serial dependence invalidate naive standard methods.
- **Conflating frequency of measurement with data structure**: growth over 1960–1985 regressed on 1960 characteristics is still a cross section.

## Key Equations & Formulas
Economic model (Becker's crime model):
$$y = f(x_1, x_2, x_3, x_4, x_5, x_6, x_7)$$

Econometric model (general multiple regression form):
$$crime = \beta_0 + \beta_1 wage + \beta_2 othinc + \beta_3 freqarr + \beta_4 freqconv + \beta_5 avgsen + \beta_6 age + u$$

Wage equation:
$$wage = \beta_0 + \beta_1 educ + \beta_2 exper + \beta_3 training + u$$

Hypothesis as parameter restriction: "legal wage has no effect on crime" $\Leftrightarrow \beta_1 = 0$; "job training effect" $\Rightarrow \beta_3$ is the parameter of interest.

## Reference Tables

Data structures at a glance:

| Structure | Units × time | Order matters? | Key feature | Typical use |
| --- | --- | --- | --- | --- |
| Cross-sectional | many units, one time | no (random sampling) | may have timing spread within period; ordering irrelevant | micro labor/IO/public finance |
| Time series | one/few units, many times | yes (chronological) | serial dependence, trends, seasonality | macro, finance, forecasting |
| Pooled cross section | independent samples, several times | no, but track year | combines periods; relationship may change over time | policy before/after comparisons |
| Panel | same units, several times | within-unit time order yes; cross-section order no | repeated units → control time-invariant unobservables | causal inference, dynamics |

Violations of random sampling:

| Violation | Mechanism | Consequence | Where treated |
| --- | --- | --- | --- |
| Sample selection | inclusion depends on outcome (wealth nonresponse) | sample not representative | Ch 17 |
| Cluster sampling | clusters sampled, then units within | within-cluster correlation | Ch 14 (cluster-robust inference) |
| Policy set at cluster level | treatment constant within school/state | policy variable correlated within cluster | Ch 14 |
| Geographic spillovers | nearby counties' policies correlated | cross-unit dependence | advanced; deferred |

## Worked Example
**Return to education (Example 1.4).** Question: if a person is given one more year of education, how much does the wage rise, ceteris paribus? The ideal experiment: a social planner randomly assigns education levels and observes wages — education would then be independent of other wage determinants, and a simple comparison identifies the effect. The available data are nonexperimental survey data (e.g., WAGE1: 526 workers, 1976) where people choose their own schooling. Education is therefore correlated with experience (more schooling → later labor-market entry; measurable, like rainfall in the fertilizer experiment) and with innate ability (unobservable, like land quality). Model: $wage = \beta_0 + \beta_1 educ + \beta_2 exper + \beta_3 training + u$, with ability inside u. Interpretation: controlling observables like experience is straightforward (Ch 3 onward); dealing with unobservable ability is the hard problem that motivates IV and panel methods later. The parallel Example 1.5 (police–crime) adds simultaneity: cities with more crime hire more police, so a positive raw correlation says nothing about deterrence.

## Key Takeaways
1. Always state the research question in ceteris paribus terms and the hypothesis as a restriction on a parameter (β₁ = 0) before estimating anything.
2. The econometric model = economic model + specified functional form + error term u; what sits inside u determines the identification threat.
3. Judge causal credibility by the counterfactual experiment test: would random assignment of the key variable make the comparison valid? How far short do the data fall?
4. Observable confounders (experience) are fixable with controls; unobservable confounders (ability) require IV, panel, or experimental variation — most econometric advances target exactly this.
5. Classify the data structure first: it determines admissible estimators, whether ordering matters, and which inference corrections (serial correlation, clustering) are required.
6. Panel data's distinctive payoff is controlling time-invariant unobserved heterogeneity — causal inference impossible from a single cross section.
7. Simultaneity (police ↔ crime) and self-selection (education, training) are the two recurring reasons nonexperimental correlations are not causal effects.

## Connects To
- **Ch 2**: justifies why random assignment makes the simple regression of y on the treatment identify the ceteris paribus effect (SLR assumptions, zero conditional mean).
- **Ch 13–14**: pooled cross sections and panel methods; cluster-robust inference for clustered sampling and cluster-level policies.
- **Ch 16**: simultaneous equations models for the police–crime simultaneity problem.
- **Ch 17**: sample selection corrections.
- **Ch 10–12**: time series trends, seasonality, and serial correlation.
- **DAG / potential-outcomes framework (Huntington-Klein)**: this chapter's counterfactual reasoning is Wooldridge's informal version of the Rubin causal model.
