from selenium import webdriver


class DriverUntil:
    __driver = None

    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        if cls.__driver:
            cls.__driver.quit()
            cls.__driver = None