import time
import unittest

from test.unit import test_argument_parsing, test_server

def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    ### unittests

    # album
    suite.addTests(loader.loadTestsFromModule(test_argument_parsing))
    suite.addTests(loader.loadTestsFromModule(test_server))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    if result.wasSuccessful():
        time.sleep(5)
        print("Success")
        exit(0)
    else:
        print("Failed")
        exit(1)


main()
