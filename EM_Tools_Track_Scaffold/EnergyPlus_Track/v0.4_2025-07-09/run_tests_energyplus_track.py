import unittest
import os

class TestEnergyPlusTrack(unittest.TestCase):
    def test_files_exist(self):
        files = [
  "EnergyPlus_Track/v0.4_2025-07-09/idf_generator/generate_idf.py",
  "EnergyPlus_Track/v0.4_2025-07-09/econ_report/econ1_generator.py",
  "EnergyPlus_Track/v0.4_2025-07-09/outputs/eplus_output_summary.csv"
]
        for f in files:
            self.assertTrue(os.path.exists(f), f"Missing: {f}")

if __name__ == "__main__":
    unittest.main()
