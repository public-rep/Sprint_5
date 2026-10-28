
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from variables import *
from register_user import *


@pytest.fixture
def driver():
        browser = webdriver.Chrome()
        yield browser
        browser.quit()    
def test_registration(driver):
        wait = WebDriverWait(driver, 10)
        email, password = register_user(driver, wait)
        
        wait.until(EC.url_to_be(EXPECTED_URL))
        
        user_name = wait.until(EC.visibility_of_element_located(USER_NAME))
        image_icon_user = wait.until(EC.visibility_of_element_located(IMAGE_USER))

       
        assert EXPECTED_URL == EXPECTED_URL
        assert user_name.text.strip()  ==  "User."
        assert image_icon_user.is_displayed()

        wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()
