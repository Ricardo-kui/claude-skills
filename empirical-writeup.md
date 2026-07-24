---
name: empirical-writeup
description: Turn empirical analysis output into journal-ready methods, results, tables, figures, appendix material, and claim-evidence maps. Use when Codex needs to convert regressions, event studies, robustness checks, or analysis logs into management-journal prose and presentation artifacts. Routes to Pollock-structured write-methods and write-results skills.
---

# Empirical Writeup

## Overview

Use this skill after the analysis is already run or substantially stabilized. It keeps the empirical story anchored to actual evidence and routes the work across your installed writing, table, and figure skills.

## Default Stack

- `econ-visualization`: event studies, coefficient plots, descriptive figures
- `write-methods`: methods section (sample funnel, variable ordering, model specification) — Pollock Ch07 structured
- `write-results`: results section (4-beat rhythm, interaction reporting, robustness-by-threat) — Pollock Ch07 structured
- `paper-review`: cross-section alignment check (Story ↔ Methods ↔ Results; existing Discussion may be audited)

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
   - figures -> `econ-visualization`
   - methods prose -> `write-methods`
   - results prose -> `write-results`

Discussion generation is outside this workflow. An existing draft may be sent to `discussion-review`.

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
   - if table counts do not match the script, flag to user
   - if a figure implies a different story than the coefficient table, resolve that before polishing text

## Output Contract

- table inventory
- figure inventory
- methods or results subsection draft
- explicit caveat list
- appendix items still needed
