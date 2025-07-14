
import json
import os
import pandas as pd

# Path to your local sync cache file
CACHE_FILE = ".last_uploaded_em_tools.json"

if not os.path.exists(CACHE_FILE):
    print(f"❌ Cache file not found: {CACHE_FILE}")
    exit(1)

# Load cache
with open(CACHE_FILE, "r") as f:
    cache = json.load(f)

# Build DataFrame
files = [{"File": path, "Extension": os.path.splitext(path)[1].lower()} for path in cache.keys()]
df = pd.DataFrame(files)

# Group by extension and show counts
summary = df["Extension"].value_counts().reset_index()
summary.columns = ["Extension", "File Count"]

print("\n📦 Synced File Summary by Type:")
print(summary)

print("\n📄 Full File List:")
print(df.sort_values("File").to_string(index=False))
