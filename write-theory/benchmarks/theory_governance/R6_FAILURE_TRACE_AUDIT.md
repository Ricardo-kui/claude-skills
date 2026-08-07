# R6 failed-task evidence audit (2026-08-07)

## Scope

Audit of the two R6 targeted losses (R6Q02, R6Q05) to classify each as (a)
SKILL/contract defect, (b) structural-protocol defect, (c) generator execution
error, (d) judge preference difference, or (e) preservation architecture gap,
and to decide whether a minimal repair is warranted. Evidence:
`R6_ACCEPTANCE_TASKS.yaml`, `R6_GOVERNED_OUTPUTS.md`, `R6_LEGACY_OUTPUTS.md`,
`R6_JUDGE_A.yaml`, `R6_JUDGE_B.yaml`, the catalog asset records, and
`corpus/sentences/moderation.md`, `corpus/sentences/hypothesis_forms.md`,
`corpus/variants/G_dialectical_opposition.md`. No R6 file, score, or label was
modified. Preservation losses R6Q07/R6Q08 are noted but not audited in depth:
both were single-judge or split decisions with sub-1.5-point margins, inside
the noninferiority band; they are logged for R7 watch, not repaired.

## R6Q02 (E, hypotheses; governed = X, 35.0 vs 38.0, both judges preferred legacy)

Chain: prompt asked for "signed conditional predictions" across a
sign-flipping boundary -> the governed derivation actually fixed opposite
per-state signs ("the two states predict opposite signs": threat attribution
→ voice ↓ under high stakes; relational investment → voice ↑ under low
stakes) -> but the hypothesis sentence collapsed into one comparative
statement: "Hypothesis 1: ... has a more negative effect ... when stakes are
high than when they are low", which fixes neither state's sign.

Asset-level mechanism: the governed route rendered
`theory:pattern:signed_more_positive_more_negative_moderation_sentence`, whose
registry description and source section (`corpus/sentences/moderation.md`
"异号增强/阻碍调节句") teach the comparative "more positive / more negative
under W" wording. That form family is designed for the dual-blade case where
per-state net signs are **not** theoretically fixed ("双刃剑净效应不定时").
R6Q02 was the opposite case: the derivation fixed each state's sign, for
which `corpus/sentences/hypothesis_forms.md`'s decision matrix prescribes the
Competing form ("[X] is positively related to [Y] for [A], but negatively for
[B]") or per-state signed hypotheses. The legacy output supplied exactly that
(H1 negative under high stakes; H2 positive under low stakes).

Root cause: the corpus contains both form families but **no routing rule
between them**. Nothing tells the generator: derivation fixes per-state signs
→ per-state signed form; per-state net signs theoretically unfixed →
comparative form. The only signed-moderation sentence asset reachable by
query teaches the comparative form unconditionally, so a correct retrieval
can still produce the weaker form. R5Q02 produced per-state signed hypotheses
(H1a/H1b) and tied, confirming the behavior is ungoverned variance, not a
stable capability.

Classification: **(b) structural-protocol gap (missing derivation→form
routing rule), with a (c) execution component (two blades merged into one
sentence even within the chosen form family).** Repair warranted.

## R6Q05 (G, propositions; governed = X, 36.0 vs 36.0, judge A legacy / judge B tie → loss)

Chain: both routes locked the two mechanisms onto the same outcome (supplier
retention) — the R5 outcome-locking repair held, and judge B explicitly
credited the governed symmetry. The divergence is in the dominance rule:
governed derived a single blended threshold (violations exceeding the buyer's
remediation capacity); legacy decomposed dominance into two independently
testable conditions, the severity-minus-expectation gap (a property of the
information/uncertainty channel) and remediability (a property of the
liability channel). Judge A preferred the decomposed rule; judge B scored the
pair a tie with equal dimension means.

Root cause assessment: the current G rule (post-R5 repair) requires dominance
conditions to be derived from mechanism properties rather than listed
correlates; the governed output satisfied that rule. What it does not state
is that when the two mechanisms have **independent strength drivers**, each
dominance condition should bind to one mechanism's observable property,
rather than being merged into a single threshold. The legacy advantage is
real but narrow: equal means, split judges.

Classification: **borderline (d)/(b-minor).** A one-line principle is
defensible — per-mechanism binding of dominance conditions — because it also
generalizes the R5Q11 lesson; anything more (prescribing two conditions,
threshold language) would be templating. Minimal repair warranted.

## Repairs implemented (rule-level only)

1. **Derivation→form routing for sign-flipping boundaries (R6Q02).**
   - `references/governed-generation-guards.md` (E section) and the registry E
     contract: if the derivation fixes the sign in each boundary state, state
     signed predictions per state (Competing form or per-state hypothesis
     pair); reserve comparative "more positive/more negative" wording for
     cases where per-state net signs are not theoretically fixed.
   - `corpus/sentences/hypothesis_forms.md` decision matrix: routing note at
     the Competing row.
   - `corpus/sentences/moderation.md` comparative-form section: applicability
     boundary (only when per-state net signs are unfixed).
2. **G per-mechanism dominance binding (R6Q05).**
   - `corpus/variants/G_dialectical_opposition.md`: when the two mechanisms
     have independent strength drivers, state dominance conditions per
     mechanism (each bound to one mechanism's observable property) rather
     than merged into a single threshold; one matching QC line.

## Forward check (fresh tasks, not R6 items)

Two fresh micro-tasks answered after the repair:

**FC01 (E, hypotheses, sign-flip).** Prompt: how does employee monitoring
intensity affect trust-repair behavior under high versus low prior procedural
fairness? Post-repair output states per-state signed hypotheses: H1: under
low prior procedural fairness, monitoring intensity is negatively related to
trust-repair behavior (read as confirmed distrust → defensive compliance);
H2: under high prior procedural fairness, monitoring intensity is positively
related to trust-repair behavior (read as caring oversight → reciprocated
stewardship); no unconditional main effect. The form routing rule held: the
derivation fixed both signs, so the comparative "more positive/negative"
collapse was not used. PASS.

**FC02 (G, propositions, independent drivers).** Prompt: symmetric benefit
and burden mechanisms through which dual-class listing shapes analyst
coverage optimism, with reconciliation. Post-repair output locks both
mechanisms on the same outcome (coverage optimism) and states dominance per
mechanism: the benefit channel (governance-signaling clarity) dominates when
the signal is externally verifiable — its driver; the burden channel
(entrenchment salience) dominates when institutional monitoring intensity is
low — its driver. The two conditions are independently testable and not
merged into one threshold. PASS.

Regression: 23/23 governance tests pass after the repair; catalog audit
unchanged (7 architectures, 120 assets); the new E contract item appears in
`generation-contract` output. Single-generator demonstration only; formal
acceptance requires a pre-registered R7 blind evaluation.
