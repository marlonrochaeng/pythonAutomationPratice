from selenium.webdriver.common.by import By
from .base_page import BasePage

class AuthenticationPage(BasePage):
    #locators
    _create_account = By.ID, "SubmitCreate"
    _email_create = By.ID, "email_create"

    _email_login = By.ID, "email"
    _password = By.ID, "passwd"
    _sign_in = By.ID, "SubmitLogin"

    
    def are_login_and_create_forms_displayed(self):
        return self.is_element_present(self._create_account) and self.is_element_present(self._email_create)\
                and self.is_element_present(self._email_login) and \
                self.is_element_present(self._password) and self.is_element_present(self._sign_in)