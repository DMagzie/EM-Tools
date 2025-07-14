def main():
    print("Running all v0.4 tests...")
    try:
        from tests.test_dual_baseline_comparison import test_compare
        test_compare()
    except Exception as e:
        print(f"❌ Test failed: {e}")
    else:
        print("✅ All tests passed.")

if __name__ == '__main__':
    main()
