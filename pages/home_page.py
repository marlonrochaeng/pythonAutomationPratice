from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    #locators
    _login_field = By.ID,"search_query_top"
    _search_button = By.NAME,"submit_search"
    _contact_us = By.XPATH, "//a[@title='Contact Us']"

    def search_product(self, product):
        self.send_keys(self._login_field, product)
        self.click_on(self._search_button)

    def go_to_contact_us(self):
        self.click_on(self._contact_us)

    