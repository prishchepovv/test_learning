import allure


@allure.title("Главная страница открывается")
def test_main_page_is_loaded(main_page):
    assert main_page.is_page_loaded()

@allure.title("Текст заголовка на главной странице")
def test_main_page_is_header_text(main_page):
    expected_title = "СЕРВИС ПОИСКА ГРУЗОВ И ПЕРЕВОЗЧИКОВ ПО РОССИИ"
    actual_title = main_page.get_header_text()

    assert actual_title == expected_title, (
        f"Ожидали заголовок '{expected_title}', но получили '{actual_title}'"
    )

@allure.title("Клик по кнопке в шапке 'Хочу перевозить'")
def test_click_want_to_transport(main_page):
    carrier_page = main_page.click_want_to_transport()

    assert carrier_page.is_page_loaded(), (
        "Страница перевозчика не загрузилась после клика"
    )

@allure.title("Клик по кнопке в шапке 'Нужна доставка'")
def test_click_need_delivery(main_page):
    delivery_page = main_page.click_need_delivery()

    assert delivery_page.is_page_loaded(), (
        "Страница доставки не загрузилась после клика"
    )

@allure.title("Клик по кнопке в шапке 'Безопасная сделка'")
def test_click_safe_deal_page(main_page):
    safe_deal_page = main_page.click_safe_deal_page()

    assert safe_deal_page.is_page_loaded(), (
        "Страница безопасной сделки не загрузилась после клика"
    )

@allure.title("Клик по кнопке в шапке 'Рассчитать стоимость'")
def test_click_calculate_cots_page(main_page):
    calculate_cost_page = main_page.click_calculate_cost_page()

    assert calculate_cost_page.is_page_loaded(), (
        "Страница рассчета стоимости не загрузилась после клика"
    )