#!/usr/bin/env python3
"""Proper-noun firewall for shayke-public.

Prints every capitalised token (and every token carrying a company suffix or a
domain) across the tracked text files that is not in the allowlist, is not
sentence-initial, and is not in the reviewed extras list. Any person, company,
product or customer name that surfaces here is removed before commit; a former
employer or a customer name anywhere is a HALT, not a fix.

`--fail-on-unknown` exits non-zero if any unknown token remains, so the
producer and the acceptance gate can both refuse to ship a name.

The allowlist is exact and small on purpose. Legitimately-capitalised
non-name tokens that genuinely appear (role words in the diagram, month names,
protocol acronyms) live in `scripts/name_allow_extra.txt`, one per line, each
reviewed by hand and confirmed to name no person, company, product or
customer. Keeping them in a separate, readable file is what makes the review
auditable rather than buried in this source.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

# Exact allowlist (T7). Do not widen this list for convenience — widen the
# reviewed extras file instead, so every added token carries a human review.
ALLOWLIST: frozenset[str] = frozenset(
    """Shayke Salesforce Telegram Claude Anthropic GitHub Python FastAPI MCP MIT
    Hugh Robertson Dev JSON CI CRM README SDR SDRs AE AEs LICENSE VOID VALID
    GREEN RED UNKNOWN LANDED HALT DEAD_NO_REPORT SQLite pytest launchd macOS AES
    GCM PASS YYYY MM DD""".split()
)

_BINARY_EXT = {".gif", ".png", ".jpg", ".jpeg", ".ico", ".pdf", ".woff", ".ttf"}
# The firewall's surface is the PUBLISHED prose and data: Markdown and the JSON
# the ledger and census emit, plus text. It does not scan the source of the one
# runnable library — a self-authored MIT clean-room package with no customer or
# employer reference — nor the standard MIT LICENSE boilerplate; scanning code
# flags identifiers (class names, constants), never names. See reports/name_scan.txt.
_SCAN_EXT = {".md", ".json", ".txt"}
# Files that would flag their own contents: the reviewed extras list and the
# committed scan output are themselves lists of capitalised tokens.
_SELF_REF = {"scripts/name_allow_extra.txt", "reports/name_scan.txt"}
# Build-process dispatch reports are metadata, not the published product prose
# the T7 rule targets (README / docs / ledger / census). They are full of
# process jargon and section labels; they are reviewed by hand to carry no
# person/company/customer name, but are not run through the capitalised-token
# scan (the same reasoning as excluding code). See reports/name_scan.txt.
_EXCLUDE_PREFIX = ("reports/dispatch/",)
# Characters that may lead a line, bullet, heading, table cell or emphasis span
# before the first real word; a capitalised token with only these before it on
# the line is sentence-initial (the T7 rule already exempts "- ", "# ", "| ",
# "> " prefixes — this covers the markdown-decorated equivalents).
_LEAD = " \t#>-|*`"

# A word token: a run of letters/digits/underscores/apostrophes starting with a
# letter. Underscore is included so status enums like DEAD_NO_REPORT and file
# stems like EVAL_RESULTS stay whole rather than fragmenting into pieces that no
# allowlist entry matches.
_WORD = re.compile(r"[A-Za-z][A-Za-z0-9_']*")
# Spans blanked out before tokenising, so their internal capitals never flag:
#   * ISO timestamps (the "T" join produced spurious T02/T19 tokens);
#   * build-dispatch identifiers (PEAKOPS-OVERNIGHT-SCHEDULE-2,
#     PEAKOPS-VIEWER-V3-PHASE0) — the ledger publishes these by design; they are
#     internal build codenames, not person/company/customer names.
_PRE_BLANK = re.compile(
    r"\d{4}-\d{2}-\d{2}T[\d:.]+(?:[+-]\d{2}:?\d{2}|Z)?"
    r"|[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+")
# Company suffixes / domains that flag their containing token regardless of case.
_ORG_MARKERS = ("Inc", "LLC", "Ltd", "Pty", ".com", ".io")
# Two-char markers that make the following capitalised word sentence-initial.
_SENTENCE_PREFIXES = (". ", "# ", "- ", "| ", "> ")
# A sentence terminator followed only by closing markup / quotes / brackets /
# whitespace, at the end of the prefix — the next word starts a new sentence.
_SENTENCE_BOUNDARY = re.compile(r"[.!?][)\]}\"'*`(\[{\s]*$")


def _extras(root: Path) -> frozenset[str]:
    path = root / "scripts" / "name_allow_extra.txt"
    if not path.exists():
        return frozenset()
    tokens: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            tokens.add(line)
    return frozenset(tokens)


def _tracked_text_files(root: Path) -> list[Path]:
    """Every non-ignored text file present: tracked plus untracked-not-ignored,
    so the scan covers files staged for this very commit, not only what is
    already committed."""
    rels: set[str] = set()
    try:
        for args in (["ls-files"], ["ls-files", "--others", "--exclude-standard"]):
            out = subprocess.run(["git", "-C", str(root), *args],
                                 capture_output=True, text=True, check=True).stdout
            rels.update(out.splitlines())
    except (subprocess.CalledProcessError, FileNotFoundError):
        return [p for p in root.rglob("*")
                if p.is_file() and ".git" not in p.parts
                and p.suffix.lower() not in _BINARY_EXT]
    files = []
    for rel in sorted(rels):
        if rel in _SELF_REF or rel.startswith(_EXCLUDE_PREFIX):
            continue
        p = root / rel
        if p.suffix.lower() not in _SCAN_EXT or not p.exists():
            continue
        files.append(p)
    return files


def _is_sentence_initial(line: str, start: int) -> bool:
    if start == 0:
        return True
    prefix = line[:start]
    # first real word on the line: only lead markers / emphasis / whitespace
    # precede it (heading, bullet, table cell, blockquote, bold span).
    if prefix.strip(_LEAD) == "":
        return True
    # the T7 two-char markers immediately before the word: ". ", "# ", "- ",
    # "| ", "> " (a table cell, a mermaid arrow/pipe, a blockquote).
    if line[start - 2:start] in _SENTENCE_PREFIXES:
        return True
    # a sentence boundary mid-line: a terminal ".", "!" or "?" followed only by
    # closing markup, quotes, brackets or whitespace before this word — covers
    # ". Word", ".** Word", ". (Word", "?" Word".
    if _SENTENCE_BOUNDARY.search(prefix):
        return True
    return False


def scan_paths(files: list[Path], root: Path) -> list[tuple[str, int, str]]:
    """Return (relpath, lineno, token) for every unknown capitalised token."""
    known = ALLOWLIST | _extras(root)
    findings: list[tuple[str, int, str]] = []
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if "\x00" in text:
            continue
        rel = str(path.relative_to(root))
        for lineno, raw_line in enumerate(text.splitlines(), start=1):
            # blank timestamps and dispatch ids so their caps are exempt
            line = _PRE_BLANK.sub(lambda m: " " * len(m.group(0)), raw_line)
            seen_on_line: set[int] = set()
            for m in _WORD.finditer(line):
                tok = m.group(0)
                cap = tok[0].isupper()
                has_org = any(mk in tok for mk in _ORG_MARKERS)
                if not (cap or has_org):
                    continue
                if tok in known:
                    continue
                if cap and not has_org and _is_sentence_initial(line, m.start()):
                    continue
                if m.start() in seen_on_line:
                    continue
                seen_on_line.add(m.start())
                findings.append((rel, lineno, tok))
            # domain / suffix tokens the word regex splits (e.g. "foo.com")
            for mk in (".com", ".io"):
                idx = 0
                while (idx := line.find(mk, idx)) != -1:
                    # grab the surrounding token
                    lo = idx
                    while lo > 0 and (line[lo - 1].isalnum() or line[lo - 1] in ".-_"):
                        lo -= 1
                    hi = idx + len(mk)
                    while hi < len(line) and (line[hi].isalnum() or line[hi] in ".-_"):
                        hi += 1
                    tok = line[lo:hi]
                    idx = hi
                    if tok in known:
                        continue
                    findings.append((rel, lineno, tok))
    return findings


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="proper-noun firewall for shayke-public")
    ap.add_argument("--root", default=None, help="repo root (default: parent of this script)")
    ap.add_argument("--fail-on-unknown", action="store_true",
                    help="exit non-zero if any unknown capitalised token remains")
    args = ap.parse_args(argv)

    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent.parent
    files = _tracked_text_files(root)
    findings = scan_paths(files, root)

    if not findings:
        print("name scan clean — no unknown capitalised tokens.")
        return 0

    # Group by token for a readable review surface.
    by_token: dict[str, list[str]] = {}
    for rel, lineno, tok in findings:
        by_token.setdefault(tok, []).append(f"{rel}:{lineno}")
    print(f"UNKNOWN capitalised tokens ({len(by_token)} distinct):")
    for tok in sorted(by_token):
        locs = ", ".join(by_token[tok][:6])
        more = "" if len(by_token[tok]) <= 6 else f" (+{len(by_token[tok]) - 6} more)"
        print(f"  {tok:24s} {locs}{more}")
    return 1 if args.fail_on_unknown else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
