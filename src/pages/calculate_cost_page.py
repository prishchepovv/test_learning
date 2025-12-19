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
    FROM_FIELD = (By.CSS_SELECTOR, "input[placeholder='Город']")
    TO_FIELD = (By.CSS_SELECTOR, "input[placeholder='Куда']")
    WEIGHT_FIELD = (By.CSS_SELECTOR, "input[placeholder='0'][inputmode='decimal']")
    PALLETS_FIELD = (by.CSS_SELECTOR, "input[placeholder='0'][inputmode='numeric']")
    POINTS_FIELD = (By.CSS_SELECTOR, "input[placeholder='0'][inputmode='numeric']")

    # Кнопка рассчитать
    CALCULATE_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    # Заголовок страницы

    HEADER = (By.TAG_NAME, "h1")

    @allure.step("Проверяем, что страница калькулятора загрузилась")
    def is_page_loaded(self):
        return self.wait_visible(self.HEADER).is_displayed()


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

    @allure.step("Заполняем поле 'Откуда'")
    def set_from(self):
        self.send_keys(self.FROM_FIELD, value)

    @allure.step("Заполняем поле 'Куда'")
    def set_to(self):
        self.send_keys(self.TO_FIELD, value)

    @allure.step("Заполняем поле 'Вес, кг'")
    def send_weight(self, value):
        self.send_keys(self.WEIGHT_FIELD, value)

    @allure.step("Нажимаем на кнопку 'Рассчитать'")
    def submit(self):
        self.click(self.CALCULATE_BTN)
