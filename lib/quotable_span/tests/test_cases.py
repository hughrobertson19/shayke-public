"""One assertion per eval case, plus the whole-set reproduction.

These pin the documented behaviour: exact match, case, punctuation, whitespace
(strict vs lax), line breaks, multiple quotes, empty quotes, malformed judge
output, and the real-but-irrelevant limit case.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from quotable_span import JudgeAdapter, Verdict, check
from quotable_span.eval import evaluate

_CASES = json.loads(
    (Path(__file__).resolve().parent.parent / "eval" / "cases.json").read_text(encoding="utf-8")
)["cases"]


@pytest.mark.parametrize("case", _CASES, ids=[c["id"] for c in _CASES])
def test_case_matches_expected(case):
    adapter = JudgeAdapter(
        lambda _g, _o=case["judge_output"]: _o, strict=case.get("strict", True)
    )
    result = adapter(case["graded"])
    assert result.status == case["expected"], (
        f"{case['id']}: expected {case['expected']}, got {result.status} ({result.reason})"
    )


def test_full_eval_set_reproduces_green():
    rows = evaluate()
    assert len(rows) == 20
    assert all(r["ok"] for r in rows), [r["id"] for r in rows if not r["ok"]]


# --- explicit class-by-class checks (independent of the JSON fixture) ---


def test_exact_match_is_valid():
    r = check(Verdict("pass", ["paid in full"]), "the invoice was paid in full.")
    assert r.status == "VALID"
    assert r.normalised is False


def test_case_difference_voids_under_strict():
    r = check(Verdict("pass", ["Paid in full"]), "the invoice was paid in full.")
    assert r.status == "VOID"
    assert r.missing == ["Paid in full"]


def test_punctuation_difference_voids():
    r = check(Verdict("pass", ["arrived and left"]), "arrived, and left")
    assert r.status == "VOID"


def test_whitespace_strict_voids_but_lax_valid():
    graded = "two  spaces here"
    strict = check(Verdict("pass", ["two spaces here"]), graded)
    lax = check(Verdict("pass", ["two spaces here"]), graded, strict=False)
    assert strict.status == "VOID"
    assert lax.status == "VALID"
    assert lax.normalised is True


def test_line_break_span_exact_is_valid():
    r = check(Verdict("pass", ["carried\nover"]), "the total was carried\nover the page.")
    assert r.status == "VALID"


def test_empty_quotes_is_void_with_named_reason():
    r = check(Verdict("pass", []), "anything")
    assert r.status == "VOID"
    assert r.reason == "no quote given"


def test_multiple_quotes_one_missing_reports_the_missing_one():
    r = check(Verdict("pass", ["arrived", "vanished"]), "the box arrived intact.")
    assert r.status == "VOID"
    assert r.missing == ["vanished"]


def test_real_but_irrelevant_quote_is_valid():
    graded = "the refund was approved. the sky was clear."
    r = check(Verdict("refund denied", ["the sky was clear"]), graded)
    assert r.status == "VALID"


# --- JudgeAdapter malformed handling ---


def test_adapter_non_mapping_voids():
    r = JudgeAdapter(lambda _g: ["pass"])("text")
    assert r.status == "VOID"
    assert "mapping" in r.reason


def test_adapter_missing_quotes_field_names_it():
    r = JudgeAdapter(lambda _g: {"label": "pass"})("text")
    assert r.status == "VOID"
    assert "quotes" in r.reason


def test_adapter_missing_label_field_names_it():
    r = JudgeAdapter(lambda _g: {"quotes": ["x"]})("text")
    assert r.status == "VOID"
    assert "label" in r.reason


def test_adapter_quotes_wrong_type_voids():
    r = JudgeAdapter(lambda _g: {"label": "pass", "quotes": "x"})("text")
    assert r.status == "VOID"


def test_adapter_raising_judge_voids_not_crashes():
    def boom(_g):
        raise RuntimeError("model down")

    r = JudgeAdapter(boom)("text")
    assert r.status == "VOID"
    assert "raised" in r.reason
