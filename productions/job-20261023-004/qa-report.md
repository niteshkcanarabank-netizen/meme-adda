# QA Report — Pilot Variants (jobs 002 / 003 / 004)

Built: 23 Oct 2026 ~22:35 IST · Builder: `pipeline/build/build_variants.py`
Trigger: nitesh's fix on job-20261023-001 — add a credited movie/TV reference;
"try everyone then we will decide".

| Check | 002 Hera Pheri | 003 Taarak Mehta | 004 Panchayat |
|---|---|---|---|
| Dimensions 1080×1920 | PASS | PASS | PASS |
| Duration 12–35 s (17.0 s) | PASS | PASS | PASS |
| Premise on frame 1 | PASS (same setup as job-001) | PASS | PASS |
| Reference still shown with slow zoom | PASS | PASS | PASS |
| Credit burned into video | PASS | PASS (auto-fit fix applied after first frame review caught clipping) | PASS |
| Credit in post caption | PASS | PASS | PASS |
| Post caption ends with a question | PASS | PASS | PASS |
| Rights logged before build | PASS — clip-20261023-004/005/006, `transformative_fair_use_assessed`, assessment note + founder decision recorded, `content_id_risk: likely_claim` | PASS | PASS |
| Dedupe hashes logged | PASS (`data/hashes/2026-10-23.json`) | PASS | PASS |

Notes:
- Frame-1 pHash is identical across all four jobs by design (shared setup
  scene) — recorded, not a collision.
- The reference stills' image binaries stay local (git-ignored); the clip.json
  records carry the audit trail, source URLs and credit lines.
- Credit is attribution, not a licence — the records say so. Nothing posts:
  Meme Adda accounts do not exist yet and nitesh's variant decision is pending.

Honest limits: stills are modest resolution (700–1366 px wide) upscaled into
the frame; flat code-drawn animation and synth audio, same as job-001.

## Amendment — 23 Oct 2026 ~23:40 IST (founder instructions)

1. Bhaiya redrawn (character v2): swept fringe hair, arched brows, open
   smile — v1's bowl-cut/stick-brow face replaced in every scene.
2. Credit placement changed: NO credit inside the video (the earlier
   "credit burned in" row above is superseded). The credit now appears
   only as the closing line of the post description (job.json post_caption).
All four videos (job-001 + variants) rebuilt with both changes; hashes re-logged.
