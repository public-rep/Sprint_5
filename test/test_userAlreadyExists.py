import test_registration
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from register_user import *

class TestUserAlreadyExists (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        if hasattr(self, "driver"):
            self.driver.quit()
    def test_user_already_exists(self):
        driver = self.driver
        wait = self.wait
        email, password = register_user(driver, wait)

        wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)) .click()

        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()

        wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(EMAIL_FIELD)).send_keys(email)

        wait.until(EC.visibility_of_element_located(PASSWORD_FIELD)).send_keys(password)

        wait.until(EC.visibility_of_element_located(CONFIRM_PASSWORD_FIELD)).send_keys(password)

        wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)).click()

        error_message = wait.until(EC.visibility_of_element_located(EMAIL_ERROR_MESSAGE))
        self.assertEqual(error_message.text.strip(), "Ошибка")

        element_collor_email_form = wait.until(EC.visibility_of_element_located(COLLOR_EMAIL_FORM))
        border_color = element_collor_email_form.value_of_css_property("border-top-color")
        self.assertEqual( border_color,"rgba(255, 105, 114, 1)")

        element_collor_password_form = wait.until(EC.visibility_of_element_located(COLLOR_PASSWORD_FORM))
        border_color = element_collor_password_form.value_of_css_property( "border-top-color")
        self.assertEqual(border_color,"rgba(255, 105, 114, 1)", f"Ожидалась красная рамка #ff6972, получено: {border_color}")

        element_collor_password_form = wait.until(EC.visibility_of_element_located(COLLOR_PASSWORD_REPEAT_FORM))
        border_color = element_collor_password_form.value_of_css_property( "border-top-color")
        self.assertEqual(border_color,"rgba(255, 105, 114, 1)")


        
    

        