import json
import csv

def export_material_summary(model_path="model_with_costs.json", output_csv="material_summary_export.csv"):
    with open(model_path, "r") as f:
        model = json.load(f)

    surfaces = model.get("surfaces", [])
    headers = ["SurfaceID", "NormalizedMaterial", "MaterialName", "Unit", "UnitCost_USD", "RegionAdjustment"]

    rows = []
    for s in surfaces:
        cost_info = s.get("CostInfo", {})
        rows.append([
            s.get("id"),
            s.get("normalized_material"),
            cost_info.get("MaterialName", "N/A"),
            cost_info.get("Unit", "N/A"),
            cost_info.get("UnitCost_USD", "N/A"),
            cost_info.get("RegionAdjustment", "N/A")
        ])

    with open(output_csv, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    print(f"✅ Exported material summary to {output_csv}")

if __name__ == "__main__":
    export_material_summary()
