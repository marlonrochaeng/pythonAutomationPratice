import pytest
from pages.home_page import HomePage
from pages.contact_page import ContactPage
import unittest
import time
from ddt import data, ddt, unpack
from utils.read_data import getCsvData


@pytest.mark.usefixtures("BrowserSetUp")
@ddt
class SentMessageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def ClassSetup(self, BrowserSetUp):
        self.home_page = HomePage(self.driver)
        self.contact_page = ContactPage(self.driver)
        self.home_page.go_to_test_url()

        yield

        self.driver.quit()

    @data(*getCsvData('data/send_message.csv'))
    @unpack
    def test_send_message(self, subject, email, order, message):              
        self.home_page.go_to_contact_us()
        self.contact_page.send_message(subject, email, order, message)
        assert self.contact_page.is_message_sent()
        

    @data(*getCsvData('data/send_wrong_message.csv'))
    @unpack
    def test_search_wrong_product(self, subject, email, order, message):              
        self.home_page.go_to_contact_us()
        self.contact_page.send_message(subject, email, order, message)
        assert self.contact_page.is_missing_field()
