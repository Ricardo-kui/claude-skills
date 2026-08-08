#!/usr/bin/env python3
"""
Methods / Results Quality Check Script
Consumes JSON output from distill-methods-exemplar or distill-results-exemplar,
performs automated QC checks, and emits a structured PASS/FLAG/REJECT report.

Usage:
    python methods_results_quality_check.py --input paper_distilled.json --type methods
    python methods_results_quality_check.py --input paper_distilled.json --type results
    python methods_results_quality_check.py --input paper_distilled.json --type results --output report.json
    python methods_results_quality_check.py --corpus-check write-methods/econometric-models
    python methods_results_quality_check.py --corpus-check write-results/econometric-models

Exit codes:
    0 = PASS
    1 = FLAG
    2 = REJECT
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional


class Severity(Enum):
    PASS = "PASS"
    FLAG = "FLAG"
    REJECT = "REJECT"


@dataclass
class CheckItem:
    check_id: str
    category: str
    description: str
    severity: Severity
    detail: str = ""
    fix_priority: int = 0  # 1 = highest
    auto_fixable: bool = False


@dataclass
class QualityReport:
    paper_id: str
    check_type: str  # "methods" or "results"
    overall_status: Severity = Severity.PASS
    items: List[CheckItem] = field(default_factory=list)
    summary: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "paper_id": self.paper_id,
            "check_type": self.check_type,
            "overall_status": self.overall_status.value,
            "items": [
                {
                    "check_id": i.check_id,
                    "category": i.category,
                    "description": i.description,
                    "severity": i.severity.value,
                    "detail": i.detail,
                    "fix_priority": i.fix_priority,
                    "auto_fixable": i.auto_fixable,
                }
                for i in self.items
            ],
            "summary": self.summary,
        }


class BaseChecker:
    """Shared checks for both methods and results."""

    CAUSAL_WORDS_WEAK = {"associated with", "related to", "linked to", "correlated with"}
    CAUSAL_WORDS_MEDIUM = {"effect of", "impact of", "influence of", "effect on"}
    CAUSAL_WORDS_STRONG = {"causes", "caused", "leads to", "led to"}
    CAUSAL_WORDS_DIRECTIONAL = {"increases", "decreases", "reduces", "raises", "lowers"}

    def __init__(self, data: Dict[str, Any]):
        self.data = data
        self.report = QualityReport(
            paper_id=data.get("paper_id", "unknown"),
            check_type=self.check_type(),
        )

    def check_type(self) -> str:
        raise NotImplementedError

    def _add(self, item: CheckItem) -> None:
        self.report.items.append(item)
        if item.severity == Severity.REJECT:
            self.report.overall_status = Severity.REJECT
        elif item.severity == Severity.FLAG and self.report.overall_status != Severity.REJECT:
            self.report.overall_status = Severity.FLAG

    def check_schema_compliance(self) -> None:
        required_top = [
            "paper_id",
            "phase_0",
            "phase_1_slot_map",
            "phase_1_5_quality_gate",
            "phase_2_distillation",
            "phase_3",
            "phase_5_qc",
        ]
        missing = [k for k in required_top if k not in self.data]
        if missing:
            self._add(
                CheckItem(
                    check_id="SCHEMA_001",
                    category="schema",
                    description="Top-level schema keys missing",
                    severity=Severity.REJECT,
                    detail=f"Missing keys: {missing}",
                    fix_priority=1,
                )
            )
        else:
            self._add(
                CheckItem(
                    check_id="SCHEMA_000",
                    category="schema",
                    description="JSON schema compliance",
                    severity=Severity.PASS,
                    detail="All required top-level keys present",
                    fix_priority=0,
                )
            )

    def check_slot_coverage(self) -> None:
        gate = self.data.get("phase_1_5_quality_gate", {})
        coverage = gate.get("slot_coverage", {})
        if isinstance(coverage, str):
            rate_str = coverage.replace("%", "")
            missing = []
        elif isinstance(coverage, dict):
            rate_str = coverage.get("coverage_rate", "0%").replace("%", "")
            missing = coverage.get("missing_slots", [])
        else:
            rate_str = "0"
            missing = []
        try:
            rate = float(rate_str)
        except ValueError:
            rate = 0.0

        detail = f"Coverage: {rate}%; Missing: {missing}"

        if rate >= 85:
            sev = Severity.PASS
        elif rate >= 60:
            sev = Severity.FLAG
        else:
            sev = Severity.REJECT

        self._add(
            CheckItem(
                check_id="SLOT_001",
                category="coverage",
                description="Slot coverage rate",
                severity=sev,
                detail=detail,
                fix_priority=1 if sev == Severity.REJECT else (2 if sev == Severity.FLAG else 0),
            )
        )

    def check_no_verbatim_copy(self) -> None:
        qc = self.data.get("phase_5_qc", {})
        ok = qc.get("no_verbatim_copy", False)
        self._add(
            CheckItem(
                check_id="VERB_001",
                category="integrity",
                description="No verbatim copy from source text",
                severity=Severity.PASS if ok else Severity.REJECT,
                detail="No continuous 8+ word phrases from original" if ok else "Potential verbatim copy detected",
                fix_priority=1,
            )
        )

    def check_fact_boundary(self) -> None:
        qc = self.data.get("phase_5_qc", {})
        ok = qc.get("fact_boundary", False)
        self._add(
            CheckItem(
                check_id="FACT_001",
                category="integrity",
                description="Non-transferable facts properly bounded",
                severity=Severity.PASS if ok else Severity.FLAG,
                detail="All paper-specific facts marked as non-transferable" if ok else "Some paper-specific facts may have been generalized",
                fix_priority=2,
            )
        )

    def check_causal_language(self, design_type: str, allowed_words: set, forbidden_words: set) -> None:
        """Audit causal language in distilled skeletons against design strength."""
        phase2 = self.data.get("phase_2_distillation", {})
        # Collect all skeleton strings (handle both nested and flat structures)
        skeletons: List[str] = []
        # Flat structure: expression_skeletons at phase_2 top level
        top_skeletons = phase2.get("expression_skeletons", [])
        if isinstance(top_skeletons, list):
            for sk in top_skeletons:
                if isinstance(sk, dict):
                    skeletons.append(sk.get("skeleton", ""))
        # Nested structure: expression_skeletons inside each slot
        for slot_data in phase2.values():
            if isinstance(slot_data, dict):
                for sk in slot_data.get("expression_skeletons", []):
                    if isinstance(sk, dict):
                        skeletons.append(sk.get("skeleton", ""))

        found_forbidden = []
        found_allowed = []
        text = " ".join(skeletons).lower()

        for word in forbidden_words:
            if word.lower() in text:
                found_forbidden.append(word)
        for word in allowed_words:
            if word.lower() in text:
                found_allowed.append(word)

        if found_forbidden:
            sev = Severity.REJECT
            detail = f"Forbidden causal words for {design_type}: {found_forbidden}"
        elif not found_allowed and allowed_words and self.check_type() != "methods":
            sev = Severity.FLAG
            detail = f"No expected causal words found for {design_type}; may be underclaiming"
        else:
            sev = Severity.PASS
            detail = f"Causal language appropriate for {design_type}"

        self._add(
            CheckItem(
                check_id="CAUSAL_001",
                category="language",
                description="Causal language matches design strength",
                severity=sev,
                detail=detail,
                fix_priority=1 if sev == Severity.REJECT else 2,
            )
        )

    def run(self) -> QualityReport:
        raise NotImplementedError


class MethodsChecker(BaseChecker):
    def check_type(self) -> str:
        return "methods"

    def run(self) -> QualityReport:
        self.check_schema_compliance()
        self.check_slot_coverage()
        self.check_no_verbatim_copy()
        self.check_fact_boundary()

        # Design-type specific causal language audit
        p0 = self.data.get("phase_0", {})
        design = p0.get("identification_strategy", "").lower()

        if "ols" in design or "fe" in design:
            self.check_causal_language(
                "OLS/FE",
                allowed_words=self.CAUSAL_WORDS_WEAK,
                forbidden_words=self.CAUSAL_WORDS_MEDIUM | self.CAUSAL_WORDS_STRONG | self.CAUSAL_WORDS_DIRECTIONAL,
            )
        elif "did" in design or "difference" in design:
            self.check_causal_language(
                "DiD",
                allowed_words=self.CAUSAL_WORDS_WEAK | self.CAUSAL_WORDS_MEDIUM | self.CAUSAL_WORDS_DIRECTIONAL,
                forbidden_words=self.CAUSAL_WORDS_STRONG,
            )
        elif "iv" in design or "2sls" in design:
            # IV with nonlinear estimators (Tobit, Poisson, survival) should stay cautious
            estimator = p0.get("estimator_family", "").lower()
            if any(e in estimator for e in ["tobit", "poisson", "weibull", "aft", "logit", "probit"]):
                self.check_causal_language(
                    "IV + Nonlinear",
                    allowed_words=self.CAUSAL_WORDS_WEAK | self.CAUSAL_WORDS_DIRECTIONAL,
                    forbidden_words=self.CAUSAL_WORDS_STRONG,
                )
            else:
                self.check_causal_language(
                    "IV/2SLS",
                    allowed_words=self.CAUSAL_WORDS_WEAK | self.CAUSAL_WORDS_MEDIUM | self.CAUSAL_WORDS_DIRECTIONAL,
                    forbidden_words=self.CAUSAL_WORDS_STRONG,
                )
        elif "experiment" in design:
            self.check_causal_language(
                "Experiment",
                allowed_words=self.CAUSAL_WORDS_WEAK | self.CAUSAL_WORDS_MEDIUM | self.CAUSAL_WORDS_STRONG,
                forbidden_words=set(),
            )
        else:
            self.check_causal_language("Unknown", allowed_words=set(), forbidden_words=set())

        # DNA metrics
        dna = self.data.get("phase_3", {})

        # Because density (calibrated: Eilert=30%, Zhou=25%, Rising=0%; MVP30 median ~35%)
        because = dna.get("because_density", 0.0)
        if because >= 0.4:
            sev, detail = Severity.PASS, f"Because density: {because:.0%}"
        elif because >= 0.2:
            sev, detail = Severity.FLAG, f"Because density below ideal: {because:.0%} (target: >=40%; MVP30 median ~35%)"
        else:
            sev, detail = Severity.FLAG, f"Because density low: {because:.0%} (MVP30 median ~35%); consider adding competitive explanations for key controls"
        self._add(
            CheckItem(
                check_id="DNA_001",
                category="dna",
                description="Control variable 'because' density",
                severity=sev,
                detail=detail,
                fix_priority=2,
            )
        )

        # Sample funnel
        funnel = dna.get("sample_funnel_completeness", False)
        self._add(
            CheckItem(
                check_id="DNA_002",
                category="dna",
                description="Sample funnel audit chain complete",
                severity=Severity.PASS if funnel else Severity.REJECT,
                detail="Start → exclusions (with counts) → final N" if funnel else "Missing numbers or exclusion reasons in funnel",
                fix_priority=1,
            )
        )

        # Diagnostic foreshadowing (calibrated: OLS/FE often omits; IV/DiD require it)
        fore = dna.get("diagnostic_foreshadowing_rate", 0.0)
        p0 = self.data.get("phase_0", {})
        design = p0.get("identification_strategy", "").lower()
        # Lower bar for simple OLS/FE; higher bar for causal designs
        if "ols" in design and "iv" not in design and "did" not in design:
            target = 0.3
        else:
            target = 0.8
        if fore >= target:
            sev, detail = Severity.PASS, f"Diagnostic foreshadowing: {fore:.0%} (target: ≥{target:.0%})"
        elif fore >= target * 0.5:
            sev, detail = Severity.FLAG, f"Diagnostic foreshadowing: {fore:.0%} (target: ≥{target:.0%})"
        elif target <= 0.3:
            # For simple OLS/FE, lack of diagnostic foreshadowing is common in top journals
            sev, detail = Severity.FLAG, f"Diagnostic foreshadowing: {fore:.0%} (target: ≥{target:.0%}; OLS/FE often omits)"
        else:
            sev, detail = Severity.REJECT, f"Diagnostic foreshadowing: {fore:.0%} (target: ≥{target:.0%})"
        self._add(
            CheckItem(
                check_id="DNA_003",
                category="dna",
                description="Diagnostic tests foreshadowed in Methods (not only in Results)",
                severity=sev,
                detail=detail,
                fix_priority=2,
            )
        )

        # Hypothesis alignment (calibrated: Eilert=80%, Zhou=85%, Rising=75%; MVP30 median ~80%)
        align = dna.get("hypothesis_alignment_density", 0.0)
        if align >= 0.85:
            sev, detail = Severity.PASS, f"Hypothesis alignment: {align:.0%}"
        elif align >= 0.7:
            sev, detail = Severity.FLAG, f"Hypothesis alignment: {align:.0%} (target: >=85%; MVP30 median ~80%)"
        else:
            sev, detail = Severity.FLAG, f"Hypothesis alignment below ideal: {align:.0%} (target: >=85%; MVP30 median ~80%)"
        self._add(
            CheckItem(
                check_id="DNA_004",
                category="dna",
                description="Predictor paragraphs link to Hypothesis numbers",
                severity=sev,
                detail=detail,
                fix_priority=2,
            )
        )

        # Temporal clarity (calibrated: Eilert=90%, Zhou=85%, Rising=80%; MVP30 median ~85%)
        temporal = dna.get("temporal_clarity_density", 0.0)
        if temporal >= 0.85:
            sev, detail = Severity.PASS, f"Temporal clarity: {temporal:.0%}"
        elif temporal >= 0.7:
            sev, detail = Severity.FLAG, f"Temporal clarity: {temporal:.0%} (target: >=85%; MVP30 median ~85%)"
        else:
            sev, detail = Severity.FLAG, f"Temporal clarity below ideal: {temporal:.0%} (target: >=85%; MVP30 median ~85%)"
        self._add(
            CheckItem(
                check_id="DNA_005",
                category="dna",
                description="Temporal ordering explicit (lags, event windows, observation periods)",
                severity=sev,
                detail=detail,
                fix_priority=3,
            )
        )

        # Summarize
        counts = {s.value: 0 for s in Severity}
        for item in self.report.items:
            counts[item.severity.value] += 1
        self.report.summary = {
            "total_checks": len(self.report.items),
            "pass_count": counts["PASS"],
            "flag_count": counts["FLAG"],
            "reject_count": counts["REJECT"],
            "design_type": p0.get("identification_strategy", "unknown"),
        }
        return self.report


class ResultsChecker(BaseChecker):
    def check_type(self) -> str:
        return "results"

    def check_slot_coverage(self) -> None:
        """Dynamic slot coverage: required slots depend on paper features."""
        gate = self.data.get("phase_1_5_quality_gate", {})
        coverage = gate.get("slot_coverage", {})
        present_slots = set(coverage.get("present_slots", []))
        missing_slots = set(coverage.get("missing_slots", []))
        p0 = self.data.get("phase_0", {})
        slot_map = self.data.get("phase_1_slot_map", {})

        # Core required slots for all Results sections
        required = {"R1", "R2", "R3", "R7"}

        # R4: required only if paper has interaction effects
        hypothesis_struct = p0.get("hypothesis_structure", "").lower()
        has_interaction = "interaction" in hypothesis_struct or "交互" in hypothesis_struct
        r4 = slot_map.get("R4", {})
        if has_interaction or r4.get("located", False):
            required.add("R4")

        # R5: required only if paper has nonlinear/U-shaped effects
        has_nonlinear = any(
            k in hypothesis_struct
            for k in ["u-shaped", "nonlinear", "quadratic", "cubic", "inverted u", "倒u型"]
        )
        r5 = slot_map.get("R5", {})
        if has_nonlinear or r5.get("located", False):
            required.add("R5")

        # R6: required only if paper has nonsignificant findings to report
        num_nonsig = p0.get("number_of_nonsignificant_findings", 0)
        r6 = slot_map.get("R6", {})
        if num_nonsig > 0 or r6.get("located", False):
            required.add("R6")

        # R8: required only if paper has exploratory/post-hoc analyses
        r8 = slot_map.get("R8", {})
        if r8.get("located", False):
            required.add("R8")

        # R9: transition paragraph is always optional
        # (many top-tier empirical papers omit it without penalty)

        present_required = present_slots & required
        rate = (len(present_required) / len(required) * 100) if required else 100.0
        missing_required = sorted(required - present_slots)

        detail = (
            f"Adjusted coverage: {rate:.0f}% (required slots: {sorted(required)}); "
            f"Present: {sorted(present_slots)}; Missing required: {missing_required}"
        )

        if rate >= 85:
            sev = Severity.PASS
        elif rate >= 60:
            sev = Severity.FLAG
        else:
            sev = Severity.REJECT

        self._add(
            CheckItem(
                check_id="SLOT_001",
                category="coverage",
                description="Slot coverage rate (adjusted for paper features)",
                severity=sev,
                detail=detail,
                fix_priority=1 if sev == Severity.REJECT else (2 if sev == Severity.FLAG else 0),
            )
        )

    def run(self) -> QualityReport:
        self.check_schema_compliance()
        self.check_slot_coverage()
        self.check_no_verbatim_copy()
        self.check_fact_boundary()

        # Estimator-specific causal language audit
        p0 = self.data.get("phase_0", {})
        estimator = p0.get("estimator_family", "").lower()

        if "aft" in estimator or "survival" in estimator or "weibull" in estimator or "cox" in estimator:
            self.check_causal_language(
                "Survival/AFT",
                allowed_words=self.CAUSAL_WORDS_WEAK | self.CAUSAL_WORDS_DIRECTIONAL | {"prolongs", "accelerates", "positive", "negative", "positive/negative"},
                forbidden_words=self.CAUSAL_WORDS_STRONG,
            )
        elif "ols" in estimator or "fe" in estimator:
            self.check_causal_language(
                "OLS/FE",
                allowed_words=self.CAUSAL_WORDS_WEAK | {"effect of"},
                forbidden_words=self.CAUSAL_WORDS_STRONG | self.CAUSAL_WORDS_DIRECTIONAL | {"leads to", "led to"},
            )
        elif "did" in estimator or "difference" in estimator:
            self.check_causal_language(
                "DiD",
                allowed_words=self.CAUSAL_WORDS_WEAK | self.CAUSAL_WORDS_MEDIUM | self.CAUSAL_WORDS_DIRECTIONAL,
                forbidden_words=self.CAUSAL_WORDS_STRONG,
            )
        elif "iv" in estimator or "2sls" in estimator:
            if any(e in estimator for e in ["tobit", "poisson", "weibull", "aft", "logit", "probit"]):
                self.check_causal_language(
                    "IV + Nonlinear",
                    allowed_words=self.CAUSAL_WORDS_WEAK | self.CAUSAL_WORDS_DIRECTIONAL,
                    forbidden_words=self.CAUSAL_WORDS_STRONG,
                )
            else:
                self.check_causal_language(
                    "IV/2SLS",
                    allowed_words=self.CAUSAL_WORDS_WEAK | self.CAUSAL_WORDS_MEDIUM | self.CAUSAL_WORDS_DIRECTIONAL,
                    forbidden_words=self.CAUSAL_WORDS_STRONG,
                )
        elif "logit" in estimator or "probit" in estimator:
            self.check_causal_language(
                "Logit/Probit",
                allowed_words=self.CAUSAL_WORDS_WEAK,
                forbidden_words=self.CAUSAL_WORDS_STRONG | self.CAUSAL_WORDS_DIRECTIONAL,
            )
        elif "experiment" in estimator or "anova" in estimator:
            self.check_causal_language(
                "Experiment",
                allowed_words=self.CAUSAL_WORDS_WEAK | self.CAUSAL_WORDS_MEDIUM | self.CAUSAL_WORDS_STRONG | self.CAUSAL_WORDS_DIRECTIONAL,
                forbidden_words=set(),
            )
        else:
            self.check_causal_language("Unknown", allowed_words=set(), forbidden_words=set())

        # DNA metrics
        dna = self.data.get("phase_3", {})

        # Four-beat completeness (calibrated: nonsignificant hypotheses naturally reduce beat count)
        beat = dna.get("four_beat_completeness_rate", 0.0)
        p0 = self.data.get("phase_0", {})
        nonsig_ratio = p0.get("number_of_nonsignificant_findings", 0) / max(p0.get("number_of_hypotheses_tested", 1), 1)
        # Adjust target downward by half the nonsig ratio (e.g., 3/6 nonsig -> target drops from 100% to 75%)
        adjusted_target = max(0.7, 1.0 - (nonsig_ratio * 0.5))
        if beat >= adjusted_target + 0.1:
            sev, detail = Severity.PASS, f"Four-beat completeness: {beat:.0%} (adjusted target: {adjusted_target:.0%} due to {nonsig_ratio:.0%} nonsig)"
        elif beat >= adjusted_target - 0.1:
            sev, detail = Severity.FLAG, f"Four-beat completeness: {beat:.0%} (adjusted target: {adjusted_target:.0%})"
        else:
            sev, detail = Severity.REJECT, f"Four-beat completeness: {beat:.0%} (adjusted target: {adjusted_target:.0%})"
        self._add(
            CheckItem(
                check_id="DNA_101",
                category="dna",
                description="R3 four-beat rhythm completeness (direction → significance → magnitude → support)",
                severity=sev,
                detail=detail,
                fix_priority=1,
            )
        )

        # Robustness organization (both threat-based and test-type-based are valid)
        gate = self.data.get("phase_1_5_quality_gate", {})
        suff = gate.get("source_sufficiency", {})
        if isinstance(suff, str):
            suff = {}
        robust_threat = suff.get("robustness_organized_by_threat", False)
        # Check if explicitly marked as organized by test type
        org = ""
        r7 = self.data.get("phase_1_slot_map", {}).get("R7", {})
        if r7:
            org = r7.get("organization", "").lower()
        is_test_type = "test" in org or "type" in org
        if robust_threat or is_test_type:
            sev = Severity.PASS
            detail = "Robustness checks organized by threat or by test type"
        else:
            sev = Severity.FLAG
            detail = "Robustness organization unclear; verify whether checks open with threat positioning or test-type enumeration"
        self._add(
            CheckItem(
                check_id="DNA_102",
                category="dna",
                description="Robustness checks organized by threat or test type",
                severity=sev,
                detail=detail,
                fix_priority=1,
            )
        )

        # Nonsignificant reporting
        nonsig = suff.get("nonsignificant_not_skipped", False)
        self._add(
            CheckItem(
                check_id="DNA_103",
                category="dna",
                description="Non-significant hypotheses reported (not skipped)",
                severity=Severity.PASS if nonsig else Severity.REJECT,
                detail="All hypotheses including null/mixed findings are reported" if nonsig else "Some non-significant hypotheses may have been omitted",
                fix_priority=1,
            )
        )

        # Economic significance
        econ = suff.get("economic_significance_present", False)
        self._add(
            CheckItem(
                check_id="DNA_104",
                category="dna",
                description="Economic significance reported alongside statistical significance",
                severity=Severity.PASS if econ else Severity.FLAG,
                detail="Substantive magnitude (one-SD change / probability shift / baseline comparison) present" if econ else "Only statistical significance reported; substantive magnitude missing",
                fix_priority=2,
            )
        )

        # Table navigation density
        nav = dna.get("table_model_positioning_rate", 0.0)
        if nav >= 0.9:
            sev, detail = Severity.PASS, f"Table/model positioning: {nav:.0%}"
        else:
            sev, detail = Severity.FLAG, f"Table/model positioning: {nav:.0%} (target: 100%)"
        self._add(
            CheckItem(
                check_id="DNA_105",
                category="dna",
                description="Each main-effect paragraph opens with table/model location",
                severity=sev,
                detail=detail,
                fix_priority=3,
            )
        )

        # Hypothesis restatement position (calibrated: table-opening restatement is valid in table-heavy Results)
        restate = dna.get("hypothesis_restatement_position", "")
        valid_positions = {"paragraph opening", "table opening", "paragraph or table opening"}
        if restate.lower() in valid_positions:
            sev, detail = Severity.PASS, f"Hypothesis restatement at {restate}"
        else:
            sev, detail = Severity.FLAG, f"Hypothesis restatement position: {restate} (target: paragraph opening or table opening)"
        self._add(
            CheckItem(
                check_id="DNA_106",
                category="dna",
                description="Hypothesis restatement at start of test paragraph or table",
                severity=sev,
                detail=detail,
                fix_priority=2,
            )
        )

        # Interaction support check (if interactions present)
        if p0.get("hypothesis_structure", "").lower() in ["主效应+交互", "三向交互"]:
            intro = dna.get("interaction_figure_introduction", "")
            has_support = any(k in intro.lower() for k in ["figure", "plot", "simple slope", "ame", "marginal effect"])
            self._add(
                CheckItem(
                    check_id="DNA_107",
                    category="dna",
                    description="Interaction effect supported by figure or simple slopes",
                    severity=Severity.PASS if has_support else Severity.REJECT,
                    detail="Interaction interpretation includes figure reference or slope decomposition" if has_support else "Interaction significant but no figure or slope decomposition provided",
                    fix_priority=1,
                )
            )

        # Post-hoc labeled as exploratory
        r8 = self.data.get("phase_1_slot_map", {}).get("R8", {})
        if r8.get("located", False):
            exploratory = r8.get("exploratory_label_present", False)
            self._add(
                CheckItem(
                    check_id="DNA_108",
                    category="dna",
                    description="Post-hoc / supplemental analyses labeled as exploratory",
                    severity=Severity.PASS if exploratory else Severity.REJECT,
                    detail="R8 explicitly marked as exploratory/confirmatory" if exploratory else "Supplemental analyses present but not labeled as exploratory vs confirmatory",
                    fix_priority=2,
                )
            )

        # Summarize
        counts = {s.value: 0 for s in Severity}
        for item in self.report.items:
            counts[item.severity.value] += 1
        self.report.summary = {
            "total_checks": len(self.report.items),
            "pass_count": counts["PASS"],
            "flag_count": counts["FLAG"],
            "reject_count": counts["REJECT"],
            "estimator_family": p0.get("estimator_family", "unknown"),
        }
        return self.report


VALID_STATUS_RE = re.compile(r"^(?:通过（\d/\d 复现）|通过（双篇/专家审计）|通过（单篇）|待交叉|可选)$")


def check_corpus_quickref(corpus_dir: Path) -> QualityReport:
    """Corpus 模式：校验目录内每个文件顶部「变体速查表」与正文变体一致。

    检查项：
    - QR_001：有正文变体但缺「变体速查表」→ REJECT
    - QR_002：速查表行与正文 `### 变体 N:` 不一致（缺行/孤儿行/状态词表违规）→ REJECT
    - QR_000：一致 → PASS
    零变体文件（骨架-only）无需速查表。
    """
    report = QualityReport(paper_id=corpus_dir.name, check_type="corpus")
    md_files = sorted(
        p for p in corpus_dir.glob("*.md")
        if p.name != "INDEX.md" and "草案" not in p.name  # 排除待预览的转写/速查表草案
    )

    for f in md_files:
        text = f.read_text(encoding="utf-8")
        body_variants = re.findall(r"^### 变体 (\d+)[:：]", text, re.M)  # 兼容半角/全角冒号（语料两套惯例）

        m = re.search(r"^## 变体速查表\s*$", text, re.M)
        if m is None:
            if body_variants:
                report.items.append(CheckItem(
                    check_id="QR_001", category="quickref", severity=Severity.REJECT,
                    description=f"{f.name}: 有 {len(body_variants)} 个正文变体但缺「变体速查表」",
                    detail="推广未覆盖或速查表被删除；需补建（槽位分组 + 六列表）",
                    fix_priority=1))
            continue  # 无正文变体且无速查表 = 骨架-only 文件，PASS

        section_end = text.find("\n## ", m.end())
        section = text[m.end(): section_end if section_end != -1 else len(text)]
        table_rows = re.findall(
            r"^\| (\d+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|",
            section, re.M,
        )
        row_nums = [r[0] for r in table_rows]
        missing = sorted(set(body_variants) - set(row_nums), key=int)
        orphan = sorted(set(row_nums) - set(body_variants), key=int)
        bad_vocab = [r[0] for r in table_rows if not VALID_STATUS_RE.match(r[4].strip())]

        if missing or orphan or bad_vocab:
            report.items.append(CheckItem(
                check_id="QR_002", category="quickref", severity=Severity.REJECT,
                description=f"{f.name}: 速查表与正文变体不一致",
                detail=(f"正文有但表中缺: {missing or '—'}; 表中有但正文缺: {orphan or '—'}; "
                        f"状态词表违规行: {bad_vocab or '—'}"),
                fix_priority=1))
        else:
            report.items.append(CheckItem(
                check_id="QR_000", category="quickref", severity=Severity.PASS,
                description=f"{f.name}: 速查表一致（{len(row_nums)} 行）"))

    n_reject = sum(1 for i in report.items if i.severity == Severity.REJECT)
    n_pass = sum(1 for i in report.items if i.severity == Severity.PASS)
    report.overall_status = Severity.REJECT if n_reject else Severity.PASS
    report.summary = {
        "total_checks": len(report.items),
        "pass_count": n_pass,
        "flag_count": 0,
        "reject_count": n_reject,
        "corpus_mode": "quickref-consistency",
    }
    return report


def print_report(report: QualityReport, output_path: Optional[str] = None) -> None:
    print(f"\n{'='*60}")
    print(f"Quality Report: {report.paper_id}")
    print(f"Type: {report.check_type.upper()}")
    print(f"Overall Status: {report.overall_status.value}")
    print(f"{'='*60}")

    # Group by severity
    for sev in [Severity.REJECT, Severity.FLAG, Severity.PASS]:
        items = [i for i in report.items if i.severity == sev]
        if not items:
            continue
        print(f"\n[{sev.value}] ({len(items)} items)")
        for item in items:
            print(f"  {item.check_id} | {item.category}")
            print(f"    {item.description}")
            if item.detail:
                print(f"    Detail: {item.detail}")
            if item.fix_priority > 0:
                print(f"    Fix Priority: {item.fix_priority}")
            print()

    print("-" * 60)
    print("Summary:")
    for k, v in report.summary.items():
        print(f"  {k}: {v}")

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(report.to_dict(), f, ensure_ascii=False, indent=2)
        print(f"\nReport saved to: {output_path}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="QC check: (a) distilled Methods/Results JSON output; (b) corpus 变体速查表一致性"
    )
    parser.add_argument("--input", "-i", help="Path to JSON file from distill skill")
    parser.add_argument("--type", "-t", choices=["methods", "results"], help="Distillation type")
    parser.add_argument("--output", "-o", help="Optional path to write JSON report")
    parser.add_argument("--corpus-check", "-c", metavar="DIR",
                        help="Corpus mode: 校验目录内所有文件的变体速查表与正文一致性")
    args = parser.parse_args()

    if args.corpus_check:
        corpus_dir = Path(args.corpus_check)
        if not corpus_dir.is_dir():
            print(f"Error: Corpus directory not found: {corpus_dir}", file=sys.stderr)
            return 2
        report = check_corpus_quickref(corpus_dir)
        print_report(report, args.output)
        return 0 if report.overall_status == Severity.PASS else 2

    if not args.input or not args.type:
        parser.error("需要 --input + --type，或 --corpus-check")

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}", file=sys.stderr)
        return 2

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if args.type == "methods":
        checker = MethodsChecker(data)
    else:
        checker = ResultsChecker(data)

    report = checker.run()
    print_report(report, args.output)

    # Exit code mapping
    if report.overall_status == Severity.PASS:
        return 0
    elif report.overall_status == Severity.FLAG:
        return 1
    else:
        return 2


if __name__ == "__main__":
    sys.exit(main())
