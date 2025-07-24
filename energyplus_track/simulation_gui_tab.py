# simulation_gui_tab.py

import os

import streamlit as st
from simulation_engine_registry import SIMULATION_ENGINES

st.header("🔧 Run Simulation")

# Scenario and engine selection
scenario_id = st.selectbox("Select Scenario", ["Scenario 1", "Scenario 2", "Scenario 3"])
engine_name = st.selectbox("Select Simulation Engine", list(SIMULATION_ENGINES.keys()))
outdir = st.text_input("Output Directory", value="outputs/")

# Buttons to trigger actions
if st.button("Export Input Files"):
    engine = SIMULATION_ENGINES[engine_name]
    os.makedirs(outdir, exist_ok=True)
    st.write(f"Exporting input files for {engine.name}...")
    engine.export_func(scenario_id, outdir)

if st.button("Run Simulation"):
    engine = SIMULATION_ENGINES[engine_name]
    if engine.run_func:
        st.write(f"Running simulation for {engine.name}...")
        engine.run_func(os.path.join(outdir, f"{scenario_id}_model"), outdir)
    else:
        st.warning(f"Running {engine.name} directly is not supported. Please run manually.")

if st.button("Parse Results"):
    engine = SIMULATION_ENGINES[engine_name]
    if engine.parse_results_func:
        st.write(f"Parsing results for {engine.name}...")
        engine.parse_results_func(outdir)
    else:
        st.warning(f"No result parser available for {engine.name}.")
