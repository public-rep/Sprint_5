
from selenium.webdriver.common.by import By


# FIELD
EMAIL_FIELD = (By.NAME, "email")
PASSWORD_FIELD = (By.NAME, "password")
CONFIRM_PASSWORD_FIELD = (By.NAME, "submitPassword") 
PRODUCT_NAME = (  By.XPATH, "/html/body/div/div/div[2]/div/form/div[2]/div[1]/div/div/input")
PRODUCT_DESCRIPTION = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/textarea")
COST = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[5]/div/div/input")


# BUTTON
LOGIN_BUTTON = ( By.XPATH, "//*[normalize-space()='Вход и регистрация']")
LOGOUT_BUTTON = (By.XPATH, "//*[normalize-space()='Выйти']")
ENTER_BUTTON = ( By.XPATH, "//form/div[3]/button[1]")
NO_ACCOUNT_BUTTON = ( By.XPATH, "/html/body/div/div/div[2]/div[5]/form/div[3]/button[2]")
CREATE_ACCOUNT_BUTTON = ( By.XPATH, "//button[normalize-space()='Создать аккаунт']")
LOGOUT_BUTTON = (By.XPATH, "//*[normalize-space()='Выйти']")
POST_AD_BUTTON = (By.XPATH, "//button[normalize-space(.)='Разместить объявление']")
CATEGORY= (By.XPATH, "/html/body/div/div/div[2]/div/form/div[2]/div[2]/div[1]/button")
CITY = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[3]/div[1]/button")
RADIO_BUTTON_CONDITION = (By.XPATH, "/html/body/div/div/div[2]/div/form/fieldset/div/div[2]/div")
SEND_PRODUCT = (By.XPATH, "/html/body/div/div/div[2]/div/form/button")
USER_PROFILE = (By.XPATH, "/html/body/div/div/div[1]/div/div[1]/button")



# element
USER_NAME = ( By.CSS_SELECTOR,".profileText")
IMAGE_USER = ( By.XPATH,"//button//*[name()='svg']")
EMAIL_ERROR_MESSAGE = (By.XPATH, "//*[text()='Ошибка']")
ERRO_UNAUTHORIZED_USER =(By.XPATH, "//*[text()='Чтобы разместить объявление, авторизуйтесь']") 
ELEMENT_BOOK=(By.XPATH, "//*[normalize-space()='Книги']")
ELEMENT_CITY=(By.XPATH, "//*[normalize-space()='Казань']")
ELEMENT_LOCATOR=(By.CSS_SELECTOR, "div.card")
CHECK_PRODUCK_NAME=(By.CSS_SELECTOR, ".about > h2:nth-child(1)")
CHECK_PRICE=(By.CSS_SELECTOR,"div.description div.price")
#FORM
COLLOR_PASSWORD_REPEAT_FORM = (By.XPATH, "/html/body/div/div/div[2]/div[5]/form/div[2]/div[3]/div/div")
COLLOR_EMAIL_FORM = ( By.XPATH, "/html/body/div/div/div[2]/div[5]/form/div[2]/div[1]/div/div")
COLLOR_PASSWORD_FORM = ( By.XPATH, "/html/body/div/div/div[2]/div[5]/form/div[2]/div[3]/div/div")
