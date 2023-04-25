import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that

class AppiumConfig:
    @pytest.fixture(scope='function',autouse=True)
    def handle_App_launch(self):
        des_cap={
            "deviceName": "oneplus",
            "app": r"C:\Components\nykaa-fashion-2-1-2.apk",
            "udid": "emulator-5554",
            "platformName": "Android",

        }

        self.driver=webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()

class TestAddProduct(AppiumConfig):
    def test_add_product(self):
        self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Skip']").click()
        # swipe until //luxe presence

        # while len(self.driver.find_elements(AppiumBy.XPATH, "//*[@text='Luxe']")) == 0:
        #     self.driver.swipe(699,743,677,1695,1000)
        para_dic = {"strategy": AppiumBy.ANDROID_UIAUTOMATOR, "selector": 'UiSelector().text("Luxe")'}
        self.driver.execute_script("mobile: scroll", para_dic)
        self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Luxe']").click()

        time.sleep(5)







