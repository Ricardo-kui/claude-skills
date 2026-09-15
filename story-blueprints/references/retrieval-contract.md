# Runtime Exemplar Retrieval Contract

Use this contract when a full-section `write-*` request needs current-run learning references. Retrieval is stateless: it uses only the current invocation's research description, section goal, design, and evidence state. Do not save recommendations to project files.

## Request

```json
{
  "section": "introduction",
  "paper_type": "quantitative",
  "story_needs": ["clarify-theme", "establish-genuine-tension"],
  "theoretical_problem_form": [],
  "retrieval_signals": ["decision-consequence-chain"],
  "validated_conditions": ["genuine-theory-conflict", "same-causal-process-facets"],
  "max_results": 2
}
```

Allowed `story_needs`: `clarify-theme`, `introduce-main-characters`, `establish-genuine-tension`, `manage-multiple-storylines`, `theory-as-rising-action`, `methods-as-credible-arena`, `results-as-climax`, `unravel-mixed-evidence`, `return-to-opening`, `close-with-concrete-insight`.

`retrieval_signals` are optional, soft description terms supplied by the current invocation (for example, `decision-consequence-chain` or `external-monitoring`). They improve ranking through overlap with a card's `classification.retrieval_signals`; the absence of any particular signal never excludes a card. A card can also qualify through a matching `story_needs` or `theoretical_problem_form` tag. The catalog nevertheless requires at least one positive soft relevance match for cards that declare retrieval signals, so a broadly useful card is not injected into an unrelated writing call. Use signals to find structurally comparable learning objects without claiming that the current project has the exemplar's constructs, setting, or causal mechanism. Request and card tags are first normalized through the hand-curated synonym table at `references/tag-normalization.yaml`, then exactly intersected; matching is exact-string only — no embedding, no semantic similarity model, no substring matching.

`validated_conditions` are optional guardrails, but they are enforced as a **ranking penalty, not a hard gate**. Add one only when the current invocation has already established it from the author's own research description and story gate. When `validated_conditions` is empty or absent the validation state is `unknown` (not "no conditions validated"): cards that declare a `requires` list stay eligible and are annotated with their unmet conditions. Every required condition the request does not explicitly validate is reported in `unmet_conditions` and pushes the card down the ranking (currently −15 each); it never removes the card. Use conditions sparingly—only where absent conditions would make the learning move incoherent rather than merely less similar.

Candidates are evaluated through a fixed, auditable fallback ladder; every result is annotated with the tier that produced it:

- **tier 1** — `suitable == "yes"` plus strict relevance: when the request declares `retrieval_signals` a signals intersection is required, otherwise a `narrative_dynamics` / `theoretical_problem_form` hit is required.
- **tier 2a** — drop the `retrieval_signals` requirement; keep a `narrative_dynamics` / `theoretical_problem_form` hit.
- **tier 2b** — additionally relax `suitable` to `partial`.
- **tier 2c** — additionally drop the tag requirement; keep the same `outlet` or `paper_type`.

A tier whose only candidates are degenerate — every candidate lacks a `theoretical_problem_form` hit **and** carries at least one unmet required condition — does not lock the outcome. Retrieval continues to the next tier; if no tier produces a non-degenerate candidate, the last degenerate result is returned marked `low_confidence` with a stated reason. Current conditions are `genuine-theory-conflict`, `same-causal-process-facets`, `distinct-outcome-processes`, `shared-higher-order-theme`, `theory-domain-shift`, `cross-domain-mechanism-bridge`, `genuine-mechanism-paradox`, `parallel-pathway-redirection`, `cross-audience-valuation`, `shared-ability-baseline`, and `identity-criteria-misalignment`. The parallel-pathway pair requires more than two mediators or outcomes: the author must have established both an actual paradox in the mechanisms and a theory-grounded reason their distinct paths jointly redirect one higher-order process. The final three require more than multiple stakeholders: an observable external evaluation, a reason it has some ability relevance to the focal evaluator, and a specified identity or normative meaning that does not align. They are guardrails, not universal story types.

## Response

Return at most one primary learning object and one contrast object. If no card is a credible fit, return no recommendation. For every result show four elements: matching reason, one learnable move, one non-transferable condition, and one comparison question. `../scripts/retrieve_exemplars.py` produces the first three (matching reason, learnable move, non-transferable condition); the **comparison question is produced by the consuming skill**, not by the script, per `../v4/rhetoric-moves/_immediate-exemplar-protocol.md` step 3 (`推荐四问`).

Do not call this interface for sentence edits, title work, table navigation, or a request explicitly marked `--exemplars=off`.
