import json
from source_code.dual_baseline_comparison import compare_baselines

def test_compare():
    with open("test_files/sample_t24.json") as f1, open("test_files/sample_ashrae90.json") as f2:
        t24 = json.load(f1)
        ashrae = json.load(f2)

    result = compare_baselines(t24, ashrae)
    assert isinstance(result, list)
    assert all("end_use" in row for row in result)
    print("✅ test_compare passed.")

if __name__ == '__main__':
    test_compare()
