# tests/test_android_app.py
import unittest
from drivers.android_driver import AndroidDriver

class AndroidAppTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = AndroidDriver().get_driver()

    def test_launch_app(self):
        # Add the steps to check the app launch
        self.driver.implicitly_wait(10)
        self.assertTrue(self.driver.is_app_installed("com.example.androidapp"))

    def tearDown(self):
        self.driver.quit()
