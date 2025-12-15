from asyncio import timeout
from cgitb import text
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging
import time


class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(__name__)

    def open(self, url):
        self.driver.get(url)
        self.logger.info(f"Открыта страница: {url}")

    def find_element(self, locator, timeout=None):
        """Найти элемент с ожиданием"""
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            self.logger.error(f"Элемент не найден: {locator}")
            return []

    def click_element(self, locator, timeout=None):
        """Кликнуть с ожиданием кликабельности"""
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            element = wait.until(EC.element_to_be_clickable(locator))
            element.click()
            self.logger.info(f"Кликнут элемент: {locator}")
        except TimeoutException:
            self.logger.error(f"Элемент не кликабелен: {locator}")
            raise

    def get_text(self, locator):
        """Получить текст элемента"""
        element = self.find_element(locator, timeout)
        return element.text

    def send_keys(self, locator, keys, timeout=None, clear=True):
        """Ввести текст в элемент"""
        element = self.find_element(locator, timeout)
        if clear:
            element.clear()
        element.send_keys(text)
        self.logger.info(f"Введен текст в элемент {locator}: {text}")

    def is_element_present(self, locator, timeout=None):
        """Проверить наличие элемента"""
        try:
            self.find_element(locator, timeout)
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def is_element_visible(self, locator, timeout=None):
        """Проверить видимость элемента"""
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_for_element_to_disappear(self, locator, timeout=None):
        """Ожидать исчезновения элемента"""
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def take_screenshot(self, name):
        """Сделать скриншот"""
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"screenshots/{name}_{timestamp}.png"
        self.driver.save_screenshot(filename)
        self.logger.info(f"Скриншот сохранен: {filename}")
        return filename