import pandas as pd

def export_manual_j(load_dict, output_path):
    df = pd.DataFrame.from_dict(load_dict, orient='index', columns=['Load (BTU/hr)'])
    df.index.name = "Room"
    df.to_excel(output_path)
