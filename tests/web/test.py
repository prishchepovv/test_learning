def test_main_page_is_loaded(main_page):
    """Проверка, что главная страница загрузилась"""
    assert main_page.is_page_loaded()

def test_main_page_is_header_text(main_page):
    """Проверка текста заголовка"""
    expected_title = "СЕРВИС ПОИСКА ГРУЗОВ И ПЕРЕВОЗЧИКОВ ПО РОССИИ"
    assert main_page.get_header_text() == expected_title

def test_clicl_want_to_transport(main_page):
    """Проверка клика на кнопку 'Хочу перевозить'"""
    main_page.click_want_to_transport()