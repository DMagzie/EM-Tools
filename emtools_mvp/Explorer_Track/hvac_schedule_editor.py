# emtools_mvp/Explorer_Track/hvac_schedule_editor.py

import streamlit as st
import json
import os

MODEL_PATH = "test_files/sample_model.json"


def load_model(path):
    with open(path, 'r') as f:
        return json.load(f)

def save_model(model, path):
    with open(path, 'w') as f:
        json.dump(model, f, indent=2)

def run_editor():
    st.header("🔧 HVAC & Schedule Editor")

    if not os.path.exists(MODEL_PATH):
        st.error(f"Model file not found: {MODEL_PATH}")
        return

    model = load_model(MODEL_PATH)

    if "zones" not in model:
        st.warning("No zones defined in model.")
        return

    for zone in model["zones"]:
        with st.expander(f"Zone: {zone['zone_id']}", expanded=True):
            new_sched = st.text_input(
                f"Occupancy Schedule for {zone['zone_id']}",
                value=zone.get("schedules", {}).get("occupancy", "N/A")
            )
            new_sys = st.text_input(
                f"System Type for {zone['zone_id']}",
                value=zone.get("system_type", "")
            )
            zone.setdefault("schedules", {})["occupancy"] = new_sched
            zone["system_type"] = new_sys

    if st.button("💾 Save Changes"):
        save_model(model, MODEL_PATH)
        st.success("Model updated.")


if __name__ == "__main__":
    run_editor()
