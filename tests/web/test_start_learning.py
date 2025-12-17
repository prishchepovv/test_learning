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