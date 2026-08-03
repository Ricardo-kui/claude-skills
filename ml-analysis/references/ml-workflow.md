# ML Workflow

## Model Ladder

1. naive benchmark
2. linear or logit baseline
3. regularized baseline
4. tree ensemble if justified by out-of-sample gain

## Metric Mapping

- regression -> RMSE, MAE, out-of-sample R-squared
- binary classification -> AUC, log loss, precision/recall, calibration
- imbalanced classes -> PR-AUC plus threshold-specific metrics
- ranking -> NDCG, MAP, top-k hit rate

## Leakage Checklist

- no future information
- no post-outcome variables
- no duplicated entities across incompatible splits
- engineered features reflect information available at decision time

## Standard Deliverables

- split rule
- feature inventory
- model comparison table
- selected model
- metrics by fold or time slice
- error analysis notes
