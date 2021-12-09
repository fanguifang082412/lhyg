from selenium.webdriver.common.by import By
import base


class RechargePage(base.ActionElement):

    recharge_frame_feature = By.XPATH, '//*[@id="layui-layer-iframe1"]'
    luodi_company_feature = By.XPATH, '//*[@id="modal_form"]/div[2]/div/div/dl/dd[2]'
    recharge_amt_feature = By.XPATH, '//*[@id="modal_form"]/div[5]/div[1]/div/input'
    upload_image_feature = By.XPATH, '//*[@id="modal_form"]/div[6]/div[2]/div/input'
    recharge_btn_feature = By.XPATH, '//*[@id="modal_form"]/div[7]/div/button[1]'
    luodi_company_select_feature = By.XPATH, '//*[@id="modal_form"]/div[2]/div/div/div/input'

    def get_recharge_frame(self):
        return self.get_element(self.recharge_frame_feature)

    def get_luodi_company_ele(self):
        return self.get_element(self.luodi_company_feature)

    def get_recharge_amt_ele(self):
        return self.get_element(self.recharge_amt_feature)

    def get_upload_image_ele(self):
        return self.get_element(self.upload_image_feature)

    def get_recharge_btn_ele(self):
        return self.get_element(self.recharge_btn_feature)

    def get_luodi_company_select(self):
        return self.get_element(self.luodi_company_select_feature)