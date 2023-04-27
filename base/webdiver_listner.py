import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from utilities import read_utils


class AppiumConfig:
    @pytest.fixture(scope='function', autouse=True)
    def handle_App_launch(self):
        json_dic = read_utils.get_dic_from_json("../test_data/config.json")

        if json_dic['device'] == 'local':
            des_cap = {
                "platformVersion": "andorid",
                "deviceName": "oneplus",
                "app": r"C:\Components\nykaa-fashion-2-1-2.apk",
                "udid": "emulator-5554"

            }

            self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",
                                           desired_capabilities=des_cap)

        else:
            des_cap = {

                "app": "bs://3a105a234e00d3cabfba4d2bf029ef9620c3d9ec",
                "platformVersion": "9.0",
                "deviceName": "Google Pixel 3",
                "bstack:options": {
                    "projectName": "First Python project",
                    "buildName": "browserstack-build-1",
                    "sessionName": "BStack first_test",
                    # Set your access credentials
                    "userName": "konikanegi_4hX5RP",
                    "accessKey": "YvRitqyW7EuQV2gupZCX"

                }

            }

            self.driver = webdriver.Remote(command_executor="http://hub.browserstack.com/wd/hub",desired_capabilities=des_cap)

        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()