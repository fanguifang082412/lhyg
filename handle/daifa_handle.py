import page


class DaifaHandle(page.DaifaPage):

    def switch_daifa_frame(self):
        self.driver.switch_to.frame(self.get_daifa_frame_ele())

    def tap_daifa_type(self):
        self.execute_tap(self.get_daifa_type_ele())

    def tap_luodi_company_select(self):
        self.execute_tap(self.get_luodi_company_ele())

    def tap_luodi_company_confirm(self):
        self.execute_tap(self.get_luodi_company_confirm_ele())

    def input_daifa_count(self, count):
        self.execute_input(self.get_daifa_count_ele(), count)

    def input_daifa_amt(self, amt):
        self.execute_input(self.get_daifa_amt_ele(), amt)

    def input_daifa_code(self, code):
        self.execute_input(self.get_daifa_code_ele(), code)

    def input_daifa_password(self, password):
        self.execute_input(self.get_daifa_password_ele(), password)

    def upload_daifa_file_ele(self, file):
        self.execute_input(self.get_upload_daifa_file_ele(), file)

    def tap_download_daifa_file(self):
        self.execute_tap(self.get_download_daifa_file_ele())

    def tap_download_daifa_file_confirm(self):
        self.execute_tap(self.get_download_daifa_file_confirm_ele())

    def tap_daifa_commit_btn(self):
        self.execute_tap(self.get_daifa_commit_btn_ele())

    def tap_luodi_company_type_select(self):
        self.execute_tap(self.get_luodi_company_type_select_ele())

    def tap_luodi_company_type_confirm(self):
        self.execute_tap(self.get_luodi_company_type_confirm_ele())