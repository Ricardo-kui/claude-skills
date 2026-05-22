#!/usr/bin/env python3
"""
Normalize distilled JSON files to the canonical schema expected by the pipeline.
Agents sometimes produce slightly different key names or value types.
"""

import json
import re
import sys
from pathlib import Path


def normalize_slot_key(key: str, section: str) -> str:
    """Normalize descriptive slot keys to canonical M1/M2/R1/R2 format."""
    prefix = "M" if section == "methods" else "R"
    if key.startswith(prefix) and len(key) > 1 and key[1].isdigit():
        # Already starts with M1, R2, etc. — extract prefix + digit(s)
        m = re.match(rf"({prefix}\d+)", key)
        if m:
            return m.group(1)
    return key


def normalize_phase_0(data: dict) -> dict:
    """Rename phase_0_metadata to phase_0 if needed."""
    if "phase_0_metadata" in data and "phase_0" not in data:
        data["phase_0"] = data.pop("phase_0_metadata")
    return data


def normalize_phase_1_slot_map(data: dict, section: str) -> dict:
    """Normalize phase_1_slot_map keys to canonical format."""
    slot_map = data.get("phase_1_slot_map", {})
    if not isinstance(slot_map, dict):
        return data
    normalized = {}
    for key, value in slot_map.items():
        norm_key = normalize_slot_key(key, section)
        normalized[norm_key] = value
    data["phase_1_slot_map"] = normalized
    return data


def normalize_phase_1_5(data: dict, section: str) -> dict:
    """Ensure phase_1_5_quality_gate exists with proper structure."""
    gate = data.get("phase_1_5_quality_gate", {})
    if not isinstance(gate, dict):
        gate = {}

    slot_map = data.get("phase_1_slot_map", {})
    required_prefix = "M" if section == "methods" else "R"
    present = [k for k in slot_map.keys() if k.startswith(required_prefix) and slot_map[k].get("located", False)]
    required = [f"{required_prefix}{i}" for i in range(1, 11 if section == "methods" else 10)]
    missing = [r for r in required if r not in present]
    rate = round(len(present) / len(required) * 100)

    coverage = gate.get("slot_coverage", {})
    if isinstance(coverage, str):
        # Try to parse a percentage from the string
        m = re.search(r'(\d+)%', coverage)
        if m:
            rate = int(m.group(1))
        coverage = {
            "required_slots": required,
            "present_slots": present,
            "missing_slots": missing,
            "coverage_rate": f"{rate}%",
        }
    elif not isinstance(coverage, dict):
        coverage = {
            "required_slots": required,
            "present_slots": present,
            "missing_slots": missing,
            "coverage_rate": f"{rate}%",
        }
    else:
        # Ensure all fields exist
        coverage.setdefault("required_slots", required)
        coverage.setdefault("present_slots", present)
        coverage.setdefault("missing_slots", missing)
        coverage.setdefault("coverage_rate", f"{rate}%")

    gate["slot_coverage"] = coverage

    # Ensure other gate fields exist
    gate.setdefault("special_design_markers", {"detected": [], "properly_addressed": [], "inadequately_addressed": []})
    gate.setdefault("source_sufficiency", {"sample_funnel_auditable": True, "diagnostic_tests_named": True, "robustness_location_specified": True})
    gate.setdefault("contradictions_or_gaps", [])
    gate.setdefault("information_poverty_dimensions", [])

    data["phase_1_5_quality_gate"] = gate
    return data


def normalize_phase_2(data: dict) -> dict:
    """Normalize phase_2_distillation values to canonical structure."""
    phase2 = data.get("phase_2_distillation", {})
    if not isinstance(phase2, dict):
        phase2 = {}

    normalized = {}
    for key, value in phase2.items():
        if value is None:
            continue
        if isinstance(value, str):
            # Flat string skeleton — wrap it
            normalized[key] = {
                "persuasive_action": "",
                "expression_skeletons": [
                    {
                        "skeleton": value,
                        "transferability": "",
                        "paradigm_exclusivity": "",
                        "design_variants": [],
                    }
                ],
                "validity_logic": {"internal": "", "construct": "", "external": ""},
            }
        elif isinstance(value, dict):
            if "expression_skeleton" in value and isinstance(value["expression_skeleton"], str):
                # Old-style single skeleton string
                skel = value.pop("expression_skeleton", "")
                func = value.pop("function", "")
                value["persuasive_action"] = func
                value["expression_skeletons"] = [
                    {
                        "skeleton": skel,
                        "transferability": "",
                        "paradigm_exclusivity": "",
                        "design_variants": [],
                    }
                ]
                value.setdefault("validity_logic", {"internal": "", "construct": "", "external": ""})
            elif "expression_skeletons" not in value and "skeleton" in value:
                # Single nested skeleton dict
                value["expression_skeletons"] = [value.pop("skeleton")] if isinstance(value["skeleton"], dict) else []
            normalized[key] = value
        else:
            normalized[key] = value

    data["phase_2_distillation"] = normalized
    return data


def normalize_phase_5(data: dict) -> dict:
    """Normalize phase_5_qc values to booleans."""
    qc = data.get("phase_5_qc", {})
    if not isinstance(qc, dict):
        qc = {}
    for key in ["completeness", "clarity", "credibility", "replicability", "no_verbatim_copy", "fact_boundary", "causal_language_audit"]:
        val = qc.get(key, "")
        if isinstance(val, str):
            qc[key] = val.upper() == "PASS"
        elif not isinstance(val, bool):
            qc[key] = False
    data["phase_5_qc"] = qc
    return data


def normalize_paper_id(data: dict) -> dict:
    """Ensure paper_id is set."""
    if not data.get("paper_id"):
        p0 = data.get("phase_0", {})
        pid = p0.get("paper_id", "unknown")
        data["paper_id"] = pid
    return data


def normalize(data: dict, section: str) -> dict:
    """Apply all normalizations."""
    data = normalize_phase_0(data)
    data = normalize_paper_id(data)
    data = normalize_phase_1_slot_map(data, section)
    data = normalize_phase_1_5(data, section)
    data = normalize_phase_2(data)
    data = normalize_phase_5(data)
    return data


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <input.json> <output.json> [--methods|--results]")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    section = "methods"
    if "--results" in sys.argv:
        section = "results"

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    data = normalize(data, section)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Normalized {input_path} -> {output_path}")


if __name__ == "__main__":
    main()
