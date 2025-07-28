"""
summarize_material_impact.py

Summarizes material-level embodied carbon impact per project and system (omniclass_element).
"""

import pandas as pd


def summarize_by_project_and_system(results_path, output_path):
    df = pd.read_excel(results_path)
    summary = (
        df
        .groupby(['project_index', 'omniclass_element'])
        .agg(
            total_mass_kg=('inv_mass', 'sum'),
            total_gwp_kgco2e=('gwp', 'sum'),
            avg_mui_cfa=('mui_cfa', 'mean'),
            material_count=('mat_type', 'count')
        )
        .reset_index()
    )
    summary.to_csv(output_path, index=False)
    print(f"Summary written to {output_path}")

if __name__ == "__main__":
    summarize_by_project_and_system("full_lca_results.xlsx", "material_impact_summary.csv")
