import os
import pandas as pd

def extract_idf_summary(idf_folder, output_excel):
    summaries = []
    for file in os.listdir(idf_folder):
        if file.endswith(".idf"):
            summaries.append({"File": file, "Status": "Parsed (placeholder)"})
    pd.DataFrame(summaries).to_excel(output_excel, index=False)
