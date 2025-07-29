import streamlit as st

try:
    from hvac_schedule_editor import run as run_editor
except ImportError:
    run_editor = None

def main():
    st.title("EM-Tools Scenario Explorer")

    tabs = st.tabs(["Scenario Viewer", "Export Controls", "HVAC + Schedule Editor"])

    with tabs[0]:
        st.write("Scenario viewer content goes here.")

    with tabs[1]:
        st.write("Export control options go here.")

    with tabs[2]:
        if run_editor:
            run_editor()
        else:
            st.warning("HVAC + Schedule Editor module not found.")

if __name__ == "__main__":
    main()
