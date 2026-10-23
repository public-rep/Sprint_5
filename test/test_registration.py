import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from register_user import *


class TestRegistration(unittest.TestCase):

    def setUp(self):
        
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        if hasattr(self, "driver"):
            self.driver.quit()
            
    
    def test_registration(self):
        driver = self.driver
        wait = self.wait
        email, password = register_user(driver, wait)
        
        expected_url = ("https://qa-desk.education-services.ru/regiatration")
        wait.until(EC.url_to_be(expected_url))
        self.assertEqual(
            driver.current_url,
            expected_url)

        user_name = wait.until(EC.visibility_of_element_located(USER_NAME))
        self.assertEqual(
            user_name.text,
            "User.")

        image_icon_user = wait.until(EC.visibility_of_element_located(IMAGE_USER))
        self.assertTrue(image_icon_user.is_displayed())

        user_logout = wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()
    