import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import *
from data import generate_login, generate_password
from conftest import BASE_URL

class TestLogin:

    @pytest.fixture(autouse=True)
    def setup_user(self, driver):
        """Фикстура создаёт нового пользователя перед каждым тестом."""
        driver.get(BASE_URL)


        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_LOGIN_MAIN)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LINK_REGISTER)).click()

        # Ожидание загрузки формы
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(BUTTON_REGISTER_SUBMIT))


        self.email = generate_login()
        self.password = generate_password()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_NAME)).send_keys("Тестовый Пользователь")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_EMAIL)).send_keys(self.email)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_PASSWORD)).send_keys(self.password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_REGISTER_SUBMIT)).click()

        # Ожидание перехода на страницу входа (после успешной регистрации)
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))

    def _login_and_verify(self, driver):
        """Выполняет вход и проверяет переход в личный кабинет."""

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_EMAIL_LOGIN)).send_keys(self.email)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_PASSWORD_LOGIN)).send_keys(self.password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_LOGIN_SUBMIT)).click()

        # После входа переходим в личный кабинет (клик по «Личный кабинет»)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_PERSONAL_CABINET)).click()


        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(BUTTON_LOGOUT))
        assert driver.find_element(*BUTTON_LOGOUT).is_displayed()

    def test_login_from_main_page(self, driver):
        """Вход по кнопке «Войти в аккаунт» на главной."""
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_LOGIN_MAIN)).click()
        self._login_and_verify(driver)

    def test_login_from_personal_cabinet_button(self, driver):
        """Вход через кнопку «Личный кабинет»."""
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_PERSONAL_CABINET)).click()
        # Ожидаем, что окажемся на странице входа
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        self._login_and_verify(driver)

    def test_login_from_registration_form(self, driver):
        """Вход через кнопку в форме регистрации."""
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_LOGIN_MAIN)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LINK_REGISTER)).click()


        login_link = (By.XPATH, "//a[text()='Войти']")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(login_link)).click()
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        self._login_and_verify(driver)

    def test_login_from_password_recovery_form(self, driver):
        """Вход через кнопку в форме восстановления пароля."""
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_LOGIN_MAIN)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LINK_FORGOT_PASSWORD)).click()


        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LINK_LOGIN_FROM_FORGOT)).click()
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        self._login_and_verify(driver)