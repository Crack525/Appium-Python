# tests/test_ios_app.py
import unittest
from drivers.ios_driver import IOSDriver

class IOSAppTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = IOSDriver().get_driver()

    def test_launch_app(self):
        # Add the steps to check the app launch
        self.driver.implicitly_wait(10)
        self.assertTrue(self.driver.is_app_installed("com.example.iosapp"))

    def tearDown(self):
        self.driver.quit()
