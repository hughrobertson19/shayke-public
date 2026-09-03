# build ledger

One record per day of activity, hash chained. Landings, halts, deaths, corrections and costs, newest first. Backfilled days are marked; days since the ledger went live are `live`.

## dispatches

| date | dispatch | repo | status | tests (p/f/s) | eval | cost |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-09-03 | PEAKOPS-ARCHITECT-3 | — | HALT | — | UNKNOWN | — |
| 2026-09-02 | AIHUGH-BASELINE-REFRESH-1 | ai-hugh | LANDED | 45/0/2 | UNKNOWN | — |
| 2026-09-02 | PEAKOPS-AGENT-PIPELINE-1 | peak-ops | LANDED | 5666/0/? | UNKNOWN | — |
| 2026-09-02 | PEAKOPS-ARCHITECT-2 | peak-ops | LANDED | 5627/0/5 | UNKNOWN | — |
| 2026-09-02 | PEAKOPS-OVERNIGHT-SCHEDULE-1 | peak-ops | LANDED | 22/?/? | UNKNOWN | — |
| 2026-09-02 | PEAKOPS-OVERNIGHT-SCHEDULE-2 | — | HALT | — | UNKNOWN | — |
| 2026-09-02 | PEAKOPS-OVERNIGHT-SCHEDULE-2 | peak-ops | LANDED | 36/?/? | UNKNOWN | — |
| 2026-09-01 | AIHUGH-DISPATCH-HOOKS-FIX-1 | ai-hugh | LANDED | 23/?/? | UNKNOWN | — |
| 2026-09-01 | AIHUGH-MERGE-CONTACT-ROLES-1 | ai-hugh | LANDED | 10308/0/21 | UNKNOWN | — |
| 2026-09-01 | AIHUGH-SALESFORCE-MULTITHREAD-CONTACT-ROLES-1 | ai-hugh | LANDED | 10307/1/21 | UNKNOWN | — |
| 2026-09-01 | PEAKOPS-ARCHITECT-1 | peak-ops | LANDED | 5626/0/5 | UNKNOWN | — |
| 2026-09-01 | PEAKOPS-ENGHEAD-SEQ-1 | peak-ops | LANDED | 5592/?/? | UNKNOWN | — |
| 2026-09-01 | PEAKOPS-HYGIENE-2 | peak-ops | LANDED | 22/?/? | UNKNOWN | — |
| 2026-09-01 | PEAKOPS-OPS-REVIVE-1 | peak-ops | LANDED | 16/?/? | UNKNOWN | — |
| 2026-09-01 | PEAKOPS-RANKING-POLICY-1 | peak-ops | LANDED | 5576/0/5 | UNKNOWN | — |
| 2026-08-31 | JUDGE-WHITESPACE-VOID-1 | peak-ops | LANDED | 5/?/? | UNKNOWN | — |
| 2026-08-31 | PEAKOPS-COO-RETIRE-1 | peak-ops | LANDED | 7/?/? | UNKNOWN | — |
| 2026-08-31 | PEAKOPS-PROVENANCE-1 | peak-ops | LANDED | 5498/?/? | UNKNOWN | — |
| 2026-08-31 | PEAKOPS-SELFIMPROVE-AUDIT-1 | peak-ops | LANDED | 19/?/? | UNKNOWN | — |
| 2026-08-31 | PEAKOPS-VIEWER-FRESH-1 | peak-ops | LANDED | 5/?/? | UNKNOWN | — |
| 2026-08-31 | PEAKOPS-VIEWER-V3-PHASE0 | peak-ops | LANDED | 20/?/? | UNKNOWN | — |
| 2026-08-30 | PEAKOPS-APIGAP-1 | peak-ops | LANDED | 5498/0/? | UNKNOWN | — |
| 2026-08-30 | PEAKOPS-F6-WIRE-1 | peak-ops | LANDED | 5508/0/5 | UNKNOWN | — |
| 2026-08-30 | PEAKOPS-FEED-HANDOFF-1 | peak-ops | LANDED | 5530/0/5 | UNKNOWN | — |
| 2026-08-30 | PEAKOPS-REDSUITE-RCA-1 | peak-ops | LANDED | 5484/3/5 | UNKNOWN | — |
| 2026-08-30 | PEAKOPS-TELEGRAM-NOTIFY-1 | peak-ops | LANDED | 5522/0/5 | UNKNOWN | — |
| 2026-08-30 | PEAKOPS-VIEWER-VOLATILE-1 | peak-ops | LANDED | 20/?/? | UNKNOWN | — |
| 2026-08-18 | AIHUGH-OVERNIGHT-HEAVY-1 | ai-hugh | DEAD_NO_REPORT | — | UNKNOWN | — |
| 2026-08-18 | PEAKOPS-OVERNIGHT-REGISTRY-SCORING-1 | peak-ops | DEAD_NO_REPORT | — | UNKNOWN | — |
| 2026-08-17 | AIHUGH-FIX-RENDER-ENV-1 | ai-hugh | DEAD_NO_REPORT | — | UNKNOWN | — |
| 2026-08-13 | AIHUGH-MODEL-TIER-BIND-1 | ai-hugh | DEAD_NO_REPORT | — | UNKNOWN | — |
| 2026-08-12 | AIHUGH-INTEGRATIONS-DEPTH-1 | ai-hugh | DEAD_NO_REPORT | — | UNKNOWN | — |
| 2026-08-12 | AIHUGH-NOTIFICATION-SOUND-1 | ai-hugh | DEAD_NO_REPORT | — | UNKNOWN | — |
| 2026-08-12 | AIHUGH-READINESS-P0-1 | ai-hugh | DEAD_NO_REPORT | — | UNKNOWN | — |
| 2026-08-12 | AIHUGH-SEGFAULT-ISOLATE-1 | ai-hugh | DEAD_NO_REPORT | — | UNKNOWN | — |
| 2026-08-12 | AIHUGH-XP-TRUTH-1 | ai-hugh | DEAD_NO_REPORT | — | UNKNOWN | — |
| 2026-08-12 | PEAKOPS-FINISH-1 | peak-ops | DEAD_NO_REPORT | — | UNKNOWN | — |
| 2026-08-11 | PEAKOPS-OUTCOME-EMIT-1 | peak-ops | DEAD_NO_REPORT | — | UNKNOWN | — |
| 2026-08-10 | AIHUGH-PLAY-ANALYZER-1 | ai-hugh | DEAD_NO_REPORT | — | UNKNOWN | — |

## corrections

My own mistakes, classed by type, published on purpose.

| date | class | settled | what it was |
| --- | --- | --- | --- |
| 2026-08-27 | mechanism-from-narrative | settled | a guard deadlock called unbounded when a backstop caps it |
| 2026-08-27 | mechanism-from-narrative | settled | a mechanism asserted from narrative fit, not from the code |
| 2026-08-25 | metric-drift | settled | a frozen figure lifted once the number was remeasured |
| 2026-08-24 | metric-drift | open | a test-count gap between two repos, open for verification |
| 2026-08-24 | other | open | a status node contradicting itself, flagged and still open |
| 2026-08-20 | stale-assumption | settled | an encryption description left stale after a fallback was removed |
| 2026-08-03 | metric-drift | settled | a staged-draft count reprinted unchecked for weeks of briefings |
| 2026-08-03 | metric-drift | settled | a harness case count the docs disagreed on |
| 2026-07-31 | chat-provenance-as-repo | settled | a re-dated external story shipped as fact, then caught |
