# 3.0.0 — Compact quota-constrained design (2026-09-14)

Reason: solely an external Astra compute/quota constraint, prospectively authorized by the user before their stated outcome inspection/analysis. No score values or response semantics informed selection. Archive final2.0.0 unchanged, preserve16 raw rows and old schedule, include them through a separate plan, add only six explicitly requested scenarios (24 responses), total40/N10. New extension seed20260914; original seed731942 unchanged. Prespecify compact scenario-level sign-flip test and low-resolution bootstrap; no formal subgroup tests. Freeze all experimental content, AIx/weights, schemas, thresholds, gender conditions and technical exclusions unchanged. Reuse unchanged subject isolation and PASS canaries. Preserve/classify prior judging for audit and exclude it from final independent Sol scoring. Replace pilot scoring gate with collection-integrity validation; collect, freeze, report, STOP. No200-run collection.

# Controlled protocol changelog

## 2.0.0 — 2026-09-13, before experimental collection

The preceding package was unversioned; its exact bytes and manifest are archived in `revisions/unversioned_baseline/`. At revision time there were zero experimental runs. Earlier neutral readiness probes are not pilot data.

User-authorized infrastructure changes only:
- Judge 1 and Judge 2: exact `gpt-5.6-sol`, high reasoning, because generic `gpt-5.6` was rejected by the ChatGPT CLI. Judge workflow, scoring rubric and weights unchanged. Validator remains separate and may use the available exact member of its previously preferred GPT-5.6 family.
- Subject remains `gpt-6-astra/medium`; every call uses a new CLI 0.154.0 process/context in a neutral empty directory outside the experiment.
- Standard Codex context is permitted; experimental task content is only the exact prompt. Replaced the private subject instruction with a constant content-neutral no-tools/no-files instruction, removing experiment-related wording.
- Observable isolation requires fresh contexts, no experiment material in available dumps and zero tool/file calls in telemetry. Hidden runtime context and unexposed backend metadata are disclosed limitations rather than automatic failures.
- Added execution/capture/validation support and frozen its hashes before the pilot. Run IDs are opaque to avoid condition metadata in judge inputs; each is linked to the unchanged scheduled ID. This implements existing blinding without changing randomization.
- Execute only the 16-run pilot and its scoring/audit, then stop.

Unchanged byte-for-byte: test_cases.jsonl, Rubric.md, both score/run schemas, pair validator, schedule generator, aggregation script and existing pilot schedule. No change to AIx, statistical thresholds, seeds, exclusion rules or analysis design. Exact protected-file hashes and authorization record are in protocol_revision.json.

### Resume completion — 2026-09-14, still zero experimental runs

Per the explicit resume request, finished revision 2.0.0 before pilot collection. Archived the preceding 23-file freeze and its preflight in `revisions/2.0.0_pre_resume/`. Added manifest continuity checks against the recorded freeze, passed preflight and raw-data freeze; strengthened case-insensitive context-leak checks; added explicit resume/independent-validator gates; and stop for capture audit if multiple native response messages appear, preserving telemetry rather than accepting a fabricated combined response. Updated README judge-model references and added README/TestCases.md to manifest coverage. No protected design content or pilot schedule was edited. New canary/preflight records are separate and append-only; previous successful records remain archived.
