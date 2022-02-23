class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://the-internet.herokuapp.com"
        self.page_path = "/"

    def open(self):
        self.driver.get(self.base_url + self.page_path)
        return self

