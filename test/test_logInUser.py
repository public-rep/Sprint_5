
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
def test_log_in_user(driver):
        wait = WebDriverWait(driver, 10)
        email, password = register_user(driver, wait)

        wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(EMAIL_FIELD)).send_keys(email)
        wait.until(EC.visibility_of_element_located(PASSWORD_FIELD)).send_keys(password)
        wait.until(EC.element_to_be_clickable(ENTER_BUTTON)).click()
        
        user_name = wait.until(EC.visibility_of_element_located(USER_NAME))
        image_icon_user = wait.until(EC.visibility_of_element_located(IMAGE_USER))

        assert user_name.text.strip()  ==  "User."
        assert image_icon_user.is_displayed()

        wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()
