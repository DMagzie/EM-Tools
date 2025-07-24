from em_core_tools import scenario_manager


def test_scenario_manager_import():
    assert hasattr(scenario_manager, "__doc__")
