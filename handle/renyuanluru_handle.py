import page


class RenyuanLuruHandle(page.RenyuanLuruPage):

    def switch_renyuanluru_frame(self):
        self.driver.switch_to.frame(self.get_renyuanluru_frame())

    def tap_download_file(self):
        self.execute_tap(self.get_download_file_ele())

    def input_upload_file(self, file_url):
        self.execute_input(self.get_upload_file_ele(), file_url)

    def tap_upload_confirm(self):
        self.execute_tap(self.get_upload_confirm_ele())
