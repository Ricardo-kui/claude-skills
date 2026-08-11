# Chapter 13: Regression

## Core Idea

Regression summarizes conditional means and can implement a valid adjustment or quasi-experimental design. It does not supply identification by itself. Causal interpretation comes from the DGP, conditioning set, functional form, and source of variation.

## Regression Contract

Before interpreting a coefficient, state:

- outcome, treatment, controls, fixed effects, and interactions;
- the estimand and population;
- why each control is pre-treatment and path-relevant;
- the support used for comparison;
- the functional form and whether marginal effects vary;
- the dependence structure governing standard errors;
- whether weights change the target population.

## From DAG to Specification

- Put the outcome on the left-hand side.
- Include the treatment whose causal contrast is targeted.
- Include a sufficient pre-treatment adjustment set that closes back doors.
- Exclude colliders and treatment-induced variables for a total-effect target.
- Add precision variables only when they do not change the estimand or induce bias.
- Represent design structure—cutoffs, instruments, treatment timing, cohort effects—explicitly rather than expecting generic controls to absorb it.

## Functional Form and Interpretation

1. Plot conditional relationships before specifying a line.
2. Use transformations and polynomials to represent plausible shapes, not to maximize fit.
3. Under interactions, interpret conditional or average marginal effects; the “main effect” is evaluated at the reference/zero values of interacting variables.
4. For nonlinear models, distinguish coefficient scale from probability, odds, rate, or marginal-effect scale.
5. Check whether results depend on extrapolation or influential support regions.

## Inference

Conventional OLS standard errors require restrictive error independence and variance assumptions. Choose uncertainty estimation based on the design:

- heteroskedasticity-consistent errors for cross-sectional heteroskedasticity;
- clustering at the treatment-assignment or dependence level;
- HAC/time-series methods for serial dependence;
- design-aware bootstrap that resamples the independent assignment units;
- small-cluster corrections when clusters are few.

A smaller standard error does not repair bias.

## Additional Threats

- **Sample weights** change representation and sometimes the estimand; document their construction.
- **Collinearity** raises uncertainty and sensitivity but is not itself confounding.
- **Measurement error** can attenuate, inflate, or otherwise distort estimates depending on what is measured and how.
- **Penalized regression** may aid prediction or nuisance estimation; outcome-driven variable selection does not replace a causal adjustment set.

## Specification and Inference Reference

| Issue | What changes | Required response |
|---|---|---|
| Interaction | Effect varies with another variable | Report marginal effects and supported values |
| Nonlinear outcome model | Coefficient is not an outcome-unit effect | Translate to probabilities/rates/marginal effects |
| Heteroskedasticity | Conditional error variance differs | Use appropriate robust variance; inspect influence |
| Within-cluster dependence | Effective information is below row count | Cluster at assignment/dependence level |
| Serial dependence | Adjacent errors are related | Use HAC or an explicit time-series structure |
| Survey/target weights | Observations represent unequal population shares | Explain weighted population and variance design |
| Measurement error | Recorded variable differs from construct | Model direction/mechanism; use validation or sensitivity |
| Many controls | Nuisance model is high dimensional | Preserve causal set; use regularization/cross-fitting only with valid target inference |

Always show how the treatment coefficient changes after residualization: which observations and support drive it. If the answer cannot name them, the regression remains algebra rather than a design.

## Failure Modes

- Table-first interpretation without raw support or marginal effects.
- Control selection by significance.
- Default standard errors unrelated to assignment.
- High-order polynomial extrapolation.
- Reporting model fit as causal credibility.
- Interpreting a coefficient on a badly measured proxy as the construct effect.

## Completion Check

A causal regression is complete only when the coefficient is mapped to an identified contrast and alternative specifications probe meaningful assumptions rather than cosmetic model choices.

## Technical Skeleton

A common adjustment model is:

Y_i = α + τD_i + X_i′β + ε_i.

The coefficient τ is a causal effect only if the selected X closes the relevant back doors, the functional form represents the conditional relationship over common support, and the coefficient's weighting matches the estimand. Under interactions or nonlinear links, report conditional or average marginal effects rather than treating τ-like coefficients as constant effects.

## Worked Example

> Synthetic application derived from the chapter's framework; not a documented case from the source.

To estimate the effect of an employee-training program, theory identifies prior performance and job category as pre-treatment common causes. Include those variables and inspect overlap. Do not add post-training motivation or manager evaluation, because training can change them.

Fit a flexible outcome model with a treatment-by-prior-performance interaction. Report the average marginal training effect and effects across the supported performance range. Use cluster-robust inference if training is assigned by workplace. Then compare with a design-weighted estimate and a specification that relaxes the performance functional form.

If the estimate changes only when extrapolating to performance levels with no untreated participants, the issue is support—not merely “model robustness.”

## Connects To

- [Ch8](ch08-causal-paths.md): select controls.
- [Ch14](ch14-matching.md): improve overlap and covariate comparability.
- [Ch16](ch16-fixed-effects.md): isolate within variation.
- [Ch23](ch23-under-the-rug.md): model and measurement uncertainty.
