import hashlib
import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import base
import handle
import os


class TestRenyuanLuru:

    def setup_class(self):
        self.driver = base.DriverUntil.get_driver()
        self.total_handle = handle.TotalHandle(self.driver)
        self.driver.get("http://47.102.168.35:8004/")
        self.total_handle.init_login().go_login("一点通股份有限公司", "123456", "8888")

    def teardown_class(self):
        base.DriverUntil.quit_driver()

    def setup(self):
        time.sleep(1)
        self.driver.get("http://47.102.168.35:8004/")

    def download_file_step(self):
        download_file_btn_feature = By.XPATH, '/html/body/div/div/div/div/div[2]/div[1]'
        download_file_btn_ele = self.total_handle.init_renyuanluru().get_element(download_file_btn_feature)
        self.total_handle.init_renyuanluru().execute_tap(download_file_btn_ele)
        self.total_handle.init_renyuanluru().tap_download_file()
        time.sleep(6)
        f = open(r"C:\Users\Administrator\Downloads\renyuanluru.xlsx", "rb")
        data = f.read()
        md5 = hashlib.md5()
        md5.update(data)
        md5_str = md5.hexdigest()
        assert True if md5_str == "4f032dd96f0a9bc3164301d9b32dd8d0" else False

    def test_download_file(self):
        self.total_handle.init_home().switch_home_frame()
        time.sleep(1)
        self.total_handle.init_home().tap_renyuan_luru()
        self.total_handle.init_renyuanluru().switch_renyuanluru_frame()

        if os.path.exists(r"C:\Users\Administrator\Downloads\renyuanluru.xlsx"):
            print("文件存在")
            os.remove(r"C:\Users\Administrator\Downloads\renyuanluru.xlsx")
            self.download_file_step()
        else:
            print("文件不存在")
            self.download_file_step()

    def test_renyuanluru(self):
        self.total_handle.init_home().switch_home_frame()
        time.sleep(1)
        self.total_handle.init_home().tap_renyuan_luru()
        self.total_handle.init_renyuanluru().switch_renyuanluru_frame()
        self.total_handle.init_renyuanluru().input_upload_file(r"C:\Users\Administrator\Desktop\renyuanluru(1).xlsx")
        time.sleep(1)
        self.total_handle.init_renyuanluru().tap_upload_confirm()
        assert_ele_feature = By.XPATH, '//*[@id="layui-layer2"]/div'
        assert_ele = self.total_handle.init_renyuanluru().get_element(assert_ele_feature)
        assert True if assert_ele.text == '人员全部录入成功' else False





