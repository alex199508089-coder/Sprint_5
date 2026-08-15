# locators.py
from selenium.webdriver.common.by import By

# ---------- Главная страница ----------
BUTTON_LOGIN_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
BUTTON_PERSONAL_CABINET = (By.XPATH, "//a[contains(@href, 'account')]")
LOGO_STELLAR_BURGERS = (By.XPATH, "//a[@href='/']")
BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")

TAB_BUNS = (By.XPATH, "//span[text()='Булки']/parent::*")
TAB_SAUCES = (By.XPATH, "//span[text()='Соусы']/parent::*")
TAB_FILLINGS = (By.XPATH, "//span[text()='Начинки']/parent::*")
ACTIVE_TAB = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]")

# ---------- Страница регистрации ----------
LINK_REGISTER = (By.XPATH, "//a[text()='Зарегистрироваться']")
INPUT_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
INPUT_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
INPUT_PASSWORD = (By.XPATH, "//input[@type='password']")
BUTTON_REGISTER_SUBMIT = (By.XPATH, "//button[text()='Зарегистрироваться']")
ERROR_INVALID_PASSWORD = (By.XPATH, "//p[contains(@class,'input__error')]")

# ---------- Страница входа ----------
INPUT_EMAIL_LOGIN = (By.XPATH, "//label[text()='Email']/following-sibling::input")
INPUT_PASSWORD_LOGIN = (By.XPATH, "//input[@type='password']")
BUTTON_LOGIN_SUBMIT = (By.XPATH, "//button[text()='Войти']")
LINK_FORGOT_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")

# ---------- Страница восстановления пароля ----------
LINK_LOGIN_FROM_FORGOT = (By.XPATH, "//a[text()='Войти']")

# ---------- Личный кабинет ----------
BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")
PROFILE_EMAIL = (By.XPATH, "//p[contains(@class,'Account_text')]")