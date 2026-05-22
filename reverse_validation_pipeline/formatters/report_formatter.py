#!/usr/bin/env python3
"""
Format InputAbstract, TemplateSelection, and GapAnalysis into standard Markdown report.
"""

from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from parsers.json_abstraction import InputAbstract
from generators.prompt_builder import GenerationPrompt
from analyzers.gap_analyzer import GapAnalysis, GapItem
from analyzers.cross_skill_consistency_analyzer import ConsistencyAnalysis
from selectors.template_selector import TemplateSelection


def _format_input_abstract(abstract: InputAbstract) -> str:
    lines = [
        "## 1. Input Abstraction",
        "",
        f"**Paper ID**: {abstract.paper_id}",
        f"**Journal**: {abstract.journal}",
        f"**Design Type**: {abstract.design_type}",
        f"**Design Family**: {abstract.design_family}",
        f"**Special Markers**: {', '.join(abstract.special_markers) if abstract.special_markers else 'None'}",
        f"**Multi-study**: {abstract.multi_study} ({abstract.study_count} studies)" if abstract.multi_study else "**Multi-study**: False",
        "",
        "### Hypotheses",
    ]
    for h in abstract.hypotheses:
        support = "Supported" if h.predicted_support else "Not supported / Nonsignificant"
        lines.append(f"- **{h.id}**: {h.text} ({support})")

    lines.extend(["", "### Variables"])
    lines.append(f"- **DV**: {', '.join(v.name for v in abstract.dependent_variables)}")
    lines.append(f"- **IV**: {', '.join(v.name for v in abstract.independent_variables)}")
    lines.append(f"- **Moderators**: {', '.join(v.name for v in abstract.moderators)}")
    lines.append(f"- **Controls**: {', '.join(v.name for v in abstract.controls)}")

    lines.extend(["", "### Model Specification"])
    spec = abstract.model_spec
    lines.append(f"- **Estimator**: {spec.estimator}")
    if spec.distribution:
        lines.append(f"- **Distribution**: {spec.distribution}")
    if spec.iv_instrument:
        lines.append(f"- **IV Instrument**: {spec.iv_instrument}")
    if spec.first_stage_f:
        lines.append(f"- **First-stage F**: {spec.first_stage_f}")
    if spec.fixed_effects:
        lines.append(f"- **Fixed Effects**: {', '.join(spec.fixed_effects)}")

    lines.extend(["", "### Robustness Checks"])
    for rc in abstract.robustness_checks:
        lines.append(f"- {rc}")

    if abstract.nonsignificant_findings:
        lines.extend(["", "### Nonsignificant Findings"])
        for ns in abstract.nonsignificant_findings:
            lines.append(f"- {ns}")

    return "\n".join(lines)


def _format_gap_table(analysis: GapAnalysis) -> str:
    lines = [
        "## 4. Gap Analysis Table",
        "",
        "| Slot | Original Feature | Template Output | Gap Rating | Specific Breakdown |",
        "|------|-----------------|-----------------|------------|-------------------|",
    ]

    # Sort by severity
    severity_order = {"严重": 0, "中等": 1, "轻微": 2, "无": 3}
    sorted_items = sorted(analysis.items, key=lambda x: severity_order.get(x.gap_rating, 99))

    for item in sorted_items:
        orig = item.original_feature.replace("|", "\\|").replace("\n", " ")
        if len(orig) > 120:
            orig = orig[:117] + "..."
        template = item.template_output.replace("|", "\\|")
        if len(template) > 80:
            template = template[:77] + "..."
        breakdown = item.breakdown.replace("|", "\\|").replace("\n", " ")
        lines.append(f"| **{item.slot_id}** | {orig} | {template} | **{item.gap_rating}** | {breakdown} |")

    if not sorted_items:
        lines.append("| — | — | — | **无** | No gaps detected in automated checks |")

    lines.extend([
        "",
        f"**Coverage Score**: {analysis.coverage_score:.0%}",
        f"- Critical gaps: {analysis.critical_gaps}",
        f"- Moderate gaps: {analysis.moderate_gaps}",
        f"- Minor gaps: {analysis.minor_gaps}",
    ])

    return "\n".join(lines)


def _format_recommendations(analysis: GapAnalysis) -> str:
    lines = [
        "## 5. Summary of Key Findings and Recommendations",
        "",
        "### 5.1 Critical Gaps (Require Template Fixes)",
        "",
    ]

    critical = [i for i in analysis.items if i.gap_rating == "严重"]
    moderate = [i for i in analysis.items if i.gap_rating == "中等"]
    minor = [i for i in analysis.items if i.gap_rating == "轻微"]

    if critical:
        for item in critical:
            lines.append(f"1. **{item.slot_id}**: {item.breakdown}")
    else:
        lines.append("No critical gaps detected.")

    lines.extend(["", "### 5.2 Moderate Gaps (Recommended Improvements)", ""])
    if moderate:
        for item in moderate:
            lines.append(f"1. **{item.slot_id}**: {item.breakdown}")
    else:
        lines.append("No moderate gaps detected.")

    lines.extend(["", "### 5.3 Minor Gaps (Cosmetic Adjustments)", ""])
    if minor:
        for item in minor:
            lines.append(f"1. **{item.slot_id}**: {item.breakdown}")
    else:
        lines.append("No minor gaps detected.")

    lines.extend([
        "",
        "### 5.4 Overall Assessment",
        "",
        f"| Dimension | Score | Notes |",
        f"|-----------|-------|-------|",
        f"| **Slot Coverage** | {analysis.coverage_score:.0%} | Based on template selection vs original presence |",
        f"| **Critical Gaps** | {len(critical)} | Requires new template variants or design-type mapping updates |",
        f"| **Moderate Gaps** | {len(moderate)} | Recommended improvements to existing variants |",
        f"| **Minor Gaps** | {len(minor)} | Cosmetic/style adjustments |",
    ])

    return "\n".join(lines)


def _format_qc_section(qc_reports: Dict) -> str:
    """Format forward QC results as a markdown section."""
    if not qc_reports:
        return ""

    lines = [
        "## 6. Forward Quality Check (Distillation QC)",
        "",
        "> This section embeds the forward quality-check results from `methods_results_quality_check.py`, "
        "run against the original distilled JSONs. It validates the input data quality before template selection.",
        "",
    ]

    for check_type in ["methods", "results"]:
        report = qc_reports.get(check_type)
        if not report:
            continue
        status_emoji = {"PASS": "", "FLAG": "⚠️", "REJECT": ""}.get(report.overall_status.value, "")
        lines.append(f"### {check_type.upper()} QC: {status_emoji} {report.overall_status.value}")
        lines.append("")

        # Group by severity
        for sev in ["REJECT", "FLAG", "PASS"]:
            items = [i for i in report.items if i.severity.value == sev]
            if not items:
                continue
            lines.append(f"**{sev}** ({len(items)} checks)")
            for item in items:
                detail = item.detail.replace("|", "\\|").replace("\n", " ")
                if len(detail) > 120:
                    detail = detail[:117] + "..."
                lines.append(f"- `{item.check_id}` — {item.description}")
                if detail:
                    lines.append(f"  - {detail}")
            lines.append("")

        summary = report.summary
        if summary:
            lines.append(f"*Summary: {summary.get('pass_count', 0)} pass, {summary.get('flag_count', 0)} flag, {summary.get('reject_count', 0)} reject*")
            lines.append("")

    return "\n".join(lines)


def _format_consistency_section(consistency: ConsistencyAnalysis) -> str:
    """Format cross-skill consistency results as a markdown section."""
    if not consistency or not consistency.items:
        return ""

    lines = [
        "## 7. Cross-Skill Consistency (Methods ↔ Results)",
        "",
        "> This section checks whether the Methods and Results narratives are internally consistent.",
        "",
        f"**Consistency Score**: {consistency.consistency_score:.0%}",
        f"- FLAG items: {consistency.flag_count}",
        f"- REJECT items: {consistency.reject_count}",
        "",
        "### Consistency Checks",
        "",
    ]

    for item in consistency.items:
        status_emoji = {"PASS": "", "FLAG": "⚠️", "REJECT": ""}.get(item.status, "")
        lines.append(f"- **{item.check_id}** {status_emoji} {item.status}: {item.description}")
        if item.detail:
            detail = item.detail.replace("|", "\\|").replace("\n", " ")
            if len(detail) > 120:
                detail = detail[:117] + "..."
            lines.append(f"  - *{detail}*")

    lines.append("")
    return "\n".join(lines)


def format_report(
    abstract: InputAbstract,
    prompt: GenerationPrompt,
    selection: TemplateSelection,
    analysis: GapAnalysis,
    skill_version: str = "2.5.0",
    qc_reports: Optional[Dict] = None,
    consistency: Optional[ConsistencyAnalysis] = None,
) -> str:
    """Produce the full markdown report."""
    lines = [
        "# Reverse End-to-End Validation Report (Automated)",
        f"## Paper: {abstract.paper_id}",
        f"## Skills Tested: write-methods v{skill_version}, write-results v{skill_version}",
        f"## Date: {datetime.now().strftime('%Y-%m-%d')}",
        f"## Automation Level: Deterministic template selection + heuristic gap analysis",
        "",
        "> **Note**: This report was generated by the automated reverse validation pipeline. "
        "The gap analysis uses deterministic heuristics to compare selected template variants against original distilled skeletons. "
        "For nuanced gaps requiring natural language understanding, manual review is still recommended.",
        "",
    ]

    lines.append(_format_input_abstract(abstract))
    lines.append("")

    lines.extend([
        "## 2. Template Selection",
        "",
        "### Methods Variants Selected",
    ])
    for slot_id in ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10"]:
        sel = selection.methods_selections.get(slot_id)
        if sel and sel.variant_names:
            lines.append(f"- **{slot_id}**: {', '.join(sel.variant_names)}")

    lines.extend(["", "### Results Variants Selected"])
    for slot_id in ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9"]:
        sel = selection.results_selections.get(slot_id)
        if sel and sel.variant_names:
            lines.append(f"- **{slot_id}**: {', '.join(sel.variant_names)}")

    lines.append("")
    lines.append("## 3. Generation Prompt")
    lines.append("")
    lines.append("> The generation prompt is saved separately as `generation_prompt.md`.")
    lines.append("")

    lines.append(_format_gap_table(analysis))
    lines.append("")

    lines.append(_format_recommendations(analysis))
    lines.append("")

    if qc_reports:
        lines.append(_format_qc_section(qc_reports))
        lines.append("")

    if consistency:
        lines.append(_format_consistency_section(consistency))
        lines.append("")

    lines.append("---")
    lines.append(f"*Report generated by reverse_validation_pipeline.py v0.1.0 against {abstract.paper_id}.*")

    return "\n".join(lines)


def write_report(
    report_text: str,
    prompt: GenerationPrompt,
    output_dir: Path,
    paper_id: str,
) -> None:
    """Write report and prompt files to output directory."""
    output_dir.mkdir(parents=True, exist_ok=True)

    # Sanitize paper_id for filename
    safe_id = paper_id.replace(" ", "_").replace("/", "_")

    report_path = output_dir / f"{safe_id}_reverse_validation_report.md"
    report_path.write_text(report_text, encoding="utf-8")

    prompt_path = output_dir / f"{safe_id}_generation_prompt.md"
    prompt_path.write_text(
        f"# Methods Generation Prompt\n\n{prompt.methods_prompt}\n\n"
        f"---\n\n# Results Generation Prompt\n\n{prompt.results_prompt}",
        encoding="utf-8",
    )

    print(f"Report saved to: {report_path}")
    print(f"Prompt saved to: {prompt_path}")
