# Feedback Protocol

Use this protocol when the user criticizes, rejects, redirects, or constrains an output produced with write-results.

## 1. Capture triggers

Capture feedback when the user:

- says the prose is stiff, list-like, generic, repetitive, or AI-like;
- corrects section or hypothesis ordering;
- says an analysis does not explain the problem it addresses;
- requests headings, a different evidence sequence, or a different reporting unit;
- bans a word, phrase, construct, or sentence pattern;
- sets a voice/tone benchmark or rejects defensive and self-referential metadiscourse;
- identifies a factual, table, sample, estimand, or interpretation error;
- rejects a corpus-derived pattern or asks for a different exemplar family.

In revision mode, also capture explicit dissatisfaction and corrections preserved in the active draft's revision records. Signals include `用户裁定`, `禁用`, `不恢复`, `作废`, `AI 痕迹`, and a documented replacement of a rejected phrase. Do not register every historical edit—only an explicit rejection, constraint, or corrective preference.

Do not record ordinary new instructions that do not criticize prior output. Do not infer satisfaction from silence.

## 2. Immediate response

1. Correct the authorized manuscript text first.
2. State the normalized rule internally in positive, executable form.
3. Choose the narrowest valid scope.
4. Record the feedback if local skill-state writes are within the current task; otherwise preserve a ready-to-register record in the response or project notes.

## 3. Scope and categories

Scopes:

- `skill`: broadly applicable to write-results
- `project`: applies to one manuscript or project
- `section`: applies to a Results evidence function such as baseline, selection, endogeneity, mechanism, heterogeneity, or robustness
- `estimator`: applies to one estimator family or corpus branch

Categories:

- `source_intake`
- `section_order`
- `hypothesis_order`
- `analysis_logic`
- `heading_navigation`
- `paragraph_cohesion`
- `voice_tone`
- `terminology`
- `language_lock`
- `evidence_interpretation`
- `mixed_evidence`
- `corpus_fit`
- `interface`

## 4. Registry schema

The canonical registry is `feedback-registry.json` in this directory. Each record contains:

```json
{
  "id": "stable fingerprint",
  "scope": "skill | project | section | estimator",
  "project": "optional project identifier",
  "section": "optional Results section",
  "estimator": "optional estimator family",
  "category": "one category above",
  "severity": "revise | reject",
  "rule": "positive executable rule",
  "reason": "what failed and why",
  "evidence": "short user wording or failure description",
  "source": "conversation/project revision log/etc.",
  "benchmark": "optional exemplar or style benchmark",
  "supersedes": ["optional prior rule id or legacy-advice label"],
  "prohibited_patterns": ["optional regex for deterministic linting"],
  "status": "active | retired",
  "count": 1,
  "first_seen": "YYYY-MM-DD",
  "last_seen": "YYYY-MM-DD"
}
```

Use `../scripts/record_feedback.py` to add or update records. The script deduplicates by scope, applicable project/section/estimator context, category, and normalized rule; it increments `count` and preserves the most recent evidence.

When applicable records contain `prohibited_patterns`, run `../scripts/lint_results_language.py <Results path> --project <project name>` after revision. The default manuscript boundary stops before `## 生成后自检记录`; use `--whole-file` only when intentionally auditing the historical log as well.

## 5. Applying feedback

Before revision-mode generation:

1. Load all active `skill` rules.
2. Load active rules matching the project.
3. Load active rules matching the section and estimator being written.
4. Remove any registry rule id or legacy advice label named by an applicable rule's `supersedes` field.
5. Resolve remaining conflicts using: current user decision > matching section/estimator rule > project rule > skill rule > corpus default.
6. Add the selected rules, benchmark, prohibited patterns, and superseded advice to `revision_constraints`.

A superseded instruction remains in the historical log but has no generative authority. This applies equally to old wording suggestions and corpus preferences; do not revive them merely because they appear later in the file or have a memorable “signature” phrase.

Project-specific terminology must not become a global prohibition. A cross-project rule requires either explicit user generalization or repeated evidence across at least two projects.

## 6. Corpus feedback

Do not automatically rewrite corpus variants from one criticism.

- `count = 1`: apply the rule in future generation; no corpus mutation.
- repeated within one project: strengthen the project constraint and regression case.
- repeated across at least two projects, or explicitly generalized by the user: inspect the relevant slot/corpus variant for ADD/EXTEND/REPLACE.
- estimator-specific criticism may also update the legacy `usage_stats` in `_evidence_registry.yaml`, but the detailed JSON registry remains canonical.

Any corpus mutation still requires the preview-and-confirm workflow of `distill-results-exemplar`.

## 7. Retirement

Retire rather than delete a registry rule when:

- the user explicitly reverses it;
- the manuscript changes such that it no longer applies;
- a more precise rule supersedes it.

Record the replacement rule before retiring the old one. Never erase the evidence trail merely because a later output passes.
