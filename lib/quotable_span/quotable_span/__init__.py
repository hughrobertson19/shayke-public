"""quotable_span — an LLM-as-judge check with one rule.

The grader must quote the exact words behind its verdict, and that quote must
appear character for character in the graded text. If it does not, the verdict
is VOID.

This package has zero runtime dependencies. It proves a quote is real; it does
not prove the quote is relevant, and it says nothing about whether a human
would agree with the verdict.
"""

from ._core import JudgeAdapter, Result, Verdict, check

__all__ = ["Verdict", "Result", "check", "JudgeAdapter"]
