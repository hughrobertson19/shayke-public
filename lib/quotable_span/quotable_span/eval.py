"""Reproduce the eval set and write EVAL_RESULTS.md.

Run from the ``lib/quotable_span`` directory:

    python -m quotable_span.eval

Every case in ``eval/cases.json`` is run through :class:`JudgeAdapter` with the
stored judge output, compared against its expected status, and printed. Wrong
cases are shown, not hidden — a table that only ever prints green teaches you
nothing. Paths are resolved relative to this file, so the command works from
any working directory.
"""

from __future__ import annotations

import json
from pathlib import Path

from ._core import JudgeAdapter

_PKG_DIR = Path(__file__).resolve().parent
_LIB_ROOT = _PKG_DIR.parent
_CASES_PATH = _LIB_ROOT / "eval" / "cases.json"
_RESULTS_PATH = _LIB_ROOT / "EVAL_RESULTS.md"


def _load_cases() -> list[dict]:
    data = json.loads(_CASES_PATH.read_text(encoding="utf-8"))
    return data["cases"]


def run_case(case: dict) -> str:
    """Run one case through the adapter and return the resulting status."""

    judge_output = case["judge_output"]
    strict = case.get("strict", True)
    adapter = JudgeAdapter(lambda _graded, _out=judge_output: _out, strict=strict)
    return adapter(case["graded"]).status


def evaluate() -> list[dict]:
    rows = []
    for case in _load_cases():
        got = run_case(case)
        rows.append(
            {
                "id": case["id"],
                "strict": case.get("strict", True),
                "expected": case["expected"],
                "got": got,
                "ok": got == case["expected"],
                "comment": case.get("comment", ""),
            }
        )
    return rows


def _render_table(rows: list[dict]) -> str:
    lines = ["| case | strict | expected | got | ok |", "| --- | --- | --- | --- | --- |"]
    for r in rows:
        mark = "yes" if r["ok"] else "NO"
        lines.append(f"| {r['id']} | {str(r['strict']).lower()} | {r['expected']} | {r['got']} | {mark} |")
    return "\n".join(lines)


_NOT_MEASURED = """## What this does not measure

This eval measures one thing: given a judge output, does `quotable_span` return
the status the case designer expected. It confirms the substring rule behaves
as specified across exact, case, punctuation, whitespace, line-break, multi-quote,
empty and malformed inputs.

It does **not** measure:

- **Human agreement.** No human has rated whether the labels in these cases are
  the labels a person would give. That number is unmeasured here. The library
  proves a quote is real; it says nothing about whether a human would agree with
  the verdict the quote is attached to.
- **Relevance.** The c15 case passes on purpose: a real but irrelevant quote is
  VALID, because the check enforces that the quote is real, not that it supports
  the label. This is the ceiling of what the tool can claim.
- **Judge quality.** The judge output is supplied by the caller. A judge that
  reasons badly but quotes real text will pass here every time.
"""


def render_report(rows: list[dict]) -> str:
    total = len(rows)
    passed = sum(1 for r in rows if r["ok"])
    body = [
        "# quotable_span — eval results",
        "",
        "Reproduce with `python -m quotable_span.eval` from the `lib/quotable_span` directory.",
        "Wrong cases are shown, not hidden.",
        "",
        f"**Totals: {passed}/{total} cases matched their expected status.**",
        "",
        _render_table(rows),
        "",
    ]
    misses = [r for r in rows if not r["ok"]]
    if misses:
        body.append("### Mismatches")
        for r in misses:
            body.append(f"- `{r['id']}`: expected {r['expected']}, got {r['got']} — {r['comment']}")
        body.append("")
    body.append(_NOT_MEASURED)
    return "\n".join(body)


def main() -> int:
    rows = evaluate()
    report = render_report(rows)
    _RESULTS_PATH.write_text(report, encoding="utf-8")
    print(_render_table(rows))
    total = len(rows)
    passed = sum(1 for r in rows if r["ok"])
    print(f"\n{passed}/{total} cases matched their expected status.")
    print(f"wrote {_RESULTS_PATH}")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
