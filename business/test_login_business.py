import sys, os
import time
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
import pytest
from selenium.webdriver.common.by import By
from base.get_test_data import GetTestData
import handle
import base



class TestLogin:

    def setup_class(self):
        self.driver = base.DriverUntil.get_driver()
        self.total_handle = handle.TotalHandle(self.driver)

    def setup(self):
        self.driver.get("http://47.102.168.35:8004/")

    def teardown_class(self):
        base.DriverUntil.quit_driver()

    @pytest.mark.parametrize("info", GetTestData.get_data("login_data", "login_fail"))
    def test_login_fail(self, info):
        self.total_handle.init_login().input_username(info["username"])
        self.total_handle.init_login().input_password(info["password"])
        self.total_handle.init_login().input_code(info["code"])
        time.sleep(0.5)
        self.total_handle.init_login().tap_login_btn()

        assert_ele = self.total_handle.init_login().get_login_btn_ele()
        time.sleep(0.5)
        assert True if assert_ele else False

    @pytest.mark.parametrize("info", GetTestData.get_data("login_data", "login_success"))
    def test_login_success(self, info):
        self.total_handle.init_login().input_username(info["username"])
        self.total_handle.init_login().input_password(info["password"])
        self.total_handle.init_login().input_code(info["code"])
        time.sleep(0.5)
        self.total_handle.init_login().tap_login_btn()
        assert_ele_feature = By.XPATH, '//div[contains(text(),"登入成功")]'
        assert_ele = self.total_handle.init_login().get_element(assert_ele_feature)
        time.sleep(0.5)
        assert True if assert_ele.text == "登入成功" else False









