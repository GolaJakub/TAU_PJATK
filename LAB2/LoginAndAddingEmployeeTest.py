import logging
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

navigate_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


class OrangeHrmTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
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

    def test_automate_login_and_adding_employee(self):
        self.logger.info("Otwieranie serwisu orangehrmlive.com")
        self.logger.info("Logowanie do serwisu")
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
        try:
            self.driver.find_element(By.CLASS_NAME, "orangehrm-dashboard-grid")
            self.logger.info("Poprawne logowanie do serwisu")
        except:
            self.logger.error("Niepoprawne logowanie do serwisu")

        self.logger.info("Test dodawania pracownika")

        # Klikniecie przycisku PIM
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()

        # Klikniecie przycisku Add
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()

        # Uzupelnienie danych w formularzu
        self.driver.find_element(By.NAME, 'firstName').send_keys("Test")
        self.driver.find_element(By.NAME, 'middleName').send_keys("Testowski")
        self.driver.find_element(By.NAME, 'lastName').send_keys("Testowy")

        # Klikniecie przycisku save
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()

        # Sprawdzenie nazwy pracownika
        if self.driver.find_element(By.XPATH,
                                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/h6').text.find(
            'Test Testowy'):
            self.logger.info("Poprawnie dodano pracownika")
        else:
            self.logger.error("Nie dodano pracownika")


if __name__ == '__main__':
    unittest.main()
