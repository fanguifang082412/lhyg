import time
import pytest
from selenium.webdriver.common.by import By
import handle
import base


class TestRecharge:
    def setup_class(self):
        self.driver = base.DriverUntil.get_driver()
        self.total_handle = handle.TotalHandle(self.driver)
        self.driver.get("http://47.102.168.35:8004/")
        self.total_handle.init_login().go_login("一点通股份有限公司", "123456", "888")

    def teardown_class(self):
        base.DriverUntil.quit_driver()

    def setup(self):
        time.sleep(1)
        self.driver.get("http://47.102.168.35:8004/")

    def recharge_step(self, info):
        self.total_handle.init_home().switch_home_frame()
        time.sleep(1)
        self.total_handle.init_home().tap_account_recharge()
        time.sleep(1)
        self.total_handle.init_recharge().switch_recharge_frame()
        self.total_handle.init_recharge().tap_luodi_company_select()
        self.total_handle.init_recharge().tap_luodi_company()
        self.total_handle.init_recharge().input_recharge_amt(info["recharge_amt"])

    @pytest.mark.parametrize("info", base.GetTestData.get_data("recharge", "recharge_success"))
    def test_recharge_success(self, info):
        self.recharge_step(info)
        self.total_handle.init_recharge().upload_recharge_image(info["recharge_url"])
        time.sleep(1)
        self.total_handle.init_recharge().tap_recharge_commit()
        time.sleep(1)
        assert_ele_feature = By.XPATH, '//*[@id="layui-layer2"]/div'
        assert_ele = self.total_handle.init_recharge().get_element(assert_ele_feature)
        assert True if assert_ele.text == info["assert_text"] else False

    @pytest.mark.parametrize("info", base.GetTestData.get_data("recharge", "recharge_fail_01"))
    def test_recharge_iamge_null(self, info):
        self.recharge_step(info)
        time.sleep(1)
        self.total_handle.init_recharge().tap_recharge_commit()
        time.sleep(1)
        assert_ele_feature = By.XPATH, '//*[@id="LAY_adminError"]'
        assert_ele = self.total_handle.init_recharge().get_element(assert_ele_feature)
        assert True if info["assert_text"] in assert_ele.text else False

    @pytest.mark.parametrize("info", base.GetTestData.get_data("recharge", "recharge_fail_02"))
    def test_recharge_fail(self, info):
        self.recharge_step(info)
        self.total_handle.init_recharge().upload_recharge_image(info["recharge_url"])
        time.sleep(1)
        self.total_handle.init_recharge().tap_recharge_commit()
        time.sleep(1)
        assert_ele = self.total_handle.init_recharge().get_recharge_btn_ele()
        assert True if assert_ele else False





