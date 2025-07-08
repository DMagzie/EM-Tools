
import os
import sys

from source_code.cbecc_to_iesve_converter import main as test_cbecc
from source_code.ashrae_idf_generator import main as test_idf
from source_code.econ1_report_generator import main as test_econ1
from source_code.dual_baseline_comparison import main as test_comparison
from source_code.manualj_load_explorer import main as test_manualj

def run_tests():
    print("\nRunning EM Explorer & Converter Tests...\n")

    tests = [
        ("CBECC to IESVE Converter", test_cbecc),
        ("ASHRAE IDF Generator", test_idf),
        ("ECON-1 Report Generator", test_econ1),
        ("Dual Baseline Comparison", test_comparison),
        ("Manual J Load Explorer", test_manualj),
    ]

    for name, test_fn in tests:
        try:
            print(f"[TEST] {name}...")
            test_fn()
            print(f"  ✅ SUCCESS\n")
        except Exception as e:
            print(f"  ❌ FAILED: {e}\n")

if __name__ == "__main__":
    run_tests()
