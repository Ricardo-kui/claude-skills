# Chapter 10: Basic Regression Analysis with Time Series Data

## Core Idea
OLS extends to time series data under Gauss-Markov assumptions TS.1–TS.5 that parallel the cross-sectional case — but temporal ordering kills random sampling, so you must explicitly assume the error is uncorrelated with regressors in **all** periods (strict exogeneity) and uncorrelated across time (no serial correlation). Handle trends and seasonality inside the regression with a time trend and seasonal dummies, or you invite spurious regression.

## Frameworks Introduced
- **Static model**: $y_t = \beta_0 + \beta_1 z_t + u_t$ — contemporaneous relationship; $\beta_1$ is the immediate effect or tradeoff between y and z.
  - When to use: modeling an immediate-effect relationship (static Phillips curve, murder rate on conviction rate).
- **Finite distributed lag (FDL) model of order q**: $y_t = \alpha_0 + \delta_0 z_t + \delta_1 z_{t-1} + \dots + \delta_q z_{t-q} + u_t$.
  - When to use: effects of z on y arrive with delay (tax exemption → fertility).
  - How: plot the estimated lag distribution $\hat\delta_j$ vs. $j$; compute cumulative effects $\delta_0+\dots+\delta_h$ and the LRP (sum of all $\delta_j$). To get a standard error for the LRP, reparameterize with $\theta_0 = \delta_0+\delta_1+\delta_2$ and regress $y_t$ on $z_t$, $(z_{t-1}-z_t)$, $(z_{t-2}-z_t)$ — the coefficient and SE on $z_t$ give $\hat\theta_0$ and its SE directly (in Stata: `reg y z d1z d2z` or `lincom` on the unrestricted regression).
- **Time series CLM assumptions (TS.1–TS.6)**: see Reference Tables. TS.1–TS.3 → unbiasedness; TS.1–TS.5 → OLS BLUE with usual variance formulas (Gauss-Markov); TS.1–TS.6 → exact t/F inference at any sample size.
- **Event study**: $R_t^f = \beta_0 + \beta_1 R_t^m + \beta_2 d_t + u_t$, with market return controlling for broad movements; multiple dummies before/after an announcement detect anticipation effects.
- **Trend/seasonality handling**: include $t$ (or $t, t^2$) and/or seasonal dummies as regressors. By frisch-waugh-lovell partialling out, the slope coefficients equal those from regressing linearly detrended (or deseasonalized) $\ddot{y}_t$ on detrended $\ddot{x}_t$ series.

## Key Concepts
- **Stochastic process / time series process**: a sequence of random variables indexed by time; a data set is one realization, and the number of time periods is the sample size.
- **Impact propensity (impact multiplier)**: $\delta_0$, the immediate change in y from a one-unit temporary increase in z.
- **Lag distribution**: the $\delta_j$ graphed against lag j; traces y's response over time to a temporary shock.
- **Long-run propensity (LRP) / long-run multiplier**: $\delta_0+\delta_1+\dots+\delta_q$, the total change in y after a permanent one-unit increase in z.
- **Contemporaneously exogenous**: $E(u_t|\mathbf{x}_t)=0$ — error uncorrelated with same-period regressors only; sufficient for consistency (Ch. 11), not unbiasedness.
- **Strictly exogenous**: $E(u_t|\mathbf{X})=0$ — error uncorrelated with regressors in every period; rules out feedback from y to future x.
- **Serial correlation / autocorrelation**: correlation in errors across time; violates TS.5 and invalidates usual standard errors.
- **Spurious regression problem**: a significant relationship between trending variables that exists only because both grow over time.
- **Index number**: an aggregate measure (IIP, CPI) meaningful only relative to its base period and base value; used to deflate nominal to real dollars.
- **Detrending / deseasonalizing**: removing a trend (via residuals from regression on t) or seasonal factors (via residuals from regression on seasonal dummies) before analysis.

## Mental Models
- Think of a time series sample as **one realization of a stochastic process**, not a random draw — history cannot be re-run, so "population" = the set of all possible realizations.
- Use **TS.3 as a feedback detector**: if a regressor responds to past outcomes (Fed policy rule reacting to past GDP growth; city police staffing reacting to past murder rates), strict exogeneity fails and OLS is biased. Ask "could x tomorrow react to u today?"
- Think of **including t in a regression as detrending every series first** (Frisch-Waugh interpretation): coefficients then measure how deviations about trends comove.
- Treat a **high R-squared in a trending regression as inflated**: SST overstates the variance of a trending y. Detrend y first, then compute R-squared to see what the x's really explain.

## Anti-patterns
- **Omitting a time trend when y and x both trend**: induces omitted-variable bias and spurious relationships (housing investment on price: elasticity flips from +1.24 significant to −0.38 insignificant once t is added).
- **Stopping at contemporaneous exogeneity for unbiasedness**: $E(u_t|\mathbf{x}_t)=0$ alone does not make OLS unbiased in time series; you need strict exogeneity against all periods' regressors.
- **Reading fit from the usual R-squared with a trending dependent variable**: SST/(n−1) is not a consistent estimator of Var(y) when E(y) trends; report R-squared from the detrended regression instead.
- **Ignoring serial correlation and using textbook SEs**: TS.5 is pervasively violated in time series; usual t and F statistics become unreliable (testing and remedies are Chapter 12).
- **Overfitting trends**: piling on high-order polynomial trend terms tracks any series but says nothing about which explanatory variables affect y.
- **Regressing nominal variables when behavior responds to real ones**: deflate with a price index first; the restriction that only real wages matter is testable as $\beta_2 = -\beta_1$ in the log-nominal decomposition.

## Key Equations & Formulas
FDL of order q and LRP:
$$y_t = \alpha_0 + \delta_0 z_t + \delta_1 z_{t-1} + \dots + \delta_q z_{t-q} + u_t, \qquad \mathrm{LRP} = \delta_0 + \delta_1 + \dots + \delta_q$$

Strict exogeneity (TS.3):
$$E(u_t \mid \mathbf{X}) = 0,\quad t = 1, 2, \dots, n$$

OLS sampling variance under TS.1–TS.5 (identical form to cross-section):
$$\mathrm{Var}(\hat\beta_j \mid \mathbf{X}) = \sigma^2 / \big[\mathrm{SST}_j (1 - R_j^2)\big], \qquad \hat\sigma^2 = \mathrm{SSR}/(n-k-1)$$

Linear and exponential (log) trends:
$$y_t = \alpha_0 + \alpha_1 t + e_t \qquad \log(y_t) = \beta_0 + \beta_1 t + e_t \;\Rightarrow\; \beta_1 \approx \text{per-period growth rate}$$

Rebase an index; deflate to real terms:
$$\text{newindex}_t = 100\,(\text{oldindex}_t / \text{oldindex}_{\text{newbase}}), \qquad \text{real wage} = w/p,\; p = \mathrm{CPI}/100$$

Detrended R-squared (with $\ddot{y}_t$ = residuals of y on trend; same SSR as the regression with trend included):
$$R^2_{\text{detrended}} = 1 - \frac{\mathrm{SSR}}{\sum_{t=1}^n \ddot{y}_t^{\,2}}$$

Monthly seasonality (January base; test no-seasonality H₀: $\delta_1=\dots=\delta_{11}=0$ by F test):
$$y_t = \beta_0 + \delta_1 feb_t + \delta_2 mar_t + \dots + \delta_{11} dec_t + \beta_1 x_{t1} + \dots + \beta_k x_{tk} + u_t$$

## Reference Tables

CLM assumptions for time series regression:

| Assumption | Statement | Needed for |
|---|---|---|
| TS.1 Linear in Parameters | $y_t = \beta_0 + \beta_1 x_{t1} + \dots + \beta_k x_{tk} + u_t$ as a stochastic process, $t=1,\dots,n$ | unbiasedness |
| TS.2 No Perfect Collinearity | No regressor constant or a perfect linear combination of others (in sample and process) | unbiasedness |
| TS.3 Zero Conditional Mean | $E(u_t \mid \mathbf{X}) = 0$ for all t — strict exogeneity; replaces MLR.4 and removes the need for MLR.2 random sampling | unbiasedness |
| TS.4 Homoskedasticity | $\mathrm{Var}(u_t \mid \mathbf{X}) = \sigma^2$ for all t | BLUE + usual variances |
| TS.5 No Serial Correlation | $\mathrm{Corr}(u_t, u_s \mid \mathbf{X}) = 0$, all $t \neq s$ | BLUE + usual variances |
| TS.6 Normality | $u_t$ independent of X, i.i.d. Normal$(0, \sigma^2)$; implies TS.3–TS.5 | exact t/F inference |

Exogeneity hierarchy: strict (TS.3) ⊃ sequential $E(u_t|\mathbf{x}_t,\mathbf{x}_{t-1},\dots,\mathbf{x}_1)=0$ ⊃ contemporaneous $E(u_t|\mathbf{x}_t)=0$.

## Worked Example
**Do antidumping filings reduce imports? (Krupp & Pollard 1996, barium chloride from China).** Event study on monthly data, Feb 1978–Dec 1988 (n = 131). Regress log(chnimp) on log(chempi), log(gas), log(rtwex) and three event dummies: befile6 (6 months before filing), affile6 (6 months after filing), afdec6 (6 months after favorable ITC decision). Estimates: befile6 = 0.060 (insignificant — imports were not unusually high pre-filing), affile6 = −0.032 (insignificant — filing alone did little), afdec6 = −0.565 (significant at 5%) — imports fell by exactly $100[\exp(-0.565)-1] \approx -43.2\%$ after the positive ruling. Controls behave as theory predicts: stronger dollar raises imports (elasticity not different from 1). Adding 11 monthly seasonal dummies leaves conclusions unchanged (joint F p-value = 0.59) — but checking them is required because the data are not seasonally adjusted.

## Key Takeaways
1. In time series, random sampling is gone: TS.3's strict exogeneity does the work of MLR.2 + MLR.4, and it fails whenever regressors feed back on past errors — scrutinize policy rules and response mechanisms before trusting OLS.
2. Only TS.1–TS.3 are needed for unbiasedness; TS.4–TS.5 buy the usual variance formulas and Gauss-Markov; TS.6 buys exact small-sample inference. Know which property rests on which assumption.
3. In FDL models, individual lag coefficients are often imprecise due to multicollinearity across lags, but the LRP can still be tightly estimated — report it (with its SE from the reparameterized regression) rather than the noisy $\hat\delta_j$.
4. Always add a time trend when any series in the regression trends — even if y itself does not — and prefer simple (linear/quadratic) trends.
5. With a trending dependent variable, report the detrended R-squared; the usual one can be grossly inflated (0.341 → 0.008 in the housing example).
6. Seasonal dummies are the in-regression fix for seasonality in unadjusted monthly/quarterly data; test them jointly and interact them with x's if effects vary across the year.
7. Use logs for constant-percentage (elasticity) effects and deflate nominal series with a price index; in log-FDL form, $\delta_0$ is the short-run elasticity and the LRP is the long-run elasticity.

## Connects To
- **Ch 3 (MLR.1–MLR.5)**: TS assumptions are the time-series reworking of the cross-sectional Gauss-Markov set; omitted-variables bias analysis carries over unchanged.
- **Ch 11**: relaxes TS.3 to contemporaneous/sequential exogeneity and covers large-sample properties when strict exogeneity fails.
- **Ch 12**: testing for serial correlation and heteroskedasticity in time series and the remedies (GLS, robust inference) when TS.5/TS.4 fail.
- **Ch 13–14**: serial correlation returns in panel data; TS.5's logic underlies cluster-robust inference.
- **Ch 18**: infinite distributed lags and forecasting build on the FDL machinery here.
- **Event studies in finance/management**: the dummy-variable event-study design here is the ancestor of modern DiD designs.
