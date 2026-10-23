# Meme Adda — Research Leg: Trend Sourcing + Verified GitHub Tooling Shortlist

**Date:** 23 October 2026 · **Scope:** foundation research only. Nothing installed, nothing downloaded beyond reading pages.
**Method (Part 2):** every repo below was verified live on 23 Oct 2026 via the GitHub CLI (`gh repo view`, GitHub API) against its real github.com page. Star counts, licences and last-push dates are as returned that day. A repo that could not be resolved does **not** appear in the shortlist — see the Rejected section.
**Method (Part 1):** web research plus established platform facts. Lead times are labelled **[evidence]** where a source states them, **[inference]** where they are my estimate from how the platforms behave — treat inference as planning guidance, not measurement.

---

## Part 1 — Trend sourcing: where Indian/Hinglish meme trends surface first

The Indian meme ecosystem is a relay, not a single source. The observed pattern (multiple listicles and Know Your Meme origin entries agree): a moment or joke surfaces on **X/Twitter or Reddit**, gets templated by template accounts, is then industrialised by big Instagram pages (RVCJ, Ghantaa, Trolls Official class), and only later shows up as Reels/Shorts volume and Google search spikes. WhatsApp forwards are a huge distribution layer but are effectively unmonitorable. One creator quoted in the Tamil-memes literature puts it plainly: on Twitter a meme on a trending topic gets reach; Instagram spreads it friends-of-friends.

### The trend-watch list

| # | Source | What surfaces there | Typical lead time before peak | How a pipeline monitors it |
|---|--------|--------------------|-------------------------------|----------------------------|
| 1 | **X (Twitter) India — trends list + cricket/Bollywood/news hashtags** | The fastest public signal in India. Match moments, breaking news, TV episodes and celebrity posts become memes *during* the event (e.g. IPL matches produce meme-fests on X in real time; Wasim Jaffer's IPL 2020 run shows even players' accounts seeding templates). | Minutes to ~2 hours ahead of Instagram/Reels versions **[inference]** | Poll India trends (X trends UI; third-party trackers trends24.in / getdaytrends keep 24h history), plus a watchlist of high-velocity meme accounts. Tools: see snscrape / twitter-api-client caveats in Part 2(d). |
| 2 | **Reddit — r/IndianDankMemes, r/indiameme, r/IndianMeyMeys, r/desimemes, r/bollywoodmemes, r/IndianMemeTemplates, r/JEENEETards** | Template *origination* and "template wars". r/IndianDankMemes is repeatedly described as the underground source mainstream pages lift from; r/IndianMemeTemplates exists specifically to publish clean templates (Know Your Meme documents template accounts posting usable templates within ~3 days of a format appearing — e.g. @InMemeTemplates on X, 5 May 2023 for a format born 2 May 2023). Exam-season communities (r/JEENEETards) generate highly shareable Hinglish formats. | ~1–3 days ahead of peak Instagram/Reels saturation **[inference, anchored on the KYM template-lag example]** | PRAW (Part 2d) polling "rising" + "hot" sorts on the listed subs every 30–60 min; alert when a post crosses velocity thresholds. |
| 3 | **Instagram — originator/aggregator pages (RVCJ Media, Ghantaa, Trolls Official, Sarcasm-class pages) + Reels audio pages** | Where formats get polished, captioned in Hinglish, and scaled. Ghantaa reportedly posts 20–30 memes/day — that volume makes these pages a confirmation signal, not the earliest one. Trending Reels *audio* also surfaces here first for sound-led formats. | Lags X/Reddit by hours to ~1 day; leads YouTube Shorts by ~0–2 days **[inference]** | Instaloader (Part 2d) on a fixed watchlist of ~15–25 pages; track new posts + Reel audio reuse counts manually. ToS risk — see caveats. |
| 4 | **Live TV / streaming moments (IPL & India cricket, Bigg Boss, Taarak Mehta reruns, Bollywood releases, reality shows)** | The raw material itself: a dialogue, reaction shot or commentary line (the Ravi Shastri "g…ti moo me tha" moment is still being remixed years later). This is the desi equivalent of Patna Pulse's news watch — the *event calendar* is the watch list. | Zero lead time — the moment **is** the start; the race is who templates it first (minutes) **[evidence: live-match meme coverage]** | Maintain an events calendar (IPL/fixtures, Bigg Boss season, big film releases, India matches, Budget day, exam results). Monitor sources 1–2 hardest during those windows. Clip-sourcing has rights/Content ID implications — covered by the formats leg, not this one. |
| 5 | **YouTube — Trending (IN) tab + Shorts feed + meme-compilation channels** | Confirms which formats have crossed into video. Compilation/reactor channels (Tanmay Bhat's Reddit-react format) surface Reddit material to a mass audience — a late-stage amplifier and a good "what already peaked" check. | Lags the origin by ~1–3 days **[inference]** | yt-dlp (Part 2d) against the IN trending feed and a channel watchlist; rising Shorts using the same audio = format still climbing. |
| 6 | **Google Trends — "Trending now" (geo=IN) + RSS feed** | Search-demand confirmation: tells you a topic has escaped social media into the general public. Google states Trending Now refreshes **on average every 10 minutes** and detects ~10× more emerging trends than the old system; the India RSS feed (`trends.google.com/trending/rss?geo=IN`) is machine-readable **[evidence: Google Trends Help + Search Central docs]**. | Confirmation, not origin: typically hours behind X, but the best *kill/keep* signal — if search interest is still "Active" and rising, the window is open | Poll the RSS feed every 15–30 min; join against the trend-watch DB to score topics. Prefer RSS over pytrends (archived — Part 2d). |
| 7 | **Know Your Meme (knowyourmeme.com)** | Post-hoc origin documentation: which post started a format, when, and its spread path (its Indian entries cite exact origin tweets/dates). | Days behind — verification layer, not detection **[evidence: KYM entry structure]** | Manual/API check before adopting a format: confirms the template's origin and age, so we don't ship a format that's already at saturation. |
| 8 | **WhatsApp forwards / Telegram mirror channels** | A major *distribution* layer in India (e.g. Telegram channels auto-mirror r/IndianDankMemes etc.). Mostly closed/encrypted — treat as a symptom, not a source. | Unmeasurable | Do not build monitoring here. Public Telegram mirrors of the Reddit subs are a cheap secondary feed if Reddit access breaks. |

### Practical reading of the map

- **Earliest actionable signals: X India trends + Reddit rising queues.** A trend watch that only looks at Instagram is structurally 1–2 days late. **[inference]**
- **The desi calendar is a source, not a backdrop.** IPL season, Bigg Boss, exam results (JEE/NEET/UPSC), festivals, Budget day and big Bollywood releases are predictable meme factories — schedule monitoring intensity around them.
- **Google Trends RSS is the scoring layer**: origin signals (X/Reddit) say "something is moving"; Trends says whether the general public cares yet — that gap is the production window.

---

## Part 2 — Verified GitHub tooling shortlist

Star counts and last-push dates as verified 23 Oct 2026 via `gh`. "Role" = what it would do in the Meme Adda pipeline (trend dashboard → production builders → dedupe, mirroring the Patna Pulse shape).

### (a) Meme / template databases & generators

| Repo | Stars | Last push | Licence | Role in pipeline |
|------|-------|-----------|---------|------------------|
| [jacebrowning/memegen](https://github.com/jacebrowning/memegen) | 1,755 | 2026-10-20 | MIT | The memegen.link engine: self-hostable API that renders text onto a large built-in template library. Our fastest path to template-based image memes with correct top/bottom text layout. |
| [D3vd/Meme_Api](https://github.com/D3vd/Meme_Api) | 889 | 2023-05-19 | MIT | REST API serving random memes (largely Reddit-sourced). Useful as a *reference/monitoring* feed for what formats are circulating; stale (no push since 2023) — do not build production on it. |
| [voxmedia/meme](https://github.com/voxmedia/meme) | 1,993 | 2022-03-15 | BSD-3-Clause | Browser-based meme generator (Vox Media). Unmaintained; of interest only as a reference implementation for an in-browser template editor. |
| [schesa/ImgFlip575K_Dataset](https://github.com/schesa/ImgFlip575K_Dataset) | 82 | 2022-11-04 | None stated | Dataset of ~575K Imgflip memes with template IDs/captions. A *template-popularity dataset* for ranking which templates historically travel — research input only, and the missing licence means no redistribution. |

### (b) Programmatic video assembly

| Repo | Stars | Last push | Licence | Role in pipeline |
|------|-------|-----------|---------|------------------|
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | 66,430 | 2026-10-22 | "Other" (Remotion's own licence — free for small teams, paid company licence at scale; **not OSI open source**) | React-based programmatic video: the strongest option for templated, data-driven Shorts/Reels (text overlays, two-clip layouts) with frame-accurate control. Licence must be checked against our use before adoption. |
| [Zulko/moviepy](https://github.com/Zulko/moviepy) | 15,016 | 2026-08-26 | MIT | Python video editing (ffmpeg underneath): clip trimming, concatenation, text overlays, compositing. The pragmatic default builder for a Python pipeline. |
| [kkroening/ffmpeg-python](https://github.com/kkroening/ffmpeg-python) | 11,011 | 2024-08-04 | Apache-2.0 | Python bindings for ffmpeg filter graphs — the low-level layer for caption burn-in, scaling to 9:16, loudness normalisation. Slow-moving but stable/mature. |
| [WyattBlue/auto-editor](https://github.com/WyattBlue/auto-editor) | 5,596 | 2026-10-22 | Unlicense | Automatic silence/dead-space cutting and speed-ramping — ideal for cutting TV/show clips down to the funny 8 seconds in a "connect the dots" two-clip format. |
| [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 134,298 | 2026-10-22 | MIT | End-to-end AI short-video generator (script → stock footage → TTS → captions → render). Extremely popular; useful as a reference architecture and for its caption/render plumbing. **Caution:** built for faceless AI-content farms — we would borrow components, not adopt its content model; audit before any use. |
| [gyoridavid/short-video-maker](https://github.com/gyoridavid/short-video-maker) | 1,427 | 2025-06-21 | MIT | MCP/REST service that assembles Shorts/Reels from scenes + TTS + captions. Interesting because its MCP interface matches an agent-driven pipeline like ours. |
| [RayVentura/ShortGPT](https://github.com/RayVentura/ShortGPT) | 8,061 | 2025-02-10 | MIT | Experimental Shorts automation framework (scripting + editing engines). Slowing maintenance; reference only. |
| [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | 32,174 | 2026-09-15 | AGPL-3.0 | Automated short-form content bot. AGPL copyleft + "make money online" framing make it a poor foundation; listed for completeness, **not recommended**. |

### (c) Auto-captions / subtitles

| Repo | Stars | Last push | Licence | Role in pipeline |
|------|-------|-----------|---------|------------------|
| [openai/whisper](https://github.com/openai/whisper) | 111,093 | 2026-08-31 | MIT | The reference speech-to-text model. Handles Hindi/Hinglish code-switching better than most; generates the base transcript + SRT for every clip. |
| [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) | 26,064 | 2026-10-16 | MIT | CTranslate2 re-implementation of Whisper — up to ~4× faster, less memory. The production transcription engine on a CPU-only box (our VM constraint). |
| [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp) | 54,573 | 2026-10-19 | MIT | Whisper in C/C++ — fastest CPU inference, no Python dependency. Alternative engine if faster-whisper is too heavy. (Repo moved from ggerganov to the ggml-org org; old links redirect.) |
| [m-bain/whisperX](https://github.com/m-bain/whisperX) | 24,786 | 2026-10-22 | BSD-2-Clause | Whisper + forced alignment → **word-level timestamps** (and diarisation). This is what makes karaoke-style word-by-word burned captions — the dominant Shorts/Reels caption look — possible. |
| [SubtitleEdit/subtitleedit](https://github.com/SubtitleEdit/subtitleedit) | 14,681 | 2026-10-22 | MIT | Full subtitle editor/format converter (300+ formats), CLI-capable. The utility belt for SRT/VTT/ASS fixing, timing shifts and format conversion before burn-in via ffmpeg. |
| [jianfch/stable-ts](https://github.com/jianfch/stable-ts) | 2,281 | 2026-05-30 | MIT | Stabilised word timestamps for Whisper. **Repo is archived** — usable as-is (it still works) but unmaintained; whisperX covers the same need actively. |

### (d) Trend trackers / social listening

| Repo | Stars | Last push | Licence | Role in pipeline | Status |
|------|-------|-----------|---------|------------------|--------|
| [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 200,498 | 2026-10-21 | Unlicense | YouTube monitoring (trending feeds, channel uploads, metadata) and reference-clip retrieval for internal analysis. | Active — the reliable workhorse. |
| [instaloader/instaloader](https://github.com/instaloader/instaloader) | 13,653 | 2026-10-21 | MIT | Instagram watchlist monitoring (posts/Reels metadata from originator pages). | Active, but Instagram rate-limits/bans aggressively and scraping breaches Meta ToS — account-risk decision needed before use. |
| [praw-dev/praw](https://github.com/praw-dev/praw) | 4,288 | 2026-10-22 | BSD-2-Clause | Official-API Reddit client — the clean way to poll r/IndianDankMemes et al. "rising" queues (needs Reddit API credentials; rate-limited but sanctioned). | Active — **the recommended Reddit route**. |
| [JustAnotherArchivist/snscrape](https://github.com/JustAnotherArchivist/snscrape) | 5,466 | 2023-11-15 | GPL-3.0 | X/Twitter scraping without API keys. | Effectively broken for X since the 2023 login-wall changes; no push since Nov 2023. Historical interest only. |
| [trevorhobenshield/twitter-api-client](https://github.com/trevorhobenshield/twitter-api-client) | 1,899 | 2024-05-22 | MIT | X GraphQL client via logged-in account cookies. | Fragile and ToS-risky; last push May 2024. Fallback only, with eyes open. |
| [GeneralMills/pytrends](https://github.com/GeneralMills/pytrends) | 3,727 | 2024-08-10 | Other | Unofficial Google Trends API. | **Archived by the owner.** Superseded for us by the official Trends RSS feed (Part 1, source 6). |
| [twintproject/twint](https://github.com/twintproject/twint) | 16,405 | 2023-02-23 | MIT | Twitter scraping/OSINT. | **Archived and dead** (X killed the endpoints it used). Do not plan around it despite the star count. |

**Honest gap:** there is no healthy open-source X/Twitter firehose anymore. The realistic X-monitoring options are (i) the paid official X API, (ii) fragile cookie-based clients, or (iii) third-party trend-history sites (trends24.in class) polled as web pages. The trend dashboard design should assume Reddit + Google Trends RSS + YouTube as the dependable automated feeds, with X as a semi-manual watch.

### (e) Dedupe — perceptual hashing

| Repo | Stars | Last push | Licence | Role in pipeline |
|------|-------|-----------|---------|------------------|
| [JohannesBuchner/imagehash](https://github.com/JohannesBuchner/imagehash) | 3,882 | 2026-10-12 | BSD-2-Clause | The standard Python perceptual hashing library (pHash, dHash, aHash, wHash). Dedupes template images and near-identical stills; the core of our "have we already posted this template?" check. |
| [akamhy/videohash](https://github.com/akamhy/videohash) | 386 | 2024-07-12 | MIT | 64-bit perceptual hash for whole videos → near-duplicate video detection. Directly serves the dedupe step for clips (e.g. the same show clip recut by five pages). Small, slow-moving, single-purpose — fine for its job. |
| [arsenetar/dupeguru](https://github.com/arsenetar/dupeguru) | 7,921 | 2026-09-07 | GPL-3.0 | Fuzzy duplicate-file finder (incl. picture mode with perceptual similarity). Good for cleaning the local asset library (downloaded clips/templates) rather than in-pipeline checks. |
| [facebook/ThreatExchange](https://github.com/facebook/ThreatExchange) | 1,402 | 2026-10-22 | Other (BSD-style for PDQ components — verify per-file) | Meta's trust-&-safety repo containing **PDQ**, the perceptual hash designed for video/frame matching at platform scale. The heavy-duty option if videohash proves too weak against cropped/re-captioned reposts. |

### Rejected / unverifiable candidates (3)

These were checked on 23 Oct 2026 and **failed verification** — they do not exist at the stated address, so they are excluded from the shortlist:

| Candidate as cited | Result | Note |
|--------------------|--------|------|
| `D3vd/MemeApi` | GitHub API: "Could not resolve to a Repository" | The real repo is `D3vd/Meme_Api` (underscore) — verified and listed above. A good example of why exact-name verification matters. |
| `DanCRichards/meme-generator` | GitHub API: "Could not resolve to a Repository" | No repo at this address. |
| `memeapi/memeapi` | GitHub API: "Could not resolve to a Repository" | Plausible-sounding but does not exist. |

Verified-but-dead tools (twint, pytrends, snscrape-for-X) are **not** in this rejected list — they exist, so they're in the shortlist with explicit dead/archived flags rather than silently dropped.

---

## Caveats that apply to the whole leg

1. **Scraping ≠ permission.** Instaloader, snscrape-class tools and cookie-based X clients breach platform ToS to varying degrees and carry account-ban risk. PRAW (official API) and Google Trends RSS are the sanctioned routes.
2. **Trend detection ≠ rights clearance.** Nothing here speaks to Content ID/claims on TV/movie clips — that is the formats leg's question; this leg only maps *when* moments surface and *what tools* can watch/build/dedupe.
3. **Star counts are a popularity signal, not a quality audit.** No code was cloned or run for this leg (per scope); maintenance status above is inferred from push dates and archive flags only.

## Sources

- Google Trends Help — "Explore the searches that are Trending now" (refresh ~every 10 minutes; RSS export): https://support.google.com/trends/answer/3076011?hl=en
- Google Search Central — Google Trends documentation (Trending Now vs Explore): https://developers.google.com/search/docs/monitor-debug/trends-start
- Google Trends India RSS feed: https://trends.google.com/trending/rss?geo=IN
- Know Your Meme — "Indian Robert Pattinson" (origin-to-template timeline, May 2023): https://knowyourmeme.com/memes/indian-robert-pattinson
- Innfinity — "Indian Meme Pages That Literally Defined Our Internet Culture" (RVCJ/Ghantaa/Trolls Official/r/IndianDankMemes roles): https://innfinity.in/indian-meme-pages-that-defined-internet/
- Wisden — Wasim Jaffer's IPL Twitter meme run (live-match meme origination): https://www.wisden.com/series/indian-premier-league-2020/cricket-news/wait-when-did-wasim-jaffer-get-so-good-at-twitter
- GummySearch — r/IndianDankMemes stats & related subreddits (r/IndianMemeTemplates etc.): https://gummysearch.com/r/IndianDankMemes/
- All Part 2 repo facts: GitHub API via `gh repo view`, 23 Oct 2026.
