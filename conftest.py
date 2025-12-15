import pytest
from requests import session
from selenium import webdriver
from appium import webdriver as appium_webdriver
import requests

# --- Фикстура для Web-тестирования (Selenium) ---
@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации и закрытия Selenium WebDriver."""
    print("\n--- Starting WebDriver ---")
    # Здесь можно добавлять логику для выбора браузера (Chrome, Firefox и тд)
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    print("\n--- Quitting WebDriver ---")
    driver.quit()

# --- Фикстура для Mobile-тестирования (Appium) ---
@pytest.fixture(scope="function")
def mobile_driver():
    """Фикстура для инициализации и закрытия Appium WebDriver."""
    print("\n--- Starting Appium Driver ---")
    desired_caps = {
        "platformName": "Android", # или "iOS"
        "deviceName": "emulator-5554", # Указать девайс
        # "app": "/path/to/your/app.apk" # Расскоментировать и указать путь к приложению!
    }
    driver = appium_webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    yield driver
    print("\n--- Quitting Appium Driver ---")
    driver.quit()

# --- Фикстура для API-тестирования (Requests) ---
@pytest.fixture(scope="session")
def api_session():
    """Фикстура для создания сессии requests для API-тестов."""
    print("\n--- Creating API session ---")
    session = requests.Session()
    session.headers.update({
    'Content-Type': 'application/json',
    'Accept': 'application/json'
})
    # Здесь можно добавить базовый URL, аутентификацию и тд
    # session.auth = ('user', 'pass')
    # session.base_url = 'https://api.example.com'
    yield session
    print("\n--- Closing API session ---")
    session.close()

    # Сохранение скриншота при падении теста
    @pytest.fixture(autouse=True)
    def take_screenshot_on_failure(request, driver):
        """Делает скриншот при падении теста"""
        yield
        if request.node.rep_call.failed:
        # Сохраняем скриншот
            screenshot_name = f"screenshot/{request.node.name}_fail.png"
            driver.save_screenshot(screenshot_name)
            print(f"Скриншот сохранен: {screenshot_name}")