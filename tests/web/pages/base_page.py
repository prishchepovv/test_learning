from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import TimeoutException, NoSuchElementException
#import time
#import logging


class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)
        self.logger.info(f"Открыта страница: {url}")

    def find_element(self, locator):
        """Найти элемент с ожиданием"""
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def click_element(self, locator):
        """Кликнуть с ожиданием кликабельности"""
        self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def get_text(self, locator):
        """Получить текст элемента"""
        return self.find_element(locator).text