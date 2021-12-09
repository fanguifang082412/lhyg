import json
from selenium.webdriver.support.wait import WebDriverWait



class ActionElement:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, feature):
        try:
            ele = WebDriverWait(self.driver, 15, 0.5).until(lambda x: x.find_element(*feature))

        except Exception as e:
            return None

        else:
            return ele

    def execute_input(self, feature, text):
        if isinstance(feature, tuple):
            self.get_element(feature).send_keys(text)

        else:
            feature.send_keys(text)

    def execute_tap(self, feature):
        if isinstance(feature, tuple):
            self.get_element(feature).click()

        else:
            feature.click()




