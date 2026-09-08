# SHAYKEPUBLIC-POLISH-1 — report

```
VERDICT
  LANDED, one commit on public/polish-1, not pushed, not merged. Two new
  files: root LICENSE, docs/README.md. T1 copyright holder line resolved
  by Hugh at the desk before writing: "Shayke, Inc." (the dispatch's own
  fallback), open item for counsel noted below, not silently defaulted.

T0 SCOPE
  repo shayke-public; new files LICENSE (root), docs/README.md; one
  commit on public/polish-1 (+ the report per T4); no push; no merge.

PRECONDITIONS (in order, all OK)
  1 branch main, clean tree
  2 HEAD == origin/main @ 2d3a7f8; 2d3a7f8 is ancestor of HEAD
  3 LICENSE and docs/README.md both absent before this dispatch
  4 lib/quotable_span/LICENSE exists
  5 no session.lock; ANTHROPIC_API_KEY absent; needle file readable,
    mode 600 (never read, never printed)
  Branch public/polish-1 created.

FOUNDER CHECK (T1, before writing)
  The dispatch flagged the copyright-holder line as unresolved and
  pointed to docs/legal/open_items_proposed_2026-09.md in ai-hugh
  (private repo, not read here) for the underlying question — whether
  Shayke, Inc. via the signed CIIAA, or Hugh personally, holds title.
  Asked Hugh directly rather than applying the dispatch's "if unsure,
  accept Shayke, Inc." fallback silently. Hugh confirmed "Shayke, Inc."
  in-session (2026-09-08). Same text the dispatch would have defaulted
  to; the difference is it was a confirmed answer, not an unattended
  guess on a legal document.

BUILT
  LICENSE (root) — verbatim as given, copyright line "Copyright (c) 2026
  Shayke, Inc. All rights reserved."
  docs/README.md — heading `# docs`, one bullet per file in docs/
  excluding demo.gif and the index itself, link text taken from each
  file's first `# ` line, in the reading guide's order (pilot runbook,
  success metric, data flow, persona findings). All four docs/ markdown
  files have an H1 and are named in the reading guide, so no alphabetical
  remainder applied.

VERIFY (T3 pasted)
  ls docs/
    README.md
    data_flow.md
    demo.gif
    persona_findings.md
    pilot_runbook.md
    success_metric.md
  cat docs/README.md
    # docs

    - [Pilot runbook](pilot_runbook.md)
    - [Success metric](success_metric.md)
    - [Data flow](data_flow.md)
    - [What broke under adversarial personas](persona_findings.md)
  grep -Eic -f ~/.shayke/public_needles.txt LICENSE docs/README.md
    LICENSE:0
    docs/README.md:0
    (grep's own exit code is 1 here because neither file matched
    anything at all across the combined run — expected at count 0, not
    a failure.)
  scripts/verify_public.sh              → exit 0, all 200
  git diff --stat main..HEAD (after commit) → LICENSE, docs/README.md,
    reports/dispatch/SHAYKEPUBLIC-POLISH-1_report.md — nothing else.
  Link resolution: docs/pilot_runbook.md, docs/success_metric.md,
    docs/data_flow.md, docs/persona_findings.md all resolve
    (test -f each, all OK).

WHAT HUGH NOW KNOWS
  Mechanism: GitHub reads a root LICENSE file to populate the repo's
  licence badge/slot; it does not look inside subfolders. A repo that
  has an MIT LICENSE only in lib/quotable_span/ and nothing at the root
  shows "no license" at the top level, which GitHub (and a reader)
  treats as "no rights granted, but also no explicit reservation" —
  ambiguous by omission, not the all-rights-reserved-except-one-folder
  position actually intended. The root LICENSE closes that gap without
  touching quotable_span's own MIT terms.
  Interview sentence: "I added a root LICENSE so the repo's licence
  status is stated, not inferred from an omission, while leaving the one
  MIT-licensed subfolder exactly as it was."

COMMITS
  public/polish-1, one commit: "SHAYKEPUBLIC-POLISH-1: root LICENSE,
  docs index" — LICENSE + docs/README.md +
  reports/dispatch/SHAYKEPUBLIC-POLISH-1_report.md. Not pushed. Not
  merged.

DESK ACTION (Hugh)
  Checkout is left on branch public/polish-1.
  - Approve the diff at the desk, especially the LICENSE copyright-holder
    line (confirmed "Shayke, Inc." above; open item for counsel per
    docs/legal/open_items_proposed_2026-09.md in ai-hugh remains open —
    this file is one line to change if that resolves differently).
  - Merge via SHAYKEPUBLIC-MERGE-2 (issued on this report), then
    git push origin main.

STOPPED
  Nothing. No push, no merge, no file outside LICENSE, docs/README.md
  and this report.
```
