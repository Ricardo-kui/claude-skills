from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent
MODULE_PATH = SKILL_ROOT / "scripts" / "select_r2_pilot.py"
SPEC = importlib.util.spec_from_file_location("select_r2_pilot", MODULE_PATH)
assert SPEC and SPEC.loader
selector = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = selector
SPEC.loader.exec_module(selector)


class R2PilotSelectorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.index = selector.load_yaml(selector.DEFAULT_INDEX)

    def ids(self, features: set[str], top_k: int | None = None) -> list[str]:
        return [asset["asset_id"] for asset in selector.select_assets(self.index, features, top_k)]

    def test_index_and_legacy_assets_are_intact(self) -> None:
        self.assertEqual(selector.validate_index(self.index), [])

    def test_standard_task_uses_only_robust_fallback(self) -> None:
        self.assertEqual(self.ids(set()), ["r2_ols_model_sequence"])

    def test_model_free_task_retrieves_specific_asset_then_fallback(self) -> None:
        self.assertEqual(
            self.ids({"model_free_evidence", "quartile_means"}),
            ["r2_ols_model_free_quartile_opening", "r2_ols_model_sequence"],
        )

    def test_heckman_task_retrieves_two_stage_navigation(self) -> None:
        self.assertEqual(
            self.ids({"heckman_selection", "separate_first_stage_table"}),
            ["r2_ols_heckman_two_stage_table_navigation", "r2_ols_model_sequence"],
        )

    def test_heckman_synonym_normalizes_to_canonical_feature(self) -> None:
        self.assertEqual(
            self.ids({"heckman_two_stage", "sample_selection"}),
            ["r2_ols_heckman_two_stage_table_navigation", "r2_ols_model_sequence"],
        )
        report = selector.selection_report(self.index, {"heckman_two_stage"})
        self.assertEqual(report["features"], ["heckman_selection"])

    def test_other_feature_aliases_retrieve_specialized_assets(self) -> None:
        cases = {
            "model_free_preview": "r2_ols_model_free_quartile_opening",
            "curvilinear_model": "r2_ols_polynomial_curve_moderation_sequence",
            "factorial_experiment": None,
        }
        for feature, expected in cases.items():
            with self.subTest(feature=feature):
                selected = self.ids({feature})
                if expected is None:
                    self.assertEqual(selected, ["r2_ols_model_sequence"])
                else:
                    self.assertEqual(selected[0], expected)

    def test_dual_correction_task_prefers_more_specific_asset(self) -> None:
        self.assertEqual(
            self.ids(
                {
                    "control_function",
                    "binary_endogenous_predictor",
                    "heckman_selection",
                    "sample_selection",
                }
            ),
            [
                "r2_ols_dual_endogeneity_selection_navigation",
                "r2_ols_heckman_two_stage_table_navigation",
                "r2_ols_model_sequence",
            ],
        )

    def test_polynomial_task_retrieves_curve_sequence(self) -> None:
        self.assertEqual(
            self.ids({"polynomial_model", "curve_moderation"}),
            ["r2_ols_polynomial_curve_moderation_sequence", "r2_ols_model_sequence"],
        )

    def test_experimental_three_way_task_retrieves_seven_model_asset(self) -> None:
        self.assertEqual(
            self.ids({"experimental_design", "three_way_interaction", "multiple_traits"}),
            ["r2_ols_experimental_seven_model_hierarchy", "r2_ols_model_sequence"],
        )

    def test_three_way_without_experimental_design_does_not_overtrigger(self) -> None:
        self.assertEqual(self.ids({"three_way_interaction"}), ["r2_ols_model_sequence"])

    def test_unknown_feature_fails_loudly_instead_of_masking_route_error(self) -> None:
        with self.assertRaises(selector.PilotIndexError):
            self.ids({"unsupported_feature"})

    def test_feature_names_normalize_case_hyphens_and_aliases(self) -> None:
        self.assertEqual(
            self.ids({"Heckman", "Sample-Selection"}),
            ["r2_ols_heckman_two_stage_table_navigation", "r2_ols_model_sequence"],
        )

    def test_feature_catalog_exposes_canonical_vocabulary(self) -> None:
        catalog = selector.feature_catalog(self.index)
        self.assertIn("heckman_selection", catalog["canonical_features"])
        self.assertEqual(catalog["aliases"]["heckman"], "heckman_selection")

    def test_top_k_is_respected(self) -> None:
        self.assertEqual(
            self.ids(
                {"control_function", "binary_endogenous_predictor", "heckman_selection"},
                top_k=1,
            ),
            ["r2_ols_dual_endogeneity_selection_navigation"],
        )

    def test_many_matching_features_cannot_displace_robust_fallback(self) -> None:
        selected = self.ids(
            {
                "model_free_evidence",
                "polynomial_model",
                "heckman_selection",
                "control_function",
                "binary_endogenous_predictor",
            }
        )
        self.assertEqual(len(selected), 3)
        self.assertEqual(selected[-1], "r2_ols_model_sequence")

    def test_rendered_heckman_context_includes_navigation_and_fact_boundaries(self) -> None:
        selected = selector.select_assets(self.index, {"heckman_selection"})
        contract = selector.render_contract(self.index, selected)
        self.assertIn("Map each hypothesis", contract)
        self.assertIn("alternative specification", contract)
        self.assertIn("Do not infer the baseline fixed-effects structure", contract)

    def test_targeted_context_is_at_least_50_percent_smaller(self) -> None:
        cases = [
            set(),
            {"model_free_evidence", "quartile_means"},
            {"heckman_selection", "separate_first_stage_table"},
            {"control_function", "binary_endogenous_predictor", "heckman_selection"},
            {"polynomial_model", "curve_moderation"},
            {"experimental_design", "three_way_interaction"},
        ]
        for features in cases:
            with self.subTest(features=features):
                report = selector.selection_report(self.index, features)
                self.assertGreaterEqual(report["context"]["character_reduction_ratio"], 0.5)


if __name__ == "__main__":
    unittest.main()
