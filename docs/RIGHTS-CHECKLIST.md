# Rights checklist — per-clip clearance (mirrors the dub project's gate)

Fill this for every clip asset before it can enter a build. Record the answers in the
clip's `clip.json` rights block — the QA gate reads the JSON, not this file.

- [ ] **Origin recorded.** `self_shot | licensed_library | tv_film_clip | user_generated | other`,
      with detail (show/film name + scene, or library + licence ID) and `source_url`.
- [ ] **Rights status set.** One of: `cleared_original | cleared_licensed |
      transformative_fair_use_assessed | unassessed | blocked`. Default at intake:
      `unassessed`.
- [ ] **Content ID risk assessed.** `none | low | likely_claim | likely_block`, with an
      `assessment_note` grounded in `research/rights/` (what the research says about this
      source class, claim-vs-block expectation).
- [ ] **Assessor and timestamp recorded.** `assessed_by`, `assessed_at`.
- [ ] **Transformative claims are written.** If status is `transformative_fair_use_assessed`,
      the note must say *what* transforms the use (owned payoff, original edit structure,
      commentary) — never "probably fine".
- [ ] **Hard refusals.** `unassessed` or `blocked` → clip cannot enter a build, full stop.
      `likely_block` → job stops at the QA pre-check.
- [ ] **Claims on posted work logged.** If a post receives a Content ID claim, record it in
      the post record (`claims`) — the claim picture compounds into our own data over time.

Ruling that overrides everything above: unlicensed TV/movie clips are rejected as a
default format (ChatGPT, 23 Oct 2026). The two-clip format runs with an owned payoff only.
