# QA Report — Real-footage cut (job-20261023-005)

Built: 23 Oct 2026 ~23:58 IST · Builder: `pipeline/build/build_real_cut.sh`
Trigger: founder direction — replace the drawn character with real videos/images.

| Check | Result |
|---|---|
| Dimensions 1080×1920, duration 17.0 s | PASS |
| Premise on frame 1 ("Salary aayi… aur gayab?") | PASS |
| Real footage: smiling man + phone (0–5 s), empty wallet (10.5–13.5 s) | PASS |
| Panchayat reference beat kept (5–10.5 s) | PASS |
| No drawn character anywhere; end card is text only | PASS |
| No credit inside the video; credit in description (job.json) | PASS |
| Rights logged before build | PASS — clips 007/008 `cleared_licensed` (Pexels License), clip-006 as before |
| Dedupe hash logged | PASS (`data/hashes/2026-10-23.json`) |

Caught on frame review and fixed before delivery: bash printf mangled the
Unicode text files (the headline rendered "aayiu2026", stamps "u2713").
Text files are now written via python3 UTF-8; stamps repositioned as three
separate chips inside the frame. Re-verified on the rebuilt file.

Honest limits: the setup clip is 720×1280 upscaled to 1080 wide; the two
stock actors differ (setup man vs wallet hands — hands only, reads fine);
synth music bed unchanged from the pilot.
