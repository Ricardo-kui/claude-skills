# Chapter 17: Event Studies

## Core Idea

An event study compares observed post-event outcomes with a counterfactual forecast constructed from pre-event behavior, market movements, comparison series, or a time-series model. The estimated effect and counterfactual-model validity are jointly tested.

## Classification Gate

Classify the design before selecting an event window or estimator:

| Design family | Counterfactual | Route |
|---|---|---|
| Financial-market event study | Expected return absent the information event | Continue here with market-model and abnormal-return logic |
| Single-series intervention / interrupted time series | Forecast of the untreated post-event series | Continue here with time-series and coincident-shock checks |
| Multiple independent events | Event-specific forecasts or comparison series | Continue here and model repeated-event dependence |
| Panel event-time design with treated and comparison groups | Untreated change path for treated cohorts | Read Ch18 and use modern DiD logic |
| Staggered adoption | Cohort-time untreated counterfactual | Route to Ch18; use cohort-aware estimates rather than conventional TWFE leads/lags |

Treat “event study” as a display label only after this classification. Let the assignment process determine the design family.

## Event-Study Contract

Specify:

- event definition and information/reaction time;
- affected unit(s);
- estimation window, event window, and post-event horizon;
- outcome transformation, such as returns rather than prices;
- counterfactual prediction model;
- concurrent events and anticipation;
- serial dependence and inference;
- aggregation across units/events.

## Design Workflow

1. Establish when treatment or new information became available.
2. Choose a window narrow enough to limit concurrent shocks but long enough to capture the response.
3. Model the untreated counterfactual using pre-event information and defensible predictors.
4. generate abnormal outcomes as observed minus predicted.
5. aggregate only effects that share a coherent estimand.
6. examine pre-event fit and fake-event performance.
7. account for autocorrelation, cross-sectional dependence, repeated events, and overlapping windows.
8. distinguish immediate information effects from later implementation effects.

## Major Variants

- **Finance event study**: estimate expected returns using a market model, then cumulate abnormal returns over a specified window.
- **Interrupted time series/segmented regression**: estimate level and slope changes around an intervention.
- **Forecast-based design**: fit an appropriate time-series model to pre-event data and forecast the post-event counterfactual.
- **Multiple affected groups**: align event time and model dependence across groups; if groups adopt at different times with comparison groups, route to modern DiD.

## Joint-Test Problem

A post-event deviation can arise from a real effect or a wrong counterfactual model. Good pre-event fit is not sufficient because the untreated process after the event is unobserved. Use:

- placebo event dates;
- unaffected outcomes or units;
- rolling-origin/backtesting of the forecasting model;
- alternative defensible counterfactual models;
- institutional checks for coincident information.

## Inference

Naive segmented regression can greatly overstate precision under autocorrelation. Use HAC, explicit time-series models, randomization/permutation logic, or cluster-aware methods as appropriate. Multiple event-time coefficients also create multiplicity and joint-inference issues.

## Counterfactual Options

| Counterfactual model | Best suited for | Main threat |
|---|---|---|
| Pre-event mean | Stationary series with no trend | Mean shifts unrelated to event |
| Market/comparison model | Asset returns or credible unaffected series | Comparison is itself affected |
| Segmented trend | Stable smooth pre-trend | Autocorrelation and trend break without treatment |
| ARIMA/time-series forecast | Long, structured pre-period | Model selection and forecast instability |
| Multiple-group event time | Repeated independent events | Common shocks, cross-group dependence |
| Synthetic counterfactual | Rich donor pool and long pre-period | Donor contamination and overfit |

Pre-register or institutionally justify the information date and event window. For repeated events, define whether the unit is removed after its first event, whether windows overlap, and how other events are handled. Report cumulative effects only when summing across periods corresponds to the substantive causal quantity.

## Failure Modes

- Choosing the event date after inspecting the outcome.
- Ignoring information leakage or anticipation.
- Confusing stock-price levels with returns.
- Treating every pre-event coefficient as a separate decisive test.
- Attributing all post-event deviation to treatment despite concurrent shocks.
- Using a staggered TWFE event-study specification without cohort-aware correction.

## Completion Check

A causal event-study conclusion must defend the event timing, counterfactual forecast, window, absence of coincident shocks, and dependence-aware inference.

## Worked Example

> Source-grounded reconstruction from Huntington-Klein (2025); compressed and paraphrased.

A firm announces an unexpected merger. Define the information timestamp, estimate expected stock returns from a pre-event estimation window using a market model, and calculate abnormal returns during a narrow event window. Cumulate only over dates justified by information leakage and market reaction.

The design needs evidence that no other firm-specific information arrived in the same window. Use alternative reasonable estimation windows, placebo dates, and market models. Account for cross-event dependence if many firms announce around common market shocks.

The estimand is the market's immediate valuation response to the new information—not the eventual realized effect of completing the merger on operations. Extending the window may capture implementation information but also opens many time-based rival explanations. This distinction should appear in the claim, not only the limitations.

## Connects To

- [Ch15](ch15-simulation.md): evaluate false positives and forecasting behavior.
- [Ch18](ch18-difference-in-differences.md): multiple groups and staggered timing.
- [Ch23](ch23-under-the-rug.md): measurement and treatment ambiguity.
