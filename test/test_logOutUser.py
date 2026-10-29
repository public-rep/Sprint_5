
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from register_user import *


def test_log_out_user(driver):
        wait = WebDriverWait(driver, 10)
        email, password = register_user(driver, wait)

        wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()

        user_name_invisible = wait.until(EC.invisibility_of_element_located(USER_NAME))
        post_ad_button = wait.until(EC.visibility_of_element_located(POST_AD_BUTTON))

        assert user_name_invisible
        assert post_ad_button.is_displayed()