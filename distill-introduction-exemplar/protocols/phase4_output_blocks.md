# Phase 4 governed output blocks

Load this file only when a distillation produces a corpus or skill-design recommendation.

## `governance_plan`

Phase 4 emits one `actions` mapping consumed only by
`../../write-introduction/scripts/introduction_corpus_governance.py`. Do not edit corpus
Markdown, the evidence registry, routing, or style sections directly.

```yaml
actions:
  - action: ADD_REFERENCE
    target_parent_id: hooks:03-data-shock
    nearest_neighbor_id: hooks:03-data-shock:vC
    title: 跨层级升级型
    source_paper: author_year (SMJ)
    template: "[Trend] escalates into [cross-level consequence]."
    capability_loss_if_merged: "新增跨层级升级这一可迁移证据载体。"
    applicability: "存在可核验趋势与跨层级后果时。"
    taboo: "不得用单一案例伪装总体趋势。"
```

Use this default order: `NONE → REUSE → EXTEND_SOURCE → ADD_REFERENCE → PROPOSE_VARIANT`.
`PROMOTE` requires one unique `source_papers` entry for every claimed paper, in addition to
the evidence status and verification basis. `MERGE` and `DEPRECATE` require explicit review.
Routing, schema, and stage-gate changes may only use `PROPOSE_ROUTING_CHANGE`.

Run, in order:

```powershell
python ../../write-introduction/scripts/introduction_corpus_governance.py apply-plan plan.yaml --dry-run
python ../../write-introduction/scripts/introduction_corpus_governance.py apply-plan plan.yaml
python ../../write-introduction/scripts/introduction_corpus_governance.py validate
python ../../write-introduction/scripts/introduction_asset_catalog.py audit
```

## Style observations

Keep paper-specific tone, rhythm, and prose observations in the Phase 3 distillation report.
`style_profile_enrichment` is retired: there is no active cross-template style consumer and no
transactional style-write action. A proposed change to a corpus `## 风格画像` section is a
review-only `skill_design_feedback` observation until a governed style interface exists.

## `skill_design_feedback`

Always include this block in Phase 4. If no rule-level issue exists, emit `observations: []`.
Use a stable `defect_id`; do not turn a corpus gap into a routing or schema defect.

```yaml
skill_design_feedback:
  batch_id: "batch_YYYY-MM-DD"
  last_updated: "YYYY-MM-DD"
  observations:
    - defect_id: "conversation-gap-coupling"
      classification: "routing_defect"
      current_rule: "[current rule in plain language]"
      rule_excerpt: "[verbatim excerpt from target]"
      rule_locator: "[heading or line hint]"
      target: "write-introduction/academic-writing-corpus/_routing_tables.yaml"
      diagnosis: "[why the rule, rather than the corpus, is insufficient]"
      absolute_rule: false
      decisive_falsifier: false
      risk: "low / medium / high"
      evidence:
        papers:
          - id: "author_year"
            journal: "AMJ"
            evidence_anchor: "Introduction P2-P3: [functional evidence]"
            evidence_quality: "full_text_verified / functional_summary / metadata_only"
      proposed_change:
        action: "decouple / conditionalize / add_branch / correct_validator / revise_output_contract"
        summary: "[minimal bounded change]"
      regression_cases:
        positive:
          prompt: "[task that exercises the proposed branch]"
          expected_invariants: ["[required functional behavior]"]
        preservation:
          prompt: "[task that must retain the old behavior]"
          expected_invariants: ["[behavior that must remain]"]
      resolution: null
```

`rule_excerpt` must be copied from the target. Only full-text evidence may support a core-rule
change. Run `_update_design_feedback.py` to aggregate evidence; it never edits the writing
skill. A later core patch needs explicit authorization, the recorded regression cases, and
successful validation.
