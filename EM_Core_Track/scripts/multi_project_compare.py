import pandas as pd

def compare_scenarios(project_files):
    summaries = []
    for path in project_files:
        df = pd.read_csv(path)
        summary = df[["Scenario", "Annual_kWh", "Cost"]].mean().to_dict()
        summary["Source"] = path
        summaries.append(summary)
    return pd.DataFrame(summaries)
