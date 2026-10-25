# 28-row CSV cleanup & duplicate-review demonstration

**Fictional practice data only. Not a paid client project or testimonial.** This AI-assisted example was reviewed for row preservation, transparent formatting changes and flags. It demonstrates a conservative, **review-first** workflow rather than automatic data deletion.

## At a glance

| Measure | Result |
| --- | ---: |
| Original product-inventory rows | 28 |
| Rows in proposed formatting copy | 28 |
| Rows flagged for manual review | 9 |
| Potential repeated SKU + variant groups | 4 |
| Ambiguous price cells left unchanged | 1 |
| Records deleted or merged | **0** |

## What changed — and what did not

The proposed review copy trims unnecessary whitespace, standardizes SKU capitalization and variant slash spacing, and removes a currency symbol only from clearly numerical unit-price values. It is **not** a final import-ready file until the owner approves its assumptions.

Repeated SKU + variant combinations are **flagged, not erased**. Some may be legitimate inventory or stock updates rather than duplicates. An ambiguous value in sample row **016**, `22.OO` (letter O), is deliberately **not** changed to `22.00` (zero). No stock quantities are combined or recalculated.

## Files to inspect

1. [Original fictional CSV — 28 product rows](01_original_fictional.csv)
2. [Proposed formatting review — same 28 rows, no deletion](02_proposed_formatting_no_deletions.csv)
3. [Manual-review flags — 9 rows requiring decisions](03_review_flags.csv)

This specific case study consists of these CSV files and a documented manual-review process; it does not include an automated data cleaning script or claim any real customer outcome. A separate [8-row example with Python script and tests](../csv-cleanup/README.md) is available for a reproducible demonstration.

## Questions to resolve with a real client

- Are the repeated SKU + variant rows duplicate imports or legitimate separate stock updates?
- Should the quantities remain separate, be merged, or be corrected only after approval?
- What is the correct unit price for row 016?
- Which column names, identifiers, import formats, and product conventions must be preserved?

## Scope, privacy and transparency

No confidential, medical, financial, identity or customer information is used. This example is invented for portfolio purposes, not evidence of paid work or earnings. Do not share customer records or sensitive spreadsheets without permission.

The optional [$30 written-only CSV cleanup and duplicate-review service](https://contra.com/s/QmMWgq2U-spreadsheet-cleanup-and-duplicate-check-or-dollar30-csv-service) covers one non-sensitive CSV with up to 100 data rows after a free scope check and agreement. Potential duplicates are reported for a decision, not automatically deleted. Contra may charge extra platform and payment-processing fees at checkout, so review the final total before purchasing. You can also use the [free five-step CSV cleanup checklist](https://ozein41489.systeme.io/eb0524ed) without purchasing anything.

**Prepared with AI assistance.** Always review proposed changes against the original data and confirm decisions before any destructive action.
