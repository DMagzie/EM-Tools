
# Note: This script requires OpenStudio CLI to be installed and available in PATH.

import json
import subprocess
from pathlib import Path

import openstudio


def export_to_osm(em_json_path, output_path="exports/model.osm"):
    with open(em_json_path) as f:
        data = json.load(f)

    model = openstudio.model.Model()

    # Add thermal zones
    for zone in data["zones"]:
        tz = openstudio.model.ThermalZone(model)
        tz.setName(zone["zone_id"])

        # Create a space and assign to the zone
        space = openstudio.model.Space(model)
        space.setName(f"{zone['zone_id']}_Space")
        space.setThermalZone(tz)

    # Ensure export directory exists
    out_path = Path(output_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # Save model to OSM
    model.save(str(out_path), True)
    print(f"✅ OSM model exported to: {output_path}")

    # Call OpenStudio CLI to convert OSM to IDF
    idf_path = out_path.with_suffix(".idf")
    try:
        subprocess.run(["openstudio", "modeltoidf", str(out_path)], check=True)
        print(f"✅ IDF file generated: {idf_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error generating IDF: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python export_to_osm.py <path_to_emjson>")
    else:
        export_to_osm(sys.argv[1])
