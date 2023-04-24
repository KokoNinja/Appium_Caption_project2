import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

class AppiumConfig:
    @pytest.fixture(scope='function',autouse=True)
    def handle_App_launch(self):
        des_cap={
            "platformVersion":"andorid",
            "deviceName": "oneplus",
            "app": r"C:\Components\nykaa-fashion-2-1-2.apk",
            "udid": "emulator-5554"


        }

        self.driver=webdriver.Remote(command_executor="http://localhost:4723/wd/hub",desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


