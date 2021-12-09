from selenium.webdriver.common.by import By
import base


class HomePage(base.ActionElement):
    home_frame_feature = By.XPATH, '//*[@id="LAY_app_body"]/div/iframe'
    account_recharge_feature = By.XPATH, '//*[@id="pricing"]/div/div/div[2]/div[1]/div/h3'
    renyuan_luru_feature = By.XPATH, '//*[@id="pricing"]/div/div/div[2]/div[2]/div/h3'
    release_service_fee_feature = By.XPATH, '//*[@id="pricing"]/div/div/div[2]/div[3]/div/h3'

    def get_home_frame_ele(self):
        return self.get_element(self.home_frame_feature)

    def get_account_recharge_ele(self):
        return self.get_element(self.account_recharge_feature)

    def get_renyuan_luru_ele(self):
        return self.get_element(self.renyuan_luru_feature)

    def get_release_service_fee_ele(self):
        return self.get_element(self.release_service_fee_feature)
