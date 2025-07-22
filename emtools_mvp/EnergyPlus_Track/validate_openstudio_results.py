# emtools_mvp/EnergyPlus_Track/validate_openstudio_results.py

import argparse
import os
import json

# Placeholder validator that simulates EUI comparison

def simulate_sql_parse(sql_path):
    # Simulate pulling EUI from OpenStudio SQL file
    return {
        "EUI": 72.5,  # kBtu/ft2-year
        "UnmetHours": 120,
        "HVAC_Breakdown": {
            "Heating": 25.0,
            "Cooling": 30.0,
            "Fans": 10.0,
            "Pumps": 7.5
        }
    }

def compare_with_baseline(sim_result, baseline_json):
    baseline_eui = baseline_json.get("building", {}).get("baseline_eui", 85.0)
    delta = baseline_eui - sim_result["EUI"]
    return {
        "Simulated EUI": sim_result["EUI"],
        "Baseline EUI": baseline_eui,
        "Improvement": delta,
        "Unmet Hours": sim_result["UnmetHours"],
        "HVAC Breakdown": sim_result["HVAC_Breakdown"]
    }

def main():
    parser = argparse.ArgumentParser(description="Validate OpenStudio results against baseline")
    parser.add_argument("--sql", required=True, help="Path to eplusout.sql")
    parser.add_argument("--json", required=True, help="Path to baseline_model.json")
    args = parser.parse_args()

    if not os.path.exists(args.sql):
        raise FileNotFoundError(f"Missing: {args.sql}")
    if not os.path.exists(args.json):
        raise FileNotFoundError(f"Missing: {args.json}")

    sim_result = simulate_sql_parse(args.sql)

    with open(args.json, 'r') as f:
        baseline = json.load(f)

    report = compare_with_baseline(sim_result, baseline)

    print("\n[VALIDATION REPORT]")
    for key, value in report.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
