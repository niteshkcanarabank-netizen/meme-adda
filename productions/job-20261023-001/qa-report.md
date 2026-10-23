# QA report — job-20261023-001 (Gate 4 pilot)

## Rights pre-check (stage 4, ran BEFORE build) — PASS
- clip-20261023-001 (setup visual, self-drawn code): `cleared_original`, Content ID risk none
- clip-20261023-002 (payoff visual, self-drawn code): `cleared_original`, risk none — the
  two-clip payoff is OWNED, per the ChatGPT ruling in `config/rights-policy.md`
- clip-20261023-003 (audio bed + SFX, numpy synthesis): `cleared_original`, risk none
- No `unassessed`/`blocked` asset in the job; nothing third-party enters the build.

## Output QA (stage 6) — PASS
- Dimensions 1080×1920 (ffprobe) — meets `qa_output.min_resolution`
- Duration 14.5s — inside the 12–35s band
- Audio present (AAC, synthesised bed + pops + sting)
- Premise on frame 1 — verified visually: "Salary aayi… aur gayab?"
- On-screen text legible at phone size; two overflow defects found in review
  (phone SMS text, AUTO-PAY chip) and fixed before this pass — frames re-checked
- Captions: pilot is text-led (no voice track); the on-screen Hinglish text IS the
  caption layer, burned in per template spec
- Post caption ends with a question ✓ · hashtags 4 (band 3–5) ✓
- End card present: "MEME ADDA — roz ka adda, roz ka meme."

## Dedupe (post-build pass)
- Frame-1 pHash `b868c73638c91bc7`, videohash recorded in `data/hashes/2026-10-23.json`
- Near-duplicates in index: none

## Honest limits
- Flat code-drawn animation; character is a simple PIL drawing, not motion-captured acting
- No human voice — text-led by design for the pilot
- Nothing is posted: Meme Adda accounts don't exist yet (account creation is
  nitesh's step), and posting additionally waits on his approver verdict below

## Approver
- Human approver: nitesh — verdict pending (approve / fix / reject recorded in job.json)
