# emtools_mvp/Explorer_Track/streamlit_app.py

import streamlit as st
from hvac_schedule_editor import run_editor as run_schedule_editor
from scenario_dashboard import run_dashboard as run_scenario_dashboard
from measures_selector import run_selector as run_measures_selector
from financial_metrics import run_financial_ui

st.set_page_config(page_title="EM Tools Suite", layout="wide")
st.title("🔧 EM Tools – MVP Suite")

TAB_MAP = {
    "📅 HVAC + Schedule Editor": run_schedule_editor,
    "📊 Scenario Dashboard": run_scenario_dashboard,
    "🛠️ Measures Selector": run_measures_selector,
    "💰 Financial Metrics": run_financial_ui
}

selected_tab = st.sidebar.radio("Select a Module:", list(TAB_MAP.keys()))

TAB_MAP[selected_tab]()
