from em_core_tools import baseline_generator


def test_baseline_generator_import():
    assert hasattr(baseline_generator, "__doc__")
