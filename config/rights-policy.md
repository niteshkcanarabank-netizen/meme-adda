# Rights policy — the rules the QA gate enforces

Binding rulings and facts (foundation research, 23 Oct 2026; see `research/rights/`):

1. **Unlicensed TV/movie clips are REJECTED as a default format.** (ChatGPT ruling,
   partners round, 23 Oct 2026.) They may not be the library's bread-and-butter source.
2. **The two-clip "connect the dots" format is a conditional test with an OWNED payoff.**
   Keep the setup→reaction grammar, but the payoff clip must be shot ourselves
   (owned character) or come from a cleared-licensed library asset.
3. **No safe number of seconds.** Content ID matching is not governed by a duration
   threshold; assume any recognisable clip can match.
4. **Claims are not strikes — but 3 real takedowns in 90 days kills a channel.** A
   claimed Short over 1 minute gets blocked worldwide. Clip-built channels risk losing
   monetisation under YouTube's reused-content policy. Meta's limited-originality
   policy names clip-stitching + captions as unoriginal content.
5. **No Indian meme/parody safe harbour exists.** Do not assume fair-use-style cover.

Per-clip rules (enforced at the QA gate, stage 4, before any build):

- Every clip carries a completed rights block. Status values:
  `cleared_original | cleared_licensed | transformative_fair_use_assessed | unassessed | blocked`
- `unassessed` is the intake default. **Nothing with `unassessed` or `blocked` may enter a build.**
- `transformative_fair_use_assessed` requires a written `assessment_note` grounded in
  `research/rights/` — a recorded decision, not a hope.
- `content_id_risk: likely_block` stops the job. `likely_claim` proceeds only with the
  assessment note on file and the claim expectation recorded in the post record later.

Rights QA sits BEFORE build deliberately: no edit time is spent on an asset that
can't ship.

## Founder decision — credited references in the Gate-4 pilot (23 Oct 2026)

nitesh (founder) directed that the Gate-4 pilot test a credited movie/TV
reference (still frame), trying three candidates before he decides. This
overrules the incharge's owned-payoff-only position **for the pilot test only**.
The default format rule above stands unless he rules otherwise after seeing
the variants. Every such reference is logged `transformative_fair_use_assessed`
with a written assessment and `content_id_risk: likely_claim` — credit is
attribution, not a licence, and the record says so.

**Credit placement (founder instruction, 23 Oct 2026 ~23:35 IST): never inside
reels or shorts — the credit goes in the post description only** (the closing
line of the job's `post_caption`).
