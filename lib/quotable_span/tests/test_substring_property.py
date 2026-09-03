"""Property-style tests for the substring rule.

No third-party dependency (no hypothesis): a fixed-seed generator drives the
properties so runs are reproducible.

Properties:
  1. Any real substring of the graded text is VALID under strict.
  2. A string that is not a substring is VOID under strict.
  3. Lax matching accepts everything strict accepts (it only relaxes whitespace).
  4. Collapsing whitespace in both the quote and the text makes lax succeed.
"""

from __future__ import annotations

import random
import string

from quotable_span import Verdict, check

_ALPHABET = string.ascii_lowercase + "   ,.\n"


def _texts(seed: int, n: int) -> list[str]:
    rng = random.Random(seed)
    out = []
    for _ in range(n):
        length = rng.randint(5, 60)
        out.append("".join(rng.choice(_ALPHABET) for _ in range(length)))
    return out


def test_every_substring_is_valid_under_strict():
    rng = random.Random(1)
    for text in _texts(1, 200):
        if not text:
            continue
        i = rng.randint(0, len(text) - 1)
        j = rng.randint(i + 1, len(text))
        span = text[i:j]
        r = check(Verdict("pass", [span]), text)
        assert r.status == "VALID", (repr(span), repr(text))


def test_absent_string_is_void_under_strict():
    # a sentinel that cannot appear: the alphabet has no digits.
    for text in _texts(2, 200):
        r = check(Verdict("pass", ["Z9Z9-not-here"]), text)
        assert r.status == "VOID"


def test_lax_accepts_everything_strict_accepts():
    rng = random.Random(3)
    for text in _texts(3, 200):
        if not text:
            continue
        i = rng.randint(0, len(text) - 1)
        j = rng.randint(i + 1, len(text))
        span = text[i:j]
        strict = check(Verdict("pass", [span]), text)
        lax = check(Verdict("pass", [span]), text, strict=False)
        if strict.status == "VALID":
            assert lax.status == "VALID"
        assert lax.normalised is True


def test_whitespace_collapse_makes_lax_match():
    graded = "alpha\t\tbeta   gamma\ndelta"
    quote = "alpha beta gamma delta"
    assert check(Verdict("pass", [quote]), graded).status == "VOID"
    assert check(Verdict("pass", [quote]), graded, strict=False).status == "VALID"


def test_empty_quote_list_always_void():
    for text in _texts(4, 50):
        assert check(Verdict("pass", []), text).status == "VOID"
