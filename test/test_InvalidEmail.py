import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from register_user import *


def test_invalid_email_shows_validation_error(driver):
    wait = WebDriverWait(driver, 10)
    email, password = register_user(driver, wait, email="uiui")

    assert wait.until(EC.visibility_of_element_located(EMAIL_ERROR_MESSAGE)).text.strip() == "Ошибка"

    assert wait.until(EC.visibility_of_element_located(COLLOR_EMAIL_FORM)).value_of_css_property( "border-top-color") == "rgba(255, 105, 114, 1)"

    assert wait.until(EC.visibility_of_element_located(COLLOR_PASSWORD_FORM)).value_of_css_property("border-top-color") == "rgba(255, 105, 114, 1)"

    assert wait.until(EC.visibility_of_element_located(COLLOR_PASSWORD_REPEAT_FORM)).value_of_css_property( "border-top-color") == "rgba(255, 105, 114, 1)"
