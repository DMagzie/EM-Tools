from em_core_tools import manual_j_module


def test_manual_j_module_import():
    assert hasattr(manual_j_module, "__doc__")
