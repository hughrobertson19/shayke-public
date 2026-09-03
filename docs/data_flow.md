# Data flow

What data enters the system, where it lives, who sees it, and what never leaves
the customer's boundary.

## What enters

Three kinds of input: the seller's own material (onboarding answers, their
profile, their words), records read from the CRM, and captured conversations
(call recordings and their transcripts). The seller drives all of it through one
chat surface; nothing is ingested about a third party without the seller
bringing it in.

## Where it is stored

Working state lives in a local SQLite database on the machine that runs the
system. Recordings and their transcripts are kept on local disk under a
per-user path.

Encryption at rest: per user AES 256 GCM default for new writes, legacy read
fallback enabled.

## Which model provider sees what

Text that needs a model — extraction from a conversation, the grading step —
goes to Claude, from Anthropic. Vision runs on a smaller Claude model.
Transcription is different: audio is transcribed locally, in process, and the
audio is not sent to any model provider. So a model provider sees extracted
text and grading prompts; it does not see raw audio, and it never sees another
customer's data, because there is one seller's material in play at a time.

## Retention

A conversation's report and its transcript are kept indefinitely; the media
(the audio) expires after thirty days (decided 2026-08-04). An unanalysed
recording is never expired. Structured logs are kept for a two-week window.

## What never leaves the customer's boundary

Mobile capture transcribes locally, redacts on the client, and shows the seller
a preview before anything is uploaded — customer data does not cross the
boundary uninspected (decided 2026-08-04). Shayke is never the source of truth
for anything a CRM already owns; it is the record only for what no CRM holds —
the conversation, the coaching, and the per-field provenance of each write. A
claim the product makes to the seller about their own accounts is held to the
same evidence standard as anything it would send outward: grounded in retrieved,
provenanced state, or marked unknown (decided 2026-08-09).
