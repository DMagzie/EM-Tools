import streamlit as st
from hvac_schedule_editor import run as run_editor
from results_viewer import run as run_results
from scenario_dashboard import run as run_dashboard
from scenario_exporter import run as run_export

st.set_page_config(page_title="EM Tools Explorer", layout="wide")

st.sidebar.title("📊 EM Tools Navigation")
tab = st.sidebar.radio("Navigate to:", [
    "Dashboard",
    "HVAC Editor",
    "Export Scenarios",
    "View Results"
])

if tab == "Dashboard":
    run_dashboard()
elif tab == "HVAC Editor":
    run_editor()
elif tab == "Export Scenarios":
    run_export()
elif tab == "View Results":
    run_results()
