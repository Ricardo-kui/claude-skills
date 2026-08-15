# Draft Revision Protocol

Use this protocol whenever the user supplies an existing Methods draft, revision history, Decision Register, or asks to continue/revise prior work.

## 1. Lock the current text

Before planning or rewriting, read:

1. the current manuscript body;
2. its revision records and explicit user decisions;
3. the current Results draft when section ownership is disputed;
4. actual data, tables, code, or Methods-facing diagnostics needed to verify factual claims;
5. only theory materials confirmed to be current.

Do not substitute an earlier draft, conversation summary, or stale theory file for the current text. Separate manuscript prose from audit/revision material; historical examples are evidence about constraints, not language to restore.

## 2. Build `revision_constraints`

Capture at least:

```yaml
revision_constraints:
  authorized_scope: full_draft | named_sections | local_passage
  preserve:
  remove:
  methods_results_boundary:
  section_order:
  slot_assignments:
  sample_and_time_scope:
  estimands_and_units:
  terminology:
  voice_benchmarks:
  prohibited_patterns:
  superseded_advice:
  stale_sources:
  unresolved_conflicts:
```

Use this priority: current user decision > matching section/design-type feedback > project feedback > current verified manuscript facts > active skill feedback > corpus default. Mark conflicts; do not silently blend incompatible versions.

## 3. Preserve Methods–Results ownership

- Methods contains the empirical setting, baseline data and sample, construct operationalization, controls, and the baseline estimator/identification strategy.
- A selection correction, IV, matching design, or diagnostic belongs in Methods only when it is part of the baseline estimator or determines the estimator choice.
- Supplemental endogeneity checks, alternative measures, sensitivity analyses, mechanisms, heterogeneity, and their findings belong in Results unless the user explicitly changes the paper architecture.
- When a variable first appears only in Results, Results must define its source, construction, timing, and sample boundary; Methods should not retain an orphaned preview.

## 4. Keep each slot's job distinct

- M1 establishes why the setting is empirically useful.
- M2 reports baseline sources and an auditable sample funnel.
- M3–M5 define and justify measures; do not preview estimator mechanics or empirical findings.
- M6 links controls to specific rival explanations without turning into a variable inventory.
- M7 explains the baseline estimator, estimand, fixed effects, standard errors, and diagnostic basis for the specification.
- M8 covers identification or validity only when it is integral to the baseline design.
- M10 is optional and must not preview coefficients or verdicts.

## 5. Voice and tense

- Use active past tense for completed research procedures: `we obtained`, `we matched`, `we measured`, `we estimated`.
- Use present tense for definitions, institutional facts, equation terms, estimator properties, and interpretation conventions.
- State measurement limitations and scope conditions directly. Do not add defensive closers, author-honesty commentary, or generic claims that a choice “mitigates concerns” without explaining the concrete threat.
- Preserve standard technical terms while rewriting source-specific sentence architecture when similarity risk is high.

## 6. Completion failures

A revision is incomplete if it:

- relies on an obsolete theory or an earlier manuscript version;
- revives a removed construct, variable, hypothesis, section, or old wording suggestion;
- moves a Results-only analysis back into Methods without a baseline-design reason;
- changes sample years, severity classes, units, or estimands without evidence;
- uses current-tense/passive procedural prose contrary to an active project rule;
- reports findings, support verdicts, or robustness outcomes in Methods;
- passes corpus similarity by copying a memorable sentence skeleton.
