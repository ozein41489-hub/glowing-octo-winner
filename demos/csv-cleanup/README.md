# Review-first CSV cleanup — fictional demonstration

**This is an original, synthetic practice example, not a customer result or testimonial.** The example and Python script were AI-assisted and checked with four local automated tests.

## What the demo shows

- Eight fictional product rows before cleanup; eight rows after. **No rows automatically deleted.**
- Trims surrounding whitespace in a separate review copy; preserves text identifiers such as SKU `0042`.
- Flags two possible repeated records (data rows 2 and 6) without assuming deletion is correct.
- Flags a SKU reused across Blue and Red variants, a missing price, and an unspecified variant for human decisions.
- Rejects spreadsheet-formula-looking cell contents rather than exporting possible active spreadsheet formulas.
- Uses only the Python standard library. No database, login, API, payment, or customer data.

## Preview

| Data row | Example issue | Result |
| --- | --- | --- |
| 2 | Similar to row 1 after whitespace cleanup | Marked as possible duplicate; **kept** |
| 3 | SKU `0042` also used for a Blue variant | Marked for product-owner review; **kept** |
| 5 | Medium-size T-shirt has its own SKU | **Kept without a warning** |
| 6 | Matches T-shirt row 4 | Marked as possible duplicate; **kept** |
| 7 | Missing price | Flagged, **not guessed** |
| 8 | Blank variant | Flagged as possibly optional |

## Files

- [`fictional_before.csv`](fictional_before.csv) — untouched sample source
- [`fictional_after_review.csv`](fictional_after_review.csv) — sample whitespace-normalized review copy and row-level flags
- [`clean_csv.py`](clean_csv.py) — standalone script to repeat the process on the included sample
- [`test_clean_csv.py`](test_clean_csv.py) — four tests covering row preservation, identifier handling, overwrite protection, formula screening, and input headers

```bash
python clean_csv.py fictional_before.csv my_review.csv
python -m unittest discover -p 'test_*.py' -v
```

This example assumes the five exact sample columns and uses conservative safety rules; it is not a universal CSV cleaner. A real client file requires agreed column meanings, allowed edits, permission, and human review of flagged values. Never send passwords, bank account details, health information, government IDs, or other sensitive personal records.

## Free guide and optional service

- [Free five-step CSV cleanup guide](https://ozein41489.systeme.io/eb0524ed) — usable without signing up
- [Optional $30 written-only CSV cleanup service](https://contra.com/s/QmMWgq2U-spreadsheet-cleanup-and-duplicate-check-or-dollar30-csv-service) — one non-sensitive CSV file, up to 100 data rows, subject to a free scope check and agreement before work begins

No purchases are needed to use the demonstration or guide. This repository demonstrates a workflow; it does **not** establish completed client jobs, earnings, or fully unattended processing.
