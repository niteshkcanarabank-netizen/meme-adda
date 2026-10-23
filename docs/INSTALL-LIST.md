# Gate 3 — Pinned Install List (APPROVED + INSTALLED)

> Status: **approved by nitesh 23 Oct 2026 (~20:43 IST) and installed the same
> evening. Gate 3 PASSED** — see the results log at the bottom of this file.
> Every entry was verified real on GitHub during the foundation research
> (see `research/tooling/`). Exact versions are frozen in `requirements.txt`
> — the install did not go past this list; adding anything later needs a
> fresh approval.

## Python packages (pip, one venv for the repo)

| Package | Pipeline stage | Why | Licence note |
|---|---|---|---|
| `praw` | intake | Reddit API wrapper — the trend-relay's template layer (r/IndianMemeTemplates etc.) | BSD-2 |
| `yt-dlp` | intake | YouTube metadata/trending pulls; no media downloading for production assets | Unlicense |
| `feedparser` | intake | Google Trends "Trending now" RSS (IN) scoring layer | BSD |
| `imagehash` | dedupe | Perceptual hashes for images (pHash) | BSD |
| `videohash` | dedupe | Perceptual hash for video assets | MIT |
| `faster-whisper` | build | Hinglish captions; fast local Whisper (CTranslate2) | MIT |
| `whisperx` | build | Word-level timestamps on top of Whisper → karaoke-style captions | BSD-2 |
| `moviepy` | build | Programmatic 9:16 assembly on top of ffmpeg | MIT |
| `Pillow` | build | Text/caption rendering, template composition | MIT-style (HPND) |

## System tools (already present on the build machine — no install)

- `ffmpeg` 8.1.2 — encoding, caption burn-in, audio
- `git` — the data audit trail

## Deliberately NOT on this list

- **Remotion** — excellent (66k★) but heavyweight Node stack and its own
  licence (not OSI); moviepy + ffmpeg covers v1. Revisit only if templated
  motion graphics become the bottleneck.
- **instaloader** — works, but Instagram ToS/ban risk on the main account;
  intake stays API/RSS-based.
- **snscrape / twint / pytrends** — verified dead, archived, or broken;
  pytrends is replaced by the Trends RSS feed.
- **MoneyPrinter-class generators** — components only, never foundations;
  nothing from them is installed without a separate audit.
- **memegen** — a hosted API/service pattern, not needed once moviepy +
  Pillow are in; template composition stays local.

## Install order (as executed)

1. `python3 -m venv .venv && pip install -r requirements.txt` (versions frozen at that moment)
2. Smoke tests per stage: intake dry-run (one subreddit, one Trends fetch) →
   dedupe self-test (hash the same file twice, expect identical) →
   caption test on a 15s sample → build test (one 9:16 render from an owned asset)
3. Results logged here; any failure stops the gate, it does not get worked around silently.

## Gate 3 results log — 23 Oct 2026

**Install:** venv at `.venv/` (2.9 GB, git-ignored). All nine approved packages
installed; exact versions frozen in `requirements.txt` (124 lines). Key versions:
praw 8.0.3 · yt-dlp 2026.10.21 · feedparser 6.0.14 · ImageHash 4.3.2 ·
videohash 3.0.1 · faster-whisper 1.2.1 · whisperx 3.8.6 · moviepy 2.2.1 ·
Pillow 11.3.0 · torch 2.8.0+cpu / torchaudio 2.8.0+cpu.

**Failure 1 (install):** the first attempt died mid-download of the stock
PyTorch wheel (888 MB) — this machine's `/tmp` is a 512 MB tmpfs
(`No space left on device`). Fix, applied openly: install temp moved to the
main disk (`TMPDIR=.pip-tmp/`) and PyTorch taken as the CPU build
(2.8.0+cpu) — this box has no GPU, so the CUDA build was dead weight.
Reinstall then completed clean.

**Smoke tests** (`pipeline/smoke_tests.py`, final run 21:12 IST — **8/8 PASS**):

| Test | Result |
|---|---|
| intake — Google Trends RSS (IN) | PASS — 10 trending entries fetched live |
| intake — praw import | PASS — 8.0.3 imports. **Caveat:** a live subreddit fetch needs Reddit app credentials (client id/secret) — an account step that stays with nitesh; not created for him |
| intake — yt-dlp import | PASS — 2026.10.21 |
| dedupe — imagehash | PASS — pHash identical across two runs of the same file |
| dedupe — videohash | PASS after fix 2 (below) — hash identical across two runs |
| captions — faster-whisper | PASS after fix 3 (below) — tiny model loaded and transcribed the test sample |
| captions — whisperx import | PASS |
| build — moviepy 9:16 render | PASS — rendered and ffprobe-verified at 1080×1920 |

**Failure 2 (videohash):** videohash 3.0.1 calls `PIL.Image.ANTIALIAS`, removed
in Pillow 10. Fix: `pipeline/compat.py` restores the alias to `LANCZOS` (what
ANTIALIAS always meant) before videohash is imported; used by the dedupe stage
and the smoke tests. Exact, documented, not silent.

**Failure 3 (faster-whisper):** faster-whisper 1.2.1 calls
`av.open(..., metadata_errors="ignore")`; the resolver had installed PyAV 19,
which dropped that argument. Fix: transitive dependency `av` pinned to
**16.0.0** in `requirements.txt` (noted inline there). No approved package
changed.

**Gate 3 verdict: PASSED.** Next is Gate 4 — the pilot: rights-logged assets
only, named human approver, dedupe + posting-verification tests — which needs
nitesh's approval before any production begins.
