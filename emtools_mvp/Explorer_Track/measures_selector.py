# emtools_mvp/Explorer_Track/measures_selector.py

import streamlit as st
import os
import json

MODEL_PATH = "test_files/sample_model.json"
MEASURES_FOLDER = "test_files/sample_measures/"


def load_model(path):
    with open(path, 'r') as f:
        return json.load(f)

def save_model(model, path):
    with open(path, 'w') as f:
        json.dump(model, f, indent=2)

def list_measures():
    if not os.path.exists(MEASURES_FOLDER):
        return []
    return [f for f in os.listdir(MEASURES_FOLDER) if f.endswith(".rb") or f.endswith(".zip")]

def run_selector():
    st.header("🛠️ Scenario Measures Selector")

    if not os.path.exists(MODEL_PATH):
        st.error(f"Missing: {MODEL_PATH}")
        return

    model = load_model(MODEL_PATH)
    available_measures = list_measures()

    if "scenario_measures" not in model:
        model["scenario_measures"] = {}

    selected = st.multiselect(
        "Select Measures to Apply to This Scenario:",
        options=available_measures,
        default=model["scenario_measures"].get("sample_scenario", [])
    )

    if st.button("💾 Save Selected Measures"):
        model["scenario_measures"]["sample_scenario"] = selected
        save_model(model, MODEL_PATH)
        st.success("Measure selections saved.")

    if selected:
        st.info("These measures will be applied before export or simulation.")
        for measure in selected:
            st.code(measure)

if __name__ == "__main__":
    run_selector()
