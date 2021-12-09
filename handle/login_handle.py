import time

import allure

import page


class LoginHandle(page.LoginPage):

    @allure.step("输入用户名")
    def input_username(self, username):
        allure.attach("用户名:","%s" % username)
        self.execute_input(self.get_username_ele(), username)

    @allure.step("输入密码")
    def input_password(self, password):
        allure.attach("密码:", "%s" % password)
        self.execute_input(self.get_password_ele(), password)

    @allure.step("输入验证码")
    def input_code(self, code):
        allure.attach("验证码:", "%s" % code)
        self.execute_input(self.get_code_ele(), code)

    @allure.step("点击登录")
    def tap_login_btn(self):
        self.execute_tap(self.get_login_btn_ele())

    def go_login(self, username, password, code):
        self.input_username(username)
        self.input_password(password)
        self.input_code(code)
        time.sleep(1)
        self.tap_login_btn()