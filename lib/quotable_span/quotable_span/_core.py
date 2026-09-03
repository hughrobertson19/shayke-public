"""Core types and the substring check.

No model calls live here. No network, no third-party imports — only the
standard library. The rule is deliberately small: a quote is valid only if it
is an exact substring of the graded text. The one permitted relaxation
(``strict=False``) collapses runs of whitespace to a single space on both
sides and nothing else.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Callable, Literal

__all__ = ["Verdict", "Result", "check", "JudgeAdapter"]

_WHITESPACE_RUN = re.compile(r"\s+")


@dataclass(frozen=True)
class Verdict:
    """What a grader claims: a label plus the exact spans it says back it."""

    label: str
    quotes: list[str]


@dataclass(frozen=True)
class Result:
    """The outcome of checking a verdict against the text it graded."""

    status: Literal["VALID", "VOID"]
    reason: str
    missing: list[str] = field(default_factory=list)
    normalised: bool = False


def _collapse(text: str) -> str:
    """Collapse every run of whitespace to a single space. Nothing else."""

    return _WHITESPACE_RUN.sub(" ", text)


def check(verdict: Verdict, graded_text: str, *, strict: bool = True) -> Result:
    """Check that every quote in ``verdict`` appears in ``graded_text``.

    Strict (the default): each quote must be an exact substring, with no
    normalisation — whitespace, case and punctuation all count.

    ``strict=False``: runs of whitespace are collapsed to one space on both
    sides before the substring test, and ``normalised=True`` is set on the
    result. No other normalisation is applied — case and punctuation still
    count.

    An empty quote list is VOID: a verdict that quotes nothing has proven
    nothing.
    """

    if not verdict.quotes:
        return Result(status="VOID", reason="no quote given", missing=[], normalised=False)

    if strict:
        haystack = graded_text
        normalised = False
    else:
        haystack = _collapse(graded_text)
        normalised = True

    missing: list[str] = []
    for quote in verdict.quotes:
        needle = quote if strict else _collapse(quote)
        if needle not in haystack:
            missing.append(quote)

    if missing:
        reason = "quote not found character for character" if strict else "quote not found after whitespace collapse"
        return Result(status="VOID", reason=reason, missing=missing, normalised=normalised)

    return Result(status="VALID", reason="every quote found verbatim", missing=[], normalised=normalised)


class JudgeAdapter:
    """Wrap an arbitrary judge callable and run its output through ``check``.

    The callable is expected to take the graded text and return a mapping with
    a ``label`` and a ``quotes`` list. Any deviation from that shape — a
    non-mapping return, a missing field, a wrong type — yields a VOID result
    whose reason names the offending field. No model is ever called from this
    package; the callable supplies whatever judgement it wants to.
    """

    def __init__(self, judge: Callable[[str], dict], *, strict: bool = True) -> None:
        self._judge = judge
        self._strict = strict

    def __call__(self, graded_text: str) -> Result:
        try:
            raw = self._judge(graded_text)
        except Exception as exc:  # noqa: BLE001 — a broken judge is a VOID, not a crash
            return Result(status="VOID", reason=f"judge raised: {type(exc).__name__}", missing=[], normalised=False)

        if not isinstance(raw, dict):
            return Result(status="VOID", reason="judge output is not a mapping", missing=[], normalised=False)

        if "label" not in raw:
            return Result(status="VOID", reason="judge output missing field: label", missing=[], normalised=False)
        if "quotes" not in raw:
            return Result(status="VOID", reason="judge output missing field: quotes", missing=[], normalised=False)

        label = raw["label"]
        quotes = raw["quotes"]
        if not isinstance(label, str):
            return Result(status="VOID", reason="judge output field label is not a string", missing=[], normalised=False)
        if not isinstance(quotes, list) or not all(isinstance(q, str) for q in quotes):
            return Result(status="VOID", reason="judge output field quotes is not a list of strings", missing=[], normalised=False)

        return check(Verdict(label=label, quotes=quotes), graded_text, strict=self._strict)
