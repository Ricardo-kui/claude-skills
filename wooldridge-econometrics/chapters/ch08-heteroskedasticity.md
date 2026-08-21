# Chapter 8: Heteroskedasticity

## Core Idea
Heteroskedasticity (violation of MLR.5) does not bias or make OLS inconsistent, and leaves R² valid — but it invalidates the usual standard errors and t/F/LM statistics even in large samples. Either report heteroskedasticity-robust inference (White/Huber/Eicker SEs) or model the variance and use WLS/FGLS for efficiency.

## Frameworks Introduced
- **Heteroskedasticity-robust standard errors (White 1980 / Eicker / Huber, "HC0")**: $\widehat{\mathrm{Var}}(\hat\beta_j)=\sum_i \hat r_{ij}^2\hat u_i^2/\mathrm{SSR}_j^2$, where $\hat r_{ij}$ are residuals from regressing $x_j$ on the other regressors.
  - When to use: default for cross-sections whenever heteroskedasticity is possible; asymptotically valid under heteroskedasticity of unknown form.
  - How: report alongside (or instead of) usual SEs — coefficients unchanged, only inference changes. HC1 multiplies by $n/(n-k-1)$; HC3 behaves best in small samples. Robust t = estimate/robust SE.
- **Heteroskedasticity-robust F / Wald / LM tests**: joint-significance tests valid under arbitrary heteroskedasticity.
  - When to use: testing exclusion restrictions or cross-group equality (robust Chow test: group dummy + full interactions, robust F).
  - How (robust LM, any package): ① residuals $\tilde u$ from restricted model; ② regress each excluded $x_j$ on all included ones, keep residuals $\tilde r_j$; ③ form products $\tilde r_j\tilde u$; ④ regress $1$ on $\tilde r_1\tilde u,\dots,\tilde r_q\tilde u$ with no intercept; LM $= n-\mathrm{SSR}_1 \overset{a}{\sim}\chi^2_q$.
- **Breusch-Pagan test**: regress $\hat u^2$ on all regressors; F or LM $= nR^2_{\hat u^2}\overset{a}{\sim}\chi^2_k$ (Koenker 1981 form preferred).
  - When to use: detecting whether Var(u|x) depends on chosen x's; small $R^2_{\hat u^2}$ can still reject strongly in large samples.
  - How: OLS → save $\hat u^2$ → auxiliary regression on chosen regressors (df = number in *auxiliary* regression) → F or LM p-value.
- **White test (special case)**: regress $\hat u^2$ on $\hat y$ and $\hat y^2$; always 2 restrictions ($F_{2,n-3}$ or $\chi^2_2$).
  - When to use: general test that conserves degrees of freedom and detects variance changing with E(y|x); use fitted values $\hat y$, never $y$.
  - How: check functional form first — a rejection can signal misspecified E(y|x) (MLR.4 failure), not heteroskedasticity.
- **WLS / GLS**: when Var(u|x) = σ²h(x) with h(x) known, divide every variable (including the constant) by $\sqrt{h_i}$ and run OLS, equivalently minimize $\sum_i (y_i-b_0-b_1x_{i1}-\dots)^2/h_i$.
  - When to use: variance form known — e.g. group-averaged or per-capita data, where Var(ūᵢ)=σ²/mᵢ so weight by group size / population.
  - How: WLS = BLUE and more efficient than OLS; valid t/F if variance correctly specified. Stata: `reg y x [aw=1/h]`.
- **Feasible GLS (FGLS)**: model Var(u|x)=σ²exp(δ₀+δ₁x₁+…+δₖxₖ); regress $\log(\hat u^2)$ on x, take fitted $\hat g$, set $\hat h=\exp(\hat g)$, run WLS with weights 1/ĥ.
  - When to use: variance form unknown but strong heteroskedasticity suspected; exponential form guarantees positive fitted variances.
  - How: 5 steps above; alternative step 3: regress $\log(\hat u^2)$ on $\hat y,\hat y^2$. FGLS is no longer unbiased but consistent and asymptotically more efficient than OLS. Always add robust SEs after WLS.

## Key Concepts
- **MLR.5 (homoskedasticity)**: Var(u|x₁,…,xₖ)=σ²; plays no role in OLS unbiasedness/consistency — only in efficiency and inference.
- **Heteroskedasticity**: Var(u|x) varies with x; OLS no longer BLUE, usual SEs biased in an unknown direction.
- **Heteroskedasticity-robust (heteroskedasticity-consistent) statistic**: t/F/LM version valid asymptotically whether or not MLR.5 holds.
- **WLS estimator**: GLS applied to heteroskedasticity; weights each squared residual by the inverse of the conditional variance.
- **FGLS estimator**: WLS with h estimated from the same data; consistent, not unbiased.
- **Misspecified variance function**: WLS still consistent under MLR.4, but usual WLS SEs invalid and efficiency not guaranteed — use fully robust SEs after WLS.
- **Group-averaged / per-capita data**: averaging homoskedastic individual errors gives Var(ūᵢ)=σ²/mᵢ → natural WLS weight = group size.
- **LPM heteroskedasticity**: binary y ⇒ Var(y|x)=p(x)[1−p(x)] by construction; the LPM is inherently heteroskedastic.

## Mental Models
- Think of heteroskedasticity as an *inference* problem, not a *bias* problem: it attacks the denominator of the t statistic, never the numerator.
- Use robust SEs when you refuse to model the variance; use WLS/FGLS when the heteroskedasticity is strong enough that OLS efficiency loss matters — and always keep robust SEs even then.
- Treat large OLS–WLS coefficient differences as a warning light for misspecified E(y|x) (MLR.4 failure), not a variance problem: under MLR.4, any positive weighting leaves WLS consistent for the same β.
- Treat BP/White tests as conditional-mean diagnostics too: fix functional form first, then test the variance.

## Anti-patterns
- **Using usual OLS SEs after a BP/White rejection**: the F, t, and LM statistics no longer have their assumed distributions — significance claims can be wrong.
- **Assuming robust SEs are always larger**: they can be smaller; there is no known direction.
- **Using y instead of ŷ in the special White test**: invalid test; ŷ is the function of the regressors.
- **Reading a White/BP rejection as pure heteroskedasticity**: if MLR.4 fails (omitted quadratics, wrong log/level choice), the test rejects even with constant variance.
- **Using a linear variance model for FGLS weights**: linear predictions can go negative; variance weights must be positive — use the exponential form.
- **Applying WLS to the LPM when any fitted value falls outside (0,1)**: ĥ=ŷ(1−ŷ) ≤ 0 breaks the weights; adjust arbitrarily or (better) stay with OLS + robust SEs.
- **Estimating the restricted WLS model with different weights than the unrestricted one**: F statistics after WLS require identical weights in both models.
- **Using WLS to fix omitted-variable bias**: wrong tool — WLS addresses variance, not MLR.4 failures.

## Key Equations & Formulas
$$\widehat{\mathrm{Var}}(\hat\beta_j)=\frac{\sum_{i=1}^n \hat r_{ij}^2\hat u_i^2}{\mathrm{SSR}_j^2}\quad\text{(robust variance, 8.4)}$$
$$F=\frac{R_{\hat u^2}^2/k}{(1-R_{\hat u^2}^2)/(n-k-1)},\qquad LM=n\cdot R_{\hat u^2}^2 \quad\text{(BP test, 8.15–8.16)}$$
$$\hat u^2=\delta_0+\delta_1\hat y+\delta_2\hat y^2+\text{error}\quad\text{(special White test, 8.20)}$$
$$\mathrm{Var}(u|\mathbf{x})=\sigma^2 h(\mathbf{x}),\qquad \min_{b}\sum_{i=1}^n (y_i-b_0-b_1x_{i1}-\cdots-b_kx_{ik})^2/h_i \quad\text{(WLS, 8.21/8.27)}$$
$$\mathrm{Var}(u|\mathbf{x})=\sigma^2\exp(\delta_0+\delta_1x_1+\cdots+\delta_kx_k),\qquad \hat h_i=\exp(\hat g_i)\ \text{from}\ \log(\hat u^2)\ \text{on}\ x \quad\text{(FGLS, 8.30–8.33)}$$
$$\mathrm{Var}(\bar u_i)=\sigma^2/m_i \Rightarrow \text{weight by } m_i \quad\text{(group-averaged data)}$$
$$\mathrm{Var}(y|\mathbf{x})=p(\mathbf{x})[1-p(\mathbf{x})],\qquad \hat h_i=\hat y_i(1-\hat y_i)\quad\text{(LPM, 8.45–8.47)}$$
$$95\%\ \text{PI:}\quad \hat y^0 \pm t_{.025}\cdot \mathrm{se}(\hat e^0),\quad \mathrm{se}(\hat e^0)=\{[\mathrm{se}(\hat y^0)]^2+\hat\sigma^2 h(\mathbf{x}^0)\}^{1/2}\quad\text{(8.37)}$$

## Reference Tables

| Test | Null | Auxiliary regression | Statistic | Remedy if rejected |
|---|---|---|---|---|
| Breusch-Pagan | H₀: Var(u\|x)=σ² (all δⱼ=0) | û² on x₁…xₖ | F(k,n−k−1) or LM=nR² ~χ²ₖ | Robust SEs, or model variance → FGLS |
| White (special) | H₀: δ₁=δ₂=0 | û² on ŷ, ŷ² | F(2,n−3) or LM ~χ²₂ | Same; first rule out functional-form misspecification |
| Robust LM (exclusions) | H₀: q excluded coefs = 0 | 1 on r̃ⱼũ (no intercept) | n−SSR₁ ~χ²_q | — |

| Estimator | Assumption on Var(u\|x) | Properties | Inference |
|---|---|---|---|
| OLS + robust SEs | Unknown/arbitrary | Consistent, unbiased under MLR.1–4; not BLUE | Robust t/F valid asymptotically |
| WLS (h known) | σ²h(x), h known | BLUE, efficient | Exact t/F under normality |
| FGLS (h estimated) | exp form, δ estimated | Consistent, asymp. more efficient than OLS; not unbiased | Asymptotic t/F; use robust SEs if variance form doubtful |
| WLS, h misspecified | h wrong | Still consistent under MLR.4; efficiency not guaranteed | Usual WLS SEs invalid → must use robust SEs |

## Worked Example
**Cigarette demand (Example 8.7, SMOKE, n=807).** Question: what drives daily cigarette consumption (cigs)? OLS of cigs on log(income), log(cigpric), educ, age, age², restaurn: educ −0.501 (sig.), age profile peaks at ≈42.8, restaurant restrictions −2.83 (sig.); income and price insignificant. BP test: R²û²=0.040 looks small, but LM=807×0.040=32.28 ~χ²₆, p<0.000015 — strong heteroskedasticity. FGLS via log(û²) regression and weights 1/ĥ: log(income) rises to 1.30 and becomes significant, log(cigpric) −2.94 (still insignificant, little price variation), restaurn −3.46. Signs and story unchanged — FGLS buys precision, not a new model. Check afterwards: White test on weighted residuals û²/ĥ still rejects (F=11.15), so the variance model is imperfect — report robust SEs after WLS.

## Key Takeaways
1. Heteroskedasticity never biases OLS point estimates; it corrupts SEs, t, F, and LM — fix inference, not coefficients.
2. In cross-sections, report heteroskedasticity-robust SEs by default in large samples; robust and usual SEs can differ in either direction.
3. Small R² in the BP regression does not mean no heteroskedasticity — compute the F/LM statistic; with large n, R²=0.04 rejects overwhelmingly.
4. Test functional form before testing heteroskedasticity; a BP/White rejection under MLR.4 failure is a misspecification signal.
5. With averaged or per-capita data, weight by group size/population — but still report robust SEs in case of individual-level heteroskedasticity or within-group correlation.
6. FGLS with an exponential variance function is the practical efficiency upgrade; it trades unbiasedness for consistency plus asymptotic efficiency.
7. For binary y, default to OLS with robust SEs; WLS on the LPM only when all fitted probabilities lie strictly in (0,1).

## Connects To
- **Ch 3–5**: MLR.1–MLR.5 framework; robust variance formula uses the partialling-out residuals r̂ᵢⱼ from Ch 3; LM mechanics from Ch 5.
- **Ch 6**: log transformations often reduce heteroskedasticity; prediction intervals (8.37) extend Section 6-4.
- **Ch 7**: LPM heteroskedasticity and the robust Chow test via dummies + interactions.
- **Ch 9**: RESET/functional-form tests — the correct first response when a White test rejects.
- **Ch 12**: GLS for serial correlation — same transformation logic, different variance structure.
- **Cluster-robust inference**: the grouped-error problem behind Var(ūᵢ)≠σ²/mᵢ generalizes to clustering in panel/micro data.
