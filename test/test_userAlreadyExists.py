import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from register_user import *




def test_user_already_exists(driver):
        wait = WebDriverWait(driver, 10)
        email, password = register_user(driver, wait)

        wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(EMAIL_FIELD)).send_keys(email)
        wait.until(EC.visibility_of_element_located(PASSWORD_FIELD)).send_keys(password)
        wait.until(EC.visibility_of_element_located(CONFIRM_PASSWORD_FIELD)).send_keys(password)
        wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)).click()

   
        assert wait.until(EC.visibility_of_element_located(EMAIL_ERROR_MESSAGE)).text.strip() == "Ошибка"

        assert wait.until(EC.visibility_of_element_located(COLLOR_EMAIL_FORM)).value_of_css_property("border-top-color") == "rgba(255, 105, 114, 1)"

        assert  wait.until(EC.visibility_of_element_located(COLLOR_PASSWORD_FORM)).value_of_css_property("border-top-color") == "rgba(255, 105, 114, 1)"

        assert wait.until(EC.visibility_of_element_located(COLLOR_PASSWORD_REPEAT_FORM)).value_of_css_property( "border-top-color") == "rgba(255, 105, 114, 1)"