import allure

@allure.title("Страница расчёта стоимости открывается")
def test_calculate_cost_page_is_loaded(main_page):
    page = main_page.click_calculate_cost_page()
    assert page.is_page_loaded(), "Страница расчета стоимости не загрузилась"

@allure.title("Можно выбрать маршрут ГОРОД")
def test_select_city_route(main_page):
    page = main_page.click_calculate_cost_page()
    page.select_city_route()
    # Проверка: кнопка должна стать активной
    assert "bg-app-red" in page.get_class(page.CITY_ROUTE_BTN), \
        "Кнопка 'ГОРОД' не стала активной"

@allure.title("Можно заполнить поля 'Откуда' и 'Куда'")
def test_fill_from_to_fields(main_page):
    page = main_page.click_calculate_cost_page()
    page.select_intercity_route()
    page.set_from("Москва")
    page.set_to("Санкт-Петербург")

    assert page.get_from_value() == "г Москва"
    assert page.get_to_value() == "г Санкт-Петербург"

@allure.title("Кнопка 'Рассчитать' активируется при заполнении формы")
def test_calculate_button_becomes_enabled(main_page):
    page = main_page.click_calculate_cost_page()
    page.select_intercity_route()
    page.set_from("Казань")
    page.set_to("Сочи")
    page.send_weight('1000')
    page.send_pallets('10')
    page.points_field('2')

    assert page.is_enabled(page.CALCULATE_BTN), \
    "Кнопка 'Рассчитать' не активировалась"

@allure.title("Можно выполнить расчет стоимости")
def test_do_calculate(main_page):
    page = main_page.click_calculate_cost_page()
    page.select_intercity_route()
    page.set_from("Новосибирск")
    page.set_to("Омск")
    page.send_weight('1000')
    page.send_pallets('10')
    page.points_field('2')
    page.submit()
    assert True