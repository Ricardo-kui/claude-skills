# R5-repair forward validation (2026-08-07)

## Protocol

Five fresh tasks (FWD01–FWD05), one per accepted repair, on settings that do
not appear in R2–R5. The generator (this session) had access to the repaired
skill rules but not to any R5 judge file, score, label map, or R5 task
content while drafting. Retrieval events were recorded in
`R5_REPAIR_FORWARD_MANIFEST.json` (5 chained `list-references` events,
`verify-manifest` valid, head `167c1822…25274`); no candidate was rendered
because none matched the fresh reasoning needs closely enough, which the
governed route permits. Each output follows the R5 output contract: compact
argument graph plus a 120–180 word rationale, in the task's requested mode.

## FWD01 (E / no_numbered_hypotheses) — targets repair 1 (boundary-as-scope graph)

Prompt: Explain how landlord adoption of algorithmic rent-setting affects
tenant organizing under high versus low municipal vacancy rates. Derive an
affirmative actor-level mechanism for each vacancy state, place the boundary
state before its interpretation and mechanism, specify level and timing, and
use no numbered hypothesis.

Argument graph: `{low vacancy (prior scope): algorithmic rent-setting → tenants read coordinated extraction from a captive market → loss-protection mobilization → tenant organizing rises; high vacancy (prior scope): algorithmic rent-setting → tenants read posted prices as one negotiable offer among vacant alternatives → exit-substitutes-voice → tenant organizing falls}`, at the municipal tenant-coalition level during the first lease-renewal cycle after adoption.

Rationale: The vacancy state exists before tenants interpret the pricing tool.
Under low vacancy, renters face a captive market: moving is costly and
alternatives are scarce. When adjacent landlords adopt the same algorithmic
tool, tenants read synchronized price increases as coordinated extraction
rather than independent decisions. That interpretation activates
loss-protection mobilization: tenants pool rent data, recruit legal aid, and
coordinate complaints, so organizing intensifies. Under high vacancy, visible
empty units make exit credible. Tenants interpret the algorithm's posted rent
as one negotiable offer among many, demand concessions individually, and exit
rather than organize, so collective action declines. The focal level is the
municipal tenant coalition, and the temporal window is the first
lease-renewal cycle after adoption. Diagnostic traces are coordinated rent
strikes and joint filings under low vacancy versus individual concession
agreements and elevated voluntary turnover under high vacancy.

Repair-1 check: boundary states appear only as prior scope labels on each
branch; no directed edge runs from X to a vacancy state; graph order matches
prose order ("vacancy state exists before tenants interpret"). PASS.

## FWD02 (D / propositions) — targets repair 3 (terminal-state closure)

Prompt: Develop a process account of an open-source project moving from
informal maintainer governance to foundation stewardship. Name the actors and
transition condition, identify an observable readiness marker that exists
before stewardship begins, include a failed-transition branch, and end with
one well-formed proposition.

Argument graph: `core maintainers govern informally and negotiate with sponsoring firms → jointly met threshold of duplicated-decision disputes plus sustainable multi-firm funding → published governance charter with named review rotation and signatory coverage appears before incorporation → interim steering board incorporates the foundation and transfers trademark, release, and election authority → routinized foundation stewardship (elected board operates budgets and release policy); if the charter stalls, maintainers fork the project, sponsors withdraw funding, or informal governance persists`.

Rationale: The current-stage actors are the volunteer core maintainers, whose
informal decision norms come under strain as corporate contributors multiply.
Transition becomes possible when two conditions are jointly met: disputes over
duplicated decision rights recur, and at least two firms commit durable
funding. The pre-stewardship marker is a published governance charter whose
review rotation is named and whose signatories span the major contributing
organizations; it precedes stewardship because it records transferable
agreement while no stewarding body yet exists. The next actor is an interim
steering board, which incorporates the foundation and transfers trademark,
release, and election authority. The terminal state is routinized foundation
stewardship: an elected board operating budgets and release policy. If the
charter stalls, dissatisfied maintainers fork, sponsors withdraw, or informal
governance persists. Proposition 1: Informal maintainer governance transitions
to foundation stewardship when maintainers and sponsors produce a broadly
signed governance charter that enables incorporation and authority transfer;
a stalled charter redirects the project toward forking or continued
informality.

Repair-3 check: the chain does not stop at the immediate next state
(incorporation); it closes at the prompt-named terminal state (routinized
stewardship), with the marker preceding, and distinct from, incorporation.
PASS.

## FWD03 (D / no_numbered_hypotheses) — targets repair 4 (discriminating open agenda)

Prompt: Build a feedback-transport account for airline line-operations safety
reporting: source, channel, translation, decision-capable recipient,
interpretation criterion, and distinct traces of reinforcement, redirection,
and termination. Preserve an open empirical agenda; use no numbered claims.

Argument graph: `line pilots' irregularity reports → confidential safety-report channel plus line-operations review meetings → safety office translates narratives into procedure-comparable categories → fleet standards board → recurrence-and-procedure-dependence criterion → reinforce / redirect / terminate → unchanged SOP with reiterated guidance / revised procedure and retraining / retired procedure or decommissioned maneuver`.

Rationale: Feedback originates with line pilots who encounter procedure
mismatches during irregular operations. It travels through confidential safety
reports and line-operations review meetings, not directly from anecdote to
rule. The safety office translates narratives into comparable categories —
procedure step, aircraft state, workload, and outcome — preserving what
happened and when so that one crew's complaint is not treated as a fleet
pattern. The fleet standards board is decision-capable because it can rewrite
operating procedures and training. It asks whether a reported problem recurs
and whether it depends on the procedure as written. Procedure-consistent
evidence reinforces, visible in unchanged procedures with reiterated guidance.
Correctable procedure dependence redirects, visible in revised steps and
retraining. Recurrent problems judged unfixable by revision terminate the
procedure. Open agenda: does reporting change outcomes because crews' voice
alters procedure content, or because the board simply selects out
accident-prone procedures while leaving crew influence unchanged?

Repair-4 check: the open agenda is a question whose rival answers
(voice-driven content change versus selection-driven attrition) map to
different interpretations of the same traces, not a generic call for more
research. PASS.

## FWD04 (G / propositions) — targets repair 2 (same-outcome locking + derived dominance)

Prompt: Develop symmetric benefit and burden mechanisms through which
carbon-border-adjustment exposure shapes export manufacturers' credit terms,
then provide a theory-based reconciliation specifying when each mechanism
dominates, and state one proposition.

Argument graph: `CBAM exposure → abatement options and verification capacity make adjustment costs legible and reducible → lender risk assessment improves → credit terms ease; CBAM exposure → disclosure reveals irreducible compliance liabilities → lender risk assessment worsens → credit terms tighten; reducible exposure plus mature verification favors benefit, structurally irreducible exposure favors burden`.

Rationale: The benefit mechanism runs from exposure to credit terms through
risk legibility: where abatement options and credible verification exist,
carbon accounting converts an opaque regulatory threat into priced,
monitorable action, and lenders ease terms because residual risk falls. The
burden mechanism runs to the same outcome with the opposite sign: where
emissions are structurally irreducible, the same disclosure reveals
liabilities that cannot be contracted away, and lenders tighten terms as
expected compliance costs rise. Both mechanisms terminate on credit terms;
neither is a side effect on a different outcome. Dominance follows from a
mechanism property — reducibility of the exposed emissions — not from a list
of correlates: legibility only helps when the revealed costs can be acted
upon, and it hurts when it merely certifies an unavoidable liability.
Proposition 1: Carbon-border-adjustment exposure improves export
manufacturers' credit terms when exposed emissions are reducible under mature
verification infrastructure, but worsens credit terms when exposed emissions
are structurally irreducible.

Repair-2 check: both mechanisms lock onto the same evaluative outcome (credit
terms) with opposite signs; dominance is derived from a mechanism property
(reducibility) that orders the two mechanisms' strength. PASS.

## FWD05 (B / no_numbered_hypotheses) — targets repair 5 (horizon-contingent net effect)

Prompt: Explain how surgical safety-checklist adoption changes operating-team
adaptive performance through countervailing error-trapping and
attentional-complacency mechanisms. Specify warrants, temporal ordering, and
divergent observable traces, without numbered hypotheses.

Argument graph: `checklist adoption → early shared explicit cues → fewer coordination errors and freed attention → adaptive performance rises; repeated routinized use → completion substitutes for situation assessment → narrowed scanning → adaptive performance falls on novel complications; net effect contingent on observation horizon`.

Rationale: In the early adoption window, a checklist gives surgeons,
anesthetists, and nurses shared explicit cues at fixed pauses. The warrant is
interdependence under time pressure: common checkpoints catch coordination
errors and free attention for anomalies, so adaptive performance rises. Early
traces include caught instrument counts, voiced concerns at pauses, and faster
recovery from routine disruptions. With routinized use, a countervailing
mechanism accumulates: completing the checklist can substitute for active
situation assessment, narrowing the team's scanning to listed items. The
warrant is that adaptive performance is reproduced through active diagnosis of
unscripted cues, not through compliance. Later traces include perfunctory
call-outs, missed unlisted complications, and slower response to novel events.
The net effect is therefore contingent on the observation horizon: positive
during early adoption, attenuating or reversing as routinization accumulates;
a single-horizon estimate would misstate the relationship in either direction.

Repair-5 check: the net effect is stated explicitly as a function of the
observation horizon, not merely temporally ordered traces. PASS.

## Summary

| Task | Repair exercised | Result |
|---|---|---|
| FWD01 | 1: E boundary-as-scope graph, no X→boundary edge, graph–prose order match | PASS |
| FWD02 | 3: D stage chain closes at prompt-named terminal state | PASS |
| FWD03 | 4: D open agenda as discriminating question over the same trace | PASS |
| FWD04 | 2: G same-outcome locking, dominance derived from mechanism property | PASS |
| FWD05 | 5: B net effect stated as horizon-contingent | PASS |

Regression evidence: `tests/test_theory_governance.py` 22/22 pass after the
repairs; `catalog audit` clean (7 architectures, 120 reference assets, status
distribution unchanged); forward manifest valid with 5 chained events.

Scientific boundary: these forward tests show the repaired rules are usable as
written on fresh tasks and no longer force the R5 failure shapes. They are
single-generator demonstrations, not independent evidence of superiority; the
next formal acceptance remains a pre-registered R6 blind evaluation on novel
tasks, with thresholds frozen before generation.
