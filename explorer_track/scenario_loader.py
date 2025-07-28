import json


def load_scenario(filepath="normalized_model.json"):
    with open(filepath) as f:
        return json.load(f)

def save_scenario(data, filepath="normalized_model.json"):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
