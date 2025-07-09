import unittest
import os

class TestReferenceDocs(unittest.TestCase):
    def test_files_exist(self):
        files = [
  "Reference_Docs/v0.4_2025-07-09/standards/ashrae_90_1_summary.md",
  "Reference_Docs/v0.4_2025-07-09/qa_qc_notes/qaqc_methodology.txt",
  "Reference_Docs/v0.4_2025-07-09/outputs/reference_table.csv"
]
        for f in files:
            self.assertTrue(os.path.exists(f), f"Missing: {f}")

if __name__ == "__main__":
    unittest.main()
