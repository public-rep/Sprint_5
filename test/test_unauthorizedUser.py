
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


class UnauthorizedUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        if hasattr(self, "driver"):
            self.driver.quit()

    def test_unauthorized_user(self):
        driver = self.driver
        wait = self.wait
        driver.get("https://qa-desk.education-services.ru/")

        wait.until(EC.visibility_of_element_located(LOGIN_BUTTON)
)
        wait.until(EC.element_to_be_clickable(POST_AD_BUTTON)).click()

        error_unauthorized_user = wait.until(EC.visibility_of_element_located(ERRO_UNAUTHORIZED_USER))
        self.assertEqual(error_unauthorized_user.text,"Чтобы разместить объявление, авторизуйтесь")
