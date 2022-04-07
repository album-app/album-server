import time
import unittest

from test.integration import test_integration_server


def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    ### integration

    # album
    suite.addTests(loader.loadTestsFromModule(test_integration_server))

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
