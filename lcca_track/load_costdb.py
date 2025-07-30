import pandas as pd


def load_cost_database(file_path="test_files/mock_CostDB.xlsx"):
    """Load system and material cost data from Excel file."""
    xls = pd.ExcelFile(file_path)
    system_costs = pd.read_excel(xls, 'System Costs')
    material_costs = pd.read_excel(xls, 'Material Costs')
    labor_markups = pd.read_excel(xls, 'Labor Markups')
    escalation = pd.read_excel(xls, 'Escalation')
    return {
        "system_costs": system_costs,
        "material_costs": material_costs,
        "labor_markups": labor_markups,
        "escalation": escalation
    }
