#!/usr/bin/env python3
"""
Smoke test for reverse_validation_pipeline.

Builds minimal synthetic *_methods_distilled.json / *_results_distilled.json
per the pipeline's input contract, runs the CLI end-to-end (subprocess), and
asserts:
  - a clean pair        -> exit 0, report file produced, no critical gaps
  - a critical-gap pair -> exit 1 (critical gap detected), report still written
  - batch mode          -> batch_summary.md produced, exit 0 on clean pairs

The pipeline prints Chinese (design family) to stdout, so the subprocess runs
with `-X utf8` to avoid the Windows-GBK UnicodeEncodeError on piped output.
"""

import json
import subprocess
import sys
from pathlib import Path

# tests/ -> reverse_validation_pipeline/ -> skills root (holds write-methods/,
# write-results/, reverse_validation_pipeline/, and the SKILL.md files the
# pipeline parses). PIPELINE lives one level up from this tests/ dir.
REPO_ROOT = Path(__file__).resolve().parents[2]
PIPELINE = Path(__file__).resolve().parents[1] / "reverse_validation_pipeline.py"
PAPER_ID = "Smoke_Test_2026_ASQ"


# ---- shared phase_* blocks required by methods_results_quality_check ----
def _quality_gate() -> dict:
    return {
        "slot_coverage": {
            "coverage_rate": "100%",
            "present_slots": [
                "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10",
                "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9",
            ],
            "missing_slots": [],
        }
    }


def _phase_3() -> dict:
    # phase_3 IS the DNA dict the checker reads directly
    return {
        "because_density": 0.45,
        "sample_funnel_completeness": True,
        "diagnostic_foreshadowing_rate": 0.9,
        "hypothesis_alignment_density": 0.9,
        "temporal_clarity_density": 0.9,
    }


def _phase_5_qc() -> dict:
    return {"no_verbatim_copy": True, "fact_boundary": True}


# ---- minimal synthetic distilled JSON ----
def _clean_methods() -> dict:
    return {
        "paper_id": PAPER_ID,
        "phase_0": {
            "design_type": "ols/fe",
            "estimator_family": "OLS",
            "identification_strategy": "ordinary least squares with firm and year fixed effects",
            "dependent_variable": "firm performance",
            "independent_variables": "product recall misconduct",
        },
        "phase_1_slot_map": {
            "M1": {"located": False},
            "M2": {"located": False},
            "M3": {"located": True, "dv_construct": "firm performance", "operationalization": "Tobin's Q", "source": "Compustat"},
            "M4": {"located": True, "predictors": [
                {"name": "recall_conduct", "hypothesis_link": "H1"},
                {"name": "prior_misconduct", "hypothesis_link": "H2"},
            ]},
            "M5": {"located": True, "moderators": ["industry munificence"], "mediators": []},
            "M6": {"located": False},
            "M7": {"located": True, "estimator_named": "OLS", "diagnostics_named": ""},
            "M8": {"located": True, "identification_assumption": "", "test_location": ""},
            "M9": {"located": False},
            "M10": {"located": False},
        },
        "phase_1_5_quality_gate": _quality_gate(),
        "phase_2_distillation": {
            "expression_skeletons": [
                {"skeleton": "X is associated with Y, controlling for firm and year fixed effects"}
            ]
        },
        "phase_3": _phase_3(),
        "phase_5_qc": _phase_5_qc(),
    }


def _clean_results() -> dict:
    return {
        "paper_id": PAPER_ID,
        "phase_0": {
            "hypothesis_structure": (
                "H1: recall conduct is negatively associated with firm performance. "
                "H2: prior misconduct is negatively associated with firm performance."
            ),
            "number_of_nonsignificant_findings": 0,
            "estimator_family": "OLS",
            "nonsignificant_findings": "",
        },
        "phase_1_slot_map": {
            "R1": {"located": False},
            "R2": {"located": False},
            "R3": {"located": True, "hypotheses_covered": ["H1", "H2"], "nonsignificant_hypotheses": []},
            "R4": {"located": False},
            "R5": {"located": False},
            "R6": {"located": False},
            "R7": {"located": True, "threats_addressed": []},
            "R8": {"located": False},
            "R9": {"located": False},
        },
        "phase_1_5_quality_gate": _quality_gate(),
        "phase_2_distillation": {
            "expression_skeletons": [
                {"skeleton": "recall conduct is associated with firm performance in Model 2"}
            ]
        },
        "phase_3": _phase_3(),
        "phase_5_qc": _phase_5_qc(),
    }


def _critical_methods() -> dict:
    """Same as clean, but M1 located with a u-shaped skeleton that has no
    corresponding Methods variant in the corpus -> deterministic critical gap."""
    m = _clean_methods()
    m["phase_0"]["special_structure"] = "u-shaped"
    m["phase_1_slot_map"]["M1"] = {"located": True}
    m["phase_2_distillation"] = {
        "M1_setting": {
            "expression_skeletons": [
                {"skeleton": "The relationship is u-shaped; recall conduct is associated with firm performance"}
            ]
        }
    }
    return m


# ---- runner helpers ----
def _write_pair(directory: Path, methods: dict, results: dict) -> tuple:
    m_path = directory / f"{PAPER_ID}_methods_distilled.json"
    r_path = directory / f"{PAPER_ID}_results_distilled.json"
    m_path.write_text(json.dumps(methods, ensure_ascii=False, indent=2), encoding="utf-8")
    r_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    return m_path, r_path


def _run(args: list, cwd: Path = REPO_ROOT) -> subprocess.CompletedProcess:
    cmd = [sys.executable, "-X", "utf8", str(PIPELINE)] + args
    return subprocess.run(
        cmd, capture_output=True, text=True, encoding="utf-8", cwd=str(cwd),
    )


def _report_path(out_dir: Path) -> Path:
    return out_dir / "validation_output" / f"{PAPER_ID}_reverse_validation_report.md"


# ---- tests ----
def test_clean_pair_runs_end_to_end(tmp_path):
    """Clean pair: exit 0, report produced, zero critical gaps."""
    _write_pair(tmp_path, _clean_methods(), _clean_results())
    proc = _run([
        "--methods-json", str(tmp_path / f"{PAPER_ID}_methods_distilled.json"),
        "--results-json", str(tmp_path / f"{PAPER_ID}_results_distilled.json"),
        "--output-dir", str(tmp_path / "validation_output"),
        "--skills-dir", str(REPO_ROOT),
    ])
    assert proc.returncode == 0, f"stdout:\n{proc.stdout}\nstderr:\n{proc.stderr}"

    report = _report_path(tmp_path)
    assert report.exists(), "report file not produced"
    text = report.read_text(encoding="utf-8")
    assert "# Reverse End-to-End Validation Report" in text
    assert "Critical gaps: 0" in text
    assert "write-methods v2.5.0" in text or "Skills Tested" in text


def test_critical_gap_triggers_exit_1(tmp_path):
    """M1 u-shaped with no Methods variant -> critical gap, exit code 1."""
    _write_pair(tmp_path, _critical_methods(), _clean_results())
    proc = _run([
        "--methods-json", str(tmp_path / f"{PAPER_ID}_methods_distilled.json"),
        "--results-json", str(tmp_path / f"{PAPER_ID}_results_distilled.json"),
        "--output-dir", str(tmp_path / "validation_output"),
        "--skills-dir", str(REPO_ROOT),
    ])
    assert proc.returncode == 1, f"expected exit 1, got {proc.returncode}\n{proc.stdout}\n{proc.stderr}"

    report = _report_path(tmp_path)
    assert report.exists(), "report should still be produced on critical gaps"
    text = report.read_text(encoding="utf-8")
    assert "Critical gaps: 1" in text
    assert "u-shaped" in text.lower()


def test_batch_mode_produces_summary(tmp_path):
    """Batch mode: clean pair -> batch_summary.md, exit 0."""
    _write_pair(tmp_path, _clean_methods(), _clean_results())
    proc = _run([
        "--batch-dir", str(tmp_path),
        "--output-dir", str(tmp_path / "validation_output"),
        "--skills-dir", str(REPO_ROOT),
    ])
    assert proc.returncode == 0, f"stdout:\n{proc.stdout}\nstderr:\n{proc.stderr}"
    summary = tmp_path / "validation_output" / "batch_summary.md"
    assert summary.exists(), "batch_summary.md not produced"
    assert "Batch Reverse Validation Summary" in summary.read_text(encoding="utf-8")
