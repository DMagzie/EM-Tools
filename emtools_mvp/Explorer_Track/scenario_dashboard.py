# emtools_mvp/Explorer_Track/scenario_dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Dummy dataset (to be replaced with parsed simulation results)
DASHBOARD_DATA = """
scenario_id,metric,value,unit,climate_zone,system_type
Baseline,EUI,85,kBtu/ft2-yr,3C,PSZ-AC
Proposed,EUI,72.5,kBtu/ft2-yr,3C,PTAC
Baseline,GHG,45,kgCO2e/ft2,3C,PSZ-AC
Proposed,GHG,36,kgCO2e/ft2,3C,PTAC
Baseline,ROI,0,%,3C,PSZ-AC
Proposed,ROI,8.5,%,3C,PTAC
"""

def load_dashboard_data():
    from io import StringIO
    return pd.read_csv(StringIO(DASHBOARD_DATA))

def run_dashboard():
    st.set_page_config(layout="wide")
    st.title("📊 Scenario Comparison Dashboard")

    df = load_dashboard_data()

    scenario_filter = st.multiselect("Filter by Scenario", options=df["scenario_id"].unique(), default=df["scenario_id"].unique())
    metric_filter = st.multiselect("Select Metrics", options=df["metric"].unique(), default=df["metric"].unique())

    filtered_df = df[df["scenario_id"].isin(scenario_filter) & df["metric"].isin(metric_filter)]

    for metric in filtered_df["metric"].unique():
        subset = filtered_df[filtered_df["metric"] == metric]
        fig = px.bar(subset, x="scenario_id", y="value", color="scenario_id",
                     title=f"{metric} Comparison", labels={"value": f"{metric} ({subset['unit'].iloc[0]})"})
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    if st.button("📤 Export as CSV"):
        st.download_button("Download CSV", data=filtered_df.to_csv(index=False), file_name="dashboard_data.csv")

if __name__ == "__main__":
    run_dashboard()
