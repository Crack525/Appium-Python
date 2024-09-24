# drivers/ios_driver.py
from appium import webdriver

class IOSDriver:
    def get_driver(self):
        capabilities = {
            "platformName": "iOS",
            "deviceName": "iPhone Simulator",
            "app": "/path/to/your/ios_app.app",
            "automationName": "XCUITest"
        }
        return webdriver.Remote("http://localhost:4723/wd/hub", capabilities)
