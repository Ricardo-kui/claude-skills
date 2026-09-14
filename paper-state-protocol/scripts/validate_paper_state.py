#!/usr/bin/env python3
"""validate_paper_state.py — 防片段/schema 漂移的轻量校验器。

校验 references/workflow-fragments.md 中全部 ```yaml 示例片段的叶子字段
均已在 references/schema.md（v1.3 权威 schema）登记；未登记字段报错退出 1。

用法：
    python scripts/validate_paper_state.py            # 校验 workflow-fragments.md
    python scripts/validate_paper_state.py EXTRA.md   # 额外校验其他片段模板文件

动态键（假设 id H1/H2、storyline id S1/S2）按 <*> 处理，不算未登记。
"""
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REFS = HERE.parent / "references"
SCHEMA_MD = REFS / "schema.md"
FRAGMENTS_MD = REFS / "workflow-fragments.md"

# 这些父路径下的直接子键为动态 id（假设 id / storyline id），归一化为 <*>
DYNAMIC_DICT_PARENTS = {
    "methods.hypothesis_variable_map",
    "results.hypothesis_results",
    "methods.story_alignment.storyline_model_map",
    "results.story_resolution.storylines",
    "methods.robustness_plan.excluded",
}


def yaml_blocks(md_path: Path):
    text = md_path.read_text(encoding="utf-8")
    for m in re.finditer(r"```yaml\n(.*?)```", text, re.S):
        block = m.group(1)
        # 去掉纯注释行后为空块的跳过
        if block.strip():
            yield block


def flatten(node, prefix="", out=None):
    """把嵌套 dict/list 展开为叶子路径集合；列表记 [*]，动态 dict 子键记 <*>。"""
    if out is None:
        out = set()
    if isinstance(node, dict):
        for k, v in node.items():
            seg = "<*>" if prefix in DYNAMIC_DICT_PARENTS else str(k)
            path = f"{prefix}.{seg}" if prefix else seg
            out.add(path)
            if isinstance(v, (dict, list)) and v:
                flatten(v, path, out)
    elif isinstance(node, list):
        for item in node:
            flatten(item, f"{prefix}[*]" if prefix else "[*]", out)
    return out


def registered_paths():
    """schema.md 中第一个 yaml 块 = 权威 schema 示例，展开为登记路径集合。"""
    schema_yaml = next(yaml_blocks(SCHEMA_MD))
    data = yaml.safe_load(schema_yaml)
    return flatten(data)


def validate_file(md_path: Path, registered: set):
    unknown = []
    for i, block in enumerate(yaml_blocks(md_path), 1):
        try:
            data = yaml.safe_load(block)
        except yaml.YAMLError as e:
            unknown.append(f"[{md_path.name} block#{i}] YAML 解析失败: {e}")
            continue
        if not isinstance(data, dict):
            continue
        for path in sorted(flatten(data)):
            if path not in registered:
                parent = path.rsplit(".", 1)[0] if "." in path else ""
                if parent not in DYNAMIC_DICT_PARENTS:
                    unknown.append(f"[{md_path.name} block#{i}] 未登记字段: {path}")
    return unknown


def main():
    registered = registered_paths()
    files = [FRAGMENTS_MD] + [Path(a) for a in sys.argv[1:]]
    problems = []
    for f in files:
        problems += validate_file(f, registered)
    if problems:
        print(f"FAIL: {len(problems)} 个未登记/解析失败项")
        for p in problems:
            print(" -", p)
        sys.exit(1)
    print(f"OK: {len(files)} 个文件的所有片段字段均已在 schema.md 登记（{len(registered)} 条登记路径）")


if __name__ == "__main__":
    main()
