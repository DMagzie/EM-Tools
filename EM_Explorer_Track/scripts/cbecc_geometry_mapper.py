import json

def extract_geometry(cbecc_json_path):
    with open(cbecc_json_path) as f:
        model = json.load(f)
    surfaces = model.get("Surfaces", [])
    return [{"id": s["id"], "area": s.get("area", 0), "azimuth": s.get("azimuth", 0)} for s in surfaces]
