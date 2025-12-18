import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CalculateCostPage(BasePage):
    HEADER = (By.TAG_NAME, "h1")

    @allure.step("Проверяем, что страница калькулятора загрузилась")
    def is_page_loaded(self):
        return self.wait_visible(self.HEADER).is_displayed()
