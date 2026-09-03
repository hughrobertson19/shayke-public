# quotable_span — eval results

Reproduce with `python -m quotable_span.eval` from the `lib/quotable_span` directory.
Wrong cases are shown, not hidden.

**Totals: 20/20 cases matched their expected status.**

| case | strict | expected | got | ok |
| --- | --- | --- | --- | --- |
| c01_exact_match | true | VALID | VALID | yes |
| c02_case_difference_strict | true | VOID | VOID | yes |
| c03_punctuation_difference_strict | true | VOID | VOID | yes |
| c04_whitespace_difference_strict | true | VOID | VOID | yes |
| c05_whitespace_difference_lax | false | VALID | VALID | yes |
| c06_line_break_span_exact | true | VALID | VALID | yes |
| c07_line_break_collapsed_lax | false | VALID | VALID | yes |
| c08_multiple_quotes_all_present | true | VALID | VALID | yes |
| c09_multiple_quotes_one_missing | true | VOID | VOID | yes |
| c10_empty_quotes | true | VOID | VOID | yes |
| c11_malformed_missing_quotes_field | true | VOID | VOID | yes |
| c12_malformed_not_a_mapping | true | VOID | VOID | yes |
| c13_malformed_quotes_wrong_type | true | VOID | VOID | yes |
| c14_malformed_missing_label | true | VOID | VOID | yes |
| c15_real_but_irrelevant_quote | true | VALID | VALID | yes |
| c16_tab_vs_space_lax | false | VALID | VALID | yes |
| c17_substring_midword | true | VALID | VALID | yes |
| c18_case_lax_still_void | false | VOID | VOID | yes |
| c19_punctuation_lax_still_void | false | VOID | VOID | yes |
| c20_empty_graded_text | true | VOID | VOID | yes |

## What this does not measure

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
