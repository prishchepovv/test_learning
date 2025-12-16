from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    """Главная страница"""

    # Локаторы
    HEADER_TITLE = (By.TAG_NAME, "h1")
    NEED_DELIVERY_BUTTON = (By.LINK_TEXT, "Нужна доставка")
    WANT_TO_TRANSPORT_BUTTON = (By.LINK_TEXT, "Хочу перевозить")
    PAGE_LOGO = (By.CSS_SELECTOR, "img.logo")

    def get_header_text(self):
        return self.get_text(self.HEADER_TITLE)

    def is_need_delivery_button_visible(self):
        return self.is_visible(self.NEED_DELIVERY_BUTTON)

    def is_want_to_transport_button_visible(self):
        return self.is_visible(self.WANT_TO_TRANSPORT_BUTTON)

    def click_need_delivery(self):
        self.click(self.NEED_DELIVERY_BUTTON)

    def click_want_to_transport(self):
        self.click(self.WANT_TO_TRANSPORT_BUTTON)

    def is_page_loaded(self):
        return all([
            self.is_visible(self.HEADER_TITLE),
            self.is_visible(self.NEED_DELIVERY_BUTTON),
            self.is_visible(self.WANT_TO_TRANSPORT_BUTTON),
        ])