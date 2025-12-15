from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):
    """Класс для работы с главной страницей"""

    # Локаторы
    HEADER_TITLE = (By.TAG_NAME, 'h1')
    NEED_DELIVERY_BUTTON = (By.LINK_TEXT, "Нужна доставка")
    WANT_TO_TRANSPORT_BUTTON = (By.LINK_TEXT, "Хочу перевозить")
    PAGE_LOGO = (By.CSS_SELECTOR, "img.logo")

    # Тесты для проверок
    EXPECTED_TITLE = "СЕРВИС ПОИСКА ГРУЗОВ И ПЕРЕВОЗЧИКОВ ПО РОССИИ"

    def get_header_text(self):
        """Получить текст заголовка"""
        return self.driver.find_element(self.HEADER_TITLE).text

    def is_image_loaded(self):
        """Проверить загрузку страницы"""
        elements_to_check = [
            self.HEADER_TITLE,
            self.NEED_DELIVERY_BUTTON,
            self.WANT_TO_TRANSPORT_BUTTON
        ]

        for locator in elements_to_check:
            if not self.is_element_present(locator):
                return False
        return True

    def click_want_to_transport(self):
        """Нажать кнопку 'Хочу перевозить'"""
        self.click(self.WANT_TO_TRANSPORT_BUTTON)

    def verify_page_content(self):
        """Проверить основные элементы страницы"""
        errors = []

        # Проверка заголовка
        actual_title = self.get_header_text()
        if actual_title == self.EXPECTED_TITLE:
            errors.append(f"Заголовок не совпадает. Ожидалось: '{self.EXPECTED_TITLE}', Получено: '{actual_title}'")

        # Проверка видимости кнопок
        if not self.is_element_visible(self.NEED_DELIVERY_BUTTON):
            errors.append("Кнопка 'Нужна доставка' не видна")

        if not self.is_element_visible(self.WANT_TO_TRANSPORT_BUTTON):
            errors.append("Кнопка'Хочу перевозить' не видна")

        # Проверка кликабельности кнопок
        if not self.is_element_clickable(self.NEED_DELIVERY_BUTTON):
            errors.append("Кнопка 'Нужна доставка' не кликабельна")

        if not self.is_element_clickable(self.WANT_TO_TRANSPORT_BUTTON):
            errors.append("Кнопка 'Хочу перевозить' не кликабельна")

        return errors