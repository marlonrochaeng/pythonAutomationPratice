import pytest
from pages.home_page import HomePage
from pages.result_page import ResultPage
import unittest
import time
from ddt import data, ddt, unpack
from utils.read_data import getCsvData


@pytest.mark.usefixtures("BrowserSetUp")
@ddt
class CheckCart(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def ClassSetup(self, BrowserSetUp):
        self.home_page = HomePage(self.driver)
        self.result_page = ResultPage(self.driver)
        self.home_page.go_to_test_url()

        yield

        self.driver.quit()

    @data(*getCsvData('data/search_product.csv'))
    @unpack
    def test_search_product(self, product):              
        self.home_page.search_product(product)
        self.result_page.add_to_cart(product)
        self.result_page.go_to_checkout()

        assert self.result_page.is_product_displayed_in_cart(product)
        