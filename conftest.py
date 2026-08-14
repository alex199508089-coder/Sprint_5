# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://stellarburgers.education-services.ru/"

@pytest.fixture(scope="function")
def driver():
    """Фикстура создаёт и закрывает драйвер для каждого теста."""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()