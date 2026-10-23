# Workflow — the pipeline in plain language

Eight stages. Each record's `status` field is the single source of where it stands.

## 1. Trend intake
Watchers (manual at v1) drop raw finds into `data/trends/<date>/<trend_id>.json`:
source URL, capture time, a velocity note, and — the trend-watch edge — **where it
surfaced first**, not just where it is already big. Statuses: `new | shortlisted |
in_production | posted | expired | rejected`.

## 2. Dedupe
Every trend item and every finished production gets a perceptual hash (thumbnail/frame
pHash is the v1 minimum; audio fingerprint where cheap). Near-duplicates cluster under
one `cluster_id`. Runs **twice**: at intake (don't chase the same trend under two links)
and before posting (don't post a near-copy of our own earlier post or of the source we
adapted). Cut-offs live in `config/thresholds.yaml`, not in code.

## 3. Template / clip selection
A shortlisted trend is matched to a template from `library/templates/`. Clips are
pulled from `library/clips/` or newly ingested as clip assets. New clips enter with
rights status **`unassessed`** — selection may proceed, **building may not**.

## 4. QA gate — rights check (BEFORE build)
- Every clip in the job has a completed rights block; none is `unassessed` or `blocked`.
- `content_id_risk` recorded per clip; `likely_block` stops the job, `likely_claim`
  proceeds only with the assessment note on file.
- Result written to the job's `rights_precheck`.
- **A failed pre-check means the build stage refuses the job** — not a warning, a refusal.

## 5. Build
The builder assembles the export to the template spec (9:16, 1080×1920, captions
burned in, premise text on frame 1) into `productions/<job_id>/out/final.mp4`, and
writes the post-build pHash for the second dedupe pass.

## 6. QA gate — output check
Spec compliance (dimensions, duration, audio present), caption legibility, brand
elements, caption text + hashtags present. Pass/fail recorded in `qa-report.md`;
fail returns the job to build.

## 7. Posting (v1: assisted-manual)
A human performs the platform steps from `docs/POSTING-RUNBOOK.md` and records the
result. Creates the post record with `live_url` and `verification.status: pending`.
API automation is a later phase, after research validates what's permitted.

## 8. Verification + metrics pull
Verification per the two hard rules (see README). Metrics (views, likes, comments,
shares where exposed) pulled at 24h / 72h / 7d into `data/metrics/<date>.json`, keyed
by `post_id` — feeding the dashboard and each template's `performance_note`.
