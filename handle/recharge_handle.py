import page


class RechargeHandle(page.RechargePage):

    def switch_recharge_frame(self):
        self.driver.switch_to.frame(self.get_recharge_frame())

    def tap_luodi_company(self):
        self.execute_tap(self.get_luodi_company_ele())

    def input_recharge_amt(self, recharge_amt):
        self.execute_input(self.get_recharge_amt_ele(), recharge_amt)

    def upload_recharge_image(self, recharge_iamge):
        self.execute_input(self.get_upload_image_ele(), recharge_iamge)

    def tap_recharge_commit(self):
        self.execute_tap(self.get_recharge_btn_ele())

    def tap_luodi_company_select(self):
        self.execute_tap(self.get_luodi_company_select())