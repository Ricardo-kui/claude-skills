#!/usr/bin/env python3
"""
Compare template selection against original distilled skeletons to identify gaps.
Deterministic checks only (no LLM call in MVP).
"""

import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from parsers.json_abstraction import InputAbstract
from selectors.template_selector import TemplateSelection


@dataclass
class GapItem:
    slot_id: str
    section: str  # "methods" or "results"
    original_feature: str
    template_output: str
    gap_rating: str  # "无", "轻微", "中等", "严重"
    breakdown: str


@dataclass
class GapAnalysis:
    paper_id: str
    items: List[GapItem] = field(default_factory=list)
    coverage_score: float = 0.0
    critical_gaps: int = 0
    moderate_gaps: int = 0
    minor_gaps: int = 0


def _get_original_skeleton(methods_data: Dict, results_data: Dict, slot_id: str) -> str:
    """Extract original skeleton text for a slot from phase_2_distillation."""
    section = "methods" if slot_id.startswith("M") else "results"
    data = methods_data if section == "methods" else results_data
    phase2 = data.get("phase_2_distillation", {})

    # Try direct key like "M1_setting" or "R3_rhythm"
    for key in phase2.keys():
        if slot_id.lower() in key.lower():
            slot_data = phase2[key]
            if not isinstance(slot_data, dict):
                continue
            skeletons = slot_data.get("expression_skeletons", [])
            if skeletons:
                texts = [s.get("skeleton", "") for s in skeletons if isinstance(s, dict)]
                return "\n".join(texts)

    return ""


def _is_slot_located(methods_data: Dict, results_data: Dict, slot_id: str) -> bool:
    """Check phase_1_slot_map to see if original paper includes content for this slot."""
    section = "methods" if slot_id.startswith("M") else "results"
    data = methods_data if section == "methods" else results_data
    slot_map = data.get("phase_1_slot_map", {})
    slot_info = slot_map.get(slot_id, {})
    return slot_info.get("located", False)


def _check_slot_coverage(
    slot_id: str,
    selection: TemplateSelection,
    abstract: InputAbstract,
    original_skeleton: str,
    methods_data: Dict,
    results_data: Dict,
) -> Optional[GapItem]:
    """Check coverage for a single slot and return GapItem if gap exists."""
    section = "methods" if slot_id.startswith("M") else "results"
    sel_dict = selection.methods_selections if section == "methods" else selection.results_selections
    sel = sel_dict.get(slot_id)
    original_has_content = _is_slot_located(methods_data, results_data, slot_id)

    if not sel:
        # Slot not selected at all
        if original_has_content or original_skeleton:
            return GapItem(
                slot_id=slot_id,
                section=section,
                original_feature="Original has content for this slot",
                template_output="No template selected",
                gap_rating="严重",
                breakdown=f"Template library missing selection for {slot_id}",
            )
        return None

    # If no variants selected and no generic, but original has content
    if not sel.selected_variants and not sel.generic_used:
        if original_has_content or original_skeleton:
            return GapItem(
                slot_id=slot_id,
                section=section,
                original_feature="Original has content for this slot",
                template_output="Slot marked as not applicable",
                gap_rating="中等",
                breakdown=f"{slot_id} marked N/A but original paper includes it",
            )
        return None

    # Check if selected variants match original design markers
    rating = "无"
    breakdown = "Template selection matches original design"

    # Heuristic: if original skeleton contains design-specific terms not in selected variants
    if original_skeleton:
        # Check for U-shaped
        if "u-shaped" in original_skeleton.lower() or "turning point" in original_skeleton.lower():
            if not any("U-shaped" in v.name or "倒U型" in v.name for v in sel.selected_variants):
                rating = "严重"
                breakdown = f"Original contains U-shaped content but no U-shaped variant selected for {slot_id}"

        # Check for three-way interaction
        elif "three-way" in original_skeleton.lower() or "three way" in original_skeleton.lower():
            if not any("三向交互" in v.name for v in sel.selected_variants):
                rating = "严重"
                breakdown = f"Original contains three-way interaction but no variant selected for {slot_id}"

        # Check for recurrent event
        elif "recurrent" in original_skeleton.lower():
            if not any("复发事件" in v.name for v in sel.selected_variants):
                rating = "中等"
                breakdown = f"Original uses recurrent events but no recurrent-event variant selected for {slot_id}"

        # Check for CEM
        elif "coarsened exact matching" in original_skeleton.lower() or "cem" in original_skeleton.lower():
            if not any("CEM" in v.name or "粗化精确匹配" in v.name for v in sel.selected_variants):
                rating = "中等"
                breakdown = f"Original uses CEM but no CEM variant selected for {slot_id}"

        # Check for sample split (strict regex to avoid false positives; skip M1/M8)
        import re
        has_sample_split = bool(re.search(r'\bsplit the sample\b|\bsubsample\b|\bsub-sample\b', original_skeleton, re.IGNORECASE))
        if has_sample_split and slot_id not in ("M1", "M8"):
            if not any("子样本" in v.name for v in sel.selected_variants):
                rating = "轻微"
                breakdown = f"Original uses sample splits but no subsample variant selected for {slot_id}"

        # Check for spatial placebo
        elif "neighboring" in original_skeleton.lower() or "spatial" in original_skeleton.lower():
            if not any("空间安慰剂" in v.name for v in sel.selected_variants):
                rating = "轻微"
                breakdown = f"Original uses spatial placebo but no variant selected for {slot_id}"

        # Check for event study GLM
        elif "glm" in original_skeleton.lower() and "car" in original_skeleton.lower():
            if not any("GLM" in v.name and "CAR" in v.name for v in sel.selected_variants):
                rating = "中等"
                breakdown = f"Original uses GLM for CAR but no variant selected for {slot_id}"

        # Check for MCMC
        elif "mcmc" in original_skeleton.lower():
            if not any("MCMC" in v.name for v in sel.selected_variants):
                rating = "轻微"
                breakdown = f"Original uses MCMC but no MCMC variant selected for {slot_id}"

        # Check for LPM
        elif "linear probability" in original_skeleton.lower() or "lpm" in original_skeleton.lower():
            if not any("LPM" in v.name for v in sel.selected_variants):
                rating = "严重"
                breakdown = f"Original uses LPM but no LPM variant selected for {slot_id}"

        # Check for formal proof (network)
        elif "perfectly overlapping" in original_skeleton.lower() or "formally" in original_skeleton.lower():
            if not any("形式化识别证明" in v.name or "部分重叠" in v.name for v in sel.selected_variants):
                rating = "严重"
                breakdown = f"Original contains formal identification proof but no variant selected for {slot_id}"

    if rating != "无":
        return GapItem(
            slot_id=slot_id,
            section=section,
            original_feature=original_skeleton[:200] + "..." if len(original_skeleton) > 200 else original_skeleton,
            template_output=" | ".join(v.name for v in sel.selected_variants) if sel.selected_variants else "Generic template",
            gap_rating=rating,
            breakdown=breakdown,
        )

    return None


def analyze_gaps(
    abstract: InputAbstract,
    selection: TemplateSelection,
) -> GapAnalysis:
    """Main entry: compare selection against original and produce gap analysis."""
    methods_data = abstract.raw_methods
    results_data = abstract.raw_results

    analysis = GapAnalysis(paper_id=abstract.paper_id)

    all_slots = list(selection.methods_selections.keys()) + list(selection.results_selections.keys())
    covered = 0
    total = 0

    for slot_id in all_slots:
        total += 1
        original = _get_original_skeleton(methods_data, results_data, slot_id)
        gap = _check_slot_coverage(slot_id, selection, abstract, original, methods_data, results_data)

        if gap:
            analysis.items.append(gap)
            if gap.gap_rating == "严重":
                analysis.critical_gaps += 1
            elif gap.gap_rating == "中等":
                analysis.moderate_gaps += 1
            elif gap.gap_rating == "轻微":
                analysis.minor_gaps += 1
        else:
            covered += 1

    analysis.coverage_score = covered / total if total > 0 else 0.0
    return analysis
