# Chapter 4: Multiple Regression Analysis: Inference

## Core Idea
Under the classical linear model (CLM) assumptions MLR.1–MLR.6, the OLS estimators are exactly normally distributed conditional on the x's, which makes t statistics, confidence intervals, and F statistics exact finite-sample tools for testing hypotheses about population parameters — not just descriptions of one sample.

## Frameworks Introduced
- **Assumption MLR.6 (Normality)**: The population error $u$ is independent of $x_1,\dots,x_k$ and $u \sim \text{Normal}(0,\sigma^2)$. Adding it to MLR.1–MLR.5 gives the CLM assumptions, compactly: $y|\mathbf{x} \sim \text{Normal}(\beta_0+\beta_1x_1+\dots+\beta_kx_k,\ \sigma^2)$.
  - When to use: required for *exact* t/F inference in finite samples; implausible when $y$ is discrete, bounded (wages ≥ 0), or takes few values — then rely on Ch. 5 asymptotics instead.
  - How: treat normality as an empirical, case-by-case question; a log transform (e.g. log(price), log(wage)) often moves the distribution closer to normal.
- **t test for a single parameter**: $t = (\hat\beta_j - a_j)/\text{se}(\hat\beta_j) \sim t_{n-k-1}$ under $\mathrm{H}_0:\beta_j=a_j$.
  - When to use: any hypothesis about one $\beta_j$ — not just $\beta_j=0$ (test $\beta_j=1$, $\beta_j=-1$ when theory predicts a value).
  - How: pick significance level and one- vs two-sided alternative *before* looking at estimates; reject when $t>c$, $t<-c$, or $|t|>c$; or compute the p-value and reject when p < α. df > 120 → use standard normal critical values (1.645 one-sided, 1.96 two-sided at 5%).
- **Confidence interval**: $\hat\beta_j \pm c\cdot\text{se}(\hat\beta_j)$, $c$ = 97.5th percentile of $t_{n-k-1}$.
  - When to use: always — communicates estimation precision and tests any two-sided $\mathrm{H}_0:\beta_j=a_j$ (reject iff $a_j$ outside the CI). Rule of thumb: df > 50 → estimate ± 2 standard errors.
- **Testing a single linear combination by reparameterization**: for $\mathrm{H}_0:\beta_1=\beta_2$, define $\theta_1=\beta_1-\beta_2$, substitute $\beta_1=\theta_1+\beta_2$, and re-run the regression with transformed regressors so $\theta_1$ appears as a coefficient.
  - When to use: comparing two coefficients (returns to two-year vs four-year college), testing $\beta_1+\beta_2=1$, etc.
  - How: rewrite the model so the parameter of interest multiplies one regressor (e.g. replace `univ` with `totcoll = jc + univ`); the reported t on the kept regressor is the test. Never compute $\text{se}(\hat\beta_1-\hat\beta_2)$ as $\text{se}(\hat\beta_1)-\text{se}(\hat\beta_2)$ — the covariance term matters. In Stata, `lincom` or `test` does the same thing.
- **F test for multiple linear restrictions**: compare restricted vs unrestricted model fit.
  - When to use: exclusion restrictions (joint significance of a group, e.g. all performance stats), general linear restrictions (e.g. $\beta_1=1,\beta_2=\beta_3=0$), overall significance of the regression.
  - How: estimate both models on the *same* observations; numerator df $q$ = number of restrictions; denominator df = $n-k-1$ of the unrestricted model; reject when $F > c$ from $F_{q,n-k-1}$. Use the R-squared form only for exclusion restrictions with the same dependent variable; use the SSR form otherwise. In Stata: `test varlist` after `reg`.

## Key Concepts
- **CLM assumptions**: MLR.1–MLR.5 (Gauss-Markov) plus MLR.6; under them OLS is *minimum variance unbiased* among all unbiased estimators, not just linear ones.
- **Significance level**: the probability of rejecting $\mathrm{H}_0$ when it is true; chosen before testing, determines the critical value.
- **p-value**: the smallest significance level at which $\mathrm{H}_0$ would be rejected; the probability of a statistic at least as extreme as observed *if $\mathrm{H}_0$ is true* — never the probability that $\mathrm{H}_0$ is true.
- **Economic (practical) significance**: size and sign of $\hat\beta_j$ (effect size); distinct from statistical significance, which is determined entirely by $|t|$.
- **Statistically significant / insignificant**: shorthand for rejecting / failing to reject $\mathrm{H}_0:\beta_j=0$ at the stated level against a (default two-sided) alternative.
- **Restricted / unrestricted model**: the model imposing $\mathrm{H}_0$ vs the full model; the restricted model always has fewer parameters and a larger SSR.
- **Exclusion restrictions**: $\mathrm{H}_0:\beta_{k-q+1}=\dots=\beta_k=0$ — a set of $q$ variables has no partial effect once the others are controlled.
- **Jointly statistically significant**: the F test rejects the exclusion restrictions; says nothing about which individual variables matter.
- **Overall significance of the regression**: the F test of $\mathrm{H}_0:\beta_1=\dots=\beta_k=0$ (all slopes zero, intercept free); reported by every regression package.
- **"Fail to reject" vs "accept"**: many mutually exclusive values of $\beta_j$ can each fail to be rejected, so never say "accept $\mathrm{H}_0$."

## Mental Models
- Use **t for one restriction, F for many**; a single-exclusion F is exactly $t^2$ (two-sided), so F adds nothing for one parameter — and t alone handles one-sided alternatives.
- Think of the F statistic as the **relative increase in SSR** when moving from the unrestricted to the restricted model: is the fit loss large relative to the number of restrictions?
- Use **F when suspects travel in packs**: highly correlated variables (hrunsyr/rbisyr, multiple firm-performance measures) can each be individually insignificant yet jointly highly significant — multicollinearity kills individual t's, not joint F's.
- Think of **statistical vs economic significance as separate dials**: large n shrinks standard errors until trivially small effects are "significant" (a 10,000-employee increase lowers 401(k) participation by only 1.3 points, yet t = −3.25); small n can hide large effects. Always discuss magnitude.

## Anti-patterns
- **Testing a joint hypothesis with separate t statistics**: individually insignificant t's do not imply joint insignificance (baseball example: three insignificant t's, F ≈ 9.55). Conversely a group can be jointly insignificant while one member is significant — never "hide" a key variable in a joint test.
- **Choosing the alternative after seeing the estimates**: peeking at the sign of $\hat\beta_j$ and then declaring a one-sided alternative invalidates classical inference; state hypotheses about population parameters before estimation.
- **Writing $\mathrm{H}_0:\hat\beta_1=0$ or "$\mathrm{H}_0: 0.237 = 0$"**: hypotheses concern unknown population parameters, never sample estimates.
- **Using the regression's overall F (all slopes zero) to test a subset of restrictions**: (4.46) is valid only for excluding *all* regressors; general exclusion tests need both models' R²s/SSRs.
- **Using the R-squared form of F when the restricted model changes the dependent variable**: e.g. testing $\beta_1=1$ requires regressing $y-x_1$ on an intercept; SST no longer cancels — use the SSR form.
- **Estimating restricted and unrestricted models on different samples**: missing data on the tested variables shrinks n for the unrestricted model; the restricted model must use the same observations or the F test is invalid (use built-in `test` commands).
- **Reading importance from p-values alone / p-hacking**: searching specifications until p < 0.05, or requiring 5% significance to act, ignores effect sizes; ASA (Wasserstein–Lazar 2016) guidelines demand transparency and attention to practical significance.

## Key Equations & Formulas
$$\hat\beta_j \sim \text{Normal}\big(\beta_j,\ \text{Var}(\hat\beta_j)\big),\qquad \frac{\hat\beta_j-\beta_j}{\text{se}(\hat\beta_j)} \sim t_{n-k-1} \quad\text{(Theorems 4.1–4.2)}$$
$$t = \frac{\text{estimate} - \text{hypothesized value}}{\text{standard error}} = \frac{\hat\beta_j - a_j}{\text{se}(\hat\beta_j)} \tag{4.13}$$
$$\text{95\% CI: } \hat\beta_j \pm c\cdot\text{se}(\hat\beta_j),\quad c = 97.5\text{th pct of } t_{n-k-1} \tag{4.16}$$
$$\text{se}(\hat\beta_1-\hat\beta_2) = \big\{[\text{se}(\hat\beta_1)]^2+[\text{se}(\hat\beta_2)]^2-2s_{12}\big\}^{1/2} \tag{4.23}$$
$$F \equiv \frac{(\text{SSR}_r-\text{SSR}_{ur})/q}{\text{SSR}_{ur}/(n-k-1)} \sim F_{q,\,n-k-1} \tag{4.37}$$
$$F = \frac{(R^2_{ur}-R^2_r)/q}{(1-R^2_{ur})/(n-k-1)} \quad\text{(R-squared form, exclusion restrictions only)} \tag{4.41}$$
$$\text{Overall } F = \frac{R^2/k}{(1-R^2)/(n-k-1)} \tag{4.46}$$

## Reference Tables

| Assumption | Statement | Role in this chapter |
|---|---|---|
| MLR.1 Linear in parameters | $y=\beta_0+\beta_1x_1+\dots+\beta_kx_k+u$ | Defines the population $\beta_j$ being tested |
| MLR.2 Random sampling | Random sample of $n$ obs from the population model | Makes errors i.i.d.; inference generalizes to population |
| MLR.3 No perfect collinearity | No regressor constant; no exact linear relationships | Ensures $\hat\beta_j$ computable |
| MLR.4 Zero conditional mean | $\mathrm{E}(u|x_1,\dots,x_k)=0$ | Unbiasedness of $\hat\beta_j$ |
| MLR.5 Homoskedasticity | $\text{Var}(u|x_1,\dots,x_k)=\sigma^2$ | Valid standard-error formulas; Gauss-Markov efficiency |
| MLR.6 Normality | $u$ independent of x's, $u\sim\text{Normal}(0,\sigma^2)$ | Exact t/F distributions; OLS minimum variance among all unbiased estimators |

| Situation | Test | Statistic / df | Reject $\mathrm{H}_0$ when |
|---|---|---|---|
| Single $\beta_j=0$, two-sided | t | $\hat\beta_j/\text{se}(\hat\beta_j)$, $t_{n-k-1}$ | $\|t\|>c$ (or p < α) |
| Single $\beta_j=0$, one-sided | t | same | $t>c$ ($\beta_j>0$) or $t<-c$ ($\beta_j<0$) |
| $\beta_j=a_j$ (e.g. 1, −1) | t | $(\hat\beta_j-a_j)/\text{se}(\hat\beta_j)$ | as above; or $a_j$ outside CI |
| Single linear combination | t | reparameterize; t on $\hat\theta_1$ | as above |
| $q$ exclusion restrictions | F | (4.37) or (4.41), $F_{q,n-k-1}$ | $F>c$ |
| All slopes = 0 (overall) | F | (4.46), $F_{k,n-k-1}$ | $F>c$ |
| General linear restrictions | F | SSR form (4.37) only | $F>c$ |

## Worked Example
**Do performance statistics affect MLB salaries? (MLB1)** Model: $\log(\text{salary})$ on years, gamesyr, bavg, hrunsyr, rbisyr; $n=353$, SSR = 183.186, $R^2=0.6278$. Question: controlling for years and games per year, do bavg, hrunsyr, rbisyr matter — $\mathrm{H}_0:\beta_3=\beta_4=\beta_5=0$ ($q=3$)? Individually, all three t statistics are insignificant at 5% (rbisyr closest, p = 0.134). But the restricted model (years, gamesyr only) has SSR = 198.311: $F = \frac{(198.311-183.186)/3}{183.186/347} \approx 9.55$, far above the 1% critical value 3.78 → soundly reject; the three variables are jointly significant. Resolution: hrunsyr and rbisyr are highly correlated, so multicollinearity inflates each standard error and kills the individual t's, while the F test detects their combined effect. Lesson: use F for groups of correlated variables; never infer joint insignificance from individual t's.

## Key Takeaways
1. Exact t and F inference requires MLR.6 on top of Gauss-Markov; when normality is clearly false (discrete or bounded $y$), wait for the Ch. 5 large-sample justification rather than forcing exact tests.
2. Report standard errors (not just t statistics), $R^2$, and n with every equation — SEs let readers test their own hypotheses and build CIs.
3. Always pair statistical significance with economic significance: interpret coefficient magnitudes in units, and use 95% CIs to show the plausible range of the effect.
4. For any hypothesis about a combination of coefficients, reparameterize the regression (or use `lincom`/`test`) so the software delivers the standard error — do not hand-compute it from individual SEs.
5. F tests need the same n in both models, numerator df = number of restrictions, and the SSR form whenever the dependent variable changes.
6. In policy evaluation (e.g. JTRAIN98 job training), controls exist to purge selection bias — their individual significance and their multicollinearity are irrelevant; report the treatment effect $\hat\tau$ with its p-value and 95% CI (train: −2.05 (0.48) simple vs +2.41 (0.44) with controls — the sign flip shows why controls matter).
7. Use p-values as evidence summaries, not decision machines: report them, avoid p-hacking, and never "accept" a null — only fail to reject.

## Connects To
- **Ch 3**: Var($\hat\beta_j$) formula (3.51) and Gauss-Markov assumptions supply the se's that feed every t and F here.
- **Ch 5**: drops MLR.6 — asymptotic normality of OLS justifies the same tests in large samples.
- **Ch 6**: functional form choices (logs, quadratics) change t outcomes (Example 4.2: enroll insignificant in levels, significant in logs); R² for choosing between forms.
- **Ch 8**: heteroskedasticity invalidates the usual SEs and hence every CI/t/F here → robust inference.
- **Policy/program evaluation (Ch 3.7e, Ch 7, 13)**: t on the treatment dummy and its CI are the standard evidence package.
