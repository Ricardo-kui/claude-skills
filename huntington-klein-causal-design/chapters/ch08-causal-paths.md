# Chapter 8: Causal Paths and Closing Back Doors

## Core Idea

Enumerate every treatment–outcome path. Preserve paths that define the target causal effect and block noncausal back-door paths without conditioning on mediators or opening colliders.

## Path Vocabulary

- **Causal/front-door path**: arrows flow from treatment toward outcome.
- **Back-door path**: the path enters treatment through an incoming arrow and can generate noncausal association.
- **Open path**: transmits association under the conditioning set.
- **Closed path**: blocked by conditioning on a noncollider or by an unconditioned collider.
- **Collider**: two arrows meet head-to-head on the path; conditioning on it—or sometimes its descendant—can open the path.
- **Mediator**: lies on a causal path from treatment to outcome; conditioning on it changes a total-effect target.

The chapter uses “good” and “bad” paths relative to the research question. Translate those labels into the precise estimand: a mediation question may intentionally include or exclude paths differently.

## Adjustment Workflow

1. List every path from treatment to outcome.
2. Mark the paths that constitute the target effect.
3. Mark open back-door paths.
4. Find a pre-treatment adjustment set that blocks every open back door.
5. Check that the set contains no collider, collider descendant, or mediator for the target total effect.
6. Check support after conditioning; a logically valid set may be empirically unusable.
7. Compare alternative minimal sets and prefer the one with better measurement and overlap.
8. State which unmeasured paths remain assumptions.

## Diagram Testing

A DAG can imply conditional independencies among variables other than treatment and outcome. If two variables should be unrelated after conditioning under the graph but remain strongly related, the graph may omit a path or misstate an arrow. Passing such a test does not prove the graph; failing it can falsify part of the graph.

## Failure Modes

- **Control everything**: can open colliders and block causal mechanisms.
- **Post-treatment adjustment**: can change the estimand and introduce selection.
- **Path omission**: evaluating only the most obvious confounder.
- **Statistical control without overlap**: relying on extrapolation instead of comparable units.
- **DAG-proof claim**: treating a diagram as evidence rather than a formalized assumption set.

## Completion Check

An adjustment claim is complete only when every relevant back door is addressed and every included control has a path-specific role.

## Worked Example

> Source-grounded reconstruction from Huntington-Klein (2025); compressed and paraphrased.

For the effect of smoking on cancer, suppose the diagram contains Smoking → Cancer and Smoking ← Income → Cancer. The first path belongs to the total causal effect; the second is an open back door. Conditioning on a pre-treatment measure of income can close the back door if the measurement is adequate and no other confounding paths remain.

Now add Smoking → MedicalScreening ← FamilyHistory → Cancer. Medical screening is a collider on that path. Restricting the sample to screened patients or controlling for screening opens an association between smoking and family history, creating bias.

The exercise is not finished after naming one confounder. Enumerate all paths, define the target effect, test every proposed control's role on each path, and check empirical overlap after conditioning. If two sufficient adjustment sets exist, prefer the one with more reliable pre-treatment measurement and support.

## Connects To

- [Ch13](ch13-regression.md): implement regression adjustment.
- [Ch14](ch14-matching.md): construct comparable covariate distributions.
- [Ch11](ch11-causality-with-less-modeling.md): test implications and relax uncertain assumptions.
