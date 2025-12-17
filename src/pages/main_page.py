import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):

    HEADER = (By.TAG_NAME, "h1")
    CARRIER_HEADER_HIGH = (By.TAG_NAME, "h1")
    WANT_TO_TRANSPORT_BTN_HIGH = (
        By.CSS_SELECTOR, "a[href*='/hochu-perevozit']"
    )

    @allure.step("Проверяем, что главная страница загрузилась")
    def is_page_loaded(self):
        return self.wait_visible(self.HEADER).is_displayed()

    @allure.step("Получаем текст заголовка главной страницы")
    def get_header_text(self):
        return self.wait_visible(self.HEADER).text

    @allure.step("Кликаем на кнопку в шапке 'Хочу перевозить'")
    def click_want_to_transport(self):
        self.click(self.WANT_TO_TRANSPORT_BTN_HIGH)

    @allure.step("Ждём, что отобразится другая страница после клика")
    def is_carrier_page_loaded(self):
        return self.wait_visible(self.CARRIER_HEADER_HIGH).is_displayed()