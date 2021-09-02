from selenium.webdriver.common.by import By
from .base_page import BasePage

class ResultPage(BasePage):
    #locators
    _add_to_cart = By.XPATH, "//button[@name='Submit']"
    _proceed_to_checkout = By.XPATH, "//a[@title='Proceed to checkout']"
    _final_checkout = By.XPATH, "(//a[@title='Proceed to checkout'])[2]"
    
    def get_searched_product(self, product):
        return By.XPATH, f"//a[@class='product-name' and contains(text(),'{product}')]"
    
    def get_cart_product(self, product):
        return By.XPATH, f"//a[contains(text(),'{product}')]"

    def get_wrong_searched_product(self, product):
        return By.XPATH, f"//p[@class='alert alert-warning' and contains(text(),'{product}')]"

    def is_wrong_product_message_displayed(self, product):
        return self.is_element_present(self.get_wrong_searched_product(product))

    def is_product_displayed(self, product):
        return self.is_element_present(self.get_searched_product(product))

    def is_product_displayed_in_cart(self, product):
        return self.is_element_present(self.get_cart_product(product))

    def add_to_cart(self, product):
        product_el = self.get_searched_product(product)
        self.click_on(product_el)

        self.click_on(self._add_to_cart)

    def go_to_checkout(self):
        self.click_on(self._proceed_to_checkout)

    def go_to_final_checkout(self):
        self.click_on(self._final_checkout)
