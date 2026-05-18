#!/usr/bin/env python3
"""
Map InputAbstract design type to relevant template variants from TemplateLibrary.
"""

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from parsers.json_abstraction import InputAbstract
from parsers.skill_parser import TemplateLibrary, TemplateVariant


@dataclass
class SlotSelection:
    slot_id: str
    generic_used: bool = True
    variant_names: List[str] = field(default_factory=list)
    composition_rules: List[str] = field(default_factory=list)
    selected_variants: List[TemplateVariant] = field(default_factory=list)
    rationale: str = ""


@dataclass
class TemplateSelection:
    methods_selections: Dict[str, SlotSelection] = field(default_factory=dict)
    results_selections: Dict[str, SlotSelection] = field(default_factory=dict)


def _load_design_type_map(config_path: Path) -> Dict:
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def _match_design_type(design_type: str, mapping: Dict) -> List[str]:
    """Find skill design types that match the distillation design_type."""
    design_type = design_type.lower().strip()
    dist_map = mapping.get("distillation_to_skill", {})

    # Exact match first
    if design_type in dist_map:
        return dist_map[design_type]

    # Partial match
    for key, values in dist_map.items():
        if key in design_type or design_type in key:
            return values

    # Token match
    tokens = set(design_type.replace("+", " ").replace("/", " ").split())
    best_match = []
    best_score = 0
    for key, values in dist_map.items():
        key_tokens = set(key.replace("+", " ").replace("/", " ").split())
        score = len(tokens & key_tokens)
        if score > best_score:
            best_score = score
            best_match = values

    return best_match if best_match else ["通用"]


def _find_variant_by_keywords(slot, keywords: List[str]) -> List[TemplateVariant]:
    """Find variants in a slot whose names contain any of the keywords."""
    found = []
    for keyword in keywords:
        for v in slot.variants:
            if keyword.lower() in v.name.lower() and v not in found:
                found.append(v)
    return found


def select_templates(
    abstract: InputAbstract,
    methods_lib: TemplateLibrary,
    results_lib: TemplateLibrary,
    config_path: Path = Path(__file__).parent.parent / "config" / "design_type_map.json",
) -> TemplateSelection:
    """
    Given an InputAbstract and parsed SKILL libraries, select the appropriate
    template variants for each slot.
    """
    mapping = _load_design_type_map(config_path)
    skill_design_types = _match_design_type(abstract.design_type, mapping)
    special_map = mapping.get("special_marker_to_variant", {})
    combo_rules = mapping.get("slot_composition_rules", {})

    selection = TemplateSelection()

    # --- METHODS SLOT SELECTION ---
    methods_slots = ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10"]

    for slot_id in methods_slots:
        slot = methods_lib.get_slot(slot_id)
        if not slot:
            continue

        sel = SlotSelection(slot_id=slot_id)

        # M1: Setting variants
        if slot_id == "M1":
            if abstract.design_family in ["DiD", "自然实验/DiD"]:
                sel.selected_variants = _find_variant_by_keywords(slot, ["自然实验/DiD", "DiD"])
            elif abstract.design_family in ["实验"]:
                sel.selected_variants = _find_variant_by_keywords(slot, ["实验"])
            elif abstract.multi_study:
                sel.selected_variants = _find_variant_by_keywords(slot, ["多研究"])
            elif abstract.design_family in ["SEM", "同时方程"]:
                sel.selected_variants = _find_variant_by_keywords(slot, ["同时方程", "SEM"])
            else:
                sel.selected_variants = []  # Use generic

        # M2: Sample funnel
        elif slot_id == "M2":
            if abstract.design_family in ["匹配DiD", "匹配DiD/广义DiD"]:
                sel.selected_variants = _find_variant_by_keywords(slot, ["PSM匹配面板"])
            elif abstract.multi_study:
                sel.selected_variants = _find_variant_by_keywords(slot, ["多研究"])
            else:
                sel.selected_variants = []

        # M3: DV
        elif slot_id == "M3":
            if "event_study" in abstract.special_markers or "event study" in abstract.model_spec.estimator.lower():
                sel.selected_variants = _find_variant_by_keywords(slot, ["事件研究"])
            elif abstract.design_family in ["文本构念测量"]:
                sel.selected_variants = _find_variant_by_keywords(slot, ["文本构念测量"])
            elif "推断二元结果" in abstract.design_type:
                sel.selected_variants = _find_variant_by_keywords(slot, ["推断二元结果"])
            else:
                sel.selected_variants = []

        # M4: Predictors
        elif slot_id == "M4":
            if abstract.design_family in ["DiD", "自然实验/DiD"]:
                sel.selected_variants = _find_variant_by_keywords(slot, ["自然实验/处理变量", "处理变量"])
            elif abstract.design_family in ["同伴效应/网络效应", "网络"]:
                sel.selected_variants = _find_variant_by_keywords(slot, ["同伴效应/网络效应", "网络"])
            elif abstract.design_family in ["SEM", "同时方程"]:
                sel.selected_variants = _find_variant_by_keywords(slot, ["同时方程"])
            else:
                sel.selected_variants = []

            # Add competing mechanism predictor if applicable
            if "mechanism" in abstract.special_markers or any("mechanism" in v.construct.lower() for v in abstract.moderators):
                mech_variants = _find_variant_by_keywords(slot, ["竞争机制预测变量"])
                sel.selected_variants.extend(mech_variants)

        # M5: Moderators
        elif slot_id == "M5":
            hypothesis_structure = abstract.raw_results.get("phase_0", {}).get("hypothesis_structure", "")
            has_indirect_moderation = "indirect moderation" in hypothesis_structure.lower() or "mediated moderation" in hypothesis_structure.lower()

            # Check for split-sample indicators in M5 original content
            m5_phase2 = abstract.raw_methods.get("phase_2_distillation", {})
            m5_content = ""
            for key, val in m5_phase2.items():
                if "m5" in key.lower():
                    if isinstance(val, dict):
                        skeletons = val.get("expression_skeletons", [])
                        m5_content += " ".join([s.get("skeleton", "") for s in skeletons if isinstance(s, dict)])

            has_split_sample = (
                "split" in hypothesis_structure.lower()
                or "sample_split" in abstract.special_markers
                or "split the sample" in m5_content.lower()
                or "subsample" in m5_content.lower()
                or "high vs low" in m5_content.lower()
                or "high and low" in m5_content.lower()
            )

            if has_indirect_moderation:
                sel.selected_variants = _find_variant_by_keywords(slot, ["间接调节", "mediated moderation"])
            elif has_split_sample:
                sel.selected_variants = _find_variant_by_keywords(slot, ["子样本分割"])
            elif abstract.design_family in ["实验"]:
                sel.selected_variants = _find_variant_by_keywords(slot, ["实验"])
            else:
                sel.selected_variants = []

        # M6: Controls
        elif slot_id == "M6":
            if abstract.design_family in ["DiD", "自然实验/DiD"]:
                sel.selected_variants = _find_variant_by_keywords(slot, ["自然实验/Bad Control", "Bad Control"])
            elif abstract.design_family in ["SEM", "同时方程"]:
                sel.selected_variants = _find_variant_by_keywords(slot, ["同时方程/方程特定控制"])
            elif abstract.design_family in ["实验"]:
                sel.selected_variants = _find_variant_by_keywords(slot, ["实验"])
            else:
                sel.selected_variants = []

        # M7: Model spec (most complex)
        elif slot_id == "M7":
            variants = []

            # Base estimator variant
            if abstract.design_family in ["生存分析"]:
                if "recurrent_event" in abstract.special_markers:
                    variants.extend(_find_variant_by_keywords(slot, ["复发事件 AFT"]))
                else:
                    variants.extend(_find_variant_by_keywords(slot, ["生存分析"]))
            elif abstract.design_family in ["面板数据/OLS", "OLS/FE"]:
                variants.extend(_find_variant_by_keywords(slot, ["通用"]))
            elif abstract.design_family in ["DiD", "自然实验/DiD"]:
                variants.extend(_find_variant_by_keywords(slot, ["DiD"]))
                # Add equation numbering for DiD
                variants.extend(_find_variant_by_keywords(slot, ["DiD 方程编号"]))
            elif abstract.design_family in ["IV/2SLS"]:
                if "lpm_2sls" in abstract.special_markers:
                    variants.extend(_find_variant_by_keywords(slot, ["线性概率模型（LPM）+ 2SLS"]))
                else:
                    variants.extend(_find_variant_by_keywords(slot, ["IV/2SLS"]))
            elif abstract.design_family in ["非线性模型"]:
                variants.extend(_find_variant_by_keywords(slot, ["非线性模型"]))
            elif abstract.design_family in ["匹配DiD", "匹配DiD/广义DiD"]:
                variants.extend(_find_variant_by_keywords(slot, ["匹配DiD/广义DiD"]))
            elif abstract.design_family in ["动态面板/GMM"]:
                variants.extend(_find_variant_by_keywords(slot, ["动态面板/GMM"]))
            elif abstract.design_family in ["堆叠扩散Logit"]:
                variants.extend(_find_variant_by_keywords(slot, ["堆叠扩散Logit"]))
            elif abstract.design_family in ["实验"]:
                variants.extend(_find_variant_by_keywords(slot, ["实验"]))
            else:
                variants.extend(_find_variant_by_keywords(slot, ["通用"]))

            # Combo designs (Tobit/Poisson + IV)
            if "iv" in abstract.design_type.lower() and any(x in abstract.design_type.lower() for x in ["tobit", "poisson", "logit", "probit"]):
                variants.extend(_find_variant_by_keywords(slot, ["组合设计注释"]))

            # Event study GLM for CAR
            if "event_study_car" in abstract.special_markers:
                variants.extend(_find_variant_by_keywords(slot, ["事件研究 GLM", "GLM 变体"]))

            # Add diagnostics if applicable
            if abstract.model_spec.diagnostics:
                diag_variants = _find_variant_by_keywords(slot, ["诊断检验补充"])
                variants.extend(diag_variants)

            sel.selected_variants = variants

        # M8: Identification
        elif slot_id == "M8":
            variants = []
            if abstract.design_family in ["DiD", "自然实验/DiD"]:
                variants.extend(_find_variant_by_keywords(slot, ["自然实验/DiD"]))
                # Permutation test preview
                variants.extend(_find_variant_by_keywords(slot, ["置换检验预览", "DiD 置换"]))
            elif abstract.design_family in ["IV/2SLS"]:
                variants.extend(_find_variant_by_keywords(slot, ["IV 排他性约束"]))
            elif abstract.design_family in ["匹配DiD", "匹配DiD/广义DiD"]:
                variants.extend(_find_variant_by_keywords(slot, ["匹配DiD 平行趋势"]))
            elif abstract.design_family in ["同伴效应/网络效应", "网络"]:
                variants.extend(_find_variant_by_keywords(slot, ["同伴效应/网络效应 falsification", "falsification"]))
                # Formal identification proof for network effects
                variants.extend(_find_variant_by_keywords(slot, ["形式化识别证明", "部分重叠同伴群体"]))
            elif abstract.design_family in ["实验"]:
                variants.extend(_find_variant_by_keywords(slot, ["实验效度"]))

            # Special variants
            if "cem_matching" in abstract.special_markers:
                variants.extend(_find_variant_by_keywords(slot, ["粗化精确匹配", "CEM"]))
            if "regime_falsification" in abstract.special_markers:
                variants.extend(_find_variant_by_keywords(slot, ["制度/政策体制安慰剂"]))

            sel.selected_variants = variants

        # M9: Multi-study
        elif slot_id == "M9":
            if abstract.multi_study:
                sel.selected_variants = _find_variant_by_keywords(slot, ["多研究"])
            else:
                sel.generic_used = False

        # M10: Transition
        elif slot_id == "M10":
            sel.selected_variants = []  # Optional, usually generic

        sel.variant_names = [v.name for v in sel.selected_variants]
        if not sel.selected_variants:
            sel.rationale = "Using generic template"
        else:
            sel.rationale = f"Matched design type: {abstract.design_type}"

        selection.methods_selections[slot_id] = sel

    # --- RESULTS SLOT SELECTION ---
    results_slots = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9"]

    for slot_id in results_slots:
        slot = results_lib.get_slot(slot_id)
        if not slot:
            continue

        sel = SlotSelection(slot_id=slot_id)

        if slot_id == "R1":
            if abstract.multi_study:
                sel.selected_variants = _find_variant_by_keywords(slot, ["多研究"])
            else:
                sel.selected_variants = []

        elif slot_id == "R2":
            if abstract.design_family in ["DiD", "自然实验/DiD"]:
                sel.selected_variants = _find_variant_by_keywords(slot, ["DiD"])
            elif abstract.design_family in ["IV/2SLS"]:
                # Check if footnote-light or Panel A/B
                if abstract.model_spec.first_stage_f:
                    sel.selected_variants = _find_variant_by_keywords(slot, ["IV/2SLS 脚注精简", "脚注"])
                else:
                    sel.selected_variants = _find_variant_by_keywords(slot, ["IV/2SLS"])
            elif abstract.design_family in ["匹配DiD", "匹配DiD/广义DiD"]:
                sel.selected_variants = _find_variant_by_keywords(slot, ["匹配DiD"])
            elif abstract.multi_study:
                sel.selected_variants = _find_variant_by_keywords(slot, ["多研究"])
            else:
                sel.selected_variants = []

            # Dual estimator navigation
            if "+" in abstract.model_spec.estimator or "event_study" in abstract.special_markers:
                sel.selected_variants.extend(_find_variant_by_keywords(slot, ["双重估计量"]))

        elif slot_id == "R3":
            variants = []
            if abstract.design_family in ["生存分析"]:
                variants.extend(_find_variant_by_keywords(slot, ["生存分析"]))
            elif abstract.design_family in ["DiD", "自然实验/DiD"]:
                variants.extend(_find_variant_by_keywords(slot, ["DiD"]))
            elif abstract.design_family in ["计数模型"]:
                variants.extend(_find_variant_by_keywords(slot, ["计数模型"]))
            elif abstract.design_family in ["实验"]:
                variants.extend(_find_variant_by_keywords(slot, ["实验"]))
            elif abstract.design_family in ["Logit/Probit/Ordered Probit", "非线性模型"]:
                if "ordered" in abstract.design_type.lower():
                    variants.extend(_find_variant_by_keywords(slot, ["有序 Probit"]))
                else:
                    variants.extend(_find_variant_by_keywords(slot, ["Logit/Probit"]))
            elif abstract.design_family in ["IV/2SLS"]:
                variants.extend(_find_variant_by_keywords(slot, ["IV/2SLS 第二阶段"]))
            elif abstract.design_family in ["推断二元结果"]:
                variants.extend(_find_variant_by_keywords(slot, ["推断二元结果"]))
            else:
                variants.extend(_find_variant_by_keywords(slot, ["OLS/FE", "通用"]))

            # Special variants
            if "u_shaped" in abstract.special_markers:
                variants.extend(_find_variant_by_keywords(slot, ["U-shaped", "倒U型"]))
            if "event_study_car" in abstract.special_markers:
                variants.extend(_find_variant_by_keywords(slot, ["GLM / 事件研究 CAR"]))
            if any(not h.predicted_support for h in abstract.hypotheses):
                variants.extend(_find_variant_by_keywords(slot, ["非显著"]))
            # Prediction/RQ style
            if any("prediction" in h.text.lower() or "research question" in h.text.lower() for h in abstract.hypotheses):
                variants.extend(_find_variant_by_keywords(slot, ["Prediction", "Proposition", "Research Question"]))

            sel.selected_variants = variants

        elif slot_id == "R4":
            hypothesis_structure = abstract.raw_results.get("phase_0", {}).get("hypothesis_structure", "")
            has_interaction_in_hypotheses = any("interaction" in h.text.lower() or "×" in h.text for h in abstract.hypotheses)
            has_interaction_in_moderators = any("×" in m.name or " x " in m.name.lower() or "interaction" in m.name.lower() for m in abstract.moderators)
            # Also detect interaction from IV names (M4 predictors) and hypothesis structure
            has_interaction_in_ivs = any("×" in v.name or " x " in v.name.lower() or "interaction" in v.name.lower() for v in abstract.independent_variables)
            has_interaction_in_structure = "interaction" in hypothesis_structure.lower()
            has_split_sample = "split" in hypothesis_structure.lower() or "sample_split" in abstract.special_markers

            if has_interaction_in_hypotheses or has_interaction_in_moderators or has_interaction_in_ivs or has_interaction_in_structure or has_split_sample or "conjoint_experiment" in abstract.special_markers:
                variants = []
                if "three_way_interaction" in abstract.special_markers:
                    variants.extend(_find_variant_by_keywords(slot, ["三向交互"]))
                elif has_split_sample:
                    variants.extend(_find_variant_by_keywords(slot, ["子样本交互", "子样本"]))
                elif abstract.design_family in ["DiD", "自然实验/DiD"]:
                    variants.extend(_find_variant_by_keywords(slot, ["DiD 调节"]))
                elif abstract.design_family in ["IV/2SLS"] and (has_interaction_in_ivs or has_interaction_in_structure):
                    variants.extend(_find_variant_by_keywords(slot, ["IV/2SLS 交互", "IV 交互"]))
                else:
                    # Find generic interaction variants; exclude design-specific ones
                    interaction_variants = _find_variant_by_keywords(slot, ["交互"])
                    excluded = ["三向交互", "非线性交互", "子样本交互", "IV/2SLS 交互", "构造暴露分解"]
                    interaction_variants = [
                        v for v in interaction_variants
                        if not any(ex in v.name for ex in excluded)
                    ]
                    variants.extend(interaction_variants)
                # Add nonlinear interaction only if not using split-sample or IV-specific variants
                if not has_split_sample and abstract.design_family not in ["IV/2SLS"]:
                    if abstract.design_family in ["计数模型", "Logit/Probit/Ordered Probit", "非线性模型"]:
                        variants.extend(_find_variant_by_keywords(slot, ["非线性交互"]))
                sel.selected_variants = variants
            # else: leave generic_used=True so gap analyzer does not flag generic R4 as missing

        elif slot_id == "R5":
            if "u_shaped" in abstract.special_markers:
                sel.selected_variants = _find_variant_by_keywords(slot, ["转折点", "最优水平"])
            elif "event_study_car" in abstract.special_markers or "quartile" in str(abstract.raw_results).lower():
                sel.selected_variants = _find_variant_by_keywords(slot, ["分位数"])
            else:
                sel.selected_variants = _find_variant_by_keywords(slot, ["通用"])

        elif slot_id == "R6":
            hypothesis_structure = abstract.raw_results.get("phase_0", {}).get("hypothesis_structure", "")
            has_indirect_moderation = "indirect moderation" in hypothesis_structure.lower() or "mediated moderation" in hypothesis_structure.lower()
            if abstract.nonsignificant_findings:
                if has_indirect_moderation:
                    sel.selected_variants = _find_variant_by_keywords(slot, ["非显著间接调节", "间接调节"])
                else:
                    sel.selected_variants = _find_variant_by_keywords(slot, ["通用"])
            # else: leave generic_used=True so gap analyzer does not flag generic R6 as missing

        elif slot_id == "R7":
            variants = []
            # Base threats
            variants.extend(_find_variant_by_keywords(slot, ["测量威胁", "模型威胁", "样本威胁", "时点威胁", "内生性威胁", "机制/边界威胁"]))

            # Design-specific
            if abstract.design_family in ["DiD", "自然实验/DiD"]:
                variants.extend(_find_variant_by_keywords(slot, ["DiD 平行趋势", "DiD 置换检验"]))
                if "spatial_placebo" in abstract.special_markers:
                    variants.extend(_find_variant_by_keywords(slot, ["空间安慰剂"]))
            elif abstract.design_family in ["IV/2SLS"]:
                variants.extend(_find_variant_by_keywords(slot, ["IV 有效性"]))
            elif abstract.design_family in ["匹配DiD", "匹配DiD/广义DiD"]:
                variants.extend(_find_variant_by_keywords(slot, ["匹配DiD 重叠支撑"]))
            elif abstract.design_family in ["同伴效应/网络效应", "网络"]:
                variants.extend(_find_variant_by_keywords(slot, ["同伴效应/网络效应 falsification"]))

            # Event study robustness
            if "event_study_car" in abstract.special_markers:
                variants.extend(_find_variant_by_keywords(slot, ["事件研究稳健性"]))
            # Leader FE robustness
            if "leader_fe" in abstract.special_markers:
                variants.extend(_find_variant_by_keywords(slot, ["市场地位/主导企业"]))

            sel.selected_variants = variants

        elif slot_id == "R8":
            variants = []
            if "mcmc_mediation" in abstract.special_markers:
                variants.extend(_find_variant_by_keywords(slot, ["MCMC / 模拟中介"]))
            if "assumption_verification" in abstract.special_markers:
                variants.extend(_find_variant_by_keywords(slot, ["假设验证", "Corroborating Evidence"]))
            # Generic mechanism/exploratory
            variants.extend(_find_variant_by_keywords(slot, ["通用", "机制检验专用", "替代机制排除"]))
            sel.selected_variants = variants

        elif slot_id == "R9":
            if abstract.multi_study:
                sel.selected_variants = _find_variant_by_keywords(slot, ["多研究"])
            else:
                sel.selected_variants = []

        sel.variant_names = [v.name for v in sel.selected_variants]
        if not sel.selected_variants:
            sel.rationale = "Using generic template" if sel.generic_used else "Slot not applicable"
        else:
            sel.rationale = f"Matched design type: {abstract.design_type}"

        selection.results_selections[slot_id] = sel

    return selection
