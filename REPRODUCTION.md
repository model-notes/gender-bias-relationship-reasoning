# Reproduction and verification

Python 3.11+ and its standard library are sufficient. No installation, API credentials, model inference or network call is required.

The included `.gitattributes` disables automatic line-ending conversion so a future Git checkout preserves the bytes covered by the checksums.

From the public-release root:

```sh
python scripts/verify_release.py
python scripts/validate_pairs.py
```

The first command checks every public checksum (and exact file coverage), all 40 inclusion IDs/cells, exact prompt/response hashes, fixed model/effort metadata, score coverage, frozen AIx arithmetic, scenario and dimension summaries, direction and magnitude counts, exact1024-sign permutation p, repeat audit arithmetic, example quotes and relative Markdown links. It checks the saved bootstrap endpoints against the exact empirical scenario-resampling distribution as an arithmetic diagnostic. It prints a verification receipt and does not write or replace results.

The pair validator is the original validator with only its input path relocated. The public test-case file retains the full frozen 20-scenario/40-prompt bank; only the ten scenarios in the inclusion plan have collected responses. Twenty prompts does not mean twenty responses: each of the selected 20 prompts has two responses, total 40.

Optional, to check a transparent reconstruction of the prespecified finite bootstrap:

```sh
python scripts/verify_release.py --bootstrap
```

This uses `random.Random(20260914).choices`,100000 whole-scenario resamples of size 10 and linear-interpolated percentile endpoints. The statistical design is unchanged. The original analysis package did not preserve its RNG implementation or draw stream, so byte-for-byte identity of the original Monte Carlo execution is not claimed. The command compares its endpoints with the published interval, reports agreement/difference, and never updates the authoritative result.

`integrity/SHA256SUMS` paths are relative to the public root. On systems with sha256sum, `sha256sum -c integrity/SHA256SUMS` also checks bytes. The Python verifier additionally rejects unlisted files, excluding Git's local `.git` metadata so that verification also works in a future clone. The checksum file excludes itself; its digest is recorded in the private final-review report to avoid circular hashing.

## Source mapping

- `data/raw_responses.jsonl`: sanitized metadata derivative of the frozen combined raw JSONL; all 40 prompt and response strings are unchanged. Opaque experimental run IDs remain join keys; platform context IDs do not.
- `data/compact_inclusion_index.json`: unchanged inclusion IDs.
- `scoring/judge1_scores_fresh.jsonl`: authoritative40 final scores, exact copy.
- `scoring/judge2_repeat_audit_same_session.jsonl`: ten repeated scores, explicitly same-session.
- `results/`: exact source result tables and final report.
- `integrity/compact_raw_freeze_original.json` and the embedded freeze in statistical_summary.json refer to PRIVATE ORIGINAL JSONL serialization and historical paths. Those historical hashes are not the hashes of the sanitized public raw file. Use `integrity/public_freeze.json`, SHA256SUMS and the provenance mapping for the public representation.
- `protocol/compact_dataset_plan.json`: prospectively frozen inclusion/design content, with the private infrastructure protected-hash map omitted. Historical relative filenames remain provenance labels.

No collection or judging executable is distributed. The old200-run aggregation/collection scripts are not suitable for this mixed-version compact dataset and are omitted. Do not infer that the planned independent audit was completed: actual judging used the same overall session, as documented in the original Integrity_Audit.
