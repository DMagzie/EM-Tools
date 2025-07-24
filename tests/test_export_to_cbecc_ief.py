from energyplus_track import export_to_cbecc_ief


def test_export_to_cbecc_ief_import():
    assert hasattr(export_to_cbecc_ief, "__doc__")
