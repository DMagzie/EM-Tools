import unittest
import os

class TestEMCoreTools(unittest.TestCase):
    def test_files_exist(self):
        files = [
  "EM_Core_Tools/v0.4_2025-07-09/comparison_module/dual_baseline_comparison.py",
  "EM_Core_Tools/v0.4_2025-07-09/docs/comparison_notes.txt",
  "EM_Core_Tools/v0.4_2025-07-09/outputs/baseline_results.csv"
]
        for f in files:
            self.assertTrue(os.path.exists(f), f"Missing: {f}")

if __name__ == "__main__":
    unittest.main()
