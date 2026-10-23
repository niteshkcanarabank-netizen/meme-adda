# Pipeline stages

Scripts that run each stage live in their own folder. Each stage reads the
previous stage's records and writes its own; a record's `status` field is the
single source of where it stands.

| Folder | Stage | Reads | Writes |
|---|---|---|---|
| `intake/` | 1. Trend intake | `config/sources.yaml`, raw finds | `data/trends/<date>/<trend_id>.json` |
| `dedupe/` | 2. Dedupe | trend items, finished productions | `dedupe.cluster_id` on records, `data/hashes/` index |
| `select/` | 3. Template/clip selection | shortlisted trends, `library/` | template/clip links on the trend or new job |
| `build/` | 5. Build | job + template spec | `productions/<job_id>/out/final.mp4` |
| `qa/` | 4 + 6. QA gates | job + clips + export | `rights_precheck`, `qa-report.md` |
| `post/` | 7. Posting | `qa_passed` jobs | `data/posts/<post_id>.json` |
| `verify/` | 8. Verification + metrics | `pending` posts | `verification` block, `data/metrics/<date>.json` |

Stage 4 (rights QA) lives in `qa/` but runs **before** `build/`: the build script must
refuse any job whose `rights_precheck.passed` is not true. Dedupe runs twice
(intake and pre-posting) — both live in `dedupe/`.

Conventions: one script per job where a script exists (`intake_trends.py`,
`hash_media.py`, …); thresholds from `config/thresholds.yaml`, never hardcoded.
