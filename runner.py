# runner.py
import unittest
import HtmlTestRunner
from tests.test_android_app import AndroidAppTest
from tests.test_ios_app import IOSAppTest

if __name__ == "__main__":
    # Create a test suite combining Android and iOS test cases
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(AndroidAppTest))
    test_suite.addTest(unittest.makeSuite(IOSAppTest))

    # Define the output folder for HTML reports
    runner = HtmlTestRunner.HTMLTestRunner(output='reports', report_name='appium_test_report', combine_reports=True)
    
    # Run the test suite
    runner.run(test_suite)
