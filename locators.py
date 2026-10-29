
from selenium.webdriver.common.by import By


# FIELD
EMAIL_FIELD = (By.CSS_SELECTOR,"input[name='email']")
PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='password']")
CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='submitPassword']") 
PRODUCT_NAME = (  By.XPATH, "//input[@placeholder='Название']")
PRODUCT_DESCRIPTION = (By.XPATH, "//textarea[@placeholder='Описание товара']")
COST = (By.XPATH, "//input[@placeholder='Стоимость']")


# BUTTON
LOGIN_BUTTON = ( By.XPATH, "//*[normalize-space()='Вход и регистрация']")
LOGOUT_BUTTON = (By.XPATH, "//*[normalize-space()='Выйти']")
ENTER_BUTTON = ( By.XPATH, "//form//button[contains(@class,'buttonPrimary')]")
NO_ACCOUNT_BUTTON = ( By.XPATH, "//button[normalize-space()='Нет аккаунта']")
CREATE_ACCOUNT_BUTTON = ( By.XPATH, "//button[normalize-space()='Создать аккаунт']")
LOGOUT_BUTTON = (By.XPATH, "//*[normalize-space()='Выйти']")
POST_AD_BUTTON = (By.XPATH, "//button[normalize-space(.)='Разместить объявление']")
CATEGORY= (By.XPATH, "//input[@name='category']/following-sibling::button")
CITY = (By.XPATH, "//input[@name='city']/following-sibling::button")
RADIO_BUTTON_CONDITION = (By.XPATH,"//label[normalize-space()='Б/У']")
SEND_PRODUCT = (By.XPATH, "//button[.='Опубликовать']")
USER_PROFILE = (By.XPATH, "//div[contains(@class,'header_flexRow')]//button[contains(@class,'circleSmall')]")



# element
USER_NAME = ( By.CSS_SELECTOR,".profileText")
IMAGE_USER = ( By.XPATH,"//button//*[name()='svg']")
EMAIL_ERROR_MESSAGE = (By.XPATH, "//*[text()='Ошибка']")
ERRO_UNAUTHORIZED_USER =(By.XPATH, "//*[text()='Чтобы разместить объявление, авторизуйтесь']") 
ERRO_UNAUTHORIZED_USER_FORM = (By.XPATH, "//form[contains(@class, 'popUp_shell')]//h1")
ELEMENT_BOOK=(By.XPATH, "//*[normalize-space()='Книги']")
ELEMENT_CITY=(By.XPATH, "//*[normalize-space()='Казань']")
ELEMENT_LOCATOR=(By.CSS_SELECTOR, "div.card")
CHECK_PRODUCK_NAME=(By.CSS_SELECTOR, ".about > h2:nth-child(1)")
CHECK_PRICE=(By.CSS_SELECTOR,"div.description div.price")
#FORM
COLLOR_PASSWORD_REPEAT_FORM = (By.XPATH, "//div[contains(@class, 'input_inputError')]")
COLLOR_EMAIL_FORM = ( By.XPATH, "//div[contains(@class, 'input_inputError')]")
COLLOR_PASSWORD_FORM = ( By.XPATH, "//div[contains(@class, 'input_inputError')]")
