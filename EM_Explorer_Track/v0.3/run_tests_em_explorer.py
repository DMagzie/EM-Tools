import unittest
import os

def load_tests(loader, standard_tests, pattern):
    test_dir = os.path.join(os.path.dirname(__file__), 'tests')
    suite = loader.discover(start_dir=test_dir, pattern='test_*.py')
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    test_loader = unittest.TestLoader()
    test_suite = load_tests(test_loader, None, None)
    runner.run(test_suite)
