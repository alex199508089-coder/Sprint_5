import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import generate_login, generate_password
from conftest import BASE_URL

class TestProfile:

    @pytest.fixture(autouse=True)
    def setup_user(self, driver):
        """Создаёт нового пользователя и выполняет вход."""
        driver.get(BASE_URL)

        # Регистрация
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_LOGIN_MAIN)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LINK_REGISTER)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(BUTTON_REGISTER_SUBMIT))

        self.email = generate_login()
        self.password = generate_password()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_NAME)).send_keys("Тестовый Пользователь")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_EMAIL)).send_keys(self.email)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_PASSWORD)).send_keys(self.password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_REGISTER_SUBMIT)).click()


        WebDriverWait(driver, 10).until(EC.url_contains("/login"))


        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_EMAIL_LOGIN)).send_keys(self.email)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_PASSWORD_LOGIN)).send_keys(self.password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_LOGIN_SUBMIT)).click()


        WebDriverWait(driver, 10).until(lambda d: "/login" not in d.current_url)

    def _go_to_profile(self, driver):
        """Переходит в личный кабинет по клику на «Личный кабинет»."""
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_PERSONAL_CABINET)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(BUTTON_LOGOUT))

    def test_go_to_personal_cabinet(self, driver):
        """Переход в личный кабинет по клику на «Личный кабинет»."""
        self._go_to_profile(driver)
        assert driver.find_element(*BUTTON_LOGOUT).is_displayed()

    def test_go_to_constructor_from_profile_by_constructor_button(self, driver):
        """Переход из личного кабинета в конструктор по клику на «Конструктор»."""
        self._go_to_profile(driver)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_CONSTRUCTOR)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TAB_BUNS))
        assert driver.find_element(*TAB_BUNS).is_displayed()

    def test_go_to_constructor_from_profile_by_logo(self, driver):
        """Переход из личного кабинета в конструктор по клику на логотип."""
        self._go_to_profile(driver)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGO_STELLAR_BURGERS)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TAB_BUNS))
        assert driver.find_element(*TAB_BUNS).is_displayed()

    def test_logout_from_profile(self, driver):
        """Выход из аккаунта по кнопке «Выход»."""
        self._go_to_profile(driver)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_LOGOUT)).click()

        WebDriverWait(driver, 10).until(lambda d: '/account' not in d.current_url)

        if '/login' in driver.current_url:

            assert WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(INPUT_EMAIL_LOGIN)
            ).is_displayed()
        else:

            assert WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(BUTTON_LOGIN_MAIN)
            ).is_displayed()
