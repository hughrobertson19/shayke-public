# quotable_span

An LLM as judge check with one rule: the grader must quote the exact words behind its verdict, and that quote must appear character for character in the graded text. If it doesn't, the verdict is VOID.

## The honest limit

This proves the quote is real. It does not prove the quote is relevant, and it says nothing about whether a human would agree with the verdict. A grader can quote a real sentence and still reason badly from it. What this library removes is the cheapest failure: a grader that invents its evidence. Human agreement with the verdicts is under measured; see `EVAL_RESULTS.md` for what has been measured and what hasn't.

## Usage

```python
from quotable_span import Verdict, check

graded = "The invoice was sent on 3 March and paid on 9 March."
verdict = Verdict(label="PASS", quotes=["paid on 9 March"])

result = check(verdict, graded)
print(result.status)   # VALID
print(result.reason)   # every quote found verbatim

bad = Verdict(label="PASS", quotes=["paid on March 9"])
print(check(bad, graded).status)   # VOID: quote not found character for character
```

No normalisation is applied by default. Whitespace, case and punctuation all count. `check(..., strict=False)` collapses whitespace only, and says so in the result.

## Eval set

`eval/cases.json` holds a small invented set: graded texts paired with judge outputs and the expected status. Run `python -m quotable_span.eval` to reproduce `EVAL_RESULTS.md`, wrong cases included.

MIT licensed.
