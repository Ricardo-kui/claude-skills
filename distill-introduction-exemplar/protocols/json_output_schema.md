# JSON Output Schema

> 外置自 `distill-introduction-exemplar/SKILL.md`。何时加载：仅在用户要求 --output-format=json 时加载。

---

## JSON Output Schema

当使用 `--output-format=json` 时，输出严格符合以下 schema。

```json
{
  "$schema": "distill-introduction-exemplar-batch/v2.2",
  "paper_id": "string",
  "phase_0_combo_profile": {
    "gap_type": "string",
    "contribution_dimension": "string",
    "conversation_strategy": "string",
    "hook_energy_level": "string",
    "narrative_structure": "string",
    "narrative_arc": "string",
    "introduction_length": "number",
    "paragraph_count": "number",
    "has_explicit_puzzle_statement": "boolean",
    "has_stakes_paragraph": "boolean"
  },
  "phase_0_story_architecture": {
    "central_knot_statement": "string",
    "protagonist_construct": "string",
    "supporting_constructs": ["string"],
    "daviss_index_types": ["string"],
    "front_end_consistent": "boolean"
  },
  "phase_1_module_map": {
    "hook": { "located": "boolean", "paragraph_range": "string", "hook_type": "string", "hook_energy_level": "string", "serves_puzzle": "boolean" },
    "literature_turn": { "located": "boolean", "paragraph_range": "string", "conversation_strategy": "string", "core_citations_count": "number", "establishes_common_ground": "boolean" },
    "tension": { "located": "boolean", "paragraph_range": "string", "gap_type_language": "string", "beyond_few_studies": "boolean", "has_specific_pain": "boolean" },
    "stakes": { "located": "boolean", "paragraph_range": "string", "stakes_type": "string", "quantified": "boolean" },
    "theory_lens": { "located": "boolean", "paragraph_range": "string", "theoretical_source": "string", "responds_to_gap": "boolean" },
    "preview": { "located": "boolean", "paragraph_range": "string", "preview_scope": "string", "overclaiming_risk": "boolean" },
    "contribution": { "located": "boolean", "paragraph_range": "string", "makadok_dimensions_visible": ["string"], "discussable": "boolean" }
  },
  "phase_1_5_quality_gate": {
    "module_coverage": { "required_modules": ["string"], "present_modules": ["string"], "missing_modules": ["string"], "coverage_rate": "string", "module_skip_detected": "object" },
    "combo_alignment": { "detected_combo": "string", "properly_addressed": ["string"], "inadequately_addressed": ["string"] },
    "narrative_sufficiency": { "puzzle_stated_explicitly": "boolean", "common_ground_established": "boolean", "departure_point_clear": "boolean", "audience_implied": "boolean", "transition_chain_continuous": "boolean" },
    "stakes_stress_test": { "generic_gap_language": "boolean", "specific_consequence_stated": "boolean", "target_audience_named": "boolean", "one_sentence_test": "boolean" },
    "prose_craft": {
      "human_face": { "hook_has_actor": "boolean", "actor_name": "string", "consensus_has_authors": "boolean", "anomaly_has_case": "boolean" },
      "showing_vs_telling": { "construct_illustration_paired": "boolean", "gap_has_consequence_scene": "boolean", "theory_consequence_specific": "boolean", "mechanism_operationalized": "boolean" },
      "conversational_voice": { "no_passive_in_key_modules": "boolean", "contribution_active_voice": "boolean", "no_inflated_symbolism": "boolean" }
    },
    "contradictions_or_gaps": ["string"],
    "information_poverty_dimensions": ["string"]
  },
  "phase_2_distillation": {
    "hook": {
      "persuasive_action": "string",
      "expression_skeletons": [{ "skeleton": "string", "transferability": "string", "paradigm_exclusivity": "string", "gap_variants": ["string"], "dorobantu_question": "string", "corpus_path": "string" }],
      "rhetorical_logic": { "audience_alignment": "string", "puzzle_gap_rq_layering": "string", "contribution_contract": "string" }
    }
  },
  "phase_3": {
    "module_density": "number",
    "hook_to_puzzle_distance": "number",
    "few_studies_density": "number",
    "tension_depth": "number",
    "stakes_specificity": "string",
    "transition_chain_completeness": "number",
    "theory_lens_responsiveness": "string",
    "makadok_visibility": "number",
    "jtbd_coverage": "number",
    "contribution_discussability": "string",
    "story_architecture": {
      "central_knot_clarity": "string",
      "protagonist_concentration": "number",
      "characters_order": "string",
      "narrative_arc_consistency": "string",
      "daviss_index_match": "number",
      "front_end_consistent": "boolean",
      "fat_suit_index": { "p1_words": "number", "first_three_paragraphs_words": "number", "background_ratio": "string" },
      "burying_the_lead_score": "string",
      "sentence_stuffing_index": "string"
    },
    "prose_craft": {
      "human_face_coverage": "string",
      "showing_ratio": "string",
      "passive_voice_density": "number",
      "inflated_symbolism_count": "number",
      "read_aloud_naturalness": "string"
    }
  },
  "phase_4_corpus_reference": {
    "vault_enrichment": {
      "new_skeletons_for_reference": [{ "module": "string", "gap_type": "string", "skeleton": "string", "source_papers": ["string"], "vault_path": "string", "note": "string" }],
      "patterns_to_note": [{ "module": "string", "gap_type": "string", "observation": "string", "note": "string" }],
      "new_anti_patterns": [{ "pattern": "string", "evidence": "string" }],
      "new_honesty_boundaries": [{ "boundary": "string", "source": "string" }]
    },
    "batch_metadata": {
      "total_papers_processed": "number",
      "combo_distribution": "object",
      "novel_skeletons_found": "number",
      "rejected_skeletons": "number",
      "rejected_reasons": ["string"]
    }
  },
  "skill_design_feedback": {
    "batch_id": "string",
    "last_updated": "YYYY-MM-DD",
    "observations": [
      {
        "defect_id": "string",
        "classification": "corpus_gap / routing_defect / validator_defect / output_contract_defect / schema_defect / stage_gate_defect",
        "current_rule": "string",
        "rule_excerpt": "string",
        "rule_locator": "string",
        "target": "string",
        "diagnosis": "string",
        "absolute_rule": "boolean",
        "decisive_falsifier": "boolean",
        "risk": "low / medium / high",
        "evidence": {
          "papers": [
            {"id": "string", "journal": "string", "evidence_anchor": "string", "evidence_quality": "full_text_verified / functional_summary / metadata_only"}
          ]
        },
        "proposed_change": {"action": "string", "summary": "string"},
        "regression_cases": {
          "positive": {"prompt": "string", "expected_invariants": ["string"]},
          "preservation": {"prompt": "string", "expected_invariants": ["string"]}
        },
        "resolution": null
      }
    ]
  },
  "phase_2_4_skeleton_critic": {
    "skeleton_id": "string",
    "verdict": "VALIDATED / REVISE / REJECT",
    "verdict_reason": "string",
    "generativity_test": { "mock_paragraph_generated": "boolean", "persuasive_action_preserved": "boolean", "notes": "string" },
    "fact_boundary_test": { "paper_specific_contamination": ["string"], "contamination_cleared": "boolean" },
    "type_fidelity_test": { "gap_type_match": "boolean", "mismatch_details": "string" }
  },
  "narrative_style_profile": {
    "tone": "string",
    "tone_evidence": "string",
    "paragraph_rhythm": "string",
    "module_ratio": { "hook": "number", "literature_turn": "number", "tension": "number", "stakes": "number", "theory_lens": "number", "preview": "number", "contribution": "number" },
    "distinctive_features": [{ "feature": "string", "example": "string" }],
    "avoids": [{ "avoid": "string", "function": "string" }],
    "quality_markers": { "what_makes_effective": "string", "strongest_aspect": "string", "weakest_aspect": "string" },
    "prose_craft_profile": {
      "human_face_strategy": "string",
      "showing_strategy": "string",
      "voice_strategy": "string",
      "fat_suit_control": "string",
      "burying_the_lead_control": "string",
      "sentence_stuffing_control": "string"
    }
  },
  "narrative_risk_ledger": [
    { "risk_id": "string", "discovery_phase": "string", "risk_type": "string", "original_manifestation": "string", "mimicry_consequence": "string", "recommended_handling": "string" }
  ],
  "phase_5_qc": {
    "completeness": "boolean",
    "clarity": "boolean",
    "credibility": "boolean",
    "replicability": "boolean",
    "no_verbatim_copy": "boolean",
    "fact_boundary": "boolean",
    "gap_type_fidelity": "boolean",
    "dorobantu_coverage": "boolean",
    "combo_honesty": "boolean",
    "overall_status": "PASS / FLAG / REJECT"
  },
  "phase_6_validation": {
    "validation_mode": "product_validation",
    "reference_metadata": { "description": "段落功能地图（来自 write-introduction 输出）" },
    "assembly_fidelity": {
      "module_coverage_rate": "number",
      "mandatory_pairings_satisfied": ["string"],
      "mandatory_pairings_broken": ["string"],
      "mutual_exclusion_violations": ["string"],
      "paragraph_count_deviation": "number",
      "deviation_matrix": [
        { "paragraph": "string", "recommended_module": "string", "actual_content": "string", "deviation_type": "module_replacement / module_missing / module_added / fidelity_ok", "severity": "high / medium / low" }
      ]
    },
    "promise_fulfillment": {
      "hook_to_puzzle": { "score": "number", "max": 3, "note": "string" },
      "gap_to_stakes": { "score": "number", "max": 3, "note": "string" },
      "theory_to_gap": { "score": "number", "max": 3, "note": "string" },
      "contribution_to_preview": { "score": "number", "max": 3, "note": "string" },
      "makadok_visibility": { "score": "number", "max": 3, "note": "string" },
      "four_questions": { "score": "number", "max": 4, "note": "string" },
      "overall_fulfillment_rate": "string"
    },
    "narrative_flow": {
      "transition_chain_score": "number",
      "transition_chain_max": 6,
      "weak_transitions": [{ "from": "string", "to": "string", "issue": "string" }]
    },
    "skeleton_generativity": {
      "validated_count": "number",
      "revise_count": "number",
      "reject_count": "number",
      "per_skeleton_assessment": [
        { "paragraph": "string", "module": "string", "key_phrases_preserved": "boolean", "persuasive_action_preserved": "boolean", "overfilling_risk": "low / medium / high", "verdict": "VALIDATED / REVISE / REJECT", "note": "string" }
      ]
    },
    "prose_craft_qc": {
      "total_checks": "number",
      "passed": "number",
      "failed": "number",
      "high_severity_failures": [
        { "check": "string", "location": "string", "issue": "string", "suggestion": "string" }
      ],
      "fat_suit_index": { "p1_words": "number", "first_three_paragraphs_words": "number", "background_ratio": "string" },
      "burying_the_lead_score": "string",
      "sentence_stuffing_count": "number"
    },
    "overall_rating": "ACCEPT / CONDITIONALLY_ACCEPT / NEEDS_REVISION / REJECT",
    "priority_fixes": [
      { "priority": "high / medium / low", "issue": "string", "current_state": "string", "recommendation": "string", "consequence_if_ignored": "string" }
    ],
    "post_validation_action": "direct_finalize / revise_and_revalidate / regenerate_assembly"
  }
}
```

---
*基于 Pollock 2025 Ch05、Dorobantu et al. (2024)、Simsek & Li (2022) JTBD 框架、MVP30 范文语料库构建。版本 2.2.0 — Introduction 蒸馏 Meta-Skill。*
