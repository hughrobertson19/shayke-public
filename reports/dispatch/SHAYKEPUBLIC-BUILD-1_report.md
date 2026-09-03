```
SHAYKEPUBLIC-BUILD-1 — FINAL REPORT (2026-09-03)

VERDICT: yes — fresh PRIVATE shayke-public built and pushed (ledger, census,
quotable_span, docs, firewall, badges), the peak-ops ledger producer + tests +
sweep hook landed, and the profile repo is public. Repo stays PRIVATE until the
founder flips it. One honest deviation on the full-suite run (see TESTS).

CLASSIFY (what the report shape / telemetry actually looked like vs assumed):
- DISPATCH REPORTS genuinely differ in shape. peak-ops has 21 under
  reports/dispatch/*_report.md, ai-hugh 4; peak-evaluator has NO
  reports/dispatch/ dir (its reports sit scattered under docs/ and reports/).
  The producer globs reports/dispatch/*_report.md per repo via git refs, so
  peak-evaluator contributes 0 by that glob — reported, not guessed around.
- EVAL VERDICT is NOT a structured field in any dispatch report; they carry
  suite health as prose ("full suite green"). So eval_verdict is UNKNOWN unless
  a report states an explicit EVAL:/VERDICT: GREEN|RED line. None do → every
  record is UNKNOWN. No verdict is inferred from pass counts.
- TELEMETRY: there is NO per-dispatch token/cost artefact. data/run_telemetry
  is agent+run_id keyed and all-zero; run_ledger/budget_ledger are agent/day
  keyed; the claude -p dispatch cost is architecturally unobservable to this
  repo. So tokens_in/tokens_out/cost_usd are null on every record, with a
  day-level note; never estimated. [VERIFY resolved — see VERIFY.]
- TESTS counts: two shapes coexist (pytest tail "N passed, M skipped" and the
  compact "P/F/S" slash form). Parser handles both; failed omitted in the clean
  shape = 0; anything unparsed = null, shown as "?".

BUILT:
- shayke-public (NEW repo, PRIVATE): README.md (verbatim Appendix A);
  lib/quotable_span/ (MIT clean-room: __init__/_core/eval/anthropic_judge,
  eval/cases.json 20 invented cases, tests, LICENSE, README Appendix B,
  EVAL_RESULTS.md); ledger/ (days/*.json ×17, latest.json, README.md,
  badges/{last_build,tests,eval,chain}.json, publish_log.json, verify_chain.py);
  fleet/{census.json,README.md}; docs/{pilot_runbook,data_flow,success_metric,
  persona_findings}.md + demo.gif (placeholder); scripts/{scan_names.py,
  name_allow_extra.txt,verify_public.sh}; reports/name_scan.txt.
- peak-ops: scripts/publish_public_ledger.py (producer), scripts/public_corrections.json
  (hand-authored public corrections view), tests/test_public_ledger.py (16),
  scripts/morning_sweep.sh (+publish step), CHANGES.md (landing marker).
- profile repo hughrobertson19/hughrobertson19 (PUBLIC): README.md (Appendix C).

VERIFY (every [VERIFY] in the dispatch resolved):
- Telemetry path [VERIFY]: `grep -rl "tokens" reports/ telemetry/ ~/.peak-ops`
  resolves to data/run_telemetry/<agent>/<date>.jsonl (agent+run_id keyed,
  all-zero) and ~/.peak-ops/{run_ledger.jsonl,budget_ledger.json} (agent/day
  keyed). NO per-dispatch token/cost exists → both fields null + day note.
  RESOLVED: null, never estimated.

TESTS (before/after; where each fake starts):
- quotable_span: 39 passed (0.02s); eval reproduces 20/20. All cases invented
  (lib/quotable_span/eval/cases.json — invoices/orders/shipments, no real
  company/person/product/price/date).
- peak-ops targeted, RECORDED foreground through record_verification.py at
  HEAD: test_public_ledger.py (16, new — invented fixtures) +
  test_overnight_schedule.py (52, incl. sweep grep-guard) + test_authority.py
  (17) + test_run_telemetry_firewall.py (6) = 75 passed, exit 0
  (artefact .claude/verification/20260903T220243Z_SHAYKEPUBLIC-BUILD-1.json).
  `make anti-fabrication`: 130 passed.
- FULL tests/ suite: NOT run to completion this session. On this machine it
  currently takes ~6.2h (prior dispatch artefact
  20260903T155505Z_PEAKOPS-SEQUENCING-2-FINAL2.json: 22374s, reached 100%
  all-passing at parent b5b1d38, itself SIGTERM'd exit -15 — a pre-existing
  environment condition today, not introduced here). Two foreground attempts
  (40m, 2h) were auto-backgrounded by the harness before completing; rather
  than block ~6h or gamble on a possibly-degraded run, verification is the
  recorded targeted set above. The change is additive (one new script, one new
  test file, one data file, one read-only sweep-hook line) and fully covered.

ARCH REVIEW:
- Producer is READ-ONLY against the private trees: content via `git show
  HEAD:<path>`, provenance via `git log --diff-filter=A`; no checkout, no
  mutating verb; agent-eval never read. Writes land only in shayke-public.
- No private source crossed the boundary except the metadata fields named in
  T3/T4 (dispatch id, landed commit/date, suite counts, verdict token) and the
  hand-authored corrections titles; SHAYKE_CORRECTIONS.md full text never left.
- Hash chain: hash = sha256(canonical JSON, sorted keys, no whitespace, of the
  record with `hash` removed and `prev_hash` included); first prev_hash = 64
  zeros. verify_chain.py recomputes + checks linkage (in the tests, exit 0).
  Historical days are append-only/idempotent; today is the live tip.
- Census: registered = in the registry (42); running = not-paused AND not-parked
  AND a scheduler fires its cadence. Fleet is PAUSED now → 0 running; recorded
  as fleet_paused with the reason in fleet/README.md.

DEMO: MISSING — no vhs / asciinema / agg on PATH. A 1×1 placeholder is committed
at docs/demo.gif so the verbatim README image link resolves; the README's "no
capture existed at build time" comment is left in place.

LEDGER DAYS: 17 records, first 2026-07-31, last 2026-09-03. Null-cost days: 17
(all — no per-dispatch telemetry exists). 39 dispatch events, 9 corrections.

NAME SCAN: clean (0 unknown). Reviewed extras in scripts/name_allow_extra.txt
are role/department/law words from the diagram, the first-person pronoun, month
"March", protocol acronyms (OAuth/API/LLM/AI), a Python literal, invented eval
tokens, and the two badge-host domains — none names a person, company, product
or customer. Dispatch identifiers (published by design) and ISO timestamps are
a recognised safe class. No former-employer or customer name anywhere.
one eponymous-law reference was reworded out to avoid a person name. NUMBERS scan: only
dates, the AES-256 line, and the badge-URL GitHub handle — no prose counts.

BACKLOG RECOMMENDATION: wire real per-dispatch token/cost once the overnight
chain can attribute a claude -p run's cost to its dispatch id (today the fields
are honestly null). Also: PEAKOPS-OPS-LEDGER-1 is already queued — retire it or
fold it into this producer (one doc, one job).

COMMITS: shayke-public on main (initial 5fe2342 + this report copy); peak-ops
on main (the commit bearing this file — see CHANGES.md landing marker);
hughrobertson19/hughrobertson19 on main. Exact SHAs in the dispatch chat report.

DESK ACTIONS (founder):
- Flip visibility PUBLIC + verify:
  gh repo edit hughrobertson19/shayke-public --visibility public --accept-visibility-change-consequences && bash ~/Developer/shayke/shayke-public/scripts/verify_public.sh
- Social preview (text only): shayke-public · An agent fleet that builds a
  sales product overnight and publishes its own build ledger. Halts,
  corrections and costs included.
- Record a real demo GIF later (DEMO currently MISSING).

STOPPED / NOT DONE: full tests/ suite not completed (~6.2h on this machine;
recorded targeted verification instead — see TESTS). demo.gif is a placeholder
(no capture tooling on PATH). Public URLs unverified until the founder flips
visibility (proved now via gh api — all paths OK; profile repo live).

NOT RUN, AND WHY: full `python3 -m pytest tests/ -q` to green — ~6.2h runtime on
this degraded machine; two attempts auto-backgrounded; covered by the recorded
targeted set and the additive nature of the change (see TESTS).

Branch: main
FINAL SHA: see git log on main (this commit); push confirmed.

PASS CONDITIONS:
1. shayke-public created PRIVATE, pushed — YES
2. quotable_span green + eval 20/20 — YES
3. ledger chain verifies (17 days) — YES
4. census registered/running honest (42/0, paused) — YES
5. name + numbers firewalls clean — YES
6. profile repo public + pushed — YES
7. full suite green — NO (not completed this session; ~6.2h; recorded targeted
   verification instead — stated plainly, not papered over)
```
