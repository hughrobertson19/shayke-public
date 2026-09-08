# SHAYKEPUBLIC-README-3 — report

```
VERDICT
  LANDED, one commit on public/readme-3, not pushed, not merged. T1
  applied verbatim. T2 applied verbatim EXCEPT the trigger the dispatch
  itself defines: no generator in this repo writes `fleet_paused`, so the
  second census sentence ("`fleet_paused` at the top of the file is a
  real flag read from the runner, not a comment.") was deleted as
  instructed. Recorded under STOPPED. No founder switch; ran unattended
  to completion.

T0 SCOPE
  repo shayke-public; README.md only (+ this report per T5); one commit
  on public/readme-3; no push; no merge.

PRECONDITIONS (in order, all OK)
  1 branch main   2 clean   3 HEAD == origin/main @ 34abaec
  4 34abaec is ancestor   5 README-2 report present
  6 not landed ("Status, 8 Sep 2026" 0; commits 0)   7 no session.lock
  8 needle file readable, mode 600 (never read, never printed)
  9 ANTHROPIC_API_KEY absent.  Branch public/readme-3 created.

READ FIRST
  README.md as landed by README-2 @ 34abaec. fleet/census.json top-level
  keys: `fleet_paused` (true) and `running_count` (0) exist with those
  exact names; `registered_count` 42. scripts/verify_public.sh before
  and after: all 200, exit 0 both times.

CLASSIFY (each symptom line, with the command)
  grey badges unexplained     ledger/badges: eval "UNKNOWN" lightgrey,
                              tests "1/?/? @ 2026-09-04" lightgrey,
                              last_build 2026-09-05 blue, chain 19 blue;
                              no explanatory line on the page   CONFIRMED
  detail section repeats fold grep -c "public window" → 2;
                              grep -c "conflating them is how fleets
                              get oversold" → 2                  CONFIRMED
  T2 trigger check            grep -rn "fleet_paused" --include=*.py
                              --include=*.sh . → no match (exit 1).
                              Only fleet/census.json, fleet/README.md
                              and two dispatch reports mention it —
                              data and prose, not a generator. TRIGGERED
                              (Context, not evidence for the page: the
                              private producer in peak-ops does write
                              the field from the runner state; that is
                              not checkable from this repo, so the
                              sentence went.)

BUILT (README.md only)
  T1 status paragraph inserted verbatim after the fourth badge line,
     blank line either side, before the DEMO comment (README line 17).
  T2 "## What's in here, in detail" replaced verbatim from the heading to
     just before "## What I can say about the private side", with the
     census second sentence deleted per the trigger. The block is
     followed directly by "## What I can say about the private side".
  T3 Fold (above first badge), "Reading guide", "How it's wired", "Why I
     built this", "What I can say about the private side", "What this is
     not", "Licence": md5 of each section identical to main.

VERIFY (T4 output, pasted)
  grep -Eic -f ~/.shayke/public_needles.txt README.md      → 0
  grep -c "public window" README.md                        → 1
  grep -c "conflating them is how fleets get oversold"     → 1
  grep -c "Status, 8 Sep 2026" README.md                   → 1
  grep -c '```mermaid' README.md                           → 1
  grep -c '!\[demo\]' README.md                            → 0
  head -1 README.md                                        → # Shayke
  scripts/verify_public.sh                                 → exit 0
  Duplicate-sentence scan
    grep -v '^\s*$' README.md | sed 's/[*_`]//g' | sort | uniq -d
                                                           → (empty)
  Byte-for-byte (python substring vs heredoc files): T1 PRESENT
  (337 bytes), T2 PRESENT (1597 bytes, census sentence deleted);
  dropped sentence absent from the file.
  ACCEPTANCE: git diff --stat main..public/readme-3 → README.md and
  reports/dispatch/SHAYKEPUBLIC-README-3_report.md only;
  git log main..public/readme-3 --oneline | wc -l → 1.

TESTS
  Where the fake starts: at the reader, again. The checks prove the
  words are present and nothing repeats; whether a grey badge now reads
  as discipline rather than breakage is Hugh's played-it verdict on the
  rendered page after push, and it outranks this report.
  EVAL: UNKNOWN — no live-judge artefact is produced by this dispatch.

ARCH REVIEW
  n/a — prose only. Nothing outside README.md and this report touched.

WHAT HUGH NOW KNOWS
  Mechanism, in plain words: under the four badges there is now one
  italic, dated line that says why two of them are grey — the fleet is
  paused, the census file proves it, model calls are moving off the
  metered API — and that grey stays grey until a dated run changes it.
  The long-form section no longer restates the fold; it opens by saying
  it is the long form, then gives each folder one paragraph the fold
  does not already contain. One sentence claiming `fleet_paused` is
  "read from the runner" was dropped because nothing in this repo can
  show a reader that; the private producer does write it, and if that
  producer (or a note it emits) ever lands here, the sentence can
  return.
  PM concept: "explain the grey" — a dated status line turns an
  unexplained failure signal into evidence of discipline. A grey badge
  with no context reads as broken; the same badge with a dated reason
  and a rule for when it changes reads as someone who refuses to
  hand-upgrade their own status.
  Interview sentence: "I put a dated line under the grey badges saying
  exactly why they're grey and what would change them, and cut the
  section that repeated the top of the page — nothing on the page is
  upgraded by hand, and the page now says so."

BACKLOG RECOMMENDATION
  - The census producer (private) could emit a one-line provenance
    note into fleet/README.md ("fleet_paused is written from the runner
    state by <script> at <time>") so the dropped mechanism sentence
    becomes checkable here and can return.
  - The T1 line is dated 8 Sep 2026; it will read stale the day the
    fleet resumes. Whichever dispatch flips `fleet_paused` back should
    also own replacing or removing this paragraph — add that to the
    resume dispatch's tasks now, not later.
  - tests badge "1/?/? @ 2026-09-04": the "?" fields still have no
    explanation on the page or in ledger/README.md (carried from
    README-2 backlog).

COMMITS
  public/readme-3, one commit: "SHAYKEPUBLIC-README-3: dated status
  under the badges; detail section no longer repeats the fold" —
  README.md + reports/dispatch/SHAYKEPUBLIC-README-3_report.md.
  Not pushed. Not merged.

DESK ACTION (Hugh)
  The checkout is left on branch public/readme-3.
  - git checkout main && git merge --ff-only public/readme-3 && git push
    origin main (main has not moved since 34abaec; ff-only is safe).
  - Repo Settings → About: description "Shayke — a chat-first Sales
    Execution Cockpit for field sellers, and the agent fleet that builds
    it. Public build ledger: halts, corrections and costs included."
    Topics: forward-deployed, evals, sales-tech. Website blank until
    app.shayke.io exists.
  - "Why I built this" — parked, founder-owned, untouched here.
  - Root LICENSE file — separate founder-edited dispatch.

STOPPED / NOT DONE
  T2 census sentence deleted per the dispatch's own trigger: could not
  confirm from this repo that `fleet_paused` is produced by code (no
  .py/.sh in this repo references it). The census paragraph now ends at
  "the two status fields per agent." Nothing else outstanding. No push,
  no merge, no other file.
```
