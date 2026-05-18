#!/usr/bin/env python3
"""
Parse distilled Methods/Results JSON files into a standardized InputAbstract.
"""

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class Hypothesis:
    id: str
    text: str
    direction: str = ""
    predicted_support: bool = True
    actual_support: Optional[bool] = None


@dataclass
class Variable:
    name: str
    construct: str = ""
    operationalization: str = ""
    source: str = ""
    level: str = ""  # firm, industry, state, etc.


@dataclass
class ModelSpec:
    estimator: str = ""
    distribution: str = ""
    fixed_effects: List[str] = field(default_factory=list)
    clustering: str = ""
    iv_instrument: str = ""
    first_stage_f: str = ""
    diagnostics: List[str] = field(default_factory=list)


@dataclass
class InputAbstract:
    paper_id: str
    journal: str
    design_type: str
    design_family: str
    special_markers: List[str] = field(default_factory=list)
    hypotheses: List[Hypothesis] = field(default_factory=list)
    dependent_variables: List[Variable] = field(default_factory=list)
    independent_variables: List[Variable] = field(default_factory=list)
    moderators: List[Variable] = field(default_factory=list)
    controls: List[Variable] = field(default_factory=list)
    model_spec: ModelSpec = field(default_factory=ModelSpec)
    robustness_checks: List[str] = field(default_factory=list)
    nonsignificant_findings: List[str] = field(default_factory=list)
    multi_study: bool = False
    study_count: int = 1
    raw_methods: Dict[str, Any] = field(default_factory=dict)
    raw_results: Dict[str, Any] = field(default_factory=dict)


def _infer_journal(paper_id: str) -> str:
    """Infer journal from paper_id like 'Zhou_Gao_Zhao_2017_ASQ'."""
    parts = paper_id.split("_")
    if len(parts) >= 2:
        return parts[-1]
    return "Unknown"


def _infer_design_type(methods_p0: Dict, results_p0: Dict) -> tuple:
    """
    Infer normalized design type and family from phase_0 metadata.
    Returns (design_type, design_family, special_markers)
    """
    estimator = methods_p0.get("estimator_family", "").lower()
    strategy = methods_p0.get("identification_strategy", "").lower()
    special = methods_p0.get("special_structure", "").lower()
    results_estimator = results_p0.get("estimator_family", "").lower()
    hypothesis_structure = results_p0.get("hypothesis_structure", "").lower()

    design_type = "unknown"
    design_family = "unknown"
    markers = []

    # Detect special markers first
    if "u-shaped" in special or "u-shaped" in hypothesis_structure:
        markers.append("u_shaped")
    if "three-way" in special or "three-way" in hypothesis_structure:
        markers.append("three_way_interaction")
    if "recurrent" in special or "recurrent" in estimator:
        markers.append("recurrent_event")
    if "cem" in special or "coarsened exact matching" in strategy:
        markers.append("cem_matching")
    if "event study" in special or "car" in special:
        markers.append("event_study_car")
    if "mcmc" in special:
        markers.append("mcmc_mediation")
    if "sample split" in special:
        markers.append("sample_split")
    if "conjoint" in special or "conjoint" in estimator or "amce" in estimator:
        markers.append("conjoint_experiment")

    # Word-boundary-safe matching for short keywords (e.g., "iv" matches "archival")
    _s = f" {strategy} "
    _e = f" {estimator} "

    # Determine design type
    if "tobit" in estimator and "poisson" in estimator and (" iv " in _s or " instrumental " in _s):
        design_type = "tobit + iv"
        design_family = "IV/2SLS"
    elif "poisson" in estimator and (" iv " in _s or " instrumental " in _s):
        design_type = "poisson + iv"
        design_family = "IV/2SLS"
    elif "lpm" in estimator and (" 2sls " in _s or " iv " in _s):
        design_type = "lpm + 2sls"
        design_family = "IV/2SLS"
        markers.append("lpm_2sls")
    elif "aft" in estimator or "weibull" in estimator or "cox" in estimator:
        design_type = "aft/weibull/survival"
        design_family = "生存分析"
        if "recurrent" in estimator:
            markers.append("recurrent_event")
    elif "did" in strategy or "difference-in-differences" in strategy:
        design_type = "did"
        design_family = "DiD"
    elif " iv " in _s or " 2sls " in _s or " instrumental " in _s:
        design_type = "iv/2sls"
        design_family = "IV/2SLS"
    elif "logit" in estimator or "probit" in estimator:
        design_type = "logit/probit"
        design_family = "非线性模型"
    elif "ols" in estimator:
        design_type = "ols/fe"
        design_family = "面板数据/OLS"
    elif "experiment" in strategy or "experiment" in estimator:
        design_type = "experiment"
        design_family = "实验"
    elif "network" in special or "peer" in special:
        design_type = "network/peer effects"
        design_family = "同伴效应/网络效应"
    elif "psm" in strategy and "did" in strategy:
        design_type = "psm + did"
        design_family = "匹配DiD"
    elif "count" in estimator or "negative binomial" in estimator or "poisson" in estimator:
        design_type = "count"
        design_family = "计数模型"
    elif "gmm" in estimator or "xtabond" in estimator or "arellano" in estimator:
        design_type = "dynamic_panel_gmm"
        design_family = "动态面板/GMM"
    elif "tobit" in estimator:
        design_type = "tobit"
        design_family = "非线性模型"
    elif "sem" in estimator or "structural equation" in strategy or "sur" in estimator or "seemingly unrelated" in estimator:
        design_type = "sem"
        design_family = "SEM"

    # Multi-study detection
    if "two-study" in special or "multi-study" in special:
        markers.append("multi_study")

    return design_type, design_family, markers


def _extract_hypotheses(results_p0: Dict, results_p1: Dict) -> List[Hypothesis]:
    """Extract hypotheses from Results phase_0 and phase_1."""
    hypotheses = []
    r3 = results_p1.get("R3", {})
    if not isinstance(r3, dict):
        r3 = {}

    covered = r3.get("hypotheses_covered", [])
    if isinstance(covered, str):
        covered = [covered] if covered else []
    nonsig = r3.get("nonsignificant_hypotheses", [])
    if isinstance(nonsig, str):
        nonsig = [nonsig] if nonsig else []

    for h_id in covered:
        if not h_id:
            continue
        h = Hypothesis(id=str(h_id), text=str(h_id))
        for ns in nonsig:
            if ns and str(h_id) in str(ns):
                h.predicted_support = False
                break
        hypotheses.append(h)

    # If no explicit list, try to infer from R3 keys like H1_result, H2a, etc.
    if not hypotheses:
        for key in r3.keys():
            m = re.match(r'(H\d+[a-z]?)', key)
            if m:
                h_id = m.group(1)
                h = Hypothesis(id=h_id, text=h_id)
                hypotheses.append(h)
        # Deduplicate by id
        seen = set()
        deduped = []
        for h in hypotheses:
            if h.id not in seen:
                seen.add(h.id)
                deduped.append(h)
        hypotheses = deduped

    # Final fallback: parse from hypothesis_structure
    if not hypotheses:
        structure = results_p0.get("hypothesis_structure", "")
        if isinstance(structure, str):
            for match in re.finditer(r'H\d+[a-z]?', structure):
                hypotheses.append(Hypothesis(id=match.group(), text=match.group()))

    return hypotheses


def _extract_variables(methods_p1: Dict) -> tuple:
    """Extract DV, IV, moderator, control variables from Methods phase_1."""
    dvs = []
    ivs = []
    mods = []
    ctrls = []

    # DV from M3
    m3 = methods_p1.get("M3", {})
    if m3.get("located"):
        dv = Variable(
            name=m3.get("dv_construct", "Dependent Variable"),
            operationalization=m3.get("operationalization", ""),
            source=m3.get("source", ""),
        )
        dvs.append(dv)

    # IV from M4
    m4 = methods_p1.get("M4", {})
    if m4.get("located"):
        for p in m4.get("predictors", []):
            if isinstance(p, dict):
                ivs.append(Variable(
                    name=p.get("name", ""),
                    construct=p.get("hypothesis_link", ""),
                ))
            elif isinstance(p, str):
                ivs.append(Variable(name=p))
        # Fallback: if no predictors list but construct_name exists
        if not ivs and m4.get("construct_name"):
            ivs.append(Variable(name=m4.get("construct_name", "")))

    # Moderators from M5
    m5 = methods_p1.get("M5", {})
    if m5.get("located"):
        for m in m5.get("moderators", []):
            if isinstance(m, dict):
                mods.append(Variable(name=m.get("name", "")))
            elif isinstance(m, str):
                mods.append(Variable(name=m))
        for m in m5.get("mediators", []):
            if isinstance(m, dict):
                mods.append(Variable(name=m.get("name", ""), construct="mediator"))
            elif isinstance(m, str):
                mods.append(Variable(name=m, construct="mediator"))

    # Controls from M6
    m6 = methods_p1.get("M6", {})
    if m6.get("located"):
        # Controls may not be explicitly listed in M6; look in phase_2
        pass

    return dvs, ivs, mods, ctrls


def _extract_model_spec(methods_p0: Dict, methods_p1: Dict) -> ModelSpec:
    """Extract model specification from Methods metadata."""
    spec = ModelSpec(
        estimator=methods_p0.get("estimator_family", ""),
    )

    m7 = methods_p1.get("M7", {})
    if m7.get("located"):
        spec.diagnostics = [d for d in [m7.get("estimator_named"), m7.get("diagnostics_named")] if d]

    m8 = methods_p1.get("M8", {})
    if m8.get("located"):
        test_loc = m8.get("test_location", "")
        # Try to extract first-stage F
        f_match = re.search(r'F\s*=\s*([\d.]+)', test_loc)
        if f_match:
            spec.first_stage_f = f_match.group(1)

    # Extract IV instrument from M8 or identification_strategy
    strategy = methods_p0.get("identification_strategy", "")
    iv_match = re.search(r'\(([^)]+)\)', strategy)
    if iv_match and "instrument" in strategy.lower():
        spec.iv_instrument = iv_match.group(1)

    return spec


def _extract_robustness(results_p1: Dict) -> List[str]:
    """Extract robustness checks from Results R7."""
    r7 = results_p1.get("R7", {})
    if r7.get("located"):
        return r7.get("threats_addressed", [])
    return []


def _extract_nonsignificant(results_p0: Dict, results_p1: Dict) -> List[str]:
    """Extract nonsignificant findings from R3 and R6."""
    findings = []
    r3 = results_p1.get("R3", {})
    for ns in r3.get("nonsignificant_hypotheses", []):
        findings.append(ns)
    # Also check R6 for nonsignificant count or located nonsignificant findings
    r6 = results_p1.get("R6", {})
    if r6.get("located", False):
        count = r6.get("nonsignificant_count", 0)
        if count > 0:
            findings.append(f"R6 reports {count} nonsignificant finding(s)")
    # Check phase_0 for explicit count
    num_nonsig = results_p0.get("number_of_nonsignificant_findings", 0)
    if num_nonsig > 0 and not findings:
        findings.append(f"phase_0 reports {num_nonsig} nonsignificant finding(s)")
    return findings


def parse_input_abstract(methods_json_path: Path, results_json_path: Path) -> InputAbstract:
    """Main entry: read both JSONs and produce InputAbstract."""
    with open(methods_json_path, "r", encoding="utf-8") as f:
        methods_data = json.load(f)
    with open(results_json_path, "r", encoding="utf-8") as f:
        results_data = json.load(f)

    paper_id = methods_data.get("paper_id", "unknown")
    journal = _infer_journal(paper_id)

    methods_p0 = methods_data.get("phase_0", {})
    methods_p1 = methods_data.get("phase_1_slot_map", {})
    results_p0 = results_data.get("phase_0", {})
    results_p1 = results_data.get("phase_1_slot_map", {})

    design_type, design_family, markers = _infer_design_type(methods_p0, results_p0)

    dvs, ivs, mods, ctrls = _extract_variables(methods_p1)
    model_spec = _extract_model_spec(methods_p0, methods_p1)
    robustness = _extract_robustness(results_p1)
    nonsig = _extract_nonsignificant(results_p0, results_p1)
    hypotheses = _extract_hypotheses(results_p0, results_p1)

    # Multi-study detection
    m9 = methods_p1.get("M9", {})
    multi_study = m9.get("located", False)
    study_count = m9.get("study_count", 1) if multi_study else 1

    return InputAbstract(
        paper_id=paper_id,
        journal=journal,
        design_type=design_type,
        design_family=design_family,
        special_markers=markers,
        hypotheses=hypotheses,
        dependent_variables=dvs,
        independent_variables=ivs,
        moderators=mods,
        controls=ctrls,
        model_spec=model_spec,
        robustness_checks=robustness,
        nonsignificant_findings=nonsig,
        multi_study=multi_study,
        study_count=study_count,
        raw_methods=methods_data,
        raw_results=results_data,
    )
