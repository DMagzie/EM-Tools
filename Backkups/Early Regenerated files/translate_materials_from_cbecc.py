import json

def translate_materials(model_data,
                        translation_map_path="Shared_Data/Materials/materials_translation_map.json"):
    with open(translation_map_path, "r") as f:
        translation_map = json.load(f)

    for surface in model_data.get("surfaces", []):
        cbecc_tag = surface.get("construction")
        normalized = translation_map["CBECC_to_IDF"].get(cbecc_tag)
        if normalized:
            surface["normalized_material"] = normalized
            surface["ies_tag"] = translation_map["IDF_to_IES"].get(normalized)
            surface["description"] = translation_map["Normalized_Descriptions"].get(normalized)
        else:
            surface["normalized_material"] = "UNMAPPED"
            surface["ies_tag"] = None
            surface["description"] = None

    return model_data

if __name__ == "__main__":
    input_file = "model_normalized.json"
    output_file = "model_with_materials.json"

    with open(input_file, "r") as f:
        model = json.load(f)

    enriched_model = translate_materials(model)

    with open(output_file, "w") as f:
        json.dump(enriched_model, f, indent=2)

    print(f"✅ Enriched model saved to {output_file}")
