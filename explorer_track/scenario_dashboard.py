import pandas as pd
import plotly.express as px
import streamlit as st


def run():
    st.title("📊 Scenario Dashboard")
    st.markdown("Compare scenario-level results across metrics.")
    data = pd.DataFrame({
        "Scenario": ["Baseline", "Efficient", "All Electric"],
        "EUI": [72.1, 58.3, 46.2],
        "GHG (kgCO₂e/m²)": [55, 42, 15],
        "Lifecycle Cost ($/m²)": [120, 130, 135]
    })
    metric = st.selectbox("Select metric", ["EUI", "GHG (kgCO₂e/m²)", "Lifecycle Cost ($/m²)"])
    fig = px.bar(data, x="Scenario", y=metric, color="Scenario", title=f"{metric} by Scenario")
    st.plotly_chart(fig)
