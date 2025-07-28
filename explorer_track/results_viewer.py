import pandas as pd
import streamlit as st


def run():
    st.title("📈 Results Viewer")
    st.markdown("Upload simulation results and visualize QA metrics.")
    uploaded = st.file_uploader("Upload Results CSV", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
        st.dataframe(df)
