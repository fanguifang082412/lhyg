import handle


class TotalHandle:
    def __init__(self, driver):
        self.driver = driver

    def init_login(self):
        return handle.LoginHandle(self.driver)

    def init_home(self):
        return handle.HomeHandle(self.driver)

    def init_recharge(self):
        return handle.RechargeHandle(self.driver)

    def init_renyuanluru(self):
        return handle.RenyuanLuruHandle(self.driver)

    def init_daifa(self):
        return handle.DaifaHandle(self.driver)