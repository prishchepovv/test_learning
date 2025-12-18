import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.carrier_page import CarrierPage
from pages.delivery_page import DeliveryPage
from pages.safe_deal_page import SafeDealPage
from pages.calculate_cost_page import CalculateCostPage

class MainPage(BasePage):

    HEADER = (By.TAG_NAME, "h1")
    WANT_TO_TRANSPORT_BTN_HIGH = (
        By.CSS_SELECTOR, "a[href*='/hochu-perevozit']"
    )
    NEED_DELIVERY_BTN_HIGH = (
        By.CSS_SELECTOR, "a[href*='/nujna-dostavka']"
    )
    SAFE_DEAL_BTN_HIGH = (
        By.CSS_SELECTOR, "a[href*='/bezopasnaya-sdelka']"
    )
    CALCULATE_COST_BTN_HIGH = (
        By.CSS_SELECTOR, "a[href*='/nujna-dostavka?type=calculate'].xl\\:flex"
    )

    @allure.step("Проверяем, что главная страница загрузилась")
    def is_page_loaded(self):
        return self.wait_visible(self.HEADER).is_displayed()

    @allure.step("Получаем текст заголовка главной страницы")
    def get_header_text(self):
        return self.wait_visible(self.HEADER).text

    @allure.step("Кликаем на кнопку в шапке 'Хочу перевозить'")
    def click_want_to_transport(self) -> CarrierPage:
        self.click(self.WANT_TO_TRANSPORT_BTN_HIGH)
        return CarrierPage(self.driver)

    @allure.step("Ждём, что отобразится другая страница после клика")
    def is_carrier_page_loaded(self):
        return self.wait_visible(self.CARRIER_HEADER_HIGH).is_displayed()

    @allure.step("Кликаем на кнопку в шапке 'Нужна доставка'")
    def click_need_delivery(self) -> DeliveryPage:
        self.click(self.NEED_DELIVERY_BTN_HIGH)
        return DeliveryPage(self.driver)

    @allure.step("Ждём, что отобразится другая страница после клика")
    def is_delivery_page_loaded(self):
        return self.wait_visible(self.DELIVERY_HEADER_HIGH).is_displayed()

    @allure.step("Кликаем на кнопку в шапке 'Безопасная сделка'")
    def click_safe_deal_page(self) -> SafeDealPage:
        self.click(self.SAFE_DEAL_BTN_HIGH)
        return SafeDealPage(self.driver)

    @allure.step("Ждём, что отобразится другая страница после клика")
    def is_safe_deal_page_loaded(self):
        return self.wait_visible(self.SAFE_DEAL_HEADER_HIGH).is_displayed()

    @allure.step("Кликаем на кнопку в шапке 'Рассчитать стоимость'")
    def click_calculate_cost_page(self) -> CalculateCostPage:
        self.click(self.CALCULATE_COST_BTN_HIGH)
        return CalculateCostPage(self.driver)

    @allure.step("Ждём, что отобразится другая страница после клика")
    def is_calculate_cost_page_loaded(self):
        return self.wait_visible(self.CALCULATE_COST_HEADER_HIGH).is_displayed()