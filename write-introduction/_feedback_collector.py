#!/usr/bin/env python3
"""
write-introduction Feedback Collector
=====================================

消费 feedback/ 目录下的原始反馈 YAML，自动更新 _evidence_registry.yaml 中的
validation_history。

用法:
    # 提交一条新反馈（交互式）
    python _feedback_collector.py --submit

    # 聚合所有反馈到 registry
    python _feedback_collector.py --aggregate [--dry-run]

    # 生成统计报告
    python _feedback_collector.py --report

    # 查看某个模板的反馈历史
    python _feedback_collector.py --history 06-paradigm-challenge

作者: Ricardo-kui
版本: 1.0.0
"""

import sys
import os
import io
import yaml
import argparse
import shutil
import uuid
from datetime import datetime
from pathlib import Path
from collections import defaultdict, Counter

# Windows 控制台 UTF-8 兼容性
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

# ============================================================
# 配置
# ============================================================

SKILL_DIR = Path(__file__).parent
FEEDBACK_DIR = SKILL_DIR / "feedback"
REGISTRY_PATH = SKILL_DIR / "academic-writing-corpus" / "_evidence_registry.yaml"
SCHEMA_PATH = FEEDBACK_DIR / "_schema.yaml"

# Registry 中各模块类别到键名的映射
REGISTRY_CATEGORIES = {
    "hook": "hooks",
    "tension": "tensions",
    "stakes": "stakes",
    "literature_turn": "literature_turns",
    "preview": "previews",
    "contribution": "contributions",
    "transition": "transitions",
    "theory_lens": "theory_lens",
    "research_question": "research_questions",
}

VALID_VERDICTS = ["validated", "revise", "reject"]

# ============================================================
# YAML 辅助函数
# ============================================================

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    docs = list(yaml.safe_load_all(content))
    if len(docs) == 0:
        return {}
    elif len(docs) == 1:
        return docs[0] or {}
    else:
        for doc in docs[1:]:
            if doc is not None:
                return doc
        return {}


def save_yaml(path, data):
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(
            data,
            f,
            allow_unicode=True,
            sort_keys=False,
            default_flow_style=False,
            width=120,
            indent=2,
        )


# ============================================================
# 核心: 读取反馈
# ============================================================

def load_all_feedbacks():
    """加载 feedback/ 目录下所有 .yaml 文件（排除 _schema.yaml）。"""
    feedbacks = []
    if not FEEDBACK_DIR.exists():
        return feedbacks
    for fp in sorted(FEEDBACK_DIR.glob("*.yaml")):
        if fp.name.startswith("_"):
            continue
        try:
            data = load_yaml(fp)
            if data and "feedback_entry" in data:
                feedbacks.append(data["feedback_entry"])
            elif data and "feedback_id" in data:
                # 也支持直接以 feedback_entry 内容作为顶层
                feedbacks.append(data)
        except Exception as e:
            print(f"  ⚠️  跳过损坏的反馈文件 {fp.name}: {e}")
    return feedbacks


# ============================================================
# 核心: 聚合到 Registry
# ============================================================

def aggregate_feedbacks(dry_run=False):
    """
    将所有反馈聚合到 _evidence_registry.yaml。

    对每个模板 canonical_id:
    - total_runs: 使用该模板的反馈总数
    - validated: 标记 validated 的数量
    - revise: 标记 revise 的数量
    - reject: 标记 reject 的数量
    - common_revise_reasons: revise/reject 中最常见的原因（Top 3）
    """
    registry = load_yaml(REGISTRY_PATH)
    feedbacks = load_all_feedbacks()

    if not feedbacks:
        print("ℹ️  feedback/ 目录中没有可聚合的反馈。")
        return

    print(f"📊 加载了 {len(feedbacks)} 条反馈，开始聚合...")

    # 按 (category, canonical_id) 分组统计
    stats = defaultdict(lambda: {
        "total_runs": 0,
        "validated": 0,
        "revise": 0,
        "reject": 0,
        "reasons": Counter(),
    })

    for fb in feedbacks:
        # 1. 收集模块级评价
        module_ratings = fb.get("module_ratings", [])
        # 如果没有模块级评价，用总体评价填充到所有使用的模板
        if not module_ratings:
            overall = fb.get("overall_verdict", "validated")
            templates = fb.get("templates_used", [])
            for t in templates:
                cat = REGISTRY_CATEGORIES.get(t.get("module", "").lower())
                cid = t.get("canonical_id", "")
                if cat and cid:
                    s = stats[(cat, cid)]
                    s["total_runs"] += 1
                    s[overall] += 1
        else:
            for mr in module_ratings:
                cid = mr.get("canonical_id", "")
                rating = mr.get("rating", "validated")
                # 推断模块类别（从 canonical_id 前缀或整体匹配）
                cat = infer_category(cid, registry)
                if cat and cid:
                    s = stats[(cat, cid)]
                    s["total_runs"] += 1
                    s[rating] += 1

        # 2. 收集修订原因
        revise_reasons = fb.get("revise_reasons", [])
        for rr in revise_reasons:
            reason_cat = rr.get("reason_category", "other")
            affected = rr.get("affected_modules", [])
            # 将原因关联到受影响的模块
            if affected:
                for mod in affected:
                    # 找到对应的 canonical_id
                    for t in fb.get("templates_used", []):
                        if t.get("module", "").lower() == mod.lower():
                            cid = t.get("canonical_id", "")
                            cat = infer_category(cid, registry)
                            if cat and cid:
                                stats[(cat, cid)]["reasons"][reason_cat] += 1
            else:
                # 未指定 affected_modules，关联到所有使用的模板
                for t in fb.get("templates_used", []):
                    cid = t.get("canonical_id", "")
                    cat = infer_category(cid, registry)
                    if cat and cid:
                        stats[(cat, cid)]["reasons"][reason_cat] += 1

    # 3. 写回 registry
    changed = 0
    for (cat, cid), s in sorted(stats.items()):
        if cat not in registry.get("evidence", {}):
            print(f"  ⚠️  Registry 中缺少类别 '{cat}'，跳过 {cid}")
            continue
        cat_data = registry["evidence"][cat]
        if cid not in cat_data:
            print(f"  ⚠️  Registry 中 {cat}/{cid} 不存在，跳过")
            continue

        entry = cat_data[cid]
        old_hist = entry.get("validation_history", {})

        # 合并已有数据（如果有）
        new_hist = {
            "total_runs": old_hist.get("total_runs", 0) + s["total_runs"],
            "validated": old_hist.get("validated", 0) + s["validated"],
            "revise": old_hist.get("revise", 0) + s["revise"],
            "reject": old_hist.get("reject", 0) + s["reject"],
            "common_revise_reasons": extract_top_reasons(
                old_hist.get("common_revise_reasons", []),
                s["reasons"],
            ),
        }

        entry["validation_history"] = new_hist
        changed += 1

        # 计算 reject_rate 用于报告
        tr = new_hist["total_runs"]
        rr = new_hist["reject"] / tr if tr > 0 else 0
        status_flag = "✅" if tr < 2 or rr < 0.50 else "⚠️ CAUTION"
        print(f"  {status_flag} {cat}/{cid}: runs={tr}, reject_rate={rr:.0%}")

    if dry_run:
        print(f"\n[DRY-RUN] 将更新 {changed} 个模板，未写入文件。")
    else:
        # 更新 meta
        registry.setdefault("meta", {})
        registry["meta"]["last_feedback_aggregate"] = datetime.now().isoformat()
        registry["meta"]["total_feedback_entries"] = len(feedbacks)
        save_yaml(REGISTRY_PATH, registry)
        print(f"\n✅ 已更新 {changed} 个模板的 validation_history → {REGISTRY_PATH}")


def infer_category(canonical_id, registry):
    """根据 canonical_id 和 registry 结构推断所属类别。"""
    evidence = registry.get("evidence", {})
    for cat, items in evidence.items():
        if canonical_id in items:
            return cat
    # 启发式回退
    cid = canonical_id.lower()
    if cid.startswith("0") and len(cid) >= 2:
        return "hooks"  # 大多数 hooks 是数字开头
    return None


def extract_top_reasons(existing_list, new_counter, top_n=3):
    """合并已有原因和新原因，返回频率最高的 top_n 个。"""
    merged = Counter()
    for item in existing_list:
        if isinstance(item, str):
            # 格式: "reason_category (count)" 或纯文本
            if "(" in item and item.endswith(")"):
                parts = item.rsplit("(", 1)
                reason = parts[0].strip()
                try:
                    count = int(parts[1].rstrip(")"))
                    merged[reason] += count
                except ValueError:
                    merged[item] += 1
            else:
                merged[item] += 1
    merged.update(new_counter)
    most_common = merged.most_common(top_n)
    return [f"{reason} ({count})" for reason, count in most_common]


# ============================================================
# 报告生成
# ============================================================

def generate_report():
    """生成当前 validation_history 的统计报告。"""
    registry = load_yaml(REGISTRY_PATH)
    evidence = registry.get("evidence", {})

    print("=" * 60)
    print("write-introduction Feedback 统计报告")
    print("=" * 60)

    grand_total = 0
    caution_count = 0

    for cat, items in sorted(evidence.items()):
        cat_runs = 0
        cat_entries = []
        for cid, entry in sorted(items.items()):
            hist = entry.get("validation_history", {})
            tr = hist.get("total_runs", 0)
            if tr == 0:
                continue
            rej = hist.get("reject", 0)
            rr = rej / tr if tr > 0 else 0
            cat_runs += tr
            grand_total += tr
            flag = "⚠️ " if tr >= 2 and rr >= 0.50 else "   "
            if flag == "⚠️ ":
                caution_count += 1
            reasons = hist.get("common_revise_reasons", [])
            reason_str = " | ".join(reasons) if reasons else "—"
            cat_entries.append(f"  {flag}{cid:40s} runs={tr:3d}  reject_rate={rr:.0%}  reasons={reason_str}")

        if cat_entries:
            print(f"\n📁 {cat} (总 runs: {cat_runs})")
            for line in cat_entries:
                print(line)

    print(f"\n{'=' * 60}")
    print(f"总反馈次数: {grand_total}")
    print(f"CAUTION 模板数: {caution_count}")
    if caution_count > 0:
        print("⚠️  这些模板 reject_rate ≥ 50% 且 total_runs ≥ 2，使用时建议验证。")


# ============================================================
# 交互式提交
# ============================================================

def interactive_submit():
    """交互式收集一条反馈。"""
    print("📝 write-introduction 反馈提交")
    print("=" * 50)

    fb = {}
    fb["feedback_id"] = str(uuid.uuid4())[:8]
    fb["timestamp"] = datetime.now().isoformat()
    fb["source"] = "manual"

    print("\n1. 用户研究上下文")
    fb["user_context"] = {
        "gap_type": input("   Gap 类型 [Incompleteness/Inadequacy/Incommensurability]: ").strip(),
        "makadok_dimension": input("   Makadok 贡献维度 [Mechanism/Boundary/...]: ").strip(),
        "target_journal": input("   目标期刊: ").strip(),
        "research_topic": input("   研究主题（一句话）: ").strip(),
    }

    print("\n2. 使用的模板（输入 'done' 结束）")
    templates = []
    while True:
        mod = input("   模块名 [hook/tension/stakes/...] (或 done): ").strip().lower()
        if mod == "done":
            break
        if not mod:
            continue
        cid = input(f"   {mod} 的 canonical_id: ").strip()
        templates.append({"module": mod, "canonical_id": cid})
    fb["templates_used"] = templates

    print("\n3. 总体评价")
    fb["overall_verdict"] = input("   总体评价 [validated/revise/reject]: ").strip().lower()

    if fb["overall_verdict"] != "validated":
        print("\n4. 修订/拒绝原因（输入 'done' 结束）")
        reasons = []
        while True:
            cat = input("   原因分类 [energy_mismatch/weak_gap/overpromise/...] (或 done): ").strip()
            if cat == "done":
                break
            if not cat:
                continue
            desc = input("   具体描述: ").strip()
            aff = input("   受影响模块（逗号分隔，如 hook,tension）: ").strip()
            affected = [x.strip() for x in aff.split(",") if x.strip()]
            reasons.append({
                "reason_category": cat,
                "description": desc,
                "affected_modules": affected,
            })
        fb["revise_reasons"] = reasons

        mod = input("   用户实际修改摘要（可选）: ").strip()
        if mod:
            fb["post_use_modifications"] = mod

    # 保存
    filename = f"{datetime.now().strftime('%Y-%m-%d')}_{fb['feedback_id']}.yaml"
    filepath = FEEDBACK_DIR / filename
    save_yaml(filepath, {"feedback_entry": fb})
    print(f"\n✅ 反馈已保存: {filepath}")
    print(f"   运行 'python _feedback_collector.py --aggregate' 以更新 registry。")


# ============================================================
# 查看历史
# ============================================================

def show_history(canonical_id):
    """查看某个模板的所有反馈历史。"""
    feedbacks = load_all_feedbacks()
    matches = []
    for fb in feedbacks:
        for t in fb.get("templates_used", []):
            if t.get("canonical_id") == canonical_id:
                matches.append(fb)
                break
        for mr in fb.get("module_ratings", []):
            if mr.get("canonical_id") == canonical_id:
                if fb not in matches:
                    matches.append(fb)

    if not matches:
        print(f"ℹ️  没有找到 {canonical_id} 的反馈历史。")
        return

    print(f"📜 {canonical_id} 的反馈历史（共 {len(matches)} 条）")
    print("=" * 60)
    for fb in matches:
        ts = fb.get("timestamp", "?")
        topic = fb.get("user_context", {}).get("research_topic", "?")
        verdict = fb.get("overall_verdict", "?")
        # 查找模块级评价
        mod_rating = ""
        for mr in fb.get("module_ratings", []):
            if mr.get("canonical_id") == canonical_id:
                mod_rating = f" [模块评价: {mr.get('rating', '?')}]"
                break
        print(f"\n  [{ts}] {topic}")
        print(f"    总体: {verdict}{mod_rating}")
        for rr in fb.get("revise_reasons", []):
            affected = rr.get("affected_modules", [])
            if not affected or any(a.lower() in [m.get("module", "").lower() for m in fb.get("templates_used", []) if m.get("canonical_id") == canonical_id] for a in affected):
                print(f"    ⚠️  {rr.get('reason_category', '?')}: {rr.get('description', '')}")


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="write-introduction Feedback Collector",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--submit", action="store_true", help="交互式提交一条反馈")
    parser.add_argument("--aggregate", action="store_true", help="聚合所有反馈到 registry")
    parser.add_argument("--report", action="store_true", help="生成统计报告")
    parser.add_argument("--history", type=str, metavar="CANONICAL_ID", help="查看某模板的反馈历史")
    parser.add_argument("--dry-run", action="store_true", help="仅模拟，不写入文件")

    args = parser.parse_args()

    if args.submit:
        interactive_submit()
    elif args.aggregate:
        aggregate_feedbacks(dry_run=args.dry_run)
    elif args.report:
        generate_report()
    elif args.history:
        show_history(args.history)
    else:
        parser.print_help()
        print("\n💡 提示: 没有反馈文件？先运行 --submit 提交一条，或手动创建 feedback/*.yaml。")


if __name__ == "__main__":
    main()
