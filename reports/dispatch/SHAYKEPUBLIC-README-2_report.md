# SHAYKEPUBLIC-README-2 — report

```
VERDICT
  LANDED, one commit on public/readme-2, not pushed, not merged. Every
  task T1–T9 applied. One T8 line needed a founder ruling: the verbatim
  T1 block is 200 words by `wc -w` (193 excluding em-dashes) against a
  stated cap of ≤170. Hugh ruled in-session (2026-09-08): keep the block
  as written, cap amended to ≤200. Founder switch for T1: VARIANT A
  (field), stated by Hugh in-session.

T0 SCOPE
  repo shayke-public; files in scope README.md only (+ this report, per
  T9); one commit; no push.

PRECONDITIONS (in order, all OK)
  1 branch main   2 clean tree   3 HEAD == origin/main @ 00a3f8e
  4 00a3f8e is ancestor   5 SHAYKEPUBLIC-BUILD-1 commits: 2
  6 README-2 not landed (README 0, commits 0)   7 no session.lock
  8 needle file readable, mode 600 (never read, never printed)
  9 ANTHROPIC_API_KEY absent from env.  Branch public/readme-2 created.

CLASSIFY (each symptom line confirmed against the file before editing)
  title is the repo slug        head -3 → "# shayke-public"         CONFIRMED
  first paragraph fleet-first   head -3 → "An agent fleet that…"    CONFIRMED
  two grey UNKNOWN badges       ledger/badges/eval.json UNKNOWN,
                                lightgrey; tests.json
                                "1/?/? @ 2026-09-04", lightgrey    CONFIRMED
  demo.gif broken image         wc -c docs/demo.gif → 42            CONFIRMED
  fleet org chart above fold    mermaid fence at line 15 (1 fence)  CONFIRMED
  CI claim contradicts ruling   grep -n "runs green in CI" → 56     CONFIRMED
  READ FIRST resolve: scripts/verify-shayke-public.sh does not exist;
  the file is scripts/verify_public.sh (curls the raw README, four badge
  endpoints, docs/demo.gif, profile repo). Run before and after: all 200,
  exit 0 both times. fleet/census.json: fleet_paused=true,
  registered_count=42, running_count=0. Badges: last_build 2026-09-05
  blue; tests "1/?/? @ 2026-09-04" lightgrey; eval UNKNOWN lightgrey;
  chain 19 blue — none changed.

BUILT (README.md only)
  T1 block applied verbatim at byte 0, VARIANT A ("a field seller").
  T2 four badge lines byte-identical, directly after the T1 block.
  T3 `![demo](docs/demo.gif)` deleted; the dated DEMO HTML comment kept
     verbatim. docs/demo.gif itself untouched (out of scope).
  T4 "## Reading guide" inserted after the DEMO comment, before
     "## How it's wired". All artefacts it names exist: docs/pilot_runbook.md,
     docs/success_metric.md, docs/data_flow.md, docs/persona_findings.md,
     lib/quotable_span/, ledger/. No clause removed.
  T5 "- The eval harness runs green in CI with live scoring." replaced
     verbatim with the hermetic-CI / UNKNOWN-badge line.
  T6 spend-breaker sentence untouched; nothing appended.
  T7 "## What's actually in here" → "## What's in here, in detail"; no
     other edit in that section.

VERIFY (T8 output, pasted)
  grep -Eic -f ~/.shayke/public_needles.txt README.md  → 0
  wc -w, text above first badge line (line 13)         → 200
      (cap ≤170 in the dispatch; the verbatim T1 block alone is 200;
       Hugh ruled 2026-09-08: accept, cap amended to ≤200)
  grep -c '!\[demo\]' README.md                        → 0
  grep -c "runs green in CI" README.md                 → 0
  head -1 README.md                                    → # Shayke
  grep -c '```mermaid' README.md                       → 1
  scripts/verify_public.sh (after)                     → exit 0, all 200
  Byte-for-byte: T1, T4, T5 written to heredoc files and checked as
  exact substrings of README.md in Python — T1 PRESENT (1209 bytes,
  starts at byte 0), T4 PRESENT (517 bytes), T5 PRESENT (223 bytes).
  ACCEPTANCE: git diff --stat main..public/readme-2 → README.md and
  reports/dispatch/SHAYKEPUBLIC-README-2_report.md only;
  git log main..public/readme-2 --oneline | wc -l → 1.

TESTS
  Where the fake starts: at the reader. The checks above prove the
  required words are present and the forbidden ones absent; none proves
  a hiring manager understands the product in 20 seconds. That is Hugh's
  played-it verdict on the rendered GitHub page after push, and it
  outranks this report.
  EVAL: UNKNOWN — no live-judge artefact is produced by this dispatch.

ARCH REVIEW
  n/a — prose only. No code, JSON, badge, script or licence state
  touched.

WHAT HUGH NOW KNOWS
  Mechanism, in plain words: the first screen now runs what → why →
  how-to-check. One bold sentence says what the product is and that it
  never runs the call; three numbered lines point at the three folders a
  stranger can verify in a minute; one line says who built it. The
  badges follow, then a reading guide that routes an engineer, a product
  reader and a sceptic to different files. The fleet chart, which used to
  be the first thing after the badges, is now below that guide. The one
  claim that overstated CI now says exactly where hermetic checks run
  and where live gates run, and that the eval badge stays UNKNOWN until
  a dated artefact exists.
  PM concept: above-the-fold hierarchy — a reader gives a page seconds,
  so the order of the first screen is the product decision: what it is,
  why it matters, how to check it, in that order, and nothing else
  before the fold.
  Interview sentence: "I re-cut the README so the first screen says what
  the product is and gives three things a stranger can verify in a
  minute, and corrected the one claim that overstated CI to say exactly
  where the live gates run."

BACKLOG RECOMMENDATION
  - Dispatch template: count the verbatim block with `wc -w` before
    setting a word cap; the T1 block and the ≤170 cap could not both
    hold.
  - F-20260827-04 names scripts/verify-shayke-public.sh; the file is
    scripts/verify_public.sh. Correct the reference.
  - The tests badge reads "1/?/? @ 2026-09-04" in grey: the "?" fields
    are a producer gap; one line on ledger/README.md explaining them
    would stop a reader guessing.
  - Repo About/Description and Topics, and the root LICENSE file, are
    desk actions below — the README's licence section already says the
    all-rights-reserved-except-quotable_span position.

COMMITS
  public/readme-2, one commit: "SHAYKEPUBLIC-README-2: product above the
  fold, reading guide, CI claim corrected, gif placeholder removed" —
  README.md + reports/dispatch/SHAYKEPUBLIC-README-2_report.md.
  Not pushed. Not merged.

DESK ACTION (Hugh)
  - Merge public/readme-2 → main (Desktop diff, Accept), push, then the
    played-it read on github.com: does the first screen say what it is in
    one breath?
  - Repo Settings → About → Description: "Shayke — a chat-first sales
    execution cockpit for sellers, and the agent fleet that builds it.
    Public build ledger: halts, corrections and costs included." Topics:
    add forward-deployed, evals, sales-tech.
  - Root LICENSE file (all-rights-reserved-except-lib/quotable_span):
    separate dispatch, founder-edited.

STOPPED / NOT DONE
  Nothing outstanding from TASKS. One deviation, ruled: T8 word cap
  170 → 200 (block kept verbatim). No push, no merge, no other file.
```
