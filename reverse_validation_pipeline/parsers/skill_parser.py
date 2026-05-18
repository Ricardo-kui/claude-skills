#!/usr/bin/env python3
"""
Parse write-methods/SKILL.md and write-results/SKILL.md into structured TemplateLibrary.
"""

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional


@dataclass
class TemplateVariant:
    name: str
    template_text: str
    slot: str
    composition_note: str = ""  # e.g., "替换首句", "在通用段落前插入"
    section: str = ""  # "methods" or "results"


@dataclass
class Slot:
    id: str
    name: str
    section: str
    generic_template: str = ""
    variants: List[TemplateVariant] = field(default_factory=list)


@dataclass
class TemplateLibrary:
    slots: Dict[str, Slot] = field(default_factory=dict)

    def get_slot(self, slot_id: str) -> Optional[Slot]:
        return self.slots.get(slot_id)

    def find_variants(self, slot_id: str, keyword: str) -> List[TemplateVariant]:
        """Find variants in a slot whose name contains keyword."""
        slot = self.slots.get(slot_id)
        if not slot:
            return []
        return [v for v in slot.variants if keyword.lower() in v.name.lower()]


def _extract_code_block(text: str, start_idx: int) -> tuple:
    """Extract text from a fenced code block starting at start_idx."""
    # Find ```text or ```
    block_start = text.find("```", start_idx)
    if block_start == -1:
        return "", start_idx
    # Find closing ```
    block_end = text.find("```", block_start + 3)
    if block_end == -1:
        return "", start_idx
    content = text[block_start + 3:block_end].strip()
    # Remove language marker if present (e.g., "text\n")
    if content.startswith("text"):
        content = content[4:].lstrip()
    return content, block_end + 3


def _parse_slot_section(section_text: str, section_name: str) -> Dict[str, Slot]:
    """Parse a section of SKILL.md (e.g., M1-M10 or R1-R9) into slots."""
    slots = {}

    # Match slot headers like "### M1. 研究情境 / 实证背景" or "### R3. 主假设检验（四拍节奏）"
    slot_pattern = re.compile(r'###\s+([MR]\d+)\.\s+(.+?)(?:\n|$)')

    # Find all slot positions
    matches = list(slot_pattern.finditer(section_text))

    for i, match in enumerate(matches):
        slot_id = match.group(1)
        slot_name = match.group(2).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(section_text)
        slot_text = section_text[start:end]

        slot = Slot(id=slot_id, name=slot_name, section=section_name)

        # Extract generic template
        generic_match = re.search(r'\*\*通用填空段落.*?\*\*\s*:\s*\n?```(?:text)?\n(.*?)```', slot_text, re.DOTALL)
        if generic_match:
            slot.generic_template = generic_match.group(1).strip()

        # Extract variants
        # Pattern: **Variant Name**（optional note）：
        # ```text
        # template
        # ```
        # We match any **...** that is followed by a code block, excluding "通用填空段落"
        variant_pattern = re.compile(
            r'\*\*([^*]+?)\*\*\s*(?:（([^）]+)）)?\s*[:：]?\s*\n?```(?:text)?\n(.*?)```',
            re.DOTALL
        )

        for vmatch in variant_pattern.finditer(slot_text):
            variant_name = vmatch.group(1).strip()
            # Skip generic template and non-variant markers
            if "通用填空段落" in variant_name or "通用" in variant_name:
                continue
            composition_note = vmatch.group(2) if vmatch.group(2) else ""
            template = vmatch.group(3).strip()

            variant = TemplateVariant(
                name=variant_name,
                template_text=template,
                slot=slot_id,
                composition_note=composition_note,
                section=section_name,
            )
            slot.variants.append(variant)

        slots[slot_id] = slot

    return slots


def parse_skill_md(skill_path: Path) -> TemplateLibrary:
    """Parse a SKILL.md file into TemplateLibrary."""
    text = skill_path.read_text(encoding="utf-8")

    # Determine if this is methods or results
    section_name = "methods" if "write-methods" in skill_path.name else "results"

    # Find the section containing the template skeletons
    # In both files, it starts with "## 填空段落骨架" and ends before "## 按设计类型一键生成示例"
    start_marker = "## 填空段落骨架"
    end_marker = "## 按设计类型一键生成示例"

    start_idx = text.find(start_marker)
    end_idx = text.find(end_marker)

    if start_idx == -1:
        # Try alternative markers
        start_idx = text.find("## M1.")
        if start_idx == -1:
            start_idx = 0
    if end_idx == -1:
        end_idx = len(text)

    skeleton_section = text[start_idx:end_idx]

    slots = _parse_slot_section(skeleton_section, section_name)
    return TemplateLibrary(slots=slots)


def list_all_variants(library: TemplateLibrary) -> List[str]:
    """Utility: list all variant names for debugging."""
    names = []
    for slot in library.slots.values():
        for v in slot.variants:
            names.append(f"{slot.id}: {v.name}")
    return names
