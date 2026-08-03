---
name: empirical-writeup
description: Turn empirical analysis output into journal-ready methods, results, tables, figures, appendix material, and claim-evidence maps. Use when Codex needs to convert regressions, event studies, robustness checks, ML metrics, or analysis logs into management-journal prose and presentation artifacts.
---

# Empirical Writeup

## Overview

Use this skill after the analysis is already run or substantially stabilized. It keeps the empirical story anchored to actual evidence and routes the work across your installed writing, table, and figure skills.

## Default Stack

- `latex-tables`: regression, balance, and summary-statistics tables
- `econ-visualization`: event studies, coefficient plots, descriptive figures
- `write-methods-and-results`: methods, results, robustness, and claim-evidence alignment
- `write-discussion-and-conclusion`: downstream implications after the empirical middle is stable
- `review-code`: use when prose, tables, and scripts appear inconsistent

## Required Inputs

- output tables or raw model objects
- figure-ready estimates or plotting data
- variable definitions and sample notes
- model choice and SE or clustering rule
- key caveats and robustness notes
- target journal or field when available

## Writeup Workflow

1. Build an evidence map:
   - claim
   - supporting table or figure
   - script or model source
   - caveat or limit

2. Route the artifact creation:
   - tables -> `latex-tables`
   - figures -> `econ-visualization`
   - prose -> `write-methods-and-results`

3. Enforce claim discipline:
   - association language for associative designs
   - causal language only when the design and diagnostics support it
   - support, partial support, or no support should track the actual estimates

4. Separate sections cleanly:
   - methods: sample, measures, model choice
   - results: hypothesis test, magnitude, interpretation
   - robustness: threat, test, implication
   - appendix: extra specs, coding details, supplementary figures

5. Reconcile disagreements before drafting final prose:
   - if table counts do not match the script, use `review-code`
   - if a figure implies a different story than the coefficient table, resolve that before polishing text

## Output Contract

- table inventory
- figure inventory
- methods or results subsection draft
- explicit caveat list
- appendix items still needed

## Reference

Read [references/writeup-matrix.md](references/writeup-matrix.md) for the artifact-to-skill routing table and claim-strength rules.
Read [references/writeup-outputs.md](references/writeup-outputs.md) for standard evidence maps and prose templates.
