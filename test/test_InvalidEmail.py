
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from register_user import *


class TestInvalidEmail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        if hasattr(self, "driver"):
            self.driver.quit()

    def test_invalid_email_shows_validation_error(self):
        driver = self.driver
        wait = self.wait
        email, password = register_user(driver, wait, email="uiui")

        error_message = wait.until(EC.visibility_of_element_located(EMAIL_ERROR_MESSAGE))
        element_collor_email_form = wait.until(EC.visibility_of_element_located(COLLOR_EMAIL_FORM))
        element_collor_password_form = wait.until(EC.visibility_of_element_located(COLLOR_PASSWORD_FORM))
        element_collor_password_repeat_form = wait.until(EC.visibility_of_element_located(COLLOR_PASSWORD_REPEAT_FORM))

        self.assertEqual(error_message.text.strip(), "Ошибка")
        self.assertEqual(element_collor_email_form.value_of_css_property("border-top-color"), "rgba(255, 105, 114, 1)")
        self.assertEqual(element_collor_password_form.value_of_css_property("border-top-color"), "rgba(255, 105, 114, 1)")
        self.assertEqual(element_collor_password_repeat_form.value_of_css_property("border-top-color"), "rgba(255, 105, 114, 1)")
