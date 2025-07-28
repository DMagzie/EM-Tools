import streamlit as st


def run():
    st.title("📤 Scenario Export")
    st.markdown("Export current scenario to simulation formats:")
    if st.button("Export to IESVE"):
        st.success("Export to IESVE triggered (stub).")
    if st.button("Export to CBECC"):
        st.success("Export to CBECC triggered (stub).")
    if st.button("Export to OpenStudio (.osm)"):
        st.success("Export to OpenStudio triggered (stub).")
