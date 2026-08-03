---
name: did-analysis
description: >
  Guides practitioners through modern Difference-in-Differences (DiD) causal
  inference analysis in R. Provides an expanded modern 5-step workflow with
  practical extensions: diagnose TWFE problems, select and run
  heterogeneity-robust estimators (Callaway-Sant'Anna, Sun-Abraham, BJS,
  Gardner, etc.), conduct power analysis for pre-trends, and perform HonestDiD
  sensitivity analysis. Use when the user needs help with DiD estimation, event
  studies, staggered treatment adoption, parallel trends testing, or TWFE
  diagnostics.
metadata:
  author: Xianyang Zhang
  version: 1.0.0
  category: statistics
  tags: [causal-inference, difference-in-differences, econometrics, R]
---

## Contents
- [Progressive Disclosure](#progressive-disclosure)
- [Before the Analysis](#before-the-analysis)
  - [Quick-Start Decision Tree](#quick-start-decision-tree)
  - [Data Requirements Checklist](#data-requirements-checklist)
- [During the Analysis: The 5-Step Modern DiD Workflow](#during-the-analysis-the-5-step-modern-did-workflow)
  - [Step 1: Assess Treatment Structure](#step-1-assess-treatment-structure)
  - [Step 2: Diagnose TWFE Problems](#step-2-diagnose-twfe-problems)
  - [Step 3: Choose and Run Robust Estimators](#step-3-choose-and-run-robust-estimators)
  - [Step 4: Power Analysis for Pre-Trends](#step-4-power-analysis-for-pre-trends)
  - [Step 5: Sensitivity Analysis (HonestDiD) and Inference](#step-5-sensitivity-analysis-honestdid-and-inference)
- [Personalized Method Selection Advice](#personalized-method-selection-advice)
  - [By Treatment Pattern](#by-treatment-pattern)
  - [By Sample Size](#by-sample-size)
  - [By Priority](#by-priority)
  - [Key Warnings at Each Step](#key-warnings-at-each-step)
- [Cross-Package Coefficient Extraction Cookbook](#cross-package-coefficient-extraction-cookbook)
- [Data Preparation Gotchas Per Estimator](#data-preparation-gotchas-per-estimator)
- [Package Installation Reference](#package-installation-reference)
- [Reference Files (references/)](#reference-files-references)
  - [Step Guides](#step-guides)
  - [Package Documentation (references/packages/)](#package-documentation-referencespackages)
- [Simulating Test Data for DiD Analysis](#simulating-test-data-for-did-analysis)

# Modern Difference-in-Differences Analysis Skill

## Progressive Disclosure

Use this order to keep context small and targeted:

1. **SKILL.md (this file)**: Decision trees, code templates, and routing. Always loaded.
2. **Step guides** (`references/did-step-{1-5}-*.md`): One step at a time. Use `references/did-advanced-methods.md` for non-standard settings.
3. **Package quick starts** (`references/packages/*_quick_start.md`): Package overview, function map, and GitHub source pointers.
4. **Full package docs** (`references/packages/*.md`): Argument-level CRAN documentation.
5. **R source code**: Each `*_quick_start.md` lists the GitHub repo URL and key source files.

---

## Before the Analysis

Verify these prerequisites before starting the 5-step workflow.

### Quick-Start Decision Tree

```
Is treatment staggered (units adopt at different times)?
├─ NO → Standard canonical DiD (TWFE is fine). Go to Step 4.
└─ YES → TWFE may be biased. Continue below.
    │
    Is treatment binary and absorbing (once treated, always treated)?
    ├─ YES → Check cohort sizes (Step 1: cohort_summary).
    │   ├─ All cohorts >= 5 units → All core estimators applicable.
    │   └─ Any cohort < 5 units  → SA likely unstable; prefer CS or Gardner.
    │         See references/did-step-3-estimation.md
    └─ NO  → Treatment is non-binary, continuous, or reversible
              Use DIDmultiplegt / DIDmultiplegtDYN
              See references/did-advanced-methods.md
```

### Data Requirements Checklist

Before running any DiD estimator, verify:

1. **Panel structure**: Data has unit identifier (`idname`) and time variable (`tname`)
2. **Treatment timing variable** (`gname`): Period when unit first receives treatment
   - Never-treated units: coding depends on estimator (0, NA, or Inf -- see Data Prep section)
3. **Outcome variable** (`yname`): Numeric, measured for all unit-time pairs
4. **No anticipation**: Units do not change behavior before treatment onset
5. **Sufficient variation**: Multiple treatment cohorts and/or never-treated units
6. **Panel balance**: Some estimators require balanced panels (BJS especially)
7. **Numeric identifiers**: Unit and group IDs must be numeric for most estimators and diagnostics.
   Convert character IDs: `df$unit_num <- as.integer(as.factor(df$unit_id))`

---

## During the Analysis: The 5-Step Modern DiD Workflow

### Step 1: Assess Treatment Structure

Determine whether treatment is:
- **Binary absorbing** (once treated, always treated) -- use core estimators
- **Non-binary / reversible / continuous** -- use DIDmultiplegt family; **Staggered** vs. **canonical**

See `references/did-step-1-treatment-structure.md` for routing details before diagnostics.

> **Visualize first**: Plot treatment rollout with `panelView` and outcome
> trajectories by cohort before proceeding to diagnostics.

### Step 2: Diagnose TWFE Problems

Run diagnostic tests to quantify TWFE bias. See `references/did-step-2-diagnostics.md` for full details.

**Bacon Decomposition** (forbidden comparison weight):
```r
library(bacondecomp)
bacon_out <- bacon(outcome ~ treatment, data = df,
                   id_var = "unit_id", time_var = "time")
# Check: what share of weight is on "Later vs Earlier" comparisons?
forbidden <- bacon_out[bacon_out$type == "Later vs Earlier Treated", ]
cat(sprintf("Forbidden comparison weight: %.1f%%\n", 100 * sum(forbidden$weight)))
```

**TwoWayFEWeights** (negative weight share):
```r
library(TwoWayFEWeights)
wt <- twowayfeweights(df, Y = "outcome", G = "unit_id",
                       T = "time", D = "treatment", type = "feTR")
# Extract negative weight share (absolute weight sums, not counts)
neg_share <- abs(wt$sum_minus) / (wt$sum_plus + abs(wt$sum_minus)) * 100
cat(sprintf("Negative weight share: %.1f%%\n", neg_share))
```

> See `references/did-step-2-diagnostics.md` for full field reference and interpretation.

**Severity Thresholds** (both diagnostics use the same bands):

| Metric                      | >50%   | 25-50%   | 10-25% | <10%    |
|-----------------------------|--------|----------|--------|---------|
| Forbidden weight %          | SEVERE | MODERATE | MILD   | MINIMAL |
| Neg. weight share (abs. wt) | SEVERE | MODERATE | MILD   | MINIMAL |

- SEVERE: Abandon TWFE entirely; use robust estimators
- MODERATE: TWFE likely problematic; strongly prefer robust estimators
- MILD: Use TWFE with caution; run robust estimators as robustness check
- MINIMAL: TWFE may be acceptable; robust estimators still recommended

### Step 3: Choose and Run Robust Estimators

See `references/did-step-3-estimation.md` for full details on all 5 core estimators.

> **Iterative PT assessment**: Start with unconditional parallel trends. If
> implausible, assess selection mechanisms, check covariate overlap, then
> re-estimate with covariates. See "Iterative Parallel Trends Workflow" in
> `references/did-step-3-estimation.md`.

**Estimator Selection Quick Reference:**

| Package         | Function                | Approach             | Best For                              | Control Group     |
|-----------------|-------------------------|----------------------|---------------------------------------|-------------------|
| `did`           | `att_gt()` + `aggte()`  | Callaway-Sant'Anna   | General purpose; transparent          | Not-yet-treated   |
| `fixest`        | `feols()` + `sunab()`   | Sun-Abraham          | Speed; large datasets; regression     | Never/last-treated|
| `didimputation` | `did_imputation()`      | Borusyak-Jaravel-Spiess | Efficiency; imputation logic       | Not-yet-treated   |
| `did2s`         | `did2s()`               | Gardner two-stage    | Speed; intuitive two-stage            | Not-yet-treated   |
| `staggered`     | `staggered()`           | Roth-Sant'Anna       | Random timing; replication            | Not-yet-treated   |

**Top 3 Estimator Code Templates:**

Callaway-Sant'Anna:
```r
library(did)
cs_out <- att_gt(yname = "outcome", tname = "time", idname = "unit_id",
                 gname = "first_treat", data = df,
                 control_group = "notyettreated", est_method = "dr")
cs_es <- aggte(cs_out, type = "dynamic")
ggdid(cs_es)
```

Sun-Abraham:
```r
library(fixest)
# sunab() drops rows where first_treat is NA; convert to Inf for never-treated
df$first_treat[is.na(df$first_treat)] <- Inf
sa_out <- feols(outcome ~ sunab(first_treat, time) | unit_id + time,
                data = df, cluster = ~unit_id)
iplot(sa_out)
```

Gardner (did2s):
```r
library(did2s)
df$treat <- ifelse(!is.na(df$first_treat) & df$first_treat > 0 &
                   df$time >= df$first_treat, 1, 0)
gardner_out <- did2s(data = df, yname = "outcome",
                     first_stage = ~ 0 | unit_id + time,
                     second_stage = ~ i(treat, ref = FALSE),
                     treatment = "treat", cluster_var = "unit_id")
```

### Step 4: Power Analysis for Pre-Trends

See `references/did-step-4-power-analysis.md` for full details.

```r
library(pretrends)
# Extract matched coefficients and VCOV from sunab model
# NOTE: coef() and vcov() have mismatched dimensions for sunab models;
# sunab_beta_vcv() returns properly aggregated, conformable objects.
bv <- HonestDiD:::sunab_beta_vcv(sa_out)
beta  <- bv$beta
sigma <- bv$sigma
tVec  <- as.numeric(gsub(".*::", "", names(coef(sa_out))))

# What linear trend slope would we detect with 50% power?
slope_50 <- slope_for_power(sigma = sigma, targetPower = 0.50,
                            tVec = tVec, referencePeriod = -1)

# Full power analysis
delta_hyp <- slope_50 * tVec
pt_results <- pretrends(betahat = beta, sigma = sigma,
                        deltatrue = delta_hyp, tVec = tVec)
```

### Step 5: Sensitivity Analysis (HonestDiD) and Inference

See `references/did-step-5-sensitivity-inference.md` for full details including coefficient extraction.

```r
library(HonestDiD)
# beta and sigma from the pretrends block above (via sunab_beta_vcv)
# sunab omits the base period (-1), so tVec already excludes it.
pre_idx  <- which(tVec < -1)
post_idx <- which(tVec >= 0)

# Subset betahat and sigma to pre + post (excluding base)
keep <- c(pre_idx, post_idx)
beta_sub  <- beta[keep]
sigma_sub <- sigma[keep, keep]

# Run sensitivity analysis
honest_results <- createSensitivityResults_relativeMagnitudes(
  betahat = beta_sub, sigma = sigma_sub,
  numPrePeriods = length(pre_idx), numPostPeriods = length(post_idx),
  Mbarvec = seq(0.5, 2, by = 0.5))
```

**Breakdown M Interpretation:**

| Breakdown M | Evidence Strength | Meaning |
|-------------|-------------------|---------|
| NULL (none) | Strong            | Effect robust to all tested M values |
| < 1         | Weak              | Effect fragile; even smaller-than-pre violations invalidate |
| 1 - 1.5     | Moderate          | Robust if post-violations similar to pre-violations |
| > 1.5       | Fairly robust     | Post-violations must be substantially larger to invalidate |

**Power Analysis Interpretation** (cumulative detectable bias / |ATT|):

| Bias / |ATT| | Power Quality | Meaning |
|---------------|---------------|---------|
| < 5%          | Excellent     | Can detect violations far smaller than the effect |
| 5% - 25%      | Good          | Good power relative to effect size |
| 25% - 100%    | Moderate      | Undetectable violations could rival the effect |
| > 100%        | Poor          | Pre-test is uninformative; see Step 4 for assessment |

**Inference Best Practices:**
- Cluster SEs at the treatment-assignment level (e.g., state if policy is state-level, even if units are counties). See Step 3 "Clustering Standard Errors" section for per-estimator syntax.
- When treated clusters < 30, cluster-robust SEs may be unreliable; supplement with wild cluster bootstrap or HonestDiD
- When treated clusters < 10, consider aggregating to the treatment level before estimation
- Report both point estimates and HonestDiD sensitivity intervals

## Personalized Method Selection Advice

### By Treatment Pattern
- **Canonical (2x2 DiD)**: Standard TWFE is appropriate; focus on parallel trends and DRDID with covariates
- **Staggered adoption**: MANDATORY diagnostics (Step 2); robust estimators required; high-priority sensitivity analysis
- **Complex (non-binary/reversible)**: Use DIDmultiplegt family; standard methods may not apply

### By Sample Size
- **Small (<100 units)**: Power analysis especially important; consider aggregating time periods; sensitivity analysis critical
- **Medium / Large**: Standard workflow; for >10K units prefer SA (fixest) for speed

### By Priority
- **Speed**: SA (fixest::sunab) primary, Gardner (did2s) secondary
- **Transparency / Robustness**: CS (did) primary; compare multiple estimators; extensive sensitivity analysis

### Key Warnings at Each Step
1. **Assessment**: Don't assume TWFE is valid without checking treatment pattern
2. **Diagnostics**: Don't skip even if you plan to use robust estimators; >25% forbidden weight = serious bias risk
3. **Estimation**: Different estimators make different assumptions; large discrepancies between methods indicate model uncertainty; compare at least two
4. **Power**: Non-significant pre-trends does NOT mean parallel trends holds; low power makes pre-test uninformative
5. **Sensitivity**: Don't skip -- crucial for credibility; low breakdown M = fragile results

## Advanced Reference

Use the bundled reference files for estimator-specific gotchas, coefficient extraction recipes, and package-level details:

- `references/did-step-1-treatment-structure.md` through `references/did-step-5-sensitivity-inference.md` for the detailed 5-step workflow.
- `references/did-advanced-methods.md` and `references/did-troubleshooting.md` for edge cases and fixes.
- `references/package-versions.md` and `references/packages/` for installation and package-specific notes.

