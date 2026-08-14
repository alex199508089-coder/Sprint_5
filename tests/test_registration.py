# tests/test_registration.py
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import generate_login, generate_password, generate_short_password
from conftest import BASE_URL

class TestRegistration:

    def test_successful_registration(self, driver):
        """Проверка успешной регистрации."""
        driver.get(BASE_URL)


        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_LOGIN_MAIN)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LINK_REGISTER)).click()


        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(BUTTON_REGISTER_SUBMIT))


        name = "Тестовый Пользователь"
        email = generate_login()
        password = generate_password()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_NAME)).send_keys(name)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_EMAIL)).send_keys(email)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_PASSWORD)).send_keys(password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_REGISTER_SUBMIT)).click()


        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url, "Не выполнен переход на страницу входа после регистрации"

    def test_registration_with_invalid_password_error(self, driver):
        """Проверка ошибки при некорректном пароле (менее 6 символов)."""
        driver.get(BASE_URL)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_LOGIN_MAIN)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LINK_REGISTER)).click()


        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(BUTTON_REGISTER_SUBMIT))


        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_NAME)).send_keys("Имя")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_EMAIL)).send_keys(generate_login())
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_PASSWORD)).send_keys(generate_short_password())
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_REGISTER_SUBMIT)).click()


        error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ERROR_INVALID_PASSWORD))
        assert error.is_displayed(), "Сообщение об ошибке не отображается"