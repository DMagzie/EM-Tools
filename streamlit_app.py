
import json
from pathlib import Path

import streamlit as st

from energyplus_track.export_to_cbecc_ief import export_to_cbecc
from shared.em_model import BuildingModel

st.set_page_config(layout="wide")
st.title("EM Tools – Scenario Explorer")

uploaded_file = st.file_uploader("Upload EM JSON model", type=["json"])
if uploaded_file:
    em_data = json.load(uploaded_file)
    try:
        model = BuildingModel(**em_data)
        st.success("Model loaded and validated successfully.")
        st.json(em_data, expanded=False)
    except Exception as e:
        st.error(f"Validation failed: {e}")
        st.stop()

    if "scenario_measures" in em_data:
        st.subheader("Scenarios")
        scenarios = list(em_data["scenario_measures"].keys())
        selected = st.selectbox("Select a scenario", scenarios)
        st.write(f"Scenario selected: {selected}")
    else:
        st.warning("No scenarios found in this model.")

    st.subheader("Export Options")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Export to CBECC XML"):
            export_path = export_to_cbecc(model, output_dir=Path("exports"))
            st.success(f"Exported to: {export_path}")
            with open(export_path, "rb") as f:
                st.download_button("Download CBECC XML", f, file_name=export_path.name, mime="application/xml")
    with col2:
        if st.button("Export to EnergyPlus IDF"):
            st.info("Export to IDF triggered (placeholder)")
    with col3:
        if st.button("Export to IESVE"):
            st.info("Export to IESVE triggered (placeholder)")
else:
    st.info("Please upload a model file to begin.")
