#!/usr/bin/env python3
"""
Automated Reverse End-to-End Validation Pipeline for write-methods / write-results skills.

Usage:
    python reverse_validation_pipeline.py \
        --methods-json zhou_2017_methods_distilled.json \
        --results-json zhou_2017_results_distilled.json \
        --output-dir ./validation_output

Batch mode:
    python reverse_validation_pipeline.py \
        --batch-dir ./distilled_jsons \
        --output-dir ./validation_output
"""

import argparse
import sys
from pathlib import Path
from typing import List, Tuple

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from parsers.json_abstraction import parse_input_abstract
from parsers.skill_parser import parse_skill_md
from selectors.template_selector import select_templates
from generators.prompt_builder import build_generation_prompt
from analyzers.gap_analyzer import analyze_gaps
from formatters.report_formatter import format_report, write_report
from analyzers.cross_skill_consistency_analyzer import analyze_cross_skill_consistency

# Forward QC integration
sys.path.insert(0, str(Path(__file__).parent.parent))
from methods_results_quality_check import MethodsChecker, ResultsChecker, Severity


def _find_distilled_pairs(batch_dir: Path) -> List[Tuple[Path, Path]]:
    """Find matching methods+results distilled JSON pairs in a directory."""
    methods_files = sorted(batch_dir.glob("*_methods_distilled.json"))
    pairs = []
    for m_path in methods_files:
        prefix = m_path.name.replace("_methods_distilled.json", "")
        r_path = m_path.parent / f"{prefix}_results_distilled.json"
        if r_path.exists():
            pairs.append((m_path, r_path))
    return pairs


def process_single_pair(
    methods_path: Path,
    results_path: Path,
    output_dir: Path,
    skills_dir: Path,
    version: str,
    methods_lib=None,
    results_lib=None,
) -> Tuple[str, int, int, int, float]:
    """Process a single methods+results pair and return summary stats."""
    if not methods_path.exists():
        print(f"Error: Methods JSON not found: {methods_path}", file=sys.stderr)
        return (methods_path.stem, 0, 0, 0, 0.0)
    if not results_path.exists():
        print(f"Error: Results JSON not found: {results_path}", file=sys.stderr)
        return (results_path.stem, 0, 0, 0, 0.0)

    # 1. Parse input abstract
    print(f"\n[1/6] Parsing input abstract from {methods_path.name} + {results_path.name}...")
    abstract = parse_input_abstract(methods_path, results_path)
    print(f"  Paper: {abstract.paper_id}")
    print(f"  Design: {abstract.design_type} ({abstract.design_family})")
    print(f"  Markers: {abstract.special_markers}")
    print(f"  Hypotheses: {len(abstract.hypotheses)}")

    # 2. Parse SKILL.md files (reuse if provided)
    print("[2/6] Parsing SKILL.md templates...")
    if methods_lib is None:
        methods_skill_path = skills_dir / "write-methods" / "SKILL.md"
        if methods_skill_path.exists():
            methods_lib = parse_skill_md(methods_skill_path)
    if results_lib is None:
        results_skill_path = skills_dir / "write-results" / "SKILL.md"
        if results_skill_path.exists():
            results_lib = parse_skill_md(results_skill_path)

    if not methods_lib or not results_lib:
        print("Error: Could not load one or both SKILL.md files. Skipping.", file=sys.stderr)
        return (abstract.paper_id, 0, 0, 0, 0.0)

    print(f"  Methods slots: {len(methods_lib.slots)}, variants: {sum(len(s.variants) for s in methods_lib.slots.values())}")
    print(f"  Results slots: {len(results_lib.slots)}, variants: {sum(len(s.variants) for s in results_lib.slots.values())}")

    # 3. Select templates
    print("[3/6] Selecting template variants...")
    selection = select_templates(abstract, methods_lib, results_lib)
    methods_selected = sum(1 for s in selection.methods_selections.values() if s.selected_variants)
    results_selected = sum(1 for s in selection.results_selections.values() if s.selected_variants)
    print(f"  Methods slots with variants: {methods_selected}/10")
    print(f"  Results slots with variants: {results_selected}/9")

    # 4. Build generation prompt
    print("[4/6] Building generation prompt...")
    prompt = build_generation_prompt(abstract, selection, methods_lib, results_lib)
    print(f"  Methods prompt length: {len(prompt.methods_prompt)} chars")
    print(f"  Results prompt length: {len(prompt.results_prompt)} chars")

    # 5. Analyze gaps
    print("[5/6] Analyzing gaps...")
    analysis = analyze_gaps(abstract, selection)
    print(f"  Coverage score: {analysis.coverage_score:.0%}")
    print(f"  Critical gaps: {analysis.critical_gaps}")
    print(f"  Moderate gaps: {analysis.moderate_gaps}")
    print(f"  Minor gaps: {analysis.minor_gaps}")

    # 5.5 Forward QC
    print("[5.5/6] Running forward quality checks...")
    import json
    with open(methods_path, "r", encoding="utf-8") as f:
        methods_data = json.load(f)
    with open(results_path, "r", encoding="utf-8") as f:
        results_data = json.load(f)
    methods_qc = MethodsChecker(methods_data).run()
    results_qc = ResultsChecker(results_data).run()
    qc_reports = {"methods": methods_qc, "results": results_qc}
    print(f"  Methods QC: {methods_qc.overall_status.value}")
    print(f"  Results QC: {results_qc.overall_status.value}")

    # 5.6 Cross-skill consistency
    print("[5.6/6] Checking cross-skill consistency...")
    consistency = analyze_cross_skill_consistency(abstract)
    print(f"  Consistency score: {consistency.consistency_score:.0%}")
    print(f"  Flags: {consistency.flag_count}, Rejects: {consistency.reject_count}")

    # 6. Format and write report
    print("[6/6] Formatting report...")
    report_text = format_report(
        abstract, prompt, selection, analysis, version,
        qc_reports=qc_reports, consistency=consistency,
    )
    write_report(report_text, prompt, output_dir, abstract.paper_id)

    return (
        abstract.paper_id,
        analysis.critical_gaps,
        analysis.moderate_gaps,
        analysis.minor_gaps,
        analysis.coverage_score,
        methods_qc.overall_status.value,
        results_qc.overall_status.value,
        consistency.consistency_score,
    )


def _write_batch_summary(
    output_dir: Path,
    results: List[Tuple],
    version: str,
) -> None:
    """Write a batch-level summary markdown file."""
    lines = [
        "# Batch Reverse Validation Summary",
        f"**Skill Version**: write-methods / write-results v{version}",
        f"**Date**: {__import__('datetime').datetime.now().strftime('%Y-%m-%d')}",
        f"**Papers Processed**: {len(results)}",
        "",
        "## Per-Paper Overview",
        "",
        "| Paper ID | Coverage | Critical | Moderate | Minor | Methods QC | Results QC | Consistency | Status |",
        "|----------|----------|----------|----------|-------|------------|------------|-------------|--------|",
    ]

    total_critical = 0
    total_moderate = 0
    total_minor = 0
    total_coverage = 0.0

    total_consistency = 0.0
    for row in results:
        paper_id, critical, moderate, minor, coverage = row[:5]
        methods_qc = row[5] if len(row) > 5 else "N/A"
        results_qc = row[6] if len(row) > 6 else "N/A"
        consistency = row[7] if len(row) > 7 else 0.0
        total_critical += critical
        total_moderate += moderate
        total_minor += minor
        total_coverage += coverage
        total_consistency += consistency
        status = "PASS" if critical == 0 else "FAIL"
        lines.append(
            f"| {paper_id} | {coverage:.0%} | {critical} | {moderate} | {minor} | {methods_qc} | {results_qc} | {consistency:.0%} | **{status}** |"
        )

    avg_coverage = total_coverage / len(results) if results else 0.0
    avg_consistency = total_consistency / len(results) if results else 0.0
    lines.extend([
        "",
        "## Aggregate Statistics",
        "",
        f"- **Average Coverage**: {avg_coverage:.0%}",
        f"- **Average Cross-Skill Consistency**: {avg_consistency:.0%}",
        f"- **Total Critical Gaps**: {total_critical}",
        f"- **Total Moderate Gaps**: {total_moderate}",
        f"- **Total Minor Gaps**: {total_minor}",
        f"- **Papers with Critical Gaps**: {sum(1 for r in results if r[1] > 0)} / {len(results)}",
        "",
        "## Detailed Reports",
        "",
    ])

    for row in results:
        paper_id = row[0]
        safe_id = paper_id.replace(" ", "_").replace("/", "_")
        lines.append(f"- [{safe_id}]({safe_id}_reverse_validation_report.md)")

    lines.append("")
    summary_path = output_dir / "batch_summary.md"
    summary_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nBatch summary saved to: {summary_path}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Automated reverse validation pipeline for academic writing skills"
    )
    parser.add_argument(
        "--methods-json", "-m", help="Path to *_methods_distilled.json"
    )
    parser.add_argument(
        "--results-json", "-r", help="Path to *_results_distilled.json"
    )
    parser.add_argument(
        "--batch-dir", "-b", help="Directory containing multiple distilled JSON pairs to process in batch"
    )
    parser.add_argument(
        "--output-dir", "-o", default="./validation_output", help="Output directory"
    )
    parser.add_argument(
        "--skills-dir",
        default=str(Path(__file__).parent.parent),
        help="Directory containing write-methods/ and write-results/ skills",
    )
    parser.add_argument(
        "--version", default="2.5.0", help="Skill version string for report header"
    )

    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    skills_dir = Path(args.skills_dir)

    # Pre-load SKILL.md files once for batch reuse
    methods_lib = None
    results_lib = None
    methods_skill_path = skills_dir / "write-methods" / "SKILL.md"
    results_skill_path = skills_dir / "write-results" / "SKILL.md"
    if methods_skill_path.exists():
        methods_lib = parse_skill_md(methods_skill_path)
    if results_skill_path.exists():
        results_lib = parse_skill_md(results_skill_path)

    if not methods_lib or not results_lib:
        print("Error: Could not load one or both SKILL.md files. Exiting.", file=sys.stderr)
        return 1

    if args.batch_dir:
        batch_dir = Path(args.batch_dir)
        if not batch_dir.exists():
            print(f"Error: Batch directory not found: {batch_dir}", file=sys.stderr)
            return 1

        pairs = _find_distilled_pairs(batch_dir)
        if not pairs:
            print(f"Warning: No distilled JSON pairs found in {batch_dir}", file=sys.stderr)
            return 0

        print(f"Found {len(pairs)} distilled JSON pair(s) in {batch_dir}")
        results = []
        exit_code = 0
        for methods_path, results_path in pairs:
            stats = process_single_pair(
                methods_path, results_path, output_dir, skills_dir, args.version,
                methods_lib=methods_lib, results_lib=results_lib,
            )
            results.append(stats)
            if stats[1] > 0:
                exit_code = 1

        _write_batch_summary(output_dir, results, args.version)
        print(f"\nBatch complete. {sum(1 for r in results if r[1] > 0)} paper(s) with critical gaps.")
        return exit_code

    elif args.methods_json and args.results_json:
        stats = process_single_pair(
            Path(args.methods_json), Path(args.results_json), output_dir, skills_dir, args.version,
            methods_lib=methods_lib, results_lib=results_lib,
        )
        if stats[1] > 0:
            return 1
        return 0

    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
