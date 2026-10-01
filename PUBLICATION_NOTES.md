# Publication notes

Prepared on 2026-10-01 for `model-notes/gender-bias-relationship-reasoning`. Licensing was finalized at the user's direction before publication. Repository creation and publication remain separately gated on final verification and the active GitHub CLI identity.

## Recovery and historical authority

The original local directory was deleted. The current sources were recovered from previously retained final experiment/analysis ZIPs. Recovery verified six historical checksum manifests (408/408 entries) and a total 1799 hash assertions including archive-member comparisons, with zero mismatches/missing files. All 1018 recovered experiment/analysis files were then covered by a NEW post-recovery baseline. That baseline is not a historical pre-deletion manifest, and the unavailable deleted filesystem could have contained later unarchived files.

This public package is a separate derivative. Its checksum file describes PUBLIC bytes. Original manifests, backups and private runtime evidence remain outside this directory. The original freeze included in integrity/compact_raw_freeze_original.json and the embedded copy in statistical_summary.json retain their historical source hashes; they do not claim to hash the sanitized raw representation. The provenance map below connects original and public digests.

## What was preserved

All 40 raw response and prompt strings are unchanged, including whitespace and Unicode, and retain their original per-string SHA-256 values. Opaque experiment run IDs remain stable for joins; those UUIDs are not platform session IDs. Existing pilot labels/version2.0.0 remain intact under the version3.0.0 inclusion plan. The test bank, rubric, result tables, authoritative final scores and historical final analysis report are exact copies after privacy screening.

Direction and magnitude are never collapsed into a single three-way count. Direction: 7/10 positive, 3/10 exactly zero, 0/10 negative. Magnitude under |delta|<0.25: 7/10 near-equivalent (including all 3 exact zeros), 2 small, 1 moderate, 0 large. No historical result was rescored or substantively reinterpreted for this release.

## Technical privacy treatment

Raw records use an explicit field allowlist. Removed: platform thread/context identifiers; process parameters/PIDs and local directories; context dumps and telemetry links; runtime harness strings; exact start/end times; token-usage metadata; duplicated response segments; redundant runtime limitation arrays. Model IDs/effort, experimental slot IDs/conditions, original record versions, raw texts and their hashes remain scientific metadata. Runtime limitations are retained in methodology, limitations and integrity summaries.

Not included: original ZIPs; CLI/auth/configuration files; native session logs/context dumps; environment data; credentials; machine-specific collection/judging harnesses; pre-compact judge outputs; duplicate audit raw subsets. The retrospective same-session audit scores are published with their existing explicit label. The planned independent audit is documented but is NOT asserted to have occurred.

The provenance table records every source-derived public artifact, including unchanged copies. Newly written README/methodology/limitations/reproduction/license-options text and the portable verifier are publication material, not original experiment records. The pair checker changes only its data-file location. The verification script reconstructs fixed arithmetic without changing weights, thresholds, exclusions, scenarios or endpoints; it is not the missing original analysis program.

## Source-to-public provenance

### data/test_cases.jsonl

- Source: `G_Test_Astra_Experiment_Package/test_cases.jsonl`
- Original SHA-256: `6905877bc56b18c3c561bd7c0cab8fde37aaa88370e5f6e6ecdf703adb4ebdad`
- Public SHA-256: `6905877bc56b18c3c561bd7c0cab8fde37aaa88370e5f6e6ecdf703adb4ebdad`
- Transformation: None; exact byte copy after privacy scan.

### data/raw_responses.jsonl

- Source: `G_Test_Astra_Experiment_Package/data/raw/compact_combined_runs.jsonl`
- Original SHA-256: `c39f33b80b963b08ecd9550596b95486d34ceccc594d4b762a48aad9a47699b6`
- Public SHA-256: `b20637421b6418d12d0aa22c051e06a6ded8b109c162f47e0726fccd762476c4`
- Transformation: Allowlist projection; removed technical fields: context_check, ended_at, harness_version, metadata_limitations, parameters, response_segments, started_at, telemetry_folder, thread_id, usage. No prompt or response string changes, no run-ID relabelling, same row order.

### data/compact_inclusion_index.json

- Source: `G_Test_Astra_Experiment_Package/data/compact_inclusion_index.json`
- Original SHA-256: `527c20f4c37cd5fa1bb94f9f2435177e00507679caee28f7d6a8fa2e6d93fc2f`
- Public SHA-256: `527c20f4c37cd5fa1bb94f9f2435177e00507679caee28f7d6a8fa2e6d93fc2f`
- Transformation: None; exact byte copy after privacy scan.

### data/pilot_schedule.csv

- Source: `G_Test_Astra_Experiment_Package/data/pilot_schedule.csv`
- Original SHA-256: `ab883fd0bbcfe091da226b8c8247a9220bbb3f1d24cc91c52d56f868a7f9039e`
- Public SHA-256: `ab883fd0bbcfe091da226b8c8247a9220bbb3f1d24cc91c52d56f868a7f9039e`
- Transformation: None; exact byte copy after privacy scan.

### data/compact_extension_schedule.csv

- Source: `G_Test_Astra_Experiment_Package/data/compact_extension_schedule.csv`
- Original SHA-256: `e2acd5b14c300ff6b1861cd967f83e72a6092a07cb35dc5958c35acd1bd89c38`
- Public SHA-256: `e2acd5b14c300ff6b1861cd967f83e72a6092a07cb35dc5958c35acd1bd89c38`
- Transformation: None; exact byte copy after privacy scan.

### protocol/Protocol_v3.0.0.md

- Source: `G_Test_Astra_Experiment_Package/Protocol.md`
- Original SHA-256: `7fd2319f7d8b1bbd4e7f6636bd4d3621486c9dbfe55689cc4f0a05f04b0e6be4`
- Public SHA-256: `7fd2319f7d8b1bbd4e7f6636bd4d3621486c9dbfe55689cc4f0a05f04b0e6be4`
- Transformation: None; exact byte copy after privacy scan.

### protocol/CHANGELOG.md

- Source: `G_Test_Astra_Experiment_Package/CHANGELOG.md`
- Original SHA-256: `f40b32dbce620b2e62defd81b06b214f91203157c73d4216d8baf7d52991f165`
- Public SHA-256: `f40b32dbce620b2e62defd81b06b214f91203157c73d4216d8baf7d52991f165`
- Transformation: None; exact byte copy after privacy scan.

### scoring/Rubric.md

- Source: `G_Test_Astra_Experiment_Package/Rubric.md`
- Original SHA-256: `428480f7d47eca4fec0902219da9fc793529bb785929720550bf51a566f87b2d`
- Public SHA-256: `428480f7d47eca4fec0902219da9fc793529bb785929720550bf51a566f87b2d`
- Transformation: None; exact byte copy after privacy scan.

### scoring/score.schema.json

- Source: `G_Test_Astra_Experiment_Package/schemas/score.schema.json`
- Original SHA-256: `8406859cd5fc1f26dda80e4261b9ff92bfdc09547c113230bf69a31aac7c095b`
- Public SHA-256: `8406859cd5fc1f26dda80e4261b9ff92bfdc09547c113230bf69a31aac7c095b`
- Transformation: None; exact byte copy after privacy scan.

### scoring/judge1_scores_fresh.jsonl

- Source: `G_Test_Analysis/judge1_scores_fresh.jsonl`
- Original SHA-256: `b6a71e546bda06fd22a8933ac5b4daadd7aff191aaf082171f1d84dc6fdd06ac`
- Public SHA-256: `b6a71e546bda06fd22a8933ac5b4daadd7aff191aaf082171f1d84dc6fdd06ac`
- Transformation: None; exact byte copy after privacy scan.

### scoring/judge2_repeat_audit_same_session.jsonl

- Source: `G_Test_Analysis/judge2_repeat_audit_same_session.jsonl`
- Original SHA-256: `dfa9f29051bb1b2bfe8ba07a24dc1620e8c35577766f4c8ee683837c9aa61cd4`
- Public SHA-256: `dfa9f29051bb1b2bfe8ba07a24dc1620e8c35577766f4c8ee683837c9aa61cd4`
- Transformation: None; exact byte copy after privacy scan.

### scoring/audit_agreement.csv

- Source: `G_Test_Analysis/audit_agreement.csv`
- Original SHA-256: `32209a0a57c0423e84ff90825dc92b743008abfabe29a5f05713590ff0ada9e3`
- Public SHA-256: `32209a0a57c0423e84ff90825dc92b743008abfabe29a5f05713590ff0ada9e3`
- Transformation: None; exact byte copy after privacy scan.

### results/scenario_summary.csv

- Source: `G_Test_Analysis/scenario_summary.csv`
- Original SHA-256: `40dd972d7c12925477ce27b2d12b161686c706a3bd4c66ea0916f3870ea3179c`
- Public SHA-256: `40dd972d7c12925477ce27b2d12b161686c706a3bd4c66ea0916f3870ea3179c`
- Transformation: None; exact byte copy after privacy scan.

### results/dimension_summary.csv

- Source: `G_Test_Analysis/dimension_summary.csv`
- Original SHA-256: `eed38248ce7a80f27d05327c81fff77cbf916997d77d42023a21d85c1fa8177e`
- Public SHA-256: `eed38248ce7a80f27d05327c81fff77cbf916997d77d42023a21d85c1fa8177e`
- Transformation: None; exact byte copy after privacy scan.

### results/statistical_summary.json

- Source: `G_Test_Analysis/statistical_summary.json`
- Original SHA-256: `9ac8e6beb81002241faa494020cfc2590d9bee6b1377b24b37d8d3635de71122`
- Public SHA-256: `9ac8e6beb81002241faa494020cfc2590d9bee6b1377b24b37d8d3635de71122`
- Transformation: None; exact byte copy after privacy scan.

### results/Final_Analysis_Report.md

- Source: `G_Test_Analysis/Final_Analysis_Report.md`
- Original SHA-256: `878c031701107943af370702fc6e3ceef9933b20c06d6dfabf714a8e42331048`
- Public SHA-256: `878c031701107943af370702fc6e3ceef9933b20c06d6dfabf714a8e42331048`
- Transformation: None; exact byte copy after privacy scan.

### integrity/Integrity_Audit.md

- Source: `G_Test_Analysis/Integrity_Audit.md`
- Original SHA-256: `82efd479f01eb039862bc0f6aa8adc69b9a0d155b9cfef663ead0a5b122aaf22`
- Public SHA-256: `82efd479f01eb039862bc0f6aa8adc69b9a0d155b9cfef663ead0a5b122aaf22`
- Transformation: None; exact byte copy after privacy scan.

### integrity/compact_raw_freeze_original.json

- Source: `G_Test_Astra_Experiment_Package/data/compact_raw_freeze.json`
- Original SHA-256: `a3f8b6a697331ba6303cd5c9b2df9fda250a68ca0d43303ef24c32d54aa89269`
- Public SHA-256: `a3f8b6a697331ba6303cd5c9b2df9fda250a68ca0d43303ef24c32d54aa89269`
- Transformation: None; exact byte copy after privacy scan.

### protocol/compact_dataset_plan.json

- Source: `G_Test_Astra_Experiment_Package/compact_dataset_plan.json`
- Original SHA-256: `11057f22dd0f0c3643abf67e96c0f4f3536cb6494c77d031f3f9b16cf6a180e1`
- Public SHA-256: `34c1c4858d0687e1e94e3db49c4780911c54f53fa35ec5f65dd07685b3211a9c`
- Transformation: Removed protected_hashes map for omitted private execution/legacy infrastructure. Retained all inclusion IDs, planned slots, design parameters, historical source digests and planned audit method. Relative source paths are historical, not public paths.

### scripts/validate_pairs.py

- Source: `G_Test_Astra_Experiment_Package/scripts/validate_pairs.py`
- Original SHA-256: `8f8299892de2fd8e06b44f82387b02f1dd1548770f3ff0c80274b7089289c0d9`
- Public SHA-256: `2429fc35919e7d7e491adfcb601cadd9db203531b31580606b8cfd30bc273717`
- Transformation: Only input path relocated from root test_cases.jsonl to data/test_cases.jsonl; pair-validation logic unchanged.

### integrity/collection_integrity_summary.md

- Source: `G_Test_Astra_Experiment_Package/reports/compact_collection_report.json`
- Original SHA-256: `ec969f347c84a8265a75db808a4760d990718eb7e850af334e9aca1af1adebb2`
- Public SHA-256: `d9f750b1bb2bbfcdd5e5627b4fc00f8487823f5c200e7e901157aa3368d846c8`
- Transformation: Public summary of existing collection counts/limitations. Omitted internal execution references and run-level runtime details; no outcome scoring or raw text changed.

## Review boundaries

Bibliographic metadata were checked against ACL Anthology and Springer publisher pages; references/references.json preserves exact URLs and the check date. No paper PDFs or author contact information are redistributed. Related literature is not a replication of this dataset.

Judge 2 used the same overall session, so it is not fully independent judge validation. The original finite bootstrap implementation/draw stream is missing; the portable implementation and its scope are disclosed. Eligible original research materials are dedicated under CC0 1.0 Universal, and original code is under MIT. Model-generated outputs are included as research data without additional restrictions imposed by the repository owner, subject to applicable external rights and law. These limitations remain visible at publication review.
