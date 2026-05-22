#!/usr/bin/env python3
"""
validate_bindings.py

自动化检查骨架-微模板映射表的完整性、正确性和一致性。

检查项：
1. YAML 结构合法性（slot / syntax_positions / bindings / entries）
2. 微模板文件存在性（micro-templates/ 目录下）
3. 章节标题存在性（对应 .md 文件中的 Markdown 标题）
4. tier 字段合法性（core / extended / full）
5. design_type_filter 中的设计类型是否存在于语料库分片索引
6. 全局约束数值合理性

用法：
    python validate_bindings.py
    python validate_bindings.py --quiet        # 仅输出最终结果
    python validate_bindings.py --json         # 输出 JSON 格式报告
"""

import sys
import json
import argparse
from pathlib import Path
from typing import List, Dict, Any, Tuple

# ---------------------------------------------------------------------------
# Paths (relative to this script)
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent.resolve()
BINDINGS_FILE = SCRIPT_DIR / "_slot_micro_template_bindings.yaml"
MICRO_TEMPLATE_DIR = SCRIPT_DIR / "micro-templates"
CORPUS_DIR = SCRIPT_DIR  # design-type shards live alongside bindings file

VALID_TIERS = {"core", "extended", "full"}
REQUIRED_SLOT_KEYS = {"description", "persuasive_action", "syntax_positions"}
REQUIRED_POSITION_KEYS = {"required", "default_tier", "bindings"}
REQUIRED_BINDING_KEYS = {"file", "section", "entries"}
REQUIRED_ENTRY_KEYS = {"label", "template", "tier"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def load_yaml(path: Path) -> dict:
    try:
        import yaml
    except ImportError:
        print("ERROR: PyYAML is required. Install with: pip install pyyaml")
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def color(text: str, code: str) -> str:
    """Return ANSI-colored text if stdout is a tty."""
    if sys.stdout.isatty():
        return f"\033[{code}m{text}\033[0m"
    return text


def red(text: str) -> str:
    return color(text, "31")


def green(text: str) -> str:
    return color(text, "32")


def yellow(text: str) -> str:
    return color(text, "33")


def cyan(text: str) -> str:
    return color(text, "36")


def extract_headings(text: str) -> List[str]:
    """Extract all Markdown headings (# … ######) from text, skipping frontmatter."""
    lines = text.splitlines()
    in_frontmatter = False
    frontmatter_closed = False
    headings = []
    for line in lines:
        if line.strip() == "---" and not frontmatter_closed:
            if not in_frontmatter:
                in_frontmatter = True
                continue
            else:
                frontmatter_closed = True
                continue
        if not frontmatter_closed and in_frontmatter:
            continue
        stripped = line.strip()
        if stripped.startswith("#"):
            # Count leading #
            level = 0
            for ch in stripped:
                if ch == "#":
                    level += 1
                else:
                    break
            if 1 <= level <= 6:
                title = stripped[level:].strip()
                headings.append(title)
    return headings


def clean_heading(heading: str) -> str:
    """Strip leading numeric prefix like '1. ' from a heading for fuzzy matching."""
    import re
    return re.sub(r"^\d+\.\s*", "", heading).strip()


def find_file_case_insensitive(directory: Path, name: str) -> Path:
    """Look for a file case-insensitively within directory. Return path if found."""
    if not directory.exists():
        return directory / name
    for child in directory.iterdir():
        if child.name.lower() == name.lower():
            return child
    return directory / name


# ---------------------------------------------------------------------------
# Validators
# ---------------------------------------------------------------------------
class Validator:
    def __init__(self, data: dict, quiet: bool = False):
        self.data = data
        self.quiet = quiet
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.stats = {
            "slots": 0,
            "syntax_positions": 0,
            "bindings": 0,
            "entries": 0,
            "tier_counts": {"core": 0, "extended": 0, "full": 0},
            "files_referenced": set(),
            "sections_found": 0,
            "sections_missing": 0,
        }
        # Cache for design-type shard names
        self._design_types: set = set()
        self._headings_cache: Dict[str, List[str]] = {}

    def _log(self, msg: str):
        if not self.quiet:
            print(msg)

    def _err(self, msg: str):
        self.errors.append(msg)
        self._log(red(f"  [ERROR] {msg}"))

    def _warn(self, msg: str):
        self.warnings.append(msg)
        self._log(yellow(f"  [WARN]  {msg}"))

    def _ok(self, msg: str):
        self._log(green(f"  [OK]    {msg}"))

    # --- design type discovery ------------------------------------------------
    def _discover_design_types(self):
        """Gather valid design type names from corpus shard filenames."""
        self._design_types = set()
        if CORPUS_DIR.exists():
            for f in CORPUS_DIR.iterdir():
                if f.is_file() and f.suffix == ".md" and not f.name.startswith("_"):
                    self._design_types.add(f.stem)
        # Also try to read from INDEX.md table as fallback / cross-check
        index_file = CORPUS_DIR / "INDEX.md"
        if index_file.exists():
            text = index_file.read_text(encoding="utf-8")
            for line in text.splitlines():
                # Rough heuristic: lines in the index table contain a pipe and a .md link
                if "[" in line and "](" in line and ".md)" in line:
                    import re
                    m = re.search(r"\[([^\]]+)\]\([^)]*\.md\)", line)
                    if m:
                        self._design_types.add(m.group(1))

    # --- cache headings -------------------------------------------------------
    def _get_headings(self, rel_path: str) -> List[str]:
        if rel_path in self._headings_cache:
            return self._headings_cache[rel_path]
        file_path = find_file_case_insensitive(MICRO_TEMPLATE_DIR, rel_path)
        if not file_path.exists():
            self._headings_cache[rel_path] = []
            return []
        text = file_path.read_text(encoding="utf-8")
        headings = extract_headings(text)
        self._headings_cache[rel_path] = headings
        return headings

    # --- schema validation ----------------------------------------------------
    def validate_schema(self):
        self._log(cyan("\n[Step 1/5] Schema validation"))

        # Top-level keys
        expected_top = {"_meta", "load_tiers"} | {f"M{i}" for i in range(1, 11)} | {"global_constraints"}
        actual_top = set(self.data.keys())
        missing_top = expected_top - actual_top
        extra_top = actual_top - expected_top
        if missing_top:
            self._err(f"Missing top-level keys: {sorted(missing_top)}")
        if extra_top:
            self._warn(f"Unexpected top-level keys: {sorted(extra_top)}")
        if not missing_top and not extra_top:
            self._ok("Top-level keys complete")

        # _meta
        meta = self.data.get("_meta", {})
        for k in ("name", "version", "created", "updated"):
            if k not in meta:
                self._warn(f"_meta missing field: {k}")

        # load_tiers
        tiers = self.data.get("load_tiers", {})
        for tier_name in VALID_TIERS:
            if tier_name not in tiers:
                self._err(f"load_tiers missing definition for '{tier_name}'")
            else:
                tdef = tiers[tier_name]
                for k in ("criteria", "max_templates_per_position"):
                    if k not in tdef:
                        self._err(f"load_tiers.{tier_name} missing '{k}'")

        # global_constraints
        gc = self.data.get("global_constraints", {})
        for k in ("max_micro_templates_per_slot", "max_micro_template_files_per_call", "default_tier", "design_type_override"):
            if k not in gc:
                self._err(f"global_constraints missing '{k}'")
        if gc.get("default_tier") not in VALID_TIERS:
            self._err(f"global_constraints.default_tier='{gc.get('default_tier')}' is not a valid tier")
        if not isinstance(gc.get("design_type_override"), bool):
            self._err("global_constraints.design_type_override must be a boolean")
        if not missing_top:
            self._ok("Schema structure looks valid")

    # --- slot-level validation ------------------------------------------------
    def validate_slots(self):
        self._log(cyan("\n[Step 2/5] Slot & syntax position validation"))
        for slot_name in [f"M{i}" for i in range(1, 11)]:
            slot = self.data.get(slot_name)
            if not slot:
                self._err(f"Slot {slot_name} is missing or empty")
                continue
            missing = REQUIRED_SLOT_KEYS - set(slot.keys())
            if missing:
                self._err(f"Slot {slot_name} missing keys: {missing}")
                continue
            self.stats["slots"] += 1
            positions = slot.get("syntax_positions", {})
            for pos_name, pos_def in positions.items():
                self.stats["syntax_positions"] += 1
                p_missing = REQUIRED_POSITION_KEYS - set(pos_def.keys())
                if p_missing:
                    self._err(f"Slot {slot_name} / position '{pos_name}' missing keys: {p_missing}")
                    continue
                if not isinstance(pos_def["required"], bool):
                    self._err(f"Slot {slot_name} / '{pos_name}': required must be boolean")
                if pos_def["default_tier"] not in VALID_TIERS:
                    self._err(f"Slot {slot_name} / '{pos_name}': default_tier '{pos_def['default_tier']}' invalid")
                bindings = pos_def.get("bindings", [])
                if not isinstance(bindings, list):
                    self._err(f"Slot {slot_name} / '{pos_name}': bindings must be a list")
                    continue
                for bidx, binding in enumerate(bindings):
                    self.validate_binding(slot_name, pos_name, bidx, binding)
        self._ok(f"Checked {self.stats['slots']} slots, {self.stats['syntax_positions']} positions")

    def validate_binding(self, slot: str, position: str, bidx: int, binding: dict):
        b_missing = REQUIRED_BINDING_KEYS - set(binding.keys())
        if b_missing:
            self._err(f"Slot {slot} / {position} / binding[{bidx}] missing keys: {b_missing}")
            return

        rel_file = binding["file"]
        section = binding["section"]
        self.stats["files_referenced"].add(rel_file)

        # File existence
        file_path = find_file_case_insensitive(MICRO_TEMPLATE_DIR, rel_file)
        if not file_path.exists():
            self._err(f"Slot {slot} / {position}: micro-template file not found: '{rel_file}'")
            return

        # Section existence (heading match)
        headings = self._get_headings(rel_file)
        if section not in headings:
            # Try fuzzy match: strip trailing colons/spaces AND leading numeric prefixes
            normalized_headings = {h.strip().rstrip(":"): h for h in headings}
            cleaned_headings = {clean_heading(h): h for h in headings}
            cleaned_section = clean_heading(section.strip().rstrip(":"))
            if (section.strip().rstrip(":") not in normalized_headings and
                    cleaned_section not in cleaned_headings):
                self._err(f"Slot {slot} / {position}: section '{section}' not found in '{rel_file}'")
                self.stats["sections_missing"] += 1
                return
        self.stats["sections_found"] += 1

        # Entries
        entries = binding.get("entries", [])
        if not isinstance(entries, list):
            self._err(f"Slot {slot} / {position} / binding[{bidx}]: entries must be a list")
            return
        for eidx, entry in enumerate(entries):
            self.validate_entry(slot, position, bidx, eidx, entry)

    def validate_entry(self, slot: str, position: str, bidx: int, eidx: int, entry: dict):
        e_missing = REQUIRED_ENTRY_KEYS - set(entry.keys())
        if e_missing:
            self._err(f"Slot {slot} / {position} / entry[{eidx}] missing keys: {e_missing}")
            return
        self.stats["entries"] += 1

        tier = entry["tier"]
        if tier not in VALID_TIERS:
            self._err(f"Slot {slot} / {position} / entry[{eidx}]: invalid tier '{tier}'")
        else:
            self.stats["tier_counts"][tier] += 1

        # design_type_filter validation
        dtf = entry.get("design_type_filter")
        if dtf is not None:
            if not isinstance(dtf, list):
                self._err(f"Slot {slot} / {position} / entry[{eidx}]: design_type_filter must be a list")
                return
            for dt in dtf:
                if dt not in self._design_types:
                    self._warn(f"Slot {slot} / {position} / entry[{eidx}]: design_type_filter value '{dt}' not found in corpus shards")

    # --- cross-file consistency -----------------------------------------------
    def validate_cross_file(self):
        self._log(cyan("\n[Step 3/5] Cross-file consistency"))
        # Ensure all referenced micro-template files actually exist
        missing_files = []
        for rel_file in self.stats["files_referenced"]:
            fp = find_file_case_insensitive(MICRO_TEMPLATE_DIR, rel_file)
            if not fp.exists():
                missing_files.append(rel_file)
        if missing_files:
            for mf in missing_files:
                self._err(f"Referenced micro-template file missing: {mf}")
        else:
            self._ok(f"All {len(self.stats['files_referenced'])} referenced micro-template files exist")

        # Ensure default_tier in global_constraints matches VALID_TIERS
        gc = self.data.get("global_constraints", {})
        if gc.get("default_tier") in VALID_TIERS:
            self._ok(f"global_constraints.default_tier = '{gc['default_tier']}' is valid")

    # --- tier distribution ----------------------------------------------------
    def validate_tier_distribution(self):
        self._log(cyan("\n[Step 4/5] Tier distribution"))
        total = sum(self.stats["tier_counts"].values())
        if total == 0:
            self._err("No entries found — bindings file may be empty or malformed")
            return
        for tier, count in self.stats["tier_counts"].items():
            pct = count / total * 100
            marker = green(f"{pct:.1f}%") if tier == "core" else yellow(f"{pct:.1f}%")
            self._log(f"  {tier:10s}: {count:3d} entries ({marker})")
        core_pct = self.stats["tier_counts"]["core"] / total * 100
        if core_pct < 50:
            self._warn(f"Core ratio {core_pct:.1f}% is below the 50% target")
        else:
            self._ok(f"Core ratio {core_pct:.1f}% meets the >50% target")

    # --- core baseline freeze -------------------------------------------------
    def validate_core_baseline(self):
        self._log(cyan("\n[Step 5/6] Core baseline freeze check"))
        meta = self.data.get("_meta", {})
        baseline = meta.get("core_baseline")
        if not baseline:
            self._warn("No core_baseline defined in _meta — freeze rule not enforced")
            return
        frozen_count = baseline.get("count")
        frozen_at = baseline.get("frozen_at", "unknown")
        if frozen_count is None:
            self._warn("core_baseline.count missing — cannot verify freeze")
            return
        current_core = self.stats["tier_counts"].get("core", 0)
        if current_core == frozen_count:
            self._ok(f"Core pool frozen at {frozen_count} entries (since {frozen_at})")
        elif current_core > frozen_count:
            self._warn(
                f"Core pool expanded: {frozen_count} → {current_core} (+{current_core - frozen_count}). "
                f"New core entries require manual review per freeze rule ({frozen_at})."
            )
        else:
            self._warn(
                f"Core pool shrunk: {frozen_count} → {current_core} ({frozen_count - current_core} removed). "
                f"Verify removals are intentional."
            )

    # --- summary --------------------------------------------------------------
    def summary(self) -> dict:
        self._log(cyan("\n[Step 6/6] Summary"))
        result = {
            "status": "PASS" if not self.errors else "FAIL",
            "errors": len(self.errors),
            "warnings": len(self.warnings),
            "stats": {
                "slots": self.stats["slots"],
                "syntax_positions": self.stats["syntax_positions"],
                "bindings": self.stats["bindings"],
                "entries": self.stats["entries"],
                "files_referenced": len(self.stats["files_referenced"]),
                "sections_found": self.stats["sections_found"],
                "sections_missing": self.stats["sections_missing"],
                "tier_distribution": self.stats["tier_counts"],
            },
            "error_details": self.errors,
            "warning_details": self.warnings,
        }
        if self.errors:
            self._log(red(f"\nRESULT: FAIL — {len(self.errors)} error(s), {len(self.warnings)} warning(s)"))
        elif self.warnings:
            self._log(yellow(f"\nRESULT: PASS with {len(self.warnings)} warning(s)"))
        else:
            self._log(green("\nRESULT: PASS — all checks green"))
        return result

    def run(self) -> dict:
        if not BINDINGS_FILE.exists():
            print(red(f"FATAL: Bindings file not found: {BINDINGS_FILE}"))
            sys.exit(1)
        self._discover_design_types()
        self.data = load_yaml(BINDINGS_FILE)
        self.validate_schema()
        self.validate_slots()
        self.validate_cross_file()
        self.validate_tier_distribution()
        self.validate_core_baseline()
        return self.summary()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Validate slot-micro-template bindings")
    parser.add_argument("--quiet", action="store_true", help="Only print final result")
    parser.add_argument("--json", action="store_true", help="Output JSON report")
    args = parser.parse_args()

    if not BINDINGS_FILE.exists():
        print(red(f"FATAL: Bindings file not found: {BINDINGS_FILE}"))
        sys.exit(1)

    validator = Validator({}, quiet=args.quiet)
    result = validator.run()

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))

    sys.exit(0 if result["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
