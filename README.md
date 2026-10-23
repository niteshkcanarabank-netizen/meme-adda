# Meme Adda

Indian/Hinglish memes for YouTube Shorts + Instagram Reels.
Trend watch → dedupe → build → QA (rights first) → post → verify.

> **Status (23 Oct 2026): Gate 2 — APPROVED by nitesh and pushed to GitHub.**
> Repo: https://github.com/niteshkcanarabank-netizen/meme-adda — built from the
> repo-design leg of the foundation research (`research/`). Nothing here installs
> anything; the pinned install list is Gate 3 (`docs/INSTALL-LIST.md`, proposed).

## Pipeline at a glance

1. **Intake** — trend finds normalised into `data/trends/<date>/<trend_id>.json`
2. **Dedupe** — perceptual hash at intake and again before posting (`config/thresholds.yaml`)
3. **Select** — trend matched to a template; clips enter the library with rights `unassessed`
4. **QA gate (rights)** — hard gate BEFORE build; failed pre-check = build refuses, not warns
5. **Build** — 9:16 export, 1080×1920, captions burned in, premise on frame 1
6. **QA gate (output)** — spec + caption + brand checks; pass/fail in `qa-report.md`
7. **Posting** — v1 is assisted-manual from `docs/POSTING-RUNBOOK.md`
8. **Verify** — live URL checked as a logged-out viewer; pending > 2h = failure to chase

Full detail: `docs/WORKFLOW.md`.

## Repo map

| Path | What |
|---|---|
| `config/` | channels, trend sources, dedupe/QA thresholds, rights policy (no secrets) |
| `research/` | foundation research legs (ecosystem, formats, rights, tooling) |
| `data/` | trends, posts, metrics, hash index — JSON, versioned in git |
| `library/` | templates and clip assets (each with ID-named JSON) |
| `pipeline/` | stage folders with the scripts that run each stage |
| `productions/` | per-job working folders (`<job_id>/`: job.json, script.md, out/, qa-report.md) |
| `dashboard/` | `build_dashboard.py` → static `site/` (GitHub Pages-ready) |
| `docs/` | workflow, rights checklist, posting runbook |

IDs: `tr-YYYYMMDD-NNN`, `tpl-<slug>`, `clip-YYYYMMDD-NNN`, `job-YYYYMMDD-NNN`, `post-YYYYMMDD-NNN`.

## The two hard rules

1. **No build without a passed rights pre-check.** Clips with rights status `unassessed` or `blocked` never enter a build.
2. **No post counts as done until its live URL is verified and recorded** — opened as a logged-out viewer, video plays, correct account, public status.

## Dashboard

Regenerated from `data/` by `dashboard/build_dashboard.py` → `dashboard/site/index.html`.
Host on GitHub Pages once the repo is created.

## Research

Foundation research (23 Oct 2026): `research/ecosystem/`, `research/formats/`, `research/rights/`, `research/tooling/`.

## Gates (programme sequence)

- Gate 1 — research ✅ complete 23 Oct 2026
- Gate 2 — this repo (draft; needs nitesh's approval + GitHub creation) ⬅ we are here
- Gate 3 — pinned install list (only what the research validates)
- Gate 4 — pilot with rights-logged assets + human approver
