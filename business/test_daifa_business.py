import sys, os
import time

import pytest
from selenium.webdriver.common.by import By
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
import handle
import base
from base import GetTestData



class TestDaifa:

    def setup_class(self):
        self.driver = base.DriverUntil.get_driver()
        self.total_handle = handle.TotalHandle(self.driver)
        self.driver.get("http://47.102.168.35:8004/")
        self.total_handle.init_login().go_login("心悦有限公司", "123456", "8888")

    def teardown_class(self):
        base.DriverUntil.quit_driver()

    def setup(self):
        time.sleep(0.5)
        self.driver.get("http://47.102.168.35:8004/")

    def daifu_step(self, info):
        self.total_handle.init_home().switch_home_frame()
        time.sleep(0.5)
        self.total_handle.init_home().tap_release_service_fee()
        self.total_handle.init_daifa().switch_daifa_frame()
        self.total_handle.init_daifa().tap_luodi_company_select()
        self.total_handle.init_daifa().tap_luodi_company_confirm()
        time.sleep(5)
        self.total_handle.init_daifa().tap_luodi_company_type_select()
        self.total_handle.init_daifa().tap_luodi_company_type_confirm()
        self.total_handle.init_daifa().input_daifa_count(info["daifa_count"])
        self.total_handle.init_daifa().input_daifa_amt(info["daifa_amt"])
        self.total_handle.init_daifa().input_daifa_code(info["code"])
        self.total_handle.init_daifa().input_daifa_password(info["password"])

    @pytest.mark.parametrize("info", GetTestData.get_data("daifu_data", "daifu_success"))
    def test_daifa_success(self, info):
        self.daifu_step(info)
        self.total_handle.init_daifa().upload_daifa_file_ele(info["daifa_file"])
        self.total_handle.init_daifa().tap_daifa_commit_btn()
        try:
            assert_ele_feature = By.XPATH, '//*[@id="layui-layer3"]/div'
            assert_ele = self.total_handle.init_daifa().get_element(assert_ele_feature)
            assert True if assert_ele.text == "提交成功" else False
        except:
            assert_ele_feature = By.XPATH, '//*[@id="LAY_adminError"]'
            assert_ele = self.total_handle.init_daifa().get_element(assert_ele_feature)
            assert True if "代付中" in assert_ele.text else False

    @pytest.mark.parametrize("info", GetTestData.get_data("daifu_data", "luodi_company_null"))
    def test_daifa_luodi_company_null(self, info):
        self.total_handle.init_home().switch_home_frame()
        time.sleep(0.5)
        self.total_handle.init_home().tap_release_service_fee()
        self.total_handle.init_daifa().switch_daifa_frame()
        self.total_handle.init_daifa().input_daifa_count(info["daifa_count"])
        self.total_handle.init_daifa().input_daifa_amt(info["daifa_amt"])
        self.total_handle.init_daifa().input_daifa_code(info["code"])
        self.total_handle.init_daifa().input_daifa_password(info["password"])
        self.total_handle.init_daifa().upload_daifa_file_ele(info["daifa_file"])
        self.total_handle.init_daifa().tap_daifa_commit_btn()
        assert_ele = self.total_handle.init_daifa().get_daifa_commit_btn_ele()
        assert True if assert_ele else False

    @pytest.mark.parametrize("info", GetTestData.get_data("daifu_data", "daifu_fail"))
    def test_daifa_fail(self, info):
        self.daifu_step(info)
        self.total_handle.init_daifa().upload_daifa_file_ele(info["daifa_file"])
        self.total_handle.init_daifa().tap_daifa_commit_btn()
        assert_ele = self.total_handle.init_daifa().get_daifa_commit_btn_ele()
        assert True if assert_ele else False

    @pytest.mark.parametrize("info", GetTestData.get_data("daifu_data", "daifu_file_null"))
    def test_daifu_file_null(self, info):
        self.daifu_step(info)
        self.total_handle.init_daifa().tap_daifa_commit_btn()
        assert_ele = self.total_handle.init_daifa().get_daifa_commit_btn_ele()
        assert True if assert_ele else False




