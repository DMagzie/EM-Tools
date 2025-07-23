# emtools_mvp/EnergyPlus_Track/export_to_iesve.py

import argparse
import json
import os


# Minimal IESVE MIT/INP text exporter (placeholder logic)
def write_iesve_inputs(em_json, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    building = em_json.get("building", {})
    zones = em_json.get("zones", [])

    mit_path = os.path.join(output_dir, "model.mit")
    inp_path = os.path.join(output_dir, "model.inp")

    with open(mit_path, 'w') as mit:
        mit.write(f"* Building: {building.get('name', 'Unnamed')}\n")
        mit.write(f"* Climate Zone: {building.get('climate_zone', 'Unknown')}\n")
        mit.write(f"* Area: {building.get('area_m2', 0)} m2\n")
        mit.write("* Geometry placeholder\n")

    with open(inp_path, 'w') as inp:
        inp.write("* Zones\n")
        for zone in zones:
            inp.write(f"ZONE: {zone['zone_id']} AREA: {zone.get('area_m2', 0)} SYSTEM: {zone.get('system_type', 'Unknown')}\n")

    print(f"[SUCCESS] Exported to {output_dir} (model.mit + model.inp)")

def main():
    parser = argparse.ArgumentParser(description="Export EM JSON to IESVE MIT/INP files")
    parser.add_argument("--input", required=True, help="Path to EM JSON input model")
    parser.add_argument("--output-folder", required=True, help="Path to output folder")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        raise FileNotFoundError(f"Missing: {args.input}")

    with open(args.input) as f:
        em_json = json.load(f)

    write_iesve_inputs(em_json, args.output_folder)

if __name__ == "__main__":
    main()
