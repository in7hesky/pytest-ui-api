from app.pages.base_page import BasePage
from app.utils.element import Element
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    @property
    def main_title(self):
        return Element(self.driver, (By.TAG_NAME, "h1"))


