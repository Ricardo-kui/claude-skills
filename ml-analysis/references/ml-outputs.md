# ML Output Contracts

## ML Design Packet

```text
Task and target:
Prediction point:
Label horizon:
Population and unit:
Feature-availability boundary:
Split rule:
Primary metric:
Untouched holdout policy:
Leakage risks and checks:
Noncausal claim ceiling:
Stop rules:
```

## ML Analysis Manifest

```text
Design Packet path:
Data Contract path:
Data Contract hash:
Runtime and environment artifact:
Data-build path:
Feature pipeline:
Baseline and candidate model ladder:
Tuning budget and search space:
Primary metric and selection rule:
Calibration plan:
Threshold or decision rule:
Error-slice plan:
Output paths:
Deviation policy:
```

## Evaluation Summary

```text
Selected model:
Validation metric(s):
Untouched holdout metric(s):
Calibration and threshold result:
Benchmark comparison:
Important error slices:
Reproduction status:
Interpretation caveats:
```

## ML Delivery Handoff

```text
Model artifact:
Preprocessing artifact:
Environment / lock artifact:
Scoring interface:
Validation and holdout evidence:
Calibration / threshold rule:
Known failure slices:
Monitoring and retraining needs:
Security or privacy limits:
Noncausal interpretation limit:
Open issues:
```

Use an Evidence Packet and writing handoff instead only when the requested endpoint is a paper or report.
