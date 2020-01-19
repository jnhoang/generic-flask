import unittest

# import test modules here
# from tests.test_main_controller       import TestMainController

# run the tests by entering `python test_all.py`
if __name__ == '__main__':
  tests = unittest.TestSuite()

  all_tests = [
    # unit tests

    # integration tests

    # service tests

    # db tests

    # etc
  ]

  for t in all_tests:
    tests.addTests(t)

  result = unittest.TextTestRunner(verbosity=2, buffer=True).run(tests)
