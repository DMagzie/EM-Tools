from explorer_track import streamlit_app


def test_streamlit_app_import():
    assert hasattr(streamlit_app, "__doc__")
