import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from register_user import *


class TestLogOutUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        if hasattr(self, "driver"):
            self.driver.quit()
    
    def test_log_out_user(self):
        driver = self.driver
        wait = self.wait
        email, password = register_user(driver, wait)

        wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()
        self.assertTrue(wait.until(EC.invisibility_of_element_located(USER_NAME)))

        post_ad_button = wait.until(EC.visibility_of_element_located(POST_AD_BUTTON))
        self.assertTrue(post_ad_button.is_displayed())


