import streamlit as st


def run():
    st.title("🛠️ HVAC + Schedule Editor")
    st.markdown("Edit HVAC system types and assign zone schedules.")
    zone = st.selectbox("Select Zone", ["Zone A", "Zone B", "Zone C"])
    system = st.selectbox("HVAC System", ["VAV w/ Reheat", "Packaged RTU", "Heat Pump"])
    schedule = st.selectbox("Schedule", ["Office", "Residential", "24/7"])
    st.write(f"📌 Editing {zone} → System: {system}, Schedule: {schedule}")
    if st.button("Save Settings"):
        st.success("Changes saved (placeholder).")
