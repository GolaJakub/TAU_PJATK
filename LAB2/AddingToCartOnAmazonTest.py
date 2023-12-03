import logging
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

navigate_url = "https://www.amazon.pl/"


class AmazonTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.get(navigate_url)
        self.driver.implicitly_wait(5)
        self.logger = logging.getLogger('selenium')
        self.logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def tearDown(self):
        self.driver.quit()

    def test_amazon_adding_to_cart(self):
        self.logger.info("Otwieranie serwisu amazon.pl")

        # Potwierdzenie cookies
        cookies = self.driver.find_element(By.ID, 'sp-cc-accept')
        if cookies:
            cookies.click()

        # Wpisanie w pole wyszukaj frazy Iphone 13
        self.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys("Iphone 13")

        # Klikniecie przycisku lupki
        self.driver.find_element(By.ID, 'nav-search-submit-button').click()

        # Klikniecie w produkt
        self.driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/span/div/div/div[2]/div[2]/h2/a/span').click()

        # Klikniecie w przycisk dodaj do koszyka
        self.driver.find_element(By.ID, 'add-to-cart-button').click()

        # Weryfikacja czy koszyk zawiera 1 produkt
        if '1' == self.driver.find_element(By.ID, 'nav-cart-count').text:
            self.logger.info("Poprawnie dodano do koszyka")
        else:
            self.logger.error("Koszyk nie zawiera Iphone 13")

if __name__ == '__main__':
    unittest.main()
