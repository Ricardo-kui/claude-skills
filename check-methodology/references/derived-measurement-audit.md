# Derived Measurement Audit

Use this branch only when a treatment, outcome, covariate, feature, or label is produced by human coding, text/image/audio processing, an LLM, or another fitted model. `check-methodology` owns measurement validity and claim limits; `review-code` owns computational provenance and reproducibility.

## Required record

Request or reconstruct a Derived Measurement Record containing:

- construct and role in the analysis;
- source corpus, inclusion rule, observation unit, and time boundary;
- coding or generation pipeline, including human and automated stages;
- model/provider/version, prompt or schema version, inference settings, call date, parsing, retries, and post-processing when applicable;
- gold-standard or adjudicated sample design and separation from development data;
- validation metrics overall and for substantively important classes, groups, and periods;
- source-reuse map showing whether two analysis variables share records, prompts, models, or upstream labels;
- stability, uncertainty, correction, or sensitivity evidence;
- proposed claim ceiling.

Missing records are findings, not permission to infer a clean measurement process.

## Audit sequence

1. **Role:** State whether the derived quantity is the treatment, outcome, confounder, mediator, feature, prediction label, or exploratory descriptor. The same error rate can have different inferential consequences in different roles.
2. **Construct and timing:** Check that the coding target matches the theoretical construct, that source information existed at the required decision or treatment time, and that prompts, training examples, or annotators did not receive future outcomes or prohibited post-treatment information.
3. **Validation:** Prefer a blinded, adjudicated human reference set sampled from the target corpus. Match metrics to the task; report class- or slice-specific performance when aggregate accuracy can hide rare-class failure. Treat human labels as fallible and report their protocol or agreement when material. Do not impose a universal sample-size or metric threshold without a project- or field-specific basis.
4. **Independence:** Map shared source documents, model calls, prompts, training examples, and post-processing. When treatment and outcome, or predictor and label, are derived from the same material or error mechanism, test whether mechanical dependence can create the reported relationship. Use source separation, sample splitting, independent coding, or an explicit error model when the threat is material.
5. **Stability:** Inspect repeat-call, batch, temporal, model-version, prompt-version, and alternative-coder sensitivity in proportion to the variable's importance. A deterministic-looking pipeline does not establish semantic stability.
6. **Inferential effect:** Connect measurement error to the estimand or metric. Evaluate misclassification, attenuation, differential error, selection, calibration, or uncertainty propagation as appropriate. A validation score alone does not authorize treating the measure as truth.
7. **Synthetic boundary:** Treat synthetic data or model-simulated respondents as debugging, design, privacy, or exploratory artifacts unless independently validated for the intended population claim. Results generated entirely by the model cannot validate claims about human or organizational behavior by themselves.

## Disposition rules

Return `fail` for the affected claim when any of these holds:

- a core derived variable has no traceable construction pipeline;
- future, outcome, or post-treatment information contaminates its construction contrary to the design;
- shared generation creates an unresolved mechanical link between variables on both sides of the claimed relationship;
- synthetic records or model-simulated respondents are used as standalone population or causal evidence.

Return at most `conditional` when provenance exists but validation, stability, slice coverage, or measurement-error consequences remain materially unresolved. Return `pass` only when evidence is proportionate to the variable's role and every remaining limitation is carried into the claim ceiling.

## Verification output

Add:

- derived variable and analytic role;
- provenance completeness;
- construct and temporal validity;
- reference-set design and validation results;
- source-reuse, leakage, and mechanical-dependence assessment;
- stability and measurement-error assessment;
- authorized, qualified, and prohibited uses of the variable.

This protocol extracts general safeguards from a secondary methods handbook. Verify current field standards, primary methods literature, provider behavior, and software semantics before publication-facing claims or live implementation.
