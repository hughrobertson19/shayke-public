# Pilot runbook

How a pilot is designed to run for a customer's engineers. This describes the
intended shape of a first engagement; where a control is already decided it
carries its date, and where it is design intent rather than shipped behaviour
it says so.

## Before anything touches production

The pilot runs against a sandbox first, never a production org. Real API calls
go to a sandbox CRM account and a test mail account, with entirely synthetic
companies, contacts and deals — fake data over real wires. No customer data
exists anywhere in the sandbox phase. Only after the customer's team has seen
the write path behave against the sandbox does a production org enter the
picture.

The connection to the customer's systems is designed to be owned by the
customer, not by us: the pilot intent is that the OAuth application authorising
CRM and mail access is registered under the company's own tenant, so access can
be reviewed and revoked by the customer at any time. (This is the target
arrangement, not a shipped default — today's connect flow still surfaces an
unverified-app warning, and closing that is part of pilot readiness.)

## Sending is off until it is deliberately armed

Outbound sending is opt-in, fail-closed, allowlist-gated and idempotent
(decided 2026-07-29; generalised to every protocol 2026-07-30). The default is
dry-run: unless two independent variables are both set on purpose, every send
resolves to dry-run. One stray configuration line cannot arm it. Reads degrade
when a gate is shut; writes and sends raise rather than proceed silently,
because being silently wrong about whether a message went out is the exact
failure the containment exists to prevent. A dry-run opens no socket — a flag
that promises a no-op may not transmit.

## Every write is a proposed, confirmed, re-read change

CRM writes are limited to a small set of guarded intents — a stage move, a
logged call, a created follow-up — each through one proven path: propose,
confirm with a single-use token, write, then re-read. Every write states the
object, the record, the field, the old value and the new value, and waits for
the seller's explicit confirm. Every write is independently re-read and
field-compared; a mismatch is a loud, typed error, never a quiet success. Every
write is audit-logged with per-field provenance. That audit log plus the
re-read is the rollback story: nothing changes without a recorded before and
after, so a wrong write is visible and reversible rather than lost.

Record creation and bulk updates are out of scope for the pilot (founder
ruling). Shayke is never the source of truth for anything a CRM already owns;
it records only what no CRM holds — the conversation, the coaching, the
provenance of each write.

## What the customer's security team can review

The pilot is designed to hand a reviewer the data-flow document (`data_flow.md`
here), the encryption-at-rest statement, the list of every place the system can
send data and under what arming, and the standard agreements in draft. Security
review is not a separate department that might be asleep — credential-leak,
scope and data-flow checks live inside the release gate as code, so nothing
ships past a red gate.

## What the founder launches by hand, forever

Four things never become automated, at any autonomy level (locked 2026-08-31):
send paths, the scoring layer, changes to the Evidence Rule, and
auth/credentials. Everything else can be delegated per class. A human arms every
action that crosses to a customer or spends money. Agents discover and draft;
the founder launches.

## The channel

The founder talks to the system through one chat channel (Telegram). Agents
draft; a human dispatches. No agent sends a message to a real person on its own.
