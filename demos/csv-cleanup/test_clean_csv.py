"""Tests for the synthetic CSV cleanup demonstration."""
import csv
import tempfile
import unittest
from pathlib import Path
from clean_csv import clean

ROOT = Path(__file__).resolve().parent


class CsvCleanupDemoTests(unittest.TestCase):
    def test_preserves_rows_and_skus(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = ROOT / "fictional_before.csv"
            target = Path(tmp) / "review.csv"
            original_bytes = source.read_bytes()
            stats = clean(source, target)
            with target.open(newline="", encoding="utf-8") as f:
                rows = list(csv.DictReader(f))
            self.assertEqual(stats, {"rows": 8, "flagged_rows": 6})
            self.assertEqual(len(rows), 8)
            self.assertEqual(rows[0]["sku"], "0042")
            self.assertEqual(rows[0]["product_name"], "Ceramic mug")
            self.assertEqual(rows[0]["price_usd"], "12.50")
            self.assertIn("possible_duplicate_of_row_1", rows[1]["review_flag"])
            self.assertIn("review_sku_used_for_multiple_variants", rows[2]["review_flag"])
            self.assertEqual(rows[4]["review_flag"], "")
            self.assertEqual(rows[6]["price_usd"], "")
            self.assertEqual(source.read_bytes(), original_bytes)

    def test_no_overwriting_source(self):
        source = ROOT / "fictional_before.csv"
        with self.assertRaisesRegex(ValueError, "original file is never overwritten"):
            clean(source, source)

    def test_rejects_formula_looking_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "formula.csv"
            bad.write_text(
                "sku,product_name,variant,price_usd,stock\n"
                "X,=2+2,Blue,1.00,2\n", encoding="utf-8"
            )
            with self.assertRaisesRegex(ValueError, "Potential spreadsheet formula"):
                clean(bad, Path(tmp) / "out.csv")
            self.assertFalse((Path(tmp) / "out.csv").exists())

    def test_header_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "bad.csv"
            bad.write_text("wrong,columns\nX,Y\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Expected headers"):
                clean(bad, Path(tmp) / "output.csv")
            self.assertFalse((Path(tmp) / "output.csv").exists())


if __name__ == "__main__":
    unittest.main()
