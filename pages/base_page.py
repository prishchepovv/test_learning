from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.qa_framework.config import DEFAULT_TIMEOUT
import logging
import time


class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)
        self.logger = logging.getLogger(self.__class__.__name__)

    def open(self, url):
        self.driver.get(url)
        self.logger.info(f"Открыта страница: {url}")

    def find_element(self, locator, timeout=DEFAULT_TIMEOUT):
        """Найти элемент с ожиданием"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click(self, locator, timeout=DEFAULT_TIMEOUT):
        """Кликнуть с ожиданием кликабельности"""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        self.logger.info(f"Кликнуть элемент: {locator}")

    def get_text(self, locator, timeout=DEFAULT_TIMEOUT):
        """Получить текст элемента"""
        return self.find_element(locator, timeout).text

    def type(self, locator, text, timeout=DEFAULT_TIMEOUT, clear=True):
        element = self.find_element(locator, timeout)
        if clear:
            element.clear()
        element.send_keys(text)
        self.logger.info(f"Type text into {locator}: {text}")

    def is_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exceptions:
            return False

    def wait_untill_disappear(self, locator, timeout=DEFAULT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        path = f"screenshot/{name}_{timestamp}.png"
        self.driver.save_screenshot(path)
        self.logger.info(f"Screenshot saved: {path}")
        return path