import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from register_user import *


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_invalid_email_shows_validation_error(driver):
    wait = WebDriverWait(driver, 10)
    email, password = register_user(driver, wait, email="uiui")

    error_message = wait.until(EC.visibility_of_element_located(EMAIL_ERROR_MESSAGE))
    element_collor_email_form = wait.until(EC.visibility_of_element_located(COLLOR_EMAIL_FORM))
    element_collor_password_form = wait.until(EC.visibility_of_element_located(COLLOR_PASSWORD_FORM))
    element_collor_password_repeat_form = wait.until(EC.visibility_of_element_located(COLLOR_PASSWORD_REPEAT_FORM))

    assert error_message.text.strip() == "Ошибка"

    assert element_collor_email_form.value_of_css_property( "border-top-color") == "rgba(255, 105, 114, 1)"

    assert element_collor_password_form.value_of_css_property("border-top-color") == "rgba(255, 105, 114, 1)"

    assert element_collor_password_repeat_form.value_of_css_property( "border-top-color") == "rgba(255, 105, 114, 1)"
