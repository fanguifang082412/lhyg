from selenium.webdriver.common.by import By
import base


class LoginPage(base.ActionElement):

    username_feature = By.XPATH, '//*[@id="LAY-user-login-username"]'
    password_feature = By.XPATH, '//*[@id="LAY-user-login-password"]'
    login_btn_feature = By.XPATH, '//*[@id="LAY-user-login"]/div/div[2]/div[5]/button'
    code_feature = By.XPATH, '//*[@id="LAY-user-login-vercode"]'

    def get_username_ele(self):
        return self.get_element(self.username_feature)

    def get_password_ele(self):
        return self.get_element(self.password_feature)

    def get_code_ele(self):
        return self.get_element(self.code_feature)

    def get_login_btn_ele(self):
        return self.get_element(self.login_btn_feature)