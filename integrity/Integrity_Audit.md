# Integrity audit

- Protocol: **3.0.0**.
- Included raw runs: **40/40 valid** across 10 scenarios, exactly 2 A + 2 B per scenario.
- Unique run IDs: **40**; unique subject thread/context IDs: **40**.
- Requested subject configuration: `gpt-6-astra`, reasoning `medium` for all 40.
- Tool calls: **0**. Isolation status: **verified** for all 40 according to stored harness checks.
- Exact prompt hashes and response hashes: verified for all 40.
- Every stored prompt exactly matches the frozen `test_cases.jsonl` condition.
- Frozen raw SHA-256 values in `data/compact_raw_freeze.json`: all verified.
- `MANIFEST.sha256`: 37 entries verified, 0 mismatches, 0 missing.
- `reports/COMPACT_DATA.sha256`: 296 entries verified, 0 mismatches, 0 missing.
- Resolved backend model/version and resolved reasoning effort are not exposed in the stored telemetry; the requested configuration and CLI controls are what can be verified.

## Post-collection judging limitation

The fresh scoring in this analysis was performed by GPT-5.6 Sol using the frozen rubric and a seeded randomized run order, without displaying counterpart scores during run-level scoring. However, all 40 scores were produced within this single ChatGPT conversation/session, not 40 platform-isolated judge contexts. The planned 10-run audit was repeated separately in a second randomized pass, but still in the same GPT-5.6 Sol session. Therefore the collection protocol passed, while the ideal independent-Judge-2 requirement is **not fully satisfied** by this analysis.
