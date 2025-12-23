import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CalculateCostPage(BasePage):

    # Переключатель ГОРОД/МЕЖГОРОД
    CITY_ROUTE_BTN = (By.XPATH, "//button[span[text()='ГОРОД']]")
    INTERCITY_ROUTE_BTN = (By.XPATH, "//button[span[text()='МЕЖГОРОД']]")

    # Переключатель типов перевозки
    TYPE_RACE_BTN = (By.XPATH, "//button[span[text()='РЕЙС']]")
    TYPE_ROUND_BTN = (By.XPATH, "//button[span[text()='КРУГОРЕЙС']]")
    TYPE_DOGR_BTN = (By.XPATH, "//button[span[text()='ДОГРУЗ']]")
    TYPE_RACE_BACK_BTN = (By.XPATH, "//button[span[text()='РЕЙС + ОБРАТКА']]")

    # Поля ввода
    FROM_FIELD = (By.XPATH, "//p[normalize-space()='Город']/following::input[1]")
    TO_FIELD = (By.XPATH, "//p[normalize-space()='Куда']/following::input[1]")
    WEIGHT_FIELD = (By.CSS_SELECTOR, "input[placeholder='0'][inputmode='decimal']")
    PALLETS_FIELD = (By.CSS_SELECTOR, "input[placeholder='0'][inputmode='numeric']")
    POINTS_FIELD = (By.CSS_SELECTOR, "input[placeholder='0'][inputmode='numeric']")

    @staticmethod
    def CITY_SUGGESTION(city):
        return (
            By.XPATH, f"//p[contains(@class, 'hover:cursor-pointer') and contains(text(), '{city}')]"
        )


    # Кнопка рассчитать
    CALCULATE_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    # Заголовок страницы

    HEADER = (By.TAG_NAME, "h2")

    @allure.step("Проверяем, что страница калькулятора загрузилась")
    def is_page_loaded(self):
        element = self.wait_visible(self.HEADER)
        return element.is_displayed()


    # Действия

    @allure.step("Выбираем маршрут 'Город'")
    def select_city_route(self):
        self.click(self.CITY_ROUTE_BTN)

    @allure.step("Выбираем маршрут 'Межгород'")
    def select_intercity_route(self):
        self.click(self.INTERCITY_ROUTE_BTN)

    @allure.step("Выбираем тип перевозки 'Рейс'")
    def select_race(self):
        self.click(self.TYPE_RACE_BTN)

    @allure.step("Заполняем поле 'Город'")
    def set_from(self, city):
        field = self.wait_visible(self.FROM_FIELD)
        field.clear()
        field.send_keys(city)

        suggestion = self.wait_visible(self.CITY_SUGGESTION(city))
        suggestion.click()

    #@allure.step("Кликаем на введенный город в поле 'Откуда'")
    #def select_city_from_suggestion(self, city):
        #locator = (By.XPATH, f"//p[contains(text(), {city}]")
        #element = self.wait_visible(locator)
        #element.click()

    @allure.step("Заполняем поле 'Куда'")
    def set_to(self, city):
        field = self.wait_visible(self.TO_FIELD)
        field.clear()
        field.send_keys(city)

        suggestion = self.wait_visible(self.CITY_SUGGESTION(city))
        suggestion.click()

    def get_from_value(self):
        return self.wait_visible(self.FROM_FIELD).get_attribute("value")

    def get_to_value(self):
        return self.wait_visible(self.TO_FIELD).get_attribute("value")

    #@allure.step("Кликаем на введенный город в поле 'Куда'")
    #def select_city_to_suggestion(self, city):
        #locator = (By.XPATH, f"//p[contains(text(), {city}]")
        #element = self.wait_visible(locator)
        #element.click()

    @allure.step("Заполняем поле 'Вес, кг'")
    def send_weight(self, value):
        self.send_keys(self.WEIGHT_FIELD, value)

    @allure.step("Нажимаем на кнопку 'Рассчитать'")
    def submit(self):
        self.click(self.CALCULATE_BTN)
