import json
import os
import pandas as pd
import argparse

def load_cache(cache_file):
    if not os.path.exists(cache_file):
        print(f"❌ Cache file not found: {cache_file}")
        return None
    with open(cache_file, "r") as f:
        return json.load(f)

def analyze_cache(cache):
    df = pd.DataFrame(cache)
    if "Extension" not in df.columns:
        df["Extension"] = df["Local Path"].apply(
            lambda x: x.split(".")[-1].lower() if "." in x else "none"
        )
    summary = df["Extension"].value_counts().reset_index()
    summary.columns = ["Extension", "Count"]
    return df, summary

def analyze_cache(cache):
    files = [{"File": path, "Extension": os.path.splitext(path)[1].lower()} for path in cache.keys()]
    df = pd.DataFrame(files)
    summary = df["Extension"].value_counts().reset_index()
    summary.columns = ["Extension", "File Count"]
    return df, summary

def main():
    parser = argparse.ArgumentParser(description="Review synced files from EM Tools cache.")
    parser.add_argument("--cache", type=str, default=".last_uploaded_em_tools.json", help="Path to sync cache file")
    args = parser.parse_args()

    cache = load_cache(args.cache)
    if cache is None:
        return

    df, summary = analyze_cache(cache)

    print("\n📦 Synced File Summary by Type:")
    print(summary.to_string(index=False))

    print("\n📄 Full File List:")
    print(df.sort_values("File").to_string(index=False))

if __name__ == "__main__":
    main()
