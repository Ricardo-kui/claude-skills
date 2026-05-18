#!/usr/bin/env python3
"""
Build a generation prompt from InputAbstract + TemplateSelection.
The prompt can be fed to Claude to produce filled Methods/Results drafts.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

from parsers.json_abstraction import InputAbstract
from parsers.skill_parser import TemplateVariant
from selectors.template_selector import SlotSelection, TemplateSelection


@dataclass
class GenerationPrompt:
    methods_prompt: str
    results_prompt: str
    metadata: Dict


def _build_slot_prompt(slot_sel: SlotSelection, generic_template: str) -> str:
    """Build prompt text for a single slot."""
    lines = [f"### {slot_sel.slot_id}"]

    if slot_sel.rationale:
        lines.append(f"<!-- Rationale: {slot_sel.rationale} -->")

    if slot_sel.selected_variants:
        for variant in slot_sel.selected_variants:
            lines.append(f"\n**{variant.name}**")
            if variant.composition_note:
                lines.append(f"<!-- Composition: {variant.composition_note} -->")
            lines.append("```text")
            lines.append(variant.template_text)
            lines.append("```")
    else:
        lines.append("\n**通用填空段落**")
        lines.append("```text")
        lines.append(generic_template)
        lines.append("```")

    return "\n".join(lines)


def _inject_variables(into_text: str, abstract: InputAbstract) -> str:
    """Simple placeholder substitution for known variables."""
    # Map common placeholders to abstract fields
    if abstract.dependent_variables:
        dv = abstract.dependent_variables[0]
        into_text = into_text.replace("[dependent variable]", dv.name)
        into_text = into_text.replace("[outcome]", dv.name)
        into_text = into_text.replace("[DV name]", dv.name)
        into_text = into_text.replace("[outcome construct]", dv.name)

    if abstract.independent_variables:
        iv = abstract.independent_variables[0]
        into_text = into_text.replace("[predictor]", iv.name)
        into_text = into_text.replace("[focal predictor]", iv.name)
        into_text = into_text.replace("[independent variable]", iv.name)

    # Replace journal
    into_text = into_text.replace("[journal]", abstract.journal)

    # Replace design type
    into_text = into_text.replace("[design type]", abstract.design_type)

    # Replace model/estimator
    into_text = into_text.replace("[estimator]", abstract.model_spec.estimator)
    into_text = into_text.replace("[model]", abstract.model_spec.estimator)

    # Replace IV instrument
    if abstract.model_spec.iv_instrument:
        into_text = into_text.replace("[instrument]", abstract.model_spec.iv_instrument)

    # Replace first-stage F
    if abstract.model_spec.first_stage_f:
        into_text = into_text.replace("[first-stage F]", abstract.model_spec.first_stage_f)

    return into_text


def build_generation_prompt(
    abstract: InputAbstract,
    selection: TemplateSelection,
    methods_lib,
    results_lib,
) -> GenerationPrompt:
    """Build the full generation prompt for Methods and Results."""

    # Build Methods prompt
    methods_lines = [
        f"# Methods Generation Prompt for {abstract.paper_id}",
        f"## Design Type: {abstract.design_type} | Journal: {abstract.journal}",
        "",
        "Fill in the bracketed placeholders below using the paper's specific information.",
        "",
    ]

    for slot_id in ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10"]:
        sel = selection.methods_selections.get(slot_id)
        if not sel:
            continue

        slot = methods_lib.get_slot(slot_id)
        generic = slot.generic_template if slot else ""

        slot_prompt = _build_slot_prompt(sel, generic)
        slot_prompt = _inject_variables(slot_prompt, abstract)
        methods_lines.append(slot_prompt)
        methods_lines.append("")

    # Build Results prompt
    results_lines = [
        f"# Results Generation Prompt for {abstract.paper_id}",
        f"## Design Type: {abstract.design_type} | Journal: {abstract.journal}",
        f"## Hypotheses: {', '.join(h.id for h in abstract.hypotheses)}",
        "",
        "Fill in the bracketed placeholders below using the paper's specific results.",
        "",
    ]

    for slot_id in ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9"]:
        sel = selection.results_selections.get(slot_id)
        if not sel:
            continue

        slot = results_lib.get_slot(slot_id)
        generic = slot.generic_template if slot else ""

        slot_prompt = _build_slot_prompt(sel, generic)
        slot_prompt = _inject_variables(slot_prompt, abstract)
        results_lines.append(slot_prompt)
        results_lines.append("")

    return GenerationPrompt(
        methods_prompt="\n".join(methods_lines),
        results_prompt="\n".join(results_lines),
        metadata={
            "paper_id": abstract.paper_id,
            "design_type": abstract.design_type,
            "journal": abstract.journal,
            "selected_variants": {
                "methods": {
                    k: v.variant_names for k, v in selection.methods_selections.items() if v.variant_names
                },
                "results": {
                    k: v.variant_names for k, v in selection.results_selections.items() if v.variant_names
                },
            },
        },
    )
