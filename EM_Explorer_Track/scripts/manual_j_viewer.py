import pandas as pd

def load_manual_j_xlsx(path):
    return pd.read_excel(path, sheet_name=None)

def summarize_loads(data):
    summary = {}
    for sheet, df in data.items():
        total = df["Load"].sum()
        summary[sheet] = total
    return summary
