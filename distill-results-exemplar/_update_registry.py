#!/usr/bin/env python3
"""
Results Evidence Registry Updater
=================================

消费 distill-results-exemplar Phase 4 输出的 corpus_enrichment YAML 块，
自动更新 write-results/academic-writing-corpus/_evidence_registry.yaml 中的定量证据。

不负责：
- 修改 corpus .md 文件中的定性内容（骨架句法、反模式提醒等）
- 创建新的 estimator 条目（需手动在 registry 中添加）
- 删除 skeleton（降级为空数组由人工处理）

用法：
    python _update_registry.py <path/to/corpus_enrichment.yaml> [--dry-run]

输入格式（corpus_enrichment）:
    ---
    corpus_enrichment:
      batch_id: "batch_2024-05-22"
      estimator_family: "OLS_FE"
      source_paper: "Darby_2023_MSOM"
      source_subfield: "om"

      slot_updates:
        - slot: "R3"
          action: "append_skeleton_or_increment"
          skeleton_id: "r3_ols_four_beat_standard"
          skeleton: "..."
        - slot: "R7"
          action: "increment_count"
          skeleton_id: "r7_ols_threat_based"

      novel_patterns:
        - slot: "R4"
          observation: "AME+区域显著性图在计数模型中的三段式引入"
          note: "..."

      batch_metadata:
        total_papers_processed: 1

作者: Ricardo-kui
版本: 1.1.0
"""

import sys
import os
import io
import yaml
import argparse
import shutil
import hashlib
from datetime import datetime
from pathlib import Path

# Windows 控制台 UTF-8 兼容性
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

# ============================================================
# 配置
# ============================================================

REGISTRY_PATH = Path.home() / ".claude" / "skills" / "write-results" / "academic-writing-corpus" / "_evidence_registry.yaml"

STATUS_RULES = {
    "EMERGING": {"paper_count_max": 2},
    "VERIFIED": {"paper_count_min": 3},
    "ROBUST": {"paper_count_min": 5, "cross_subfields_min": 2},
}

VALID_SUBFIELDS = ["strategy", "ob_hr", "om", "marketing", "finance", "accounting"]
VALID_SLOTS = [f"R{i}" for i in range(1, 10)]
VALID_ACTIONS = ["create_new", "append_skeleton_or_increment", "increment_count"]
VALID_SKELETON_LEVELS = ["paragraph", "sentence"]

# Estimator 键名到 corpus 文件名的映射
# 大部分情况下：下划线替换为连字符。中文名保持不变。
ESTIMATOR_TO_CORPUS_FILE = {
    # 显式映射（当自动替换规则不适用时）
    "OLS_FE": "OLS-FE.md",
    "Logit_Probit_Ordered_Probit": "Logit-Probit-Ordered-Probit.md",
    "IV_2SLS": "IV-2SLS.md",
    # 中文名直接映射
    "生存分析": "生存分析.md",
    "计数模型": "计数模型.md",
    "实验": "实验.md",
    "多研究": "多研究.md",
    "匹配DiD": "匹配DiD.md",
    "堆叠扩散Logit": "堆叠扩散Logit.md",
    "同伴效应_网络效应": "同伴效应-网络效应.md",
    "推断二元结果": "推断二元结果.md",
    "跨受众构念对比": "跨受众构念对比.md",
    "三向交互": "三向交互.md",
    "构造暴露分解": "构造暴露分解.md",
}

def estimator_to_corpus_path(estimator_family):
    """将 estimator 键名转换为 corpus 文件名。"""
    if estimator_family in ESTIMATOR_TO_CORPUS_FILE:
        filename = ESTIMATOR_TO_CORPUS_FILE[estimator_family]
    else:
        # 默认规则：下划线替换为连字符
        filename = estimator_family.replace("_", "-") + ".md"
    return f"academic-writing-corpus/{filename}"

# 头部注释（每次保存时保留）
REGISTRY_HEADER_LINES = [
    "# Results Evidence Registry",
    "# Schema: estimator-slot-skeleton v1.0.0",
    "# 设计说明见 INDEX.md",
    "",
]

# ============================================================
# YAML 辅助函数
# ============================================================

def load_yaml(path):
    """
    加载 YAML 文件。
    兼容两种格式：
    1. 单一文档（当前标准格式）
    2. 多文档（旧版 frontmatter + 正文）——返回第二个文档
    """
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 检查是否为多文档（含有未在字符串中的 ---）
    docs = list(yaml.safe_load_all(content))

    if len(docs) == 0:
        return {}
    elif len(docs) == 1:
        return docs[0] or {}
    else:
        # 旧版格式：frontmatter + 正文，返回正文（第二个文档）
        # 跳过 frontmatter，返回第一个非 None 的正文文档
        for doc in docs[1:]:
            if doc is not None:
                return doc
        return {}


def save_yaml(path, data, header_lines=None):
    """
    保存 YAML，保留可读性。
    可选在文件头部追加注释行。
    """
    output = ""

    if header_lines:
        output += "\n".join(header_lines) + "\n"

    output += yaml.dump(
        data,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
        width=120,
        indent=2,
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(output)


# ============================================================
# 状态计算
# ============================================================

def compute_status(skeleton, status_rules):
    """
    根据 paper_count 和 subfield_distribution 计算 skeleton 的 status。

    规则：
    - ROBUST: paper_count >= 5 且跨 >=2 个子领域
    - VERIFIED: paper_count >= 3
    - EMERGING: paper_count <= 2
    """
    paper_count = skeleton.get("paper_count", 0)
    subfield_dist = skeleton.get("subfield_distribution", {})
    cross_subfields = sum(1 for v in subfield_dist.values() if v > 0)

    if paper_count >= status_rules["ROBUST"]["paper_count_min"] and \
       cross_subfields >= status_rules["ROBUST"]["cross_subfields_min"]:
        return "ROBUST"
    elif paper_count >= status_rules["VERIFIED"]["paper_count_min"]:
        return "VERIFIED"
    else:
        return "EMERGING"


def recompute_all_statuses(registry, status_rules):
    """重新计算 registry 中所有 skeleton 的 status。"""
    estimators = registry.get("estimators", {})
    for estimator_name, estimator_data in estimators.items():
        slots = estimator_data.get("slots", {})
        for slot_name, slot_data in slots.items():
            variants = slot_data.get("skeleton_variants", [])
            for variant in variants:
                variant["status"] = compute_status(variant, status_rules)
    return registry


# ============================================================
# 核心更新逻辑
# ============================================================

def apply_slot_update(registry, update, source_paper, source_subfield, status_rules, dry_run=False):
    """
    应用单个 slot_update 到 registry。

    action 类型：
    - create_new: 创建新 skeleton，paper_count=1
    - append_skeleton_or_increment: 若 skeleton_id 存在则计数+1，否则创建
    - increment_count: 仅对已有 skeleton 计数+1（不存在则报错）
    """
    estimator_family = update.get("estimator_family")
    slot = update.get("slot")
    action = update.get("action")
    skeleton_id = update.get("skeleton_id")
    skeleton_text = update.get("skeleton", "")
    skeleton_level = update.get("skeleton_level", "paragraph")

    if slot not in VALID_SLOTS:
        print(f"  ⚠️  跳过无效 slot: {slot}")
        return False

    if action not in VALID_ACTIONS:
        print(f"  ⚠️  跳过无效 action: {action}")
        return False

    if skeleton_level not in VALID_SKELETON_LEVELS:
        print(f"  ⚠️  无效 skeleton_level '{skeleton_level}'，默认使用 'paragraph'")
        skeleton_level = "paragraph"

    # 定位 estimator 和 slot
    estimators = registry.get("estimators", {})
    if estimator_family not in estimators:
        print(f"  ⚠️  Estimator '{estimator_family}' 不在 registry 中。跳过（如需新增请手动编辑 registry）。")
        return False

    estimator_data = estimators[estimator_family]
    slots = estimator_data.get("slots", {})
    if slot not in slots:
        # 自动创建 slot 结构
        if not dry_run:
            slots[slot] = {"description": "", "skeleton_variants": []}
        print(f"  ℹ️  自动创建 slot {slot}（尚未在 registry 中定义）")

    slot_data = slots.get(slot, {"description": "", "skeleton_variants": []})
    variants = slot_data.setdefault("skeleton_variants", [])

    # 查找是否已存在该 skeleton_id
    existing = None
    for v in variants:
        if v.get("id") == skeleton_id:
            existing = v
            break

    if action == "create_new":
        if existing:
            print(f"  ⚠️  skeleton_id '{skeleton_id}' 已存在，跳过 create_new（使用 append_skeleton_or_increment）")
            return False
        if dry_run:
            print(f"  [DRY-RUN] 将创建新 skeleton: {skeleton_id} (EMERGING)")
            return True
        new_variant = {
            "id": skeleton_id,
            "skeleton": skeleton_text,
            "skeleton_level": skeleton_level,
            "paper_count": 1,
            "status": "EMERGING",
            "subfield_distribution": {source_subfield: 1} if source_subfield else {},
            "sources": [source_paper] if source_paper else [],
            "transferability": "",
            "paradigm_exclusivity": "",
            "rhythm_tags": [],
            "notes": "",
            "corpus_path": estimator_to_corpus_path(estimator_family),
        }
        variants.append(new_variant)
        print(f"  ✅ 创建新 skeleton: {skeleton_id} (EMERGING, level={skeleton_level})")
        return True

    elif action == "append_skeleton_or_increment":
        if existing:
            if dry_run:
                print(f"  [DRY-RUN] 将更新 skeleton: {skeleton_id} (count: {existing['paper_count']} → {existing['paper_count'] + 1})")
                return True
            existing["paper_count"] = existing.get("paper_count", 0) + 1
            if source_subfield:
                existing["subfield_distribution"][source_subfield] = \
                    existing["subfield_distribution"].get(source_subfield, 0) + 1
            if source_paper and source_paper not in existing.get("sources", []):
                existing["sources"].append(source_paper)
            old_status = existing["status"]
            existing["status"] = compute_status(existing, status_rules)
            print(f"  ✅ 更新 skeleton: {skeleton_id} (count: {existing['paper_count']}, status: {old_status} → {existing['status']})")
        else:
            if dry_run:
                print(f"  [DRY-RUN] 将创建新 skeleton (append_or_increment fallback): {skeleton_id} (EMERGING)")
                return True
            new_variant = {
                "id": skeleton_id,
                "skeleton": skeleton_text,
                "skeleton_level": skeleton_level,
                "paper_count": 1,
                "status": "EMERGING",
                "subfield_distribution": {source_subfield: 1} if source_subfield else {},
                "sources": [source_paper] if source_paper else [],
                "transferability": "",
                "paradigm_exclusivity": "",
                "rhythm_tags": [],
                "notes": "",
                "corpus_path": estimator_to_corpus_path(estimator_family),
            }
            variants.append(new_variant)
            print(f"  ✅ 创建新 skeleton (append_or_increment fallback): {skeleton_id} (EMERGING, level={skeleton_level})")
        return True

    elif action == "increment_count":
        if not existing:
            print(f"  ❌ skeleton_id '{skeleton_id}' 不存在，无法 increment_count")
            return False
        if dry_run:
            print(f"  [DRY-RUN] 将更新 skeleton: {skeleton_id} (count: {existing['paper_count']} → {existing['paper_count'] + 1})")
            return True
        existing["paper_count"] = existing.get("paper_count", 0) + 1
        if source_subfield:
            existing["subfield_distribution"][source_subfield] = \
                existing["subfield_distribution"].get(source_subfield, 0) + 1
        if source_paper and source_paper not in existing.get("sources", []):
            existing["sources"].append(source_paper)
        old_status = existing["status"]
        existing["status"] = compute_status(existing, status_rules)
        print(f"  ✅ 更新 skeleton: {skeleton_id} (count: {existing['paper_count']}, status: {old_status} → {existing['status']})")
        return True

    return False


def apply_novel_patterns(registry, patterns, estimator_family, dry_run=False):
    """应用 novel_patterns 到 cross_slot_patterns。"""
    if not estimator_family or estimator_family not in registry.get("estimators", {}):
        return

    estimator_data = registry["estimators"][estimator_family]
    cross_patterns = estimator_data.setdefault("cross_slot_patterns", [])
    existing_ids = {p.get("id") for p in cross_patterns}

    for pattern in patterns:
        # 使用 hash 生成稳定的 pattern_id
        obs_hash = hashlib.md5(pattern.get("observation", "").encode()).hexdigest()[:8]
        pattern_id = f"csp_{estimator_family}_{pattern.get('slot', 'unknown')}_{obs_hash}"

        if pattern_id in existing_ids:
            if dry_run:
                print(f"  [DRY-RUN] pattern '{pattern_id}' 已存在，跳过")
            continue

        if dry_run:
            print(f"  [DRY-RUN] 将添加 novel cross-slot pattern: {pattern_id} (EMERGING)")
            continue

        new_pattern = {
            "id": pattern_id,
            "pattern": pattern.get("observation", ""),
            "from_slot": pattern.get("slot", ""),
            "to_slot": "",
            "paper_count": 1,
            "status": "EMERGING",
            "note": pattern.get("note", ""),
        }
        cross_patterns.append(new_pattern)
        print(f"  ✅ 添加 novel cross-slot pattern: {pattern_id} (EMERGING)")


# ============================================================
# 主函数
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="更新 Results Evidence Registry")
    parser.add_argument("input", help="corpus_enrichment.yaml 路径")
    parser.add_argument("--dry-run", action="store_true", help="预览变更但不写入文件")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"❌ 输入文件不存在: {input_path}")
        sys.exit(1)

    if not REGISTRY_PATH.exists():
        print(f"❌ Registry 文件不存在: {REGISTRY_PATH}")
        print("   请确认 write-results/academic-writing-corpus/_evidence_registry.yaml 已创建")
        sys.exit(1)

    # 备份（dry-run 时也备份，以便对比）
    if not args.dry_run:
        backup_path = str(REGISTRY_PATH) + f".backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        shutil.copy2(REGISTRY_PATH, backup_path)
        print(f"💾 Registry 已备份至: {backup_path}")

    # 加载输入
    print(f"📖 读取 corpus_enrichment: {input_path}")
    input_data = load_yaml(input_path)
    enrichment = input_data.get("corpus_enrichment", input_data)

    if not enrichment:
        print("❌ 输入文件中没有 corpus_enrichment 数据")
        sys.exit(1)

    batch_id = enrichment.get("batch_id", f"batch_{datetime.now().strftime('%Y-%m-%d')}")
    estimator_family = enrichment.get("estimator_family")
    source_paper = enrichment.get("source_paper", "")
    source_subfield = enrichment.get("source_subfield", "")
    slot_updates = enrichment.get("slot_updates", [])
    novel_patterns = enrichment.get("novel_patterns", [])
    batch_metadata = enrichment.get("batch_metadata", {})

    # subfield 验证
    if source_subfield and source_subfield not in VALID_SUBFIELDS:
        print(f"⚠️  无效 subfield '{source_subfield}'，跳过分布更新")
        source_subfield = ""

    print(f"\n🎯 Batch: {batch_id}")
    print(f"   Estimator: {estimator_family}")
    print(f"   Source: {source_paper} ({source_subfield or '未指定'})")
    print(f"   Slot updates: {len(slot_updates)}")
    print(f"   Novel patterns: {len(novel_patterns)}")
    if args.dry_run:
        print("\n🚧 DRY-RUN 模式：不会实际修改 registry")

    # 加载 registry
    print(f"\n📖 读取 registry: {REGISTRY_PATH}")
    registry = load_yaml(REGISTRY_PATH)

    # 执行更新
    updated_count = 0
    print("\n🔄 应用 slot updates...")
    for update in slot_updates:
        if not update.get("estimator_family") and estimator_family:
            update = dict(update)
            update["estimator_family"] = estimator_family
        if apply_slot_update(registry, update, source_paper, source_subfield, STATUS_RULES, dry_run=args.dry_run):
            updated_count += 1

    # 应用 novel patterns
    if novel_patterns:
        print("\n🔄 应用 novel patterns...")
        apply_novel_patterns(registry, novel_patterns, estimator_family, dry_run=args.dry_run)

    # 重新计算所有 status
    print("\n🔄 重新计算所有 skeleton status...")
    registry = recompute_all_statuses(registry, STATUS_RULES)

    # 更新 meta
    meta = registry.setdefault("meta", {})
    meta["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    meta["last_batch_id"] = batch_id
    meta["batches_processed"] = meta.get("batches_processed", 0) + (0 if args.dry_run else 1)

    # 使用 batch_metadata.total_papers_processed 或回退到 source_paper
    papers_in_batch = batch_metadata.get("total_papers_processed", 1 if source_paper else 0)
    meta["total_papers_indexed"] = meta.get("total_papers_indexed", 0) + (0 if args.dry_run else papers_in_batch)

    # 追加 batch_history
    if not args.dry_run:
        batch_history = registry.setdefault("batch_history", [])
        batch_history.append({
            "batch_id": batch_id,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "estimator_family": estimator_family,
            "source_paper": source_paper,
            "source_subfield": source_subfield,
            "slot_updates_count": len(slot_updates),
            "novel_patterns_count": len(novel_patterns),
        })

    # 保存
    if args.dry_run:
        print(f"\n🚧 DRY-RUN 完成，未写入 registry")
    else:
        print(f"\n💾 保存 registry...")
        save_yaml(REGISTRY_PATH, registry, header_lines=REGISTRY_HEADER_LINES)

    # 汇总报告
    print("\n" + "=" * 50)
    if args.dry_run:
        print("🚧 DRY-RUN 预览完成")
    else:
        print("✅ 更新完成")
    print(f"   Registry 路径: {REGISTRY_PATH}")
    print(f"   本次更新 skeleton: {updated_count}")
    print(f"   Batch ID: {batch_id}")
    if not args.dry_run:
        print(f"   累计 batches: {meta['batches_processed']}")
        print(f"   累计 papers: {meta['total_papers_indexed']}")
    print("=" * 50)


if __name__ == "__main__":
    main()
