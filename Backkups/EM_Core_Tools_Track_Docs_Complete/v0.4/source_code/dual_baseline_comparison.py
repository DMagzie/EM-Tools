def compare_baselines(t24_data, ashrae_data):
    comparison = []
    for key in t24_data:
        if key in ashrae_data:
            t24 = t24_data[key]
            ashrae = ashrae_data[key]
            delta = ashrae - t24
            pct_change = (delta / t24) * 100 if t24 else None
            comparison.append({
                "end_use": key,
                "T24_kBtu": t24,
                "ASHRAE_90.1_kBtu": ashrae,
                "Delta_kBtu": delta,
                "Percent_Change": pct_change
            })
    return comparison

def main():
    import json
    with open("test_files/sample_t24.json") as f1, open("test_files/sample_ashrae90.json") as f2:
        t24 = json.load(f1)
        ashrae = json.load(f2)
    result = compare_baselines(t24, ashrae)
    with open("outputs/baseline_comparison.csv", "w") as out:
        out.write("end_use,T24_kBtu,ASHRAE_90.1_kBtu,Delta_kBtu,Percent_Change\n")
        for row in result:
            out.write(f"{row['end_use']},{row['T24_kBtu']},{row['ASHRAE_90.1_kBtu']},{row['Delta_kBtu']},{row['Percent_Change']:.2f}\n")
    print("✅ Comparison complete. Output written to outputs/baseline_comparison.csv")

if __name__ == '__main__':
    main()
