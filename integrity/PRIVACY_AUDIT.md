# Public privacy and preservation audit

Date: 2026-10-01. Scope: all public files, every raw prompt/response string, source-to-public metadata projection, and excluded private artifact classes.

Checks cover local account names and absolute paths; email patterns; API/GitHub/JWT/private-key patterns; secret assignments; environment assignments; platform session/context UUIDs; forbidden runtime metadata fields; archive/binary/cache inclusion; and exact preservation of all 40 prompt/response strings. Credentials were not opened from account stores. No remote upload was performed.

All raw strings passed the pattern screen without redaction. The structured metadata projection removed internal context IDs, PIDs, directories, timings and runtime data before public output. Published opaque experiment run IDs are intentional join keys, not platform session IDs. Scholarly author names and the user-specified proposed GitHub account are intentional public-facing attribution, not leaked account credentials.

Pattern scanning cannot prove the absence of every possible personal reference or novel secret format. The dataset consists of constructed unnamed scenarios; no identifiable subject/person data were observed in the inspected material. Internal runtime logs and configuration were excluded entirely rather than relying on redaction.

Preservation checks compare all 40 public prompt/response strings and their SHA-256 values with the authoritative private source, and verify every published original/derivative digest. The exact artifact inventory is FILE_INVENTORY.md. `integrity/SHA256SUMS` covers every public file except itself; the private final-review report records its digest.

Final automated result and any findings are recorded below after executing the check. Licensing was finalized separately at the user's direction; this privacy audit does not provide legal advice.

## Executed checks

- Pattern/known-context-ID findings: **0**.
- Original-to-public prompt strings: **40/40 exact**.
- Original-to-public response strings: **40/40 exact**.
- Source-derived artifact provenance hashes: **21/21 verified**.
- Original recovered baseline: **1018/1018 unchanged**.
- No forbidden binaries, archives, credential stores, runtime logs or cache folders included.
- Existing scores/results are preserved; no new judging or inference.
- Status: **PASS within the stated scan scope; licensing finalized; publication identity and release checks remain required**.
