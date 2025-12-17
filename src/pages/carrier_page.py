import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CarrierPage(BasePage):
    HEADER = (By.TAG_NAME, "h1")

    @allure.step("Проверяем, что страница перевозчика загружена")
    def is_page_loaded(self):
        return self.wait_visible(self.HEADER).is_displayed()