import json
import os

import streamlit as st

# Path to the model file (ensure it's correct for your environment)
MODEL_PATH = "test_files/sample_model.json"

def load_model(path):
    """
    Load the model from the specified path.
    """
    with open(path) as f:
        return json.load(f)

def save_model(model, path):
    """
    Save the model to the specified path.
    """
    with open(path, 'w') as f:
        json.dump(model, f, indent=2)

def run_editor():
    """
    Run the Streamlit-based editor for the HVAC model.
    """
    st.header("🔧 HVAC & Schedule Editor")

    # Check if the model file exists
    if not os.path.exists(MODEL_PATH):
        st.error(f"Model file not found: {MODEL_PATH}")
        return

    # Load the model data from the file
    model = load_model(MODEL_PATH)

    # If there are no zones in the model, show a warning
    if "zones" not in model:
        st.warning("No zones defined in model.")
        return

    # Loop through each zone and provide an editor for occupancy and system type
    for zone in model["zones"]:
        with st.expander(f"Zone: {zone['zone_id']}", expanded=True):
            # Occupancy schedule input
            new_sched = st.text_input(
                f"Occupancy Schedule for {zone['zone_id']}",
                value=zone.get("schedules", {}).get("occupancy", "N/A")
            )
            # System type input
            new_sys = st.text_input(
                f"System Type for {zone['zone_id']}",
                value=zone.get("system_type", "")
            )

            # Update the zone with new values
            zone.setdefault("schedules", {})["occupancy"] = new_sched
            zone["system_type"] = new_sys

    # Button to save the changes to the model
    if st.button("💾 Save Changes"):
        save_model(model, MODEL_PATH)
        st.success("Model updated.")

if __name__ == "__main__":
    run_editor()
