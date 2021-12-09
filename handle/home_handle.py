import page


class HomeHandle(page.HomePage):

    def switch_home_frame(self):
        self.driver.switch_to.frame(self.get_home_frame_ele())

    def tap_account_recharge(self):
        self.execute_tap(self.get_account_recharge_ele())

    def tap_renyuan_luru(self):
        self.execute_tap(self.get_renyuan_luru_ele())

    def tap_release_service_fee(self):
        self.execute_tap(self.get_release_service_fee_ele())