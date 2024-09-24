# drivers/android_driver.py
from appium import webdriver

class AndroidDriver:
    def get_driver(self):
        capabilities = {
            "platformName": "Android",
            "deviceName": "Android Emulator",
            "app": "/path/to/your/android_app.apk",
            "automationName": "UiAutomator2"
        }
        return webdriver.Remote("http://localhost:4723/wd/hub", capabilities)
