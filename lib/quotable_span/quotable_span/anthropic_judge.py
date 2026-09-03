"""Optional adapter that asks a Claude model to produce a judge verdict.

This module is entirely optional and is never exercised by the test suite. It
is gated behind ``import anthropic`` so the core package keeps its promise of
zero runtime dependencies. If the ``anthropic`` package is not installed,
importing this module raises a clear error and nothing else in ``quotable_span``
is affected.

The model is only ever asked to *propose* a label and the quotes it says back
that label. Those quotes are then run through the same deterministic
:func:`quotable_span.check`, so a model that invents its evidence still voids.
"""

from __future__ import annotations

import json
from typing import Any

from ._core import JudgeAdapter, Result

try:  # pragma: no cover - optional dependency, never imported by tests
    import anthropic
except ImportError as exc:  # pragma: no cover
    raise ImportError(
        "quotable_span.anthropic_judge requires the optional 'anthropic' package. "
        "Install it with `pip install anthropic`. The core quotable_span package "
        "has no such dependency."
    ) from exc


_PROMPT = (
    "You are grading the text below. Return only JSON of the form "
    '{{"label": "...", "quotes": ["..."]}}. Every string in "quotes" MUST be an '
    "exact, character-for-character substring of the text. Do not paraphrase, "
    "do not fix punctuation, do not normalise whitespace.\n\n---\n{graded}\n---"
)


def _parse(raw_text: str) -> dict[str, Any]:
    return json.loads(raw_text)


def build_judge(client: "anthropic.Anthropic", model: str) -> JudgeAdapter:  # pragma: no cover
    """Return a :class:`JudgeAdapter` backed by a Claude model.

    Malformed model output (non-JSON, missing fields, wrong types) yields a VOID
    result through the adapter, exactly as any other malformed judge does.
    """

    def judge(graded: str) -> dict[str, Any]:
        message = client.messages.create(
            model=model,
            max_tokens=1024,
            messages=[{"role": "user", "content": _PROMPT.format(graded=graded)}],
        )
        text = "".join(block.text for block in message.content if getattr(block, "type", None) == "text")
        return _parse(text)

    return JudgeAdapter(judge)


__all__ = ["build_judge", "Result"]
