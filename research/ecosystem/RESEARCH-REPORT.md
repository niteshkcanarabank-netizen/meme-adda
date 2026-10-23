# Meme Adda — Foundation Research Report

**Date:** 23 Oct 2026 · **Status:** Research phase complete. Production remains PAUSED.
**Sequence (ChatGPT, incharge — binding):** Research → GitHub → install → production. No installs and no production until the gates below pass.
**Legs:** `partners-round.md` · `ecosystem-leg.md` · `formats-contentid-leg.md` · `trends-tooling-leg.md` · `repo-design-leg.md`

---

## 1. Partner roll-call

- **ChatGPT (incharge) — ANSWERED.** Approved the restart sequence as binding, set hard evidence standards for every research area, and defined the four gates (§6). Full ruling verbatim in `partners-round.md`.
- **Gemini (auditor) — SILENT.** Attempt 1: HTTP 503 (model high demand). Attempt 2: timeout after ~93s. Not a gate, per standing practice; the rights facts were instead built from official YouTube/Meta sources directly.
- **Grok (intel) — DARK.** One permitted attempt returned no answer text (credits). Trend evidence comes from the trends leg's inspectable sources instead.
- **Fo — NO LIVE ROUTE** in this setup. Nothing simulated.
- **Muse — coordination + all five research legs.**

## 2. The ecosystem (sample: 14 web searches, ~150 IG/FB posts sampled directly, 2 channels inspected first-hand, ~40 accounts named, 12 in depth)

Three competitor tiers:

1. **IG/FB meme-page networks** — RVCJ Media (~13M IG / ~15M FB), Sarcasm (~10–13M), Trolls Official (~11.7M), Ghantaa (~7.4–9M). They post **20–30 times/day** and monetise through brand deals, not platform revenue. *(Audience figures are approximate ranges — sources disagreed by millions on the same page.)*
2. **Legacy YouTube sketch stars** — Round2hell (~31–36M), Ashish Chanchlani (~30M), BB Ki Vines (~26M). They won on **recurring characters and series**; their verified hits are series instalments (*School Life Part-2* 142M views, *Aladdin* 127M, *Dhindora EP01* 84M).
3. **Shorts-native channels** — e.g. Real Fools Shorts Official (~52.9M subs, ~19.8B views) doing near-silent village slapstick; plus a long tail of clip-compilation channels carrying the rights exposure examined in §4.

**What travels:** recognition. TV/Bollywood clip templates (Taarak Mehta/Jethalal is the richest vein), relatable desi-life situations, cricket (IPL is a seasonal super-spike), festival cycles, and viral sounds/catchphrases — where the travelling unit is often a *re-performed parody audio*, not the film clip. The biggest mechanics are participatory (comments continue the joke). WhatsApp forwards are the real distribution layer; "this is us" is the forwarding trigger.

**Language:** Hinglish online is **Roman script** — 93.17% of code-mixed posts by native Hindi speakers vs 2.93% Devanagari (2014 study); YouTube comments split 52% Romanised Hindi / 46% English / 1% Devanagari. Hinglish preference is rising (Nature 2024); Hindi posts diffuse furthest across regions (ShareChat, 1.2M posts); ~85% of Indian short-video consumption is in Hindi/other Indian languages, comedy is the No. 1 Shorts category for Gen Z (FICCI–EY).

**Strategic read:** the volume game (20–30 posts/day, staffed networks) is not winnable for a small operation. The open lane is **original, character-led Hinglish short-form at 1–2 strong posts/day**.

## 3. Formats that travel

- **Two-clip "connect the dots" — REAL and widespread** in Indian/Hinglish Reels: a setup cuts to a famous reaction (Baburao/*Hera Pheri* repeatedly in the sample) and the juxtaposition is the joke. Sampled outcomes ranged ~14 to ~15K likes: the format guarantees *legibility*, not reach. Its rights problem is §4 — the fix is in §7.
- **Original multi-role sketches/re-enactments drew the strongest engagement in the sample** (~96K and ~220K likes on two posts) — directional only (50-post, query-biased sample; views/shares mostly unavailable).
- **POV text-overlay sketches** are a strong fully-owned format (premise in frame 1).
- **Templates travel by replication-with-modification** (peer-reviewed study of 2M Reddit memes): the durable asset is the comic grammar, not the same protected clip reposted.
- **Lifespans (secondary sources, labelled as such):** sounds ~3–7 days, formats ~2–4 weeks, event trends peak in 1–2 weeks. YouTube officially states Shorts discovery does not favour a format — retention and satisfaction decide.

## 4. Content ID / rights — the facts (official YouTube + Meta sources; detail in `formats-contentid-leg.md`)

- **There is no safe number of seconds.** Content ID matches segments; the rights holder's policy decides block / monetise / track, per territory. Short, edited, or credited clips get no exemption.
- **Claims ≠ strikes.** Claims do not accumulate into termination. A formal takedown = a strike; **3 strikes in 90 days can terminate the account and associated channels**. Disputing a weak claim can escalate it into a takedown.
- **Shorts rule:** a Short **over 1 minute with any active claim is blocked globally** — unplayable, unrecommended, not monetisation-eligible (no channel penalty for the block itself). Under 1 minute, the claimant's normal policy applies.
- **Channel-level risk beyond copyright:** a channel built mainly on repurposed clips can lose monetisation under YouTube's **reused-content** policy. Meta separately penalises **limited-originality** content and *expressly names* stitching clips together, adding captions/borders, or minor edits as unoriginal — reduced distribution, non-recommendability, demonetisation. Meta's Rights Manager/IP system can restrict repeat-infringer accounts.
- **Highest exposure:** Bollywood scenes/songs/trailers, Indian TV-serial scenes and dialogue, broadcast/sports clips, other creators' videos as payoff clips, compilations with captions as the only addition. YRF's own FAQ prohibits third-party publishing of YRF content outright.
- **Law:** Indian fair dealing (s.52(1)(a)) covers private use, criticism/review, reporting current events — **no verified general meme/parody safe harbour**. US fair use is case-by-case and is not decided by Content ID.
- **Comparatively safe:** original footage/scripts/performances/music; original re-enactments that don't reproduce protected dialogue/music line-for-line; properly licensed clips (licence covering asset, platform, territory, term, editing, monetisation); YouTube Audio Library and in-tool Remix audio; verified public domain (checking film, performance, and music layers separately).

**ChatGPT's stance (incharge, strict):** building on unlicensed TV/movie clips is **rejected as a default format**. The two-clip format is a **conditional test only** — and the research conclusion sharpens it: keep the two-clip joke, but shoot the payoff (original acted reaction or a recurring owned character) instead of downloading it.

## 5. Trend sourcing + tooling

**The trend relay (earliest first):** X India (minutes–~2h lead; inference) → Reddit template subs — r/IndianDankMemes, r/indiameme, r/IndianMeyMeys, r/desimemes, r/bollywoodmemes, **r/IndianMemeTemplates**, r/JEENEETards (~1–3 days ahead of saturation; inference) → Instagram originator pages (hours–1 day lag) → the **live-event calendar** (IPL, Bigg Boss, releases, exam results — the desi equivalent of a news watch) → YouTube Trending IN (confirmation, 1–3 day lag) → Google Trends "Trending now" IN + RSS (refreshes ~every 10 min per Google; the scoring layer) → Know Your Meme (origin verification). WhatsApp is distribution, not a source. **Honest gap:** no healthy open-source X firehose exists — automate Reddit (official API) + Trends RSS + YouTube; keep X semi-manual.

**Verified GitHub shortlist** (every repo opened and checked live via GitHub on 23 Oct 2026; stars as shown — full table with licences/activity in `trends-tooling-leg.md`):
- Meme/templates: `jacebrowning/memegen` (1,755★), `D3vd/Meme_Api` (889★, stale), `voxmedia/meme` (1,993★, unmaintained)
- Video assembly: `remotion-dev/remotion` (66,430★; Remotion licence, not OSI), `Zulko/moviepy` (15,016★), `kkroening/ffmpeg-python` (11,011★), `WyattBlue/auto-editor` (5,596★), `gyoridavid/short-video-maker` (1,427★)
- Captions: `openai/whisper` (111,093★), `SYSTRAN/faster-whisper` (26,064★), `m-bain/whisperX` (24,786★ — word-level timestamps for karaoke captions)
- Trend/data: `yt-dlp/yt-dlp` (200,498★), `praw-dev/praw` (4,288★ — the recommended Reddit route), `instaloader/instaloader` (13,653★; ToS risk flagged)
- Dedupe: `JohannesBuchner/imagehash` (3,882★), `akamhy/videohash` (386★), Meta's PDQ inside `facebook/ThreatExchange` (1,402★)
- **Rejected as non-existent (3):** `D3vd/MemeApi`, `DanCRichards/meme-generator`, `memeapi/memeapi` — none resolve. **Verified but dead/archived (kept, flagged):** twint, pytrends (use Trends RSS instead), snscrape (broken for X). MoneyPrinter-class repos are components-only/audit-first, not foundations.

## 6. The GitHub foundation — and one flag

**⚠️ "patna-pulse" was not found anywhere**: no directory or doc in the workspace, and the GitHub account holds exactly three repos (cocos-copy-colour-books, hindi-dubbed-short-dramas, video-link-directory) — `patna-pulse` returns 404. The design in `repo-design-leg.md` is therefore built from the five named components, borrowing conventions from the two real production repos. If patna-pulse lives under another name or account, point us at it and the design gets re-diffed against the real thing.

**Design headline:** `config/` · `research/` · `data/` (trends/posts/metrics as versioned JSON — git is the audit trail, no database at v1) · `library/` (templates + clips) · `pipeline/` (intake → **dedupe** → select → **rights QA gate** → build → post → verify) · `productions/<job_id>/` · `dashboard/` · `docs/`. Date-scoped IDs (`tr-`, `tpl-`, `clip-`, `job-`, `post-`) thread trend → job → post. Every clip asset carries a **mandatory rights block** (status enum + Content ID risk); `unassessed` is the default and bars the clip from any build — a failed rights pre-check makes the build stage *refuse*, not warn. **Verified posting** is defined concretely: a post counts as done only when its live URL is recorded AND checked as a logged-out viewer, playing, on the correct account, with the evidence written to the post record; unverified >2h is a dashboard failure. Dashboard v1 = four panels generated from the JSON into static HTML (the colouring-books pattern).

## 7. What this means — the founding shape the research supports

1. **Original, character-led Hinglish comedy** (recurring owned characters/series — the tier-2 lesson), Roman-script captions, premise in frame 1.
2. **Two-clip grammar, owned payoff:** setup + our own acted reaction/character — the format survives, the Content ID exposure doesn't.
3. **Cadence 1–2 strong posts/day**, timed to the trend relay and the event calendar — not a 20-post volume war.
4. **Every asset rights-logged before build**; nothing unassessed ever renders.

## 8. Gates (ChatGPT's ruling — production restarts only through these)

1. **Research verified** — this report.
2. **GitHub foundation approved** — the meme-adda repo built to the design in §6.
3. **Install limited to a pinned approved list** drawn from §5's verified shortlist — nothing else gets installed.
4. **Production restart** — rights-logged assets only, a human approver on the pilot, dedupe + posting-verification tested, pilot approved before cadence begins.

**Open item for nitesh:** where does patna-pulse actually live? (Not in this workspace or your GitHub.) One pointer from you and the design is re-checked against it before Gate 2.
