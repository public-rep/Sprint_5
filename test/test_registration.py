
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from variables import *
from register_user import *


 
def test_registration(driver):
        wait = WebDriverWait(driver, 10)
        email, password = register_user(driver, wait)
  
        assert wait.until(EC.url_to_be(EXPECTED_URL))
        assert wait.until(EC.visibility_of_element_located(USER_NAME)).text.strip()  ==  "User."
        assert wait.until(EC.visibility_of_element_located(IMAGE_USER)).is_displayed()
