import random
import string
from locators import *
from selenium.webdriver.support import expected_conditions as EC


PASSWORD = "Password123!"
BASE_URL = "https://qa-desk.education-services.ru/"


def generate_email(domain="domen.ru"):
    random_name = ''.join(
        random.choices(string.ascii_lowercase + string.digits, k=10)
    )
    return f"{random_name}@{domain}"


def register_user(driver, wait, email=None):
    driver.get(BASE_URL)

    wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()

    if email is None:
        email = generate_email()

    wait.until(EC.visibility_of_element_located(EMAIL_FIELD)).send_keys(email)
    wait.until(EC.visibility_of_element_located(PASSWORD_FIELD)).send_keys(PASSWORD)
    wait.until(EC.visibility_of_element_located(CONFIRM_PASSWORD_FIELD)).send_keys(PASSWORD)

    wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)).click()

    return email, PASSWORD