
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from variables import *


@pytest.fixture
def driver():
        browser = webdriver.Chrome()
        yield browser
        browser.quit()   
def test_unauthorized_user(driver):
        wait = WebDriverWait(driver, 10)

        driver.get(BASE_URL)

        wait.until(EC.visibility_of_element_located(LOGIN_BUTTON))
        wait.until(EC.element_to_be_clickable(POST_AD_BUTTON)).click()

        error_unauthorized_user = wait.until(EC.visibility_of_element_located(ERRO_UNAUTHORIZED_USER))

        assert error_unauthorized_user.text.strip() == ("Чтобы разместить объявление, авторизуйтесь")