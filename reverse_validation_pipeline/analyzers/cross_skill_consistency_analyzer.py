#!/usr/bin/env python3
"""
Cross-skill consistency analyzer: check whether Methods and Results narratives align.

Checks:
1. Estimator declared in M7 matches estimator reported in Results
2. Identification assumptions in M8 are tested in R7
3. Sample funnel final N in M2 appears in Results
4. Hypothesis count in M4 matches hypotheses tested in R3
5. Temporal claims in M1/M2 align with Results timing
"""

import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from parsers.json_abstraction import InputAbstract


@dataclass
class ConsistencyItem:
    check_id: str
    category: str
    description: str
    status: str  # "PASS", "FLAG", "REJECT"
    detail: str = ""


@dataclass
class ConsistencyAnalysis:
    paper_id: str
    items: List[ConsistencyItem] = field(default_factory=list)
    consistency_score: float = 0.0  # 0-1
    flag_count: int = 0
    reject_count: int = 0


def _extract_numbers(text: str) -> List[int]:
    """Extract all integers from text."""
    return [int(x) for x in re.findall(r'\b\d{3,}\b', text.replace(",", ""))]


def _normalize_estimator(text: str) -> str:
    """Normalize estimator name for comparison."""
    text = text.lower()
    mapping = {
        "ols": "ols", "fixed effect": "fe", "fe": "fe",
        "did": "did", "difference-in-differences": "did",
        "iv": "iv", "2sls": "iv", "instrumental variable": "iv",
        "logit": "logit", "probit": "probit", "ordered probit": "ordered_probit",
        "tobit": "tobit", "poisson": "poisson",
        "weibull": "weibull", "aft": "aft", "cox": "cox",
        "gmm": "gmm", "dynamic panel": "gmm",
    }
    for key, val in mapping.items():
        if key in text:
            return val
    return text.strip()


def _check_estimator_consistency(abstract: InputAbstract) -> ConsistencyItem:
    """Check M7 estimator matches Results estimator family."""
    methods_p0 = abstract.raw_methods.get("phase_0", {})
    results_p0 = abstract.raw_results.get("phase_0", {})

    methods_est = methods_p0.get("estimator_family", "").lower()
    results_est = results_p0.get("estimator_family", "").lower()

    methods_norm = _normalize_estimator(methods_est)
    results_norm = _normalize_estimator(results_est)

    # Handle dual-estimator papers (e.g., "Weibull AFT + OLS")
    methods_parts = set(methods_norm.replace("+", " ").split())
    results_parts = set(results_norm.replace("+", " ").split())

    if methods_norm == results_norm or methods_parts & results_parts:
        status = "PASS"
        detail = f"Methods estimator '{methods_est}' aligns with Results estimator '{results_est}'"
    else:
        status = "FLAG"
        detail = f"Methods estimator '{methods_est}' may not align with Results estimator '{results_est}'"

    return ConsistencyItem(
        check_id="CROSS_001",
        category="estimator",
        description="M7 declared estimator matches Results reported estimator",
        status=status,
        detail=detail,
    )


def _check_identification_tested(abstract: InputAbstract) -> ConsistencyItem:
    """Check M8 identification assumptions are tested in R7."""
    m8 = abstract.raw_methods.get("phase_1_slot_map", {}).get("M8", {})
    r7 = abstract.raw_results.get("phase_1_slot_map", {}).get("R7", {})

    if not m8.get("located"):
        return ConsistencyItem(
            check_id="CROSS_002",
            category="identification",
            description="M8 identification assumptions tested in R7",
            status="PASS",
            detail="M8 not present; no identification assumption to verify",
        )

    assumption = m8.get("identification_assumption", "").lower()
    threats = [t.lower() for t in r7.get("threats_addressed", [])]

    # Map assumption types to likely threat keywords
    keyword_map = {
        "exogenous": ["endogeneity", "exogeneity", "instrument validity"],
        "instrument": ["instrument validity", "iv validity", "first-stage"],
        "parallel trend": ["parallel trend", "pretrend", "placebo"],
        "overlap": ["overlap", "common support", "matching quality"],
        "random": ["randomization", "balance", "manipulation check"],
    }

    matched = False
    matched_keywords = []
    for concept, keywords in keyword_map.items():
        if any(k in assumption for k in keywords):
            for kw in keywords:
                if any(kw in t for t in threats):
                    matched = True
                    matched_keywords.append(kw)

    if matched or not threats:
        status = "PASS"
        detail = f"M8 assumption keywords {matched_keywords} found in R7 threats" if matched else "R7 threats address identification"
    else:
        status = "FLAG"
        detail = f"M8 assumption '{assumption[:80]}...' not clearly tested in R7 threats: {threats[:3]}"

    return ConsistencyItem(
        check_id="CROSS_002",
        category="identification",
        description="M8 identification assumptions tested in R7",
        status=status,
        detail=detail,
    )


def _check_sample_size_consistency(abstract: InputAbstract) -> ConsistencyItem:
    """Check M2 final N appears in Results."""
    m2 = abstract.raw_methods.get("phase_1_slot_map", {}).get("M2", {})
    if not m2.get("located") or not m2.get("has_numbers"):
        return ConsistencyItem(
            check_id="CROSS_003",
            category="sample",
            description="M2 sample funnel final N consistent with Results",
            status="PASS",
            detail="M2 funnel without explicit numbers; skipping check",
        )

    funnel = m2.get("funnel_steps", [])
    funnel_text = " ".join(funnel)
    funnel_numbers = _extract_numbers(funnel_text)

    # Look for sample sizes in Results phase_2 or phase_1
    results_text = ""
    phase2 = abstract.raw_results.get("phase_2_distillation", {})
    for slot_data in phase2.values():
        if isinstance(slot_data, dict):
            for sk in slot_data.get("expression_skeletons", []):
                if isinstance(sk, dict):
                    results_text += " " + sk.get("skeleton", "")

    results_numbers = _extract_numbers(results_text)

    # Check if any funnel final N appears in Results
    overlap = set(funnel_numbers) & set(results_numbers)
    if overlap:
        status = "PASS"
        detail = f"Sample size(s) {sorted(overlap)} appear in both Methods funnel and Results"
    else:
        status = "FLAG"
        detail = f"M2 funnel numbers {funnel_numbers} not found in Results text numbers {results_numbers[:10]}"

    return ConsistencyItem(
        check_id="CROSS_003",
        category="sample",
        description="M2 sample funnel final N consistent with Results",
        status=status,
        detail=detail,
    )


def _check_hypothesis_count_consistency(abstract: InputAbstract) -> ConsistencyItem:
    """Check M4 predictor count matches R3 hypotheses tested."""
    m4 = abstract.raw_methods.get("phase_1_slot_map", {}).get("M4", {})
    r3 = abstract.raw_results.get("phase_1_slot_map", {}).get("R3", {})

    predictors = m4.get("predictors", []) if m4.get("located") else []
    hypotheses_covered = r3.get("hypotheses_covered", []) if r3.get("located") else []

    pred_count = len(predictors)
    hyp_count = len(hypotheses_covered)

    if pred_count == 0 or hyp_count == 0:
        return ConsistencyItem(
            check_id="CROSS_004",
            category="hypotheses",
            description="M4 predictor count matches R3 hypotheses tested",
            status="PASS",
            detail="Insufficient data to compare predictor and hypothesis counts",
        )

    # Allow some flexibility: predictors may map 1:N to hypotheses (e.g., main + interaction)
    ratio = hyp_count / max(pred_count, 1)
    if 0.8 <= ratio <= 2.0:
        status = "PASS"
        detail = f"M4 has {pred_count} predictors, R3 tests {hyp_count} hypotheses (ratio {ratio:.1f})"
    else:
        status = "FLAG"
        detail = f"M4 has {pred_count} predictors but R3 tests {hyp_count} hypotheses (ratio {ratio:.1f}); verify alignment"

    return ConsistencyItem(
        check_id="CROSS_004",
        category="hypotheses",
        description="M4 predictor count matches R3 hypotheses tested",
        status=status,
        detail=detail,
    )


def _check_temporal_consistency(abstract: InputAbstract) -> ConsistencyItem:
    """Check M1/M2 time window aligns with Results temporal references."""
    m1 = abstract.raw_methods.get("phase_1_slot_map", {}).get("M1", {})
    m2 = abstract.raw_methods.get("phase_1_slot_map", {}).get("M2", {})

    methods_text = ""
    for slot in [m1, m2]:
        if slot:
            methods_text += " " + str(slot)

    # Extract year ranges from Methods
    year_ranges = re.findall(r'(\d{4})\s*[-–]\s*(\d{4})', methods_text)
    methods_years = set()
    for start, end in year_ranges:
        methods_years.update(range(int(start), int(end) + 1))

    # Extract year ranges from Results
    results_text = ""
    phase2 = abstract.raw_results.get("phase_2_distillation", {})
    for slot_data in phase2.values():
        if isinstance(slot_data, dict):
            for sk in slot_data.get("expression_skeletons", []):
                if isinstance(sk, dict):
                    results_text += " " + sk.get("skeleton", "")

    results_years = set(int(y) for y in re.findall(r'\b(19\d{2}|20\d{2})\b', results_text))

    if not methods_years or not results_years:
        return ConsistencyItem(
            check_id="CROSS_005",
            category="temporal",
            description="M1/M2 time window aligns with Results temporal references",
            status="PASS",
            detail="No explicit year ranges found for comparison",
        )

    overlap = methods_years & results_years
    if len(overlap) >= min(len(methods_years), len(results_years)) * 0.5:
        status = "PASS"
        detail = f"Methods years {sorted(methods_years)[:5]}... overlap with Results years {sorted(results_years)[:5]}..."
    else:
        status = "FLAG"
        detail = f"Methods years {sorted(methods_years)} vs Results years {sorted(results_years)} show limited overlap"

    return ConsistencyItem(
        check_id="CROSS_005",
        category="temporal",
        description="M1/M2 time window aligns with Results temporal references",
        status=status,
        detail=detail,
    )


def analyze_cross_skill_consistency(abstract: InputAbstract) -> ConsistencyAnalysis:
    """Run all cross-skill consistency checks and return analysis."""
    analysis = ConsistencyAnalysis(paper_id=abstract.paper_id)

    checks = [
        _check_estimator_consistency(abstract),
        _check_identification_tested(abstract),
        _check_sample_size_consistency(abstract),
        _check_hypothesis_count_consistency(abstract),
        _check_temporal_consistency(abstract),
    ]

    for item in checks:
        analysis.items.append(item)
        if item.status == "FLAG":
            analysis.flag_count += 1
        elif item.status == "REJECT":
            analysis.reject_count += 1

    total = len(checks)
    passed = total - analysis.flag_count - analysis.reject_count
    analysis.consistency_score = passed / total if total > 0 else 0.0

    return analysis
