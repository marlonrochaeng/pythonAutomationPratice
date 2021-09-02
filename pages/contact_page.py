from selenium.webdriver.common.by import By
from .base_page import BasePage

class ContactPage(BasePage):
    #locators
    _subject = By.ID,"id_contact"
    _email = By.ID,"email"
    _order = By.ID, "id_order"
    _message = By.ID, "message"
    _send = By.ID, "submitMessage"
    _sent_message = By.XPATH, "//p[@class='alert alert-success']"
    _missing_field = By.XPATH, "//div[@class='alert alert-danger']"


    def send_message(self, subject, email, order, message):
        self.select_element_by_text(self._subject, subject)
        self.send_keys(self._email, email)
        self.send_keys(self._order, order)
        self.send_keys(self._message, message)
        self.click_on(self._send)
    
    def is_missing_field(self):
        return self.is_element_present(self._missing_field)

    def is_message_sent(self):
        return self.is_element_present(self._sent_message)
    
    