# Chapter 22: A Gallery of Rogues—Other Methods

## Core Idea

Advanced methods extend the toolbox but do not repeal identification. Use this chapter as a frontier map; read current primary methods literature before execution because assumptions, estimators, and software are evolving.

## Method Router

### Synthetic Control

Use for one or a few treated units with a rich donor pool and many pre-treatment periods. Construct weights that reproduce pre-treatment outcomes/predictors, then compare post-treatment divergence.

Check donor contamination, anticipation, spillovers, pre-treatment fit, interpolation versus extrapolation, and placebo/permutation distributions. A good pre-fit is necessary but does not prove the post-treatment counterfactual.

### Matrix Completion

Use panel structure and low-rank/common-factor assumptions to impute untreated potential outcomes. Check missing-treatment pattern, rank/factor sensitivity, pre-treatment prediction, cross-validation that respects time, and whether treatment assignment depends on latent factors in unsupported ways.

### Causal Discovery

Use conditional-independence or score-based algorithms to propose equivalence classes of graphs under assumptions such as acyclicity, faithfulness, adequate measurement, and sometimes causal sufficiency. Treat outputs as hypotheses to combine with theory and interventions—not as a data-only proof of arrow direction.

### Double Machine Learning

Use flexible nuisance models for outcome and treatment while preserving a low-dimensional causal target through orthogonal scores and cross-fitting. It still requires identification such as unconfoundedness, overlap, valid instruments, or a valid design. Cross-fit by independent assignment units; report nuisance performance and target inference.

### Causal Forests and Heterogeneous Effects

Use when treatment-effect heterogeneity is the target and sample size/overlap support flexible estimation. Use honest sample splitting or cross-fitting, report CATE uncertainty and calibration, distinguish discovery from confirmation, and validate any policy rule out of sample. Individual treatment-effect predictions are not observed outcomes.

### Sorted Effects

Display a model-implied distribution of effects rather than only its average. The distribution inherits the model, identification, and support assumptions; tail estimates are especially noisy.

### Structural Estimation

Specify behavioral/institutional primitives and solve a model that maps them to observed choices. Structural models can answer counterfactuals outside reduced-form variation but rely on stronger functional-form, equilibrium, preference, and invariance assumptions. Validate fit on moments not mechanically targeted and expose sensitivity to alternative structures.

## Selection Rule

Choose an advanced method only when it addresses a specific design limitation and its additional assumptions are more credible than those of the simpler alternative.

## Advanced-Method Comparison

| Method | Extra leverage | Extra assumption burden |
|---|---|---|
| Synthetic control | Data-adaptive donor weighting | Long stable pre-fit and uncontaminated donors |
| Matrix completion | Latent factor imputation in panels | Low-rank/stable latent structure |
| Causal discovery | Graph hypotheses from conditional independence | Faithfulness, measurement, acyclicity, equivalence limits |
| Double ML | Flexible nuisance functions with valid target inference | Base identification, overlap, cross-fitting |
| Causal forests | Flexible CATE structure | Large support, honest validation, noisy individual effects |
| Sorted effects | Full model-implied effect distribution | Correct outcome/effect model, tail uncertainty |
| Structural estimation | Rich policy counterfactuals | Behavioral structure and invariant primitives |

Use sample splitting for exploratory heterogeneity and confirmatory evaluation. A subgroup found because it has an extreme estimated effect inherits selection bias; evaluate it on held-out data or a new sample. For any frontier method, record the literature/software date because defaults and recommended estimators may change rapidly.

## Failure Modes

- Adding machine learning to an unidentified design.
- Using post-treatment prediction accuracy as causal validation.
- Treating synthetic-control visual fit as a p-value.
- Interpreting discovered graphs without acknowledging Markov equivalence and assumptions.
- Mining heterogeneous effects and reporting the most extreme subgroup.
- Using a structural model without checking which parameters are identified by which moments.

## Completion Check

Before using any method here, name its identifying assumption, target estimand, validation strategy, simpler benchmark, and current-literature check.

## Worked Example

> Synthetic application derived from the chapter's framework; not a documented case from the source.

A single state adopts a platform-regulation law while many states remain untreated, with ten pre-treatment years and five post-treatment years. Standard DiD requires a credible comparison trend. Synthetic control instead chooses donor weights to reproduce the treated state's pre-law outcome path and predictors.

Before using it:

1. exclude states affected by spillovers or similar policies;
2. report donor weights and pre-treatment fit;
3. compare post-law divergence with in-space and in-time placebos;
4. examine leave-one-donor-out sensitivity;
5. state whether inference is permutation-based and what exchangeability it assumes.

Matrix completion could be a rival if a low-rank panel structure is plausible. A flexible method is not automatically superior: if both rely on contaminated donors, neither solves the identification problem.

## Connects To

- [Ch15](ch15-simulation.md): stress-test advanced estimators.
- [Ch18](ch18-difference-in-differences.md): synthetic controls and panel counterfactuals.
- [Ch23](ch23-under-the-rug.md): model uncertainty and measurement.
