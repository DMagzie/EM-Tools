from shared import em_model


def test_em_model_import():
    assert hasattr(em_model, "__doc__")
