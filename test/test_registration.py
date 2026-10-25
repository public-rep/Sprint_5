
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from variables import *
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
        
       # 
        wait.until(EC.url_to_be(EXPECTED_URL))
        
        user_name = wait.until(EC.visibility_of_element_located(USER_NAME))
        image_icon_user = wait.until(EC.visibility_of_element_located(IMAGE_USER))

        self.assertEqual(driver.current_url, EXPECTED_URL)
        self.assertEqual(user_name.text, "User.")
        self.assertTrue(image_icon_user.is_displayed())

        wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()
