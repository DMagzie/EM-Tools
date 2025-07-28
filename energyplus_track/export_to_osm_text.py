
import json
from pathlib import Path

OSM_HEADER = """<?xml version="1.0" encoding="UTF-8"?>
<OpenStudioModel xmlns="http://openstudio.nrel.gov/OSM" version="3.1.0" osm_version="3.0.0">
"""

OSM_FOOTER = "</OpenStudioModel>\n"

def zone_block(zone_id):
    return f"""  <OS:ThermalZone>
    <string>{zone_id}</string>
    <string>{zone_id}</string>
    <string></string>
    <double>0.0</double>
    <double>0.0</double>
    <double>0.0</double>
    <double>0.0</double>
    <double>0.0</double>
    <double>0.0</double>
    <string>Autocalculate</string>
    <string>Autocalculate</string>
  </OS:ThermalZone>\n"""

def space_block(zone_id):
    return f"""  <OS:Space>
    <string>{zone_id}_Space</string>
    <string></string>
    <string>{zone_id}</string>
    <string></string>
    <string></string>
    <string></string>
    <string></string>
    <string></string>
    <string></string>
    <string></string>
    <double>0</double>
    <double>0</double>
    <double>0</double>
    <double>0</double>
    <double>0</double>
    <double>0</double>
  </OS:Space>\n"""

def write_osm_from_emjson(em_json_path, osm_output_path="exports/model.osm"):
    with open(em_json_path) as f:
        model = json.load(f)

    osm_lines = [OSM_HEADER]

    # Zones and Spaces
    for zone in model["zones"]:
        zone_id = zone["zone_id"]
        osm_lines.append(zone_block(zone_id))
        osm_lines.append(space_block(zone_id))

    osm_lines.append(OSM_FOOTER)

    out_path = Path(osm_output_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        f.writelines(osm_lines)

    print(f"✅ Text-based OSM written to: {osm_output_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python export_to_osm_text.py <path_to_normalized_model.json>")
    else:
        write_osm_from_emjson(sys.argv[1])
