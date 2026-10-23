# Posting runbook — assisted-manual v1

A human performs the platform steps below for each job that reaches `qa_passed`.
No posting automation exists at v1 — this runbook is the automation.

## Before posting
1. Open the job folder `productions/<job_id>/`: confirm `qa-report.md` shows
   `qa_passed` and `rights_precheck.passed: true` in `job.json`.
2. Confirm the export `out/final.mp4` plays end-to-end (audio present, captions legible).
3. Have the caption (ends with a question), 3–5 hashtags, and template notes ready.

## Posting steps (per platform)
1. Upload `final.mp4` to the platform as the brand account (`config/channels.yaml`).
2. Paste caption + hashtags. Do not alter the premise/caption pairing without updating
   the job record — caption text is part of the QA'd asset.
3. Publish. Note the exact publish time (IST).

## Recording the post (immediately)
1. Create `data/posts/<post_id>.json` per the schema: `job_id`, platform, account handle,
   `posted_at`, and the **`live_url`**.
2. Set `verification.status: pending`. The post does NOT count as done yet.

## Verification (within 2 hours — this is the definition of "posted")
1. Open the `live_url` **as a logged-out/public viewer** — not from inside the posting
   account's studio/dashboard, which can show videos that aren't actually public yet.
2. Confirm: correct account, correct video, status public/live (not processing, private,
   or removed), video plays.
3. Write `verification.checked_at` and a one-line `evidence` note into the post record.
   Set status `verified_live` or `failed`.
4. Record any Content ID claim or restriction visible at check time under `claims`.
5. If still `pending` after 2 hours: treat as a failure to chase — check the platform's
   verification/processing steps (a "Verify that it's you" modal, a policy hold) and
   record what you found. This is why the Minor Panic batch-1 uploads taught us the
   distinction: an upload can sit behind platform verification and "posted" can silently
   not be true.

## After verification
- Schedule the metrics pulls (24h / 72h / 7d) into `data/metrics/<date>.json`.
- Regenerate the dashboard: `python3 dashboard/build_dashboard.py`.
