---
name: empirical-writeup
description: Package verified empirical outputs into an Evidence Packet and route journal-ready tables, figures, methods, results, and appendix work. Use after execution and verification to map claims to regressions, event studies, robustness checks, ML metrics, scripts, and caveats. Do not authorize claims that exceed the Design Packet or Verification Report.
---

# Empirical Writeup

## Overview

Use this skill after execution is stabilized and verification is complete. It constructs the evidence boundary before prose drafting and routes the work across installed writing, table, and figure skills.

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
- Design Packet and Analysis Manifest
- Verification Report and its disposition
- Run Manifest and Results Inventory
- target journal or field when available

For direct entry with externally produced or user-asserted verified tables, construct a provisional Evidence Packet. Mark verification provenance as `user_asserted`, record missing design or run artifacts, and narrow claim language accordingly. Do not fabricate formal verification.

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
   - stop if verification disposition is `fail`; a `conditional` disposition must carry its unresolved conditions into every affected claim

4. Separate sections cleanly:
   - methods: sample, measures, model choice
   - results: hypothesis test, magnitude, interpretation
   - robustness: threat, test, implication
   - appendix: extra specs, coding details, supplementary figures

5. Reconcile disagreements before drafting final prose:
   - if table counts do not match the script, use `review-code`
   - if a figure implies a different story than the coefficient table, resolve that before polishing text

## Evidence Packet Contract

- table inventory
- figure inventory
- claim-to-evidence-to-script map
- effect magnitude and uncertainty
- authorized, qualified, and prohibited claims
- explicit caveat and unresolved-issue list
- appendix items still needed
- recommended writing skill and section target

## Reference

Read [references/writeup-matrix.md](references/writeup-matrix.md) for the artifact-to-skill routing table and claim-strength rules.
Read [references/writeup-outputs.md](references/writeup-outputs.md) for standard evidence maps and prose templates.
