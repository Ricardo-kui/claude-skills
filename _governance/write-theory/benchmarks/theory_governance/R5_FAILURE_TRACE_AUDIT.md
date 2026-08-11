# R5 failed-task evidence audit (2026-08-07)

## Scope and evidence boundary

This audit covers the five R5 tasks the pre-registered evaluation marked as
governed losses: R5Q01, R5Q03, R5Q06 (targeted) and R5Q11, R5Q12
(preservation). Evidence used: `R5_ACCEPTANCE_TASKS.yaml` (prompts),
`R5_GOVERNED_OUTPUTS.md`, `R5_LEGACY_OUTPUTS.md`, `R5_JUDGE_A.yaml`,
`R5_JUDGE_B.yaml`, `R5_LABEL_MAP.yaml`, and the current skill internals
(SKILL.md, `references/governed-generation-guards.md`,
`references/phase-3-hypothesis-derivation.md`,
`references/phase-4-qc-alignment.md`,
`corpus/subprotocols/process_transition_operators.md`,
`corpus/variants/{B,E,G}_*.md`, `corpus/_evidence_registry.yaml`,
`tests/test_theory_governance.py`). No R5 file, score, label, or threshold was
modified. Each failure is classified as: (a) SKILL/contract defect, (b)
structural-protocol defect, (c) generator execution error, (d) judge
preference difference, or (e) preservation architecture gap.

## R5Q01 (E, governed = X, critical failure; both judges preferred legacy)

Chain: prompt explicitly required "place the boundary state before its
interpretation and mechanism" -> governed prose complied ("confront a binding
resource constraint before interpreting the project") -> governed argument
graph wrote `Data-center expansion -> high water scarcity -> residents read
added withdrawals as a threat -> ...`, placing the boundary state downstream
of X. Judge B recorded `unsupported_causal_language`; judge A penalized the
same graph without a critical flag.

Root cause: the governed rule's own notation. Three governed locations encode
the E graph as a linear chain beginning `X -> boundary state -> ...`:

- `SKILL.md` step 4: "E 型逐边记录 X → boundary state → actor interpretation/capacity → mechanism → outcome"
- `references/governed-generation-guards.md` line 20: `X → boundary state → actor interpretation/capacity → named mechanism → Y`
- `corpus/_evidence_registry.yaml` line 2939 (returned verbatim by
  `generation-contract`; locked by `tests/test_theory_governance.py:99`)

Read literally, the notation makes the boundary state a downstream node of X.
The R4 repair ("place the boundary state before the condition-specific
interpretation and mechanism") added the correct prose sentence but kept the
contradictory chain, so rule text and notation disagree. The generator
followed the notation in the graph and the prose sentence in the rationale,
producing an internally inconsistent output. The same flawed graph shape
appears in the R5Q02 governed output and went unflagged, so the defect is
systematic; only its detection is stochastic. No graph–prose consistency
check exists in `references/phase-4-qc-alignment.md`.

Classification: **(b) structural-protocol defect (notation level), with a
(c) execution component (no consistency self-check).**

## R5Q03 (D, governed = Y, loss; judge A penalized, judge B tie)

Chain: prompt asks for a process account "from pilot evaluation to
institutional adoption" -> governed output supplied a complete boundary
handoff (actors, joint threshold, signed readiness memorandum as
pre-next-stage marker, failed branch) but ended at "capital committee
authorizes institutional procurement and implementation planning" -> legacy
carried authorization through to "routinized institutional adoption"
(department heads embedding the tool in schedules, protocols, accountability).
Judge A: "X carries the transition through authorization into routinized
departmental adoption, whereas Y ends closer to procurement and implementation
planning."

Root cause: the stage-boundary operator
(`corpus/subprotocols/process_transition_operators.md`) and the D generation
contract define one boundary crossing ending at "next actor/state". Neither
requires the chain to close at the terminal process state named in the task.
"Next state" is the immediate successor; nothing chains additional handoffs
to the terminal state. The governed output therefore satisfied every written
rule while stopping one handoff short of the prompt's named endpoint.

Classification: **(b) structural-protocol gap (missing terminal-state closure
rule).** The marker discipline itself worked and must not be weakened: the
fix must not relabel the marker or the immediate next state as the outcome.

## R5Q06 (D, governed = X, loss; judge B pairwise preference only)

Chain: both judges gave both outputs perfect scores on all eight dimensions.
Only judge B's pairwise vote went to legacy, citing "inclusion of stalled and
exited founders and its redesign-versus-selection question" as "a slightly
stronger open empirical agenda."

Comparison: governed open agenda — "research must establish which translation
rules and committee judgments actually generate each trace" (open, but
generic). Legacy open agenda — "whether negative founder feedback triggers
redesign or merely selects out difficult ventures" (two rival interpretations
of the same trace; evidence can discriminate them).

Root cause assessment: the feedback-transport operator requires per-branch
observable traces but says nothing about the form an open empirical agenda
must take when the task requires one. This is the weakest of the three
targeted failures: zero dimension-level penalties, one judge's marginal
preference. It is consistent with (d) judge preference; the only defensible
rule-level reading is a narrow (b) gap about the *form* of a required open
agenda.

Classification: **borderline (d)/(b-minor).** Any fix must be a single QC
principle (open agenda = a question whose rival answers map to different
branches or interpretations of the same trace), not a template sentence.

## R5Q11 (G, preservation, governed = Y, loss; both judges penalized, 35.5 vs 40)

Chain: governed benefit mechanism terminates on "decision confidence / deal
advancement" while the burden mechanism terminates on "favorable deal
evaluation" — the two mechanisms are not locked to the same outcome. The
governed reconciliation lists correlates ("mature data plus manageable
dependency" vs "fragmented data plus high dependency") rather than deriving
when each mechanism dominates. Judge A: "X keeps both mechanisms on the same
evaluative outcome and derives dominance from remediability and value-capture
timing more coherently." Judge B: "Y's uncertainty reduction more directly
supports confidence than favorable evaluation."

Root cause: `corpus/variants/G_dialectical_opposition.md` requires symmetric
step counts, a dialectical-turn marker, and theory-based reconciliation, but
nowhere states that (i) both opposing mechanisms must terminate on the same
evaluative outcome with opposite signs, or (ii) dominance conditions must be
derived from a mechanism property that orders the two mechanisms' relative
strength. Hard constraint #10 in SKILL.md has the same omission. Legacy
satisfied both implicitly.

Classification: **(e) preservation architecture gap (G outcome-locking and
derived-dominance rules missing), with a (c) execution component.** Strongest
preservation signal in R5 (both judges, largest margin).

## R5Q12 (B, preservation, governed = X, loss; judge B preference only, 39 vs 39.5)

Chain: governed gave the temporal ordering of traces ("visibility benefits
should appear during initial work packages, whereas deskilling requires
accumulated substitution") and divergent traces, as the prompt requested.
Judge B preferred legacy because it "more carefully leaves the net effect
contingent on horizon and explains how tacit coordination is reproduced
through local problem solving."

Root cause assessment: `corpus/variants/B_mechanism_elaboration.md` contains
no rule about countervailing mechanisms with different time constants (no
mention of net effect, horizon contingency, or temporal ordering). Governed
complied with every explicit task requirement. The legacy advantage is one
explicit sentence: net effect as a function of the observation horizon.

Classification: **(c)/(d), weak evidence.** At most a one-line principle is
warranted (when opposing mechanisms have different time constants, state the
net effect as horizon-contingent, not merely ordered); no structural change.

## Summary classification

| Task | Stratum | Evidence strength | Classification | Priority |
|---|---|---|---|---|
| R5Q01 | targeted (critical) | strong; systematic defect also present unflagged in R5Q02 | (b) notation-level protocol defect + missing consistency gate | 1 |
| R5Q11 | preservation | strong (both judges, 4.5-point margin) | (e) G architecture gap: same-outcome locking + derived dominance | 2 |
| R5Q03 | targeted | moderate (one judge, two dimension penalties) | (b) D protocol gap: terminal-state closure | 3 |
| R5Q06 | targeted | weak (zero dimension penalties, one pairwise vote) | borderline (d)/(b-minor): open-agenda form | 4 (optional) |
| R5Q12 | preservation | weak (0.5-point margin, one judge) | (c)/(d) | 5 (optional) |

## Candidate minimal repairs (for approval before implementation)

1. **E boundary notation (R5Q01).** Replace `X -> boundary state -> ...` with
   a boundary-as-scope form in all three governed locations (SKILL.md step 4,
   governed-generation-guards.md, registry E contract): the boundary state is
   a prior scope node; no directed edge may run from X to the boundary state;
   branch form `X -> {S_high: interpretation_H -> mechanism_H -> Y_H;
   S_low: ...}` is the canonical graph. Add a graph–prose consistency line to
   the E guard and a phase-4 QC check. Update the locked test assertion at
   `tests/test_theory_governance.py:99`. The registry snapshot hash covers
   architectures/patterns only (`inventory_fingerprint(architectures,
   patterns)`), so guard-text edits do not invalidate it.
2. **G outcome-locking (R5Q11).** Add to the G variant key principles and QC:
   both mechanisms must terminate on the same evaluative outcome with
   opposite signs; dominance conditions must be derived from a mechanism
   property that orders relative strength, not listed as correlates. Mirror
   the same-outcome requirement in SKILL.md hard constraint #10.
3. **D terminal-state closure (R5Q03).** Add to the stage-boundary operator
   and the D generation contract: the stage chain must close at the terminal
   process state named in the task or contribution claim; if the immediate
   next stage is not terminal, chain further boundary crossings (each with
   its own marker); never relabel a marker or intermediate state as the
   terminal outcome.
4. **D open-agenda form (R5Q06, optional).** One QC line in the
   feedback-transport operator: when the task requires an open empirical
   agenda, state it as a question whose rival answers correspond to different
   branches or interpretations of the same trace.
5. **B horizon-contingent net effect (R5Q12, optional).** One line in the B
   variant: when countervailing mechanisms have different time constants,
   state the net effect as contingent on the observation horizon.

## Non-actions (explicitly rejected)

- No change to any R5 task, output, pair, label, score, judge file, or
  threshold; R5 stays a failed acceptance.
- No promotion of benchmark outputs or legacy text into the corpus as
  exemplars; all repairs are rule-level.
- No new template sentences for open agendas or reconciliations.
- No per-task tuning against R5 items; validation requires fresh tasks (R6
  pre-registration) after repairs land and regression tests pass.
