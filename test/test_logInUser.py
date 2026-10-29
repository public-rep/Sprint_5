
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from register_user import *



def test_log_in_user(driver):
        wait = WebDriverWait(driver, 10)
        email, password = register_user(driver, wait)

        wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(EMAIL_FIELD)).send_keys(email)
        wait.until(EC.visibility_of_element_located(PASSWORD_FIELD)).send_keys(password)
        wait.until(EC.element_to_be_clickable(ENTER_BUTTON)).click()

        assert wait.until(EC.visibility_of_element_located(USER_NAME)).text.strip()  ==  "User."
        assert wait.until(EC.visibility_of_element_located(IMAGE_USER)).is_displayed()

        wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()
