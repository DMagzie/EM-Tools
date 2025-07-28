from lcca_track import load_costdb


def test_load_cost_database():
    db = load_costdb.load_cost_database("test_files/mock_CostDB.xlsx")
    assert "system_costs" in db
    assert "material_costs" in db
