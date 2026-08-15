from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import *
from conftest import BASE_URL

class TestConstructor:

    def test_buns_section_active_after_click(self, driver):
        """Проверка активации раздела «Булки» после клика (с переключением с «Соусов»)."""
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TAB_SAUCES))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TAB_SAUCES)).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]//span[text()='Соусы']")
            )
        )

        # Теперь кликаем по «Булки» обычным способом
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TAB_BUNS)).click()

        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]//span[text()='Булки']")
            )
        )
        assert active_tab.is_displayed(), "Раздел «Булки» не активирован"

    def test_sauces_section_active_after_click(self, driver):
        """Проверка активации раздела «Соусы» после клика."""
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TAB_SAUCES))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TAB_SAUCES)).click()
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]//span[text()='Соусы']")
            )
        )
        assert active_tab.is_displayed(), "Раздел «Соусы» не активирован"

    def test_fillings_section_active_after_click(self, driver):
        """Проверка активации раздела «Начинки» после клика."""
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TAB_FILLINGS))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TAB_FILLINGS)).click()
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]//span[text()='Начинки']")
            )
        )
        assert active_tab.is_displayed(), "Раздел «Начинки» не активирован"