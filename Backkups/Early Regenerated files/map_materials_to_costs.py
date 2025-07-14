import csv
import json

def load_rsmeans_costs(path="Shared_Data/Materials/RSMeans_material_costs.csv"):
    costs = {}
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            costs[row["AssemblyID"]] = {
                "MaterialName": row["MaterialName"],
                "Unit": row["Unit"],
                "UnitCost_USD": float(row["UnitCost_USD"]),
                "RegionAdjustment": float(row["RegionAdjustment"])
            }
    return costs

def map_costs_to_model(model_path, lookup_path="Shared_Data/Materials/material_lookup_tables.json",
                       rsmeans_path="Shared_Data/Materials/RSMeans_material_costs.csv",
                       output_path="model_with_costs.json"):

    with open(model_path, "r") as f:
        model = json.load(f)

    with open(lookup_path, "r") as f:
        material_map = json.load(f)

    cost_data = load_rsmeans_costs(rsmeans_path)

    for surface in model.get("surfaces", []):
        norm = surface.get("normalized_material")
        rs_id = None

        for group in material_map.values():
            if isinstance(group, dict) and group.get("NormalizedName") == norm:
                rs_id = group.get("RSMeans_ID")

        if rs_id and rs_id in cost_data:
            surface["CostInfo"] = cost_data[rs_id]
        else:
            surface["CostInfo"] = {"error": "No cost mapping"}

    with open(output_path, "w") as f:
        json.dump(model, f, indent=2)

    print(f"✅ Model with cost data saved to {output_path}")

if __name__ == "__main__":
    map_costs_to_model("model_with_materials.json")
