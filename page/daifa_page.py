from selenium.webdriver.common.by import By
import base


class DaifaPage(base.ActionElement):
    daifa_frame_feature = By.XPATH, '//*[@id="layui-layer-iframe1"]'
    daifa_type_feature = By.XPATH, '//*[@id="modal_form"]/div[1]/div/div[1]'
    luodi_company_feature = By.XPATH, '//*[@id="modal_form"]/div[3]/div/div/div/div'
    luodi_company_confirm_feature = By.XPATH, '//*[@id="modal_form"]/div[3]/div/div/div/dl/dd[2]'
    luodi_company_type_select_feature = By.XPATH, '//*[@id="leibie"]/div/div/div/div'
    luodi_company_type_confirm_feature = By.XPATH, '//*[@id="leibie"]/div/div/div/dl/dd[2]'
    daifa_count_feature = By.XPATH, '//*[@id="modal_form"]/div[5]/div[1]/div/input'
    daifa_amt_feature = By.XPATH, '//*[@id="modal_form"]/div[5]/div[2]/div/input'
    daifa_code_feature = By.XPATH, '//*[@id="LAY-user-login-vercode"]'
    daifa_password_feature = By.XPATH, '//*[@id="modal_form"]/div[8]/div/div/input'
    upload_daifa_file_feature = By.XPATH, '//*[@id="avatar"]'
    download_daifa_file_feature = By.XPATH, '//*[@id="modal_form"]/div[9]/div'
    download_daifa_file_confirm_feature = By.XPATH, '//*[@id="modal_form"]/div[9]/div/a'
    daifa_commit_btn_feature = By.XPATH, '//*[@id="modal_form"]/div[11]/div/button[1]'

    def get_daifa_frame_ele(self):
        return self.get_element(self.daifa_frame_feature)

    def get_daifa_type_ele(self):
        return self.get_element(self.daifa_type_feature)

    def get_luodi_company_ele(self):
        return self.get_element(self.luodi_company_feature)

    def get_luodi_company_confirm_ele(self):
        return self.get_element(self.luodi_company_confirm_feature)

    def get_daifa_count_ele(self):
        return self.get_element(self.daifa_count_feature)

    def get_daifa_amt_ele(self):
        return self.get_element(self.daifa_amt_feature)

    def get_daifa_code_ele(self):
        return self.get_element(self.daifa_code_feature)

    def get_daifa_password_ele(self):
        return self.get_element(self.daifa_password_feature)

    def get_upload_daifa_file_ele(self):
        return self.get_element(self.upload_daifa_file_feature)

    def get_download_daifa_file_ele(self):
        return self.get_element(self.download_daifa_file_feature)

    def get_download_daifa_file_confirm_ele(self):
        return self.get_element(self.download_daifa_file_confirm_feature)

    def get_daifa_commit_btn_ele(self):
        return self.get_element(self.daifa_commit_btn_feature)

    def get_luodi_company_type_select_ele(self):
        return self.get_element(self.luodi_company_type_select_feature)

    def get_luodi_company_type_confirm_ele(self):
        return self.get_element(self.luodi_company_type_confirm_feature)

