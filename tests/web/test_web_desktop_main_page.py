import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.web
def test_gruzapp_main_page(driver):
    """Проверяет, что заголовок страницы Грузапп корректен."""

    # Открываем страницу
    driver.get("https://gruz.app/")

    # Ждем загрузки страницы
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "loading-spinner"))
    )

    # Гибкая проверка title (не точный текст, а ключевые слова)
    title=driver.title.lower()
    print(f"Фактический title: '{driver.title}'")

    # Проверяем наличие ключевых слов в любом порядке
    keyword = ["груз", "перевоз", "росси", "сервис", "поиск"]
    found_keywords = [kw for kw in keyword if kw in title]

    assert len(found_keywords) >= 2, (
        f"В title '{driver.title}' должно быть хотя бы 2 ключевых слова из {keyword}."
        f"Найдены: {found_keywords}"
    )
