#!/usr/bin/env python3
"""Review-first CSV cleanup demo. Synthetic sample data only."""
import argparse
import csv
from collections import Counter
from pathlib import Path

COLUMNS = ("sku", "product_name", "variant", "price_usd", "stock")


def clean(source: Path, destination: Path) -> dict:
    if source.resolve() == destination.resolve():
        raise ValueError("Use a different output path; the original file is never overwritten.")

    with source.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or tuple(reader.fieldnames) != COLUMNS:
            raise ValueError("Expected headers: " + ", ".join(COLUMNS))
        original = list(reader)

    rows = [{key: (row[key] or "").strip() for key in COLUMNS} for row in original]
    # Refuse spreadsheet-formula-looking cells instead of exporting potentially active formulas.
    if any(value.startswith(("=", "+", "-", "@")) for row in rows for value in row.values()):
        raise ValueError("Potential spreadsheet formula detected; manual review required.")
    sku_variants = {}
    for row in rows:
        sku_variants.setdefault(row["sku"], set()).add(row["variant"])

    first_seen = {}
    flagged = Counter()
    for index, row in enumerate(rows, start=1):
        flags = []
        row_signature = tuple(row[key] for key in COLUMNS)
        if row_signature in first_seen:
            flags.append(f"possible_duplicate_of_row_{first_seen[row_signature]}")
        else:
            first_seen[row_signature] = index
        if row["sku"] and len(sku_variants[row["sku"]]) > 1:
            flags.append("review_sku_used_for_multiple_variants")
        if not row["price_usd"]:
            flags.append("missing_price")
        if not row["variant"]:
            flags.append("check_if_variant_optional")
        row["review_flag"] = "; ".join(flags)
        for flag in flags:
            flagged[flag.split("_of_row_")[0]] += 1

    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=(*COLUMNS, "review_flag"), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    assert len(rows) == len(original)
    return {"rows": len(rows), "flagged_rows": sum(bool(row["review_flag"]) for row in rows)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Normalize whitespace and flag questionable CSV rows")
    parser.add_argument("input", type=Path, help="Original CSV (will not be modified)")
    parser.add_argument("output", type=Path, help="Separate review copy")
    args = parser.parse_args()
    result = clean(args.input, args.output)
    print(f"Preserved {result['rows']} data rows; flagged {result['flagged_rows']} for human review.")
