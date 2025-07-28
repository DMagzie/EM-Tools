
import json
import sys
from pathlib import Path

# Force Python to use the OpenStudio SDK binding
sys.path.insert(0, "/Applications/OpenStudio-3.9.0/Ruby")
import openstudio


def export_to_osm(json_path, osm_path="exports/model_sdk.osm"):
    # Load EM JSON
    with open(json_path) as f:
        em_data = json.load(f)

    model = openstudio.model.Model()

    # Add zones and spaces
    for zone in em_data["zones"]:
        zone_name = zone["zone_id"]
        thermal_zone = openstudio.model.ThermalZone(model)
        thermal_zone.setName(zone_name)

        space = openstudio.model.Space(model)
        space.setName(f"{zone_name}_Space")
        space.setThermalZone(thermal_zone)

    # Ensure export folder exists
    osm_path = Path(osm_path)
    osm_path.parent.mkdir(parents=True, exist_ok=True)

    # Save the model
    model.save(str(osm_path), overwrite=True)
    print(f"✅ OpenStudio .osm saved to {osm_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_osm_sdk.py <path_to_normalized_model.json>")
        sys.exit(1)

    export_to_osm(sys.argv[1])
