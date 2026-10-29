
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from register_user import register_user



def test_add_post(driver):
    wait = WebDriverWait(driver, 10)
    email, password = register_user(driver, wait)

    wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()

    wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()

    wait.until(EC.visibility_of_element_located(EMAIL_FIELD)).send_keys(email)

    wait.until(EC.visibility_of_element_located(PASSWORD_FIELD)).send_keys(password)

    wait.until(EC.element_to_be_clickable(ENTER_BUTTON)).click()

    wait.until(EC.visibility_of_element_located(LOGOUT_BUTTON))

    wait.until(EC.element_to_be_clickable(POST_AD_BUTTON)).click()

    product_name = "Товар"
    description = "Описание"
    cost = "8800555"

    wait.until( EC.visibility_of_element_located(PRODUCT_NAME)).send_keys(product_name)

    wait.until( EC.visibility_of_element_located(PRODUCT_DESCRIPTION)).send_keys(description)

    wait.until( EC.visibility_of_element_located(COST)).send_keys(cost)

    wait.until(EC.element_to_be_clickable(CATEGORY)).click()

    wait.until(EC.element_to_be_clickable(ELEMENT_BOOK)).click()

    wait.until(EC.element_to_be_clickable(CITY)).click()
    
    wait.until(EC.element_to_be_clickable(ELEMENT_CITY)).click()

    wait.until( EC.element_to_be_clickable(RADIO_BUTTON_CONDITION)).click()

    wait.until(EC.element_to_be_clickable(SEND_PRODUCT)).click()

    wait.until(EC.invisibility_of_element_located(SEND_PRODUCT))

    wait.until(EC.element_to_be_clickable(USER_PROFILE)).click()

    card = wait.until( EC.visibility_of_element_located(ELEMENT_LOCATOR) )

    title = card.find_element(*CHECK_PRODUCK_NAME)
    actual_price = card.find_element(*CHECK_PRICE).text.replace(" ", "").replace("\u00a0", "")

    assert title.text.strip() == product_name
    assert cost in actual_price
