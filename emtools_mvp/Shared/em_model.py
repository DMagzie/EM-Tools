# emtools_mvp/shared/em_model.py

import json

from jsonschema import ValidationError, validate

# Basic schema definition for EM JSON
EM_SCHEMA = {
    "type": "object",
    "required": ["building", "zones"],
    "properties": {
        "project_id": {"type": "string"},
        "building": {
            "type": "object",
            "required": ["name", "area_m2", "climate_zone"],
            "properties": {
                "name": {"type": "string"},
                "area_m2": {"type": "number"},
                "climate_zone": {"type": "string"},
                "type": {"type": "string"}
            }
        },
        "zones": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["zone_id"],
                "properties": {
                    "zone_id": {"type": "string"},
                    "area_m2": {"type": "number"},
                    "system_type": {"type": "string"},
                    "schedules": {"type": "object"}
                }
            }
        },
        "hvac_systems": {
            "type": "array",
            "items": {"type": "object"}
        }
    }
}

def validate_em_model(data):
    try:
        validate(instance=data, schema=EM_SCHEMA)
        return True, "Valid EM JSON"
    except ValidationError as e:
        return False, str(e)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Validate an EM JSON model against the schema")
    parser.add_argument("--input", required=True, help="Path to EM JSON file")
    args = parser.parse_args()

    with open(args.input) as f:
        model_data = json.load(f)

    valid, message = validate_em_model(model_data)
    if valid:
        print("[VALID]", message)
    else:
        print("[INVALID]", message)
