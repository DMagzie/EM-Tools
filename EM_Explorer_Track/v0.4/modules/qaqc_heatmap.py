"""
Module for generating QA/QC heatmaps from simulation data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def generate_dummy_qaqc_report(output_dir="outputs"):
    # Create a dummy dataframe of spatial QA/QC issues
    data = {
        "Zone": [f"Zone{i}" for i in range(1, 6)],
        "Cooling Load (kBtu/sf)": np.random.normal(30, 10, 5).round(1),
        "Flagged": [True, False, True, False, True]
    }
    df = pd.DataFrame(data)

    # Save CSV
    os.makedirs(output_dir, exist_ok=True)
    csv_path = os.path.join(output_dir, "qaqc_report.csv")
    df.to_csv(csv_path, index=False)

    # Create dummy heatmap
    heatmap_data = np.random.rand(10, 10)
    plt.imshow(heatmap_data, cmap='coolwarm', interpolation='nearest')
    plt.colorbar()
    plt.title("QAQC Heatmap")
    png_path = os.path.join(output_dir, "qaqc_map.png")
    plt.savefig(png_path)
    plt.close()

    return csv_path, png_path
