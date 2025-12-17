import allure
from qa_framework.waits import wait_visible, wait_clickable

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    def open(self, url):
        self.driver.get(url)

    @allure.step("Ждём, что элемент станет видимым: {locator}")
    def wait_visible(self, locator):
        return wait_visible(self.driver, locator)

    @allure.step("Кликаем по элементу: {locator}")
    def click(self, locator):
        element = wait_clickable(self.driver, locator)
        element.click()