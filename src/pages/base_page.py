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

    def get_value(self, locator):
        return self.wait_visible(locator).get_attribute("value")

    def get_class(self, locator):
        return self.wait_visible(locator).get_attribute("class")

    def is_enable(self, locator):
        return self.wait_visible(locator).is_enabled()

    def send_keys(self, locator, value):
        element = wait_visible(self.driver, locator)
        element.clear()
        element.send_keys(value)

    def is_enabled(self, locator):
        return wait_visible(self.driver, locator).is_enabled()

