# SHAYKEPUBLIC-README-4 — report

```
VERDICT
  LANDED, one commit on public/readme-4, not pushed, not merged. T1 and
  T2 a–j applied by script (python str.replace with an assert that each
  OLD occurs exactly once), every NEW present exactly once, every OLD
  absent. Em dashes 11 → 0. No founder switch; ran unattended.

T0 SCOPE
  repo shayke-public; README.md only (+ this report per T5); one commit
  on public/readme-4; no push; no merge.

PRECONDITIONS (in order, all OK)
  1 branch main   2 clean   3 HEAD == origin/main @ edb8da8
  4 edb8da8 is ancestor   5 README-3 report present
  6 not landed ("People buy from people" 0; commits 0)   7 no session.lock
  8 needle file readable, mode 600 (never read, never printed)
  9 ANTHROPIC_API_KEY absent
  10 baseline: em dashes 11 (expected 11); spaced-hyphen lines 0.
  Branch public/readme-4 created.

CLASSIFY
  narrative understates       README:52 begins "I came to this from
                              selling, not from engineering. Five months"
                              — contains "Not long", "smaller sales role"
                                                               CONFIRMED
  11 em dashes, all README-2/3 grep -n '—' → lines 7, 8, 9, 18 (×2), 25,
                              58, 60, 62, 64, 71 = 11; every one inside
                              text introduced by README-2 or README-3
                                                               CONFIRMED
  spaced hyphens as dashes    grep -c ' - \| -- ' → 0 at baseline
  scripts/verify_public.sh before: all 200, exit 0.

BUILT (README.md only)
  T1  narrative paragraph (one line, 52) replaced by the three supplied
      paragraphs, blank line between, byte for byte.
  T2  a–j applied exactly as given: a, b, c (fold list; b also
      hash-chained → hash chained), d (status line, two dashes → two
      sentences), e (reading guide), f, g, h, i (detail section),
      j (private-side CI line). Each OLD found once; each NEW now once.
  T2k remaining hyphens checked: stroke-dasharray (mermaid, code),
      shields endpoint URLs (code), Chat-first / phone-first (fold,
      README-2 verbatim), adversarial-persona / data-flow (reading
      guide, README-2 verbatim), fixed-cost (status line, README-3
      verbatim). All hyphenated compounds or code, none a spaced dash;
      left as the rule says. `per-field` does not appear.
  T3  Fold apart from a–c, badges, diagram, "What this is not",
      "Licence": untouched. Section md5 vs main: "How it's wired",
      "What this is not", "Licence" identical; "Reading guide", "What's
      in here, in detail", "What I can say about the private side"
      differ only by the listed substrings (20 changed lines total in
      the diff, all accounted for by T1 + T2).

VERIFY (T4 pasted; precondition-10 baseline → after)
  grep -o '—' README.md | wc -l                       → 0   (was 11)
  grep -c ' - \| -- ' README.md                       → 0   (was 0; no
                                                          hit inside the
                                                          mermaid fence)
  grep -Eic -f ~/.shayke/public_needles.txt README.md → 0
  grep -c "People buy from people" README.md          → 1
  grep -c "Five months" README.md                     → 0
  grep -c "Not long" README.md                        → 0
  grep -c '```mermaid' README.md                      → 1
  head -1 README.md                                   → # Shayke
  scripts/verify_public.sh (after)                    → exit 0, all 200
  Duplicate-sentence scan
    grep -v '^\s*$' README.md | sed 's/[*_`]//g' | sort | uniq -d
                                                      → (empty)
  T1 NEW present byte for byte (count 1); each T2 NEW exactly once;
  each T2 OLD absent — asserted by the script, re-checked after write.
  ACCEPTANCE: git diff --stat main..public/readme-4 → README.md
  (+15/−11) and reports/dispatch/SHAYKEPUBLIC-README-4_report.md only;
  git log main..public/readme-4 --oneline | wc -l → 1.

TESTS
  Where the fake starts: at the reader. The checks prove the founder's
  text landed and the dashes left; whether the paragraph now reads as
  someone worth calling is Hugh's played-it verdict on the phone after
  push, and it outranks this report.
  EVAL: UNKNOWN — no live-judge artefact is produced by this dispatch.

ARCH REVIEW
  n/a — prose only. Nothing outside README.md and this report touched.

WHAT HUGH NOW KNOWS
  Mechanism, in plain words: nothing on the page was drafted here. Every
  change was an exact-match replacement — the old string had to occur
  exactly once or the script stopped, the new string was written in its
  place, and afterwards each new string was counted once and each old
  string zero times. That is how you edit a public page without
  drafting on it: the founder supplies every character, the executor
  supplies only the count assertions.
  PM concept: a founder narrative is a claim about the founder and gets
  the same evidence discipline as a product claim. "Division I at
  Illinois", "seven years as a police officer", "outside sales for a
  start up" are checkable facts about a person, stated in that person's
  words, and they replace a paragraph that hedged ("Not long", "smaller
  sales role") — hedging on a page that elsewhere refuses to hedge read
  as a different author.
  Interview sentence: "I replaced the founder story with my own words
  and stripped every dash off the page by exact-match substitution with
  count assertions, so the public README carries nothing an executor
  drafted."

BACKLOG RECOMMENDATION
  - The em-dash and spaced-hyphen greps belong in scripts/verify_public.sh
    (or a small style check) so README-2/3 cannot reintroduce them; the
    house style is now a stated invariant, make it executable.
  - The narrative's three facts (Division I at Illinois, seven years
    policing, outside sales for a start up) are claims about the founder
    with no pointer on the page; if the profile repo or a linked page
    carries them, a reading-guide line could point there. Founder's call.
  - Carried: tests badge "1/?/? @ 2026-09-04" still unexplained;
    fleet_paused provenance note from the census producer (README-3
    backlog).

COMMITS
  public/readme-4, one commit: "SHAYKEPUBLIC-README-4: founder narrative
  in Hugh's words; dashes removed" — README.md +
  reports/dispatch/SHAYKEPUBLIC-README-4_report.md. Not pushed. Not
  merged.

DESK ACTION (Hugh)
  The checkout is left on branch public/readme-4.
  - cd ~/Developer/shayke/shayke-public && git checkout main && git merge
    --ff-only public/readme-4 && git push origin main && git rev-parse
    --short main
  - Phone read of "Why I built this".
  - Repo About/Topics if still not done. Root LICENSE as its own
    founder-edited dispatch.

STOPPED / NOT DONE
  Nothing. No push, no merge, no other file.
```
