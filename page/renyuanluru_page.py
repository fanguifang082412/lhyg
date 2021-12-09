from selenium.webdriver.common.by import By
import base


class RenyuanLuruPage(base.ActionElement):
    renyuanluru_frame_feature = By.XPATH, '//*[@id="layui-layer-iframe1"]'
    download_file_feature = By.XPATH, '/html/body/div/div/div/div/div[2]/div[1]/a'
    upload_file_feature = By.XPATH, '/html/body/div/div/div/div/div[2]/div[2]/div/input'
    upload_confirm_feature = By.XPATH, '//*[@id="test9"]'

    def get_renyuanluru_frame(self):
        return self.get_element(self.renyuanluru_frame_feature)

    def get_download_file_ele(self):
        return self.get_element(self.download_file_feature)

    def get_upload_file_ele(self):
        return self.get_element(self.upload_file_feature)

    def get_upload_confirm_ele(self):
        return self.get_element(self.upload_confirm_feature)

