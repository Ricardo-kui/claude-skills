# Feedback Protocol

Use this protocol when the user criticizes, rejects, redirects, or constrains an output produced with write-methods.

## 1. Capture triggers

Capture feedback when the user:

- says the Methods prose is stiff, defensive, generic, overtechnical, repetitive, or AI-like;
- corrects Methods–Results ownership, section order, or slot assignment;
- corrects a sample, date window, unit of analysis, estimand, variable definition, or estimator rationale;
- bans a word, construct, sentence pattern, voice, or tense;
- identifies an obsolete theory or source that must no longer govern the draft;
- sets an exemplar or voice benchmark;
- rejects a corpus-derived pattern or declares prior wording advice void.

In revision mode, also scan the current draft's revision records for explicit decisions marked by signals such as `用户裁定`, `禁用`, `撤出`, `删除`, `作废`, `AI 痕迹`, or a documented replacement. Do not register every edit; capture explicit dissatisfaction, constraints, and corrective preferences.

## 2. Immediate response

1. Correct the authorized manuscript text first when the task includes manuscript revision.
2. Normalize the criticism into a positive, executable rule.
3. Choose the narrowest valid scope.
4. Record the rule when skill-state writes are authorized.

## 3. Scope and categories

Scopes:

- `skill`: broadly applicable to write-methods
- `project`: one manuscript or project
- `section`: one Methods function or slot
- `design_type`: one design or estimator family

Categories:

- `source_intake`
- `methods_results_boundary`
- `section_order`
- `slot_assignment`
- `sample_scope`
- `estimand_definition`
- `terminology`
- `language_lock`
- `voice_tone`
- `measurement_argument`
- `estimator_justification`
- `evidence_interpretation`
- `corpus_fit`
- `interface`

## 4. Registry schema

The canonical feedback store is `feedback-registry.json`. Each record contains:

```json
{
  "id": "stable fingerprint",
  "scope": "skill | project | section | design_type",
  "project": "optional project identifier",
  "section": "optional Methods section or slot",
  "design_type": "optional design family",
  "category": "one category above",
  "severity": "revise | reject",
  "rule": "positive executable rule",
  "reason": "what failed and why",
  "evidence": "short user wording or failure description",
  "source": "conversation/revision log/etc.",
  "benchmark": "optional exemplar or style benchmark",
  "supersedes": ["optional prior rule id or legacy-advice label"],
  "prohibited_patterns": ["optional regex for deterministic linting"],
  "status": "active | retired",
  "count": 1,
  "first_seen": "YYYY-MM-DD",
  "last_seen": "YYYY-MM-DD"
}
```

Use `../scripts/record_feedback.py` to add or update records. Repetition increments `count` while preserving the rule's rationale, latest evidence, scope, benchmark, and executable constraints.

## 5. Applying feedback

Before revision-mode generation:

1. Load all active skill rules.
2. Load active rules matching the project.
3. Load matching section and design-type rules.
4. Remove registry rule IDs or legacy advice labels named in `supersedes`.
5. Resolve conflicts using: current user decision > section/design-type rule > project rule > skill rule > corpus default.
6. Add selected rules, benchmarks, prohibited patterns, and superseded advice to `revision_constraints`.

A superseded instruction remains visible in the historical record but has no generative authority. Project terminology and manuscript-specific architecture must not become global rules without explicit user generalization or repeated evidence across projects.

When applicable records contain `prohibited_patterns`, run `../scripts/lint_methods_language.py <Methods path> --project <project name>`. By default the scanner stops before a dated revision record or `## 生成后自检记录`; use `--whole-file` only to audit the historical log intentionally.

## 6. Relationship to the corpus evidence registry

`feedback-registry.json` is the canonical store for user decisions. `corpus/_evidence_registry.yaml` remains a secondary corpus-routing asset:

- detailed criticism, wording decisions, and project constraints belong in the JSON registry;
- aggregate design-type revise/reject counts may be synchronized later for corpus maintenance;
- a count never replaces the reason, evidence, scope, or executable rule;
- one project's criticism does not automatically rewrite a design variant;
- corpus mutation requires explicit user direction or repeated cross-project evidence and the `distill-methods-exemplar` workflow.

## 7. Retirement

Retire rather than delete a rule when the user reverses it, the manuscript changes, or a more precise rule supersedes it. Record the replacement before retiring the old rule.
