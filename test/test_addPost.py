import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from register_user import register_user


class TestAddPost(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        if hasattr(self, "driver"):
            self.driver.quit()

    def test_add_post(self):
        driver = self.driver
        wait = self.wait

        email, password = register_user(driver, wait)

        wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()
        time.sleep(0.5)

        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()
        time.sleep(0.5)

        wait.until(EC.visibility_of_element_located(EMAIL_FIELD)).send_keys(email)
        time.sleep(0.5)

        wait.until(EC.visibility_of_element_located(PASSWORD_FIELD)).send_keys(password)
        time.sleep(0.5)

        wait.until(EC.element_to_be_clickable(ENTER_BUTTON)).click()
        time.sleep(0.5)

        wait.until(EC.visibility_of_element_located(LOGOUT_BUTTON))


        wait.until(EC.element_to_be_clickable(POST_AD_BUTTON)).click()
        time.sleep(0.5)

        product_name = "Товар"
        description = "Описание"
        cost = "8800555"

        wait.until(EC.visibility_of_element_located(PRODUCT_NAME)).send_keys(product_name)
        time.sleep(0.5)

        wait.until(EC.visibility_of_element_located(PRODUCT_DESCRIPTION)).send_keys(description)
        time.sleep(0.5)

        wait.until(EC.visibility_of_element_located(COST)).send_keys(cost)
        time.sleep(0.5)

        wait.until(EC.element_to_be_clickable(CATEGORY)).click()
        time.sleep(0.5)

        wait.until( EC.element_to_be_clickable(ELEMENT_BOOK)).click()
        time.sleep(0.5)

        wait.until(EC.element_to_be_clickable(CITY)).click()
        time.sleep(0.5)

        wait.until(
        EC.element_to_be_clickable(ELEMENT_CITY)).click()
        time.sleep(0.5)

        wait.until(EC.element_to_be_clickable(RADIO_BUTTON_CONDITION)).click()
        time.sleep(0.5)

        wait.until(EC.element_to_be_clickable(SEND_PRODUCT)).click()
        time.sleep(0.5)

        wait.until(EC.element_to_be_clickable(USER_PROFILE)).click()


        card = wait.until( EC.visibility_of_element_located(ELEMENT_LOCATOR))


        title = card.find_element(*CHECK_PRODUCK_NAME)
        self.assertEqual(title.text.strip(), product_name)

        price = card.find_element(*CHECK_PRICE)
        actual_price = price.text.replace(" ", "").replace("\u00a0", "")
        self.assertIn(cost, actual_price)
