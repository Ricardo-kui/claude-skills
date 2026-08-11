# Legacy Evidence Layer

The 59 v0.3 blueprints are a read-only evidence layer. Their sole growth function is to help the current v0.4 seed corpus find a small number of papers worth re-reading in full. They are not a runtime exemplar library, a general story-rule corpus, or a project-story selector.

## Authority and use

- `blueprints/*.md` remains unchanged historical source material.
- `legacy/legacy-manifest.json` is a generated, read-only derivative. Rebuild it with `scripts/build_legacy_manifest.py`; do not edit it by hand.
- `legacy/legacy-overrides.yaml` is the only place to add human-verified fields that v0.3 did not encode. To mark an item `candidate`, add a `seed_relations` record naming the v0.4 seed and the comparison question.
- `scripts/query_legacy_candidates.py` supports discovery for comparison and re-reading. Its output is never a writing recommendation and always has `runtime_eligibility: no`.
- Only a full v0.4 re-reading can change an item's `migration_status` to `reviewed` or make an item eligible for runtime retrieval.

## Interpretation rules

`legacy_coverage_confidence` records how complete the earlier reading claims to be. It is not a story-quality assessment, proof of a good introduction, proof of causal credibility, or permission to reuse a story form.

`legacy_interpretation` retains the old knot and resolution labels only as historical analyst interpretation. It is not a taxonomy for the user's project, a write-skill routing value, or a v0.4 retrieval condition.

## Seed-led migration lifecycle

```text
v0.4 seed → discovery query → candidate → full-text re-reading → reviewed → migrated
                                                        └──────────────────→ retained_as_legacy
```

The six current v0.4 cards—Zhou, Ridge, Wowak, Zhong, Post, and Fini—are the only active seeds. Use `candidate` only when a seed exposes a concrete comparison question, a real writing call exposes a retrieval blind spot, or a repeated mis-match needs an adversarial contrast. A historical knot label alone is never enough.

For every candidate, record:

```yaml
seed_relations:
  - seed_id: "[one of the current v0.4 card IDs]"
    relation_hypothesis: "[what may be structurally comparable or contrastive]"
    comparison_question: "[what full-text re-reading must decide]"
    status: proposed | confirmed | refuted
```

`reviewed` requires a complete v0.4 story reading and assessment. `migrated` requires a valid v0.4 card; it does not imply the legacy card was correct in every respect.

## What the legacy manifest must not do

- Do not derive default writing moves from the 59 cards.
- Do not turn a `legacy_interpretation.knot_primary` match into a recommendation.
- Do not promote a candidate because it shares a journal, topic, U-shape, multiple outcomes, or an old story label with a seed.
- Do not fill a v0.4 card from legacy text alone; re-read the full paper first.

## Commands

```powershell
python scripts/build_legacy_manifest.py
python scripts/validate_legacy_manifest.py
python scripts/query_legacy_candidates.py --legacy-knot paradigms-at-war --limit 3
```
