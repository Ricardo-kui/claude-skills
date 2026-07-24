---
name: write-discussion
description: Compatibility-only boundary for the retired Pollock Discussion writing skill. Use only when an older workflow explicitly invokes write-discussion; do not draft, template, or standardize Discussion prose. Route an existing Discussion draft to discussion-review and explain that the Pollock writing stack intentionally excludes Discussion generation.
---

# Retired Discussion Writing Boundary

## Policy

Discussion generation is intentionally outside this standardized writing package. Discussion depends on paper-specific literature accumulation, interpretation, and theoretical judgment that should not be reduced to reusable fill-in templates.

This compatibility skill must not:

- generate a Discussion outline, paragraph map, sentence skeleton, or completed prose;
- load the legacy templates in this directory;
- infer theoretical implications from Results;
- appear in default routers or implicit invocation.

## Handling

- If the user provides an existing Discussion draft, route it to `$discussion-review`.
- If the user requests a new Discussion, state that this Pollock stack supports Introduction, Theory, Methods, and Results writing only.
- If a whole manuscript is supplied, `$paper-review` or `$pollock-qc` may still diagnose whether the existing Discussion delivers the paper's contribution.

Legacy assets remain on disk only for path compatibility and historical recovery. They are not active writing guidance.
