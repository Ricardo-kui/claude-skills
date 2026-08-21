# Chapter 16: Simultaneous Equations Models

## Core Idea
When a regressor is jointly determined with the outcome in equilibrium (price–quantity, police–crime, wage–hours), OLS on a structural equation is biased and inconsistent; an identified equation must be screened by the order/rank conditions on exclusion restrictions and then estimated by 2SLS using all exogenous variables in the system as instruments.

## Frameworks Introduced
- **Autonomy requirement**: each equation in an SEM must have its own ceteris paribus, causal interpretation.
  - When to use: before writing any SEM — test whether an SEM is warranted at all.
  - How: ask a counterfactual ("what would $y_1$ be if $y_2$ were different?") for each equation. Fails when the *same agent* chooses both variables (household's housing vs. saving; firm's price vs. advertising).
- **Rank condition for identification**: the first equation in a two-equation SEM is identified iff the second equation contains at least one exogenous variable (with nonzero coefficient) excluded from the first.
  - When to use: every structural equation before estimation.
  - How: (1) check the order condition (count exclusions); (2) estimate the reduced form for the endogenous regressor and run a t/F test that the excluded variable(s) matter.
- **2SLS estimation of SEM equations**: instruments = exogenous variables appearing anywhere in the system.
  - When to use: any identified equation, cross-section, time series, or panel.
  - How: `ivregress 2sls y1 (y2 = z_excluded) z_own` in Stata; endogeneity, overidentification, heteroskedasticity, and serial-correlation tests carried over from Ch. 15.
- **Panel SEM (two-step)**: (1) first-difference or time-demean each structural equation to remove the unobserved effect; (2) apply pooled 2SLS to the transformed equation with time-varying instruments.
  - When to use: simultaneity plus unobserved heterogeneity in panel data.
  - How: `ivregress 2sls D.y1 (D.y2 = D.z_iv) D.z_own i.year`, or `xtivreg, fe`; instruments must vary over time within unit.

## Key Concepts
- **Simultaneous equations model (SEM)**: a system in which endogenous variables are jointly determined by an equilibrium condition (e.g., supply = demand).
- **Structural equation**: an equation derived from economic behavior with a ceteris paribus interpretation; its errors are the **structural errors** and its coefficients the **structural parameters**.
- **Reduced form equation**: an endogenous variable expressed as a linear function of all exogenous variables and structural errors; its coefficients are nonlinear functions of the structural parameters. Reduced forms are estimable by OLS.
- **Exclusion restrictions**: assuming certain exogenous variables appear in one equation but not another — the identifying variation of an SEM.
- **Order condition** (necessary only): # excluded exogenous variables ≥ # right-hand-side endogenous variables.
- **Simultaneity bias**: bias/inconsistency of OLS because the jointly determined regressor is correlated with the structural error (via the reduced-form error).
- **Predetermined variable**: a lagged endogenous (or lagged exogenous) variable, usable as an instrument when the error is uncorrelated with all past variables.
- **Heterogeneity vs. idiosyncratic endogeneity**: in panel SEMs, correlation of regressors with the unit effect $a_i$ (fixed by FD/FE) vs. with the time-varying error $u_{it}$ (needs IVs).

## Mental Models
- Use an **SEM** when different equations describe different agents or different sides of a market (supply/demand, murderers/city officials); reach for single-equation OLS or IV instead when one agent chooses both variables.
- Think of the **reduced form** as the observable surface of the system: you can always estimate it, and a structural equation is identified exactly when excluded shifters in the reduced form trace it out.
- Think of identification as **market geometry**: an exogenous supply shifter traces out the demand curve; an exogenous demand shifter traces out the supply curve. No observed shifter → no estimation.
- Use **FD/FE + IV as orthogonal fixes**: differencing kills heterogeneity endogeneity; instruments kill simultaneity. Panel SEMs need both because they have two error components.

## Anti-patterns
- **Using an SEM for two variables chosen by the same agent**: housing vs. saving, study hours vs. work hours — neither equation has a ceteris paribus interpretation, and without sensible exclusions the equations are indistinguishable and unidentified.
- **Assuming joint determination implies an SEM**: simultaneity is necessary, not sufficient; autonomy is required.
- **Trusting the order condition alone**: it is only necessary. An excluded variable with a zero coefficient in the other equation ($\beta_{34} = 0$ in the three-equation example) provides no identifying variation — verify the rank condition with a reduced-form t/F test.
- **Running OLS on a structural equation**: the endogenous regressor's reduced-form error contains $u_1$, so OLS is biased and inconsistent; in the police–murder example the bias is positive, understating police effectiveness.
- **Time-constant instruments in a differenced panel SEM**: a level instrument is uncorrelated with changes (e.g., $\Delta exper_{it} = 1$ for all workers — useless). Instruments must vary over time.
- **Estimating static aggregate SEMs in levels**: trending I(1) series (consumption, income, interest rates) violate weak dependence; respecify in growth rates or first differences.

## Key Equations & Formulas
Two-equation structural model:
$$y_1 = \alpha_1 y_2 + \beta_1 z_1 + u_1, \qquad y_2 = \alpha_2 y_1 + \beta_2 z_2 + u_2$$
Reduced form for $y_2$ (exists iff $\alpha_2\alpha_1 \neq 1$):
$$y_2 = \pi_{21} z_1 + \pi_{22} z_2 + v_2, \qquad v_2 = (\alpha_2 u_1 + u_2)/(1-\alpha_2\alpha_1)$$
Direction of OLS asymptotic bias for $\alpha_1$ (simple case, $\operatorname{Cov}(u_1,u_2)=0$):
$$\operatorname{Cov}(y_2, u_1) = \frac{\alpha_2}{1-\alpha_2\alpha_1}\,\sigma_1^2$$
Panel SEM in first differences:
$$\Delta y_{it1} = \alpha_1 \Delta y_{it2} + \Delta \mathbf{z}_{it1}\boldsymbol{\beta}_1 + \Delta u_{it1}$$
FE (time-demeaned) variant, pooled 2SLS with corrected $df = N(T-1) - k_1$:
$$\ddot{y}_{it1} = \alpha_1 \ddot{y}_{it2} + \ddot{\mathbf{z}}_{it1}\boldsymbol{\beta}_1 + \ddot{u}_{it1}$$

## Reference Tables

| Equation type (by order condition) | Excluded exog. vars vs. RHS endog. | Estimable by 2SLS? |
|---|---|---|
| Unidentified | fewer excluded than RHS endogenous | No |
| Just identified | exactly equal | Yes (one IV per endog.) |
| Overidentified | more excluded than RHS endogenous | Yes; # overidentifying restrictions = total exogenous in system − total explanatory vars in equation; testable (Ch. 15) |

| Identification check | Statement | Status |
|---|---|---|
| Order condition | # excluded exogenous ≥ # RHS endogenous | Necessary |
| Rank condition | ≥1 excluded exogenous has nonzero coefficient in the other equation | Necessary and sufficient; test via t/F in reduced form |

| Data type | Recipe |
|---|---|
| Cross-section | 2SLS per identified equation; IVs = all system exogenous vars |
| Time series | Lagged values as IVs if $E(u_t \mid I_{t-1}) = 0$; work in growth rates if I(1); test AR(1) via lagged 2SLS residual (its own instrument) |
| Panel | FD or time-demean each equation, then pooled 2SLS with time-varying IVs; cluster-robust SEs |

## Worked Example
**Effect of prison population on violent crime (Levitt 1996; Example 16.8).** Question: does expanding prison population reduce violent crime at the state level? Fixed-effects model in logs, first-differenced: $\Delta\log(crime_{it}) = \xi_t + \alpha_1 \Delta\log(prison_{it}) + \Delta\mathbf{z}_{it1}\boldsymbol{\beta}_1 + \Delta u_{it1}$, 51 states × 14 years (1980–1993, PRISON). Simultaneity: more crime induces more incarceration, so OLS is inconsistent. Instruments: prison overcrowding litigation — dummies for a final decision reached one or two years earlier (plausibly exogenous shifters of prison growth). Results: pooled OLS $\hat\alpha_1 = -0.181$ (se 0.048); pooled 2SLS $\hat\alpha_1 = -1.032$ (se 0.370) — the causal deterrent effect is nearly six times larger than OLS suggests, though much less precise. AR(1) test on differenced residuals: coefficient 0.076 (t = 1.67), so serial independence is acceptable.

## Key Takeaways
1. The SEM question comes before the estimation question: use an SEM only when each equation has a ceteris paribus interpretation of its own (autonomy requirement).
2. OLS on a structural equation is biased and inconsistent; in simple systems you can sign the bias via $\alpha_2/(1-\alpha_2\alpha_1)$.
3. Identification = exclusion restrictions + nonzero coefficients elsewhere in the system; screen with the order condition, verify with a reduced-form t/F test (rank condition).
4. Estimate each identified equation by 2SLS using all exogenous variables in the system as instruments; all Ch. 15 diagnostics (endogeneity, overidentification, weak instruments) apply unchanged.
5. In time series SEMs, lagged variables are valid instruments only under $E(u_t \mid I_{t-1}) = 0$; specify systems in growth rates when series are I(1).
6. In panel SEMs, difference/demean to remove the unobserved effect, then instrument with variables that change over time — this handles heterogeneity endogeneity and simultaneity simultaneously.
7. 2SLS estimates can dwarf OLS in magnitude (crime–prison: −1.03 vs. −0.18): attenuation or bias toward zero in OLS is not a reason to trust the smaller number.

## Connects To
- **Ch 15 (IV/2SLS)**: mechanics, endogeneity and overidentification tests, weak instruments, 2SLS with serial correlation — the SEM chapter is an application layer on top.
- **Ch 11 / Ch 18 (time series, unit roots)**: weak dependence and I(1) concerns for aggregate SEMs; cointegration as the modern alternative.
- **Ch 13–14 (FD/FE panel methods)**: the differencing/demeaning step of panel SEMs and the distinction between heterogeneity and idiosyncratic endogeneity.
- **Ch 17 (limited dependent variables)**: sample selection issues when equilibrium quantities are only observed for participants (e.g., wage offers only for working women).
