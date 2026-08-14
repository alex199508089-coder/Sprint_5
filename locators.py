# locators.py
from selenium.webdriver.common.by import By

# ---------- Главная страница ----------
# Кнопка «Войти в аккаунт» на главной
BUTTON_LOGIN_MAIN = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")

# Кнопка «Личный кабинет» в шапке
BUTTON_PERSONAL_CABINET = (By.XPATH, "//a[contains(text(),'Личный кабинет')]")

# Логотип Stellar Burgers (кликабельный)
LOGO_STELLAR_BURGERS = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]//a")

# Вкладка «Булки» в конструкторе
TAB_BUNS = (By.XPATH, "//span[contains(text(),'Булки')]/parent::div")

# Вкладка «Соусы» в конструкторе
TAB_SAUCES = (By.XPATH, "//span[contains(text(),'Соусы')]/parent::div")

# Вкладка «Начинки» в конструкторе
TAB_FILLINGS = (By.XPATH, "//span[contains(text(),'Начинки')]/parent::div")

# Активный раздел конструктора (проверка класса)
ACTIVE_TAB = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]")

# ---------- Страница регистрации ----------
# Ссылка «Зарегистрироваться» (на странице входа)
LINK_REGISTER = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")

# Поле «Имя»
INPUT_NAME = (By.XPATH, ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']")

# Поле «Email»
INPUT_EMAIL = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")

# Поле «Пароль»
INPUT_PASSWORD = (By.XPATH,  ".//input[@type='password' and @name='Пароль']")

# Кнопка «Зарегистрироваться» (submit)
BUTTON_REGISTER_SUBMIT = (By.XPATH, ".//button[text()='Зарегистрироваться']")

# Сообщение об ошибке (некорректный пароль)
ERROR_INVALID_PASSWORD = (By.XPATH, ".//p[contains(@class, 'input__error')]")

# ---------- Страница входа ----------
# Поле Email
INPUT_EMAIL_LOGIN = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")

# Поле Пароль
INPUT_PASSWORD_LOGIN = (By.XPATH, ".//input[@type='password' and @name='Пароль']")

# Кнопка «Войти»
BUTTON_LOGIN_SUBMIT = (By.XPATH, "//button[contains(text(),'Войти')]")

# Ссылка «Восстановить пароль»
LINK_FORGOT_PASSWORD = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")

# ---------- Страница восстановления пароля ----------
# Ссылка «Войти» (в форме восстановления)
LINK_LOGIN_FROM_FORGOT = (By.XPATH, "//a[contains(text(),'Войти')]")

# ---------- Личный кабинет ----------
# Кнопка «Выйти»
BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(),'Выйти')]")

# Кнопка «Конструктор» в шапке (переход в конструктор)
BUTTON_CONSTRUCTOR = (By.XPATH, "//a[contains(text(),'Конструктор')]")

# Текст с email в личном кабинете (для проверки входа)
PROFILE_EMAIL = (By.XPATH, "//p[contains(@class,'Account_text')]")