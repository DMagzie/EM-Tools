import unittest
import os
import pandas as pd
from modules import qaqc_heatmap

class TestQAQCTool(unittest.TestCase):
    def test_generate_qaqc_outputs(self):
        # Run the dummy generator
        csv_path, png_path = qaqc_heatmap.generate_dummy_qaqc_report(output_dir="EM_Explorer_Track/v0.4/outputs")

        # Check files exist
        self.assertTrue(os.path.exists(csv_path), f"Missing: {csv_path}")
        self.assertTrue(os.path.exists(png_path), f"Missing: {png_path}")

        # Check CSV content
        df = pd.read_csv(csv_path)
        self.assertIn("Zone", df.columns)
        self.assertIn("Flagged", df.columns)
        self.assertGreater(len(df), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
