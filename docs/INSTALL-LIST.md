# Gate 3 — Pinned Install List (PROPOSED)

> Status: **proposed 23 Oct 2026, awaiting nitesh's approval.** Nothing on this
> list has been installed. Every entry was verified real on GitHub during the
> foundation research (see `research/tooling/`). At install time, exact versions
> are frozen into `requirements.txt` (pip) — the install does not proceed past
> this list; adding anything later needs a fresh approval.

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

## Install order (when Gate 3 is approved)

1. `python3 -m venv .venv && pip install -r requirements.txt` (versions frozen at that moment)
2. Smoke tests per stage: intake dry-run (one subreddit, one Trends fetch) →
   dedupe self-test (hash the same file twice, expect identical) →
   caption test on a 15s sample → build test (one 9:16 render from an owned asset)
3. Results logged here; any failure stops the gate, it does not get worked around silently.
