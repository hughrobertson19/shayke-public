# What broke under adversarial personas

These findings come from an adversarial harness: synthetic personas, not real
customers. No customer data is involved anywhere below. The personas drive the
product the way a difficult, distracted or hostile user would, and a separate
graded harness checks what happened. The point of publishing this is that a
green wall proves nothing — the failures are the evidence the checking works.

They are ranked by the ledger's own severity vocabulary: blocks-the-company
first, then blocks-a-pilot, then blocks-a-seller.

## Blocks-the-company

- **The anti-fabrication gate was, briefly, not there.** The deterministic
  checks graded the seller's typed claim against the seller's own typed
  confirmation, so invented statistics passed, were stored, and carried no
  caveat. Every other failure that week failed closed or failed silent; this one
  shipped something false. That is the difference between a gate that is too
  strict and a gate that is not a gate.
- **Whole classes of claim never reached the gate.** Durations, capability
  lists, certifications and named-customer outcomes were never tagged, so the
  rule never fired on them in a live draft. Coverage of the claims that mattered
  was a fraction of the claims that existed.
- **A vetoed statistic reached the drafter anyway.** The gate correctly refused
  a number and the profile correctly stored nothing — and the raw conversation
  turn seeded the draft prompt regardless. The gate worked and the data went
  around it.
- **Auth holes a second account would have opened.** A knowledge endpoint
  returned every resolved fact to an anonymous request with no credential. A
  login path returned success for any password. A deal route discarded the
  caller's identity, so one authenticated user could read and re-stage another's
  deals — a cross-tenant breach waiting for a second account to exist.
- **The honest exit still sent the claim.** Marking a claim unverifiable
  returned "removed" and unlocked send — and left the claim sitting in the
  message body. It filed a to-do about the claim and mailed the claim at once.
- **Concurrent transcription could take the server down.** A lock guarded
  loading the model but not decoding with it, so two overlapping dictations
  could corrupt each other and crash the process.

## Blocks-a-pilot

- **Integrations failed silently.** A broken integration was indistinguishable
  from an integration with nothing to report: a seller saw no meetings and
  concluded they had none, when in fact nothing was wired.
- **Nobody independently tested the CRM write path** — the one path that
  reaches a customer's system of record.

## Blocks-a-seller

- **A read gesture destroyed onboarding answers.** Tapping to inspect a
  flagged answer prefilled it empty, and the only way out was save — so a long,
  careful answer became blank through curiosity, not editing.
- **A spelled-out number was read as a marketing statistic.** The seller
  described their own product using ordinary words, the classifier demanded a
  document to support them, and the single most important field was left
  permanently unresolved.
- **Onboarding could rate-limit a fast seller** mid-interview, because the
  interview shared a tight request budget with everything else.

Every item here was caught before any customer saw the product. That is the
whole design: agents discover, gates block, and a confidently reported fix is
still checked by an adversary before release.
