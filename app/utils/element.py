from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Element(object):
    WAIT_SECONDS = 10

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, self.WAIT_SECONDS).until(
            EC.visibility_of_element_located(self.locator)
        )
        self.web_element = element
        return None

    def click(self):
        element = WebDriverWait(self.driver, self.WAIT_SECONDS).until(
            EC.element_to_be_clickable(self.locator)
        )
        element.click()
        return None

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    @property
    def text(self):
        text = self.web_element.text
        return text
