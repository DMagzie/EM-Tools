import unittest
import os

class TestLCCATrack(unittest.TestCase):
    def test_files_exist(self):
        files = [
  "LCCA_Track/v0.4_2025-07-09/format_inputs/format_lcca_inputs.py",
  "LCCA_Track/v0.4_2025-07-09/lcca_xlsm/LCCA_Tool_v0.04.xlsm",
  "LCCA_Track/v0.4_2025-07-09/notes/module_connections.txt"
]
        for f in files:
            self.assertTrue(os.path.exists(f), f"Missing: {f}")

if __name__ == "__main__":
    unittest.main()
