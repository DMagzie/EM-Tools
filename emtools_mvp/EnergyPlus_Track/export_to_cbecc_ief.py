# emtools_mvp/EnergyPlus_Track/export_to_cbecc_ief.py

import argparse
import json
import os

# Minimal XML writer for CBECC IEF format (placeholder logic)
def write_cbecc_xml(em_json, output_path):
    building = em_json.get("building", {})
    zones = em_json.get("zones", [])

    with open(output_path, 'w') as f:
        f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
        f.write("<CBECCModel>\n")
        f.write(f"  <Building name=\"{building.get('name', 'Unnamed')}\" ")
        f.write(f"climateZone=\"{building.get('climate_zone', 'Unknown')}\" ")
        f.write(f"type=\"{building.get('type', 'Unknown')}\"/>\n")

        f.write("  <Zones>\n")
        for zone in zones:
            f.write(f"    <Zone id=\"{zone['zone_id']}\" area=\"{zone.get('area_m2', 0)}\" />\n")
        f.write("  </Zones>\n")

        f.write("</CBECCModel>\n")

    print(f"[SUCCESS] Exported to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Export EM JSON to CBECC .xml file")
    parser.add_argument("--input", required=True, help="Path to EM JSON input model")
    parser.add_argument("--output", required=True, help="Path to output .xml file")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        raise FileNotFoundError(f"Missing: {args.input}")

    with open(args.input, 'r') as f:
        em_json = json.load(f)

    write_cbecc_xml(em_json, args.output)

if __name__ == "__main__":
    main()
