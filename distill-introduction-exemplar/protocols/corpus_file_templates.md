# Introduction corpus 治理计划模板

> Phase 4.6 需要写回 corpus 时加载。所有写入必须通过
> `../../write-introduction/scripts/introduction_corpus_governance.py`；不要手工追加编号。

## Reference 计划

单篇论文只能形成 `ADD_REFERENCE`：

```yaml
actions:
  - action: ADD_REFERENCE
    target_parent_id: tensions:01-despite-progress-unaddressed
    nearest_neighbor_id: tensions:01-despite-progress-unaddressed:vD
    title: 多重利益相关者论证型
    source_paper: author_year (AMJ)
    template: "[Gap] matters because it affects [stakeholder A] and [stakeholder B]."
    capability_loss_if_merged: "新增同一遗漏对两个利益相关者产生不同后果的证据组织能力。"
    applicability: "存在两个可核验且理论相关的利益相关者后果时。"
    taboo: "不得为了凑双重 stakes 人为增加不相关群体。"
```

治理脚本自动分配下一个稳定字母 ID，并写入：

- 模板；
- 来源；
- `reference_exemplar` 角色；
- 最近邻与能力损失；
- 适用边界和禁忌。

## 来源扩展

新论文复现既有说服能力时使用：

```yaml
actions:
  - action: EXTEND_SOURCE
    target_asset_id: tensions:01-despite-progress-unaddressed:vD
    source_paper: author_year (SMJ)
```

重复执行必须幂等，不能生成第二个来源或第二个变体。

## 晋升、合并与废弃

```yaml
actions:
  - action: PROMOTE
    target_asset_id: tensions:01-despite-progress-unaddressed:vD
    role: generative_variant
    evidence_status: VERIFIED
    paper_count: 3
    verification_basis: cross_paper_full_text
    source_papers:
      - author_a_2024 (AMJ)
      - author_b_2025 (SMJ)
      - author_c_2026 (OS)

  - action: MERGE
    source_asset_id: tensions:01-despite-progress-unaddressed:vAF
    target_asset_id: tensions:01-despite-progress-unaddressed:vD
    capability_overlap: "两者均以具体理由证明遗漏为何令人意外。"

  - action: DEPRECATE
    target_asset_id: hooks:03-data-shock:vX
    reason: "证据来源撤回且无可验证替代来源。"

  - action: SET_REFERENCE_MENU
    target_parent_id: tensions:01-despite-progress-unaddressed
    asset_ids:
      - tensions:01-despite-progress-unaddressed:vA
      - tensions:01-despite-progress-unaddressed:vB
      - tensions:01-despite-progress-unaddressed:vC
      - tensions:01-despite-progress-unaddressed:vD
      - tensions:01-despite-progress-unaddressed:vG
```

晋升要求 VERIFIED/ROBUST 与完整依据；低于3篇只能由
`verification_basis: user_expert_audit` 显式覆盖。合并和废弃保留旧 ID，禁止物理删除历史证据。

## 执行

```powershell
python ../../write-introduction/scripts/introduction_corpus_governance.py apply-plan plan.yaml --dry-run
python ../../write-introduction/scripts/introduction_corpus_governance.py apply-plan plan.yaml
python ../../write-introduction/scripts/introduction_corpus_governance.py validate
python ../../write-introduction/scripts/introduction_asset_catalog.py audit
```

任何 snapshot、重复 ID、悬空 merge、角色门槛、父策略归属或每父策略候选上限错误都使 writeback 失败。
