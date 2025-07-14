import pandas as pd

def format_for_excel_output(inputs_dict, output_path):
    df = pd.DataFrame.from_dict(inputs_dict)
    df.to_excel(output_path, index=False)
